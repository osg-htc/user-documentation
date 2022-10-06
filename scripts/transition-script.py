"""
This script was created to facilitate the moving of the website from freshdesk to portal.

I am keeping it because I don't have a good reason to delete it, but don't care/it won't effect anything if
it is deleted in the future.

Author: Cannon Lock
GH: CannonLock
"""

import difflib
import os
import glob
from pathlib import Path
import yaml
import frontmatter


# This is a list of file paths from the root of the connectbook repo that should be included here
CONNECTBOOK_PATHS = [
    '/connectbook/start/account/generate-add-sshkey.md',
    '/connectbook/start/account/registration-and-login.md',
    '/connectbook/start/account/starting-project.md',
    '/connectbook/welcome/overview/is-it-for-you.md',
    '/connectbook/welcome/overview/acknowledgOSG.md',
    '/connectbook/start/data/file-transfer-via-htcondor.md',
    '/connectbook/start/data/file-transfer-via-http.md',
    '/connectbook/start/data/osgconnect-storage.md',
    '/connectbook/start/data/output-file-transfer-via-htcondor.md',
    '/connectbook/start/data/scp.md',
    '/connectbook/start/data/stashcache.md',
    '/connectbook/start/resources/gpu-jobs.md',
    '/connectbook/start/resources/large-memory-jobs.md',
    '/connectbook/start/resources/multicore-jobs.md',
    '/connectbook/start/resources/openmpi-jobs.md',
    '/connectbook/start/resources/requirements.md',
    '/connectbook/start/scaling-up/checkpointing-on-OSPool.md',
    '/connectbook/start/scaling-up/dagman-workflows.md',
    '/connectbook/start/scaling-up/preparing-to-scale-up.md',
    '/connectbook/start/scaling-up/submit-multiple-jobs.md',
    '/connectbook/start/software/available-containers-list.md',
    '/connectbook/start/software/compiling-applications.md',
    '/connectbook/start/software/containers.md',
    '/connectbook/start/software/containers-docker.md',
    '/connectbook/start/software/containers-singularity.md',
    '/connectbook/start/software/example-compilation.md',
    '/connectbook/start/software/new_modules_list.md',
    '/connectbook/start/software/singularity-containers.md',
    '/connectbook/start/software/software-overview.md',
    '/connectbook/start/software/software-request.md',
    '/connectbook/start/jobdurationcategory.md',
    '/connectbook/start/roadmap.md',
    '/connectbook/hpcadmin/osg-flock.md',
    '/connectbook/hpcadmin/osg-xsede.md',
    '/connectbook/welcome/overview/getting-help-from-RCFs.md',
    '/connectbook/welcome/overview/gracc.md',
    '/connectbook/welcome/overview/policy.md',
    '/connectbook/examples/conda-on-osg.md',
    '/connectbook/examples/java-on-osg.md',
    '/connectbook/examples/julia-on-osg.md',
    '/connectbook/examples/manage-python-packages.md',
    '/connectbook/examples/FreeSurfer/Introduction.md',
    '/connectbook/training/training/osgusertraining.md',
    '/connectbook/training/training/osg-user-school.md',
    '/connectbook/training/training/previous-training-events.md',
    '/connectbook/training/resources/contact-information.md',
    '/connectbook/training/resources/frequently-asked-questions-faq-.md',
    '/connectbook/start/jobs/tutorial-command.md',
    '/tutorials/tutorial-AutoDockVina/README.md',
    '/tutorials/tutorial-blast-split/README.md',
    '/tutorials/tutorial-bwa/README.md',
    '/tutorials/tutorial-error101/README.md',
    '/tutorials/tutorial-matlab-HelloWorld/README.md',
    '/tutorials/tutorial-organizing/README.md',
    '/tutorials/tutorial-osg-locations/README.md',
    '/tutorials/tutorial-pegasus/README.md',
    '/tutorials/tutorial-quickstart/README.md',
    '/tutorials/tutorial-R/README.md',
    '/tutorials/tutorial-R-addlibSNA/README.md',
    '/tutorials/tutorial-ScalingUp-Python/README.md',
    '/tutorials/tutorial-ScalingUp-R/README.md',
    '/tutorials/tutorial-tensorflow-containers/README.md',
    '/tutorials/tutorial-wordfreq/README.md'
]

CONNECTBOOK_MAP = [['/connectbook/start/account/generate-add-sshkey.md', 'overview/account_setup/generate-add-sshkey.md'], ['/connectbook/start/account/registration-and-login.md', 'overview/account_setup/registration-and-login.md'], ['/connectbook/start/account/starting-project.md', 'overview/account_setup/starting-project.md'], ['/connectbook/welcome/overview/is-it-for-you.md', 'overview/account_setup/is-it-for-you.md'], ['/connectbook/welcome/overview/acknowledgOSG.md', 'overview/references/acknowledgeOSG.md'], ['/connectbook/start/data/file-transfer-via-htcondor.md', 'htc_workloads/managing_data/file-transfer-via-htcondor.md'], ['/connectbook/start/data/file-transfer-via-http.md', 'htc_workloads/managing_data/file-transfer-via-http.md'], ['/connectbook/start/data/osgconnect-storage.md', 'htc_workloads/managing_data/osgconnect-storage.md'], ['/connectbook/start/data/output-file-transfer-via-htcondor.md', 'htc_workloads/managing_data/output-file-transfer-via-htcondor.md'], ['/connectbook/start/data/scp.md', 'htc_workloads/submitting_workloads/tutorial-quickstart/README.md'], ['/connectbook/start/data/stashcache.md', 'htc_workloads/managing_data/stashcache.md'], ['/connectbook/start/resources/gpu-jobs.md', 'htc_workloads/specific_resource/gpu-jobs.md'], ['/connectbook/start/resources/large-memory-jobs.md', 'htc_workloads/specific_resource/large-memory-jobs.md'], ['/connectbook/start/resources/multicore-jobs.md', 'htc_workloads/specific_resource/multicore-jobs.md'], ['/connectbook/start/resources/openmpi-jobs.md', 'htc_workloads/specific_resource/openmpi-jobs.md'], ['/connectbook/start/resources/requirements.md', 'htc_workloads/using_software/requirements.md'], ['/connectbook/start/scaling-up/checkpointing-on-OSPool.md', 'htc_workloads/submitting_workloads/checkpointing-on-OSPool.md'], ['/connectbook/start/scaling-up/dagman-workflows.md', 'htc_workloads/automated_workflows/dagman-workflows.md'], ['/connectbook/start/scaling-up/preparing-to-scale-up.md', 'htc_workloads/workload_planning/preparing-to-scale-up.md'], ['/connectbook/start/scaling-up/submit-multiple-jobs.md', 'htc_workloads/submitting_workloads/submit-multiple-jobs.md'], ['/connectbook/start/software/available-containers-list.md', 'htc_workloads/using_software/available-containers-list.md'], ['/connectbook/start/software/compiling-applications.md', 'htc_workloads/using_software/compiling-applications.md'], ['/connectbook/start/software/containers.md', 'htc_workloads/using_software/containers.md'], ['/connectbook/start/software/containers-docker.md', 'htc_workloads/using_software/containers-docker.md'], ['/connectbook/start/software/containers-singularity.md', 'htc_workloads/using_software/containers-singularity.md'], ['/connectbook/start/software/example-compilation.md', 'htc_workloads/using_software/example-compilation.md'], ['/connectbook/start/software/new_modules_list.md', 'htc_workloads/using_software/new_modules_list.md'], ['/connectbook/start/software/singularity-containers.md', 'htc_workloads/using_software/containers.md'], ['/connectbook/start/software/software-overview.md', 'htc_workloads/using_software/software-overview.md'], ['/connectbook/start/software/software-request.md', 'htc_workloads/using_software/software-request.md'], ['/connectbook/start/jobdurationcategory.md', 'overview/references/contact-information.md'], ['/connectbook/start/roadmap.md', 'htc_workloads/workload_planning/roadmap.md'], ['/connectbook/hpcadmin/osg-flock.md', 'hpc_administration/osg_for_hpc_administrators/osg-flock.md'], ['/connectbook/hpcadmin/osg-xsede.md', 'hpc_administration/osg_for_hpc_administrators/osg-xsede.md'], ['/connectbook/welcome/overview/getting-help-from-RCFs.md', 'support_and_training/get_help!/getting-help-from-RCFs.md'], ['/connectbook/welcome/overview/gracc.md', 'overview/references/gracc.md'], ['/connectbook/welcome/overview/policy.md', 'overview/references/policy.md'], ['/connectbook/examples/conda-on-osg.md', 'software_examples/other_languages_tools/conda-on-osg.md'], ['/connectbook/examples/java-on-osg.md', 'software_examples/other_languages_tools/java-on-osg.md'], ['/connectbook/examples/julia-on-osg.md', 'software_examples/other_languages_tools/julia-on-osg.md'], ['/connectbook/examples/manage-python-packages.md', 'software_examples/python/manage-python-packages.md'], ['/connectbook/examples/FreeSurfer/Introduction.md', 'software_examples/freesurfer/Introduction.md'], ['/connectbook/training/training/osgusertraining.md', 'support_and_training/training/osgusertraining.md'], ['/connectbook/training/training/osg-user-school.md', 'support_and_training/training/osg-user-school.md'], ['/connectbook/training/training/previous-training-events.md', 'support_and_training/training/previous-training-events.md'], ['/connectbook/training/resources/contact-information.md', 'overview/references/contact-information.md'], ['/connectbook/training/resources/frequently-asked-questions-faq-.md', 'overview/references/frequently-asked-questions-faq-.md'], ['/connectbook/start/jobs/tutorial-command.md', 'htc_workloads/submitting_workloads/tutorial-command.md'], ['/tutorials/tutorial-AutoDockVina/README.md', 'software_examples/drug_discovery/tutorial-AutoDockVina/README.md'], ['/tutorials/tutorial-blast-split/README.md', 'software_examples/bioinformatics/tutorial-blast-split/README.md'], ['/tutorials/tutorial-bwa/README.md', 'software_examples/bioinformatics/tutorial-bwa/README.md'], ['/tutorials/tutorial-error101/README.md', 'htc_workloads/submitting_workloads/tutorial-error101/README.md'], ['/tutorials/tutorial-matlab-HelloWorld/README.md', 'software_examples/matlab_runtime/tutorial-matlab-HelloWorld/README.md'], ['/tutorials/tutorial-organizing/README.md', 'htc_workloads/submitting_workloads/tutorial-organizing/README.md'], ['/tutorials/tutorial-osg-locations/README.md', 'htc_workloads/submitting_workloads/tutorial-osg-locations/README.md'], ['/tutorials/tutorial-pegasus/README.md', 'htc_workloads/automated_workflows/tutorial-pegasus/README.md'], ['/tutorials/tutorial-quickstart/README.md', 'htc_workloads/submitting_workloads/tutorial-quickstart/README.md'], ['/tutorials/tutorial-R/README.md', 'software_examples/r/tutorial-R/README.md'], ['/tutorials/tutorial-R-addlibSNA/README.md', 'software_examples/r/tutorial-R-addlibSNA/README.md'], ['/tutorials/tutorial-ScalingUp-Python/README.md', 'software_examples/python/tutorial-ScalingUp-Python/README.md'], ['/tutorials/tutorial-ScalingUp-R/README.md', 'software_examples/r/tutorial-ScalingUp-R/README.md'], ['/tutorials/tutorial-tensorflow-containers/README.md', 'software_examples/machine_learning/tutorial-tensorflow-containers/README.md'], ['/tutorials/tutorial-wordfreq/README.md', 'software_examples/python/tutorial-wordfreq/README.md']]

def build_url_frontmatter():
    """Build the frontmatter for the pages"""

    for doc_path in glob.glob("/Users/clock/PycharmProjects/user-documentation/documentation/**/*.md", recursive=True):
        with open(doc_path, "r") as fp:
            doc = frontmatter.load(fp)

            doc['osgconnect'] = {}
            doc['osgconnect']['path'] = doc_path.replace("/Users/clock/PycharmProjects/user-documentation/documentation/", "")

        with open(doc_path, "w") as fp:
            fp.write(frontmatter.dumps(doc))

def map_connectbook_to_mkdocs():
    """One off function to map the readmes to their correct locations"""

    yml = yaml.load(open('/Users/clock/PycharmProjects/connectbook/mkdocs.yml'), Loader=yaml.SafeLoader)

    # Recursively get all values in dictionary
    correct_paths = []
    def get_values(o):
        if isinstance(o, dict):
            for v in o.values():
                get_values(v)
        elif isinstance(o, list):
            for v in o:
                get_values(v)
        else:
            correct_paths.append(o)

    get_values(yml['nav'])

    comparison_paths = ["/".join(x.split("/")[-2:]) for x in correct_paths]

    mappings = []
    for path in CONNECTBOOK_PATHS:
        mappings.append([path, difflib.get_close_matches(path, comparison_paths, 1, 0.0)[0]])

    for mapping in mappings:
        mapping[1] = list(filter(lambda x: x.endswith(mapping[1]), correct_paths))[0]

    print(mappings)

    return mappings


def symlink_connectbook_to_mkdocs():
    """Symlink the connectbook to the mkdocs directory"""

    for path in CONNECTBOOK_MAP:

        directory = os.path.dirname(f"../documentation/docs/osgconnect/{path[1]}")
        if not os.path.exists(directory):
            Path(directory).mkdir(parents=True, exist_ok=True)

        try:
            os.symlink(f"/Users/clock/PycharmProjects/user-documentation{path[0]}", f"../documentation/docs/osgconnect/{path[1]}")
        except FileExistsError:
            if path[0].split("/")[-1] != path[1].split("/")[-1]:
                print(f"{path[0]} -> {path[1]}")


def freshdesk_to_mkdocs():
    """Convert docs intended for freshdesk to mkdocs formatting"""

    for path in CONNECTBOOK_MAP:
        pass

build_url_frontmatter()
