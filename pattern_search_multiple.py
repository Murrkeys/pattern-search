"""
Purpose :  Define a function that finds non-overlapping indices that are 
greater than or equal to the given threshold value.
    
Created on 15/4/2020
@author: Murray Keogh

Program description: 
    Write a function that finds non-overlapping indices that are greater 
    than or equal to the given threshold value. Also the indices must satisfy
    the following criteria:
        - an index is not selected if the value at the index is less than
              a value at one of it's overlapping indices.
        - an index is not selected if it is overlapping with first or last
              index.
    We say two indices are overlapping if the distance between them is 
    less than the width of the pattern.
    
    
Data dictionary:
    
   pattern_search_multiple: Function that finds indices
   data series            : given data series list
   pattern_width          : given pattern width
   threshold              : given threshold value
   index_start            :starting point of loop, ignores overlap with first
   index_end              :ending point of loop, ignores overlap with last
   output                 :output of function, list or string
   
"""

def pattern_search_multiple(data_series, pattern_width, threshold):
    """ Searches the data_series for all the values that satisfy the criteria
        mentioned below and in the assignment specification document.
        The function returns the indices of these values.

    Parameters
    ----------
    data_series : [float]
        A list of float values representing a data series. You are looking
        for instances of the pattern inside this data_series.

    pattern_width : [float]
        A float value. The length/width of the pattern.

    threshold : [float]
        A float value. Selected similarity measure needs to be greater than or
        equal to the given threshold value.

    Returns
    -------
    List of floats
        A list of non overlapping indices (defined below) where
        it's similarity value is greater than or equal to the given threshold
        value and that satisfy the following criteria:
            - an index is not selected if the value at the index is less than
              a value at one of it's overlapping indices.
            - an index is not selected if it is overlapping with first or last
              index.
        Overlapping indices: Two indices are overlapping if the
        distance between them is less than the width of the pattern.
    """

    #check if length of data series is shorter than length of pattern
    if len(data_series) < pattern_width:
        output = 'Insufficient data'  #assign message to output  
    else:
        #Initialize start and end variables and empty list
        output = []
        index = pattern_width
        index_end = len(data_series)-pattern_width-1

        #loop through data series
        #loop ignores any index that overlaps with first or last index
        while index <= index_end:
        
        #check if value is greater than threshold
        #check if value is the max of all values at overlapping indices
            if ((data_series[index] >= threshold)
            and (data_series[index] 
            == max(data_series[index-(pattern_width-1):index+pattern_width]))):
                
                output.append(index) #add index if criteria are true
                
                index = index+pattern_width #set index to next non-overlapping
            else:
                index = index+1 #set index to next index
                
                                
    #check if output list remains empty            
    if len(output) == 0:
        output = 'Not detected' #assign message to output
    
    return output
