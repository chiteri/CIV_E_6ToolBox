from learning_curve_effect import learning_percentage as lp, \
learning_coefficient as lc, performance_time as pt, \
activity_discount as ad 

activity_budgeted_man_hours = [12800, 84500, 21530, 53575, 17750] 

activity_learning_curves = [0.95, 0.90, 0.95, 0.90, 0.95] 

total_man_hours1 = 0.00
total_man_hours2 = 0.00
total_man_hours3 = 0.00
total_man_hours4 = 0.00
total_man_hours5 = 0.00

#Calculate the man hours required for each activity 
for counter in range(5):
    learning_coefficient = lc(activity_learning_curves[counter])

    # Loop fifty times to find out the activity discounts 
    for repetition in range(25):      
        discount = ad(repetition+1, learning_coefficient) 

        # Find total man hour requirements depending on counter value 
        if counter == 0: 
            total_man_hours1 += activity_budgeted_man_hours [counter] * discount 
        if counter == 1: 
            total_man_hours2 += activity_budgeted_man_hours [counter] * discount 
        if counter == 2: 
            total_man_hours3 += activity_budgeted_man_hours [counter] * discount 
        if counter == 3: 
            total_man_hours4 += activity_budgeted_man_hours [counter] * discount 
        if counter == 4: 
            total_man_hours5 += activity_budgeted_man_hours [counter] * discount 

# Print the results to screen 
total_man_hours = total_man_hours1 + total_man_hours2 + total_man_hours3 + total_man_hours4 + total_man_hours5
print ( "It will take {0} man hours to complete 50 units of activities with the given learning percentages if a new team starts after completing 25 units.".format(total_man_hours * 2))