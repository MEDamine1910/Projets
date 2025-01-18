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


# Algorithme North West Corner
def north_west_corner(factory_capacities, client_demands, transport_costs):
    num_factories = len(factory_capacities)
    num_clients = len(client_demands)
   
    # Matrice de transport initiale
    transport_plan = np.zeros((num_factories, num_clients))
   
    i, j = 0, 0
    while i < num_factories and j < num_clients:
        amount = min(factory_capacities[i], client_demands[j])
        transport_plan[i][j] = amount
        factory_capacities[i] -= amount
        client_demands[j] -= amount
       
        # Si l'usine est saturée, passer à la suivante
        if factory_capacities[i] == 0:
            i += 1
        # Si le client est satisfait, passer au suivant
        if client_demands[j] == 0:
            j += 1
   
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
   
    # Appliquer l'algorithme de North West Corner
    print("\nResult of the North West Corner algorithm :")
    transport_plan_nwc = north_west_corner(factory_capacities.copy(), client_demands.copy(), transport_costs)
    print(pd.DataFrame(transport_plan_nwc, columns=[f"Client {j+1}" for j in range(num_clients)],
                       index=[f"Usine {i+1}" for i in range(num_factories)]))
    # Calcul du coût total pour North West Corner
    total_cost_nwc = calculate_total_cost(transport_plan_nwc, transport_costs)
    print(f"Total cost (North West Corner): {total_cost_nwc}")
# Exécution du programme
if __name__ == "__main__":
  main()