class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print("stack contents :",s.items)