#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <thread>
#include <chrono>

// Classe Article
class Article
{
public:
    std::string reference;
    double prix;
    int quantite_stock;

    Article(std::string ref, double price, int stock) : reference(ref), prix(price), quantite_stock(stock) {}

    // Compare deux articles sur la base de leur référence
    bool operator==(const Article& other) const
    {
        return this->reference == other.reference;
    }

    bool operator<(const Article& other) const
    {
        return this->reference < other.reference;
    }
};

// Classe Panier
class Panier
{
private:
    std::map<Article, int> contenu;

public:
    // Fonction pour ajouter un article au panier
    void ajouterArticle(Article& article, int quantite)
{
    if (quantite <= article.quantite_stock)
    {
        contenu[article] += quantite;
        std::cout << "Article ajoute.\n";

        // Mettre à jour la quantité en stock de l'article
        article.quantite_stock -= quantite;

        // Afficher le stock mis à jour
        std::cout << "Stock de l'article " << article.reference << " mis à jour : " << article.quantite_stock << "\n";

        // Mettre à jour l'état de la commande
        std::cout << "Etat de la commande mis à jour : article ajoute.\n";
    }
    else
    {
        std::cout << "Quantité demandée non disponible en stock.\n";
    }
}


    void modifierQuantite(const Article& article, int nouvelleQuantite)
    {
        int k = 0;
        std::string referenc = article.reference;
        for (const auto& pair : contenu)
        {
            if (pair.first.reference == referenc)
            {
                std::cout << "Article Trouve: " << pair.first.reference;
                if (nouvelleQuantite <= pair.first.quantite_stock)
                {
                    contenu[article] = nouvelleQuantite;
                    std::cout << "\nEtat du panier mis à jour : quantite modifiee.\n";
                    k = 1;

                }


            }
        }
        if (k == 0)
        {
            std::cout << "Quantite demandee non disponible en stock.\n";
        }
    }

    void retirerArticle(const Article& article)
    {
        if (contenu.find(article) != contenu.end())
        {
            contenu.erase(article);
            std::cout << "Etat du panier mis à jour : article retire.\n";
        }
    }

    void viderPanier()
    {
        contenu.clear();
        std::cout << "Panier vide.\n";
    }

    double calculerTotal() const
    {
        double total = 0.0;
        for (auto& pair : contenu)
        {
            double prixArticle = (pair.first.prix * pair.second);
            if (pair.second > 10)
            {
                prixArticle *= 0.8; // Remise de 20%
            }
            total += prixArticle;
        }
        return total;
    }

    void afficherPanier() const
    {
        // Copie des éléments du panier dans un vecteur temporaire
        std::vector<std::pair<Article, int>> panierVector(contenu.begin(), contenu.end());

        // Fonction de comparaison pour trier le vecteur en fonction du prix de chaque article
        auto comparerPrix = [](const std::pair<Article, int>& a, const std::pair<Article, int>& b) {
            return a.first.prix < b.first.prix;
        };

        // Tri du vecteur en fonction du prix de chaque article (croissant)
        std::sort(panierVector.begin(), panierVector.end(), comparerPrix);

        // Affichage des articles du panier triés par prix
        for (const auto& pair : panierVector)
        {
            std::cout << "\n+---------------------------------------------------------+";
            std::cout << "Reference: " << pair.first.reference << ", Quantite: " << pair.second << ", Prix unitaire: " << pair.first.prix << "\n";
            std::cout << "\n+---------------------------------------------------------+";
        }
    }

    Article trouverArticlePlusCher() const
    {
        return (*std::max_element(contenu.begin(), contenu.end(),
            [](const std::pair<Article, int>& a, const std::pair<Article, int>& b)
            {
                return a.first.prix < b.first.prix;
            })).first;
    }

    void afficherArticlesDansPlageDePrix(double minPrix, double maxPrix) const
    {
        std::for_each(contenu.begin(), contenu.end(), [minPrix, maxPrix](const std::pair<Article, int>& pair)
            {
                if (pair.first.prix >= minPrix && pair.first.prix <= maxPrix)
                {
                    std::cout << "Reference: " << pair.first.reference << ", Prix: " << pair.first.prix << "\n";
                }
            });
    }

    const Article* obtenirInfosArticle(const std::string& reference) const
    {
        auto it = std::find_if(contenu.begin(), contenu.end(), [&reference](const std::pair<Article, int>& pair)
            {
                return pair.first.reference == reference;
            });
        return (it != contenu.end()) ? &it->first : nullptr;
    }
};

// Classe Client
class Client 
{
public:
    std::string email;
    std::string nom;
    Panier panier;

    Client(std::string email, std::string nom) : email(email), nom(nom) {}
    
    void saisirNom()
    {
        std::cout << "\n+-------------------------------------+";
        std::cout << "\n| Veuillez entrer votre nom : ";
        std::cin >> nom;
    }

    void afficherDetails() const
    {
        std::cout << "Nom du client: " << nom << "\n";
        std::cout << "Email du client: " << email << "\n";
    }
};

// Classe Commande
class Commande
{
public:
    int numero;
    Client client;
    Panier panier;
    std::string etat;

    Commande(int num, const Client& cli) : numero(num), client(cli), etat("En attente de traitement") {}

    void afficherEtat() const
    {
        std::cout << "Etat de la commande: " << etat << "\n";
    }

};


int main()
{
    int numeroCommande = 1;
    Panier panier;
    std::string reference;
    std::string confirmation;
    double prix;
    int quantite, choix;
    int stock;
    const std::string defaultEmail = "yassinesefiani3547@gmail.com";
    while (true)
    {
        std::string email;
        std::cout << "  _____    _______   __   ___          \n";
        std::cout << " |  __ \\  |  _____| |  | /  /          \n";
        std::cout << " | |  | | |  |____  |  |/  /          \n";
        std::cout << " | |  | | |   ____| |     \\        \n";
        std::cout << " | |__| | |  |      |  |\\  \\     \n";
        std::cout << " |_____/  |__|      |__| \\__\\        \n";
        std::cout << "\n+-----------------------------------+";
        std::cout << "\n|          Connexion Client         |";
        std::cout << "\n+-----------------------------------+";
        std::cout << "\n| Entrez votre email : ";
        std::cin >> email;

        if (email == defaultEmail)
        {
            std::cout << "\n| Loading !                         |";
            std::this_thread::sleep_for(std::chrono::seconds(3));
            std::cout << "\n| Connexion reussie. Bienvenue !    |";
            std::cout << "\n+-----------------------------------+";
            std::this_thread::sleep_for(std::chrono::seconds(2));
            std::system("cls");
            break;
        }
        else
        {
            std::cout << "\n| Loading !                         |";
            std::this_thread::sleep_for(std::chrono::seconds(3));
            std::cout << "\n| Adresse email incorrecte !        |";
            std::cout << "\n+-----------------------------------+";
        }
    }
    Client client(defaultEmail, "");
    client.saisirNom();
    client.panier;
    Commande nouvelleCommande(numeroCommande++, client);
    nouvelleCommande.panier = client.panier;
    std::this_thread::sleep_for(std::chrono::seconds(3));
    std::system("cls");
    
    while (true)
    {
        std::cout << "\n+---------------------------------------------------------+";
        std::cout << "\n|            Menu du Panier Virtuel                       |";
        std::cout << "\n+---------------------------------------------------------+";
        std::cout << "\n|  1. Ajouter un Article au Stock                         |";
        std::cout << "\n|  2. Modifier la Quantite d'un Article                   |";
        std::cout << "\n|  3. Retirer un Article                                  |";
        std::cout << "\n|  4. Vider le Panier                                     |";
        std::cout << "\n|  5. Afficher le Panier                                  |";
        std::cout << "\n|  6. Afficher le Montant Total du Panier                 |";
        std::cout << "\n|  7. Trouver l'Article le Plus Cher                      |";
        std::cout << "\n|  8. Afficher les Articles dans une Plage de Prix        |";
        std::cout << "\n|  9. Obtenir les Informations d'un Article par Reference |";
        std::cout << "\n|  10. Afficher les Informations du Client                |";
        std::cout << "\n|  11. Proceder au Payement                               |";
        std::cout << "\n|  12. Quitter                                            |";
        std::cout << "\n+---------------------------------------------------------+";
        std::cout << "\nChoisissez une option: ";
        std::cin >> choix;
        std::system("cls");

        switch (choix)
        {
        case 1:
        {
            nouvelleCommande.etat = "En cours de preparation.";
            std::cout << "Entrer la reference, le prix, et la quantite en stock de l'article: ";
            std::cin >> reference >> prix >> stock;
            std::cout << "Entrer la quantite a ajouter: ";
            std::cin >> quantite;
            Article article(reference, prix, stock);
            client.panier.ajouterArticle(article, quantite);
            std::this_thread::sleep_for(std::chrono::seconds(1));
            std::system("cls");
            break;
        }
        case 2:
        {
            nouvelleCommande.etat = "En cours de preparation.";
            std::cout << "Entrer la reference de l'article a modifier: ";
            std::cin >> reference;
            std::cout << "Entrer la nouvelle quantite: ";
            std::cin >> quantite;
            Article tempArticle(reference, 0, 0);  // Prix et stock ne sont pas utilisés ici
            client.panier.modifierQuantite(tempArticle, quantite);
            std::this_thread::sleep_for(std::chrono::seconds(1));
            std::system("cls");
            break;
        }
        case 3:
        {
            nouvelleCommande.etat = "En cours de preparation.";
            std::cout << "Entrer la reference de l'article a retirer: ";
            std::cin >> reference;
            Article tempArticle(reference, 0, 0);
            client.panier.retirerArticle(tempArticle);
            std::this_thread::sleep_for(std::chrono::seconds(1));
            std::system("cls");
            break;
        }
        case 4:
            nouvelleCommande.etat = "En attente de traitement.";
            client.panier.viderPanier();
            std::this_thread::sleep_for(std::chrono::seconds(1));
            std::system("cls");
            break;
        case 5:
            client.panier.afficherPanier();
            std::this_thread::sleep_for(std::chrono::seconds(3));
            std::system("cls");
            break;
        case 6:
            std::cout << "Montant total du panier: " << client.panier.calculerTotal() << " EUR\n";
            std::this_thread::sleep_for(std::chrono::seconds(3));
            std::system("cls");
            break;
        case 7:
        {
            Article cher = client.panier.trouverArticlePlusCher();
            std::cout << "L'article le plus cher est: " << cher.reference << " au prix de " << cher.prix << " DHS\n";
            std::this_thread::sleep_for(std::chrono::seconds(3));
            std::system("cls");
            break;
        }
        case 8:
        {
            double minPrix, maxPrix;
            std::cout << "\nEntrer le prix minimum et maximum: ";
            std::cin >> minPrix >> maxPrix;
            client.panier.afficherArticlesDansPlageDePrix(minPrix, maxPrix);
            std::this_thread::sleep_for(std::chrono::seconds(2));
            std::system("cls");
            break;
        }
        case 9:
        {
            std::cout << "Entrer la reference de l'article recherche: ";
            std::cin >> reference;
            const Article* info = client.panier.obtenirInfosArticle(reference);
            if (info)
            {
                std::cout << "Article: " << info->reference << ", Prix: " << info->prix << ", Quantite en stock: " << info->quantite_stock << "\n";
            }
            else
            {
                std::cout << "Aucun article trouvé avec cette reference.\n";
            }
            std::this_thread::sleep_for(std::chrono::seconds(2));
            std::system("cls");
            break;
        }
        case 10:
            client.afficherDetails();
            nouvelleCommande.afficherEtat();
            std::this_thread::sleep_for(std::chrono::seconds(3));
            std::system("cls");
            break;
        case 11:
            std::cout << "Montant total du panier: " << client.panier.calculerTotal() << " EUR\n";
            std::cout << "Confirmez-vous cet achat ? : Yes/No \n";
            std::cin >> confirmation;
            if (confirmation == "Yes") {
                nouvelleCommande.etat = "En cours de d'expedition.";
                std::cout << "Nous vous remercions sincerement pour votre achat dans notre application !";
                std::cout << "Votre Commande sera en cours de livraison tres bientot !";
                std::this_thread::sleep_for(std::chrono::seconds(2));
                std::system("cls");
                break;
            }
            else{
            std::this_thread::sleep_for(std::chrono::seconds(2));
            std::system("cls"); 
            break;
            }
        case 12:
            std::cout << "Nous vous remercions chaleureusement pour avoir utilise notre programme !";
            std::this_thread::sleep_for(std::chrono::seconds(3));
            exit(EXIT_SUCCESS);
        default:
            std::cout << "Option invalide. Veuillez choisir une option valide.\n";
        }
               // Clearing cin errors and ignoring the rest of the input until a new line is found
               std::cin.clear();
               std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }

        return 0;
}