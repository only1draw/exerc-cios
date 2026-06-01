from colorama import *

ph=int(input("\nDigite o valor do ph da agua:\n"))
if ph<5:
    print(Fore.RED + "nivel 1 Muito baixo (crítico). {}".format(ph))
if ph >= 5 and ph <= 6:
    print(Fore.YELLOW + "nivel 2 baixa. {}".format(ph))
if ph == 7 :
    print(Fore.GREEN + "nivel 3 media. {}".format(ph)) 
if ph == 8 :
    print(Fore.CYAN + "nivel 4 alto. {}".format(ph))
if ph >=9 :
    print(Fore.BLUE + "nivel 5 Muito alto (crítico). {}".format(ph))

