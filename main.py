#importing libbaries
import sqlite3
import site
import PyQt5
#intzilating variables
site.getsitepackages()
#connecting to databases
class chatsesion:
  def __init__(self, joincode, chatmesages):
    self.joincode = joincode
    self.chatmesages = chatmesages
    return [self.joincode, self.chatmessage]
  def __init__getmessages(self):
    self.itemlist = list(sqlite3.fechall())
    return self.itemlist
  def addmessage(self, messagetoadd):
    pass
class user:
  def __init__(self):
    pass
logintable = sqlite3.connect("login table")
chatsesionstable = sqlite3.connect("chat sesions tabel")
while True:
  pass