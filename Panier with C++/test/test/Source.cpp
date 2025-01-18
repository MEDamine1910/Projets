#include <iostream>

int main() {
    std::cout << "\n+-------------------------------------+";
    std::cout << "\n| Veuillez entrer votre nom : ";
    std::cout << "\n+-------------------------------------+\n";

    std::string nom;
    std::getline(std::cin, nom); // Lire une ligne de texte saisie par l'utilisateur

    // Affichage du nom saisi dans le tableau ASCII
    std::cout << "\n+-------------------------------------+";
    std::cout << "\n|                " << nom;
    std::cout << "\n+-------------------------------------+\n";

    return 0;
}