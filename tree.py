class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def printTree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.printTree()

def buildTree():
    root = TreeNode("Rock")

    #SwitchFoot
    sf = TreeNode("Switchfoot")
    sf_1 = TreeNode("Dare you to move")
    sf_2 = TreeNode("You")
    sf_3 = TreeNode("Meant to live")

    #DeathCab
    db = TreeNode("Death Cab for Cutie")
    db_1 = TreeNode("A lack of color")
    db_2 = TreeNode("I will follow you into the dark")
    db_3 = TreeNode("A movie script ending")

    root.addChild(sf)
    root.addChild(db)

    sf.addChild(sf_1)
    sf.addChild(sf_2)
    sf.addChild(sf_3)

    db.addChild(db_1)
    db.addChild(db_2)
    db.addChild(db_3)

    root.printTree()


if __name__ == '__main__':
    buildTree()
    