import list_functions as lf
import statistics

lists = {}

items_data = {}

list_intervals = []

pred_items = {}

pred_lists = {}

def prompt_user():
    # Ask if input, generate, or exit
    response = input('Would you like to input a list or generate a list? (input/generate/exit)\n')

    if response == 'input':
        # get_list if user wants to input
        lf.get_list(lists, items_data, pred_items, list_intervals)
        # Restart process once done
        prompt_user()
    elif response == 'generate':
        # generate_list if user wants to generate
        lf.generate_list(lists, pred_items, items_data, list_intervals, pred_lists)
        # Restart process once done
        prompt_user()
    elif response == 'exit':
        # End program 
        return None
    else:
        # Re-prompt user if incorrect input
        print('Please type "input" to input a list, "generate" to generate a list, or "exit" to exit the app.\n')
        prompt_user()

def main():
    # Welcome user
    print('## WELCOME TO GROCERY LIST CREATOR ##')

    # Prompt user actions
    prompt_user()        
    
    return None
    

if __name__ == '__main__':
    main()
