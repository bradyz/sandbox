public class Test1 {
    public static void main (String[] args) {
        // function inputs -> outputs
    
        // inputs -> int myAge, int yourAge
        // ouputs -> int result
        
        // input -> int n
        // output -> double result
        
        // 6, 1.5 cup
        // 6 => 0 loop 0
        // 5 => 1.5 loop 1
        // 4 => 3.0 loop 2 
        // 3 => 4.5
        // input -> int
        // ouput -> double
        System.out.println(GPA(0, 0, 0));
    }

    public static double howMuchCoffee (int x) {
        double y = 0.0;
        if( x == 0) {
            return 6 * 1.5;
        } else if(x > 6) {
            return 0.0;
        } else {
            for (int i = 1; i <= (6 - x); i++){
                y = y + 1.5;
            }
        }
        return y;
    }

    public static double howMuchCoffeeV2 (int hoursOfSleep) {
        if (hoursOfSleep >= 6)
            return 0.0;

        int hoursUnderSix = 6 - hoursOfSleep;
        double multiplier = 1.5;

        double cups = hoursUnderSix * multiplier;
        return cups;
    }

    public static double howMuchCoffeeV3 (int hoursOfSleep) {
        double multiplier = 1.5;
        double cups = 0.0;

        // hoursOfSleep 5
        // i 5  6
        // cups 0.0 1.5
        for (int i = hoursOfSleep; i < 6; ++i) {
            cups = cups + multiplier;
        }

        return cups;
    }

    // inputs -> int numA, int numB, int numC
    // output -> double
    public static double GPA (int numA, int numB, int numC){
        double pointsForA = 4.0;
        double pointsForB = 3.0;
        double pointsForC = 2.0;
        double x = numA * pointsForA + numB * pointsForB + numC * pointsForC;
        double normalized = x / (numA + numB + numC);
        return normalized;
    }

    public static double GPAv2 (int As, int Bs, int Cs){
        return (As * 4.0 + Bs * 3.0 + Cs * 2.0) / (As + Bs + Cs);
    }

    // A, A, B, C
    // GPA(2, 1, 1)
    // (4.0 + 4.0 + 3.0 + 2.0) / 4 
}
