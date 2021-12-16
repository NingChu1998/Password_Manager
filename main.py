# A library that allows us to copy and past text
# Step1:  ....

import pyperclip

# This dict is made for holding key value pairs 
password_dict = {'fb':'social_beast_123',
                 'ig':'showoff_123',
                 'gmail':'textmom_567',
                 'github':'softwarebaby_987',
                 'notion':'notion_progirl_345',
                 'binance':'to_the_moon888'}

# Create a boolean value

repeat_forever = True

# sort and display all the options we have
def get_password():
    for account in password_dict:
        print('-' + account)

    # Add a try block to make sure that user doesn't mess up anything and if they do it will not crash
    try:
        account_selected = input("Which account would you like to get the password for?").lower()
        # if we insert the site we want, it will check what values associated with the site. It will give us the password
        password_selected = password_dict[account_selected]
        # copy to our clipboard
        pyperclip.copy(password_selected)
        print("------------------------------")
        print("Password for" + account_selected + "has been copied to your clipboard")
        print("------------------------------")
    # adding except block to prevent error
    except:
        print("Please enter an account form the list.")
        get_password()

# Call this function for the first time
get_password()
# Make sure that after this executed the program does not finish abruptly to create a while loop
while repeat_forever:
    get_another_password = input('Would you like to get another password? y/n')
    if get_another_password == 'y':
        get_password()
    else:
        repeat_forever = False
        print("Got it! See you next time👍")
