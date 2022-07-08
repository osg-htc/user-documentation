import glob
import frontmatter
import os


def link_in_documentation():
    """Build the frontmatter for the pages"""

    for doc_path in glob.glob("../documentation/**/*.md", recursive=True):
        with open(doc_path, "r") as fp:
            doc = frontmatter.load(fp)

        destination_path = f"../data/docs/osgconnect/{doc['osgconnect']['path']}"

        # Build path if not their
        if not os.path.exists(os.path.dirname(destination_path)):
            os.makedirs(os.path.dirname(destination_path))

        os.symlink(src=doc_path, dst=destination_path)

link_in_documentation()