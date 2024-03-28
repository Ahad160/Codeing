#include <windows.h>
#include <stdio.h>

int main(void){
    HINSTANCE hDLL;

    // Load a DLL
    hDLL = LoadLibrary(TEXT("main2.dll"));

    // if DLL was loaded
    if (hDLL != NULL){
        printf("DLL Found");
    } else
    {
        printf("DLL Not Found");
    }

    return 0;
    
}