import random
class User:
    def __init__(self, name, status):
        self.user_name = name
        self.status = status
        with open('file/Users_id',"r") as f:
            data = f.read().split('\n')
        self.id = random.randint(0, 2000000000)
        self.count_pisem = 0
        while True:
            a = 0
            for i in range(len(data)):
                if data[i] == str(self.id)+" "+self.user_name + " " + self.status:
                    a = 1
                    break
            if a == 0:
                break
            else:
                self.id = random.randint(0, 2000000000)

        with open('file/Users_id', "w") as f:
            data.append(str(self.id) + " " + self.user_name + " " + self.status)
            for i in range(len(data)):
                f.write(str(data[i])+"\n")
    def info (self):
        print("id_user: ", self.id)
        print("name: ", self.user_name)
        print("count_pisem: ", self.count_pisem)
    def message_to (self, id_consider, content):
        name = ""
        with open('File/Users_id', "r") as f:
            data = f.read().split('\n')
            datas=[]
            for i in range(len(data)):
                if(data[i]!=""):
                    data[i]=data[i].split()
            for i in range(len(data)):
                if(i%2==1):
                    datas.append(data[i])
        print(datas)
        for i in range(len(datas)):
            if datas[i][0] == id_consider:
                name = datas[i][1]
        with open(f'Messaege_to/{name}.txt',"w") as f:
            f.write(content)
