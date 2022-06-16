"""
Holds some general functions to handle mapping files and symlinks
"""

import frontmatter
from io import TextIOWrapper


def connectbook_to_mkdocs():



def read_meta_data(file: str):
    """Reads the existing meta-data on a document"""

    with open(file, "rw") as fp:

        return frontmatter.load(fp).metadata


def write_meta_data(file: str, d: dict, merge: bool = True):
    """Writes a dictionary of meta-data to the top of a document"""

    with open(file, "rw") as fp:

        p = frontmatter.load(fp)

        if merge:
            p.metadata = {**d, **p.metadata}
        else:
            p.metadata = d

        fp.write(frontmatter.dumps(p))