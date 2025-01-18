# algokruskal.py

import networkx as nx
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox

# Fonction pour générer des noms de sommets en séquences alphabétiques (A, B, C, ..., AA, AB, ...)
def generer_etiq_sommets(n):
    etiqs = []
    i = 0
    while len(etiqs) < n:
        etiq = ''
        temp = i
        while temp >= 0:
            etiq = chr(temp % 26 + 65) + etiq
            temp = temp // 26 - 1
        etiqs.append(etiq)
        i += 1
    return etiqs

# Fonction pour générer un graphe aléatoire avec des sommets étiquetés par des lettres
def generer_graphe_aleatoire(nb_sommets):
    G = nx.Graph()  # Créer un graphe non orienté
    etiquettes = generer_etiq_sommets(nb_sommets)  # Créer des étiquettes A, B, C... AA, AB, ...

    # Ajouter des nœuds avec des lettres
    for etiquette in etiquettes:
        G.add_node(etiquette)

    # Ajouter des arêtes avec des poids aléatoires
    for _ in range(nb_sommets * 2):  # Ajouter plusieurs arêtes pour bien connecter les sommets
        u = random.choice(etiquettes)
        v = random.choice(etiquettes)
        if u != v:  # Éviter les boucles
            poids = random.randint(1, 100)  # Poids aléatoire entre 1 et 100
            G.add_edge(u, v, weight=poids)

    return G

# Fonction pour appliquer l'algorithme de Kruskal
def kruskal(graphe):
    # Convertir le graphe en une liste d'arêtes triées par poids
    arbre_couvrant = []
    edges = sorted(graphe.edges(data=True), key=lambda x: x[2]['weight'])  # Trier par poids
    union_find = {i: i for i in graphe.nodes}  # Union-Find pour détecter les cycles

    def find(u):
        if union_find[u] != u:
            union_find[u] = find(union_find[u])
        return union_find[u]

    def union(u, v):
        parent_u = find(u)
        parent_v = find(v)
        if parent_u != parent_v:
            union_find[parent_u] = parent_v

    for u, v, data in edges:
        if find(u) != find(v):  # Si les sommets ne forment pas un cycle
            arbre_couvrant.append((u, v, data['weight']))
            union(u, v)

    return arbre_couvrant

# Fonction pour exécuter l'algorithme de Kruskal et afficher le graphe en 3D
def run_algokruskal(num_vertices, root):
    # Générer un graphe aléatoire
    graphe = generer_graphe_aleatoire(num_vertices)
    
    # Créer une nouvelle fenêtre Tkinter pour afficher le graphe
    result_window = tk.Toplevel(root)
    result_window.title("Result of Kruskal's algorithm")
    result_window.geometry("800x800")

    # Appliquer Kruskal
    arbre_couvrant = kruskal(graphe)

    # Calculer le coût total
    cout_total = sum([poids for _, _, poids in arbre_couvrant])
    result = f"Total cost of chosen edges: {cout_total}"

    # Créer une figure 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Intégrer la figure dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=result_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Générer des positions aléatoires en 3D pour chaque sommet
    pos_3d = {node: (random.random(), random.random(), random.random()) for node in graphe.nodes()}

    # Extraire les positions x, y, z pour chaque sommet
    x_pos = [pos_3d[node][0] for node in graphe.nodes()]
    y_pos = [pos_3d[node][1] for node in graphe.nodes()]
    z_pos = [pos_3d[node][2] for node in graphe.nodes()]

    # Dessiner les arêtes normales en noir et annoter les poids
    for u, v, data in graphe.edges(data=True):
        x_vals = [pos_3d[u][0], pos_3d[v][0]]
        y_vals = [pos_3d[u][1], pos_3d[v][1]]
        z_vals = [pos_3d[u][2], pos_3d[v][2]]
        ax.plot(x_vals, y_vals, z_vals, color='gray', alpha=0.5)

        # Calculer la position moyenne pour placer le texte (milieu de l'arête)
        mid_x = sum(x_vals) / 2
        mid_y = sum(y_vals) / 2
        mid_z = sum(z_vals) / 2

        # Annoter le poids de l'arête
        weight = data['weight']
        ax.text(mid_x, mid_y, mid_z, f"{weight}", color='blue', fontsize=8)

    # Dessiner les arêtes de l'arbre couvrant minimal en rouge
    for u, v, poids in arbre_couvrant:
        x_vals = [pos_3d[u][0], pos_3d[v][0]]
        y_vals = [pos_3d[u][1], pos_3d[v][1]]
        z_vals = [pos_3d[u][2], pos_3d[v][2]]
        ax.plot(x_vals, y_vals, z_vals, color='red', linewidth=2)

        # Annoter le poids des arêtes de l'arbre couvrant minimal
        mid_x = sum(x_vals) / 2
        mid_y = sum(y_vals) / 2
        mid_z = sum(z_vals) / 2
        ax.text(mid_x, mid_y, mid_z, f"{poids}", color='red', fontsize=8, weight='bold')

    # Dessiner les sommets en 3D
    ax.scatter(x_pos, y_pos, z_pos, c='lightblue', s=200)

    # Ajouter les labels des sommets
    for node, (x, y, z) in pos_3d.items():
        ax.text(x, y, z, node, fontsize=12, color='black')

    # Configurer la vue 3D
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Minimal spanning tree (Kruskal) in 3D")

    # Afficher le résultat dans une boîte de dialogue
    messagebox.showinfo("Result of Kruskal's algorithm", result)