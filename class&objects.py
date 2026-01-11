#FIRST CODE IN CLASS

# class faculty:
#     def putdata(self):  
#         self.id=int(input("enter the faculty id: "))
#         self.name=input("enter the name: ")
#         self.salary=float(input("enter the faculty salary: " ))

#     def display(self):
#         print("faculty id :",self.id)
#         print("faculty name",self.name)
#         print("faculty salary",self.salary)
# a=faculty()#objects
# a.putdata()#objects        
# a.display()#objects
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

a = Node(5)
b = Node(7)
c = Node(2)
a.next = b
b.next = c
head = a

print(head.data)
print(head.next.data)
print(head.next.next.data)

