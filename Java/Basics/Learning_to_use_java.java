import java.util.Scanner;

public class Learning_to_use_java {

    public static void main(String[] args) {

        // Creating Scanner object
        Scanner sc = new Scanner(System.in);

        // Printing text
        System.out.println("===== JAVA PRACTICE =====");
        System.out.print("Welcome! ");
        System.out.println("Let's learn Java.\n");

        // Variables
        String name;
        int age;
        double height;
        char grade;
        boolean likesCoding;

        // Taking String input
        System.out.print("Enter your name: ");
        name = sc.nextLine();

        // Taking integer input
        System.out.print("Enter your age: ");
        age = sc.nextInt();

        // Taking decimal input
        System.out.print("Enter your height (in cm): ");
        height = sc.nextDouble();

        // Taking character input
        System.out.print("Enter your grade (A/B/C): ");
        grade = sc.next().charAt(0);

        // Taking boolean input
        System.out.print("Do you like coding? (true/false): ");
        likesCoding = sc.nextBoolean();

        // Output
        System.out.println("\n===== DETAILS =====");
        System.out.println("Name : " + name);
        System.out.println("Age : " + age);
        System.out.println("Height : " + height + " cm");
        System.out.println("Grade : " + grade);
        System.out.println("Likes Coding : " + likesCoding);

        // Arithmetic
        System.out.println("\n===== MATH =====");
        int a = 20;
        int b = 6;

        System.out.println("Addition = " + (a + b));
        System.out.println("Subtraction = " + (a - b));
        System.out.println("Multiplication = " + (a * b));
        System.out.println("Division = " + (a / b));
        System.out.println("Remainder = " + (a % b));

        // Updating variables
        age = age + 1;
        System.out.println("\nNext year you will be " + age + " years old.");

        // Constants
        final double PI = 3.14159;
        System.out.println("Value of PI = " + PI);

        // Escape characters
        System.out.println("\n===== ESCAPE CHARACTERS =====");
        System.out.println("Hello\nWorld");
        System.out.println("Java\tProgramming");
        System.out.println("\"Learning Java\"");
        System.out.println("C:\\Users\\Shree");

        // Closing Scanner
        sc.close();
    }
}
