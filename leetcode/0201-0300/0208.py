class treeNode:
    def __init__(self, x):
        self.val = x
        self.child = []
        
class Trie:
    root = treeNode("|")
        
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = treeNode("|")
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for c in word:
            flag = False
            for n in current.child:
                if n.val == c:
                    flag = True
                    current = n
                    break
            if flag:
                continue
            else:
                current.child.append(treeNode(c))
                current = current.child[-1]
        for n in current.child:
            if n.val == "#":
                return
        current.child.append(treeNode("#"))

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for c in word:
            flag = False
            for n in current.child:
                if n.val == c:
                    flag = True
                    current = n
                    break
            if flag:
                continue
            else:
                return False
        for n in current.child:
            if n.val == "#":
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for c in prefix:
            flag = False
            for n in current.child:
                if n.val == c:
                    flag = True
                    current = n
                    break
            if flag:
                continue
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
