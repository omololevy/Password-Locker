import credentials

class User:
  """
  Class that generates new instances of account users
  """
  users_list = []

  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.credential=credentials.Credentials()

  @classmethod
  def add_new_user(cls, new_user): 
    """This adds a new user to the users list."""
    cls.user_list.append(new_user)
