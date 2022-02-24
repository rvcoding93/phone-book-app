
"""
OBJECTIVES
1. If they choose to look up an entry, you will ask them for the person's name, 
and then look up the person's phone number by the given name and print it to the screen.
2. f they choose to set an entry, you will prompt them for the person's name and 
the person's phone number,
3. If they choose to delete an entry, you will prompt them for the person's 
name and delete the given person's entry.
4. If they choose to list all entries, you will go through all entries 
in the dictionary and print each out to the terminal.
5. If they choose to quit, end the program.
"""

userQuit = False
menu = """
      PHONE  BOOK
=========================
1. Look up an entry: 
2. Set an entry: 
3. Delete an entry:  
4. List all entries: 
5. Quit? 
""" 
phonebook = {}
while not(userQuit):

      print(menu)

      selected_option = input("What do you want to do (1-5)?: " )

      if selected_option == "2":
            name = input("What is the contact's name?: ")
            phone_number = input("what is the contact's phone number?:  ")
            phonebook[name] = phone_number
            print("Contact added successfully!")
      elif selected_option == "1":
            name = input("What contact information would you like to see?: ")
            if phonebook.get(name) == None:
                  print ("There is no contact with that name")
            else: 
                  print ("This is their phone number: "+ phonebook[name])
      elif selected_option == "5":
            userQuit = True
