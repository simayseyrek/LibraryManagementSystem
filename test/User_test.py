import sys
sys.path.append('..')
from User import User


user1 = User(20202305,"simay seyrek", "simay@gmail.com", "1254ss",1)

print(user1.id_no)
print(user1.name)
print(user1.e_mail)
print(user1.password)
print(user1.level)


