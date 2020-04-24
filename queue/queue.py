class queue:
    def __init__(self):
        self.bucket = []

    def enqueue(self, item):
        self.bucket.append(item)

    def dequeue(self):
        return self.bucket.pop(0)

    def is_empty(self):
        return len(self.bucket) == 0

    def size(self):
        return len(self.bucket)
