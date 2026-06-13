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
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print("stack before pop: ",s.items)
removed=s.pop()
print("popped element: ",removed)
print("stack content after pop: ",s.items)