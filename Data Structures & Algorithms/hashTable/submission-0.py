class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        #self.prev = None

class LinkedList:
    def __init__(self, head: Node):
        self.head = head

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashmap = [LinkedList(Node(None, None)) for i in range(capacity)]
        

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key) 
        ll = self.hashmap[index]
        curr = ll.head.next
        #print(curr)
        while curr:
            if curr.key == key:
                curr.val = value
                print("key ", key, "already present , updating value to ", value)
                print("updated linked list at index ", index, " is ")
                self.llAtIndex(index)
                return
            else:
                curr = curr.next
        
        if not curr:
            n = Node(key, value)
            prev, next = ll.head, ll.head.next
            n.next, n.prev = next, prev
            prev.next = n
            if next:
                next.prev = n
            #ll.head.next = n
        print("inserting new key, value ", key, ",", value, " at index ", index, )
        print("updated linked list at index ", index, " is ")
        self.llAtIndex(index)
        self.size += 1
        if self.size >= self.capacity // 2:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr = self.hashmap[index].head.next
        
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1   


    def remove(self, key: int) -> bool:
        index = self.hash(key)
        ll = self.hashmap[index].head
        curr = self.hashmap[index].head.next
        while curr:
            if curr.key == key:
                prev, next = curr.prev, curr.next
                prev.next = next
                if next:
                    next.prev = prev
                self.size -= 1
                print("updated linked list after removing ", key, " at index ", index, " is ")
                self.llAtIndex(index)
                return True
            else:
                curr = curr.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newhashmap = [LinkedList(Node(None, None)) for i in range(self.capacity)]
        oldhashmap = self.hashmap
        self.hashmap = newhashmap
        self.size = 0
        for ll in oldhashmap:
            if ll.head.next:
                curr = ll.head.next
                while curr:
                    self.insert(curr.key, curr.val)
                    curr = curr.next


    def hash(self, key) -> int:
        sumAscii = 0
        for l in str(key):
            #print(l)
            sumAscii += ord(l)
        #print(sumAscii)
        index = sumAscii % self.capacity
        #print(index)
        return index

    def llAtIndex(self, index:int) -> None:
        curr = self.hashmap[index].head.next
        while curr:
            print(curr.key, curr.val)
            curr = curr.next

