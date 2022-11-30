#include <stdio.h>
#include <string.h>

int openFile(char * File) {
    FILE *fichier = fopen(File, "r");
    int nb_pass = 0;

    int min, max, i, count = 0;
    char car;
    char password[20];
    int taille;

    while(fscanf(fichier, "%d-%d %c: %s", &min, &max, &car, password) != EOF) {
        taille = strlen(password);
        for(i=0; i < taille; i++) {
            if(password[i] == car) {
                count++;
            }
        }
        if(password[min-1] == car && password[max-1] != car || password[min-1] != car && password[max-1] == car) {
            nb_pass++;
        }
        count = 0;
    }

    return nb_pass;
}

int main() {
    printf("Result : %d\n", openFile("input.txt"));
    return 0;
}