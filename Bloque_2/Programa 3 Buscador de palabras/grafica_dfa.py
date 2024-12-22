import networkx as nx
import matplotlib.pyplot as plt

# Definir la tabla de transición como un diccionario
transiciones = {
    '1': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '2': {'e': '2', 's': '6', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '3': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '7', 'o': '1', 'f': '1', 'm': '1'},
    '4': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '8', 'o': '1', 'f': '1', 'm': '1'},
    '5': {'e': '9', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '13', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '6': {'e': '2', 's': '1', 'c': '10', 'u': '1', 'l': '1', 'a': '4', 't': '11', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '7': {'e': '9', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '12', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '8': {'e': '9', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '13', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '14'},
    '9': {'e': '2', 's': '6', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '15', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '10': {'e': '2', 's': '1', 'c': '3', 'u': '16', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '7', 'o': '1', 'f': '1', 'm': '1'},
    '11': {'e': '2', 's': '1', 'c': '3', 'u': '17', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '12': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '18', 'm': '19'},
    '13': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '18', 'm': '1'},
    '14': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '20', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '15': {'e': '2', 's': '1', 'c': '21', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '16': {'e': '22', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '17': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '23', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '18': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '24', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '19': {'e': '25', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '20': {'e': '2', 's': '26', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '8', 'o': '1', 'f': '1', 'm': '1'},
    '21': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '7', 'o': '27', 'f': '1', 'm': '1'},
    '22': {'e': '2', 's': '6', 'c': '3', 'u': '1', 'l': '28', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '23': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '29', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '24': {'e': '30', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '25': {'e': '2', 's': '6', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '31', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '26': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '27': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '32', 'o': '1', 'f': '1', 'm': '1'},
    '28': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '33', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '29': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '34', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '30': {'e': '2', 's': '35', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '31': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '32': {'e': '9', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '33': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '8', 'o': '1', 'f': '1', 'm': '1'},
    '34': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '36', 'r': '8', 'o': '1', 'f': '1', 'm': '1'},
    '35': {'e': '2', 's': '1', 'c': '10', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '36': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '37', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '37': {'e': '38', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '38': {'e': '2', 's': '39', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'},
    '39': {'e': '2', 's': '1', 'c': '3', 'u': '1', 'l': '1', 'a': '4', 't': '1', 'd': '1', 'i': '1', 'n': '1', 'r': '5', 'o': '1', 'f': '1', 'm': '1'}
}

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos
for nodo in transiciones:
    G.add_node(nodo)


# Agregar las transiciones como aristas y combinar etiquetas
edge_labels_dict = {}  # Diccionario para agrupar etiquetas por aristas
for nodo_actual, transiciones_letras in transiciones.items():
    for letra, nodo_destino in transiciones_letras.items():
        edge = (nodo_actual, nodo_destino)
        if edge not in edge_labels_dict:
            edge_labels_dict[edge] = []
        edge_labels_dict[edge].append(letra)
        

# Añadir las aristas al grafo con las etiquetas agrupadas
for (nodo_origen, nodo_destino), letras in edge_labels_dict.items():
    G.add_edge(nodo_origen, nodo_destino, label=",".join(letras))


node_colors = ['lightblue' if nodo not in ['26', '31', '32', '33', '35', '39'] else 'lightgreen' for nodo in G.nodes()]

# Dibujar el grafo
pos = nx.spring_layout(G, seed=42)  # Posiciones para los nodos
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=12, font_weight="bold", arrows=True)

# Etiquetas para las aristas
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)


# Mostrar el grafo
plt.title("Grafo de Transiciones")
plt.show()