import os
from colorama import Fore, Style, init

# Set up colorama for Windows compatibility
init(autoreset=True)

# Logo with green ASCII art and red "programmed by" text
logo = Fore.GREEN + """
                                                                                        
                                         ,d                                                  
                                         88                                                  
                 adPPYba,  ,adPPYYba,  MM88MMM  8b       d8  ,adPPYYba,  88,dPYba,,adPYba,   
                I8[    ""  ""     `Y8    88     `8b     d8'  ""     `Y8  88P'   "88"    "8a  
                 `"Y8ba,   ,adPPPPP88    88      `8b   d8'   ,adPPPPP88  88      88      88  
                aa    ]8I  88,    ,88    88,      `8b,d8'    88,    ,88  88      88      88  
""" + Fore.RED + "programmed by" + Fore.GREEN + """   `"YbbdP"'  `"8bbdP"Y8    "Y888      Y88'     `"8bbdP"Y8  88      88      88  
                                                    d8'                                        
                                                   d8'                                                                                                                     
""" + Style.RESET_ALL 

print(logo)

# Print the social media link in blue
print("\nCheck out more cool projects here: " + Fore.BLUE + "tinyurl.com/hero-hu" + Style.RESET_ALL + " \n")

# Prompt the user to enter a directory path
directory_path = input("Enter the directory path: ")

# Checing if the directory exists
if os.path.isdir(directory_path):
    files_in_directory = os.listdir(directory_path)
    for index, file in enumerate(files_in_directory, start=1):
        # Create the full path to the item
        full_path = os.path.join(directory_path, file)
        if os.path.isfile(full_path):
            print(f"{index}. {file}")
else:
    print("That directory doesn't seem to exist.")

# Wait for the user to press Enter before closing this helps to prevent sudden closing of window
input("\nPress Enter to exit...")