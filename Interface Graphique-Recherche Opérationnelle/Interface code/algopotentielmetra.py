import random
from tabulate import tabulate
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import simpledialog, Toplevel, Label, Text, Button
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D  # Import pour le 3D

def generate_task_table(num_tasks):
    """Générer un tableau de tâches avec durées et antériorités."""
    tasks = {}
    for i in range(1, num_tasks + 1):
        duration = random.randint(1, 10)  # Durée aléatoire (1-10 jours)
        predecessors = random.sample(range(1, i), random.randint(0, min(2, i - 1)))
        tasks[f"T{i}"] = {"duration": duration, "predecessors": [f"T{p}" for p in predecessors]}
    return tasks

def calculate_potential_metra(tasks):
    """Calculer les dates au plus tôt, au plus tard, la durée totale et le chemin critique."""
    early_start = {}
    late_start = {}

    # Calcul des dates au plus tôt
    for task in tasks:
        predecessors = tasks[task]["predecessors"]
        early_start[task] = max([early_start[p] + tasks[p]["duration"] for p in predecessors] + [0])

    # Durée totale du projet
    total_duration = max(early_start[task] + tasks[task]["duration"] for task in tasks)

    # Calcul des dates au plus tard
    late_start = {task: total_duration - tasks[task]["duration"] for task in tasks}
    for task in sorted(tasks, key=lambda x: -early_start[x]):
        successors = [t for t in tasks if task in tasks[t]["predecessors"]]
        if successors:
            late_start[task] = min([late_start[s] - tasks[task]["duration"] for s in successors])

    # Chemin critique
    critical_path = [task for task in tasks if early_start[task] == late_start[task]]

    return early_start, late_start, total_duration, critical_path

def plot_potential_metra_3d(tasks, early_start, total_duration, critical_path):
    """Afficher un graphe du potentiel Métra en 3D avec NetworkX."""
    G = nx.DiGraph()
    for task, details in tasks.items():
        for predecessor in details["predecessors"]:
            G.add_edge(predecessor, task)

    # Générer des positions 3D aléatoires pour les nœuds
    pos_3d = {node: (random.random(), random.random(), random.random()) for node in G.nodes()}

    # Extraire les positions x, y, z pour chaque nœud
    x_pos = [pos_3d[node][0] for node in G.nodes()]
    y_pos = [pos_3d[node][1] for node in G.nodes()]
    z_pos = [pos_3d[node][2] for node in G.nodes()]

    # Créer une nouvelle fenêtre pour le graphe 3D
    graph_window = tk.Toplevel()
    graph_window.title("Graph 3D Potentiel Métra")
    graph_window.geometry("800x600")

    # Créer une figure matplotlib en 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Dessiner les arêtes en 3D avec des flèches
    for u, v in G.edges():
        x_start, y_start, z_start = pos_3d[u]
        x_end, y_end, z_end = pos_3d[v]

        # Dessiner une flèche pour représenter l'orientation de l'arête
        ax.quiver(
            x_start, y_start, z_start,  # Point de départ
            x_end - x_start, y_end - y_start, z_end - z_start,  # Direction
            color='black', arrow_length_ratio=0.1, linewidth=1
        )

    # Dessiner les nœuds en 3D
    ax.scatter(x_pos, y_pos, z_pos, c='lightblue', s=500)

    # Ajouter les labels des nœuds
    for node, (x, y, z) in pos_3d.items():
        ax.text(x, y, z, node, fontsize=10, color='black')

    # Configurer la vue 3D
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f"Graph potentiel Métra 3D (Total duration: {total_duration})", fontsize=14)

    # Intégrer la figure dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

def potentiel_metra(gui, output_label):
    """Fonction principale pour exécuter l'algorithme du Potentiel Métra via l'interface graphique."""
    num_tasks = simpledialog.askinteger("Entrée", "Entrez le nombre de tâches :", parent=gui, minvalue=1)
    if num_tasks is None:  # Si l'utilisateur annule
        output_label.config(text="Action annulée par l'utilisateur.")
        return

    tasks = generate_task_table(num_tasks)

    # Calcul du potentiel Métra
    early_start, late_start, total_duration, critical_path = calculate_potential_metra(tasks)

    # Créer une nouvelle fenêtre pour afficher les résultats textuels
    result_window = tk.Toplevel(gui)
    result_window.title("Résultats du Potentiel Métra")
    result_window.geometry("600x400")
    result_window.configure(bg="#f0f0f0")  # Couleur de fond moderne

    # Style des polices et couleurs
    title_font = ("Helvetica", 16, "bold")
    text_font = ("Helvetica", 12)
    button_font = ("Helvetica", 12, "bold")
    primary_color = "#4CAF50"  # Vert moderne
    secondary_color = "#8BC34A"  # Vert clair
    background_color = "#E8F5E9"  # Vert très clair
    text_color = "#1B5E20"  # Vert foncé

    # Titre de la fenêtre
    title_label = tk.Label(
        result_window,
        text="Résultats du Potentiel Métra",
        font=title_font,
        bg=background_color,
        fg=primary_color,
    )
    title_label.pack(pady=20)

    # Cadre pour contenir les résultats
    result_frame = tk.Frame(result_window, bg=background_color)
    result_frame.pack(pady=10, padx=20, fill="both", expand=True)

    # Afficher les résultats dans un widget Text
    result_text = (
        f"Metra potential calculation results:\n"
        f"Earliest dates: {early_start}\n"
        f"Latest dates: {late_start}\n"
        f"Total project duration: {total_duration}\n"
        f"Critical path: {critical_path}\n"
    )

    result_display = Text(
        result_frame,
        wrap=tk.WORD,
        font=text_font,
        bg="white",
        fg=text_color,
        relief="flat",
        bd=2,
        height=10,
        width=50,
    )
    result_display.insert(tk.END, result_text)
    result_display.config(state="disabled")  # Empêcher l'édition du texte
    result_display.pack(pady=10, padx=10, fill="both", expand=True)

    # Bouton pour fermer la fenêtre
    close_button = tk.Button(
        result_window,
        text="Fermer",
        font=button_font,
        bg=primary_color,
        fg="white",
        activebackground=secondary_color,
        activeforeground="white",
        relief="flat",
        bd=0,
        padx=20,
        pady=10,
        command=result_window.destroy,
    )
    close_button.pack(pady=20)

    # Afficher le graphe en 3D dans une autre fenêtre
    plot_potential_metra_3d(tasks, early_start, total_duration, critical_path)