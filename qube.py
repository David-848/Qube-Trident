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
	site = input("\033[92m[1]\033[mhttps\n\033[92m[2]\033[mhttp\n\033[92m[3]\033[mOther\n[+]Qube:>>>")
	if site=="1":
		uweb = input("Enter Web: ")
		page = requests.get('https://www.' + uweb + '.com')
		tree = BeautifulSoup(page.content, 'html.parser')
		print(tree.prettify())
	elif site=="2":
		usr_w = input("Enter Web: ")
		branch = requests.get('http://www.' + usr_w + '.com')
		bionic = BeautifulSoup(branch.content, 'html.parser')
		print(bionic.prettify())
	elif site=="3":
		usr_pro = input("Enter web: ")
		ice = requests.get('' + usr_pro + '')
		rex = BeautifulSoup(ice.content,'html.parser')
		print(rex.prettify())
elif nav=="2":
	exit('[~]\033[92mThank You For Using Qube\033[m[~]')