# dHTC User Documentation

This repository holds the documentation for the PATh Facility and OSGConnect.

**NOTE: This documentation is being manually mirrored to the [previous repo](https://github.com/OSGConnect/connectbook)**

Please update the documentation in the previous repo when making changes to this repo until the previous repo is deprecated.

## Guides

- [Adding Documentation](#adding-documentation)

## Adding Documentation

Add your new documentation to the 'documentation' directory.

For frontmatter use the following template:

```yaml
    ---
    osgconnect:
      path: <location where this file should be served from in osgconnect>
    ---
```

The path that you add can be different from the location where the file is stored in documentation, 
the current file hierarchy is purely organizational. It is best that the path aligns with the names in the
navigation config.

Then add the path you added above to the navigation hosted in 'data/configs' in the appropriate section.
