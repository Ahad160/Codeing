#include<stdio.h>
#include<string.h>

struct emplouee
{
    int code;
    float salary;
    char name[10];
};

int main(){
    
    struct emplouee person;
    {
      person. code =100;
      person.salary=74.62;
      strcpy(person.name,"Raiden") ;     
    };

    printf("%d\n",person.code);
    printf("%f\n",person.salary);
    printf("%s\n",person.name);



    
    
    return 0;
}