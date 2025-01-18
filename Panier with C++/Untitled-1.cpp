#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <string>

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
    void ajouterArticle(const Article& article, int quantite)
    {
        if (quantite <= article.quantite_stock)
        {
            contenu[article] += quantite;
            std::cout << "Article ajouté.\n";
        }
        else
        {
            std::cout << "Quantite demandee non disponible en stock.\n";
        }
    }

    void modifierQuantite(const Article& article, int nouvelleQuantite)
    {
        int k = 0;
        std::string referenc=article.reference;
        for (const auto& pair : contenu)
        {
            if (pair.first.reference == referenc)
            {
                std::cout << "Article found: " << pair.first.reference;
                if (nouvelleQuantite <= pair.first.quantite_stock)
                {
                    contenu[article] = nouvelleQuantite;
                    std::cout << "Quantite modifiee.\n";
                    k = 1;

                }


            }
        }
        if (k==0)
        {
            std::cout << "Quantite demandee non disponible en stock.\n";
        }
    }

    void retirerArticle(const Article& article)
    {
        if (contenu.find(article) != contenu.end())
        {
            contenu.erase(article);
            std::cout << "Article retire du panier.\n";
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
        for (auto& pair : contenu)
        {
            std::cout << "Reference: " << pair.first.reference << ", Quantite: " << pair.second << ", Prix unitaire: " << pair.first.prix << "\n";
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

    Client(std::string email, std::string nom) : email(email), nom(nom) {}
};

// Classe Commande
class Commande
{
public:
    int numero;
    Client client;
    Panier panier;
    std::string etat;

    Commande(int num, const Client& cli) : numero(num), client(cli), etat("en attente de traitement") {}

    void afficherEtat() const
    {
        std::cout << "Etat de la commande: " << etat << "\n";
    }
};


int main()
{
    Panier panier;
    std::string reference;
    double prix;
    int quantite, choix;
    int stock;

    while (true)
    {
        std::cout << "\nMenu du Panier Virtuel\n";
        std::cout << "1. Ajouter un Article\n";
        std::cout << "2. Modifier la Quantite d'un Article\n";
        std::cout << "3. Retirer un Article\n";
        std::cout << "4. Vider le Panier\n";
        std::cout << "5. Afficher le Panier\n";
        std::cout << "6. Afficher le Montant Total du Panier\n";
        std::cout << "7. Trouver l'Article le Plus Cher\n";
        std::cout << "8. Afficher les Articles dans une Plage de Prix\n";
        std::cout << "9. Obtenir les Informations d'un Article par Reference\n";
        std::cout << "10. Quitter\n";
        std::cout << "Choisissez une option: ";
        std::cin >> choix;
        std::system("cls");

        switch (choix)
        {
        case 1:
        {
            std::cout << "Entrer la reference, le prix, et la quantite en stock de l'article: ";
            std::cin >> reference >> prix >> stock;
            std::cout << "Entrer la quantite a ajouter: ";
            std::cin >> quantite;
            Article article(reference, prix, stock);
            panier.ajouterArticle(article, quantite);
            break;
        }
        case 2:
        {
            std::cout << "Entrer la reference de l'article a modifier: ";
            std::cin >> reference;
            std::cout << "Entrer la nouvelle quantite: ";
            std::cin >> quantite;
            Article tempArticle(reference, 0, 0);  // Prix et stock ne sont pas utilisés ici
            panier.modifierQuantite(tempArticle, quantite);
            break;
        }
        case 3:
        {
            std::cout << "Entrer la reference de l'article a retirer: ";
            std::cin >> reference;
            Article tempArticle(reference, 0, 0);
            panier.retirerArticle(tempArticle);
            break;
        }
        case 4:
            panier.viderPanier();
            break;
        case 5:
            panier.afficherPanier();
            break;
        case 6:
            std::cout << "Montant total du panier: " << panier.calculerTotal() << " EUR\n";
            break;
        case 7:
        {
            Article cher = panier.trouverArticlePlusCher();
            std::cout << "L'article le plus cher est: " << cher.reference << " au prix de " << cher.prix << " DHS\n";
            break;
        }
        case 8:
        {
            double minPrix, maxPrix;
            std::cout << "Entrer le prix minimum et maximum: ";
            std::cin >> minPrix >> maxPrix;
            panier.afficherArticlesDansPlageDePrix(minPrix, maxPrix);
            break;
        }
        case 9:
        {
            std::cout << "Entrer la reference de l'article recherche: ";
            std::cin >> reference;
            const Article* info = panier.obtenirInfosArticle(reference);
            if (info)
            {
                std::cout << "Article: " << info->reference << ", Prix: " << info->prix << ", Quantité en stock: " << info->quantite_stock << "\n";
            }
            else
            {
                std::cout << "Aucun article trouvé avec cette reference.\n";
            }
            break;
        }
        case 10:
            std::cout << "Quitter\n";
            return 0;
        default:
            std::cout << "Option invalide. Veuillez choisir une option valide.\n";
        }
        // Clearing cin errors and ignoring the rest of the input until a new line is found
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }

    return 0;
}