from math import exp
import numpy as np
import matplotlib.pyplot as plt 

# Get the gamma 
def gamma(ratio_067, beta_half):
    return exp(8 * ratio_067 * beta_half) - 2

# Calculate the beta ratio of time and total duration
def beta(start, time, total_duration):
    return ((time - start) + 1) / total_duration

# Get the project labour hours for an activity at a particular time 
def activity_duration(budgeted_man_hours, ratio_067, gamma, beta):
    return budgeted_man_hours * ( 1 + gamma * exp(-8 * ratio_067) / 1 - exp(-8 * ratio_067) ) *\
     (1 - exp(-8 * ratio_067 * beta)) / (1 + gamma * exp(-8 * ratio_067 * beta))

# Calculate the peak man-hour requirements and time of occurence for an activity
def peak_hours_calculator(budget_man_hours, start_time, duration, ratio_067, beta_half):
    # 
    # ratio_067 = 1 
    # beta_half = 0.5
    y = gamma(ratio_067, beta_half)  

    time_span = [] 
    man_hours = [] 

    peak_hour_requirements = 0.00 
    peak_hour_time = 0 # An index to hold the time of occurence 
    difference = 0.0 # Difference between adjacent man hours

    # Get the durations for each time span 
    for time in range(0, duration):
        time_span.append(start_time + time)
        b = beta(start_time, time + start_time, duration)
        man_hours.append( activity_duration(budget_man_hours, ratio_067, y, b)) 

        # Find difference between current and previous man hours
        if time == 0: 
            peak_hour_requirements = man_hours[time] # 0, first element 
        elif time > 0: 
            difference = man_hours[time] - man_hours[time-1]

            if difference > peak_hour_requirements: 
                peak_hour_requirements = difference
                peak_hour_time = time_span[time]

    print ('Peak man hours requirements are {0} occuring at time {1}'.format( peak_hour_requirements, peak_hour_time))