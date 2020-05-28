import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]

sleeping = [7, 8, 6, 11, 7, 6, 5]
eating = [2, 3, 4, 3, 2, 4, 9]
working = [7, 8, 7, 2, 2, 7, 6]
relaxing = [8, 5, 7, 8, 13, 7, 4]

slices = [5, 9, 6, 4]
activities = ['Sleeping', 'Eating', 'Working', 'Relaxing']
cols = ['b', 'g', 'm', 'r', ]
plt.pie(slices,
        labels=activities,
        colors=cols,  
        startangle=90,  
        shadow=True,  
        explode=(0.1, 0.0, 0, 0), 
        autopct='%1.1f%%') 
plt.xlabel('') 
plt.ylabel('')  
plt.title('Hourly Breakdown Of\nEach Day Of The Week')
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.show()