class node:
 def__init__(self,info,next=None):
 self.data=info
 self.next=next

class SinglyLinkedList:
 def __init__(self,head=None):
  self.head=head

 def insert_at_end(self,value):
  Temp = node(value)
