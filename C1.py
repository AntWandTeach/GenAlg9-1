from B1_B2 import User
class Server:
    def __init__(self, spisok):
        self.chat = spisok
        self.user_list = []
    def head_10 (self):
        b = ""
        for i in range(10):
            b+= str(self.chat[i]) + ' '
        print(b)
    def foot_10 (self):
        c = ""
        for i in range(1, 11):
            c += str(self.chat[-i]) + ' '
        print(c)


    def add_user (self, user):
        self.user_list.append(user)

server = Server([1,2,3,4,5,6,7,8,8,9,97,6,5])
a= User("Ben", "online")
server.add_user(a)
server.add_user(User("Savely", "online"))
server.add_user(User("Sacha", "offline"))
a = server.user_list[0].message_to(str(server.user_list[1].id),"lll")








y=input()

with open('file/Users_id', "r+") as f:
    f.truncate(0)



