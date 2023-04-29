import list_functions as lf
import statistics

lists = {}

pred_items = {}

def prompt_user():
    # Ask if input, generate, or exit
    response = input('Would you like to input a list or generate a list? (input/generate/exit)\n')

    if response == 'input':
        # get_list if user wants to input
        lf.get_list(lists, pred_items)
        # Restart process once done
        prompt_user()
    elif response == 'generate':
        # generate_list if user wants to generate
        lf.generate_list()
        # Restart process once done
        prompt_user()
    elif response == 'exit':
        # End program if asked 
        return None
    else:
        print('Please type "input" to input a list, "generate" to generate a list, or "exit" to exit the app.\n')
        prompt_user()

def main():
    # Welcome user
    print('## WELCOME TO GROCERY LIST CREATOR ##')

    prompt_user()        
    
    return None
    

if __name__ == '__main__':
    main()
