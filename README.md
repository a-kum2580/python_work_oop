the video explaining number two of the presentation work
class StudentQueue:
    def _init_(self):
        self.queue = []

    def enqueue(self, student):
        self.queue.append(student)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage:
student_queue = StudentQueue()

# Students join the queue
student1 = {"name": "Alice", "course": "Computer Science"}
student2 = {"name": "Bob", "course": "Mathematics"}
student3 = {"name": "Charlie", "course": "Physics"}
student_queue.enqueue(student1)
student_queue.enqueue(student2)
student_queue.enqueue(student3)

# Students get served
student1 = {"name": "Alice", "course": "Computer Science"}
student2 = {"name": "Bob", "course": "Mathematics"}
student3 = {"name": "Charlie", "course": "Physics"}
student_queue.enqueue(student1)
student_queue.enqueue(student2)
student_queue.enqueue(student3)

# Students get served
served_student = student_queue.dequeue()
print(f"Served student: {served_student['name']}")

# Check if the queue is empty
if student_queue.is_empty():
    print("The queue is empty.")
else:
    print("The queue is not empty.")

# Determine the current size of the queue
queue_size = student_queue.size()
print(f"The current size of the queue is: {queue_size}")
