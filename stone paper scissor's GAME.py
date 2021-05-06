import random as rnd
import time
a=['STONE','PAPER','SCISSOR']

upt=0#FOR STORING COMPUTER POINTS
cpt=0#FOR STORING USER POINTS

you=input('Enter Your Name : ')
print(f'\nWelcome {you} to the Game ')
while True:
    
    try:
        rounds=int(input('\nEnter Total No.of Rounds to be Played : '))#FOR TOTAL ROUNDS
        total=rounds
    except Exception as e:
        print('Please Enter Positive Integer Value more than Zero')
        continue
    break

while rounds!=0: 
    print('\nEnter Your Choice ')  # FOR TAKING INPUT
    user=int(input('1. STONE  \n2. PAPER  \n3. SCISSOR\n==>'))
    comp=rnd.choice(a)
    if user==1:
        print(f'\n{you}\'s Choice : STONE')
    elif user==2:
        print(f'\n{you}\'s Choice : PAPER')
    elif user==3:
        print(f'\n{you}\'s Choice : SCISSOR')
    else:
        print('\nWrong Choice')
        continue
    time.sleep(0.3)
    print('Computer\'s Choice :',comp)

    rounds=rounds-1

    while rounds>=0:#FOR DECIDING WINNER

        if user==1 :
            if comp=='PAPER':
                print('\nComputer Wins')
                cpt=cpt+1
                break
            elif comp=='SCISSOR':
                print(f'\nYayy {you} Wins')
                upt=upt+1
                break
            else:
                print('\nOhhh It\'s a Tie Break')
                break
            
        if user==2 :
            if comp=='SCISSOR':
                print('\nComputer Wins')
                cpt=cpt+1
                break
            elif comp=='STONE':
                print(f'\nYayy {you} Wins')
                upt=upt+1
                break
            else:
                print('\nOhhh It\'s a Tie Break')
                break
            
        if user==3 :
            if comp=='STONE':
                print('\nComputer Wins')
                cpt=cpt+1
                break
            elif comp=='PAPER':
                print(f'\nYayy {you} Wins')
                upt=upt+1
                break
            else:
                print('\nOhhh It\'s a Tie Break')
                break
                rounds=rounds-1

print('\n\nTOTAL ROUNDS PLAYED :',total)
print(f'\n{you}\'s TOTAL POINTS :',upt)
print('COMPUTER\'s TOTAL POINTS :',cpt)

if cpt>upt:
    print(f'\nOH NOO !!! {you} LOST THE GAME BY {cpt}-{upt}')
elif cpt==upt:
    print(f"\nOOPS !! THE GAME IS TIED BY {upt}-{cpt}")
else:
    print(f'\nHURREYY !!! {you} WON THE GAME BY {upt}-{cpt}')
