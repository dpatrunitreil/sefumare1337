import os, requests, colorama, time
from colorama import Fore, Back, Style
colorama.init(strip=False)
# imports

os.system('title Server Spamer')
os.system("color f")


print(Fore.LIGHTRED_EX + r"""                                          REYZ SPAM BOT ON TOP!
                      ----- S P A M         B O T         B Y         R E Y Z -----                    
                      ----- S P A M         B O T         B Y         R E Y Z -----                    
                      """ + Fore.RED + r"""----- S P A M         B O T         B Y         R E Y Z -----                    
                      ----- S P A M         B O T         B Y         R E Y Z -----                    
                      ----- S P A M         B O T         B Y         R E Y Z ----- 
                                          REYZ SPAM BOT ON TOP!""")

print(r""" 


→ → → →
       ↓
       ↓
       ↓
       ↓""")
ask1 = input(Fore.GREEN + "TOKEN: " + Fore.RED)
print(Fore.RESET)

ask = input(Fore.GREEN + "MESSAGE: "+ Fore.RED)
print(Fore.RESET)

ask2 = input(Fore.GREEN + "CHANNEL ID: "+ Fore.RED)
api = "https://discord.com/api/v9/channels/" + ask2 + "/messages"
print(Fore.RESET)

ask3 = int(input(Fore.GREEN + "HOW MANY TIMES:"+ Fore.RED))
print(Fore.RESET)
# message die gespammt wird und die channel id wo die msg gespammt wird


payload = {
 'content': ask
}
# die message

header = {
 'authorization' : ask1
}


# die ganzen tokens


for i in range (ask3):
    ass = time.strftime("%H:%M:%S")
    print(Fore.RESET + "[" + Fore.LIGHTGREEN_EX + ass + Fore.RESET + "]" + Fore.GREEN + " Spamming..." + Fore.RESET)
    # log in der konsole
    r = requests.post(api, data=payload, headers=header)
    time.sleep(1)
    # damit es abgesendet wird

input(Fore.CYAN + "Spam was sucessfull! press enter to close this window... " + Fore.BLACK)