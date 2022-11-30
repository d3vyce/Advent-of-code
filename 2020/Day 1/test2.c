#include <stdio.h>

int openFile(char * File) {
    FILE *fichier = fopen(File, "r");
    int tmp, i = 0, j, k, inte = 0;
    int tab[200] = {0};


    while(fscanf(fichier, "%d", &tmp) != EOF) {
        tab[i] = tmp;
        i++;
    }

    for(i=0; i < 200; i++) {
        for(j=0; j < 200; j++) {
            for(k=0; k < 200; k++) {
                inte++;
                if((tab[i] + tab[j] + tab[k]) == 2020) {
                    printf("Tentatives : %d \n", inte);
                    return tab[i] * tab[j] * tab[k];
                }
            }
        }
    }
}

int main() {
    printf("Result : %d\n", openFile("input.txt"));
    return 0;
}