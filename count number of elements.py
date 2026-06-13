class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
s=stack()
n=int(input("enter the range of elemnts:"))
for i in range(n):
    num=int(input("Enter the elements:"))
    s.push(num)
    print("Total elements:",len(s.items))