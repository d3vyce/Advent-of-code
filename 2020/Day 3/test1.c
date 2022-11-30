#include <stdio.h>

int openFile(char * File) {
    FILE *fichier = fopen(File, "r");
    int output = 0, i = 0, j, k, w = 0, taillle = 31, ligne = 323;
    int r1 = 0, r2 = 0, r3 = 0, r4 = 0, r5 = 0;
    char tab[323][2500];

    while(fscanf(fichier, "%s", tab[i]) != EOF) {
        i++;
    }

    for(j=0; j < 323; j++) {
        for(k=31; k < 2500; k++) {
            tab[j][k] = tab[j][k-31];
        }
    }

    i = 0;
    w = 0;

    while(i < 323) {
        i += 1;
        w += 3;

        if(tab[i][w] == '#') {
            output++;
        }
    }

    return output;
}

int main() {
    printf("Result : %d\n", openFile("input.txt"));
    return 0;
}