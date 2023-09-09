public class _03_pr_04_Detect_Spaces {
    public static void main(String[] args) {
        String Text ="To  capitalize a word is   to make its first";

        System.out.printf("Does This String has Double Spaces-{%s} And The index is %d\n",Text.contains("   "),Text.indexOf("  "));
        System.out.printf("Does This String has Triple Spaces-{%s} And The index is %d",Text.contains("   "),Text.indexOf("   "));



    }  
}
