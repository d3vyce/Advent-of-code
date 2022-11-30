#include <stdio.h>
#include <stdlib.h>

#define PREAMBLE 25
#define TAILLE 1000
#define ANSWER 400480901

long long int openFile(char * File) {
    FILE *fichier = fopen(File, "r");
    int i, j, k, count;
    long long int output, min, max, tmp;
    long long int tab[TAILLE] = {0};

    while(fscanf(fichier, "%lld", &tmp) != EOF) {
        tab[i] = tmp;
        i++;
    }

    i = 0;
    output = 0;

    while(i < TAILLE) {

        while(output < ANSWER) {
            output += tab[j];
            if(output == ANSWER) {
                min = tab[i];
                max = tab[i];
                for(k=i; k < j; k++) {
                    if(min > tab[k]) min = tab[k];
                    if(max < tab[k]) max = tab[k];
                }
                return min + max;
            }
            j++;
        }
        i++;
        j = i;
        output = 0;
    }

}

int main() {
    printf("Result : %lld\n", openFile("input.txt"));
    return 0;
}