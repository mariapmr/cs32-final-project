import list_functions as lf
import statistics
# Import Rich library to style terminal
from rich import print
from rich.console import Console
console = Console()

lists = {}

items_data = {}

list_intervals = []

pred_items = {}

pred_lists = {}

def prompt_user():
    # Ask if input, generate, or exit
    response = console.input('Would you like to [bold green]input[/] a list or [bold blue]generate[/] a list? ([bold green]input[/]/[bold blue]generate[/]/[bold red]exit[/])\n')

    if response == 'input':
        console.rule(style='bold bright_green')
        # get_list if user wants to input
        lf.get_list(lists, items_data, pred_items, list_intervals)
        console.rule(style='bold bright_magenta')
        # Restart process once done
        prompt_user()
    elif response == 'generate':
        console.rule(style='bold bright_blue')
        # generate_list if user wants to generate
        lf.generate_list(lists, pred_items, items_data, list_intervals, pred_lists)
        console.rule(style='bold bright_magenta')
        # Restart process once done
        prompt_user()
    elif response == 'exit':
        console.print('## THANK YOU FOR USING GROCERY LIST CREATOR ##', style='bold white on red', justify='center')
        console.rule(style='bold bright_red')
        # End program 
        return None
    else:
        # Re-prompt user if incorrect input
        print('Please type "input" to input a list, "generate" to generate a list, or "exit" to exit the app.\n')
        prompt_user()

def main():
    # Welcome user
    console.print('## WELCOME TO GROCERY LIST CREATOR ##', style='bold white on red', justify='center')

    console.rule(style='bold bright_magenta')
    # Prompt user actions
    prompt_user()        
    
    return None
    

if __name__ == '__main__':
    main()
