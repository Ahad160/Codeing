#include<stdio.h>
void display();
void display1();
void display2();

    int main(){
        int user,user2;

    printf("Driveing Licence Chackeing\n");
    
    printf("Enter Youer Age\n");
    scanf("%d",&user);

    if(user==1020){
        display1();
        return 0;
    }
    if(user<18 || user>80){
     
     display2();

    } 
    else if(user>18 || user<80){

         display();
     }

    return 0;
}
 void display(){
     
    printf("You can drive\n");
    
}

void display1(){
     
    printf("You can drive, You have the VIP Pass\n");
}

void display2(){
     
    printf("You cant drive\n");
}