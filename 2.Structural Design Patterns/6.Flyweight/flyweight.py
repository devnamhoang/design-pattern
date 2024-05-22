from typing import List

class TreeType:
    name: str
    color: str
    texture: str
    
    def __init__(name, color, texture):
        pass
    
    def draw(canvas, x, y):
        # 1. Create a bitmap of a given type, color & texture.
        # 2. Draw the bitmap on the canvas at X and Y coords.
        pass

# Flyweight factory decides whether to re-use existing
# flyweight or to create a new object.
class TreeFactory:
    treeTypes: List[TreeType]
    
    def getTreeType(self, name, color, texture):
        type = self.treeTypes.find(name, color, texture)
        if (type == None):
            type = TreeType(name, color, texture)
            self.treeTypes.append(type)
        return type

# The contextual object contains the extrinsic part of the tree
# state. An application can create billions of these since they
# are pretty small: just two integer coordinates and one
# reference field.
class Tree:
    x: int
    y: int
    type: TreeType
    def __init__(x, y, type):
        pass
    def draw(self, canvas):
        type.draw(canvas, self.x, self.y)

# The Tree and the Forest classes are the flyweight's clients.
# You can merge them if you don't plan to develop the Tree
# class any further.
class Forest:
    trees: List[Tree]

    def plantTree(self, x, y, name, color, texture):
        type = TreeFactory.getTreeType(name, color, texture)
        tree = Tree(x, y, type)
        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)