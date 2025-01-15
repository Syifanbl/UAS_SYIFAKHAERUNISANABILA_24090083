class stack :
    def __init___(self):
        self.items = []
    self.items = mahasiswa 90
    def push (self,item ):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
             self.items.pop()
        else :
           print ('Data Kosong')

    def top(self):
        if not self.isEmpty():
            print(self.items[-1])
        else :
            print('Data Kosong')

    def isEmpty(self):
        return len(self.items) == 0

