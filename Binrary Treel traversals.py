import random
class node():
    def __init__(self,val):
        self.val = val
        self.r = None
        self.l = None
        print "Node created : ",val
class btree():

    def __init__(self):
        self.head = None
        self.q=queue()
    
    def add(self,val):
        if self.head == None:
            self.head = node(val)
            print "No head,",
            print "Created",val,"as Head"
        else:
            self.searchandadd(self.head,val)
            
    def searchandadd(self,cur,val):
        if cur.val >= val:
            if cur.l == None:
                cur.l = node(val)
            else:
                self.searchandadd(cur.l,val)
        else:
            if cur.r == None:
                cur.r = node(val)
            else:
                self.searchandadd(cur.r,val)
                
    def preorder(self,cur):     # ROOT, LEFT, RIGHT
        if cur != None:
            print cur.val,"->",
            self.preorder(cur.l)
            self.preorder(cur.r)
            
    def postorder(self,cur):    # LEFT, RIGHT, ROOT
        if cur != None:
            self.postorder(cur.l)
            self.postorder(cur.r)
            print cur.val,"->",

    def inorder(self,cur):      # LEFT, ROOT, RIGHT
        if cur != None:
            self.inorder(cur.l)
            print cur.val,"->",
            self.inorder(cur.r)

    def levelorder(self):
        self.q.push(self.head)
        cur=self.q.pop()
        print cur.val,"->",
        while cur != None :             
            if cur.l!=None:
                print cur.l.val,"->",
                self.q.push(cur.l)
            if cur.r!=None:
                print cur.r.val,"->",
                self.q.push(cur.r)
            cur=self.q.pop()

    def inor(self,cur):
        s = stack()
        while cur != None or s.head !=None:
            if cur != None:
                s.push(cur)
                print "pushed ",cur.val
                cur = cur.l
            else:
                cur = s.pop()
                print "      popped ",cur.val
                cur = cur.r
    def height(self,cur):
        if cur == None:
            return 0
        else:
            return max(self.height(cur.l),self.height(cur.r))+1
                   
class queue_node():
    
    def __init__(self,val):
        self.data=val
        self.link=None
        
class queue():
    
    def __init__(self):
        self.tail = None
        self.head = None
        
    def push(self,val):         #insert in tail
        cur = queue_node(val)
        if self.tail != None:
            self.tail.link = cur
        self.tail = cur
        if self.head == None:
            self.head = cur
        
    def pop(self):		#take it from head
        if self.head!= None:
            cur = self.head
            self.head = self.head.link
            return cur.data
        else:
            return None
        
    def display(self,cur):
        if cur != None:
            print cur.data,"->",
            self.display(cur.link)

class stack_node():
    def __init__(self,val):
        self.data = val
        self.link = None
        
class stack():
    def __init__(self):
        self.head = None

    def push(self,val):
        if val == None:
            return
        cur = stack_node(val)
        cur.link = self.head
        self.head = cur

    def pop(self):
        cur = self.head
        if self.head != None:
            self.head = self.head.link
            return cur.data
        return None

    def display(self,cur):
        if cur != None:
            print cur.data,"->",
            self.display(cur.link)

b=btree()
q=queue()
s=stack()
data=[8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
print '''
             8
     4                  12
  2     6          10         14
 1 3  5  7      9    11   13    15
'''
for i in data:
    b.add(i)
    s.push(i)
print
print "HEIGHT is ",b.height(b.head)
print
print "PREORDER"
b.preorder(b.head)
print
print "INORDER"
b.inorder(b.head)
print
print "POSTORDER"
b.postorder(b.head)
print
print "LEVELORDER"
b.levelorder()
print
print "STACK"
s.display(s.head)
print
#Trying inorder traversal without recursion
print "TRIAL INOR"
b.inor(b.head)
print '''
          a
       b
    c
      d
    e
 f
g h'''
t=btree()
t.head=node('a')
t.head.l=node('b')
t.head.l.l=node('c')
t.head.l.l.r=node('d')
t.head.l.l.r.l=node('e')
t.head.l.l.r.l.l=node('f')
t.head.l.l.r.l.l.l=node('g')
t.head.l.l.r.l.l.r=node('h')
t.inor(t.head)
