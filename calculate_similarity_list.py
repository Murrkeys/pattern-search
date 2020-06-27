"""
Purpose :  Define a function that calculates the similarity for all data
segments in a list and the pattern.
    
Created on 15/4/2020
@author: Murray Keogh

Program description: 
    Write a function that calculates the similarity between all data segment in
    a list and a given pattern by using loop. Returns a list of similarity
    values. 
    
    
Data dictionary:
    
   calculate_similarity_list  : Function that calculate similarity list
   cs                         : import calculate similarity file
   patt_len                   : length of the pattern
   out_len                    : length of output list, number of unique segments
   similarity_list            : output of calculated similarity values
   slice_end                  : end point of each data segment given patt_len
   data_segment               : segment of data series to compare to pattern
   data series                : given data series list
   pattern                    : given pattern list
   
"""
import calculate_similarity as cs

def calculate_similarity_list(data_series, pattern):
    """ Calculate the similarity measures between all possible data segments
    and the pattern.

    The function calculates the similarity measures, using the 
    function 'calculate_similarity', of all possible data segments in a 
    data_series against a given pattern and returns the list of calculated 
    similarity values.

    Parameters
    ----------
    data_series : [float]
        A list of float values representing a data series. 
        
    pattern : [float]
        A list of float values representing the pattern. 

    Returns
    -------
        List of floats
            The list of calculated similarity values.

    """
    #Initialize length variables and empty list
    patt_len = len(pattern)
    out_length = len(data_series) - (patt_len-1)
    similarity_list = [0]*out_length
    
    #Loop through data series, calculate similarity for each segment
    for k in range(0,out_length):
        #end of segment 
        slice_end = k+patt_len 
        #slice from index to end of segment
        data_segment = data_series[k:slice_end] 
        #calculate similarity for each segment, store in similarity list
        similarity_list[k] = cs.calculate_similarity(data_segment,pattern)
    
    return similarity_list
