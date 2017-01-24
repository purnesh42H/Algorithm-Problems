from queue import *

class Animal:
    dogs = None
    cats = None
    lastAnimal = 0

    def enqueue(self, type):
        lastAnimal = self.lastAnimal + 1
        if type == 'dog':
            if self.dogs == None:
                self.dogs = Dog(lastAnimal)
            else:
                self.dogs.enqueue(lastAnimat)
        elif type == 'cat':
            if self.cats == None:
                self.cats = Cat(lastAnimal)
            else:
                self.cats.enqueue(lastAnimal)

        self.lastAnimal = lastAnimal

    def dequeueAny(self):
        if self.cats == None and self.dogs == None:
            return None
        elif self.cats == None:
            return self.dogs.dequeue()
        elif self.dogs == None:
            return self.cats.dequeue()
        else:
            if self.dogs.peek() > self.cats.peek():
               return self.cats.dequeue()
            else:
               return self.dogs.dequeue()

    def dequeueDog(self):
        return self.dogs.dequeue()

    def dequeueCat(self):
        return self.cats.dequeue()

class Dog():
    dogQueue = None

    def __init__(self, data):
        self.dogQueue = MyQueue(data)

    def dequeue(self):
        return Dog(self.dogQueue.delete())

    def enqueue(self, data):
        self.dogQueue.insert(data)

    def peek(self):
        return self.dogQueue.peek()
                

class Cat():
    catQueue = None

    def __init__(self, data):
        self.catQueue = MyQueue(data)

    def dequeue(self):
        return Cat(self.catQueue.delete())

    def enqueue(self, data):
        self.catQueue.insert(data)

    def peek(self):
        return self.catQueue.peek()
