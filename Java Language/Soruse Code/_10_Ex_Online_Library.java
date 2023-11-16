import java.util.Scanner;
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
        System.out.printf("\n\n");  //For Looking Good
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


        for(int i=1;i>0;i++){
            System.out.printf("\n\n1.Show Available Books\n2.Add Books\n3.Issued Book\n4.Return Book\nSelect Any Option --> ");
            int user = input.nextInt();
            if (user==1) {
                object.Show_Available_Books();
            }
            else if(user==2) {
                object.AddBook();
            }
            else if(user==3) {
                object.Issued_Book();
            }
            else if(user==4) {
                object.ReturnBook();
            }
        }

    }
}
