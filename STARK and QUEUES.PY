#what is the stack

#STACK is the linear data structure the followa the LIFO(last in first out)
#the last element insert is the first tobe popped out.

#BASIC OPERATION OF THE STACK
#push  (to insart the element)Ex. st.push(5)
#pop   (to remov the first element insart)Ex. st.pop()
#top   (to axces the element )Ex. st.top()
#isEmpty (to chack the stack is the empty or not)Ex. 
#isFull (to stack is full or not )

#LIST IMPLITAION OF THE STACK

#BY BASIC
# ST=[]
# ST.append(5)
# ST.append(3)
# ST.append(2)
# ST.append(4) 
# print(ST[-1])      #this is the important

# print(ST)

#BY THE USEING THE OBJECT OR THE OPPS

# class stack:
#     def _init_(self):
#         self.ST=[]
#     def push(self ,x):
#         self.ST.append(x)    
#     def pop(self):
#         if len (self.ST)  ==0:
#             return -1
#         x=self.ST[-1]
#         self.ST.pop()
#         return x    
#     def top(self):
#         if len (self.ST)  ==0:
#             return -1
#         return self.ST[-1]
#     def size(self):
#         return 
# stack=stack()
# stack.Push(4)
# stack.Push(5)
# stack.Push(3)
# stack.Push(9)

# print(stack.pop())

#how to implementation of the stack using the linked list

# class node:
#     def _init_(self,data):
#         self.data=data
#         self.next=None

# class staack:
#     def _init_(self)   :
#         self.top  =None
# class push( self ,x):
#     if self.top is None:
#         top=None(x)
#         return
#     else:
#         newnod=Node(x)
#         newNode.next=self.top
#         top=newNode



#appliction of the stack 
  #recursion / backtracking /dynamic programing
  #undo / redo
  #lru-cache
  #memory-management


  #INTRODUCIONT TO THE QUEUE DATA STRUCTURE

    #queue is a linear data sture that follow FLFO(first in first out)
    #so the first element insted is the first to be popped out
    #the meaning of the queue is line or we can represant by the pipe

#same basic operation in the queqe
   #push
   # pop
   # front 
   # isEnpty
   # isfull 


#list implementation of queue

x=0
class queue:
    def _init_(self):
        self.q=[]
        self.front =-1


    def put(self,x):
        if self.front == -1:  
          self.front=0  
        self.q.append(x)    

    def pop(self): 
        if len(self.q)==0:
            return -1
        X=self.q[self.front]
        self.front+=1
        if self.front==len(self.q):
            self,front=-1
            self.q=[]
        return x  
      
    def Front(self):
        if len(self.q)==0:
            return -1
        return self.q[self.front]
    

    def size (self):
        if self.front==-1:
            return-1
        return self.q[self.front]
    def size (self):
        if self.front==-1:
            return 0
        return len(self.q)- self.front
    
queue=queue()    
queue.put(5)
queue.put(4)
queue.put(3)    
queue.put(1)

print(queue.getFront())        






