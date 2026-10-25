class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = Node(key, val)
        if self.root:
            curr = self.root
            prev = None
            while curr:
                if key < curr.key:
                    prev = curr
                    curr = curr.left
                elif key > curr.key:
                    prev = curr
                    curr = curr.right
                else:
                    curr.val = val
                    return
            if key < prev.key:
                prev.left = newNode
            else:
                prev.right = newNode
        else:
            self.root = newNode
        
        return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1
    def getMin(self) -> int:
        curr = self.root
        prev = None
        while curr:
            if curr.left:
                curr = curr.left
            else:
                return curr.val
        return -1
    def getMinKeyVal(self, root : Node) -> int:
        curr = root
        prev = None
        while curr:
            if curr.left:
                curr = curr.left
            else:
                return (curr.key,curr.val)
        return (-1, -1)


    def getMax(self) -> int:
        curr = self.root
        prev = None
        while curr:
            if curr.right:
                curr = curr.right
            else:
                return curr.val
        return -1
    def remove(self, key : int) -> None:
        self.root = self.remove1(self.root, key)

    def remove1(self, root : Node, key: int) -> Node:
        curr = root
        if not curr:
            return None
        
        if key > curr.key:
            curr.right = self.remove1(curr.right, key)
        elif key < curr.key:
            curr.left = self.remove1(curr.left, key)
        else:
            if not curr.left:
                curr = curr.right
            elif not curr.right:
                curr = curr.left
            else:
                minKey, minVal = self.getMinKeyVal(curr.right)
                curr.key, curr.val = minKey, minVal
                curr.right = self.remove1(curr.right, minKey)
        return curr
        """curr = self.root
        #prev = None
        while curr:
            if key == curr.key:
                #prev = curr
                break
                
            elif key < curr.key:
                #prev = curr
                curr = curr.left
            else:
                curr = curr.right
        old_node = curr
        if curr.right:
            curr = curr.right
        prev = None
        while curr.left:
            prev = curr
            curr = curr.left
        if old_node.key != curr.key:
            old_node.key = curr.key
            old_node.val = curr.val
        if prev:
            prev.left = None
        else:
            old_node.right = None
        #curr.key, curr.val = None, None
        #curr = None
        return
        """

        
    def getInorderKeys(self) -> List[int]:
        
        in_keys = []
        root = self.root
        
        def getInorderKeys1(root : Node, in_keys : List[int]) -> List[int]:
            if not root:
                return in_keys

            in_keys = getInorderKeys1(root.left, in_keys)
            in_keys.append(root.key)
            in_keys = getInorderKeys1(root.right, in_keys)

            return in_keys
        in_keys = getInorderKeys1(root, in_keys)
        return in_keys
