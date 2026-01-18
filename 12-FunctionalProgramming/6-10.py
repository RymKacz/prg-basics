import matplotlib.pyplot as plt

# Data from measuring stations
data = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Sorting the data by temperature to ensure a readable bar chart
sorted_items = sorted(data.items(), key=lambda x: x[1])

# Using map() to create two arrays of data for the chart
cities = list(map(lambda x: x[0], sorted_items))
temperatures = list(map(lambda x: x[1], sorted_items))

# Creating the bar chart
plt.bar(cities, temperatures, color='skyblue')

# Adding title and axis labels
plt.title('Temperatures Recorded in Cities')
plt.xlabel('City')
plt.ylabel('Temperature ($^{\circ}$C)')

# Save the plot
plt.savefig('temperatures_chart.png')