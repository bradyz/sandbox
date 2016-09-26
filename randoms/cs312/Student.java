public class Student {
    public static void main(String[] args) {
        int cash;

        cash = startingSalary(3.87, 178, 16); // 0
        System.out.println(cash);

        cash = startingSalary(1.99, 185, 55); // 0
        System.out.println(cash);

        cash = startingSalary(2.7, 380, 50); // 65000
        System.out.println(cash);

        cash = startingSalary(3.7, 200, 29); // 77700
        System.out.println(cash);

        cash = startingSalary(3.7, 200, 30); // 115700
        System.out.println(cash);

        cash = startingSalary(3.8, 185, 0); // 115700
        System.out.println(cash);
    }

    public static int startingSalary(double gpa, int total, int honors) {
        if (total < 180 || gpa < 2.0)
            return 0;

        if ((double) honors / total >= 0.15)
            gpa *= 1.15;

        if (gpa < 2.8)
            return 65000;
        else if (gpa < 3.8)
            return 77000;
        return 115700;
    }
}
