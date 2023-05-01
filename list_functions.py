# Import statistics for mode
import statistics
# Import datetime library to manipulate dates
import datetime

def get_list(lists, items_data, pred_items, list_intervals):
    '''
        Collects grocery list input from user --
        This function collects intervals between purchases 
        and updates a dictionary of inputted lists.
        Nested functions include: get_date(), get_items(),
        and update_predictions()
    '''

    # Initialize date variable 
    ilist_date = ''
    # Store return of get_date
    ilist_date_info = get_date(ilist_date)

    # Store datetime object
    ilist_date = ilist_date_info[0]
    # Store weekday of inputted date
    ilist_weekday = ilist_date_info[1]

    # Find interval between this purchase and last purchase
    # Store previous purchase dates as list
    list_dates = list(lists.keys())

    # Check if previous purchases exist
    if len(list_dates) != 0:
        # Find most recent purchase
        most_recent = max(list_dates)

        # Subtract dates to find interval between purchases
        interval = ilist_date - most_recent

        # Add to list of all intervals between purchases
        list_intervals.append(interval)

    # Initialize list of items
    items = []

    # Store return of get_items
    ilist_info = get_items(ilist_date, ilist_weekday, items, items_data)
    
    # List of item tuples - (item name, quantity)
    items = ilist_info[0]

    '''
        Dictionary containing item data - 
        {item name: 
            {'dates': [* list of dates when item was purchased as datetime *]},
            {'quantity': [* list of quantities as str *]},
            {'weekday': [* list of weekdays as int *]},
            {'interval': [* list of intervals as timedelta *]}
        }
    '''
    items_data = ilist_info[1]

    # Initialize dictionary where inputted items are stored
    ilist_items_dict = {}
    
    # Iterate through item tuples
    for i in range(len(items)):
        # Set item name as key, quantity as value
        ilist_items_dict[items[i][0]] = items[i][1]
    
    # Update lists dictionary
    # Set inputted date as key, inputted items dict as value 
    lists[ilist_date] = ilist_items_dict

    # Update dictionary containing prediction values
    pred_items = update_predictions(items_data, pred_items)

    return lists, items_data, list_intervals, pred_items

def get_date(ilist_date):
    '''
        Collects inputted list date from user
    '''
    # Get date from user input
    date_input = input('Please input the date of your purchase (dd/mm/year):\n')

    # Convert input to datetime object
    # Create list of elements of date
    date_input = list(map(int, date_input.split('/')))

    # Convert list to datetime object (year, month, day)
    ilist_date = datetime.datetime(date_input[2], date_input[1], date_input[0])

    # Get day of week from datetime object
    ilist_weekday = ilist_date.weekday()

    return ilist_date, ilist_weekday

def get_items(ilist_date, ilist_weekday, items, items_data):
    '''
        Collects inputted items item-by-item
    '''
    # Prompt item input
    response = input('Input item? (Y/N)\n')

    # Check response for correct input to begin info collection
    if response == 'Y':
        # User inputs item name
        item_name = input('Item name?\n')

        # User inputs item quantity
        item_quant = input('Item quantity? (# unit i.e. 6 oz)\n')

        # Store item name and quantity
        item_info = (item_name, item_quant)

        # Add item to list of items
        items.append(item_info)

        # Print list after each item addition
        # Print list date and printout format
        print(f'List on {ilist_date}\n')
        # Print each element from items list
        for i in range(len(items)):
            print(f'{items[i]}')

        # Check if item is in items_data dictionary
        if item_name not in items_data:
            # If not, create new key with item
            items_data[item_name] = {
                'dates': [],
                'quantity': [],
                'weekday': [],
                'interval': []
            }

            # Add data points from item info collected
            items_data[item_name]['dates'].append(ilist_date)
            items_data[item_name]['quantity'].append(item_quant)
            items_data[item_name]['weekday'].append(ilist_weekday)
            # Do not add interval if first time collecting data on item
        else:
            # Find most recent date from 'dates' category prior to ilist_date
            # Used to find interval
            most_recent = max(items_data[item_name]['dates'])

            # If already in dictionary, add data points
            items_data[item_name]['dates'].append(ilist_date)
            items_data[item_name]['quantity'].append(item_quant)
            items_data[item_name]['weekday'].append(ilist_weekday)
        
            # Find interval between last purchase and new purchase
            interval = ilist_date - most_recent
            
            # Add interval to dictionary as timedelta object
            items_data[item_name]['interval'].append(interval)

        # Loop through asking for items until user finishes 
        response = get_items(ilist_date, ilist_weekday, items, items_data)
    # User has finished inputs
    elif response == 'N':
        # Print finalized list
        print(f'List on {ilist_date}\n')
        for i in range(len(items)):
            print(f'{items[i]}\n')
        
        # *** STRETCH GOAL *** 
        '''
        # Prompt for corrections
        correct_list(items)
        '''
    # Re-prompt user if input is incorrect
    else:
        print('Please input \'Y\' for yes or \'N\' for no.')
        get_items(ilist_date, ilist_weekday, items, items_data)
    
    return items, items_data

def update_predictions(items_data, pred_items):
    '''
        Updates dictionary where predicted values
        are stored for each item
        Called after each input of a list
    '''
    # Get keys from items_data as item_names
    item_names = list(items_data.keys())

    # Iterate through keys to form pred_items
    for i in range(len(item_names)):
        # Replace previous data with updated data with each function call
        # Check if there is an interval (item was inputted more than once)
        if len(items_data[item_names[i]]['quantity']) > 1:
            pred_items[item_names[i]] = {
                'pred_quantity': statistics.mode(items_data[item_names[i]]['quantity']),
                'pred_weekday': statistics.mode(items_data[item_names[i]]['weekday']),
                'pred_interval': statistics.mode(items_data[item_names[i]]['interval'])
            }
        else:
            # If no interval, only updated quantity and weekday
            pred_items[item_names[i]] = {
                'pred_quantity': statistics.mode(items_data[item_names[i]]['quantity']),
                'pred_weekday': statistics.mode(items_data[item_names[i]]['weekday']),
            }

    return pred_items


def generate_list(lists, pred_items, items_data, list_intervals, pred_lists):
    '''

    '''
    
    # Initialize predicted items list to be printed
    pred_list_items = []
    
    # Get list of purchase dates
    lists_dates = list(lists.keys())
    # Find most recent purchase date
    most_recent = max(lists_dates)

    # Find most common interval between purchases
    pred_purchase_interval = statistics.mode(list_intervals)

    # Set predicted purchase date as last purchase + interval
    pred_list_date = most_recent + pred_purchase_interval

    # Get weekday of predicted date
    pred_list_weekday = pred_list_date.weekday()

    # Iterate through each item in pred_items to see if likely to be in this purchase
    for item_name in pred_items:
        # Get weekday from pred_items
        pred_item_weekday = pred_items[item_name]['pred_weekday']
        # Get interval from pred_items
        pred_item_interval = pred_items[item_name]['pred_interval']
        # Check for weekday match
        if pred_item_weekday == pred_list_weekday:
            # Check for interval match
            # Find most recent purchase of item
            last_purchase = max(items_data[item_name]['dates'])

            # Find interval between last purchase and predicted list date
            interval = pred_list_date - last_purchase

            # Check if interval matches prediction
            if pred_item_interval == interval:
                # If yes, add to generated list
                pred_list_items.append((item_name, pred_items[item_name]['pred_quantity']))

    # Print predicted list
    print(f'List generated for {pred_list_date}\n')
    for i in range(len(pred_list_items)):
        print(f'{pred_list_items[i]}')

    # Store predicted list items in dictionary
    pred_list_items_dict = {}

    # Iterate through pred_list_item tuples
    for i in range(len(pred_list_items)):
        # Set item name as key, quantity as value
        pred_list_items_dict[pred_list_items[i][0]] = pred_list_items[i][1]
    
    # Set predicted list date as key, items dict as value
    pred_lists[pred_list_date] = pred_list_items_dict

    return pred_lists