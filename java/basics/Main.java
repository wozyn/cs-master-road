import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("请输入年龄：");
        int age = sc.nextInt();
        if (age >=18){
            System.out.println("成年人");
        }else{
            System.out.println("未成年人");
        }

        System.out.println("你的年龄是：" + age);

        sc.close();
    }
}