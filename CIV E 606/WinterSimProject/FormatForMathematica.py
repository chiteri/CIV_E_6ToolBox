import csv 

with open('Pendulum simulation - Results.csv') as csvfile:
    reader = csv.DictReader(csvfile) 
    result = []
    for row in reader: 
        # result.append(float(row['Theta - radians (5 m, 20 degrees)']))
        # result.append(float(row['Theta - degrees (5 m, 20 degrees)']))
        # result.append(float(row['Theta - radians (5 m, 15 degrees)']))
        # result.append(float(row['Theta - degrees (5 m, 15 degrees)']))
        # result.append(float(row['Theta - radians (2.5 m, 20 degrees)']))
        # result.append(float(row['Theta - degrees (2.5 m, 20 degrees)']))
        # result.append(float(row['Theta - radians (2.5 m, 15 degrees)'])) 
        result.append(float(row['Theta - degrees (2.5 m, 15 degrees)']))

    print (result)