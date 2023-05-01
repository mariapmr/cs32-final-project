# cs32-final-project

This project will focus on creating an algorithm that analyzes the grocery purchases made by a user to identify what items are purchased regularly, at what interval items are purchased (i.e. I bulk buy rice once a month, but buy milk once a week), and how much of an item is purchased. By analyzing the data, the program should find trends and be able to automatically create a grocery list.

Dream features in this project include giving users the ability to give feedback on the list (i.e. mark an item as irrelevant or put on the list at an inappropriate time, mark an item as missing from the list when it was needed) that would then lead to more accurate results.

For the purposes of this project, I would likely be creating sample data based on my family's grocery data and any other people who may volunteer to help me. One question is whether future iterations of the project could scan receipts or access data from grocery shopping platforms like InstaCart to automate the process of users inputting their grocery data.

# fp-design-update

In terms of functionality, the script I will write will take grocery purchases as a csv file. The csv will then be converted to extract patterns. Currently, I am using mode and the statistics library to accomplish this, but would like to take a more probabilistic approach. 
The inputs will consist of:
  day of week, date, item, quantity number, and quantity units
The outputs will consist of:
  a generated grocery list complete with weekday, date, items, quantity number, and quantity unit
 
The main functional blocks of code consists of opening the sample data as a csv, inserting the data into lists, and using the statistics function to find the mode of the weekday list to find the most likely weekday that the user makes grocery purchases.

Next steps would be to figure out how to have the computer generate output probabilistically. I would like to have a dictionary where the keys are the purchased items and the values are the interval between purchases, quantity, and unit of quantity. The values would be updated with each input of a grocery purchase.