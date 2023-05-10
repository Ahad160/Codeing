#include<stdio.h>
//celcius to farenheit
int farenheit(int a);

    int main(){
    int user;
    printf("Enter the celcius\n");
    scanf("%d",&user);

    printf("Celcius to fareheit is %d\n",farenheit(user));
    return 0;
}
//(0°C × 9/5) + 32 = 32°F
int farenheit(int a){
 int result;
 result = (a*9/5) + 32;
 return result;

}