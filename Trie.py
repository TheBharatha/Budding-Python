class Trie:

    def __init__(self):
        self.trieStack = list()

    def insert(self, word):
        self.trieStack.append(word)

    def search(self, word):
        return(word in self.trieStack)
        

    def startsWith(self, prefix):
        found = False
        for word in self.trieStack:
            if str(word).startswith(prefix):
                found = True
                break
        return(found)

if __name__ == "__main__":
    obj = Trie()
    obj.insert('sword')
    param_2 = obj.search('word')
    print(param_2)
    param_3 = obj.startsWith('sw')
    print(param_3)