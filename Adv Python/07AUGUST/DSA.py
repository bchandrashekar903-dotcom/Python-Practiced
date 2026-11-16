'''           Stack Data structure     '''
class Stack:
    def __init(self):
        self.st = []
    def is_empty(self):
        return len(self.st) == 0
    def push(self,data):
        self.st.append(data)
    def pop(self):
        self.st.pop()
    def size(self):
        return len(self.st)
    def peek(self):
        return self.st[-1]
    def display(self):
        print(self.st)
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.display()
s.pop()
s.display()