#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>
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
char cin[8];
float numtel;
date daten;
char adresse[50];
historique dossiermed;
}patient;
typedef struct liste {
patient p;
struct liste *next;
}liste;
void planning_mois(liste *head,int mois){
liste *s;
s=head;
printf("Planning du mois %d\n",mois);
while(s!=NULL){
    if(s->p.dossiermed.rdv.date.mois == mois){
        printf("---------------------------------\n");
        printf("Nom : %s\nPrenom : %s\n",s->p.nom,s->p.prenom);
    }
    s=s->next;
}
printf("----------------------------------\n");
getch();
system("cls");
gestion_de_fiche_patients(head);
}
void planning_jour(liste *head,int jour){
liste *s;
s=head;
printf("Planning du jour %d\n",jour);
while(s!=NULL){
    if(s->p.dossiermed.rdv.date.jour == jour){
        printf("---------------------------------\n");
        printf("Nom : %s\nPrenom : %s\n",s->p.nom,s->p.prenom);
    }
    s=s->next;
}
printf("----------------------------------\n");
getch();
system("cls");
gestion_de_fiche_patients(head);
}
liste *chercher_date(liste *head,int j,int m){
liste *s;
liste *p;
s=head;
while(s->p.dossiermed.rdv.date.jour != j && s->p.dossiermed.rdv.date.mois != m){

    s=s->next;
}if(s->p.dossiermed.rdv.date.jour == j && s->p.dossiermed.rdv.date.mois == m){
        printf("---------------------------------\n");
        printf("Nom : %s\nPrenom : %s\n",s->p.nom,s->p.prenom);

}
printf("----------------------------------\n");
getch();
system("cls");
gestion_de_fiche_patients(head);
}
void supprimer_date(liste *head,int mois){
liste *s;
liste *p;
s=head;
if( s->p.dossiermed.rdv.date.mois == mois ){
    p = s;
    head = s->next;
    free(p);
    printf("Les donnees ont ete supprimes");
    getch();
    system("cls");
    gestion_des_rendezvous(head);
}
printf("Les donnees ont ete supprimes");
getch();
system("cls");
gestion_des_rendezvous(head);
}
void type_rdv(liste *head,int id){
liste *s;
int f=0;
s=head;
while(s->p.dossiermed.rdv.id != id){
    s=s->next;
}
if(s->p.dossiermed.rdv.id == id){
    printf("entrez le type : \n 1.Consultation \n 2.Controle \n");
scanf("%d",&f);
printf("\n");
switch (f){
case 1:
    printf("Consultation\n");
    /strcpy(s->p.dossiermed.rdv.type,consultation);/
break;
case 2:
    printf("Controle\n");
    /strcpy(s->p.dossiermed.rdv.type,controle);/
    break;
    }
}
getch();
system("cls");
gestion_des_rendezvous(head);
}
void date_rdv(liste *head,int id){
liste *s;
s=head;
while(s->p.dossiermed.rdv.id != id){
    s=s->next;
}
if(s->p.dossiermed.rdv.id == id){
/do{/
printf("entrez la date de rendez-vous : ");
      scanf("%d", &s->p.dossiermed.rdv.date.jour);
      scanf("%d",&s->p.dossiermed.rdv.date.mois );
      scanf("%d",&s->p.dossiermed.rdv.date.annee);
/}while (s->p.dossiermed.rdv.date.jour>31 || s->p.dossiermed.rdv.date.jour<0 || s->p.dossiermed.rdv.date.mois>12 || s->p.dossiermed.rdv.date.mois<0 || s->p.dossiermed.rdv.date.annee>2023 || s->p.dossiermed.rdv.date.annee<0 );/}
getch();
system("cls");
gestion_des_rendezvous(head);
}
void ancien_patient(liste *head,int id){
liste *s;
int f=0;
s=head;
while(s->p.dossiermed.rdv.id != id){

    s=s->next;
}
if(s->p.dossiermed.rdv.id == id){
printf("entrez votre nom : ");
scanf("%s",s->p.nom);
printf("\n");
printf("entrez votre prenom : ");
scanf("%s" ,s->p.prenom);
printf("\n");
/do{/
printf("entrez la date de rendez-vous : ");
      scanf("%d", &s->p.dossiermed.rdv.date.jour);
      scanf("%d",&s->p.dossiermed.rdv.date.mois );
      scanf("%d",&s->p.dossiermed.rdv.date.annee);
/}while (s->p.dossiermed.rdv.date.jour>31 || s->p.dossiermed.rdv.date.jour<0 || s->p.dossiermed.rdv.date.mois>12 || s->p.dossiermed.rdv.date.mois<0 || s->p.dossiermed.rdv.date.annee>2023 || s->p.dossiermed.rdv.date.annee<0 );//*printf("entrez votre heure : ");
scanf("%s" ,s->p.dossiermed.rdv.heure);   //16:12//
printf("\n");
/do{/
printf("entrez votre id : ");
scanf("%d",&s->p.dossiermed.rdv.id);
printf("\n");
/*while(s!=NULL){
    if(s->p.dossiermed.rdv.id = p->p.dossiermed.rdv.id){                //probleme id affiche pas le reste//
        j++;
    }
    s=s->next;
}*/
printf("entrez le type : \n 1.Consultation \n 2.Controle \n");
scanf("%d",&f);
printf("\n");
switch (f){
case 1:
    printf("Consultation\n");
    /strcpy(s->p.dossiermed.rdv.type,consultation);/
break;
case 2:
    printf("Controle\n");
    /strcpy(s->p.dossiermed.rdv.type,controle);/
    break;
    }
printf("\n Les donnees sont enregistrees avec succes. ");
getch();
system("cls");
gestion_des_rendezvous(head);
}/*else{
    printf("\n L'id saisit n'existe pas. \nVoulez-vous modifier un patient ?\n1.Oui\n2.Non\n");
    scanf("%d",&k);
    if(k==1){
        printf("saisir un nouveau id :\n");
        scanf("%d",&id);
        getch();
        system("cls");
        modifier_patient(head,id);
}else{
        getch();
        system("cls");
        gestion_deS_rendezvous(head);
}
}*/
}
void nouveau_patient(liste *head){
liste *p=malloc(sizeof(patient));
liste *s;
int f=0;
s=head;
printf("entrez votre nom : ");
scanf("%s",p->p.nom);
printf("\n");
printf("entrez votre prenom : ");
scanf("%s" ,p->p.prenom);
printf("\n");
/do{/
printf("entrez la date de rendez-vous : ");
      scanf("%d", &s->p.dossiermed.rdv.date.jour);
      scanf("%d",&s->p.dossiermed.rdv.date.mois );
      scanf("%d",&s->p.dossiermed.rdv.date.annee);
/}while (s->p.dossiermed.rdv.date.jour>31 || s->p.dossiermed.rdv.date.jour<0 || s->p.dossiermed.rdv.date.mois>12 || s->p.dossiermed.rdv.date.mois<0 || s->p.dossiermed.rdv.date.annee>2023 || s->p.dossiermed.rdv.date.annee<0 );/
/*printf("entrez l'heure : ");
scanf("%s" ,p->p.dossiermed.rdv.heure);   //16:12//
printf("\n");
/do{/
printf("entrez votre id : ");
scanf("%d",&p->p.dossiermed.rdv.id);
printf("\n");
/*while(s!=NULL){
    if(s->p.dossiermed.rdv.id = p->p.dossiermed.rdv.id){                //probleme id affiche pas le reste//
        j++;
    }
    s=s->next;
}*/
printf("saisir le type du rendez-vous : \n 1.Consultation \n 2.Controle \n");
scanf("%d",&f);
printf("\n");
switch (f){
case 1:
    printf("Consultation\n");
    /strcpy(s->p.dossiermed.rdv.type,consultation);/
break;
case 2:
    printf("Controle\n");
    /strcpy(s->p.dossiermed.rdv.type,controle);/
    break;
    }
printf("\n Les donnees sont enregistrees avec succes");
p->next = head;
head = p;
getch();
system("cls");
gestion_des_rendezvous(head);
}
void liste_patient(head){
liste *s;
s=head;
while(s->next->next!=NULL){
     printf("---------------------------------\n");
        printf("Nom : %s\nPrenom : %s\n",s->p.nom,s->p.prenom);
s=s->next;
}
printf("---------------------------------\n");
getch();
system("cls");
gestion_de_fiche_patients(head);
}
void chercher_nom(liste *head,char *o[]){
liste *s;
s=head;
/*while(s->p.nom != o){

    s=s->next;
}if(s->p.nom == o){
        printf("---------------------------------\n");
}
printf("---------------------------------\n");*/
getch();
system("cls");
gestion_de_fiche_patients(head);
}
void *chercher_prenom(liste *head,char *o[]){
liste *s;
liste *p;
s=head;
/*while(s->p.nom != o){

    s=s->next;
}if(s->p.nom == o){
        printf("---------------------------------\n");
}
printf("---------------------------------\n");*/
getch();
system("cls");
gestion_de_fiche_patients(head);

}
liste *chercher_cin(liste *head,char *o[]){
liste *s;
liste *p;
s=head;
/*while(s->p.nom != o){

    s=s->next;
}if(s->p.nom == o){
        printf("---------------------------------\n");
}
printf("---------------------------------\n");*/
getch();
system("cls");
gestion_de_fiche_patients(head);
}
liste *chercher_numtel(liste *head,float numtel){
liste *s;
liste *p;
s=head;
while(s->p.numtel != numtel){

    s=s->next;
}if(s->p.numtel == numtel){
        printf("---------------------------------\n");
        printf("Nom : %s\nPrenom : %s\n",s->p.nom,s->p.prenom);

}
printf("----------------------------------\n");
getch();
system("cls");
gestion_de_fiche_patients(head);
}
void ajouter_patient(liste *head){
liste *p=malloc(sizeof(patient));
liste *s;
int j=0;
int f=0;
s=head;
printf("entrez votre nom : ");
scanf("%s",p->p.nom);
printf("\n");
printf("entrez votre prenom : ");
scanf("%s" ,p->p.prenom);
printf("\n");
printf("entrez votre sexe : \n 1.Masculin \n 2.Feminin \n");
scanf("%d",&f);
printf("\n");
switch (f){
case 1:
    printf("masculin\n");
    /strcpy(p->p.sexe,masculin);/
break;
case 2:
    printf("feminin\n");
    /strcpy(p->p.sexe,feminin);/
    break;
    }
printf("entrez votre CIN : ");
scanf("%s",p->p.cin);
printf("\n");
printf("entrez votre numero de telephone : ");
scanf("%f",&p->p.numtel);
printf("\n");
do{
printf("entrez votre date de naissance : ");
scanf("%d  ", &p->p.daten.jour);
      scanf("%d",&p->p.daten.mois );
      scanf("%d",&p->p.daten.annee);
}while (p->p.daten.jour>31 || p->p.daten.jour<0 || p->p.daten.mois>12 || p->p.daten.mois<0 || p->p.daten.annee>2023 || p->p.daten.annee<0 );
printf("entrez votre adresse : ");
scanf("%s",p->p.adresse);
printf("\n");
/do{/
printf("entrez votre id : ");
scanf("%d",&p->p.dossiermed.rdv.id);
printf("\n");
/*while(s!=NULL){
    if(s->p.dossiermed.rdv.id = p->p.dossiermed.rdv.id){                //probleme id affiche pas le reste//
        j++;
    }
    s=s->next;
}
}while( j != 0 );
printf("entrez votre examens complementaires : ");
scanf("%s",p->p.dossiermed.examens_complementaires);  //probleme scanf char//
printf("\n");
printf("entrez votre examens cliniques : ");
scanf("%s",p->p.dossiermed.examens_cliniques);
printf("\n");
printf("entrez votre ordonnance : ");
scanf("%s",p->p.dossiermed.ordonnance);
printf("\n");
printf("entrez votre observations : ");
scanf("%s",p->p.dossiermed.observations);
printf("\n");*/
printf("\n Les donnees sont enregistrees avec succes. ");
p->next = head;
head = p;
getch();
system("cls");
gestion_de_fiche_patients(head);
}
void modifier_patient(liste *head,int id){
liste *s;
int f=0;
int k=0;
s=head;
while(s->p.dossiermed.rdv.id != id){

    s=s->next;
}
if(s->p.dossiermed.rdv.id == id){
printf("entrez votre nom : ");
scanf("%s",s->p.nom);
printf("\n");
printf("entrez votre prenom : ");
scanf("%s" ,s->p.prenom);
printf("\n");
printf("entrez votre sexe : \n 1.Masculin \n 2.Feminin \n");
scanf("%d",&f);
printf("\n");
switch (f){
case 1:
    printf("masculin\n");
    /strcpy(s->p.sexe,masculin);/
break;
case 2:
    printf("feminin\n");
    /strcpy(s->p.sexe,feminin);/
    break;
    }
printf("entrez votre CIN : ");
scanf("%s",s->p.cin);
printf("\n");
printf("entrez votre numero de telephone : ");
scanf("%f",&s->p.numtel);
printf("\n");
do{
printf("entrez votre date de naissance : ");
scanf("%d  ", &s->p.daten.jour);
      scanf("%d",&s->p.daten.mois );
      scanf("%d",&s->p.daten.annee);
}while (s->p.daten.jour>31 || s->p.daten.jour<0 || s->p.daten.mois>12 || s->p.daten.mois<0 || s->p.daten.annee>2023 || s->p.daten.annee<0 );
printf("entrez votre adresse : ");
scanf("%s",s->p.adresse);
printf("\n");
/*printf("entrez votre examens complementaires : ");
scanf("%s",s->p.dossiermed.examens_complementaires);  //probleme scanf char//
printf("\n");
printf("entrez votre examens cliniques : ");
scanf("%s",s->p.dossiermed.examens_cliniques);
printf("\n");
printf("entrez votre ordonnance : ");
scanf("%s",s->p.dossiermed.ordonnance);
printf("\n");
printf("entrez votre observations : ");
scanf("%s",s->p.dossiermed.observations);
printf("\n");*/
printf("\n Les donnees sont modifies avec succes. ");
getch();
system("cls");
gestion_de_fiche_patients(head);
}/*else{
    printf("\n L'id que vous avez saisit n'existe pas. \nVoulez-vous modifier un patient ?\n1.Oui\n2.Non\n");
    scanf("%d",&k);
    if(k==1){
        printf("saisir un nouveau id :\n");
        scanf("%d",&id);
        getch();
        system("cls");
        modifier_patient(head,id);
}else{
        getch();
        system("cls");
        gestion_de_fiche_patients(head);
}
}*/
}
void supprimer_patient(liste *head,int id){
liste *s;
liste *p;
s=head;
while(s->p.dossiermed.rdv.id != id){
    s=s->next;
}
p=s->next;
s->next=s->next->next;
free(p);
printf("\n Le patient a ete supprime avec succes. ");
getch();
system("cls");
gestion_de_fiche_patients(head);
}
void gestion_des_rendezvous(liste *head){
int k=0,l=0,id=0,jour=0,mois=0,annee=0,numtel=0;
liste *s;
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
			nouveau_patient(head);
			getch();
			system("cls");
			break;
			case 2:
            printf("saisir l'id : \n");
            scanf("%d",&id);
			ancien_patient(head,id);
			getch();
			system("cls");
			break;
			case 3:
			gestion_des_rendezvous(head);
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
            printf("saisir l'id : \n");
            scanf("%d",&id);
			date_rdv(head,id);
			getch();
			system("cls");
			break;
			case 2:
            printf("saisir l'id : \n");
            scanf("%d",&id);
			type_rdv(head,id);
			getch();
			system("cls");
			break;
			case 3:
			gestion_des_rendezvous(head);
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
            printf("saisir la date : \n");
            scanf("%d\n",&mois);
			supprimer_date(head,mois);
			getch();
			system("cls");
			break;
			case 2:
            s = head;
			free(s);
			getch();
			system("cls");
			gestion_des_rendezvous(head);
			break;
			case 3:
			gestion_des_rendezvous(head);
			getch();
			system("cls");
			break;
	}
	break;
	case 4:
		printf("--------------------\n1. Par Date\n2. Par Nom\n3. Par Prenom\n4. Par CIN\n5. Par NumTel\n6. Retour\n--------------------\n");
		scanf("%d",&l);
		getch();
		system("cls");
		switch (l){
		case 1:
			printf("saisir la date : \n");
			    scanf("%d\n%d",&jour,&mois);
				chercher_date(head,jour,mois);
			getch();
			system("cls");
			break;
		case 2:
			printf("Erreur");/chercher_nom();/
			getch();
			system("cls");
			break;
		case 3:
			printf("Erreur");/chercher_prenom();/
			getch();
			system("cls");
			break;
		case 4:
			printf("Erreur");/chercher_cin();/
			getch();
			system("cls");
			break;
		case 5:
			  printf("saisir le numTel : \n");
			    scanf("%f",&numtel);
				chercher_numtel(head,numtel);
			getch();
			system("cls");
			break;
		case 6:
			gestion_des_rendezvous(head);
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
			    printf("saisir le jour : \n");
			    scanf("%d",&jour);
			planning_jour(head,jour);
			getch();
			system("cls");
			break;
			case 2:
			    printf("saisir le mois : \n");
			    scanf("%d",&mois);
			planning_mois(head,mois);
			getch();
			system("cls");
			break;
			case 3:
			gestion_des_rendezvous(head);
			getch();
			system("cls");
			break;
	}
	break;
	case 6:
	menu_principal(head);
	getch();
	system("cls");
	break;
}
}
void gestion_de_fiche_patients(liste *head){
int k=0,l=0;
float numtel=0;
int id=0;
char o[50];
float m;
printf("-------------------------------------------\n\tGestion de Fiche Patients\n-------------------------------------------\n       1- Ajouter un patient\n       2- Modifier un patient\n       3- Supprimer un patient\n       4- Chercher un patient\n       5- Liste des patients\n       6- Menu Principale\n-------------------------------------------\n");
scanf("%d",&k);
getch();
system("cls");
switch (k){
	case 1:
		ajouter_patient(head);
		getch();
		system("cls");
		break;
	case 2:
	    printf("Entrez l'id pour modifier.\n");
	    scanf("%d",&id);
		modifier_patient(head,id);
		getch();
		system("cls");
		break;
	case 3:
	    printf("Entrez l'id pour supprimer.\n");
	    scanf("%d",&id);
		supprimer_patient(head,id);
		id=0;
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
			    printf("saisir le nom : \n");
			    scanf("%s",&o);
				chercher_nom(head,o);
				getch();
				system("cls");
				break;
			case 2:
				printf("saisir le prenom : \n");
				gets(o);/p=chercher_prenom(head,o);/
				getch();
				system("cls");
				break;
			case 3:
			    printf("saisir le CIN : \n");
			    gets(o);
				printf("Erreur");/p=chercher_cin(head,o);/
				getch();
				system("cls");
				break;
			case 4:
			    printf("saisir le numTel : \n");
			    scanf("%f",&numtel);
				chercher_numtel(head,numtel);
				getch();
				system("cls");
				break;
			case 5:
				gestion_de_fiche_patients(head);
				getch();
				system("cls");
				break;
	}
		break;
	case 5:
		liste_patient(head);  //Affiche les patients avec Traits entre les patients + retour//
		getch();
		menu_principal(head);
		system("cls");
		break;
	case 6:
		menu_principal(head);
		getch();
		system("cls");
		break;
}
}
void menu_principal(liste *head){
	int k,c;
	system("mode con cols=80 lines=40");
	system("COLOR 0E");
	printf("--------------------------------------------------------------\n\t\t\tMENU PRINCIPAL\n--------------------------------------------------------------\n       1. Gestion des Rendez-vous.\n       2. Gestion du Fiche Patients.\n       3. QUITTER\n--------------------------------------------------------------\n");
	scanf("%d",&k);
	system("cls");
switch(k){
	case 1:
		gestion_des_rendezvous(head);
		system("cls");
		break;
	case 2:
		gestion_de_fiche_patients(head);
		system("cls");
		break;
	case 3:
		system("cls");
		break;
		return;
}
}
void main(){
liste *head=malloc(sizeof (liste));
menu_principal(head);
};
