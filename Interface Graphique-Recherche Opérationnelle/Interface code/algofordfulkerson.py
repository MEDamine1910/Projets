import random
import networkx as nx
from collections import deque
import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Fonction pour générer un graphe aléatoire
def generate_random_graph(num_vertices, max_capacity=10):
    G = nx.DiGraph()  # Création d'un graphe dirigé
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j:  # Pas d'arcs auto-bouclants
                capacity = random.randint(1, max_capacity)  # Capacités aléatoires entre 1 et max_capacity
                G.add_edge(i, j, capacity=capacity)
    return G

# Fonction de recherche en largeur (BFS) pour trouver un chemin augmentant
def bfs(capacity, flow, source, sink):
    parent = [-1] * len(capacity)  # Tableau pour stocker le parent de chaque nœud
    parent[source] = -2  # Marquer la source comme visitée
    queue = deque([(source, float('inf'))])  # File d'attente avec le flot infini
    while queue:
        u, min_cap = queue.popleft()
        
        for v in range(len(capacity)):
            if parent[v] == -1 and capacity[u][v] - flow[u][v] > 0:  # Si le nœud v n'est pas encore visité et qu'il reste de la capacité
                parent[v] = u
                new_flow = min(min_cap, capacity[u][v] - flow[u][v])
                if v == sink:
                    return new_flow, parent  # Retourner le flot minimum et le tableau des parents
                queue.append((v, new_flow))
    return 0, parent  # Aucun chemin trouvé

# Algorithme de Ford-Fulkerson pour trouver le flot maximal
def ford_fulkerson(capacity, source, sink):
    n = len(capacity)
    flow = [[0] * n for _ in range(n)]  # Flot initialisé à 0
    max_flow = 0
    
    while True:
        path_flow, parent = bfs(capacity, flow, source, sink)
        if path_flow == 0:  # Aucun chemin augmentant trouvé
            break
        max_flow += path_flow
        
        # Mise à jour des flots dans les arcs du chemin trouvé
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow  # Mise à jour du flot résiduel
            v = u
    return max_flow, flow

# Fonction pour trouver la coupe minimale en utilisant un BFS
def find_min_cut(capacity, flow, source):
    visited = [False] * len(capacity)
    queue = deque([source])
    visited[source] = True
    
    while queue:
        u = queue.popleft()
        for v in range(len(capacity)):
            if capacity[u][v] - flow[u][v] > 0 and not visited[v]:  # Si le flot résiduel est positif
                visited[v] = True
                queue.append(v)
    return visited

# Fonction pour afficher le graphe en 3D avec Tkinter
def display_graph_3d(G, min_cut):
    # Créer une nouvelle fenêtre Tkinter
    graph_window = tk.Toplevel()
    graph_window.title("Graph Ford-Fulkerson (3D)")
    graph_window.geometry("800x600")

    # Créer une figure 3D avec matplotlib
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Positionnement des nœuds en 3D
    pos = nx.spring_layout(G, dim=3)

    # Extraire les coordonnées des nœuds
    xs, ys, zs = zip(*[pos[node] for node in G.nodes()])

    # Dessiner les nœuds
    for node in G.nodes():
        x, y, z = pos[node]
        color = "green" if min_cut[node] else "blue"  # Couleur en fonction de la coupe minimale
        ax.scatter(x, y, z, c=color, s=100, alpha=0.8)
        ax.text(x, y, z, str(node), fontsize=10, color="black")

    # Dessiner les arêtes
    for (u, v) in G.edges():
        x1, y1, z1 = pos[u]
        x2, y2, z2 = pos[v]
        color = "red" if min_cut[u] and not min_cut[v] else "black"  # Couleur en fonction de la coupe minimale
        ax.plot([x1, x2], [y1, y2], [z1, z2], color=color, linewidth=1)

    # Configurer les axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Graphe 3D de Ford-Fulkerson")

    # Intégrer la figure dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # Bouton de fermeture
    close_button = tk.Button(graph_window, text="Fermer", command=graph_window.destroy)
    close_button.pack(pady=10)

# Fonction principale pour exécuter Ford-Fulkerson et afficher le graphe
def run_ford_fulkerson_interface():
    root.withdraw()
    num_vertices = simpledialog.askinteger("Nombre de sommets", "Entrez le nombre de sommets :", minvalue=1)
    if num_vertices is None:
        return

    # Génération du graphe
    G = generate_random_graph(num_vertices)
    source = 0  # Source fixée au sommet 0
    sink = num_vertices - 1  # Puits fixé au dernier sommet

    # Matrice de capacité
    capacity = [[0] * num_vertices for _ in range(num_vertices)]
    for u, v, data in G.edges(data=True):
        capacity[u][v] = data['capacity']

    # Calcul du flot maximal avec Ford-Fulkerson
    max_flow, flow = ford_fulkerson(capacity, source, sink)

    # Trouver la coupe minimale
    min_cut = find_min_cut(capacity, flow, source)

    # Afficher le graphe en 3D
    display_graph_3d(G, min_cut)

    # Afficher le flot maximal dans une boîte de dialogue
    messagebox.showinfo("Flot maximal", f"Le flot maximal est : {max_flow}")

# Point d'entrée du programme
if __name__ == "__main__":
    root = tk.Tk()
    run_ford_fulkerson_interface()
    root.mainloop()