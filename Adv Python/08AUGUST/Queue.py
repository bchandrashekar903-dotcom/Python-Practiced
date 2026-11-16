'''      Queue DSA    
Types -> 
        1. Simple Queue -> Queue using list
        2. Circular Queue -> Queue using list but with fixed size
        3. Double Ended Queue -> Queue where element is inserted at both ends
        4. Priority Queue -> Queue where element is inserted based on priority
'''
'''Simple Queue '''
# class Queue:
#     def __init__(self):
#         self.q = []
#     def enqueue(self,data):
#         self.q.append(data)
#     def dequeue(self):
#         self.q.pop(0)
#     def display(self):
#         print(self.q)
# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.display()
# q.dequeue()
# q.display()

'''Double 
In simple queue we can add the elements only at the rear ie enqueue operation 
    and element is removed only from the front ie dequeue operation
    But when we  are using dequeue we can pop the elements either from from=nt or rear 
    and in the same way .We are going to append the vslues in both front and rear
    and we can use dequeue operation only by importibg from collections module 
    
    Ex : from collections import dequeue
'''
'''               Deque DSA                    '''
# from collections import deque
# q = deque([])
# q.append(10)
# q.append(20)
# q.appendleft(30)
# q.popleft()
# print(q)

'''               Circular queue                 '''
# class Circular_q:
#     def __init__(self,size):
#         self.size = size
#         self.q = [None]*self.size
#         self.front = -1
#         self.rear = -1

#     def enqueue(self,data):
#         if (self.rear+1)%self.size== self.front:
#             print("Queue is full")
#         elif self.front == -1:
#             self.front=self.rear=0
#             self.q[self.rear]=data
#         else:
#             self.rear=(self.rear+1)%self.size
#             self.q[self.rear] = data

#     def dequeue(self):
#         if self.front == -1:
#             print("Queue is empty")
#             return 
#         if self.front == self.rear:
#             self.front = self.rear =-1
#         self.front = (self.front+1)%self.size

#     def display(self):
#         if self.front == -1:
#             print("Queue is empty")
#             return
#         i = self.front
#         while True:
#             print(self.q[i],end = " ")
#             if i == self.rear:
#                 break
#             i = (i+1)%self.size

# q = Circular_q(5)
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)
# q.enqueue(60)
# q.dequeue()
# q.display()


'''                           Priority Queue                           '''
import heapq
priority_q = []
heapq.heappush(priority_q,3)
heapq.heappush(priority_q,2)
heapq.heappush(priority_q,1)

print(priority_q)

