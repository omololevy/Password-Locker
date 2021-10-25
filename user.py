
class User:
  user_list = []

  def __init__(self, username, password):
    self.username = username
    self.password = password

  @classmethod
  def add_new_user(cls, new_user): #This adds a new user to the users list.
    cls.user_list.append(new_user)