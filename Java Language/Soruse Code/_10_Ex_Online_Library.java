import java.util.Scanner;
import javax.print.DocFlavor.STRING;

import java.util.ArrayList;
class Parent{

    public ArrayList<String> Array;
    public Scanner input;
    
    public Parent(ArrayList<String> aL,Scanner input){
        this.Array=aL;
        this.input=input;
    }
    public void AddBook(){
        System.out.printf("Which Book You Add -->");
        String user = input.next();
        Array.add(user);
    
    }
    public void Issued_Book(){
        System.out.printf("Which Book You want to Borrow -->");
        String user = input.next();
        Array.remove(user);
        
    }
    public void Show_Available_Books(){
        for(String element:Array){
            System.out.printf("%s\n",element);
        }
    }
    public void ReturnBook(){
        System.out.printf("Which Book You want to Return -->");
        String user = input.next();
        Array.add(user);
    }
}

public class _10_Ex_Online_Library {
    public static void main(String[] args) {
    //     YOU have to implement a library using Java Class Library
    //     Methods: addBook, issueBook, returnBook, showAvailableBooks
    //     Properties: Array to store the available books,
    //                 Array to store the issued books
        Scanner input = new Scanner(System.in);
        ArrayList<String> AL = new ArrayList<>();

        AL.add("DSA");
        AL.add("Java");
        AL.add("Web");
        AL.add("ELC-2");
        AL.add("CP");

        Parent object = new Parent(AL,input);



        // int Issued_Books [] = {};

        
        object.Show_Available_Books();
        object.Issued_Book();
        object.Show_Available_Books();



        
    }
}
