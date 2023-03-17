# dHTC User Documentation

This repository holds the documentation for the PATh Facility and OSGConnect.

## Guides

- [Repository Layout](#repository-layout)
- [Editing Documentation](#editing-documentation)
  - [Creating the document](#creating-the-document)
  - [Adding it to the Navigation](#adding-it-to-the-navigation)
  - [Adding Images](#adding-images)
  - [Adding Videos](#adding-videos)
- [Previewing Documentation](#previewing-documentation)
- [Adding Documentation](#adding-documentation)
- [Updating Submodules](#updating-submodules)

## Repository Layout

### ./data

This folder is what will be read by the MKDOCS website to create the documentation page. 

In the ```./data/configs``` folder you will find the navigation for the websites. This file will have to be 
edited whenever documentation is added or removed. 

In the ```./data/docs/``` is the pre-processed documentation. The documentation here is nested according
to the path in each documents frontmatter. **You should not edit any files in this folder**

### ./documentation

This is where you will update existing documentation. The documentation is organized logically, but 
remember that you can change that organization on specific sites ( PATH vs. OSPool ) by using
the frontmatter. 

## Editing Documentation 

To edit documentation navigate to the page you want to edit in the ```./documentation``` folder and edit it accordingly. 

When you are content you can make a PR and on merge your changes will be deployed to the documentation website. 

## Adding Documentation

### Creating the document

To add documentation, you should add a new file to the ```./documentation``` folder. 

All documentation in this repo should have frontmatter at the top to declare where you would like that document to live on 
its respective site. You can/should use the template below. Either can be omitted to have it not published to the site. 

```yaml
---
ospool:
  path: <location where this file should be served from in osgconnect>/filename.md
path:
  path: <location where this file should be served from in the path portal>/filename.md
---
```

**Note:** The path declared in the frontmatter is where this documentation will be available on its respective site. 

To keep things organized you should choose a path that aligns with documentation in its grouping. 

For example the following would be available at portal.osg-htc.org/path0/path1/filename.md and portal.path-cc.io/path2/filename.md.

```yaml
---
ospool:
  path: path0/path1/filename.md
path:
  path: path2/filename.md
---
```

### Adding it to the Navigation

To add documentation to the navigation you will need to update the appropriate navigation metadata in the ```./data/configs``` folder.

You should follow these rules when adding your document:
  - Use the same path that you referenced in the document frontmatter
  - Make your document triply nested
    - Should be nav -> category -> sub-category -> document
    
**Example**

```yaml
nav:
  - Overview:
    - Welcome And Account Setup:
      - "Computation on the Open Science Pool ": overview/account_setup/is-it-for-you.md
```

### Adding Images

All images should be placed in ```./docs/assets```, this is because without frontmatter to know where to place the image
it will not be added to the websites documentation. 

Because of this all of the images should be added to the MD using the following markdown. 

```![](../../assets/<your-image-path>)```

For instance if you wanted to use the OSG_logo it would be:

```![](../../assets/OSG_Logo.png)```

**Note:** This is only valid if the documentation is triply nested. If this pattern is deviated from the solution will
vary. 


### Adding videos

[Video Demo](https://youtu.be/3xHFCpglNxA)

- Go to the Youtube page and click share under the video player
- Click embed and enable privacy-enhanced mode 
- Copy and paste the html where you want the video to be
- Change the width value to 100% so it spans the document viewport


## Previewing your Work

You can develop the documentation locally by running the below line at the root of this directory. As you alter files they 
will change in the website so there is no need to rebuild for each change.

Use the links to go to the served website, the console will say to go to port 8000 but to prevent clashing you should use
ports 8010 and 8011 as specified below. 


**OSG**
```shell
docker run -it -p 8010:8000 -v ${PWD}:/docs/user-documentation hub.opensciencegrid.org/opensciencegrid/osg-portal-documentation:latest
```

[localhost:8010](http://0.0.0.0:8010/documentation/)

**PATh**
```shell
docker run -it -p 8011:8011 -v ${PWD}:/docs/user-documentation hub.opensciencegrid.org/opensciencegrid/path-portal-documentation:latest
```

[localhost:8011](http://0.0.0.0:8011/documentation/)





## Updating Submodules

To update the tutorial submodules after pushing a change to them you should run the 
[Update Submodules Action](https://github.com/osg-htc/user-documentation/actions/workflows/update-submodules.yml).

The action should be run on the main branch. 

After the action has completed you should create a PR on branch [update-submodules-reserved](https://github.com/osg-htc/user-documentation/compare/main...update-submodules-reserved) as it now the main branch with its submodules updated.

