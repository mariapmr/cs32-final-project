# Import statistics for probabiity
import statistics
# Import datetime library to manipulate dates
import datetime

def get_list():
    # Get list input from user for each item
        
    # Get date of grocery purchase
    ilist_date_info = get_date()

    ilist_date = ilist_date_info[0]
    ilist_weekday = ilist_date_info[1]

    item_info = get_item()
    
    # *** What to do if multiple purchases on same day? ***
    # *** Could I integrate inputting stores to see if
    # certain stores are more common on certain days/items? ***
    
    # Item name

    # Item 
    
    # Program stores list instance and prints for user
    
    
    # Program prompts any corrections, if none move on (separate function?)
    
    
    # Create dictionary of items_data
        # Check if item input in dictionary
        # If yes, add data to key value set
    
    
    # Based on changes to items_data, update items_prediction dictionary


    # Insert list into lists dictionary, date as key and entire list as value

    return

def get_date():
    # Get date from user input
    date_input = input('Please input the date of your purchase (dd/mm/year):')

    # Convert input to date object from datetime lib
    date_input = date_input.split('/')

    ilist_date = datetime.date(date_input[2], date_input[1], date_input[0])

    # Get day of week from date object
    ilist_weekday = datetime.weekday(ilist_date)

    return ilist_date, ilist_weekday

def get_item():
    # Prompt item input
    response = input('Input item? (Y/N)')

    if response == 'Y':
        get_item_info()
    elif response == 'N':
        break
    else:
        print('Please input /'Y'/ for yes or /'N'/ for no.')
        response = get_item()

def get_item_info():
    

def check_recent(item):
    # Find most recent date in "date" of items_data[item]

    return


def generate_list():
    # Get last grocery shopping date, find interval that is next
    # Get current date and pick date for list closest to today, set as list_date


    # Find items that match to interval and day of week


    # Print list


    # Prompt user for feedback (add or remove items, edit quantities)


    # Take info from list and place in items_data to update
    


    # I would want to eventually add ability to correct data after purchases.
    # On web app, when user opens, prompt --This was our last prediction. Is this accurate to what you purchased?-- Update items_data from there
    # ***How can I replace the values taken from OG list to updated list in dictionary?*** 

    return