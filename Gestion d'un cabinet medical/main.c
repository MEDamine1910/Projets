#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
typedef struct date {
	int jour;
	int mois;
	int annee;
}date;
typedef struct rendezvous {
int id;
date date;
char heure;
char type;
char Npatient[50];
}rendezvous;
typedef struct historique {
struct rendezvous rdv;
char examens_complementaires[50];
char examens_cliniques[50];
char ordonnance[50];
char observations[50];
}historique;
typedef struct patient {
char nom[50];
char prenom[50];
char sexe[50];
char cin[50];
float numtel;
date date_naissance[50];
char adresse[50];
historique dossier_medicale
}patient;

void gestion_des_rendezvous(){
int k=0,l=0;
printf("-------------------------------------------\n\tGestion des Rendez-Vous\n-------------------------------------------\n       1- Ajouter\n       2- Modifier\n       3- Supprimer\n       4- Chercher\n       5- Planning\n       6- Menu Principale\n-------------------------------------------\n");
scanf("%d",&k);
getch();
system("cls");
switch (k){
	case 1:
		printf("--------------------\n1. Nouveau Patient\n2. Ancien Patient\n3. Retour\n--------------------\n");
		scanf("%d",&l);
		getch();
		system("cls");
		switch (l){
			case 1:
			printf("Erreur");/*nouveau_patient();*/
			getch();
			system("cls");
			break;
			case 2:
			printf("Erreur");/*ancien_patient();*/
			getch();
			system("cls");
			break;
			case 3:
			gestion_des_rendezvous();
			getch();
			system("cls");
			break;
		}
		break;
	case 2:
		printf("--------------------\n1. Date RDV\n2. Type RDV\n3. Retour\n--------------------\n");
		scanf("%d",&l);
		getch();
		system("cls");
		switch(l){
			case 1:
			printf("Erreur");/*date_rdv();*/
			getch();
			system("cls");
			break;
			case 2:
			printf("Erreur");/*type_rdv();*/
			getch();
			system("cls");
			break;
			case 3:
			gestion_des_rendezvous();
			getch();
			system("cls");
			break;
			}
		break;
	case 3:
		printf("--------------------\n1. Par Date\n2. Tout\n3. Retour\n--------------------\n");
		scanf("%d",&l);
		getch();
		system("cls");
			switch(l){
			case 1:
			printf("Erreur");/*supprimer_date();*/
			getch();
			system("cls");
			break;
			case 2:
			printf("Erreur");/*supprimer_tout();*/
			getch();
			system("cls");
			break;
			case 3:
			gestion_des_rendezvous();
			getch();
			system("cls");
			break;
	}
	break;
	case 4:
		printf("--------------------\n1. Par Date (Mois, Jour)\n2. Par Nom\n3. Par Prenom\n4. Par CIN\n5. Par NumTel\n6. Retour\n--------------------\n");
		scanf("%d",&l);
		getch();
		system("cls");
		switch (l){
		case 1:
			printf("Erreur");/*chercher_date();*/
			getch();
			system("cls");
			break;
		case 2:
			printf("Erreur");/*chercher_nom();*/
			getch();
			system("cls");
			break;
		case 3:
			printf("Erreur");/*chercher_prenom();*/
			getch();
			system("cls");
			break;
		case 4:
			printf("Erreur");/*chercher_cin();*/
			getch();
			system("cls");
			break;
		case 5:
			printf("Erreur");/*chercher_numtel();*/
			getch();
			system("cls");
			break;
		case 6:
			gestion_des_rendezvous();
			getch();
			system("cls");
			break;
	}
	break;
	case 5:
		printf("--------------------\n1. Par Jour\n2. Par Mois\n3. Retour\n--------------------\n");
		scanf("%d",&l);
		getch();
		system("cls");
		switch (l){
			case 1:
			printf("Erreur");/*planning_jour();*/
			getch();
			system("cls");
			break;
			case 2:
			printf("Erreur");/*planning_mois();*/
			getch();
			system("cls");
			break;
			case 3:
			gestion_des_rendezvous();
			getch();
			system("cls");
			break;
	}
	break;
	case 6:
	menu_principal();
	getch();
	system("cls");
	break;
}
}
void gestion_de_fiche_patients(){
int k=0,l=0;
printf("-------------------------------------------\n\tGestion de Fiche Patients\n-------------------------------------------\n       1- Ajouter un patient\n       2- Modifier un patient\n       3- Supprimer un patient\n       4- Chercher un patient\n       5- Liste des patients\n       6- Menu Principale\n-------------------------------------------\n");
scanf("%d",&k);
getch();
system("cls");
switch (k){
	case 1:
		printf("Erreur");/*ajouter_patient();*/
		getch();
		system("cls");
		break;
	case 2:
		printf("Erreur");/*modifier_patient();*/
		getch();
		system("cls");
		break;
	case 3:
		printf("Erreur");/*supprimer_patient();*/
		getch();
		system("cls");
		break;
	case 4:
		printf("--------------------\n1. Par Nom\n2. Par Prenom\n3. Par CIN\n4. Par Numtel\n5. Retour\n--------------------\n");
		scanf("%d",&l);
		getch();
		system("cls");
		switch (l){
			case 1:
				printf("Erreur");/*chercher_nom();*/
				getch();
				system("cls");
				break;
			case 2:
				printf("Erreur");/*chercher_prenom();*/
				getch();
				system("cls");
				break;
			case 3:
				printf("Erreur");/*chercher_cin();*/
				getch();
				system("cls");
				break;
			case 4:
				printf("Erreur");/*chercher_numtel();*/
				getch();
				system("cls");
				break;
			case 5:
				gestion_de_fiche_patients();
				getch();
				system("cls");
				break;
	}
		break;
	case 5:
		printf("Erreur");/*liste_patient();*/
		getch();
		system("cls");
		break;
	case 6:
		menu_principal();
		getch();
		system("cls");
		break;
}
}
void menu_principal(){
	int k,c;
	system("mode con cols=80 lines=40");
	system("COLOR 0A");
	printf("--------------------------------------------------------------\n\t\t\tMENU PRINCIPAL\n--------------------------------------------------------------\n       1. Gestion des Rendez-vous.\n       2. Gestion du Fiche Patients.\n       3. QUITTER\n--------------------------------------------------------------\n");
	scanf("%d",&k);
	system("cls");
switch(k){
	case 1:
		gestion_des_rendezvous();
		system("cls");		
		break;
	case 2:
		gestion_de_fiche_patients();
		system("cls");
		break;
	case 3:
		printf("Merci d'avoir choisi notre cabinet medical!!");
		system("cls");
		break;
		return;
}
}
int main(){
menu_principal();
return 0;
}
