class RouteTrieNode(object):
    def __init__(self):
        self.child = {}
        self.handle = None

    def insert(self, path_block):
        if path_block not in self.child:
            self.child[path_block] = RouteTrieNode()
        else:
            pass

class RouteTrie(object):

    def __init__(self, rootHandle):
        self.root = RouteTrieNode()
        self.handle = rootHandle

    def insert(self, path, handle):
        temp = self.root
        for block in path:
            temp.insert(block)
            temp = temp.child[block]
        temp.handle = handle

    def find(self, path):
        temp = self.root
        for block in path:
            if block not in temp.child:
                return None
            temp = temp.child[block]
        return temp.handle

class Router:
    def __init__(self, rootHandle, non_found):
        self.router = RouteTrie(rootHandle=rootHandle)
        self.non_found = non_found

    def add_handler(self, raw_path, handle):
        path = self._split_path(raw_path)
        self.router.insert(path=path, handle=handle)

    def lookup(self, input_path):
        path = self._split_path(input_path)

        if len(path) == 0:
            return self.router.handle

        finding = self.router.find(path=path)

        if finding is None:
            return self.non_found
        else:
            return finding

    @staticmethod
    def _split_path(input_path):
        temp = input_path.split(sep='/')
        return [element for element in temp if element != '']



router = Router("root handler", "not found handler") 
router.add_handler("/home/about", "about handler") 


print(router.lookup("/")) 
# Output:-root handler
print(router.lookup("/home")) 
# Output:-not found handler
print(router.lookup("/home/about")) 
# Output:-about handler
print(router.lookup("/home/about/")) 
# Output:-about handler
print(router.lookup("/home/about/me")) 
# Output:-not found handler
