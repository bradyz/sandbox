import java.util.ArrayList;
import java.util.HashMap;


// M2S = Morse to String
class M2S {
    static final HashMap<String, String> MORSE;
    static {
        MORSE = new HashMap<String, String>();
        MORSE.put(".-", "a");
        MORSE.put("-...", "b");
        MORSE.put("-.-.", "c");
        MORSE.put("-..", "d");
        MORSE.put(".", "e");
    }
}

public class Morse {
    // runtime is O(k^m) where k is number of words in the alphabet, 
    // m is length of string
    public static void findPossibleWords (String morse, String word, ArrayList<String> possible) {
        // If we have reached the end and we have made some word
        if (morse.equals("") && !word.equals(""))
            possible.add(word);
        
        // We can do some optimizations here since we know the longest morse code
        // is like 4, so when i is greater than 4, we can break
        for (int i = 0; i <= morse.length(); ++i) {
            String english = M2S.MORSE.get(morse.substring(0, i));

            if (english != null)
                findPossibleWords(morse.substring(i), word+english, possible);
        }
    }

    public static ArrayList<String> wrapper (String morse) {
        ArrayList<String> result = new ArrayList<>();
        findPossibleWords(morse, "", result);
        return result;
    }

    public static void main (String args[]) {
        for (String s: wrapper("-...."))
            System.out.println(s);
    }
}
