import unittest

import pyperclip
from account import Account
from credentials import Credentials
from user import User
from password import Password

class UserTest(unittest.TestCase):
  """Test class that tests cases for the password locker and executions
  Args:
      unittest.TestCase
  """
  def setUp(self):
    """
    Setup method to run before each test cases.
    """
    self.account_info=Account("Twitter", "Levy", "levy1010")
    self.user_info=User("Levy", "levy1010")
    self.credentials_info=Credentials()

  def tearDown(self):
    """
    This method cleans the tests after every test cases
    """
    User.user_list = []

  def test_account_init(self):
    """
    This checks if the objects of Account class are intitialized correctly.
    """
    self.assertEqual(self.account_info.acc_name, "Twitter")
    self.assertEqual(self.account_info.acc_userName, "Levy")
    self.assertEqual(self.account_info.acc_pass, "levy1010")

  def test_gen_password(self):
    """
    Method to test if the password generated satitsfies the required length
    """
    pass_length=input("Test the system genereated password length:\n")
    self.assertEqual(len(Password.gen_password()),pass_length)

  def test_gen_password_copy(self):
    """
    Tests if the password generated is copied to the clipboard
    """
    self.assertEqual(Password.gen_password(),pyperclip.paste())

  def test_user_init(self):
    """
    This method tests if the objects of the class User are properly initialized.
    """
    self.assertEqual(self.user_info.username, "Levy")
    self.assertEqual(self.user_info.password, "levy1010")

  def test_add_user(self):
    """
    This method tests if a user can be added to the userlist
    """
    self.user_info.add_new_user(self.user_info)
    self.assertEqual(len(User.users_list), 1)

    