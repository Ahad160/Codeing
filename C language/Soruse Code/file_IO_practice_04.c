#include<stdio.h>

typedef struct data{
    float salary;
    char name[10];
}data;

int main(){
  
    data a,b;
    
printf("1st User\n\n");
    printf("Enter Youer Name\n");
    scanf("%s",&a.name);
    printf("Enter Youer Salary\n");
    scanf("%f",&a.salary);


printf("2nd User\n");
    printf("Enter Youer Name\n");
    scanf("%s",&b.name);
    printf("Enter Youer Salary\n");
    scanf("%f",&b.salary);

  FILE *ptr;

  ptr =fopen("simple.txt","w");
  fprintf(ptr,"Name- %s , Salary-%f\n",a.name,a.salary);
  fprintf(ptr,"Name- %s , Salary-%f\n",b.name,b.salary);
  fclose(ptr);
  
    
    return 0;
}