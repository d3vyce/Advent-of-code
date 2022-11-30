#include <stdio.h>
#include <stdlib.h>

int resolve(char tab[637][4], int tab_bis_bis[637]) {
    int state[637] = {0};
    int output = 0, i = 0;

    while(1) {
        if(state[i] == 1) {
            return -1;
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
        } else if (i == 637) {
            return output;
        } else {
            printf("error (tab[%d] -> %s -> %d) \n", i, tab[i], tab_bis_bis[i]);
            return -1;
        }
    }
}

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

    for(i=0; i < 637; i++) {
        if(tab[i][0] == 'j') {
            tab[i][0] = 'n';
            output = resolve(tab, tab_bis_bis);
            if(output != -1) return output;
            tab[i][0] = 'j';
        } else if (tab[i][0] == 'n') {
            tab[i][0] = 'j';
            output = resolve(tab, tab_bis_bis);
            if(output != -1) return output;
            tab[i][0] = 'n';
        }
    }

    
}

int main() {
    printf("Result : %d\n", openFile("input.txt"));
    return 0;
}