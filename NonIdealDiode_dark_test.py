# Package import
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
# Import homemade package by VLC
from core.DiodeFit_func import *

def test_NonIdealDiode_dark(J0,n,Rs,Rsh,T,show_plot=False):
    """ Test the NonIdealDiode function
        
    Parameters
    ----------
    J0 : float
        Dark Saturation Current.
    n : float
        Ideality factor.
    Rs : float
        Series resistance.
    Rsh : float
        Shunt resistance.
    T : float, optional
        Absolute temperature , by default 300
    show_plot : bool, optional
        If True, show the plot, by default False
    
    Returns
    -------
    None.   
    """    
    # Solve non-ideal diode equation in the dark
    V = np.arange(-0.5,5,0.001) # Voltage [V]
    J = NonIdealDiode_dark(V, J0, n, Rs, Rsh, T)

    # Get differential resistance
    Rdiff = DifferentialResistance(V, J)
    
    # Get differential ideality factor
    V1 = V[V>0.4]
    J2 = J[V>0.4] 
    ndiff = DifferentialIdealityFactor(V1,J2,T)

    # Plot the result
    if show_plot:
        fig, axs = plt.subplots(1, 3, figsize=(16,12))
        # JV curve
        axs[0].semilogy(V, abs(J))
        axs[0].set_xlabel('V [V]')
        axs[0].set_ylabel('|J| [A/m2]')
        axs[0].set_xlim(-0.5,2)
        axs[0].set_ylim(1e-6,1e4)
        
        # Rdiff curve
        axs[1].semilogy(V[:-1], Rdiff)
        axs[1].set_xlabel('V [V]')
        axs[1].set_ylabel('Rdiff [Ohm m^2]')
        axs[1].set_ylim(1e-4,1e5)

        # ndiff curve
        axs[2].semilogy(V1[:-1], ndiff)
        axs[2].set_xlabel('V [V]')
        axs[2].set_ylabel('ndiff')
        axs[2].set_xlim(0.4,1)
        axs[2].set_ylim(0.8,2.5)

        plt.show()
        
    assert abs((Rdiff[-1] - Rs)/Rs) < 1.1e-1
    assert abs((Rdiff[0] - Rsh)/Rsh) < 1.1e-1

    if Rs <= 1e-3 and Rsh >= 1e1: # don't test when Rs is too small or Rsh is too large
        assert abs((min(ndiff) - n)/n) < 0.25


if __name__ == "__main__":
    # Input parameters for testing
    J0 = [1e-9,1e-7] # A/m2
    n = [1,1.5,2] # Ideality factor
    Rs = [1e-4,1e-3] # Series resistance [Ohm m^2]
    Rsh = [1,1e1,1e2] # Shunt resistance [Ohm m^2]
    Jph = [200] # Photocurrent [A/m2]
    T = [300] # Temperature [K]

    for i in list(itertools.product(J0,n,Rs,Rsh,T)):
        test_NonIdealDiode_dark(i[0],i[1],i[2],i[3],i[4])
    
    print('All tests passed')