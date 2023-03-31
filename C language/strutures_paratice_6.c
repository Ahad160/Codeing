#include<stdio.h>
  
  typedef struct Zone{
    int date;
    int month;
    int Year;

  }Moment;

  int display(Moment a,Moment b){
    //For Date
    if(a.date<b.date){
      return -1;
    }
    if(a.date>b.date){
      return 1;
    }
    //For Month
    if(a.month<b.month){
      return -1;
    }
    if(a.month>b.month){
      return 1;
    }
    //For Year
    if(a.Year<b.Year){
      return -1;
    }
    if(a.Year>b.Year){
      return 1;
    }

    return 0;
     printf("The Zone is %d/%d/%d\n",a.date,a.month,a.Year);
  }


int main(){

    Moment u1={20,9,2022};
    Moment u2={20,9,2022};

    
    int a= display(u1,u2);
    printf("Date Comparison is %d\n",a);

    
    return 0;
}