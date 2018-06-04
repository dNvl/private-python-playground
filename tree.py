# Let's build a tree

class mLeaf:
    left = None
    right = None
    parent = None
    value = None
    def __init__(self, parent, leafVal):
        print('Created leaf with {}'.format(leafVal))
        if(leafVal != None):
            self.value = int(leafVal)
            self.parent = parent

        return self;

def insertLeaf(preLeaf, leafVal):
    if(preLeaf.value == None):
        preLeaf.value = leafVal
    else:
        if(preLeaf.value <= leafVal):
            # check left
            if(preLeaf.left == None):
                preLeaf.left = mLeaf(leafVal)
            else:
                insertLeaf(preLeaf.left, leafVal)
        else:
            # check right
            if(preLeaf.right == None):
                preLeaf.right = mLeaf(leafVal)
            else:
                insertLeaf(preLeaf.right, leafVal)

def traverse(leaf):
    print("do.")

# Now build a tree
root = mLeaf(None, 0)
l1 = insertLeaf(myT, root, 1)
l2 = insertLeaf(myT, l1, 3)
l3 = insertLeaf(myT, l2, 7)
l4 = insertLeaf(myT, l3, 4)