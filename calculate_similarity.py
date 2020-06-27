"""
Purpose :  Define a function that calculates the similarity between one
data segment and a given pattern. 
    
Created on 15/4/2020
@author: Murray Keogh

Program description: 
    Write a function that calculates the similarity between a data segment
    and a given pattern. If the segment is shorter than the pattern, 
    print out 'Error' message.
    
    
Data dictionary:
    
   calculate_similarity   : Function that calculate similarity
   ds                     : Numpy array of given data segment
   patt                   : Numpy array of given pattern
   output                 : Output of function, float or string
   data_segment           : given segment of data
   pattern                : given pattern list
   
"""

import numpy as np

def calculate_similarity(data_segment, pattern):
    """ Calculate the similarity between one data segment and the pattern.

    Parameters
    ----------
    data_segment : [float]
        A list of float values to compare against the pattern.

    pattern : [float]
        A list of float values representing the pattern. 

    Returns
    -------
    float
        The similarity score/value.
        
    "Error"
        If data segment and pattern are not the same length.

    """

    # Assign given float lists to numpy array variables
    ds = np.array(data_segment)
    patt = np.array(pattern)
    
    #Check if length of segment is shorter than length of pattern
    if len(ds) != len(patt):
       output = 'Error' #Assign 'Error' to output
       
    else:
        output = np.sum(ds*patt) #assign similarity calculation to output 
    
    return output
    
