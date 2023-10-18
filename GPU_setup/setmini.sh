# Create a new directory called "work"
mkdir -p work && \

# Navigate to the new directory
cd work && \

# Copy the Miniconda installation script from a shared directory
cp /home/Share/Miniconda3-latest-Linux-x86_64.sh . && \

# Run the installation script
bash Miniconda3-latest-Linux-x86_64.sh
