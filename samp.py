import getpass
np=""
while 1:
  np=getpass.getpass("enter passyy: ")
  repass=getpass.getpass("Retype: ")
  if np==repass:
    break
  print("TRy again")
print(np)