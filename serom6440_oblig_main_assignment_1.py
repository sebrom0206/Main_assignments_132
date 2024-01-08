# Obligatory Main assignment 1

# Task 1
'''
import math

def pi(d=2):
    if d==2:
        print(f'{math.pi:.2f}')
    elif d>15:
        print('Too many decimals.\n',math.pi, sep='')
    else: 
        print(f'{math.pi:.{d}f}')
    
        
# Task 2

def temperature_converter(temp, scale='C'):
    if scale=='C':
        print(f'{temp*9/5+32:.1f}')
    elif scale=='F':
        print(f'{(temp-32)*5/9:.1f}')
    else:
        print(f'{temp*9/5+32:.1f}')
'''
# Task 3


# a)

balance = 500
interest_rate = 0.01
last_actions = []

def saldo():
    global balance
    print(balance)

def deposit(d):
    global balance
    global interest_rate
    balance += d

def withdrawal(w):
    global balance
    global interest_rate
   
    if w>balance:
        print('Too large withdrawal.')
    else:
        balance -= w
    
"""
def calculate_interest():
    global balance, interest_rate, last_changes

    new_balance = interest_rate*balance
    return new_balance
"""
def interest_settelment():
    global balance
    global interest_rate
    global last_changes
    
    if balance < 1000000:
        interest_rate = 0.01
        last_actions.append('+' + str(balance*interest_rate))
        balance += balance*interest_rate
        
        return balance
    
    else:
        interest_rate = 0.02
        last_actions.append('+' + str(balance*interest_rate))
        balance += balance*interest_rate
    
        return balance


    #balance+=(balance*interest_rate)
    #return balance

    
# b) c)
# jobbet med semol5515

def choose():
    while True:
        try: 
            print('------------------------')
            print('1 - show balanse')
            print('2 - deposit')
            print('3 - withdraw')
            print('4 - interest settelment')
            print('5 - last changes')
            print('6 - Quit')
            print('------------------------')

            global balance
            global interest_rate
            
            if balance>=1000000 and interest_rate==0.01:
                print('Your balance is over 1 million NOK, you get a higher rate!')
                interest_rate=0.02
            elif balance<1000000 and interest_rate==0.02:
                print('Your balance is under 1 million NOK, you now have a normal rate')
                interest_rate=0.01
                 
            action = int(input('Choose action: '))
            
            if action == 1:
                #last_actions.append(balance)
                print('Balance:', balance)
                    
            elif action == 2:
                dep=int(input('Amount:'))
                deposit(dep)
                        
                last_actions.append('+' + str(dep))
                    
            elif action == 3:
                wit=int(input('Amount:'))
                withdrawal(wit)
                last_actions.append('-' + str(wit))
                    
            elif action == 4:
                interest_settelment()
                #last_actions.append('+' + str(calculate_interest()))
                    
            elif action == 5:
                print('Last changes:')
                for i in last_actions[-3:]:
                    print(i)
                        
            elif action == 6:
                print('Thank you')
                break
            
        except ValueError:
            print('You must choose a integer between 1-6')
choose()
# Task 4
'''
import random

def three_random():
    number_one = random.randrange(1,10)
    number_two = random.randrange(1,10)
    number_three = random.randrange(1,10)

    small = min(number_one, number_two, number_three)
    big = max(number_one, number_two, number_three)

    tot = number_one+number_two+number_three-small-big

    print(small,tot,big,sep='')
'''
