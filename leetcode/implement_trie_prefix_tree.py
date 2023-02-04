# Q: https://leetcode.com/problems/implement-trie-prefix-tree

class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = Node()

            current = current.children[char]
        
        current.end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            if char not in current.children:
                return False
            
            current = current.children[char]
        
        return current.end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False
            
            current = current.children[char]
        
        return True