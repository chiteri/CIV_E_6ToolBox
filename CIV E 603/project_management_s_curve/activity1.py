from project_s_curve import gamma, beta, activity_duration
import numpy as np
import matplotlib.pyplot as plt 

# Plot the symmetric s curve for activity 1 
ratio_067 = 1 
beta_half = 0.5
y = gamma(ratio_067, beta_half) 

budgeted_man_hours = 12800 
man_hours = [] 
time_span = np.linspace(0, 9, 40)

# Get the durations for each time span 
for time in time_span: # range(10):
    b = beta(0, time, 10)
    man_hours.append( activity_duration(budgeted_man_hours, ratio_067, y, b))

plt.plot(time_span, man_hours, label = 'Activity 1')
plt.legend(loc='upper right')
plt.xlabel('Time span')
plt.ylabel('Man hours') 
plt.show()