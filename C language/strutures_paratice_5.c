#include<stdio.h>
    typedef struct Bank{
        int bankid;
        char name[10];
        int Balance;
        int RG_date;
        int RG_month;
        int RG_year;

    }Bankc;
    
    void display(Bankc a){
        printf("User Name is %s\n",a.name);
        printf("User Bank ID is %d\n",a.bankid);
        printf("User Account Created in %d/%d/%d\n",a.RG_date,a.RG_month,a.RG_year);
        printf("User Bank Balance is %d\n",a.Balance);

    }

int main(){
    
        
        Bankc u1;

      u1.Balance=50000;
      u1.RG_date=05;
      u1.RG_month=02;
      u1.RG_year=2019;

      

    
     printf("Enter Bank ID\n");
     scanf("%d",&u1.bankid);
    
     printf("Enter youer Name \n");
     scanf("%s",&u1.name);
     
     printf("\n\n\n");
     
     display(u1);



    return 0;
}