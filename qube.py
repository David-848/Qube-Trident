from bs4 import BeautifulSoup
import requests                                             #/modules/

flag = 0                                                   #/*/count number of tries

#/%/_________Art__________/%/
print("\033[91m")
print("           ;               ,              ___        _         ")
print("         ,;                 '.           / _ \ _   _| |__   ____  ")
print("        ;:                   :;         | | | | | | | '_ \ / _ \ ")
print("       ::                     ::        | |_| | |_| | |_) |  __/")
print("       ':                     :          \__\_\\__,_|_.__/ \___|")
print("        :.                    :                   [~]TRIDENT[~]")
print("     ;' ::                   ::  '     ")
print("    .'  ';                   ;'  '.    ")
print("   ::    :;                 ;:    ::   ")
print("   ;      :;.             ,;:     ::   ")
print('   :;      :;:           ,;"      ::   ')
print("   ::.      ':;  ..,.;  ;:'     ,.;:   ")
print('    "'"...   '::,::::: ;:   .;.;""'    ")
print("\033[m")
print("Made by NIght KIng with <3 ")
#/%/_________Art__________/%/
nav = input("\033[92m[1]\033[mStart program\n\033[92m[2]\033[mExit program\n[+]Qube:>>>")   #/*/navigation for users
if nav=="":
	exit('Invalid Input')
elif nav=="1":
	print("\033[92m")
	print("     \_______/")
	print(" `.,-'\_____/`-.,'")
	print("  /`..'\ _ /`.,'\ ")
	print(" /  /`.,' `.,'\  \ ")
	print("/__/__/     \__\__\__")
	print("\  \  \     /  /  /")
	print(" \  \,'`._,'`./  /")
	print("  \,'`./___\,'`./")
	print(" ,'`-./_____\,-'`.")
	print("     /       \ ")
	print("\033[m")
	usr_pro = input("Enter web: ")
	ice = requests.get('' + usr_pro + '')
	rex = BeautifulSoup(ice.content,'html.parser')
	print(rex.prettify())
elif nav=="2":
	exit('[~]\033[92mThank You For Using Qube\033[m[~]')
