class BSTNode():
    def __init__(self,key,val=None):
        self.key=key
        self.value=val
        self.left=None
        self.right=None
        self.parent=None

def find(root,key):
    tmp = None
    while root != None:
        if root.key == key:
            return root
        elif key < root.key:
            tmp = root.key
            root = root.left
        else:
            root = root.right

    return None

def insert(root: BSTNode, newKey, newVal=None):
    p = root
    while p != None:
        if p.key == newKey:
            return root
        elif newKey > p.key:
            if p.right == None:
                q = BSTNode(newKey,newVal)
                p.right = q
                q.parent = p
                return root
            p = p.right
        else:
            if p.left == None:
                q = BSTNode(newKey,newVal)
                p.left = q
                q.parent = p
                return root
            p = p.left
    
    q = BSTNode(newKey,newVal)
    return q
    
def remove(root: BSTNode, keyToRem):
    q = find(root, keyToRem)
    if q == None: return root

    if q.right != None and q.left != None: #dwoje dzieci
        # szuka nastepnika (istnieje i nie ma lewego dziecka)
        qNext = BSTNext(q)
        #zamienia dane w q
        q.value = qNext.value
        q.key = qNext.key
        #przepina wskazniki pomiedzy qNext oraz usuwa wskazniki z qNexT
        p = qNext.parent
        child = qNext.right

        qNext.parent = None
        qNext.right = None

        if p.right == qNext:
            p.right = child
        else:
            p.left = child

        if child == None: return root #nastepnik nie mial dzieci
        child.parent = p

        return root

    elif q.right == None and q.left == None: #lisc
            p = q.parent
            if p.left == q: p.left = None
            else: p.right = None
            q.parent = None

    else: #jedno dziecko
        p = q.parent
        child = q.right if q.right != None else q.left

        if p.right == q:
            p.right = child
        else:
            p.left = child

        child.parent = p
        q.parent = None
        q.right, q.left = None, None

    return root

def BSTPrev(v: BSTNode): #poprzednik czyli mniejsza od aktualnej
    if v.left != None:
        v = v.left
        while v.right != None:
            v = v.right
        
        return v
    
    else:
        currKey = v.key
        v = v.parent

        # jezeli v.parent==None to
        # v nie ma nastepnika
        if v == None: return None
    
        prevV = v
        v = v.parent

        while v!= None:
            if prevV.key != v.right.key: break
            prevV = v
            v = v.parent
        
        # jezeli mielismy najmniejszy mozliwy key to nie ma nastepnika
        if prevV.key > currKey: return None
        return v

def BSTNext(v: BSTNode):
    if v.right != None:
        v = v.right
        while v.left != None:
            v = v.left
        
        return v
    else:
        currKey = v.key
        v = v.parent

        # jezeli v.parent==None to
        # v nie ma nastepnika
        if v == None: return None

        prevV = v
        v = v.parent

        while v!= None:
            if prevV.key != v.left.key: break
            prevV = v
            v = v.parent
        
        # jezeli mielismy najwieszky mozliwy key to nie ma nastepnika
        if prevV.key < currKey: return None
        return prevV
        
def BSTMax(root: BSTNode):
    while root.right!=None:
        root = root.right
    return root

def BSTMin(root: BSTNode):
    while root.left!=None:
        root = root.left
    return root


####################################
def print_breadth_first(tree):
  if tree is None:
    print('Empty')
    return

  children = [tree]
  while len(children) > 0:
    _children = []
    
    for node in children:
      print(node.key, end=' ')
      if node.left is not None:
        _children.append(node.left)
      if node.right is not None:
        _children.append(node.right)

    print()
    children = _children 


def print_node(node):
  print(f'key: {node.key}')

  if node.left is not None:
    print(f'left: {node.left.key}')
  else:
    print('left: None')

  if node.right is not None:
    print(f'right: {node.right.key}')
  else:
    print('right: None')

tree = BSTNode(20)

tree = insert(tree, 10)
tree = insert(tree, 27)

tree = insert(tree, 5)
tree = insert(tree, 15)
tree = insert(tree, 13)

tree = insert(tree, 22)
tree = insert(tree, 30)
tree = insert(tree, 28)
tree = insert(tree, 35)
tree = insert(tree, 40)

print_breadth_first(tree)

# lisc
print()
tree = remove(tree, 5)
print_node(find(tree, 10))

# 1 dziecko
print()
tree = remove(tree, 15)
print_node(find(tree, 10))

# 2 dzieci
print()
tree = remove(tree, 30)
print_node(find(tree, 27))

print()
tree = remove(tree, 35)
print_node(find(tree, 40))

print()
print_breadth_first(tree)