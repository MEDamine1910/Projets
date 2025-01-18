# algodijkstra.py
import time
import networkx as nx
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox

def generate_random_graph(num_vertices):
    G = nx.Graph()
    G.add_nodes_from(range(num_vertices))
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.choice([True, False]):
                weight = random.randint(1, 100)
                G.add_edge(i, j, weight=weight)
    return G

def run_algodijkstra(num_vertices, start_vertex, end_vertex, root):
    start_time = time.time()

    # Générer le graphe aléatoire
    G = generate_random_graph(num_vertices)

    # Créer une nouvelle fenêtre Tkinter pour afficher le graphe
    result_window = tk.Toplevel(root)
    result_window.title("Result of Dijkstra's algorithm")
    result_window.geometry("800x800")

    # Créer une figure 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Générer des positions aléatoires en 3D pour chaque sommet
    pos_3d = {i: (random.random(), random.random(), random.random()) for i in G.nodes()}

    # Extraire les positions x, y, z pour chaque sommet
    x_pos = [pos_3d[node][0] for node in G.nodes()]
    y_pos = [pos_3d[node][1] for node in G.nodes()]
    z_pos = [pos_3d[node][2] for node in G.nodes()]

    # Dessiner les arêtes en 3D et annoter les poids
    for edge in G.edges():
        x_vals = [pos_3d[edge[0]][0], pos_3d[edge[1]][0]]
        y_vals = [pos_3d[edge[0]][1], pos_3d[edge[1]][1]]
        z_vals = [pos_3d[edge[0]][2], pos_3d[edge[1]][2]]
        ax.plot(x_vals, y_vals, z_vals, color='gray')

        # Calculer la position moyenne pour placer le texte (milieu de l'arête)
        mid_x = sum(x_vals) / 2
        mid_y = sum(y_vals) / 2
        mid_z = sum(z_vals) / 2

        # Annoter le poids de l'arête
        weight = G[edge[0]][edge[1]]['weight']
        ax.text(mid_x, mid_y, mid_z, f"{weight}", color='red', fontsize=8)

    # Dessiner les sommets en 3D
    ax.scatter(x_pos, y_pos, z_pos, c='lightblue', s=300)

    # Ajouter les labels des sommets
    for i, (x, y, z) in pos_3d.items():
        ax.text(x, y, z, str(i), fontsize=10, color='black')

    # Intégrer la figure dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=result_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Appliquer l'algorithme de Dijkstra
    if start_vertex in G and end_vertex in G:
        try:
            length, path = nx.single_source_dijkstra(G, start_vertex, end_vertex, weight='weight')
            result = f"Minimum distance from {start_vertex} to {end_vertex} : {length}\nShortest path : {' -> '.join(map(str, path))}"
        except nx.NetworkXNoPath:
            result = f"No path between {start_vertex} and {end_vertex}."
    else:
        result = "One of the vertices does not exist in the graph."

    # Afficher les résultats dans une boîte de dialogue
    messagebox.showinfo("Result of Dijkstra's algorithm", result)

    return result