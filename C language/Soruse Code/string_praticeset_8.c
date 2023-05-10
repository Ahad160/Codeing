#include<stdio.h>
int occurence(char st[],char c);
int main(){
     char user;
     char st[] = {'R','a','i','d','e','n','\0'};
    

    printf("Enter the character \n");
    scanf("%s",&user);

    int count= occurence(st,user);


    return 0;
}
int occurence(char st[],char c){

    char *ptr = st;
    int count=0;
   
        if(*ptr==c){
           printf("The character is present in the strings\n");
            
        }
        
        else{
             printf("The character is missing in the strings\n");
            
        }
        
 }

    
//     for(int i=0;st[i] != '\0';i++){
        
//         if(st[i]==c){
//             printf("The character is present in the strings\n");
//             break;
            
//         }
        
//   }
// }
