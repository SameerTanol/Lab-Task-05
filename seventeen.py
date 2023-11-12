class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        if len(self.queue) < self.capacity:
            self.queue.append(item)
            print(f"{item} enqueued to the queue.")
        else:
            print("Queue is full. Cannot enqueue.")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"{item} dequeued from the queue.")
            return item
        else:
            print("Queue is empty. Cannot dequeue.")

my_queue = Queue(5)

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Is the queue empty?", my_queue.is_empty())

print("Size of the queue:", my_queue.size())

my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()

my_queue.dequeue()

print("Is the queue empty?", my_queue.is_empty())
