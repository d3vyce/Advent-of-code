#include <stdio.h>
#include <stdlib.h>

#define PREAMBLE 25
#define TAILLE 1000

long long int openFile(char * File) {
    FILE *fichier = fopen(File, "r");
    int output = 0, i = 0, j, k;
    long long int tmp;
    long long int tab[TAILLE] = {0};
    int count;

    while(fscanf(fichier, "%lld", &tmp) != EOF) {
        tab[i] = tmp;
        i++;
    }

    i=PREAMBLE;

    while(i < TAILLE) {
        for(j=1; j <= PREAMBLE; j++) {
            for(k=1; k <= PREAMBLE; k++) {
                if(tab[i-j] + tab[i-k] == tab[i]) count++;
            }
        }
        if(count == 0) {
            return tab[i];
        }
        i++;
        count = 0;
    }

}

int main() {
    printf("Result : %lld\n", openFile("input.txt"));
    return 0;
}