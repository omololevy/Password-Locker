from pyperclip import init_klipper_clipboard
import pyperclip
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
    print("  \n Create your credential here.")
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

  def view_credentials(self):
    """Method to display stored credentials."""
    print("  \n View your credential here.")
    print("-"*15)
    if len(self.credntial_list)==0:
      print("No saved credentilas yet. Please add.")

    else:
        for item in self.credntial_list:
          print(f"Account: {item.acc_name}; Username: {item.acc_userName}; Password: {item.acc_pass}")

  def delete_credential(self):
    """Method to delete stored credentials from the app."""
    print("  \n Delete a credential.")
    print("-"*10)
    self.view_credentials()
    print(" ")
    if len(self.credntial_list)==0:
      print("No credential available for delete!!")
      pass
    else:
      delete_operation=True
      while delete_operation:
        acc_delete=input("type account name you intend to delete:\n")
        for item in self.credntial_list:
          if item.acc_name==acc_delete:
            self.credntial_list.remove(item)
            print(f"{acc_delete} account credentials deleted successfully!")
            delete_operation=False
            break
          else:
              delete_operation=True

        if delete_operation==False:
          pass
        else:
            print(f"Account \"{acc_delete}\" not found!!")

  def copy_credential(self):
    """
    Method that copies user credentials (username and password) to clipboard
    """
    print("  \n Copy username and password.")
    print("-"*10)
    self.view_credentials()
    print("\n")
    if len(self.credntial_list)==0:
      print("No credetial to copy to clipboard!")
      pass
    else:
      copy_operation=True
      while copy_operation:
        acc_copy= input("Enter the account name you intend to copy.")
        for item in self.credntial_list:
          if item.acc_name==acc_copy:
            userAndPassword=item.acc_userName+ " "+item.acc_pass
            pyperclip.copy(userAndPassword)
            print(f"{acc_copy} username and password copied to clipboard!")

            copy_operation=False
            break
          else:
            copy_operation=True
        if copy_operation==False:
          pass
        else:
          print(f"Account \"{acc_copy}\" not found!!")
