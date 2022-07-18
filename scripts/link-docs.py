import glob
import frontmatter
import os

OSGCONNECT_FILE_MAP = {
    'documentation/tutorials/tutorial-tensorflow-containers/README.md': 'software_examples_for_osg/machine_learning/tutorial-tensorflow-containers/README.md',
    'documentation/tutorials/tutorial-ScalingUp-Python/README.md': 'software_examples_for_osg/python/tutorial-ScalingUp-Python/README.md',
    'documentation/tutorials/tutorial-quickstart/README.md': 'managing_htc_workloads_on_osg_connect/submitting_htc_workloads_with_htcondor/tutorial-quickstart/README.md',
    'documentation/tutorials/tutorial-blast-split/README.md': 'software_examples_for_osg/bioinformatics/tutorial-blast-split/README.md',
    'documentation/tutorials/tutorial-bwa/README.md': 'software_examples_for_osg/bioinformatics/tutorial-bwa/README.md',
    'documentation/tutorials/tutorial-organizing/README.md': 'managing_htc_workloads_on_osg_connect/submitting_htc_workloads_with_htcondor/tutorial-organizing/README.md',
    'documentation/tutorials/tutorial-AutoDockVina/README.md': 'software_examples_for_osg/drug_discovery/tutorial-AutoDockVina/README.md',
    'documentation/tutorials/tutorial-R-addlibSNA/README.md': 'software_examples_for_osg/r/tutorial-R-addlibSNA/README.md',
    'documentation/tutorials/tutorial-wordfreq/README.md': 'software_examples_for_osg/python/tutorial-wordfreq/README.md',
    'documentation/tutorials/tutorial-error101/README.md': 'managing_htc_workloads_on_osg_connect/submitting_htc_workloads_with_htcondor/tutorial-error101/README.md',
    'documentation/tutorials/tutorial-pegasus/README.md': 'managing_htc_workloads_on_osg_connect/automated_workflows/tutorial-pegasus/README.md',
    'documentation/tutorials/tutorial-osg-locations/README.md': 'managing_htc_workloads_on_osg_connect/submitting_htc_workloads_with_htcondor/tutorial-osg-locations/README.md',
    'documentation/tutorials/tutorial-matlab-HelloWorld/README.md': 'software_examples_for_osg/matlab_runtime/tutorial-matlab-HelloWorld/README.md',
    'documentation/tutorials/tutorial-R/README.md': 'software_examples_for_osg/r/tutorial-R/README.md',
    'documentation/tutorials/tutorial-ScalingUp-R/README.md': 'software_examples_for_osg/r/tutorial-ScalingUp-R/README.md'
}

def build_path(path: str):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

def link_in_documentation(file_map: dict):
    """Build the frontmatter for the pages"""

    # Remove the directory first
    os.system("rm -rf data/docs/osgconnect")

    non_tutorial_docs = set(glob.glob("documentation/**/*.md", recursive=True)) - set(glob.glob("documentation/**/README.md", recursive=True))

    for doc_path in non_tutorial_docs:
        with open(doc_path, "r") as fp:
            doc = frontmatter.load(fp)

        destination_path = f"data/docs/osgconnect/{doc['osgconnect']['path']}"

        # Build path if not there
        build_path(destination_path)

        os.symlink(src=os.path.relpath(doc_path, os.path.dirname(destination_path)), dst=destination_path)

    for doc_path in glob.glob("documentation/assets/**/*.*", recursive=True):
        destination_path = f"data/docs/osgconnect/assets/{doc_path.replace('documentation/assets/', '')}"

        # Build path if not their
        if not os.path.exists(os.path.dirname(destination_path)):
            os.makedirs(os.path.dirname(destination_path))

        os.symlink(src=os.path.relpath(doc_path, os.path.dirname(destination_path)), dst=destination_path)

    for doc_path in glob.glob("documentation/stylesheets/**/*.css", recursive=True):
        with open(doc_path, "r") as fp:
            doc = frontmatter.load(fp)

        destination_path = f"data/docs/osgconnect/{doc['osgconnect']['path']}"

        # Build path if not their
        build_path(destination_path)

        with open(destination_path, "w") as fp:
            fp.write(doc.content)

    for doc_path, destination_path in file_map.items():

        destination_path = f"data/docs/osgconnect/{destination_path}"

        # Build path if not their
        build_path(destination_path)

        os.symlink(src=os.path.relpath(doc_path, os.path.dirname(destination_path)), dst=destination_path)


link_in_documentation(OSGCONNECT_FILE_MAP)
