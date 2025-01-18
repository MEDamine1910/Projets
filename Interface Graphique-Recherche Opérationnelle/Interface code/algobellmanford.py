# AlgoBellmanFord.py

import networkx as nx
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox

# Générer un graphe orienté aléatoire avec des distances aléatoires et un pourcentage de liaisons
def generer_graphe_oriente(n, pourcentage_liaisons=0.3):
    G = nx.DiGraph()  # Graphe orienté
    sommets = [f"x{i}" for i in range(n)]

    # Ajouter les sommets
    for sommet in sommets:
        G.add_node(sommet)

    # Ajouter des arcs avec des distances aléatoires entre les sommets
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < pourcentage_liaisons:  # Utiliser le pourcentage de liaisons
                distance = random.randint(1, 100)
                G.add_edge(sommets[i], sommets[j], weight=distance)

    return G

# Fonction pour exécuter l'algorithme de Bellman-Ford et afficher le graphe en 3D
def run_bellman_ford(num_vertices, pourcentage_liaisons, start_vertex, end_vertex, root):
    # Générer le graphe orienté
    G = generer_graphe_oriente(num_vertices, pourcentage_liaisons)
    
    # Créer une nouvelle fenêtre Tkinter pour afficher le graphe
    result_window = tk.Toplevel(root)
    result_window.title("Result of the Bellman-Ford algorithm")
    result_window.geometry("800x800")

    # Créer une figure 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Intégrer la figure dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=result_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Générer des positions aléatoires en 3D pour chaque sommet
    pos_3d = {node: (random.random(), random.random(), random.random()) for node in G.nodes()}

    # Extraire les positions x, y, z pour chaque sommet
    x_pos = [pos_3d[node][0] for node in G.nodes()]
    y_pos = [pos_3d[node][1] for node in G.nodes()]
    z_pos = [pos_3d[node][2] for node in G.nodes()]

    # Dessiner les arêtes en 3D avec des flèches et annoter les poids
    for u, v, data in G.edges(data=True):
        x_start, y_start, z_start = pos_3d[u]
        x_end, y_end, z_end = pos_3d[v]

        # Dessiner une flèche pour représenter l'orientation de l'arc
        ax.quiver(
            x_start, y_start, z_start,  # Point de départ
            x_end - x_start, y_end - y_start, z_end - z_start,  # Direction
            color='gray', alpha=0.5, arrow_length_ratio=0.1
        )

        # Calculer la position moyenne pour placer le texte (milieu de l'arête)
        mid_x = (x_start + x_end) / 2
        mid_y = (y_start + y_end) / 2
        mid_z = (z_start + z_end) / 2

        
        # Annoter le poids de l'arête
        weight = data['weight']
        ax.text(mid_x, mid_y, mid_z, f"{weight}", color='red', fontsize=8)

    # Appliquer l'algorithme de Bellman-Ford
    try:
        distances, chemins = nx.single_source_bellman_ford(G, start_vertex, weight='weight')
        chemin = chemins[end_vertex]
        distance_totale = distances[end_vertex]

        # Dessiner les arêtes du chemin le plus court en rouge avec des flèches
        for i in range(len(chemin) - 1):
            u, v = chemin[i], chemin[i + 1]
            x_start, y_start, z_start = pos_3d[u]
            x_end, y_end, z_end = pos_3d[v]

            # Dessiner une flèche rouge pour représenter le chemin le plus court
            ax.quiver(
                x_start, y_start, z_start,  # Point de départ
                x_end - x_start, y_end - y_start, z_end - z_start,  # Direction
                color='red', arrow_length_ratio=0.1, linewidth=2
            )

        # Afficher les résultats
        result = f"The shortest path between {start_vertex} and {end_vertex} is : {' -> '.join(chemin)}\nTotal distance : {distance_totale}"
    except nx.NetworkXNoPath:
        result = f"No path between {start_vertex} and {end_vertex}."
    except nx.NetworkXUnbounded:
        result = f"The graph contains a negative cycle accessible from {start_vertex}."

    # Ajouter les labels des sommets
    for node, (x, y, z) in pos_3d.items():
        ax.text(x, y, z, node, fontsize=12, color='black')

    # Configurer la vue 3D
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Shortest path (Bellman-Ford) in 3D")

    # Afficher les résultats dans une boîte de dialogue
    messagebox.showinfo("Result of the Bellman-Ford algorithm", result)