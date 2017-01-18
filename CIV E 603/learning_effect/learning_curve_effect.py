from math import log, pow

# Find the learning percentage as a fraction of times taken to 
# carry out a task in the first and second repetitions
def learning_percentage(first_repetition_time, second_repetition_time):
     return second_repetition_time / first_repetition_time

# Determine the learning coefficient beta given the learning percentage
def learning_coefficient(learning_percentage):
    return log(learning_percentage, 10) / log(2, 10)

# Find the performance time given the repetition number 
def performance_time(first_repetition_time, repetition_number, learning_coefficient):
    return first_repetition_time * pow(repetition_number, learning_coefficient)

# Factor to discount a construction activity given the 
# repetition number and learning curve factor 
def activity_discount(repetition_number, learning_coefficient): 
    return pow(repetition_number, learning_coefficient)