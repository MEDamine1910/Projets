from algodijkstra import run_algodijkstra
from algowelshpowell import run_algowelshpowell
from algokruskal import run_algokruskal
from algobellmanford import run_bellman_ford  
from algonorthwest import generate_data, calculate_total_cost, north_west_corner
from algomoindrecout import generate_data, moindre_cout  
from algosteppingstone import generate_data, stepping_stone  
from algofordfulkerson import generate_random_graph, ford_fulkerson, find_min_cut, display_graph_3d
from algopotentielmetra import potentiel_metra
from tkinter import messagebox, simpledialog
from tkinter import Toplevel, Label, Entry, Button
import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import ttk
import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
import networkx as nx
from tkinter import Toplevel, Label 
from collections import deque  
from tkinter import PhotoImage
import sys
import os
import tkinter as tk
from tabulate import tabulate
plt.ioff() #pour desactiver l'affichage de figure matplotlib

# Fonction pour gérer les chemins d'accès
def resource_path(relative_path):
    """Get the absolute path to a resource."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Couleurs modernes
PRIMARY_COLOR = "#2E86C1"  # Bleu foncé
SECONDARY_COLOR = "#F4D03F"  # Jaune doré
BACKGROUND_COLOR = "#EAEDED"  # Gris clair
TEXT_COLOR = "#17202A"  # Noir profond
BUTTON_COLOR = "#3498DB"  # Bleu clair
BUTTON_HOVER_COLOR = "#5DADE2"  # Bleu plus clair
ERROR_COLOR = "#E74C3C"  # Rouge
SUCCESS_COLOR = "#28B463"  # Vert

# Police moderne
FONT = ("Helvetica", 12)
FONT_BOLD = ("Helvetica", 12, "bold")
FONT_TITLE = ("Helvetica", 20, "bold")

# Style des boutons
BUTTON_STYLE = {
    "font": FONT_BOLD,
    "bg": BUTTON_COLOR,
    "fg": "white",
    "activebackground": BUTTON_HOVER_COLOR,
    "activeforeground": "white",
    "relief": "flat",
    "bd": 0,
    "highlightthickness": 0,
    "padx": 10,
    "pady": 5,
}

# Style des labels
LABEL_STYLE = {
    "font": FONT,
    "bg": BACKGROUND_COLOR,
    "fg": TEXT_COLOR,
}

# Style des entrées
ENTRY_STYLE = {
    "font": FONT,
    "bg": "white",
    "fg": TEXT_COLOR,
    "relief": "flat",
    "bd": 2,
    "highlightthickness": 0,
}

# Fonction pour appliquer un style professionnel à une fenêtre
def apply_professional_style(window, title):
    window.title(title)
    window.geometry("600x400")
    window.minsize(400, 300)
    window.configure(bg=BACKGROUND_COLOR)
    window.option_add("*Font", FONT)

    # Titre de la fenêtre
    title_label = tk.Label(
        window,
        text=title,
        font=FONT_TITLE,
        bg=BACKGROUND_COLOR,
        fg=PRIMARY_COLOR,
    )
    title_label.pack(pady=20)

# Fonction pour créer un bouton stylisé
def create_styled_button(parent, text, command):
    button = tk.Button(
        parent,
        text=text,
        command=command,
        **BUTTON_STYLE
    )
    button.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_HOVER_COLOR))
    button.bind("<Leave>", lambda e: e.widget.config(bg=BUTTON_COLOR))
    return button

# Fonction pour exécuter l'algorithme de Dijkstra
def run_dijkstra():
    root.withdraw()
    input_window = tk.Toplevel(root)
    apply_professional_style(input_window, "Entering parameters - Dijkstra")

    tk.Label(input_window, text="Number of vertices :", **LABEL_STYLE).pack(pady=5)
    num_vertices_entry = tk.Entry(input_window, **ENTRY_STYLE)
    num_vertices_entry.pack(pady=5)

    tk.Label(input_window, text="Starting vertex (ex: 0) :", **LABEL_STYLE).pack(pady=5)
    start_vertex_entry = tk.Entry(input_window, **ENTRY_STYLE)
    start_vertex_entry.pack(pady=5)

    tk.Label(input_window, text="Arrival vertex (ex: 1) :", **LABEL_STYLE).pack(pady=5)
    end_vertex_entry = tk.Entry(input_window, **ENTRY_STYLE)
    end_vertex_entry.pack(pady=5)
    input_window.geometry("")  # Supprime la taille fixe

    def on_submit():
        num_vertices = int(num_vertices_entry.get())
        start_vertex = int(start_vertex_entry.get())
        end_vertex = int(end_vertex_entry.get())
        input_window.destroy()
        result = run_algodijkstra(num_vertices, start_vertex, end_vertex, root)
        
    submit_button = create_styled_button(input_window, "Validate", on_submit)
    submit_button.pack(pady=20)

    input_window.protocol("WM_DELETE_WINDOW", lambda: [input_window.destroy(), root.deiconify()])

# Fonction pour exécuter l'algorithme de Welsh-Powell
def run_welsh_powell_interface():
    root.withdraw()
    num_vertices = simpledialog.askinteger("Number of vertices", "Enter the numbre of vertices :", minvalue=1)
    result = run_algowelshpowell(num_vertices)
    
# Fonction pour exécuter l'algorithme de Kruskal
def run_kruskal_interface():
    root.withdraw()
    num_vertices = simpledialog.askinteger("Number of vertices", "Enter the numbre of vertices :", minvalue=1)
    result = run_algokruskal(num_vertices, root)
    
# Fonction pour exécuter l'algorithme de Bellman-Ford
def run_bellman_ford_interface():
    root.withdraw()
    input_window = tk.Toplevel(root)
    apply_professional_style(input_window, "Entering parameters - Bellman-Ford")

    tk.Label(input_window, text="Number of vertices :", **LABEL_STYLE).pack(pady=5)
    num_vertices_entry = tk.Entry(input_window, **ENTRY_STYLE)
    num_vertices_entry.pack(pady=5)

    tk.Label(input_window, text="Percentage of links (0.0 à 1.0) :", **LABEL_STYLE).pack(pady=5)
    pourcentage_liaisons_entry = tk.Entry(input_window, **ENTRY_STYLE)
    pourcentage_liaisons_entry.pack(pady=5)

    tk.Label(input_window, text="Number of vertices (ex: x0) :", **LABEL_STYLE).pack(pady=5)
    start_vertex_entry = tk.Entry(input_window, **ENTRY_STYLE)
    start_vertex_entry.pack(pady=5)

    tk.Label(input_window, text="Arrival vertex (ex: x1) :", **LABEL_STYLE).pack(pady=5)
    end_vertex_entry = tk.Entry(input_window, **ENTRY_STYLE)
    end_vertex_entry.pack(pady=5)
    input_window.geometry("")  # Supprime la taille fixe

    def on_submit():
        num_vertices = int(num_vertices_entry.get())
        pourcentage_liaisons = float(pourcentage_liaisons_entry.get())
        start_vertex = start_vertex_entry.get()
        end_vertex = end_vertex_entry.get()
        input_window.destroy()
        result = run_bellman_ford(num_vertices, pourcentage_liaisons, start_vertex, end_vertex, root)

    submit_button = create_styled_button(input_window, "Validate", on_submit)
    submit_button.pack(pady=20)

    input_window.protocol("WM_DELETE_WINDOW", lambda: [input_window.destroy(), root.deiconify()])

# Fonction pour exécuter l'algorithme North-West Corner
def run_north_west_corner_interface():
    root.withdraw()
    input_window = tk.Toplevel(root)
    apply_professional_style(input_window, "Entering parameters - North-West Corner")

    tk.Label(input_window, text="Factory capacities :", **LABEL_STYLE).pack(pady=5)
    num_factories_entry = tk.Entry(input_window, **ENTRY_STYLE)
    num_factories_entry.pack(pady=5)

    tk.Label(input_window, text="Clients requests :", **LABEL_STYLE).pack(pady=5)
    num_clients_entry = tk.Entry(input_window, **ENTRY_STYLE)
    num_clients_entry.pack(pady=5)

    def on_submit():
        try:
            num_factories = int(num_factories_entry.get())
            num_clients = int(num_clients_entry.get())
            if num_factories < 1 or num_clients < 1:
                messagebox.showerror("Erreur", "Please enter valid values (≥ 1).")
                return
            input_window.destroy()
            factory_capacities, client_demands, transport_costs = generate_data(num_factories, num_clients)
            transport_plan_nwc = north_west_corner(factory_capacities.copy(), client_demands.copy(), transport_costs)
            total_cost = calculate_total_cost(transport_plan_nwc, transport_costs)
            show_results("Result of the North-West Corner algorithm", factory_capacities, client_demands, transport_costs, transport_plan_nwc, total_cost)
        except Exception as e:
            messagebox.showerror("Erreur", f"An error has occurred : {e}")

    submit_button = create_styled_button(input_window, "Validate", on_submit)
    submit_button.pack(pady=20)

    input_window.protocol("WM_DELETE_WINDOW", lambda: [input_window.destroy(), root.deiconify()])

# Fonction pour exécuter l'algorithme Moindre Coût
def run_moindre_cout_interface():
    root.withdraw()
    input_window = tk.Toplevel(root)
    apply_professional_style(input_window, "Entering parameters - Moindre Coût")

    tk.Label(input_window, text="Factory capacities :", **LABEL_STYLE).pack(pady=5)
    num_factories_entry = tk.Entry(input_window, **ENTRY_STYLE)
    num_factories_entry.pack(pady=5)

    tk.Label(input_window, text="Clients requests :", **LABEL_STYLE).pack(pady=5)
    num_clients_entry = tk.Entry(input_window, **ENTRY_STYLE)
    num_clients_entry.pack(pady=5)

    def on_submit():
        try:
            num_factories = int(num_factories_entry.get())
            num_clients = int(num_clients_entry.get())
            if num_factories < 1 or num_clients < 1:
                messagebox.showerror("Erreur", "Please enter valid values (≥ 1).")
                return
            input_window.destroy()
            factory_capacities, client_demands, transport_costs = generate_data(num_factories, num_clients)
            transport_plan_moindre = moindre_cout(factory_capacities.copy(), client_demands.copy(), transport_costs)
            total_cost = calculate_total_cost(transport_plan_moindre, transport_costs)
            show_results("Result of the Moindre Cout algorithm", factory_capacities, client_demands, transport_costs, transport_plan_moindre, total_cost)
        except Exception as e:
            messagebox.showerror("Erreur", f"An error has occurred : {e}")

    submit_button = create_styled_button(input_window, "Validate", on_submit)
    submit_button.pack(pady=20)

    input_window.protocol("WM_DELETE_WINDOW", lambda: [input_window.destroy(), root.deiconify()])

# Fonction pour exécuter l'algorithme Stepping Stone
def run_steppingstone_algorithm_interface():
    root.withdraw()
    input_window = tk.Toplevel(root)
    apply_professional_style(input_window, "Entering parameters - Stepping Stone")

    tk.Label(input_window, text="Factory capacities :", **LABEL_STYLE).pack(pady=5)
    num_factories_entry = tk.Entry(input_window, **ENTRY_STYLE)
    num_factories_entry.pack(pady=5)

    tk.Label(input_window, text="Clients requests :", **LABEL_STYLE).pack(pady=5)
    num_clients_entry = tk.Entry(input_window, **ENTRY_STYLE)
    num_clients_entry.pack(pady=5)

    def on_submit():
        try:
            num_factories = int(num_factories_entry.get())
            num_clients = int(num_clients_entry.get())
            if num_factories < 1 or num_clients < 1:
                messagebox.showerror("Erreur", "Please enter valid values (≥ 1).")
                return
            input_window.destroy()
            factory_capacities, client_demands, transport_costs = generate_data(num_factories, num_clients)
            transport_plan_nwc = north_west_corner(factory_capacities.copy(), client_demands.copy(), transport_costs)
            optimized_plan, cost_stepping_stone = stepping_stone(transport_plan_nwc.copy(), factory_capacities.copy(), client_demands.copy(), transport_costs)
            show_results("Result of the Stepping Stone algorithm", factory_capacities, client_demands, transport_costs, optimized_plan, cost_stepping_stone)
        except Exception as e:
            messagebox.showerror("Erreur", f"An error has occurred : {e}")

    submit_button = create_styled_button(input_window, "Validate", on_submit)
    submit_button.pack(pady=20)

    input_window.protocol("WM_DELETE_WINDOW", lambda: [input_window.destroy(), root.deiconify()])

# Fonction pour exécuter Ford-Fulkerson et afficher le graphe
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

    # Afficher le graphe avec Tkinter
    display_graph_3d(G, min_cut)

    # Afficher le flot maximal dans une boîte de dialogue
    messagebox.showinfo("Flot maximal", f"Le flot maximal est : {max_flow}")
    
def call_potentiel_metra():
    root.withdraw()
    try:
        # Créer un label pour afficher les résultats
        output_label = tk.Label(root, text="", justify="left", font=("Arial", 12))
        output_label.grid(row=3, column=0, pady=20)  # Utiliser grid() au lieu de pack()

        # Appeler la fonction du Potentiel Métra
        potentiel_metra(root, output_label)
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
        
def create_table(parent, data, headers):
    # Créer un conteneur pour le tableau avec des barres de défilement
    container = ttk.Frame(parent)
    container.pack(fill="both", expand=True)

    # Configurer le conteneur pour qu'il utilise tout l'espace
    container.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    # Créer un canvas pour permettre le défilement
    canvas = tk.Canvas(container)
    canvas.grid(row=0, column=0, sticky="nsew")  # Prend tout l'espace du conteneur

    # Barres de défilement
    scrollbar_x = ttk.Scrollbar(container, orient="horizontal", command=canvas.xview)
    scrollbar_y = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar_x.grid(row=1, column=0, sticky="ew")
    scrollbar_y.grid(row=0, column=1, sticky="ns")

    canvas.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

    # Créer un frame flexible dans le canvas
    table_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=table_frame, anchor="nw")

    # Configurer `table_frame` pour qu'il s'étende
    table_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Configurer le tableau Treeview
    table = ttk.Treeview(table_frame, columns=headers, show="headings")
    for header in headers:
        table.heading(header, text=header)
        table.column(header, anchor="center", width=100)  # Largeur initiale

    # Ajouter les données au tableau
    for index, row in data.iterrows():
        table.insert("", "end", values=[index] + list(row))

    # Ajuster les colonnes pour qu'elles soient flexibles
    def adjust_column_widths():
        for col in headers:
            max_width = max(
                table.column(col, "width"),
                *[len(str(table.set(item, col))) * 10 for item in table.get_children()]
            )
            table.column(col, width=max_width)

    adjust_column_widths()

    # Empaqueter le tableau dans `table_frame`
    table.pack(fill="both", expand=True)

    return container


def show_results(title, factory_capacities, client_demands, transport_costs, transport_plan, cost=None):
    output_window = tk.Toplevel(root)
    apply_professional_style(output_window, title)
    output_window.geometry("800x600")  # Définir une taille initiale
    output_window.minsize(600, 500)  # Définir une taille minimale

    # Créer un canvas avec une barre de défilement verticale
    canvas = tk.Canvas(output_window)  
    scrollbar = ttk.Scrollbar(output_window, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Placer le canvas et la barre de défilement
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Affichage des capacités des usines
    tk.Label(scrollable_frame, text="Factory capacities:", **LABEL_STYLE).pack(pady=5)
    capacities_df = pd.DataFrame(factory_capacities, columns=["Capacity"], index=[f"Factory {i+1}" for i in range(len(factory_capacities))])
    capacities_table = create_table(scrollable_frame, capacities_df, ['Factory', 'Capacity'])
    capacities_table.pack(pady=5, padx=10, fill='both', expand=True)

    # Affichage des demandes des clients
    tk.Label(scrollable_frame, text="Clients requests:", **LABEL_STYLE).pack(pady=5)
    demands_df = pd.DataFrame(client_demands, columns=["Requests"], index=[f"Client {j+1}" for j in range(len(client_demands))])
    demands_table = create_table(scrollable_frame, demands_df, ['Client', 'Requests'])
    demands_table.pack(pady=5, padx=10, fill='both', expand=True)

    # Affichage des coûts de transport
    tk.Label(scrollable_frame, text="Transportation costs:", **LABEL_STYLE).pack(pady=5)
    costs_df = pd.DataFrame(transport_costs, columns=[f"Client {j+1}" for j in range(len(client_demands))], index=[f"Factory {i+1}" for i in range(len(factory_capacities))])
    costs_table = create_table(scrollable_frame, costs_df, ['Factory'] + list(costs_df.columns))
    costs_table.pack(pady=5, padx=10, fill='both', expand=True)

    # Affichage du plan de transport
    tk.Label(scrollable_frame, text=f"{title}:", **LABEL_STYLE).pack(pady=5)
    plan_df = pd.DataFrame(transport_plan, columns=[f"Client {j+1}" for j in range(len(client_demands))], index=[f"Factory {i+1}" for i in range(len(factory_capacities))])
    plan_table = create_table(scrollable_frame, plan_df, ['Factory'] + list(plan_df.columns))
    plan_table.pack(pady=5, padx=10, fill='both', expand=True)
    
    # Affichage du coût total (si applicable)
    if cost is not None:
        tk.Label(scrollable_frame, text=f"Total cost: {cost}", **LABEL_STYLE).pack(pady=5)

    # Bouton de fermeture
    close_button = create_styled_button(scrollable_frame, "Close", output_window.destroy)
    close_button.pack(pady=20)

    # Gestion de la fermeture de la fenêtre
    output_window.protocol("WM_DELETE_WINDOW", lambda: output_window.destroy())

    # Permettre à la fenêtre d'être redimensionnée
    output_window.resizable(True, True)
    
# Fonction pour créer des boutons stylés et plus grands
def create_styled_buttonn(parent, text, command):
    button = tk.Button(
        parent,
        text=text,
        font=("Helvetica", 14, "bold"),  # Augmentation de la taille de la police
        bg=BUTTON_COLOR,
        fg="white",
        activebackground=BUTTON_HOVER_COLOR,
        activeforeground="white",
        relief="raised",
        bd=2,
        width=20,  # Largeur du bouton en termes de caractères
        height=2,  # Hauteur du bouton en termes de lignes de texte
        command=command,
    )
    return button
# Fonction pour ouvrir la fenêtre des algorithmes
def open_entree_window():
    second_window = tk.Toplevel(root)
    apply_professional_style(second_window, "Operational research algorithms")

    # Cadre pour contenir les boutons
    button_frame = tk.Frame(second_window, bg=BACKGROUND_COLOR)
    button_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Liste des algorithmes (texte, commande)
    algorithms = [
        ("Welsh-Powell", run_welsh_powell_interface),
        ("Kruskal", run_kruskal_interface),
        ("Dijkstra", run_dijkstra),
        ("Bellman-Ford", run_bellman_ford_interface),
        ("Ford-Fulkerson", run_ford_fulkerson_interface),
        ("Potentiel Metra", call_potentiel_metra),
        ("North West", run_north_west_corner_interface),
        ("Moindre Coût", run_moindre_cout_interface),
        ("Stepping Stone", run_steppingstone_algorithm_interface),
    ]

    # Ajouter les boutons dans une matrice 3x3
    rows, cols = 3, 3
    for index, (text, command) in enumerate(algorithms):
        row = index // cols
        col = index % cols
        button = create_styled_buttonn(button_frame, text, command)
        # Placer le bouton dans la grille sans permettre l'agrandissement de sa taille
        button.grid(row=row, column=col, padx=10, pady=10)

    # Rendre les espaces autour des boutons flexibles (sans agrandir les boutons eux-mêmes)
    for i in range(rows):
        button_frame.grid_rowconfigure(i, weight=1)  # Espace flexible pour les lignes
    for j in range(cols):
        button_frame.grid_columnconfigure(j, weight=1)  # Espace flexible pour les colonnes
    
    # Gestion de la fermeture de la fenêtre
    second_window.protocol("WM_DELETE_WINDOW", lambda: [second_window.destroy(), root.deiconify()])

# Couleurs pour le style vert et blanc
BACKGROUND_COLOR = "#e8f5e9"  # Vert très clair (fond principal)
PRIMARY_COLOR = "#388e3c"  # Vert foncé (texte principal)
TEXT_COLOR = "#1b5e20"  # Vert encore plus foncé (texte secondaire)
BUTTON_COLOR = "#4caf50"  # Vert moyen (boutons)
BUTTON_HOVER_COLOR = "#81c784"  # Vert clair pour le clic ou survol
ERROR_COLOR = "#d32f2f"  # Rouge (pour messages d'erreur ou boutons spécifiques)

# Fonction pour créer des boutons stylés et plus grands
def create_styled_button(parent, text, command):
    button = tk.Button(
        parent,
        text=text,
        font=("Helvetica", 14, "bold"),  # Augmentation de la taille de la police
        bg=BUTTON_COLOR,
        fg="white",
        activebackground=BUTTON_HOVER_COLOR,
        activeforeground="white",
        relief="raised",
        bd=2,
        width=15,  # Largeur du bouton en termes de caractères
        height=1,  # Hauteur du bouton en termes de lignes de texte
        command=command,
    )
    return button

def close_window(window):
    # Fonction pour fermer la fenêtre
    window.destroy()  # Ferme la fenêtre

# Création de la fenêtre principale
root = tk.Tk()
root.title("Graphical Interface Tkinter - GUI")
root.geometry("600x400")
root.minsize(500, 400)
root.configure(bg=BACKGROUND_COLOR)

# Charger l'image
image_path = resource_path("emsi logo.png")  # Utiliser resource_path pour obtenir le chemin correct
try:
    logo_image = tk.PhotoImage(file=image_path)
    logo_image = logo_image.subsample(2, 2)  # Réduire la taille de l'image de moitié
    logo_label = tk.Label(root, image=logo_image, bg=BACKGROUND_COLOR)
    logo_label.image = logo_image  # Garder une référence pour éviter la suppression par le garbage collector
    logo_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")  # Logo en haut à gauche
except Exception as e:
    print(f"Erreur lors du chargement de l'image : {e}")

# Cadre principal pour centrer le contenu
center_frame = ttk.Frame(root, style="Custom.TFrame")
center_frame.grid(row=1, column=0, sticky="nsew")  # Centrer le cadre

# Configuration des poids pour centrer le cadre principal
root.grid_rowconfigure(1, weight=1)  # Ligne 1 : Contient le cadre principal
root.grid_columnconfigure(0, weight=1)  # Colonne 0 : Centrer horizontalement

# Sous-titre centré
subtitle_label = tk.Label(
    center_frame,
    text="Operational research algorithms",
    font=FONT_TITLE,
    bg=BACKGROUND_COLOR,
    fg=PRIMARY_COLOR,
)
subtitle_label.grid(row=0, column=0, pady=10)  # Centrer le sous-titre

# Boutons centrés
button_frame = tk.Frame(center_frame, bg=BACKGROUND_COLOR)
button_frame.grid(row=1, column=0, pady=20)  # Cadre pour les boutons (centré)

# Configuration des boutons dans le cadre
btn_entree = create_styled_button(button_frame, "Open", open_entree_window)
btn_entree.grid(row=0, column=0, padx=20, pady=10)

btn_sortie = create_styled_button(button_frame, "Close", lambda: close_window(root))
btn_sortie.grid(row=0, column=1, padx=20, pady=10)

# Configuration des poids pour centrer le contenu dans center_frame
center_frame.grid_rowconfigure(0, weight=1)  # Ligne pour le sous-titre
center_frame.grid_rowconfigure(2, weight=1)  # Ligne pour les boutons
center_frame.grid_columnconfigure(0, weight=1)  # Colonne unique (centrée)

# Ajouter les lignes de texte en bas
bottom_frame = ttk.Frame(root, style="Custom.TFrame")
bottom_frame.grid(row=2, column=0, sticky="s")  # Texte en bas

realisee_par_label = tk.Label(
    bottom_frame,
    text="Directed by : ROUISS MOHAMED AMINE",
    font=FONT,
    bg=BACKGROUND_COLOR,
    fg=TEXT_COLOR,
)
realisee_par_label.grid(row=0, column=0, pady=5)  # Texte en bas

encadre_par_label = tk.Label(
    bottom_frame,
    text="Supervised by : Mrs.EL MKHALET MOUNA",
    font=FONT,
    bg=BACKGROUND_COLOR,
    fg=TEXT_COLOR,
)
encadre_par_label.grid(row=1, column=0, pady=5)  # Texte en bas

# Ajustement flexible à la taille de la fenêtre
root.grid_rowconfigure(0, weight=0)  # Logo en haut (pas de poids)
root.grid_rowconfigure(1, weight=1)  # Centrer le cadre principal
root.grid_rowconfigure(2, weight=0)  # Texte en bas (pas de poids)
root.grid_columnconfigure(0, weight=1)  # Centrer le contenu horizontalement

# Style avec ttk
style = ttk.Style()
style.configure("Custom.TFrame", background=BACKGROUND_COLOR)

# Boucle principale
root.mainloop()
