# PVLC_Diode_Fit

## Author
Vincent M. Le Corre

## Description
Series of utilities for fitting non-ideal diode models to JV data. 
The utilities can be used to fit a dark JV curve of a solar cells with the following equation:
$$J = J_0\left[\exp\left(-\frac{V-R_s J}{n k_b T}\right)-1\right] + \frac{V-R_s J}{R_{sh}}$$

or to fit the light JV with:
$$J = J_{ph} - J_0\left[\exp\left(-\frac{V-R_s J}{n k_b T}\right)-1\right] - \frac{V-R_s J}{R_{sh}}$$

The method used to calculate the dark JV is based on the the study by Ortiz-Conde et al. published in [Solid-State Electronics 44 (2000) 1861-1864](https://doi.org/10.1016/S0038-1101(00)00132-5).\
And for the light JV, the method is based on the study by Jain et al. published in [Solar Energy Materials & Solar Cells 81 (2004) 269–277](https://doi.org/10.1016/j.solmat.2003.11.018)

## Repository Folder Structure
    .
    ├── Main                                    # Main directory, place Notebooks here to run them
        ├── core                                # Contains main custom packages and functions
        ├── test_data                           # Directory with some test samples of JV data
        ├── Notebooks                           # Contains clean versions of the Notebooks, Notebooks need to be moved to the main directory to be used
    └── README.md
