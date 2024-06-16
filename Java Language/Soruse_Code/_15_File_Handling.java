import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

public class _15_File_Handling {
    public static void main(String[] args) {
        //For Create a new file
        File object = new File("E:/Codeing/Java Language/Soruse_Code/_15_GEN.txt");
        try {
            object.createNewFile();
        } catch (Exception e) {
            System.out.printf("Error To Create a File\n");
        }
        // For Write in a file
        try {
            FileWriter writer = new FileWriter("E:/Codeing/Java Language/Soruse_Code/_15_GEN.txt");
            writer.write("Raiden in Finishing The course\n");
            writer.close();
        } catch (Exception e) {
            System.out.printf("Error To write on a File\n");
        }
        // For read  a file
        try { 
            File Readfile = new File("E:/Codeing/Java Language/Soruse_Code/_15_GEN.txt");
            Scanner sc = new Scanner(Readfile);
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                System.out.println(line);
            }
            sc.close();
        } catch (Exception e) {
            System.out.printf("Error to Read the file\n");

        }
        // For Deleting a file
        File Filedel = new File("E:/Codeing/Java Language/Soruse_Code/_15_GEN.txt");

        if (Filedel.delete()) {
            System.out.printf("File is Deleted %s\n",Filedel.getName());
        }else{
            System.out.printf("File is not Deleted %s\n",Filedel.getName());

        }

        
    }
    
}
