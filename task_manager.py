# First we import our date and time.
# The reason for this function is that the code requests, a date task was assigned to user.
# Then we create a variable for our in the dictionary named userDisc.
from datetime import date

userDic = {}

# We give access to the file user.txt by opening it.
# We open it by calling function with open and input the reading method.
# We use function readlines().
# Which reads all the lines of the text file and returns a list of strings.
# We now introduce our for loop which will execute a group of statements.
# We pass two variables in our for loop
# User name and password whch will be stored as a dictionary.

with open('user.txt','r') as username_password:
    data_inside_file = username_password.readlines()
    for item in data_inside_file:
        username, password = item.strip('\n').split(', ')
        userDic[username] = password
        
# We then create a variable for the user to input the username
# We test/Check the input using a while loop.
# We use while not as it will return the opposite. 

username = input('Please enter username: ')
while not username in userDic:
    username = input('Wrong user:\nPlease enter username: ')


# Then we also create a variable for our userpassword for the user to input.
# A while will execute the statements within until its false
# We say while the username is not equal to the password assigned to the Value.
# It will request the user to input a valid password.

userpassword = input("Password: ")
while userDic[username] != userpassword:
    userpassword = input('Wrong Password:\nPlease enter correct Password: ')


# Now we enter into our main program 
# We start off by creating a while loop
# While loop is True it will run without any conditions until the break statements is executed.
# We therefore incorparate our statements.
# Firstly the we use the if statement to check if the user name is admin. 
# Else we provide the user with a different menu. 
# The else menu does not have an option to register a user. Only admin can register user.

while True:
    if username == 'admin':
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - View Statistics
e - Exit
: ''').lower()

    else:
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

# r for registering a user
# From the if statements above we then match with what the user has entered.
# if the username is admin and they have selected the register method from the menu.
# Then they will be able to register a new user.

# We then open the user.txt and use append text file to add a new user.
# We create a new variable for the username and password. 
# We then confirm if the user entered the same password.
# While come in very handy here. 
# We will make sure with a while loop that the user enters/confirms the valid password.
# The 'a' witll insert as per the default at the end of the text file.
# The writelines() will write the items to the file.
# We there call upon our dedicated file name username_password.
# Then write the first line with an escape character next line(\n).
# Then add the new username, seperate it with (', ') and write the password.

    if menu == 'r' and username == 'admin':
        
        with open('user.txt','a') as username_password:

            new_username = input('Please enter new username: \n')
            new_password = input('Please enter new password: \n')
            confirm_password = input("Please confirm password you just entered: ")
            while confirm_password != new_password:
                confirm_password = input('''Password does not match,
                Please confirm password you just entered: ''')
            
            username_password.writelines('\n')
            username_password.writelines(new_username)
            username_password.writelines(', ')
            username_password.writelines(confirm_password)


    
    
# 'a' for Adding a task 
# if else the user choose's 'a' which is open to admin and any-user
# We also follow the steps of opening a file.
# Then we create a variable for user who will be assigned a task.
# The variables created are title,description and due date.
# We then use datetime for formatting date objects into readable strings
# The strftime() takes one parameter.
# Then we use %d - Day of the month.
# Then we use %b - Month name in short version e.g Jan
# Then we use %Y - Year in full version 2022
# We therefore add the task by at the end using our .formart and writelines().


    elif menu == 'a':
        with open('tasks.txt','a+') as username_password:
            assigned_username = input('''Please enter,
            Username you would like to assigned task to: ''')
            title_task = input('''Please enter the
            The title of the task: ''')
            description_task = input('''Please enter the
            The description of the task: ''') 
            due_date = input('''Please enter the
            The due date of the task: ''')
            today = date.today()
            strdate = today.strftime("%d %b %Y")
            task_complete = 'No'
            username_password.writelines("\n"f'{assigned_username}, {title_task}, {description_task}, {strdate}, {due_date}, {task_complete}')
    


# 's' to View Statistics
# We proceed with the elif statement
# This will only execute if username is equal to admin.
# We create a total for users and taks and our counter to zero.
# We open the file as a read format. 
# Create a for loop where each line in our file named username_password
# Will take the the counter and procced to add 1.
# This is therefore print the total number of users and .format to call upon our global counter.
# Then we open the tasks.txt as we need to read from this file.
# We proceed with the same methods and edited our print statements to print tasks.

    elif menu == 's' and username == 'admin':
        users_total_number = 0
        tasks_total_number = 0

        with open('user.txt', 'r') as username_password:
            
            for each_line in username_password:
                users_total_number = users_total_number + 1
        
        print(f'Total number of users are {users_total_number}') # unintend 
        
        with open('tasks.txt', 'r') as username_password:
            for each_line in username_password:
                tasks_total_number = tasks_total_number + 1

        print(f'The total numbers tasks {tasks_total_number} ')
        


# 'va' to View all tasks
# First we open our list in the read format 
# we create a variable called task_items.
# We then create a strip any leading/spaces and tralling  characters 
# Then we split the string into a list (', ')
# We also create a for loop to to execute our statement.
# We create another for loop which calls each index in the task_items
# We print our tasks as indexs using [0][1][2][3][4]
# We use an escape \n to print in a readable formart and use tab to separate.

    elif menu == 'va':
        with open('tasks.txt','r') as username_password:
            tasks_items = [tasks_items.strip().split(', ') for tasks_items in username_password]

            for index in tasks_items:
                print(f'''
The Assigned user is:               {index[0]}\n
The title for the task is:          {index[1]}\n
The task was given on:              {index[3]}\n
The due date is:                    {index[4]}\n
Task Complete:                      {'No'}\n
The description of the task is:     {index[2]}\n''')

# 'vm' to view my task.
# We use the same methods as above.
# We create a new varaible name as view_my_tasks.

    elif menu == 'vm':
        view_my_tasks = input('Please enter the admin you would like to view tasks: ')
        with open('tasks.txt','r') as username_password:
           
            tasks_items = [tasks_items.strip().split(', ') for tasks_items in username_password]
            
            for line in tasks_items:
                if view_my_tasks == line[0]:
            
                    print(f'''
The Assigned user is:               {line[0]}\n
The title for the task is:          {line[1]}\n
The task was given on:              {line[3]}\n
The due date is:                    {line[4]}\n
Task Complete:                      {'No'}\n
The description of the task is:     {line[2]}''')
            break
    

# 'e' for Exit
# if user enter e then the program will exist.
# It will also print out a statement to advise your out.

    elif menu == 'e':
        print('You have existed the programm. Goodbye!!!')
        exit()

# Lastly our else statement 
# If the user enters anything thats not on the menu.
# The else statement will be executed. 
# Since it is in a while loop it will give the user a chance to try again.

    else:
        print("You have made a wrong choice, Please Try again")
