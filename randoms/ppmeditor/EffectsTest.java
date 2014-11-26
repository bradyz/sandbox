import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.FileOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.Map.Entry;

public class EffectsTest { public static void main(String args[]) {

    ArrayList<File> fileList = new ArrayList<File>();
    Map<Integer, Map<Integer, Integer>> colorVals = new HashMap<Integer, Map<Integer, Integer>>();
    int numInputs;
    int len = 0;
    int width = 0;
    String fileName = "";
    Scanner fileInput;
    Scanner keyboard = new Scanner(System.in); 
    Effects e = new Effects();

    /* System.out.println("Enter number of input files: "); */
    /* numInputs = keyboard.nextInt(); */
    /*  */
    /* keyboard.nextLine(); */
    /*  */
    /* for(int n = 0; n < numInputs; n++) { */
    /*   System.out.println("Enter a file name: "); */
    /*   fileName = keyboard.nextLine(); */
    /*  */
    /*   File f = new File(fileName); */
    /*   fileList.add(f); */
    /* } */

    File f1 = new File("tinypix.ppm");
    File f2 = new File("tinypix1.ppm");
    File f3 = new File("tinypix2.ppm");

    fileList.add(f1);
    fileList.add(f2);
    fileList.add(f3);

    for(int n = 0; n < fileList.size(); n++)
    {
      try {
        fileInput = new Scanner(new FileReader(fileList.get(n)));
        fileInput.nextLine();
        len = fileInput.nextInt();
        width = fileInput.nextInt();
        fileInput.nextLine();
        String range = fileInput.nextLine();

        int val;
        Map<Integer, Integer> tmp = new HashMap<Integer, Integer>();
        Map<Integer, Integer> tmpEntry = new HashMap<Integer, Integer>();

        for(int x = 0; x < width * 3 * len; x ++)
        {
          val = fileInput.nextInt();
          if(!colorVals.containsKey(x)) {
            tmpEntry = new HashMap<Integer, Integer>();
            tmpEntry.put(val, 1);
          }
          else {
            tmpEntry = colorVals.get(x);
            if(!tmp.containsKey(val)) {
              tmpEntry = new HashMap<Integer, Integer>();
              tmpEntry.put(val, 1);
            }
            else {
              tmpEntry.put(val, tmpEntry.get(val) + 1);
            }
          }
          colorVals.put(x, tmpEntry);
        }
      } 
      catch (Exception ex) {
        ex.printStackTrace();
      }
    }

    System.out.println("Output File: ");
    String writeFile = keyboard.nextLine();

    try {
      FileWriter fw = new FileWriter(writeFile);

      fw.write("P3\n");
      fw.write(len + " " + width + "\n");
      fw.write("255\n");

      int pos = 0;
      int max = 0;
      int count = 0;

      Map<Integer, Integer> tmp = new HashMap<Integer, Integer>();

      for(Entry<Integer, Map<Integer,Integer>> posVal : colorVals.entrySet()) {
        pos = posVal.getKey();
        tmp = posVal.getValue();

        for(Entry<Integer, Integer> valCount : tmp.entrySet()) {
          if(valCount.getValue() > count) {
            max = valCount.getKey();
            count = valCount.getValue();
          }
        }

        fw.write(max + " ");

        count = 0;

        if((pos + 1) % (3 * width) == 0)
          fw.write("\n");
      }

      fw.close();
    } catch (Exception ex) {
      ex.printStackTrace();
    }
  }
}
