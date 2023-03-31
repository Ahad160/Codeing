#include<stdio.h>
#include<string.h>

struct data
{
    int code;
    float salary;
    char name[10];
};

int main(){
    
struct data a;

printf("Enter the code of a\n");
scanf("%d",a.code);

printf("Enter the salary of a\n");
scanf("%f",a.salary);

printf("Enter the name of a\n");
scanf("%s",a.name);


printf("the code of a is %d\n",a.code);
printf("the salary of a is %f\n",a.salary);
printf("the name of a is %s\n",a.name);


    return 0;
}