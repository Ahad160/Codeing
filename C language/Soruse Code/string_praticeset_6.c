#include<stdio.h>
void decrypt(char *c);
int main(){
    char c[] ="Xfmmdpnf!up!ipnfgpsou!sfwpmvujpo";
    decrypt(c);
    printf("The decypt string is-- %s",c);
    return 0;
}
void decrypt(char *c){
    char *ptr =c;
    while(*ptr != '\0'){
        *ptr = *ptr-1;
        ptr++;

    }
}
