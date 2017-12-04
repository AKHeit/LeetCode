#
# Lengthy Docstring about Python Rules
#

"""
- help(object/class) will get the description and docstring u
- q exits the help menu
- ctrl + l clears the terminal
- type(object) will report back a class
- print(object) will specify object and it's hex address
- help(object/class) will show documentation of said class
"""


#
# Define Classes
#

# Define the binary treen node object
class TreeNode(object):
    def __init__(self,value):
        self.val   = value
        self.left  = None
        self.right = None

# Tree object
class Tree(object):
    def __init__(self,value,max_depth):
        length        = 2**max_depth - 1
        self.list     = [None] * 63
        self.depth    = 0
        self.list[0]  = TreeNode(value)
    
    def insert_children(self,children):
        # check that values has the correct length
        if len(children) != (2**(self.depth + 1)):
            print("tree updating list of children has incorrect length")
            raise

        # update the parents/children
        offset = 2**(self.depth + 1) - 2 
        for ind in range(2 ** self.depth):
            # sorting indices
            ind_p  = offset + ind:
            ind_li = 2*ind + 1
            ind_ri = 2*ind + 2
            # updating parents
            self.list[ind_p].left  = children[ind_l]
            self.list[ind_p].right = children[ind_r]
            # updating children
            ind_left = 2*ind_p + 1
            ind_right= 2*ind_2 + 2
            if TreeNode(children[ind_l]) != None:
                self.list[ind_left]  = TreeNode(children[ind_l])
            if TreeNode(children[ind_r])!= None:
                self.list[ind_right] = TreeNode(children[ind_r])   

    def print(self):
        value_list = [None]* len(self.list)
        for i in range(len(self.list)):
            node = self.list[i]
            if node != None:
                value_list = node.val
        print("Tree values in list format is")
        print(value_list)



# testing code
def test():
    # test tree creation and insertion
    t1 = Tree(1,4)
    t2 = Tree(2,4)
    print(t1)
    return [] 



   

    


if __name__== "__main__":
    test()







