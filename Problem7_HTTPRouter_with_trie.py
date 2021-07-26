# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler 
    
    def insert(self, path_part):
        # Insert the node as before
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler='root handler', notfound_handler='404 page not found'):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.notfound_handler = notfound_handler
    
    def insert_handler(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root

        for path_part in path_list:
            if path_part not in node.children:
                node.insert(path_part)
            node = node.children[path_part]
        
        node.handler = handler


    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for path_part in path_list:
            if path_part in node.children:
                node = node.children[path_part]
            else:
                return self.notfound_handler
        if node.handler:
            return node.handler
        else:
            return self.notfound_handler
            

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler='root handler', notfound_handler='404 page not found'):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler, notfound_handler)


    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        self.route_trie.insert_handler(path_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        if path_list == []:
            return self.route_trie.root.handler
        return self.route_trie.find(path_list)


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_parts = path.split('/')
        return [element for element in path_parts if element != '']


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/daily/blogs", "blogs handler") 

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
#root handler
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
#not found handler
print(router.lookup("/home/about")) # should print 'about handler'
#about handler
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
#about handler
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
#not found handler
print(router.lookup("/home/daily/blogs"))
#blog handler
print(router.lookup("/home/daily"))
#not found handler