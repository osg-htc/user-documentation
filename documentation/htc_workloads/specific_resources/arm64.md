---
ospool:
  path: htc_workloads/specific_resource/arm64.md
---

ARM64
=====

ARM64 (AArch64) and x86_64 are both 64-bit architectures, but they
differ in design and application. ARM64 is renowned for its energy
efficiency, making it ideal for mobile devices and other low-power
environments. In contrast, x86_64, predominantly used in Intel and AMD
processors, emphasizes raw performance and compatibility with legacy
software, establishing it as the standard for desktops, laptops, and
servers. However, ARM64's energy efficiency has increasingly driven its
adoption in high-throughput and high-performance computing environments.

A small number of sites within the OSPool now offer ARM64 resources,
though these resources currently see limited demand. The availability
of these underutilized cycles provides a strong incentive for users to
incorporate ARM64 resources when running their jobs.

## Listing Available Resources

To see the ARM64 resources in the OSPool, use `condor_status` with a
constraint for the archtechture (note that on Linux and HTCondor, the
offical label for ARM64 is `aarch64`):

    condor_status -constraint 'Arch == "aarch64"'


## Requesting ARM64

By default, HTCondor will automatically send your job to the same
architechture as the access point you are submitting from, which
currently is the x86_64 architechture. If you also want to target
ARM64, add the following to your `requirements`.

    requirements = (Arch == "X86_64" || Arch == "aarch64")


## Software Considerations

Since ARM64 is a different architecture, x86_64 binaries and containers
are incompatible. Additionally, OSPool's container synchronization is
not yet ARM64-compatible. Therefore, the options for software on ARM64
resources are limited to the following:

 * **Simple Python codes.** If you have a simple Python script which runs
   on the OSPool default images, it will probably work fine on ARM64 as
   well. All you need to this in this case, is update your `requirements`
   as described in the previous section.

 * **Pre-built binaries.** If you have built binaries for multiple
   architechtures, you can use HTCondor's machine add substitution 
   mechanism to switch between the binaries depending on what machine
   the job lands on. Please the the [HTCondor documentation](https://htcondor.readthedocs.io/en/latest/users-manual/submitting-a-job.html#vanilla-universe-example-for-execution-on-differing-architectures)
   for more details.

 * **Multiarch containers.** If you are able to build multiarch
   containers (for example, with `docker buildx build --platform linux/amd64,linux/arm64`),
   you can specify which container to use similar to the pre-built
   binaries case. However, the image synchronization is still a 
   manual process, so please contact support@osg-htc.org for help
   with this setup.




