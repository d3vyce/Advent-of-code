#include <stdio.h>
#include <stdlib.h>

int openFile(char * File) {
    FILE *fichier = fopen(File, "r");
    int output = 0, i = 0;
    char tab[637][4];
    char tempo[5];
    int tab_bis_bis[637];
    int state[637] = {0};

    while(fscanf(fichier, "%s  %s", tab[i], tempo) != EOF) {
        tab_bis_bis[i] = atoi(tempo);
        i++;
    }

    i = 0;

    while(1) {
        if(state[i] == 1) {
            return output;
        }
        if(tab[i][0] == 'a') {
            state[i] = 1;
            output += tab_bis_bis[i];
            i++;
        } else if(tab[i][0] == 'j') {
            state[i] = 1;
            i += tab_bis_bis[i];
        } else if(tab[i][0] == 'n') {
            state[i] = 1;
            i++;
        } else {
            printf("error (tab[%d] -> %s -> %d) \n", i, tab[i], tab_bis_bis[i]);
            return -1;
        }
    }
}

int main() {
    printf("Result : %d\n", openFile("input.txt"));
    return 0;
}