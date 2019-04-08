class _BSTMapIterator :
     def __init__( self, root ):
       self._theStack = Stack()
       self._traverseToMinNode( root )
     def __iter__( self ):
       return self
     def __next__( self ):
       if self._theStack.isEmpty() :
          raise StopIteration
       else :
           node = self._theStack.pop()
           key = node.key
           if node.right is not None :
             self._traverseToMinNode( node.right )
     def _traverseToMinNode( self, subtree ):
        if subtree is not None :
          self._theStack.push( subtree )
self._traverseToMinNode( subtree.left )
