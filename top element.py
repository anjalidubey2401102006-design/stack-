class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
    def peek(self):
        return self.items[-1]
s=stack()
n=int(input("How many elements do you want to enter?\n"))
for i in range(n):
    num=int(input("Enter numbers:\n"))
    s.push(num)
print("Top element:",s.peek())