#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int display(char user ,char com){
   //Draw
   if(user==com){  
    return 0;
   }

   if(user=='r' && com=='p'){
        return 1;
    }
    else if(user=='p' && com=='r'){
        return 2;
    }

    if(user=='r' && com=='s'){
        return 1;
    }
    else if(user=='s' && com=='r'){
        return 2;

    }

    if(user=='p' && com=='s'){
        return 2;
    }
    else if(user=='s' && com=='p'){
        return 1;
    }
}
  int displayresult(char user,char com){
    if(user=='r' && com=='p'){
        printf("You Choose Rock and Computer Paper");
    }
    else if(user=='p' && com=='r'){
        printf("You Choose Paper and Computer Rock");

    }

    if(user=='r' && com=='s'){
        printf("You Choose Rock and Computer Siser");

    }
    else if(user=='s' && com=='r'){
        printf("You Choose Siser and Computer Rock");

    }

    if(user=='p' && com=='s'){
        printf("You Choose Paper and Computer Siser");

    }
    else if(user=='s' && com=='p'){
        printf("You Choose Siser and Computer Paper");

    }
  }


int main(){
    int number;
    char user,com;

    srand(time(0));
    number= rand()%100+1;

    if(number<33){
        com='r';
    }
    else if (number>33 && number<66)
    {
        com='p';
    }
    else{
        com='s';
    }
    

    printf("Enter Character Rock = 'r' , Paper = 'p' , Siser = 's' \n");
    scanf("%c",&user);

    int result=display(user,com);

    if(result == 0){
         printf("Game Draw\n");
    }
   if (result == 1){
        printf("You Win\n");
    }
    else{
        printf("You Lose!\n");     
    }
    
    
    displayresult(user,com);

    getch();

    return 0;
}