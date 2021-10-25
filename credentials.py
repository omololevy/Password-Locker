import password
import account

passcord= password.Password()
class Credentials:
  """This class adds user credential."""
  def __init__(self):
      self.credntial_list=[]

  def add_credential(self):
    '''Adds already existing credenial to the app'''
    print("  \n Add your credential here.")
    print("-"*15)

    acc_name= input("Enter account name:\n")
    acc_userName= input("Account username:\n")
    acc_pass=input("Account password:\n")

    new_acc =account.Account(acc_pass, acc_userName, acc_pass)
    self.credntial_list.append(new_acc)
    print(f"{acc_name} account credentials added successfully!")

    #if a user wants a valid generated password
    need_password =True
      