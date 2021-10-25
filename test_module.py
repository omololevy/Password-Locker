import unittest
from account import Account
from credentials import Credentials
from user import User

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
    User.user_list = []