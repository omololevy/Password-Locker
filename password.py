import string
import random
import pyperclip

class Password:
  """This class generates system passwords."""
  pass_letters= (string.ascii_letters)
  pass_nums=list(string.digits)
  pass_symbols=["&","%","$","#","@","!","~"]
  pass_chars=[]
  pass_chars.extend(pass_letters)
  pass_chars.extend(pass_nums)
  pass_chars.extend(pass_symbols)

  @classmethod
  def gen_password(cls):
    """
    Method to generate random passwords for a system.
    
    Returns:
      System generated password
    """
    pass_length = 10
    num_valid = True
    while num_valid:
      try:
        pass_length = int(input("Enter a password length of your desire(Not less than 8):\n"))
        if pass_length<8:
          print("\nThis is too short!! Try Again.\n")
          num_valid=True

        else:
          num_valid=False

      except ValueError:
        print("\nInvalid Input!! Kindly use numbers.\n")
        num_valid=True

    generated_password="".join(random.sample(cls.pass_chars, pass_length))

    pyperclip.copy(generated_password)

    return generated_password
    