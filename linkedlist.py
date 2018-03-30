'''
#basic linked list
class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
lst=[]
class link_list:
    def __init__(self):
        self.head=node()


    def insert_node(self,data):
        c=0
        global lst
        new_node=node(data)
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            c+=1
        cur_node.next=new_node
        lst.append(data)
        print('node inserted at {} position with memory address {}'.format(c,new_node))
        print(cur_node,self.head.next,self.head.next.data)


    def delete_node(self,index):
        global lst
     '''   '''if index>=self.length():
            print('Index out of range')
        elif index<0:
            print("Index value should be grtr than equal to 0")''''''
        cur_pos=0
        cur_node=self.head
        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_pos==index:
                last_node.next=cur_node.next
                print('node deleted at %d position',index)
                del lst[index]
                return
            cur_pos+=1


obj=link_list()
obj.insert_node(3)
obj.insert_node(4)
obj.insert_node(2)
obj.insert_node(1)
print(lst)
obj.delete_node(1)
print(lst)'''

'''
#STACK implementation using linked list

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

list=[]
class stack:
    def __init__(self):
        self.top=node()

    def push(self,data):
        global list
        new_node=node(data)
        if self.top.next==None:
            self.top.next=new_node
        else:
            cur_node=self.top
            new_node.next=cur_node.next
            cur_node.next=new_node
        list.insert(0,data)
        print('New node inserted into the stack')
        print("List is:",list,'top elmnt is:',self.top.next.data)


    def pop(self):
        global list
        cur_node=self.top
        if cur_node.next==None:
            print("STACK already empty")
        else:
            cur_node.next=cur_node.next.next
            print("Top node removed from STACK")
            print('Top element is:',self.top.next.data)
            del list[0]
            print('New list is:',list)


    def disp_middle(self):
        m=0
        cur_node=self.top
        if cur_node.next==None:
            print("No node present in the STACK")
        elif cur_node.next.next==None:
            print('Only single node present in the STACK')
        else:
            try:
                mid_node=cur_node
                while(cur_node.next.next!=None):
                    cur_node=cur_node.next.next
                    mid_node=mid_node.next
                    m+=1
                print('middle node of stack is: {} at {} position'.format(mid_node.next.data,m+1))
            except:
                print('middle node of stack is: {} at {} position'.format(mid_node.data,m))
              


obj=stack()
obj.push([0,1,2])
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.pop()
obj.disp_middle()
'''


'''
#QUEUE implementation using doubly liked list

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.prev=None
list=[]
class queue:
    def __init__(self):
        self.front=node()
        self.rare=node()

    def push(self,data):
        global list
        new_node=node(data)
        cur_node=self.front
        last_node=self.rare
        if cur_node.next==None:
            cur_node.next=new_node
            last_node.prev=new_node
            
        else:
            new_node.prev=last_node.prev
            last_node.prev=new_node
            new_node.prev.next=new_node

        print('NODE INSERTED SUCCESSFULL!!')
        print('Rare node is:',self.rare.prev.data)
        list.append(data)
        print('List is:',list)
        
    def pop(self):
        global list
        cur_node=self.front
        last_node=self.rare
        if cur_node.next==None:
            print('QUEUE already empty')
        elif cur_node.next==last_node.prev:
            cur_node.next=last_node.prev=cur_node.next.next
            del list[0]
            print('List is:',list)
        else:
            cur_node.next=cur_node.next.next
            cur_node.next.prev=None
            print("Node deleted from Queue",)
            del list[0]
            print('Front node is:',self.front.next.data)
            print('List is:',list)


obj=queue()
obj.push(0)
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
'''






