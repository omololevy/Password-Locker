from pyperclip import init_klipper_clipboard
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

  def create_credential(self):
    """This method create new credential and adds it to the app"""
    print("  \n Add your credential here.")
    print("-"*15)
    acc_name= input("Enter account name:\n")
    acc_userName= input("Account username:\n")
    acc_pass= " "

      #if a user wants a valid generated password
    need_password =True
    while need_password:
      need_syst_password=input("Do you want the password generated for you? Y/n")
      if need_syst_password =="Y":
        need_password= False
        acc_pass=passcord.gen_password()
        print(f"Your password: {acc_pass} (copied to clipboard)")

      elif need_password=="n":
        acc_pass=input("Enter Account password:\n")
        pass_confirm=input("Confirm the password:\n")
        if acc_pass==pass_confirm:
          need_password=False

        else:
          print("Passwords did not match!! Try again.")
          need_password= True

      else:
          print("..Invalid Choice!! Choose Y/n")
          need_password=True

    new_acc=account.Account(acc_name,acc_userName,acc_pass)
    self.credntial_list.append(new_acc)
    print(f"{acc_name} account credentials created successfully!")

      