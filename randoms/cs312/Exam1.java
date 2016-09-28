public class Exam1 {
    public static void main (String[] args) {
        problem1();
        problem2();
        problem3();
        problem4();
    }

    public static void problem1() {
        System.out.println("==================================================");
        System.out.println("Problem 1.");
        System.out.println("==================================================");

        int A = 8 + 5 * 3 / 2;
        System.out.println("int A, " + A);

        int B = 3 * (7 + 1) - 3 - 7 + 2;
        System.out.println("int B, " + B);

        int C = 23 % 5 + 31 / 4 % 3 - 17 % (16 % 10);
        System.out.println("int C, " + C);

        String D = "1" + 2 + 3 + "4" + 5 * 6 + "7" + (8 + 9);
        System.out.println("String D, " + D);

        String E = 1 + 1 + "(8 ; 2)" + (8 - 2) + 1 + 1;
        System.out.println("String E, " + E);

        double F = 29 / 4 / 2.0 + 18 / 5 + 1.5;
        System.out.println("double F, " + F);

        double G = 5 / 2 + 123 / 10 / 10.0;
        System.out.println("double G, " + G);

        int H = 13 % 5 + 43 % (11 % 3);
        System.out.println("int H, " + H);

        int I = -(6 + 3 - 2 * 3);
        System.out.println("int I, " + I);

        double J = 9 / 2 / 2.0 + 9 / 2.0 / 2;
        System.out.println("double J, " + J);

        String K = 1 + "x" + 11 / 10 + " is" + 10 / 2;
        System.out.println("String K, " + K);

        double L = 1 / 2 + -(157 / 10 / 10.0) + 9.0 * 1 / 2;
        System.out.println("double L, " + L);

        String M = 2 + "(int)2.0" + 2 * 2 + 2;
        System.out.println("String M, " + M);

        double N = Math.round(-6.4) + Math.ceil(6.5);
        System.out.println("double N, " + N);

        double O = Math.floor(Math.max(Math.min(-5, 5.5), Math.max(-4.5, -6)));
        System.out.println("double O, " + O);

        double P = Math.pow(3, 2);
        System.out.println("double P, " + P);

        double Q = Math.ceil(5.2) + Math.floor(-5.2);
        System.out.println("double Q, " + Q);

        double R = (double) 3 / 4 + (int) (5.0 / 6 + 1 / 6.0);
        System.out.println("double R, " + R);
    }

    public static void problem2() {
        System.out.println("==================================================");
        System.out.println("Problem 2.");
        System.out.println("==================================================");

        System.out.println("Part A.");
        int xa = 2;
        xa = -3;
        xa -= -5;
        xa++;
        System.out.println(xa);

        System.out.println("Part B.");
        int xb = 4;
        xb++;
        int zb = xb + 2;
        double ab = zb / xb;
        ab -= 2 + xb;
        System.out.println(xb + " " + zb + " " + ab);

        System.out.println("Part C.");
        int xc = 3;
        int yc = 4;
        String sc = "xc";
        xc++;
        sc = xc + yc + sc;
        System.out.println(xc + " " + sc);

        System.out.println("Part D.");
        int yd = 2;
        for(int j = 0; j <= 3; j++) {
            int xd = 3 - j;
            yd = yd + xd;

        }
        System.out.println(yd);

        System.out.println("Part E.");
        int ae = 5;
        int be = 12;
        double xe = be / ae;
        int re = be % ae;
        System.out.println(re + " " + xe);

        System.out.println("Part F.");
        for (int i = 1; i <= 5; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print("*");

            }
        }
        System.out.println();

        System.out.println("Part G.");
        for (int i = 1; i <= 10; i++) {
            for (int j = i; j <= 10; j++) {
                System.out.print("*");
            }
        }
        System.out.println();


        System.out.println("Part H.");
        for (int i = 7; i > -3; i--) {
            System.out.print("*");
            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }
            System.out.println("*");
        }

        System.out.println("Part I.");
        int x = 5;
        int y = 13;
        if (x % y == 3) {
            System.out.print("A");
        } else if (x + y > 15) {
            System.out.print("B");
        }
        if (x >= 5) {
            System.out.print("C");

        } else {
            System.out.print("D");
        }
        System.out.println();
    }

    public static void problem3() {
        System.out.println("==================================================");
        System.out.println("Problem 3.");
        System.out.println("==================================================");

        System.out.println("Part A.");
        System.out.println("for (int i = 0; i < da; i++) {");
        System.out.println("error: variable i is already defined in method");
        /* int aa = 12; */
        /* int i = 31; */
        /* double da = i * aa++ - 2; */
        /* for (int i = 0; i < da; i++) { */
        /*   System.out.print("*"); */
        /* } */

        System.out.println("Part B.");
        System.out.println("int by = Math.pow(_bx, bz);");
        System.out.println("error: incompatible types: possible lossy conversion");
        /* int _bx; */
        /* _bx = 5; */
        /* double bz = 3; */
        /* int by = Math.pow(_bx, bz); */
        /* System.out.print(bz + " " + by * bz); */

        System.out.println("Part C.");
        System.out.println("double 2x = 2 * cx;");
        System.out.println("error: not a statement");
        /* int cx = 5; */
        /* double 2x = 2 * cx; */
        /* String cs = "CS" + 2x; */
        /* System.out.print(cx + " " + cs); */

        System.out.println("Part D.");
        System.out.println("sum /= i;");
        System.out.println("error: variable sum might not have been initialized");
        /* double sum; */
        /* int dz = 5; */
        /* for (int i = 1; i <= dz; i++) { */
        /*   sum /= i; */
        /* } */
        /* System.out.println(sum); */

        System.out.println("Part E.");
        System.out.println("if (ez = 5)");
        System.out.print("error: incompatible types: double cannot be ");
        System.out.println("converted to boolean");            
        /* int ea = -3; */
        /* double ez = 5 * ea; */
        /* if (ez = 5) { */
        /*   System.out.print(ez); */
        /* } */
    }

    public static class Mystery {
        public static void doStuff() {
            int one = 4;
            int two = 3;
            int three = 10;
            int num = 17;
            int four = 3; 
            racket(one, two, three);
            racket(three, four, 5);
            racket(2, two * 2, num);
            racket(num, three * one, four);
            racket(three - four, one, two + 8);
        }

        public static void racket(int two, int one, int three) {
            System.out.println(three + " is roughly " + two + " plus " + one);
            if (one + two > three) {
                bark();
            } else if (one >= three - two) {
                sneeze();
            } else {
                holler();
            } 
            System.out.println();
        }

        public static void holler() {
            System.out.println(" YES");
            bark();
            sneeze();
        }

        public static void bark() {
            sneeze();
            System.out.println(" NO");
        }

        public static void sneeze() {
            System.out.println(" maybe");
        }
    }

    public static void problem4() {
        System.out.println("==================================================");
        System.out.println("Problem 4.");
        System.out.println("==================================================");

        Mystery.doStuff();
    }
}
