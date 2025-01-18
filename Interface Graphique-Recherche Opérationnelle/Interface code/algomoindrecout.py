import numpy as np
import random
import pandas as pd  # Pour un affichage lisible


# Étape 1 : Générer les données aléatoires
def generate_data(num_factories, num_clients):
    # Capacités des usines
    factory_capacities = [random.randint(50, 150) for _ in range(num_factories)]
   
    # Demandes des clients
    client_demands = [random.randint(50, 150) for _ in range(num_clients)]
   
    # Coûts de transport (matrice des coûts entre usines et clients)
    transport_costs = np.random.randint(1, 10, size=(num_factories, num_clients))
   
    return factory_capacities, client_demands, transport_costs


# Fonction pour calculer le coût total
def calculate_total_cost(transport_plan, transport_costs):
    return np.sum(transport_plan * transport_costs)

# Algorithme Moindre Coût
def moindre_cout(factory_capacities, client_demands, transport_costs):
    num_factories = len(factory_capacities)
    num_clients = len(client_demands)
   
    # Matrice de transport initiale
    transport_plan = np.zeros((num_factories, num_clients))
   
    # Création d'une liste des coûts avec indices
    cost_list = [(i, j, transport_costs[i][j]) for i in range(num_factories) for j in range(num_clients)]
    cost_list.sort(key=lambda x: x[2])  # Trier par coût croissant
   
    for i, j, _ in cost_list:
        if factory_capacities[i] > 0 and client_demands[j] > 0:
            amount = min(factory_capacities[i], client_demands[j])
            transport_plan[i][j] = amount
            factory_capacities[i] -= amount
            client_demands[j] -= amount
   
    return transport_plan

# Main
def main():
    num_factories = int(input("Enter the number of factories : "))
    num_clients = int(input("Enter the number of customers : "))
   
    # Génération des données aléatoires
    factory_capacities, client_demands, transport_costs = generate_data(num_factories, num_clients)
   
    print("\nFactory capacities :")
    print(pd.DataFrame(factory_capacities, columns=["Capacities"], index=[f"Factory {i+1}" for i in range(num_factories)]))
   
    print("\nCustomer requests :")
    print(pd.DataFrame(client_demands, columns=["Requests"], index=[f"Client {j+1}" for j in range(num_clients)]))
   
    print("\nTransportation costs :")
    print(pd.DataFrame(transport_costs, columns=[f"Client {j+1}" for j in range(num_clients)],
                       index=[f"Usine {i+1}" for i in range(num_factories)]))
    # Réinitialisation des données pour l'algorithme Moindre Coût
    factory_capacities, client_demands, _ = generate_data(num_factories, num_clients)
   
    # Appliquer l'algorithme de Moindre Coût
    print("\nResult of the Moindre Cout algorithm :")
    transport_plan_moindre = moindre_cout(factory_capacities.copy(), client_demands.copy(), transport_costs)
    print(pd.DataFrame(transport_plan_moindre, columns=[f"Client {j+1}" for j in range(num_clients)],
                       index=[f"Usine {i+1}" for i in range(num_factories)]))
    # Calcul du coût total pour Moindre Coût
    total_cost_moindre = calculate_total_cost(transport_plan_moindre, transport_costs)
    print(f"Total cost (Moindre Coût): {total_cost_moindre}")
   
# Exécution du programme
if __name__ == "__main__":
  main()
  