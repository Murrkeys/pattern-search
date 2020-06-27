"""
Purpose :  Define a function that finds highest similarity value than is also
greater than or equal to threshold and returns the index.
    
Created on 15/4/2020
@author: Murray Keogh

Program description: 
    Write a function that finds highest similarity value than is also
    greater than or equal to threshold and returns the index. Returns index, 
    "Insufficient Data" if data series shorter than pattern, or "Not detected"
    if all similarity measures less than threshold. 
    
    
Data dictionary:
    
   pattern_search_max     : Function that finds max similarity
   csl                    : import of calculate similarity list file
   similarity_list        : list of similarity calculations
   data series            : given data series list
   pattern                : given pattern list
   threshold              : given threshold value
   output                 :output of function, float or string
   
"""
import calculate_similarity_list as csl

def pattern_search_max(data_series, pattern, threshold):
    """ Search for the highest similarity measure that is also greater than
        or equal to the given threshold value and returns the index of that
        value.

        The function finds the index of the highest similarity value,
        using the similarity_list returned by the function
        'calculate_similarity_list'.

    Parameters
    ----------
    data_series : [float]
        A list of float values representing a data series.

    pattern : [float]
        A list of float values representing the pattern.

    threshold : [float]
        A float value. Selected similarity measure needs to be greater than or
        equal to the given threshold value.

    Returns
    -------
    "Insufficient data" : [String]
        If the given data_series is shorter than the given pattern.

    "Not detected" : [String]
        If all the similarity measures are (strictly) less than the given
        threshold value.

    float
        Index of the highest similarity measure that is also greater than
        or equal to the given threshold value.
    """

    
    #check if length of data series is shorter than length of pattern
    if len(data_series) < len(pattern):
        output = 'Insufficient data' #assign message to output
    else:
        #use csl import to create list of similarity measures
        similarity_list = csl.calculate_similarity_list(data_series,pattern)
        #check if maximum value is greater or equal to threshold
        if max(similarity_list) >= threshold:
            #assign the index of max value to output
            output = similarity_list.index(max(similarity_list))
        else:
            #if max value less than threshold, assign message to output
            output = 'Not detected' 
    
    return output
        
