"""
This script parses the documentation content and turns it into a /doc folder that can be parsed by mkdocs.

Markdown is parsed using the path in the frontmatter

CSS is parsed using the same with the caveat that the frontmatter is deleted

All image assets are expected to be in the assets folder.

"""

import glob
import frontmatter
import os


def build_path(path: str):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

def link_in_documentation():
    """Build the frontmatter for the pages"""

    portal_keys = ["path", "ospool"]

    for portal_key in portal_keys:

        # Remove the directory first
        os.system(f"rm -rf data/docs/{portal_key}")

        non_tutorial_docs = glob.glob("documentation/**/*.md", recursive=True)

        for doc_path in non_tutorial_docs:
            with open(doc_path, "r") as fp:
                doc = frontmatter.load(fp)

            if portal_key in doc:
                destination_path = f"data/docs/{portal_key}/{doc[portal_key]['path']}"

                # Build path if not there
                build_path(destination_path)

                print(f"Linking Destination Path: {destination_path}")
                os.symlink(src=os.path.relpath(doc_path, os.path.dirname(destination_path)), dst=destination_path)

        for doc_path in glob.glob("documentation/assets/**/*.*", recursive=True):
            destination_path = f"data/docs/{portal_key}/assets/{doc_path.replace('documentation/assets/', '')}"

            # Build path if not there
            build_path(destination_path)

            print(f"Linking Destination Path: {destination_path}")
            os.symlink(src=os.path.relpath(doc_path, os.path.dirname(destination_path)), dst=destination_path)

        for doc_path in glob.glob("documentation/stylesheets/**/*.css", recursive=True):
            with open(doc_path, "r") as fp:
                doc = frontmatter.load(fp)

            if portal_key in doc:

                destination_path = f"data/docs/{portal_key}/{doc[portal_key]['path']}"

                # Build path if not there
                build_path(destination_path)

                print(f"Copying to Destination Path: {destination_path}")
                with open(destination_path, "w") as fp:
                    fp.write(doc.content)



if __name__ == "__main__":

    if "DEBUG" in os.environ and os.environ["DEBUG"]:
        os.chdir("../")

    link_in_documentation()
