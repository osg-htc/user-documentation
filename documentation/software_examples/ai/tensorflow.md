---
ospool:
  path: software_examples/ai/tensorflow.md
---

The OSPool enables AI (Artificial Intelligence) workloads by providing
 access to GPUs and custom software stacks via containers. An example of this support is the machine learning platform TensorFlow.
# TensorFlow

[https://www.tensorflow.org/](https://www.tensorflow.org/) desribes TensorFlow as:

> TensorFlow is an open source software library for numerical
> computation using data flow graphs. Nodes in the graph represent
> mathematical operations, while the graph edges represent the
> multidimensional data arrays (tensors) communicated between them. The
> flexible architecture allows you to deploy computation to one or more
> CPUs or GPUs in a desktop, server, or mobile device with a single
> API. TensorFlow was originally developed by researchers and engineers
> working on the Google Brain Team within Google's Machine Intelligence
> research organization for the purposes of conducting machine learning
> and deep neural networks research, but the system is general enough to
> be applicable in a wide variety of other domains as well.

TensorFlow can be a complicated software to install as it requires many dependencies and specific environmental configurations. Software ontainers solve this problem by defining a
full operating system image, containing not only the complex software package, but
dependencies and environment configuration as well. Working with GPUs and
containers are detailed in the general documentation:

  * [GPU Jobs](../../../htc_workloads/specific_resource/gpu-jobs/)
  * [Containers - Apptainer/Singularity](../../../htc_workloads/using_software/containers-singularity/)

## Python Code

    #!/usr/bin/env python3
    
    # example adopted from https://www.tensorflow.org/tutorials/quickstart/beginner
    
    import tensorflow as tf
    print("TensorFlow version:", tf.__version__)
    
    # this will show that the GPU was found
    tf.debugging.set_log_device_placement(True)
    
    # load a dataset
    mnist = tf.keras.datasets.mnist
    
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    
    # build a machine learning model
    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10)
    ])
    
    predictions = model(x_train[:1]).numpy()
    
    # convert to probabilities
    tf.nn.softmax(predictions).numpy()
    
    # loss function
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    loss_fn(y_train[:1], predictions).numpy()
    
    # compile model
    model.compile(optimizer='adam',
                  loss=loss_fn,
                  metrics=['accuracy'])
    
    # train
    model.fit(x_train, y_train, epochs=5)
    
    # evaluate
    model.evaluate(x_test,  y_test, verbose=2)


## Submit File

    universe = container
    container_image = /cvmfs/singularity.opensciencegrid.org/htc/tensorflow:2.15

    log = job_$(Cluster)_$(Process).log
    error = job_$(Cluster)_$(Process).err
    output = job_$(Cluster)_$(Process).out
    
    executable = run-tf.py
    #arguments = 
   
    # specify both general requirements and gpu requirements 
    requirements = True
    require_gpus = (Capability > 7.5)
    
    request_gpus = 1
    request_cpus = 1
    request_memory = 4GB
    request_disk = 4GB
    
    queue 1


