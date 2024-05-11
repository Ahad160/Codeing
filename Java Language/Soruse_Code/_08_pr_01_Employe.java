class Employe{
        int salary;
        String name;

        public int getsalary(){
            return salary;
        }
        public String getname(){
            return name;
        }
        public String setname(){
            return name="X--X";
        }
    }
public class _08_pr_01_Employe {
    public static void main(String[] args) {
        Employe object = new Employe();

        object.name="Raiden";
        object.salary=5000;
        System.out.printf("%s,%d",object.name,object.salary);

        System.out.printf("\ngetname() is %s\n",object.getname());

        System.out.printf("\nsetname() is %s\n",object.setname());

        System.out.printf("\nsetsalary() is %d\n",object.getsalary());




    }    
}