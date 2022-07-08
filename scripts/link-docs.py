import glob
import frontmatter
import os

def link_in_documentation():
    """Build the frontmatter for the pages"""

    # Remove the directory first
    os.system("rm -rf data/docs/osgconnect")

    for doc_path in glob.glob("../documentation/**/*.md", recursive=True):
        with open(doc_path, "r") as fp:
            doc = frontmatter.load(fp)

        destination_path = f"../data/docs/osgconnect/{doc['osgconnect']['path']}"

        # Build path if not their
        if not os.path.exists(os.path.dirname(destination_path)):
            os.makedirs(os.path.dirname(destination_path))

        os.symlink(src=os.path.relpath(doc_path, os.path.dirname(destination_path)), dst=destination_path)

    for doc_path in glob.glob("../documentation/assets/**/*.*", recursive=True):
        destination_path = f"../data/docs/osgconnect/assets/{doc_path.replace('../documentation/assets/', '')}"

        # Build path if not their
        if not os.path.exists(os.path.dirname(destination_path)):
            os.makedirs(os.path.dirname(destination_path))

        os.symlink(src=os.path.relpath(doc_path, os.path.dirname(destination_path)), dst=destination_path)

    for doc_path in glob.glob("../documentation/stylesheets/**/*.css", recursive=True):
        with open(doc_path, "r") as fp:
            doc = frontmatter.load(fp)

        destination_path = f"../data/docs/osgconnect/{doc['osgconnect']['path']}"

        # Build path if not their
        if not os.path.exists(os.path.dirname(destination_path)):
            os.makedirs(os.path.dirname(destination_path))

        with open(destination_path, "w") as fp:
            fp.write(doc.content)

link_in_documentation()