import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Effects {

  ArrayList<File> fileList = new ArrayList<File>();
  ArrayList<ArrayList<String>> listList = new ArrayList<ArrayList<String>>();

  public void addInputs() {
    Scanner fileInput = null;
    for(int n = 0; n < fileList.size(); n++) {
      ArrayList<String>tmpList = new ArrayList<String>();
      try {
        fileInput = new Scanner(new FileReader(fileList.get(n)));
      }
      catch (Exception ex) {
        ex.printStackTrace();
      }
      while(fileInput.hasNextLine()) {
        String tmpLine = fileInput.nextLine();
        tmpList.add(tmpLine);
      }
      listList.add(tmpList);
    }
  }

  public void filter(ArrayList<File> fileList, String newName) {
    FileWriter fw = null;
    try {
      fw = new FileWriter(newName);
    } catch (Exception ex) {
      ex.printStackTrace();
    }
    ArrayList<String>tmpList = new ArrayList<String>();
    this.fileList = fileList;
    this.addInputs();
    ArrayList<String> lineList = new ArrayList<String>();
    for(int i = 0; i < listList.get(0).size(); i++) {
      lineList = new ArrayList<String>();
      for(int j = 0; j < listList.size(); j++) {
        tmpList = listList.get(j);
        String line = tmpList.get(i);
        lineList.add(line);
      }
      System.out.println(lineList);
      Collections.sort(lineList);
      System.out.println(lineList);
      int max = 0;
      String current = "";
      String correctLine = "";
      int count = 1;
      for(int n = 0; n < lineList.size(); n++) {
        current = lineList.get(n);
        System.out.println(current);
        if(n == lineList.size() - 1)
          break;

        if (lineList.get(n) == lineList.get(n + 1)) {
          count++;
        }
        else {
          count = 1;
        }

        if (count > max) {
          max = count;
          correctLine = current;
        }
      }

      try {
        fw.write(correctLine + "\n");
      }
      catch (Exception ex) {
        ex.printStackTrace();
      }
    }
    try {
      fw.close();
    }
    catch (Exception ex) {
      ex.printStackTrace();
    }
  }
}
