# dHTC User Documentation

This repository holds the documentation for the PATh Facility and OSGConnect.

## Guides

- [Repository Layout](#repository-layout)
- [Editing Documentation](#editing-documentation)
  - [Creating the document](#creating-the-document)
  - [Adding it to the Navigation](#adding-it-to-the-navigation)
  - [Adding Images](#adding-images)
  - [Adding Videos](#adding-videos)
  - [Linking Documentation](#linking-documentation)
  - [Creating Styled Code Blocks](#creating-styled-code-blocks)
  - [Adding a Tutorial](#adding-a-tutorial)
  - [Documentation Style Guide](#documentation-style-guide)
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


### Linking Documentation

#### Other Portal Documentation 

All links to other portal documentation should be a relative link ( prepended with ../ ). 

For instance, starting on the OSG User School Page:

[https://portal.osg-htc.org/documentation/support_and_training/training/osg-user-school/](https://portal.osg-htc.org/documentation/support_and_training/training/osg-user-school/) 

To link to a page in the same directory you would use:

[../previous-training-events/](https://portal.osg-htc.org/documentation/support_and_training/training/osg-user-school/../previous-training-events/)

To link to a document in another directory farther up the tree you can use:

[../../../software_examples/python/tutorial-wordfreq/](https://portal.osg-htc.org/documentation/support_and_training/training/osg-user-school/../../../software_examples/python/tutorial-wordfreq/)

#### Tutorials

Use the full documentation path, this way the tutorial will still have valid links if
used as a standalone later on. 

For instance to link to Office Hours from a tutorial use:

[https://portal.osg-htc.org/documentation/support_and_training/support/getting-help-from-RCFs/](https://portal.osg-htc.org/documentation/support_and_training/support/getting-help-from-RCFs/)

### Creating Styled Code Blocks

There are three options for styled code blocks: terminal (term), submit file (sub), file (file).

To use these styles you have to use html, view the example below to convert a markdown block to styled html. 

```markdown
	requirements = (OSGVO_OS_STRING == "RHEL 7")
```

```html
<pre class="file"><code>requirements = (OSGVO_OS_STRING == "RHEL 7")</code></pre>
```

**Note**: Tabs and Newlines are preserved, if you don't want them don't include them in the html block

```markdown
	./configure
	make
	make install
```

```html
<pre class="file"><code>./configure
make
make install</code></pre>
```

### Adding a Tutorial 

To add a tutorial you need to do two things:

#### 1. Add the appropriate frontmatter so the the README is linked correctly 

This is accomplished by going into the tutorial repository and adjusting the README there. 

If you do this step second run the update submodule action to pull in the new changes. 

[How to adjust the README](#creating-the-document)

#### 2. Add the tutorial as a submodule in the tutorial directory

When running the script below confirm that that submodule gets cloned into the folder that you identify. 
If the repo you are hoping to add does not show up please reach out to Cannon. 

```
# From repo root
# Replace <git-url> and <tutorial-name> before running
git submodule add <https://github-url.git> ./documentation/tutorials/<tutorial-name>
```

#### 3. Add the document to the websites navigation 

Read more [above](#adding-it-to-the-navigation)

### Documentation Style Guide

#### One top level header per page

Use only one h1 ( # value ) to indicate the title. All other header elements should be >= h2 ( ##... value ).

**Good**
```
# Title

## Subtitle
```

**Bad**
```
# Title

# Subtitle
```


## Previewing your Work

You can develop the documentation locally by running the below line at the root of this directory. As you alter files they 
will change in the website so there is no need to rebuild for each change.

Use the links to go to the served website, the console will say to go to port 8000 but to prevent clashing you should use
ports 8010 and 8011 as specified below. 


**OSG**
```shell
docker run -it -p 8010:8010 -v ${PWD}:/docs/user-documentation hub.opensciencegrid.org/opensciencegrid/osg-portal-documentation:latest
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
After the action has completed you should create a PR on branch [update-submodules-reserved](https://github.com/osg-htc/user-documentation/compare/main...update-submodules-reserved) as it now the main branch with its submodules updated.

The steps to update the tutorial submodules are:

1. Click on the "Actions" tab in the navigation bar at the top of the repository.
2. Click on "Update Submodules" in the left-hand navigation sidebar.
3. In the blue banner is a "Run workflow" dropdown button. Click the dropdown and then click "Run Workflow" (make sure the action is run on the main branch).
4. After action has completed, compare `update-submodules-reserved` branch against `main` ([link](https://github.com/osg-htc/user-documentation/compare/main...update-submodules-reserved)), where you should see the changes you made to the tutorial(s).
5. Click on the "Create Pull Request" button to create the pull request.
6. Merge the pull request. DO NOT DELETE `update-submodules-reserved` branch!!
