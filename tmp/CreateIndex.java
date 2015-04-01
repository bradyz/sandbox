import java.io.File;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.Arrays;

public class CreateIndex {
	
    private Map<String, LinkedList<Integer>> index;
 
    public CreateIndex () {
        index = new HashMap<String, LinkedList<Integer>>();
    }

    public Map<String, LinkedList<Integer>> readFile(File f) {
        Scanner fileInput = null;
        try {
            fileInput = new Scanner(new FileReader(f));
        }
        catch (Exception ex) {
            ex.printStackTrace();
        }
        int lineNumber = 0;
        while(fileInput.hasNextLine()) {
            String line = fileInput.nextLine();
            String[] words = line.split(" ");
            for(String tmp : words) {
                /* if(index.get(tmp) == null) { */
                if(!index.containsKey(tmp)) {
                    LinkedList<Integer> lines = new LinkedList<Integer>();
                    lines.add(lineNumber);
                    this.index.put(tmp, lines);
                }
                else {
                    LinkedList<Integer> lines = index.get(tmp);
                    lines.add(lineNumber);
                    this.index.put(tmp, lines);
                }
            }
            lineNumber++;
        }
        fileInput.close();
        return index;
    }
 
    public LinkedList<Integer> getIndex(String word) {
        return index.get(word);
    }

    public void asdf() {
        System.out.println();

        System.out.println(this.index.size());
        Iterator<Entry<String, LinkedList<Integer>>> it = index.entrySet().iterator();
        while(it.hasNext()) {
            Map.Entry<String, LinkedList<Integer>> pair = it.next();
            System.out.println(Arrays.toString(pair.getValue().toArray()));
        }
    }
 
    public static void main(String[] args) {
        String fileName = args[0];
        CreateIndex test = new CreateIndex();
        try {
            File f = new File(fileName);
            Map<String, LinkedList<Integer>> index = test.readFile(f);
            Iterator<Entry<String, LinkedList<Integer>>> it = index.entrySet().iterator();
            while (it.hasNext()) {
                Map.Entry<String, LinkedList<Integer>> pair = it.next();
                LinkedList<Integer> lines = pair.getValue();
                ListIterator<Integer> listIterator = lines.listIterator();
                String numbers = "";
                while (listIterator.hasNext()) {
                    numbers += Integer.toString(listIterator.next()) + " ";
                }
                System.out.println(pair.getKey() + " " + numbers);
            }

            // Printing out all of the entrys
            test.asdf();
        }
        catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
