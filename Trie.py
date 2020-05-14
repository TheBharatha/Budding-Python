class Trie:

    def __init__(self):
        self.trieStack = list()

    def insert(self, word):
        self.trieStack.append(word)

    def search(self, word):
        return(word in self.trieStack)
        

    def startsWith(self, prefix):
        prefixCheck = list(word for word in self.trieStack if str(word).startswith(prefix))
        return(any(prefixCheck))

if __name__ == "__main__":
    obj = Trie()
    obj.insert('nword')
    param_2 = obj.search('word')
    print(param_2)
    param_3 = obj.startsWith('sw')
    print(param_3)