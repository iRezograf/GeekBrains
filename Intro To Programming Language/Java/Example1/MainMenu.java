import java.util.Scanner;

/* пример компиляции и запуска https://habr.com/ru/post/125210/ */


public  class MainMenu {
    public static void main(String[] args) {
        System.out.println("Наконец-то!!!");
        
        Scanner in = new Scanner(System.in);
        System.out.print("Input a number: ");
        int num = in.nextInt();
          
        System.out.printf("Your number: %d \n", num);
        in.close();
        /*
        String name = "Tom";
        int age = 30;
        float height = 1.7f;
          
        System.out.printf("Name: %s  Age: %d  Height: %.2f \n", name, age, height);
         */
    }
}