
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
password="hello123"


print(Fore.GREEN + """
 _       ___    ____  ____  ____  
| |     /   \  /    ||    ||    \ 
| |    |     ||   __| |  | |  _  |
| |___ |  O  ||  |  | |  | |  |  |
|     ||     ||  |_ | |  | |  |  |
|     ||     ||     | |  | |  |  |
|_____| \___/ |___,_||____||__|__|""")

login=input("Enter Pass" + Back.BLUE + "$")
if login == ("Angles0001"):
    print("Hey daddy welcome back<3333")
