#!/bin/bash

# Create new conda environment for TensorFlow with GPU support
conda create -y -n tf_gpu

# Activate the new conda environment
conda activate tf_gpu

# Install CUDA Toolkit and cuDNN through conda-forge channel
conda install -y -c conda-forge cudatoolkit=11.2 cudnn=8.1.0

# Install pip in the environment
conda install -y pip

# Install TensorFlow GPU and TensorFlow
pip install tensorflow_gpu==2.10.0 tensorflow==2.10.0

# Install additional libraries such as Matplotlib, Pandas, and Keras
pip install matplotlib pandas keras

# Set environment variable to update LD_LIBRARY_PATH for NVIDIA GPU libraries
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

# Test the GPU setup by running a TensorFlow script
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

# conda deactive and conda active (edited)

#python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"