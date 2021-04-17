class Budget:
  category_funds = {"food": 0 , "clothing": 0, "entertainment": 0 }
  name = ''

  def __init__(self, name):
      self.name = name
      
    

  def welcome(self):

      print('Welcome '+ self.name)
      print('What operation do you want to perform')
      print('1: Withdraw')
      print('2: Deposit')
      print('3: Check balance')
      print('4: Transfer funds')
      user_input = int(input())

      if user_input == 1:
          self.withdraw()
      elif user_input == 2:
          self.deposit()
      elif user_input == 3:
          self.balance()
      elif user_input == 4:
          self.transfers()


  def deposit(self):

      print('Dear ' + self.name + ' Which category do you want to deposit funds')
      print('Choose the following')
      print('1: food')
      print('2: clothing')
      print('3: entertainment')
      user_input = int(input())

      if user_input == 1:

          deposit_amount = int(input('How much do you want to deposit'))
          self.category_funds['food'] = self.category_funds['food'] + deposit_amount
          print('Funds deposited. New balance:'+ str(self.category_funds['food']))
          self.welcome()
      elif user_input == 2:
          deposit_amount = int(input('How much do you want to deposit'))
          self.category_funds['clothing'] = self.category_funds['clothing'] + deposit_amount
          print('Funds deposited. New balance:'+ str(self.category_funds['clothing']))
          self.welcome()
      elif user_input == 3:
          deposit_amount = int(input('How much do you want to deposit'))
          self.category_funds['entertainment'] = self.category_funds['entertainment'] + deposit_amount
          print('Funds deposited. New balance:'+ str(self.category_funds['entertainment']))
          self.welcome()
      else:
          pass



  def withdraw(self):
      print('Dear ' + self.name + ' Which category do you want to withdraw funds ')
      print('Choose the following')
      print('1: food')
      print('2: clothing')
      print('3: entertainment')
      user_input = int(input())

      if user_input == 1 and self.category_funds['food'] != 0:

          withdraw_amount = int(input('How much do you want to withdraw '))
          self.category_funds['food'] = self.category_funds['food'] - withdraw_amount
      elif user_input == 2 and self.category_funds['clothing'] != 0:
          withdraw_amount = int(input('How much do you want to withdraw '))
          self.category_funds['clothing'] = self.category_funds['clothing'] - withdraw_amount
      elif user_input == 3 and category_funds['entertainment'] != 0:
          withdraw_amount = int(input('How much do you want to withdraw '))
          self.category_funds['entertainment'] = self.category_funds['entertainment'] + withdraw_amount
      else:
           print('Insufficient funds. First deposit funds')
           self.welcome()

  def balance(self):
      user_input = int(input('Check balance: Choose 1. Food 2. Clothing 3. Entertainment'))
      print()
      if user_input == 1:
          print('Food balance: ' + str(self.category_funds['food']))
          print()
          self.welcome()
      elif user_input == 2:
          print('Clothing balace: ' + str(self.category_funds['clothing']))
          print()
          self.welcome()
      elif user_input == 3:
          print('Entertainment balance: ' + str(self.category_funds['entertainment']))
          print()
          self.welcome()

  def transfers(self):
      user_input_debit = int(input('Transfer from. 1: Food 2: Clothing 3: Entertainment '))
      user_input_credit = int(input('Transfer to. 1: Food 2: Clocthing 3: Entertainment '))
      debit_amt = int(input('How much do you want to transfer '))
      
      if self.category_funds[key] > debit_amt:
          self.category_funds[self.checksum(user_input_credit)] = self.category_funds[self.checksum(user_input_credit)] + debit_amt
          self.category_funds[self.checksum(user_input_debit)]  = self.category_funds[self.checksum(user_input_debit)]  - debit_amt

          
      else:
          print('insufficent balance')
          print()
          self.welcome()

  def checksum(self,user_input):


      choice = ""
      if user_input == 1:

          choice = "food"
      elif user_input == 2:
          choice = "clothing"
      elif user_input == 3:
          choice = "entertainment"
      return choice

username = input('Please login by typing your name ')

Budget1 = Budget(username)
Budget1.welcome()