#include<stdio.h>
   
    int main(){
     
     //first Part
      int user;
      int quantity;

     //scend Part
      int user2;
      int quantity2;

     //third Part
      int user3;
      int quantity3;
      
       printf("1.Renew\n2.Clone\n3.Pending Clone\n");
       scanf("%d",&user);

     if(user==1)
    {
        printf("Quantity\n");
        scanf("%d",&quantity);
        printf("Youer Restrict\n---------------\n o Renew option\n o Quantity is %d\n---------------",quantity);

    }
    else if(user==2)
    {
        printf("1.Normal clone\n2.Renew Clone\n");
        scanf("%d",&user2);

         if(user2==1)
         {
            printf("Quantity\n");
            scanf("%d",&quantity2);
            printf("Youer Restrict\n----------------------\n o Normal Clone option\n o Quantity is %d\n----------------------",quantity2);
        }

         else if(user2==2)
         {
            printf("Quantity\n");
            scanf("%d",&quantity2);
            printf("Youer Restrict\n----------------------\n o Renewly Clone option\n o Quantity is %d\n----------------------",quantity2);
        }  
        
    }
    else if(user==3){

        printf("1.Renewly Clone\n2.Check Renewly Clone\n");
        scanf("%d",&user3);
         
         if(user3==1)
         {
            printf("Quantity\n");
            scanf("%d",&quantity3);
         }

         else if(user3==2){

            printf("Youer Restrict\n----------------------\n o Pending Renewly Clone option\n o Quantity is %d\n----------------------",quantity3);
         }
    } 
    
    return 0;
}