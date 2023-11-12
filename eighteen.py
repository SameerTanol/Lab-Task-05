class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == self.rear == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def size(self):
        if self.is_empty():
            return 0
        elif self.is_full():
            return self.capacity
        elif self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return (self.capacity - self.front) + (self.rear + 1)

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
            print(f"{item} enqueued to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
        else:
            item = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity
            print(f"{item} dequeued from the queue.")
            return item

my_circular_queue = CircularQueue(5)

my_circular_queue.enqueue(1)
my_circular_queue.enqueue(2)
my_circular_queue.enqueue(3)

print("Is the queue empty?", my_circular_queue.is_empty())
print("Is the queue full?", my_circular_queue.is_full())

print("Size of the queue:", my_circular_queue.size())

my_circular_queue.dequeue()
my_circular_queue.dequeue()
my_circular_queue.dequeue()

my_circular_queue.dequeue()

print("Is the queue empty?", my_circular_queue.is_empty())
