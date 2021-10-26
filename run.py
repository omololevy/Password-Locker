#!/usr/bin /env python3.9
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
            print("The username is too short!!")
        else:
            valid_username = False

    need_password = True
    while need_password:
        need_sys_password = input(
            "Do you want the password generated for you? Y/n")
        if need_sys_password == "Y":
            need_password = False
            register_password = password_info.gen_password()
            print(
                f"Your password: {register_password} (copied to clipboard)\n Registration Successful!")
        elif need_sys_password == "n":
            register_password = input(
                "Enter password, at least 8 characters:\n")
            confirm_password = input("Confirm password:\n")
            if len(register_password) < 8:
                need_password = True
                print("Password too short!")

            elif confirm_password == register_password:
                print("Registration Successful!")
                need_password = False

            else:
                print("Passwords do not match!")

        else:
            print("Invalid Choice!! Choose Y/n")

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
            print("Login successful!")
            is_login = False
            user_info = user.User.return_user(login_username, login_password)
            account_menu(login_username, user_info)
        else:
            print("Login Failed!!")
            is_login = True


def account_menu(this_user_name, this_user_object):
    """
    Function that displays a navigation menu in a user's account.
    """

    print(f"WELCOME TO YOUR ACCOUNT, {this_user_name.upper()}")
    print("Options menu")
    print("1. Add existing credential  - press 1")
    print("2. Create new credential    - press 2")
    print("3. View saved credentials   - press 3")
    print("4. Copy username & password - press 4")
    print("5. Delete saved credential  - press 5")
    print("6. Log out                  - press 6")

    is_selected = True
    while is_selected:
        print(" ")
        selected = input(
            "What operation do you want to do? Select an option from above: ")
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
            is_selected = False
            print("LOGGED OUT.")
            print(" ")
        else:
            print("nvalid Option!")
            is_selected = True


def main():
    """
    This is the main method that runs the entire app.
    """
    print("PASSWORD LOCKER.")
    print("`"*20)
    proceed = "1"
    to_proceed = True
    while to_proceed:
        proceed = input("Press 1 to login or 0 to exit: ")
        if proceed == "1":
            to_proceed = True

            has_valid_account = True
            while has_valid_account:
                has_account = input("Have an account? (Y/n): ")
                if has_account == "Y":
                    login()
                    has_valid_account = False
                elif has_account == "n":
                    register()
                    has_valid_account = False
                else:
                    print("Invalid choice!! Choose Y/n")
                    has_valid_account = True

        elif proceed == "0":
            to_proceed = False
        else:
            print("Invalid Option!!")
            to_proceed = True
    print("GOOD BYE. NICE TIME!")

if __name__ == "__main__":
    main ()