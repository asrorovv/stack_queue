class Queue:
    """Queue objecti"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Bo`sh ekanligini tekshirish"""
        return self.items == []

    def enqueue(self, item):
        """Elemnt qo`shish, navbatning orqa (oxiri) qismiga element qo‘shish"""
        self.items.append(item)

    def dequeue(self):
        """Elementni sug`irib olish yoki(o`chirib yuborish), navbatning old qismidan (boshidan) elementni olib tashlash va qaytarish"""
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        """Eng birinchi elementni ko'rish, Navbatning oldingi qismidagi elementni olib tashlamasdan ko'rish"""
        if not self.is_empty():
            return self.items[0]

    def size(self):
        """Navbatdagi elementlar sonini qaytarish"""
        return len(self.items)

queue = Queue()
print("Is queue empty:", queue.is_empty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Is queue empty:", queue.is_empty())
print("Queue size:", queue.size())
print("Front element:", queue.peek())

print("Dequeued element:", queue.dequeue())
print("Queue size:", queue.size())
print("Front element:", queue.peek())
