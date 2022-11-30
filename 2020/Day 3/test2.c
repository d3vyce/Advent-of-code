#include <stdio.h>

int count(int c_i, int c_w, char tab[323][2500]) {
    int i = 0;
    int w = 0;
    int output = 0;

    while(i < 323) {
        i += c_i;
        w += c_w;

        if(tab[i][w] == '#') {
            output++;
        }
    }

    return output;
}

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

    return count(1, 1, tab)*count(1, 3, tab)*count(1, 5, tab)*count(1, 7, tab)*count(2, 1, tab);
}

int main() {
    printf("Result : %d\n", openFile("input.txt"));
    return 0;
}