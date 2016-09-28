public class Mystery {
    public static void main(String[] args) {
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
