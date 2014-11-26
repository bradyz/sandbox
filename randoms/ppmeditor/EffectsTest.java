import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.OutputStream;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class EffectsTest { public static void main(String args[]) {

    ArrayList<File> fileList = new ArrayList<File>();
    Map<Integer, Map<Integer, Integer>> colorVals = new HashMap<Integer, Map<Integer, Integer>>();
    int numInputs;
    String fileName = "";
    Scanner fileInput;
    Scanner keyboard = new Scanner(System.in); 
    Effects e = new Effects();

    System.out.println("Enter number of input files: ");
    numInputs = keyboard.nextInt();

    keyboard.nextLine();

    for(int n = 0; n < numInputs; n++) {
      System.out.println("Enter a file name: ");
      fileName = keyboard.nextLine();

      File f = new File(fileName);
      fileList.add(f);
    }

    for(int n = 0; n < fileList.size(); n++)
    {
      try {
        fileInput = new Scanner(new FileReader(fileList.get(n)));
        fileInput.nextLine();
        int len = fileInput.nextInt();
        int width = fileInput.nextInt();
        fileInput.nextLine();
        String range = fileInput.nextLine();

        /* System.out.println(len); */
        /* System.out.println(width); */
        /* System.out.println(range); */

        int val;

        for(int x = 0; x < width * 3 * len; x ++)
        {
          val = fileInput.nextInt();
          /* Map<Integer, Integer> tmp =  */
          /* colorVals.put(x,  */

        }
      } 
      catch (Exception ex) {
        ex.printStackTrace();
      }
    }
  }
}
