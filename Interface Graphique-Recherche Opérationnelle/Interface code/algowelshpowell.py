# algowelshpowell.py

import networkx as nx
import matplotlib.pyplot as plt
import random
import time
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox

def generate_random_graph(x):
    G = nx.Graph()
    G.add_nodes_from(range(x))
    for i in range(x):
        for j in range(i + 1, x):
            if random.choice([True, False]):
                G.add_edge(i, j)
    return G

def algowelshpowell(G):
    sorted_nodes = sorted(G.nodes, key=lambda x: G.degree[x], reverse=True)
    color_map = {}
    current_color = 0
    for node in sorted_nodes:
        if node not in color_map:
            color_map[node] = current_color
            for neighbor in sorted_nodes:
                if neighbor not in color_map and not any((neighbor, adj) in G.edges() or (adj, neighbor) in G.edges() for adj in color_map if color_map[adj] == current_color):
                    color_map[neighbor] = current_color
            current_color += 1
    return color_map

def run_algowelshpowell(num_vertices):
    start_time = time.time()

    # Générer le graphe aléatoire
    random_graph = generate_random_graph(num_vertices)
    
    # Créer une nouvelle fenêtre Tkinter pour afficher le graphe
    result_window = tk.Toplevel()
    result_window.title("Result of the Welsh-Powell algorithm")
    result_window.geometry("800x800")


    # Appliquer l'algorithme de Welsh-Powell pour colorer le graphe
    colors = algowelshpowell(random_graph)

    # Créer une figure 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    # Intégrer la figure dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=result_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Générer des positions aléatoires en 3D pour chaque sommet
    pos_3d = {i: (random.random(), random.random(), random.random()) for i in random_graph.nodes()}

    # Extraire les positions x, y, z pour chaque sommet
    x_pos = [pos_3d[node][0] for node in random_graph.nodes()]
    y_pos = [pos_3d[node][1] for node in random_graph.nodes()]
    z_pos = [pos_3d[node][2] for node in random_graph.nodes()]

    # Dessiner les arêtes en 3D
    for edge in random_graph.edges():
        x_vals = [pos_3d[edge[0]][0], pos_3d[edge[1]][0]]
        y_vals = [pos_3d[edge[0]][1], pos_3d[edge[1]][1]]
        z_vals = [pos_3d[edge[0]][2], pos_3d[edge[1]][2]]
        ax.plot(x_vals, y_vals, z_vals, color='black')

    # Dessiner les sommets en 3D
    color_values = [colors[node] for node in random_graph.nodes()]
    ax.scatter(x_pos, y_pos, z_pos, c=color_values, cmap=plt.cm.rainbow, s=100)

    # Ajouter les labels des sommets
    for i, (x, y, z) in pos_3d.items():
        ax.text(x, y, z, str(i), fontsize=10, color='black')

    # Afficher le nombre de couleurs utilisées (chromatic number)
    min_colors_used = max(colors.values()) + 1  # +1 car les couleurs commencent à 0
    result = f"Minimum number of colors used (χ(G)) : {min_colors_used}"

    # Afficher le résultat dans une boîte de dialogue
    messagebox.showinfo("Result of the Welsh-Powell algorithm", result)

    return result