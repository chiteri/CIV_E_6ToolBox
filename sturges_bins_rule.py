from math import log

# Calculate the number of bins for a histogram based on Sturge's rule
# Formula is: Number of columns = [ 1 + 3.3 log (n) ]

def no_of_bins_sturges( no_of_observations ):
    return 1 + 3.3 * log(no_of_observations, 10)
