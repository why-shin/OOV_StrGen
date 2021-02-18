# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:25:25 2021

@author: yongjin
"""
import numpy as np

 
######### FUNCTIONS ###########
def Write_POSCAR(filename,CN_str,lattice,A_array,B_array,O_array, A='Sr', B='Fe'):
    """
    Parameters
    ----------
    filename : str
        name of POSCAR file. PatternLength_PatternNumber_TransVector.vasp
    CN_str : str
        Sequence of numbers indicating coordination number of B-cations
    lattice : numpy array
        3x3 array describing lattice vectors
    A_array : numpy array
        n x 3 array; atomic position of A-caitons.
    B_array : numpy array
        n x 3 array; atomic position of B-caitons.
    O_array : numpy array
        list of lists. Sub-lists have 3 numbers representing position of oxygen atoms
    A : str
        Name of A-cation if not defined, Sr is used.
    B : str
        Name of B-cation if not defined, Fe is used.

    Returns
    -------
    None.

    """
    out_file=open(filename,'w')
    out_file.write("{0}, CN={1}\n".format(filename,CN_str)) #first comment line
    out_file.write("1.0\n") # scale 
    for i in range(np.shape(lattice)[0]):
        out_file.write("{0:20.10f} {1:20.10f} {2:20.10f}\n".format(lattice[i,0],lattice[i,1],lattice[i,2]))
    out_file.write("   {0}   {1}   O\n".format(A,B)) # Atom labels
    out_file.write("   {0}    {1}   {2}\n".format(np.shape(A_array)[0],
                                              np.shape(B_array)[0],
                                              np.shape(O_array)[0]))
    out_file.write("   Direct\n")
    for i in range(np.shape(A_array)[0]):
        out_file.write("{0:16.10f} {1:19.10f} {2:19.10f}\n".format(A_array[i,0],A_array[i,1],A_array[i,2]))
    # for i,B_site in enumerate(B_list):
    #     out_file.write("    "+"        ".join('%.10f' % entry for entry in B_site))
    #     out_file.write("\n")
    #     out_file.close()
    for i in range(np.shape(B_array)[0]):
        out_file.write("{0:16.10f} {1:19.10f} {2:19.10f}\n".format(B_array[i,0],B_array[i,1],B_array[i,2]))
    for i in range(np.shape(O_array)[0]):
        out_file.write("{0:16.10f} {1:19.10f} {2:19.10f}\n".format(O_array[i,0],O_array[i,1],O_array[i,2]))
    # Printing oxygen sites is a bit different as it is with list format
    # for i,O_site in enumerate(O_list):
    #     out_file.write("    "+"        ".join('%.10f' % entry for entry in O_site))
    #     out_file.write("\n")
    #     out_file.close()



    