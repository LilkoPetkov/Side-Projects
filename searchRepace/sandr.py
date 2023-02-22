import os
from funcs import functions


print("Initiating search and replace...")

u_input1 = input("Would you like to create a database backup? - Yes / No\n")

if u_input1 == "Yes":
    functions.db_backup_creation()
elif u_input1 == "No":
    print("No backup would be crated. Proceeding with the S&R... ")
else:
    print("Invalid input, backup would not be created! ")
 
search = input("Search for (URL): ")
replace = input("Replace with (URL): ")
 
print(functions.search_replace(search, replace))

user_input = input("Would you like to also replace links in the .CSS files? - Yes / No\n")

if user_input == "Yes":
    print("Loading... ")
    functions.css_search_replace(search, replace)
    print("Process completed successfully. ")
elif user_input == "No":
    print("Closing the script. Bye-bye! ")
else:
    user_input = input("Invalid input. Please restart the script. ")

user_input = input("Would you like to flush all caching? - Yes / No\n")

if user_input == "Yes":
    print("Loading... ")
    functions.cache_flush()
elif user_input == "No":
    print("Cache would not be flushed. \nClosing script...")
else:
    print("Invalid input, please restart the script. ")

print("You are all set! ")
