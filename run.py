#!/usr/bin /env python3.9
import password
import user

password_info= password.Password()
def register():
  """
  This method creates new user registration or sign up
  """
  register_username= " "
  register_password= " "

  print("   \n *****Register Here.****")
  valid_username = True
  while valid_username:
    register_username= input("Enter username:(at least 3 characters):\n")
    if len(register_username)<3:
      valid_username =True
      print("The username is too short!!")
    else:
      valid_username=False

  need_password = True
  while need_password:
    need_sys_password= input("Do you want the password generated for you? Y/n")
    if need_sys_password=="Y":
      need_password=False
      register_password= password_info.gen_password()
      print(f"Your password: {register_password} (copied to clipboard)\n Registration Successful!")
    elif need_sys_password=="n":
      register_password= input("Enter password, at least 8 characters:\n")
      confirm_password= input("Confirm password:\n")
      if len (register_password)<8:
        need_password=True
        print ("Password too short!")

      elif confirm_password==register_password:
        print ("Registration Successful!")
        need_password= False

      else:
          print("Passwords do not match!")

    else:
      print("Invalid Choice!! Choose Y/n")

  new_user= user.User(register_username, register_password)
  new_user.add_new_user(new_user)
  login()
  
def login():
    """
    Function that allows a user with an existing account to login.
    """
    is_login=True
    while is_login:
        
        login_username=input("Enter username:\n")
        login_password=input("Enter Password:\n")
        valid_login=user.User.check_login(login_username, login_password)
        if valid_login:
            print("Login successful!")
            is_login=False
            user_info=user.User.return_user(login_username, login_password)
            account_menu(login_username, user_info)
        else:
            print("Login Failed!!")
            is_login=True


