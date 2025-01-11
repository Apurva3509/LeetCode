# The idea is to maintain a hashmap of length = capacity, store the key as key of hashmap
# and value will be a pointer to a nod ein a dounle LL storing the inputs. 
# In the double LL we will keep the left most node which is LRU and right most node as the recently used
# This will be acheived just by swapping the nodes as we get a function with that key

# Node class for 2x LL
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {} # map the key to NODES

        # Left = LRU, Right = most recent
        self.left, self.right = Node(0, 0), Node(0, 0)  
        self.left.next, self.right.prev = self.right, self.left

    # Lets say we have a double linked-list: leftnode <---> node <---> right node
    # now to remove the node we can just move prev aka leftnode to point to right of node and mkae the right node point to left node

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    # Lets say we have a double linked-list: leftnode <---> rightnode <---> 
    # Now we want to insert in between we can do the following:
    # 1) prev.next to the new node
    # 2) leftnode.next to right
    # 3) newnode.prev to left
    # 4) right.prev = newnode

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            # when we use get function the node becomes the most recently used
            # to swap that in our LL we can remove it from left and insert at right
            self.remove(self.cache[key]) 
            self.insert(self.cache[key])
            return self.cache[key].val # cache[key] is storing the pointer so we do .val to return value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key]) 
        self.cache[key] = Node(key, value) # now the hashmap has a pointer to this node
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove and delete the LRU 
            # remove from LL and delete the LRU from the hashmap
            lru = self.left.next # self.left.next will always be the LRU
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)