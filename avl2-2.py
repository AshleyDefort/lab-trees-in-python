# Cargar el dataset desde un archivo CSV
def load_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dataset.append(row)
    return dataset

# Dibujar el árbol utilizando Graphviz
def draw_tree(tree):
    dot = Digraph()

    def add_nodes_edges(node):
        if node:
            dot.node(str(node.data['name']), label=str(node.data))
            if node.left:
                dot.node(str(node.left.data['name']), label=str(node.left.data))
                dot.edge(str(node.data['name']), str(node.left.data['name']))
                add_nodes_edges(node.left)
            if node.right:
                dot.node(str(node.right.data['name']), label=str(node.right.data))
                dot.edge(str(node.data['name']), str(node.right.data['name']))
                add_nodes_edges(node.right)

    add_nodes_edges(tree.root)
    dot.render('avl_tree', format='png', view=True)

# Punto de entrada principal
if __name__ == "__main__":
    # Cargar el dataset
    dataset = load_dataset('images_dataset.csv')

    # Crear un árbol AVL y agregar los datos del dataset
    avl_tree = AVLTree()
    for data in dataset:
        avl_tree.insert(data)

    # Dibujar el árbol
    draw_tree(avl_tree)
