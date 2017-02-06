class Queue:
    first = []
    second = []

    def insert(self, data):
        while len(self.second) > 0:
            self.first.append(self.second.pop())
        self.first.append(data)

    def delete(self):
        while len(self.first) > 0:
            self.second.append(self.first.pop())
        return self.second.pop()
    
        
