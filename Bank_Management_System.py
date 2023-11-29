import random

class Bank:
    def __init__(self) -> None:
        self.accounts = {}
        self.total_loan = 0
        self.available_balance = 0
        self.loan_feature = 1
        self.bankrupt = 1
        

    def create_account(self):
        name = input("Enter Your Name: ")
        email = input("Enter Your Email: ")
        address = input("Enter Your Address: ")
        account_type = input("Enter Your Account_Type: Savings or Current: ")

        account_number = random.randint(100, 999)
        self.accounts[account_number] = {
            'name' : name,
            'email' : email,
            'address' : address,
            'account_type' : account_type,
            'balance' : 0,
            'transactions' : [],
            'loan_taken': 0
        }
        print(f'Your Account created Successfully and Account Number {account_number}')

    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            self.available_balance += amount
            self.accounts[account_number]['transactions'].append(f'Deposited {amount} Tk.')
            print('Deposit Successful')
        else:
            print('Account Does not Exist')


    def withdraw(self, account_number, amount):
        if self.bankrupt == 0:
            print('The Bank is Bankrupt.')
        else:
            if account_number in self.accounts:
                if self.accounts[account_number]['balance'] >= amount:
                    self.accounts[account_number]['balance'] -= amount
                    self.available_balance -= amount
                    self.accounts[account_number]['transactions'].append(f'Withdraw {amount} Tk.')
                    print('Withdraw Successful')
                else:
                    print('Withdrawa amount exceeded')
            else:
                print('Account Does not Exist')


    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f'Available balance: {self.accounts[account_number]['balance']} Tk.')
        else:
            print("Account does not exist.") 


    def transaction_history(self, account_number):
        if account_number in self.accounts:
            print("Transaction History:")
            for transaction in self.accounts[account_number]['transactions']:
                print(transaction)
        else:
            print("Account does not exist.")


    def take_loan(self, account_number, loan_amount):
        if self.loan_feature == 0:
            print('Taking Loan Is not available now')
        else:
            if account_number in self.accounts:
                if self.accounts[account_number]['loan_taken'] < 2:
                    self.accounts[account_number]['balance'] += loan_amount
                    self.accounts[account_number]['loan_taken'] += 1
                    self.total_loan += loan_amount
                    self.available_balance -= loan_amount
                    self.accounts[account_number]['transactions'].append(f"Loan taken: {loan_amount} Tk.")
                    print("Loan taken successfully.")
                else:
                    print("You have already taken loan two times")
            else:
                print("Account does not exist.")



    def transfer_amount(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if self.accounts[from_account]['balance'] >= amount:
                self.accounts[from_account]['balance'] -= amount
                self.accounts[from_account]['transactions'].append(f"Transferred {amount} Tk to account {to_account} Tk")
                self.accounts[to_account]['balance'] += amount
                self.accounts[to_account]['transactions'].append(f"Received {amount} Tk from account {from_account}")
                print("Transfer successful.")
            else:
                print("Insufficient balance. Does not Transfer")
        else:
            print("Account does not exist.")


    def is_bankrupt(self, bankrupt_on_of):
        self.bankrupt = bankrupt_on_of

    
    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print('Account Deleted Successfully')
        else:
            print('Account Does not Exist')


    def see_all_account(self):
        if self.accounts:
            for account_number,  account_info in self.accounts.items():
                print(f'Account No: {account_number}, Name: {account_info['name']}, Email: {account_info['email']}, Address: {account_info['address']}, Account Type: {account_info['account_type']}, Balance: {account_info['balance']}')
        else:
            print('No Account in this Bank')   

           
    def available_balance_cheak(self):
        print(f'Total balance is {self.available_balance} Tk')


    def loan_check(self):
        print(f'Total loan is {self.total_loan}')


    def loan_feature_on_of(self, loan_on_of):
        self.loan_feature = loan_on_of


bank = Bank()

    



while(True):
    print('-----------------------------------------------')
    print('-----------------------------------------------')
    ch = int(input('Choose Option: 1: User /// 2: Admin:  '))
    if ch == 1:
        while(True):
            print('-----------------------------------------------')
            print('-----------------------------------------------')
            print('Now You Are User Login /// Press 0 To Log Out:')
            print('Choose Option:')
            print('1.Create Account.')
            print('2.Deposit.')
            print('3.Withdraw.')
            print('4.Check Balance.')
            print('5.Transaction History.')
            print('6.Take Loan.')
            print('7.Balance Transfer.')

            c = int(input())
            if c == 0:
                break
            if c == 1:
                bank.create_account()
            elif c == 2:
                account_no = int(input('Enter Account Number: '))
                amount = int(input('Enter Amount: '))
                bank.deposit(account_no, amount)
            elif c == 3:
                account_no = int(input('Enter Account Number: '))
                amount = int(input('Enter Amount: '))
                bank.withdraw(account_no, amount)
            elif c == 4:
                account_no = int(input('Enter Account Number: '))
                bank.check_balance(account_no)
            elif c == 5:
                account_no = int(input('Enter Account Number: '))
                bank.transaction_history(account_no)
            elif c == 6:
                account_no = int(input('Enter Account Number: '))
                amount = int(input('Enter Amount: '))
                bank.take_loan(account_no, amount)                
            elif c == 7:
                f_account = int(input('Enter Sending Account Number: '))
                t_account = int(input('Enter Receiving Account Number: '))
                amount = int(input('Enter Amount: '))
                bank.transfer_amount(f_account, t_account, amount)
    elif ch == 2:
        print('-----------------------------------------------')
        print('-----------------------------------------------')
        while(True):        
            print('-----------------------------------------------')
            print('-----------------------------------------------')
            print('Now You Are Admin Login /// Press 0 To Log Out:')
            print('Choose Option:')
            print('1.Create Account.')
            print('2.Delete Account.')
            print('3.See User List.')
            print('4.Total Balance Of Bank.')
            print('5.Total Loan.')
            print('6.Control Loan Feature.')
            print('7.Control Bankrupt Feature.')

            c = int(input())
            if c == 0:
                break
            if c == 1:
                bank.create_account()
            elif c == 2:
                account_no = int(input('Enter Account Number: '))
                bank.delete_account(account_no)
            elif c == 3:
                bank.see_all_account()
            elif c == 4:
                bank.available_balance_cheak()
            elif c == 5:
                bank.loan_check()
            elif c == 6:
                on_of = int(input('Enter 0 for off loan system: '))
                bank.loan_feature_on_of(on_of)
                print('Loan System Turn Off Successfully')
            elif c == 7:
                on_of = int(input('Enter 0 for Declare Bankrupt: '))
                bank.is_bankrupt(on_of)
                print('Declare Bankrupt option Successfully')