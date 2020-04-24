class stack:
    
    def __init__(self):
        self.bucket = []

    def push(self, item):
        self.bucket.append(item)

    def pop(self):
        return self.bucket.pop()

    def size(self):
        return len(self.bucket)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.bucket[self.size() - 1]

    def __str__(self):
        return str(self.bucket)