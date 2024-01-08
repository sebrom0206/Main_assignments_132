class bank:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.int_r = 0.01
        self.last_actions = []

    def deposit(self, dep):

        self.balance += dep
        self.last_actions.append('+' + str(dep))

    def withdraw(self, wit):

        if wit > self.balance:
            print('Too large withdrawal.')
        else:
            self.balance -= wit
        self.last_actions.append('-' + str(wit))

    def balance(self):

        print(self.balance)

    def interest_settlement(self):

        if self.balance < 1000000:
            interest_rate = 0.01
            self.last_actions.append('+' + str(self.balance * interest_rate))
            self.balance += self.balance * interest_rate

            return self.balance

        else:
            interest_rate = 0.02
            self.last_actions.append('+' + str(self.balance * interest_rate))
            self.balance += self.balance * interest_rate

            return self.balance

    def show_last_actions(self):
        for i in self.last_actions[-3:]:
            print(i)

    def check_int_r(self):

        if self.balance >= 1000000 and self.int_r == 0.01:
            print('Your balance is over 1 million NOK, you get a higher rate!')
            self.int_r = 0.02
        elif self.balance < 1000000 and self.int_r == 0.02:
            print('Your balance is under 1 million NOK, you now have a normal rate')
            self.int_r = 0.01

def go(obj):
    while True:
        print('------------------------')
        print('1 - show balance')
        print('2 - deposit')
        print('3 - withdraw')
        print('4 - interest settlement')
        print('5 - last changes')
        print('6 - Quit')
        print('------------------------')

        obj.check_int_r()

        action = int(input(f'User logged in: {obj.name}\nChoose action: '))

        if action == 1:
            print(f'Balance: {obj.balance}\nInterest rate: {obj.int_r}')
        elif action == 2:
            d = int(input('Enter amount: '))
            obj.deposit(d)
        elif action == 3:
            w = int(input('Enter amount: '))
            obj.withdraw(w)
        elif action == 4:
            obj.interest_settlement()
        elif action == 5:
            print('Last changes: ')
            for i in obj.last_actions[-3:]:
                print(i)
        elif action == 6:
            print('Bye')
            break

# test run

namep1 = input('Enter name: ')
balancep1 = int(input('Enter balance: '))

person1 = bank(namep1, balancep1)
go(person1)
