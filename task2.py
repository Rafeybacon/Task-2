import sys #Importing the sys module to allow access to the exit() function

yes = ['yes', 'y'] #Store values for the program to recognise a yes response
no = ['no', 'n'] #Store values for the program to recognise a no response
screen_problem = ['screen', 'display', 'fuzzy', ] #Store keywords for the program to recognise a screen problem
battery_problem = ['battery', 'overheating', 'charging'] #Store keywords for the program to recognise a battery problem

end = False #Variable controls whether program is finished or not


def menu(): #Function that contains the main logic of the program
    usr_name = str(input('Hello please enter your name: ')) #Variable to store the users name
    device = input('Please enter what device you have: ') #Variable to store the users device

    if usr_name == '' or device == '': #Checking if any of the to variables are empty
        print('You have not entered your name or device!') #If they are then prompt user to enter them again
        usr_name = str(input('Please enter your name: '))
        device = input('Please enter what device you have: ')
        

    while not end: #Loop doesn't break till it becomes true
        print('Hello', usr_name, ) #Welcome the user
        print('\nExplain the problem you are experiencing with your device',
              '\nEnsure you use keywords to be as specific as you can and we will find a solution!')
        
        usr_inp = input('Explain your problem: ') #Variable to store the users input
        while usr_inp == '': #loop is false until usr_inp has data
            usr_inp = input('No data detected! Please explain the problem to continue... ') #prompt user to enter data 

        for x in screen_problem: #For loop to compare values in screen_problem list and the users input
           if x in usr_inp: #If values in screen_problem are in users input call screen() function
                screen()
                break; 
           
        for x in battery_problem: #For loop to compare values in battery_problem list and the users input
            if x in usr_inp: #If values in battery_problem are in users input call battery() function
                battery()
                break;

        for x in battery_problem or screen_problem:
            if x not in usr_inp:
                menu()


def screen(): #Function for handling opening and reading text file with solution to screen problem
    finish = False
    screen_text = open('screen.txt', 'r') #Opening screen.txt and reading it
    
    for line in screen_text: #prints every line in the text file
        print(line)

    while not finish:

        usr_inp = str(input('Has the problem been solved? ')) #Checking if users problem is solved

        if usr_inp in yes: #If problem is solved ask user if they want to return to start
            print('Great!')
            usr_inp = str(input('Would you like to return to the start? '))

            if usr_inp in no: #If they dont call exit() function and program exits
                sys.exit('Exiting...')
            elif usr_inp in yes: #If they do they are retruned to the beginning of the loop
                finish = True

        elif usr_inp in no: #If problem isn't solved advise user to contact support
             print('That is unfortunate!')
             print('It is recommended that you contact support in order to get further support')

             usr_inp = str(input('Would you like to return to the start? ')) #Ask user if they'd like to return to start

             if usr_inp in no: #If they don't call exit() function
                  sys.exit('Exiting...')
             elif usr_inp in yes: #If they do return them to start of loop
                 finish = True


def battery(): #Function for handling opening and reading text file with solution to battery problem
    finish = False
    battery_text = open('battery.txt', 'r') #Opening battery.txt and reading it

    for line in battery_text: #prints every line in the text file
        print(line)
        
    while not finish:
        
        usr_inp = str(input('Has the problem been solved? ')) #Checking if users problem is solved

        if usr_inp in yes: #If problem is solved ask user if they want to return to start
            print('Great!')
            usr_inp = str(input('Would you like to return to the start? '))

            if usr_inp in no: #If they dont call exit() function and program exits
                sys.exit('Exiting...')
            elif usr_inp in yes: #If they do they are retruned to the beginning of the loop
                end = True

        elif usr_inp in no: #If problem isn't solved advise user to contact support
            print('That is unfortunate!')
            print('It is recommended that you contact support in order to get further support')

            usr_inp = str(input('Would you like to return to the start? ')) #Ask user if they'd like to return to start

            if usr_inp in no: #If they don't call exit() function
                sys.exit('Exiting...')
            elif usr_inp in yes: #If they do return them to start of loop
                end = True


menu() #calls the menu() function to start the program
