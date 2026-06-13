class stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print(item,"pushed into stack")
    def pop(self):
        if len(self.stack)==0:
            print("stack underflow! stack is empty")
        else:
            print("popped element:",self.stack.pop())
    def peek(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            print("top element:",self.stack[-1])
    def display(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:ss
            print("stack elements:",self.stack)
s=stack()
while True:
    print("\n----STACK MENU---")
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    choice=int(input("Enter your choices:"))
    if choice==1:
        item=input("Enter element to push:")
        s.push(item)
    elif choice==2:
        s.pop()
    elif choice==3:
        s.peek()
    elif choice==4:
        s.display()
        print("Program terminated")
        break
    else:
        print("Invalid choice!")