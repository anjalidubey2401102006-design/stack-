class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
    def pop(self):
        return self.items.pop()
s=stack()
num=input("enter a number:")
for i in num:
    s.push(i)
reverse=" "
while len(s.items)>0:
    reverse=reverse+s.pop()
print("reversed number:",reverse)