

class Stack:
    """Stack objecti"""
    try:
        def __init__(self):
            self.stack = []
        
        def isEmpty(self):
            """Bo`sh ekanligini tekshirish"""
            return len(self.stack) == 0
        
        def push(self, data):
            """Elemnt qo`shish"""
            self.stack.append(data)
            return True
        
        def pop(self):
            """Elementni sug`irib olish yoki(o`chirib yuborish)"""
            if self.isEmpty():
                return "Stack is Empty"
            else:
                self.stack.pop()
                return True
        def peek(self):
            """Eng oxirgi elementni ko`rish"""
            if self.isEmpty():
                return "Stack is Empty"
            else:
                return self.stack[-1]

        def size(self):
            """Uzunligini o`lchash"""
            return len(self.stack)

    except Exception as error:
        print(f"Error!:{error}")

stack = Stack()
print("Is stack empty:", stack.isEmpty())

stack.push(1)
stack.push(2)
stack.push(3)
print("Is stack empty:", stack.isEmpty())
print("Stack size:", stack.size())
print("Top element:", stack.peek())

print("Popped element:", stack.pop())
print("Stack size:", stack.size())
print("Top element:", stack.peek())
