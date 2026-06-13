class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
    def pop(self):
        if len(self.items)==0:
            print("stack is empty")
        else:
            return self.items.pop()
s=stack()
n=int(input("How many elements do you want to enter?"))
for i in range(n):
    num=int(input("Enter the elements:\n"))
    s.push(num)
print("stack before pop:",s.items)
removed=s.pop()
print("popped element:",removed)
print("stack after pop:",s.items)