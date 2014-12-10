import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;

public class EffectsTest {

  public static void main(String[] args){ 

    Effects e = new Effects();
    ArrayList<File> fileList = new ArrayList<File>();
    int inputFiles = 0;
    String fileName = "";
    Scanner keyboard = new Scanner(System.in);

    System.out.println("Enter the number of input files: ");
    inputFiles = keyboard.nextInt();
    keyboard.nextLine();
    for(int n = 0; n < inputFiles; n++) {
      System.out.println("Enter file name: ");
      fileName = keyboard.nextLine();
      try {
        File f = new File(fileName);
        fileList.add(f);
      }
      catch (Exception ex) {
        ex.printStackTrace();
      }
    }
    System.out.println("Enter new file name: ");
    String newName = keyboard.nextLine();
    e.filter(fileList, newName);
  }
}
