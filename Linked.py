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

    def res(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.nextpoint
           
        return

lst1 = LList()
lst1.Start(3)
lst1.End(10)
lst1.Start(1)
lst1.Start(5)
#lst1.Search(12)
lst1.MiddleEnd(3,30)
lst1.MiddeleStart(3,40)
lst1.res()
print("\n")