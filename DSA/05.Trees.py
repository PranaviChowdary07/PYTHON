class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level 

    def print_tree(self):
        spaces = ' '*self.get_level()*4
        prefix = spaces+"|__" if self.parent else " "
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


    def add_child(self,child):
        child.parent = self
        self.children.append(child)

def build_tree():
    root = TreeNode("Tollywood")

    heroin = TreeNode('heroins')
    heroin.add_child(TreeNode('Samantha'))
    heroin.add_child(TreeNode('Shreya'))
    heroin.add_child(TreeNode('Anushka'))
    heroin.add_child(TreeNode('Pooja'))

    hero = TreeNode('hero')
    hero.add_child(TreeNode('Ram'))
    hero.add_child(TreeNode('Raviteja'))
    hero.add_child(TreeNode('Maheshbabu'))
    hero.add_child(TreeNode('Nani'))

    comedian = TreeNode('comedian')
    comedian.add_child(TreeNode('Venu'))
    comedian.add_child(TreeNode('Brahmanandan'))
    comedian.add_child(TreeNode('Ali'))
    comedian.add_child(TreeNode('Vennela kishore'))

    root.add_child(heroin)
    root.add_child(hero)
    root.add_child(comedian)
    root.print_tree()

if __name__ == '__main__':
    build_tree()

    """ 
     OUTPUT:
      
       Tollywood   -->ROOT NODE
   |__heroins      IF parentnode these come child nodes/--->CHILD NODE these come leafnodes
      |__Samantha
      |__Shreya
      |__Anushka
      |__Pooja
   |__hero    -->CHILD NODE
      |__Ram
      |__Raviteja
      |__Maheshbabu
      |__Nani
   |__comedian   -->CHILDNODE
      |__Venu
      |__Brahmanandan
      |__Ali
      |__Vennela kishore """