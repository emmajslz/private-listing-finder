# Private Real Estate Listing Finder

Program that finds private real estate listings (posted by individuals and not real estate agents).

## Set up the program

### Clone the respository:

   ```bash
   git clone https://github.com/emmajslz/private-listing-finder.git
   cd private-listing-finder
   ```

### Conda environment

To run this project, you'll need to recreate the Conda environment with all the necessary dependencies.

1. Install Conda from [Anaconda](https://www.anaconda.com/download) or [Miniconda](https://docs.anaconda.com/miniconda/miniconda-install/).

    [Anaconda vs. Miniconda](https://docs.anaconda.com/distro-or-miniconda/)

2. Create the conda environment

    ```bash
    conda env create -f environment.yml
    ```

3. Activate the environment

    ```bash
    conda activate private-listing-finder
    ```

4. Verify that the installation was successful

    ```bash
    python --version
    conda list
    ```
