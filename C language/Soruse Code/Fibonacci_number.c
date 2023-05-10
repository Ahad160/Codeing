// #include<stdio.h>
// int Fibonacci(int a);

//     int main(){
//         int fib=9;
//         printf("the Fibonacci aequence is %d\n",Fibonacci(fib));
    
//     return 0;
// }
// int Fibonacci(int a){

//            if(a<=1){
//                return a;
//          return Fibonacci(a-1) + Fibonacci(a-2);
//     }
// }
#include<stdio.h>
int fib(int n)
{
   if (n <= 1)
      return n;
   return fib(n-1) + fib(n-2);
}
 
int main ()
{
  int n = 9;
  printf("%d", fib(n));
  getchar();
  return 0;
}