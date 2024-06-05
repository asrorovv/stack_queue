class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    """Queue objecti"""
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        """Bo`sh ekanligini tekshirish"""
        return self.head == None

    def peek(self):
        """Eng birinchi elementni ko'rish, Navbatning oldingi qismidagi elementni olib tashlamasdan ko'rish"""
        return self.head.data

    def enqueue(self, data):
        """Elemnt qo`shish, navbatning orqa (oxiri) qismiga element qo‘shish"""
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
            self.tail = self.head
        else:
            self.tail.next = new_data
            self.tail = new_data

    def dequeue(self):
        """Elementni sug`irib olish yoki(o`chirib yuborish), navbatning old qismidan (boshidan) elementni olib tashlash va qaytarish"""
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
           self.tail = None

        return data

#bu algoritmni kitoblardan ko'rib o'rganib yozdim