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
    