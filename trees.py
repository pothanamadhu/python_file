class Node:
      def __init__(self,data):
            self.left=None
            self.data=data
            self.right=None
"""
if(root==null)
  {
     Node node=new Node();
     node.data=value;
     node.left=null;
     node.right=null;
     root=node;
 }
 else if(root.data>value)
      root.left=Insert(root.left,value);
  else if(root.data<value)
      root.right=Insert(root.right,value);

  return root;
}
"""
class Tree:
      def createNode(self,data):
            return Node(data)
      def insert(self,node,data):
            if node is None:
                  return self.createNode(data)
            else:
                  if data<node.data:
                        node.left=self.insert(node.left,data)
                  else:
                        node.right=self.insert(node.right,data)
            return node
      def inorder(self,root):
            if root is not None:
                  self.inorder(root.left)
                  print(root.data)
                  self.inorder(root.right)
tree=Tree()
root=tree.createNode(5)
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)
tree.inorder(root)
