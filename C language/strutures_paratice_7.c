#include<stdio.h>
  //yyyy-mm-dd hh:mm:ss.
  typedef struct Zone{
    int Year;
    int month;
    int date;
    int hour;
    int minute;
    int secend;

  }Moment;

  int display(Moment a,Moment b){

    //For Year
    if(a.Year<b.Year){
      return -1;
    }
    if(a.Year>b.Year){
      return 1;
    }

    //For Month
    if(a.month<b.month){
      return -1;
    }
    if(a.month>b.month){
      return 1;
    }

    //For Date
    if(a.date<b.date){
      return -1;
    }
    if(a.date>b.date){
      return 1;
    }
    
    //For Hour
    if(a.hour>b.hour){
      return -1;
    }
    if(a.hour>b.hour){
      return 1;
    }

    //For Minute
    if(a.minute>b.minute){
      return -1;
    }
    if(a.minute>b.minute){
      return 1;
    }
    
     //For Secend
    if(a.secend>b.secend){
      return -1;
    }if(a.secend>b.secend){
      return 1;
    }

    return 0;
     printf("The Zone is %d/%d/%d\n",a.date,a.month,a.Year);
  }


int main(){

    Moment u1={2022,9,20,6,25,56};
    Moment u2={2022,9,21,6,25,56};

    
    int a= display(u1,u2);
    printf("Date Comparison is %d\n",a);

    
    return 0;
}