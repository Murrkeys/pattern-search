# pattern-search

This project aims to determine whether a given pattern appears in a data series, and if so, where it is located in the data series. The method used is known as matched filtering and is also widely used in communication systems.  Project was completed as coursework for Masters of Health Data Science at University of New South Wales. 

Scripts included : 

* calculate_similarity.py : Define a function that calculates the similarity between one data segment and a given pattern. 

* calculate_simiarity_list.py : Define a function that calculates the similarity for all data segments in a list and the pattern.

* pattern_search_max.py : Define a function that finds highest similarity value than is also greater than or equal to threshold and returns the index.

* pattern_search_multiple : Define a function that finds non-overlapping indices that are greater than or equal to the given threshold value.
