#!/usr/bin /env python3.9.5
import password
import user

password_info = password.Password()

def register():
    """
    This method creates new user registration or sign up
    """
    register_username = " "
    register_password = " "

    print("   \n *****Register Here.****")
    valid_username = True
    while valid_username:
        register_username = input("Enter username:(at least 3 characters):\n")
        if len(register_username) < 3:
            valid_username = True
            print("\nThe username is too short!!\n")
        else:
            valid_username = False

    need_password = True
    while need_password:
        need_sys_password = input("Do you want the password created for you? y/n\n").lower()
        if need_sys_password == "y":
            need_password = False
            register_password = password_info.gen_password()
            print(f"Your password: {register_password} (copied to clipboard)\n\n Registration Successful!\n")
        elif need_sys_password == "n":
            register_password = input("Create a password, at least 8 characters:\n")
            confirm_password = input("Confirm the password:\n")
            if len(register_password) < 8:
                print("This password is too short!")
                need_password=True

            elif confirm_password == register_password:
                print("Registration Successful! Your Account has been created.\n")
                print("*"*60)
                print("\n```Now Login!````")
                need_password = False

            else:
                print("Passwords do not match!\n")
                need_password=True

        else:
            print("Invalid Choice!! Choose y/n")
            need_password=True

    new_user = user.User(register_username, register_password)
    new_user.add_new_user(new_user)
    login()


def login():
    """
    Function that allows a user with an existing account to login.
    """
    is_login = True
    while is_login:

        login_username = input("Enter username:\n")
        login_password = input("Enter Password:\n")
        valid_login = user.User.check_login(login_username, login_password)
        if valid_login:
            print("Login successful!\n")
            is_login = False
            user_info = user.User.return_user(login_username, login_password)
            account_menu(login_username, user_info)
        else:
            print("Login Failed!! You don't have an existing account.\n")
            print("Kindly consider Registration.\n")
            is_login = True
            register()


def account_menu(this_user_name, this_user_object):
    """
    Function that displays a navigation menu in a user's account.
    """
    print("*"*20)
    print(f"HELLO  {this_user_name.upper()}, WELCOME TO YOUR ACCOUNT!")
    print("*"*20)
    print("Options Menu.")
    print("`"*15)
    print("1. To Add Existing credential  - press 1")
    print("2. To Create new credential    - press 2")
    print("3. To View Saved credentials   - press 3")
    print("4. To Copy Username & Password - press 4")
    print("5. To Delete saved credential  - press 5")
    print("6. Log out                     - press 6")
    print("7. QUIT!!                      - press 7")

    is_selected = True
    while is_selected:
        print(" ")
        selected = input("CHOOSE ACTION. select option from above:\n")
        if selected == "1":
            is_selected = True
            this_user_object.credential.add_credential()
        elif selected == "2":
            is_selected = True
            this_user_object.credential.create_credential()
        elif selected == "3":
            is_selected = True
            this_user_object.credential.view_credentials()
        elif selected == "4":
            is_selected = True
            this_user_object.credential.copy_credential()
        elif selected == "5":
            is_selected = True
            this_user_object.credential.delete_credential()
        elif selected == "6":
            print("LOGGED OUT.\n")
            break
        elif selected == "7":
            is_selected = False
            print("EXITED!.\n")
            print(" ")
        else:
            print("Invalid Option!\n")
            is_selected = True
            account_menu()


def main():
    """
    This is the main method that runs the entire app.
    """
    print("\n")
    print("`"*60)
    print("\n\t\tPASSWORD LOCKER.")
    print("`"*60)
    proceed = "1"
    to_proceed = True
    while to_proceed:
        proceed = input("Press 1 to LAUNCH APP or 0 to EXIT:\n\n")
        if proceed == "1":
            to_proceed = True

            has_valid_account = True
            while has_valid_account:
                has_account = input("Do you have an account? (y/n):\n").lower()
                if has_account == "y":
                    login()
                    has_valid_account = False
                elif has_account == "n":
                    register()
                    has_valid_account = False
                else:
                    print("Invalid choice!! Choose y/n\n")
                    has_valid_account = True
                                 
        elif proceed == "0":
            to_proceed = False
        else:
            print("Invalid Option!!")
            to_proceed = True

    
    print("GOOD BYE. NICE TIME!")

if __name__ == "__main__":
    main ()