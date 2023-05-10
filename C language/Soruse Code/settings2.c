#include<stdio.h>

int main(){
    
    int scan1;
    int scan2;

      for(scan1=1; scan1<100;){
    printf("Settings\n");
    printf("\n");

    printf("1.Airplane mode\n2.VPN\n3.Hotspot\n4.Network\n");
    scanf("%d",&scan1);

    if(scan1==1){
        printf("1.Airplane mode (ON)\n2.Airplane mode (OFF)\n");
        scanf("%d",&scan2);

        if(scan2==1){
            printf("Airplane mode is ON\n");
        }
        else if(scan2==2){
            printf("Airplane mode is (OFF)\n");
        return 0;
        }
    } 
    else if(scan1==2){
        printf("1.VPN (ON)\n2.VPN (OFF)\n");
        scanf("%d",&scan2);

        if(scan2==1){
            printf("VPN is ON\n");
            continue;
        }
        else if(scan2==2){
            printf("VPN  is (OFF)\n");
            continue;
        return 0;
        }
    }
        
      }
    return 0;
}