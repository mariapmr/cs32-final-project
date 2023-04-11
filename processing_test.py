'''
This is a test of what a portion of my final project may look like. It utilizes generated sample data designed to be an easy test case. 

There are many limitations to this test case and the methods I am currently using (i.e. using mode can miss important patterns). 

I hope to use an ML approach or more probabilistic approach in future versions but currently don't have the knowledge to build this.
'''
# Import csv to manipulate sample data
import csv
# Import statistics to use mode
import statistics


# open the file in read mode
sample_data1 = open('sample_data1.csv', 'r')

data = csv.DictReader(sample_data1)
 
# creating empty lists
date = []
weekday = []
item = []
quantity = []
unit = []
 
# iterating over each row and append
# values to empty list
for col in data:
    date.append(col['Date'])
    weekday.append(col['Day of week'])
    item.append(col['Item'])
    quantity.append(col['Quantity'])
    unit.append(col['Unit'])


# Function that identifies most common day of week for purchases
def day_of_week(weekday):
    # Find mode of "Day of week" column, set as purchase_day
    purchase_day = statistics.mode(weekday)
    print(purchase_day)
    

day_of_week(weekday)
# Function that identifies repeated items and gathers quantities, and dates in separate lists
# Iterate through "Item" column
    # If item[i] == item[j], grab quantity and date
    # Subtract dates to find spacing between purchases
    # Find mode in dates and use as purchase_interval
    # Find mode in quantity and set as purchase_quantity

