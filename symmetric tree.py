def isSymmetric(self, root):
    
        if not root:
            return True

        def isMirror(tree1, tree2):
            if not tree1 or not tree2:
                return tree2 == tree1
            if tree1.val != tree2.val:
                return False

            return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)

        return isMirror(root.left, root.right)
