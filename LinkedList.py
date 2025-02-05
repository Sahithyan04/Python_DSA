
class Node:
    def __init__(self,data):
        self.data = data 
        self.nextpoint = None
class LList:
    def __init__(self):
        self.head = None
    def Start(self , data):
        new_node = Node(data)
        new_node.nextpoint = self.head
        self.head = new_node
    def End(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        temp = self.head
        while temp.nextpoint:
            temp = temp.nextpoint
        temp.nextpoint = new_node
    def Search(self, Key):
        if self.head == None:
            print(" == Empty List == ")
            return
        else:
            temp = self.head
            while temp :
                if temp.data == Key:
                    print("Key is in List")
                    return

                temp = temp.nextpoint
            print("Key not in list")
            return
    def MiddleEnd(self,Key,data):
        new_node = Node(data)
        if self.head == None:
            print(" ==List Empty == ")
        else:
            temp = self.head
            while temp:
                if temp.data == Key:
                    new_node.nextpoint = temp.nextpoint
                    temp.nextpoint = new_node
                    print("Key inserted")
                    return
                temp = temp.nextpoint
            print("Key not found")
            return
    def MiddeleStart(self, Key, data):
        new_node = Node(data)
        if self.head == None:
            print(" == List Empty == ")
        else:
            temp =self.head
            while temp:
                if temp.nextpoint.data == Key:
                    new_node.nextpoint = temp.nextpoint
                    temp.nextpoint = new_node
                    print("Key inserted at Node")
                    return
                temp =temp.nextpoint
            print("Key not found")
            return
    def Update(self, Key,data):
        new_node = Node(data)
        if self.head == None:
            print(" == Empty List == ")
            return
        else:
            temp = self.head
            while temp :
                if temp.data == Key:
                    temp.data = data
                    return

                temp = temp.nextpoint
            print("Key not in list")
            return
        
    def DeletionAtstart(self):
        if self.head == None:
            print("== Empty list ==")
        else:
            temp = self.head
            self.head = self.head.nextpoint
            temp = None
    def DeletionAtEnd(self):
        if self.head == None:
            print(" ==EmptyList== ")
        else:
            temp = self.head
            while temp.nextpoint.nextpoint:
                temp = temp.nextpoint
            temp.nextpoint = None

    def DeletionAtMid(self, Key):
        if self.head == None:
            print("==Empty List==")
            return
         
        if self.head.data == Key:
            self.DeletionAtstart()
            return
        temp = self.head

        while temp.nextpoint :
            
            if temp.nextpoint.data == Key:
                temp.nextpoint = temp.nextpoint.nextpoint
                return
            temp = temp.nextpoint

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.nextpoint
            current.nextpoint = prev
            prev = current
            current = next_node
        self.head = prev

    def res(self):
        temp = self.head
        while temp:
            print(temp.data,end = "->")
            temp = temp.nextpoint
           
        return
## LIST VALUES -----
lst1 = LList()
lst1.Start(30)
lst1.End(10)
lst1.Start(18)
lst1.Start(73)
lst1.End(60)
lst1.Start(65)
# lst1.Start(77)

#LIST FUNCTIONS -----


#lst1.Search(12)
# lst1.MiddleEnd(3,30)
# lst1.MiddeleStart(30,40)
# lst1.Update(30,97)
# lst1.DeletionAtEnd()
# lst1.DeletionAtMid(65)
lst1.res()
lst1.reverse()
print("\n")
lst1.res()
print("\n")