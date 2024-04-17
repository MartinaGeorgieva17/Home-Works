
def deposit(account, amount):
    account['balance']+=amount
      
def withdraw(account, amount):
    if account ['balance']<amount:
        print('Not enought balance!')
        return
    account['balance']-=amount
      

def show_details(account):
    print(f'{account['owner']}=>{account['balance']}')
     
      
if __name__ == '__main__':
   account1 =[
       {
           'owner':'Maria', 
           'balance':1300
           }
           'owner':'Petar', 
           'balance':100
           }
   ]
   
   for account 