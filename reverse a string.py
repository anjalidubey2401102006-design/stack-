class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
    def pop(self):
        return self.items.pop()
s=stack()
string=input("Enter the string:")
for ch in string:
    s.push(ch)
reverse=" "
while len(s.items)>0:
    reverse=reverse+s.pop()
print("reversed string:",reverse)