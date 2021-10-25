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