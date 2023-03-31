#include<stdio.h>
void slice (char *st, int m ,int n);
int main(){

    char st[] = "Raiden";
    slice(st,2,6);
    printf("%s",st); 
    
    return 0;
}
void slice (char *st, int m ,int n){
    int i=0;
    while((m+i)<n){//1+0 <6
        st[i] = st[i+m];//0+1 = r+1
        i++;
    }
    st[i] = '\0';
}
