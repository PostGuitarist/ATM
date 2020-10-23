import turtle
from turtle import *
import time
import random

turtle = turtle.Turtle()
turtle.speed(0)
turtle.hideturtle()
 
class Account:
    # Construct an Account object
    def __init__(self, id, balance = 0):
        self.id = id
        self.balance = balance
 
    # User Pin 
    def getId(self):
        return self.id
    
    # Returns Balance
    def getBalance(self):
        return self.balance
 
    # Withdraws Number
    def withdraw(self, amount):
        self.balance -= amount
 
    # Deposits Number
    def deposit(self, amount):
        self.balance += amount

# Draws ATM
def drawatm():
  turtle.hideturtle()
  turtle.speed(0)
  turtle.pu()
  turtle.goto(-150,-160)
  turtle.left(90)
  turtle.pd()
  turtle.fd(350)
  turtle.right(90)
  turtle.fd(350)
  turtle.right(90)
  turtle.fd(350)
  turtle.right(90)
  turtle.fd(350)
  turtle.pu()
  turtle.goto (-110,-160)
  turtle.pd()
  turtle.right(90)
  turtle.fd(350)
  turtle.pu()
  turtle.goto(157,-160)
  turtle.pd()
  turtle.fd(350)
  turtle.pu()
  turtle.goto(-100,-150)
  turtle.pd()
  turtle.fd(100)
  turtle.right(90)
  turtle.fd(245)
  turtle.right(90)
  turtle.fd(100)
  turtle.right(90)
  turtle.fd(245)
  turtle.pu()
  turtle.goto(-100, -20)
  turtle.right(90)
  turtle.pd()
  turtle.fd(200)
  turtle.right(90)
  turtle.fd(245)
  turtle.right(90)
  turtle.fd(200)
  turtle.right(90)
  turtle.fd(245)
  turtle.pu()
  
# Draws options on ATM
def drawoptions():
  turtle.goto(-90, 150)
  style = ('Courier', 15)
  turtle.pd()
  turtle.write('1. View Balance', font=style)
  turtle.pu()
  turtle.goto(-90, 100)
  turtle.write('2. Withdraw', font=style)
  turtle.pu()
  turtle.goto(-90, 50)
  turtle.write('3. Deposit', font=style)
  turtle.pu()
  turtle.goto(-90, 0)
  turtle.write('4. Exit', font=style)

def main():
   drawatm()
   # Creating accounts
   accounts = []
   for i in range(1000, 9999):
       account = Account(i, 0)
       accounts.append(account)
   # ATM Processes
   while True:
 
       # Reading id from user
       id = int(input('\nEnter account pin: '))
 
       # Loop till id is valid
       while id != 1234:
           id = int(input('\nInvalid Id.. Re-enter: '))
 
       # Iterating over account session
       while True:
           drawoptions()
 
           # Printing menu
           print('-----------------------------------------------------------------')
           print('\n1 - View Balance \t2 - Withdraw \t3 - Deposit \t4 - Exit ')
 
           # Reading selection
           selection = int(input('\nEnter your selection: '))
           print('-----------------------------------------------------------------')
 
           # Getting account object
           for acc in accounts:
               # Comparing account id
               if acc.getId() == id:
                   accountObj = acc
                   break
 
           # View Balance
           if selection == 1:
               style = ('Courier', 15)
               turtle.reset()
               drawatm()
               turtle.goto(-90, 150)
               turtle.pd()
               turtle.write('Your balance is: ', font=style)
               turtle.pu()
               turtle.goto(-90, 100)
               turtle.pd()
               turtle.write(str(accountObj.getBalance()), font=style)
               turtle.pu()
               
               # Printing balance
               print(accountObj.getBalance())
               time.sleep(3)
               
               turtle.reset()
               drawatm()
 
           # Withdraw
           elif selection == 2:
               style = ('Courier', 15)
               style2 = ('Courier', 12)
               turtle.reset()
               drawatm()
               
               turtle.goto(-90, 150)
               turtle.pd()
               turtle.write('Withdraw:', font=style)
               
               # Reading amount
               amt = float(input('\nEnter amount to withdraw: '))
               ver_withdraw = input('Is this the correct amount, ' + str(amt) + 'USD. Yes or No:')
 
               if ver_withdraw == 'Yes' or ver_withdraw == 'yes' or ver_withdraw == 'Y' or ver_withdraw == 'y':
                   print('Withdraw Verified')
                   turtle.reset()
                   drawatm()
               else:
                   break
 
               if amt < accountObj.getBalance():
                  # Calling withdraw method
                  accountObj.withdraw(amt)
                  
                  turtle.reset()
                  drawatm()
                  turtle.goto(-90, 150)
                  turtle.pd()
                  turtle.write('Updated Balance: ', font=style)
                  turtle.pu()
                  turtle.goto(-90, 100)
                  turtle.pd()
                  turtle.write(str(accountObj.getBalance()), font=style)
                  
                  # Printing updated balance
                  print('\nUpdated Balance: ' + str(accountObj.getBalance()) + 'USD')
                  time.sleep(2)
                  turtle.reset()
                  drawatm()
               else:
                  turtle.reset()
                  drawatm()
                  turtle.goto(-90, 150)
                  turtle.write("You're balance is", font=style)
                  turtle.goto(-70, 125)
                  turtle.write('less than the', font=style)
                  turtle.goto(-70, 100)
                  turtle.write('withdraw amount.', font=style)
                  turtle.goto(-90, 25)
                  turtle.write('Please make a deposit.', font=style2)
                  print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + 'USD')
                  print('\nPlease make a deposit.');
                  time.sleep(5)
                  turtle.reset()
                  drawatm()
 
           # Deposit
           elif selection == 3:
               style = ('Courier', 15)
               turtle.reset()
               drawatm()
               turtle.goto(-90,150)
               turtle.pd()
               turtle.write('Deposit:', font=style)
               
               # Reading amount
               amt = float(input('\nEnter amount to deposit: '))
               ver_deposit = input('Is this the correct amount, ' + str(amt) + 'USD. Yes or No:')
 
               if ver_deposit == 'Yes' or ver_deposit == 'yes' or ver_deposit == 'Y' or ver_deposit == 'y':
                  # Calling deposit method
                  accountObj.deposit(amt);
                  
                  turtle.reset()
                  drawatm()
                  turtle.goto(-90, 150)
                  turtle.pd()
                  turtle.write('Updated Balance: ', font=style)
                  turtle.pu()
                  turtle.goto(-90, 100)
                  turtle.pd()
                  turtle.write(str(accountObj.getBalance()), font=style)
                  
                  # Printing updated balance
                  print('\nUpdated Balance: ' + str(accountObj.getBalance()) + 'USD')
                  time.sleep(2)
                  turtle.reset()
                  drawatm()
               else:
                  break
                  time.sleep(2)
                  turtle.reset()
                  drawatm()
 
           elif selection == 4:
               style = ('Courier', 15)
               turtle.reset()
               drawatm()
               turtle.goto(-90, 150)
               turtle.pd()
               turtle.write('Transaction is now - ', font=style)
               turtle.pu()
               turtle.goto(-70, 125)
               turtle.pd()
               turtle.write('complete.', font=style)
               turtle.pu()
               turtle.goto(-90, 75)
               turtle.write('Transaction number:', font=style)
               turtle.pu()
               turtle.goto(-90, 50)
               turtle.pd()
               turtle.write(str(random.randint(0, 100000)), font=style)
               turtle.pu()
               turtle.goto(-90, 0)
               turtle.pd()
               turtle.write('Balance:' + str(accountObj.getBalance()), font=style)
               
               print('Transaction is now complete.')
               print('Thank you for choosing us as your bank.')
               time.sleep(5)
               turtle.reset()
               main()
 
           # Any other choice
           else:
               print("\nThat is an invalid choice.")
 
# Main function
main()

# Keeps turtle window open
turtle.done()



