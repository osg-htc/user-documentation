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

CONNECTBOOK_MAP = [['/connectbook/start/account/generate-add-sshkey.md', 'overview/welcome_and_account_setup/generate-add-sshkey.md'], ['/connectbook/start/account/registration-and-login.md', 'overview/welcome_and_account_setup/registration-and-login.md'], ['/connectbook/start/account/starting-project.md', 'overview/welcome_and_account_setup/starting-project.md'], ['/connectbook/welcome/overview/is-it-for-you.md', 'overview/welcome_and_account_setup/is-it-for-you.md'], ['/connectbook/welcome/overview/acknowledgOSG.md', 'overview/references/acknowledgeOSG.md'], ['/connectbook/start/data/file-transfer-via-htcondor.md', 'managing_htc_workloads_on_osg_connect/managing_data_for_jobs/file-transfer-via-htcondor.md'], ['/connectbook/start/data/file-transfer-via-http.md', 'managing_htc_workloads_on_osg_connect/managing_data_for_jobs/file-transfer-via-http.md'], ['/connectbook/start/data/osgconnect-storage.md', 'managing_htc_workloads_on_osg_connect/managing_data_for_jobs/osgconnect-storage.md'], ['/connectbook/start/data/output-file-transfer-via-htcondor.md', 'managing_htc_workloads_on_osg_connect/managing_data_for_jobs/output-file-transfer-via-htcondor.md'], ['/connectbook/start/data/scp.md', 'managing_htc_workloads_on_osg_connect/submitting_htc_workloads_with_htcondor/tutorial-quickstart/README.md'], ['/connectbook/start/data/stashcache.md', 'managing_htc_workloads_on_osg_connect/managing_data_for_jobs/stashcache.md'], ['/connectbook/start/resources/gpu-jobs.md', 'managing_htc_workloads_on_osg_connect/considerations_for_specific_resource_needs/gpu-jobs.md'], ['/connectbook/start/resources/large-memory-jobs.md', 'managing_htc_workloads_on_osg_connect/considerations_for_specific_resource_needs/large-memory-jobs.md'], ['/connectbook/start/resources/multicore-jobs.md', 'managing_htc_workloads_on_osg_connect/considerations_for_specific_resource_needs/multicore-jobs.md'], ['/connectbook/start/resources/openmpi-jobs.md', 'managing_htc_workloads_on_osg_connect/considerations_for_specific_resource_needs/openmpi-jobs.md'], ['/connectbook/start/resources/requirements.md', 'managing_htc_workloads_on_osg_connect/using_software_on_the_osg/requirements.md'], ['/connectbook/start/scaling-up/checkpointing-on-OSPool.md', 'managing_htc_workloads_on_osg_connect/submitting_htc_workloads_with_htcondor/checkpointing-on-OSPool.md'], ['/connectbook/start/scaling-up/dagman-workflows.md', 'managing_htc_workloads_on_osg_connect/automated_workflows/dagman-workflows.md'], ['/connectbook/start/scaling-up/preparing-to-scale-up.md', 'managing_htc_workloads_on_osg_connect/htc_workload_planning_testing_scaling_up/preparing-to-scale-up.md'], ['/connectbook/start/scaling-up/submit-multiple-jobs.md', 'managing_htc_workloads_on_osg_connect/submitting_htc_workloads_with_htcondor/submit-multiple-jobs.md'], ['/connectbook/start/software/available-containers-list.md', 'managing_htc_workloads_on_osg_connect/using_software_on_the_osg/available-containers-list.md'], ['/connectbook/start/software/compiling-applications.md', 'managing_htc_workloads_on_osg_connect/using_software_on_the_osg/compiling-applications.md'], ['/connectbook/start/software/containers.md', 'managing_htc_workloads_on_osg_connect/using_software_on_the_osg/containers.md'], ['/connectbook/start/software/containers-docker.md', 'managing_htc_workloads_on_osg_connect/using_software_on_the_osg/containers-docker.md'], ['/connectbook/start/software/containers-singularity.md', 'managing_htc_workloads_on_osg_connect/using_software_on_the_osg/containers-singularity.md'], ['/connectbook/start/software/example-compilation.md', 'managing_htc_workloads_on_osg_connect/using_software_on_the_osg/example-compilation.md'], ['/connectbook/start/software/new_modules_list.md', 'managing_htc_workloads_on_osg_connect/using_software_on_the_osg/new_modules_list.md'], ['/connectbook/start/software/singularity-containers.md', 'managing_htc_workloads_on_osg_connect/using_software_on_the_osg/containers.md'], ['/connectbook/start/software/software-overview.md', 'managing_htc_workloads_on_osg_connect/using_software_on_the_osg/software-overview.md'], ['/connectbook/start/software/software-request.md', 'managing_htc_workloads_on_osg_connect/using_software_on_the_osg/software-request.md'], ['/connectbook/start/jobdurationcategory.md', 'overview/references/contact-information.md'], ['/connectbook/start/roadmap.md', 'managing_htc_workloads_on_osg_connect/htc_workload_planning_testing_scaling_up/roadmap.md'], ['/connectbook/hpcadmin/osg-flock.md', 'hpc_administration/osg_for_hpc_administrators/osg-flock.md'], ['/connectbook/hpcadmin/osg-xsede.md', 'hpc_administration/osg_for_hpc_administrators/osg-xsede.md'], ['/connectbook/welcome/overview/getting-help-from-RCFs.md', 'support_and_training_resources/get_help!/getting-help-from-RCFs.md'], ['/connectbook/welcome/overview/gracc.md', 'overview/references/gracc.md'], ['/connectbook/welcome/overview/policy.md', 'overview/references/policy.md'], ['/connectbook/examples/conda-on-osg.md', 'software_examples_for_osg/other_languages_tools/conda-on-osg.md'], ['/connectbook/examples/java-on-osg.md', 'software_examples_for_osg/other_languages_tools/java-on-osg.md'], ['/connectbook/examples/julia-on-osg.md', 'software_examples_for_osg/other_languages_tools/julia-on-osg.md'], ['/connectbook/examples/manage-python-packages.md', 'software_examples_for_osg/python/manage-python-packages.md'], ['/connectbook/examples/FreeSurfer/Introduction.md', 'software_examples_for_osg/freesurfer/Introduction.md'], ['/connectbook/training/training/osgusertraining.md', 'support_and_training_resources/education_and_training/osgusertraining.md'], ['/connectbook/training/training/osg-user-school.md', 'support_and_training_resources/education_and_training/osg-user-school.md'], ['/connectbook/training/training/previous-training-events.md', 'support_and_training_resources/education_and_training/previous-training-events.md'], ['/connectbook/training/resources/contact-information.md', 'overview/references/contact-information.md'], ['/connectbook/training/resources/frequently-asked-questions-faq-.md', 'overview/references/frequently-asked-questions-faq-.md'], ['/connectbook/start/jobs/tutorial-command.md', 'managing_htc_workloads_on_osg_connect/submitting_htc_workloads_with_htcondor/tutorial-command.md'], ['/tutorials/tutorial-AutoDockVina/README.md', 'software_examples_for_osg/drug_discovery/tutorial-AutoDockVina/README.md'], ['/tutorials/tutorial-blast-split/README.md', 'software_examples_for_osg/bioinformatics/tutorial-blast-split/README.md'], ['/tutorials/tutorial-bwa/README.md', 'software_examples_for_osg/bioinformatics/tutorial-bwa/README.md'], ['/tutorials/tutorial-error101/README.md', 'managing_htc_workloads_on_osg_connect/submitting_htc_workloads_with_htcondor/tutorial-error101/README.md'], ['/tutorials/tutorial-matlab-HelloWorld/README.md', 'software_examples_for_osg/matlab_runtime/tutorial-matlab-HelloWorld/README.md'], ['/tutorials/tutorial-organizing/README.md', 'managing_htc_workloads_on_osg_connect/submitting_htc_workloads_with_htcondor/tutorial-organizing/README.md'], ['/tutorials/tutorial-osg-locations/README.md', 'managing_htc_workloads_on_osg_connect/submitting_htc_workloads_with_htcondor/tutorial-osg-locations/README.md'], ['/tutorials/tutorial-pegasus/README.md', 'managing_htc_workloads_on_osg_connect/automated_workflows/tutorial-pegasus/README.md'], ['/tutorials/tutorial-quickstart/README.md', 'managing_htc_workloads_on_osg_connect/submitting_htc_workloads_with_htcondor/tutorial-quickstart/README.md'], ['/tutorials/tutorial-R/README.md', 'software_examples_for_osg/r/tutorial-R/README.md'], ['/tutorials/tutorial-R-addlibSNA/README.md', 'software_examples_for_osg/r/tutorial-R-addlibSNA/README.md'], ['/tutorials/tutorial-ScalingUp-Python/README.md', 'software_examples_for_osg/python/tutorial-ScalingUp-Python/README.md'], ['/tutorials/tutorial-ScalingUp-R/README.md', 'software_examples_for_osg/r/tutorial-ScalingUp-R/README.md'], ['/tutorials/tutorial-tensorflow-containers/README.md', 'software_examples_for_osg/machine_learning/tutorial-tensorflow-containers/README.md'], ['/tutorials/tutorial-wordfreq/README.md', 'software_examples_for_osg/python/tutorial-wordfreq/README.md']]

def build_url_frontmatter():
    """Build the frontmatter for the pages"""

    for doc_path in glob.glob("/Users/clock/PycharmProjects/user-documentation/documentation/**/*.md", recursive=True):
        with open(doc_path, "rw") as fp:
            doc = frontmatter.load(fp)

            doc['osgconnect'] = {}
            doc['osgconnect']['path'] = doc_path.replace("/Users/clock/PycharmProjects/user-documentation/documentation/", "")

            frontmatter.dump(doc, fp)

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

symlink_connectbook_to_mkdocs()
