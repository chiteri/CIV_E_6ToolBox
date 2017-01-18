from learning_curve_effect import learning_percentage as lp, \
learning_coefficient as lc, performance_time as pt, \
activity_discount as ad
import csv

# def calculate_learning_curve(repetition, first_duration, second_duration, learning_percent):
def calculate_learning_curve(repetition, learning_percent):
    learning_coefficient = lc(learning_percent)
    return ad(repetition, learning_coefficient)

# Pass the repetition around to determine the percentage of learning
def process_values(repetition): 
    # Begin looping with the parameters below 
    LOW, HIGH, STEP = 60, 100, 5

    for percentage in range (LOW, HIGH, STEP): 
        duration_discount = calculate_learning_curve(repetition, percentage / 100)
        print ('{0:.4f}'.format(duration_discount), end=' ')

        if percentage == 95:
            percent_95.append(duration_discount)

        if percentage == 90:
            percent_90.append(duration_discount)

        if percentage == 85:
            percent_85.append(duration_discount)

        if percentage == 80:
            percent_80.append(duration_discount)

        if percentage == 75:
            percent_75.append(duration_discount)

        if percentage == 70:
            percent_70.append(duration_discount)

        if percentage == 65:
            percent_65.append(duration_discount)
        
        if percentage == 60:
            percent_60.append(duration_discount)

# Lists to hold the values of percentage discounts
percent_95 = []
percent_90 = []
percent_85 = []
percent_80 = []
percent_75 = []
percent_70 = []
percent_65 = []
percent_60 = []

def main():
    print('{0} {1} {2} {3} {4} {5} {6} {7} {8}'.format('Rpt. ', ' 60%'.ljust(6),\
    ' 65%'.ljust(6), ' 70%'.ljust(6), ' 75%'.ljust(6), ' 80%'.ljust(6), \
    ' 85%'.ljust(6), ' 90%'.ljust(6), ' 95%'.ljust(6) ))

    x_axis = [] # A list to hold the X-axis values
    y_axis = [0, 1] # The  Y-axis has a range of 0 to 1

    # First ten with a step of 1
    for repetition in range(1, 11):  
        print ('{0:4d}'.format(repetition), end=' ')

        # Pass the repetition around to determine the percentage of learning
        process_values(repetition)
        x_axis.append(repetition)

        print ()

    # Next twelve with a step of 2
    for repetition in range(12, 25, 2):
        print ('{0:4d}'.format(repetition), end=' ')
        
        # Pass the repetition around to determine the percentage of learning
        process_values(repetition)
        x_axis.append(repetition)

        print ()

    # The following 25 with a step of 5
    for repetition in range(25, 50, 5): 
        print ('{0:4d}'.format(repetition), end=' ')
        
        # Pass the repetition around to determine the percentage of learning
        process_values(repetition)
        x_axis.append(repetition)

        print ()

    # Following 50 with a step of 10 
    for repetition in range(50, 100, 10): 
        print ('{0:4d}'.format(repetition), end=' ')
        
        # Pass the repetition around to determine the percentage of learning
        process_values(repetition)
        x_axis.append(repetition)

        print ()

    # Following 100 with a step of 20 
    for repetition in range(100, 200, 20):
        print ('{0:4d}'.format(repetition), end=' ')
        
        # Pass the repetition around to determine the percentage of learning
        process_values(repetition)
        x_axis.append(repetition)

        print ()

    # The next 300 with a step of 50 
    for repetition in range(200, 500, 50):
        print ('{0:4d}'.format(repetition), end=' ')
        
        # Pass the repetition around to determine the percentage of learning
        process_values(repetition)
        x_axis.append(repetition)

        print ()

    # Last 500 with a step of 100 
    for repetition in range(500, 1001, 100):
        print ('{0:4d}'.format(repetition), end=' ')
        
        # Pass the repetition around to determine the percentage of learning
        process_values(repetition)
        x_axis.append(repetition)

        print ()

    # plot your results 
    import numpy as np
    import matplotlib.pyplot as plt

    plt.plot(x_axis, percent_95, label = '95 %') #, \
    plt.plot(x_axis, percent_90, label = '90 %') #, \
    plt.plot(x_axis, percent_85, label = '85 %') #, \
    plt.plot(x_axis, percent_80, label = '80 %') #, \
    plt.plot(x_axis, percent_75, label = '75 %') #, \
    plt.plot(x_axis, percent_70, label = '70 %') #, \
    plt.plot(x_axis, percent_65, label = '65 %') #, \
    plt.plot(x_axis, percent_60, label = '60 %') #, \
    # 'b-')
    plt.axis([0, 1000, 0, 1])

    plt.legend(loc='upper right')
    plt.xlabel('Repetitions')
    plt.ylabel('Percent Learning') 
    plt.show()

    # Write the results to a csv file 
    with open('learning_activity_discounts.csv', 'w') as csvfile: 
        fieldnames = ['Rpt.', '60%', '65%', '70%', '75%', '80%', '85%', '90%', '95%'] 
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader() 

        for repetition in range(len(x_axis)):
             writer.writerow({'Rpt.': x_axis[repetition], '60%': percent_60[repetition], '65%': percent_65[repetition], \
             '70%': percent_70[repetition], '75%': percent_75[repetition], '80%': percent_80[repetition], '85%': percent_85[repetition], \
             '90%': percent_90[repetition], '95%': percent_95[repetition]})

if __name__ == '__main__':
    main()
