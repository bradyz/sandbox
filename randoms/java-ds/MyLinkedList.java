import java.util.HashSet;

public class MyLinkedList<AnyType> implements Iterable<AnyType>{

    private int theSize;
    private int modCount = 0;
    private Node<AnyType> beginMarker;
    private Node<AnyType> endMarker;

    private static class Node<AnyType> {
        public Node( AnyType d, Node<AnyType> p, Node<AnyType> n  ) {
            data = d; prev = p; next = n;

        }
        public AnyType data;
        public Node<AnyType>   prev;
        public Node<AnyType>   next;
    }

    public MyLinkedList() {
        doClear();
    }

    public void doClear() {
        beginMarker = new Node<>( null, null, null  );
        endMarker = new Node<>( null, beginMarker, null  );
        beginMarker.next = endMarker;

        theSize = 0;
        modCount++;
    }

    public int size() {
        return theSize;
    }

    public boolean isEmpty() {
        return size() == 0;
    }

    private Node<AnyType> getNode( int idx, int lower, int upper  ) {
        Node<AnyType> p;

        if( idx < lower || idx > upper  )
            throw new IndexOutOfBoundsException( "getNode index: " + idx + "; size: " + size(  )  );

        if( idx < size() / 2  ) { // Search through list from the beginning
            p = beginMarker.next;
            for( int i = 0; i < idx; i++  )
                p = p.next;            
        } else { // serch through the list from the end
            p = endMarker;
            for( int i = size(); i > idx; i--  )
                p = p.prev;
        } 

        return p;
    }

    private Node<AnyType> getNode( int idx  )
    {
        return getNode( idx, 0, size(  ) - 1  );
    }

    public AnyType get( int idx  ) {
        return getNode( idx  ).data;
    }

    public AnyType set( int idx, AnyType newVal  ) {
        Node<AnyType> p = getNode( idx  );
        AnyType oldVal = p.data;

        p.data = newVal;   
        return oldVal;
    }

    private void addBefore( Node<AnyType> p, AnyType x  ) {
        Node<AnyType> newNode = new Node<>( x, p.prev, p  );
        newNode.prev.next = newNode;
        p.prev = newNode;         
        theSize++;
        modCount++;
    }   

    public void add(int idx, AnyType x) {
        addBefore( getNode(idx, 0, size()), x  );
    }

    public boolean add( AnyType x  ) {
        add( size(  ), x  );   
        return true;         
    }

    private AnyType remove( Node<AnyType> p  ) {
        p.next.prev = p.prev;
        p.prev.next = p.next;
        theSize--;
        modCount++;

        return p.data;
    }

    public AnyType remove( int idx  ) {
        return remove( getNode( idx  )  );
    }

    public String toString() {
        StringBuilder sb = new StringBuilder( "[ " );
        for( AnyType x : this  )
            sb.append( x + " "  );
        sb.append( "]"  );
        return new String( sb  );
    }

    public java.util.Iterator<AnyType> iterator(  ) {
        return new LinkedListIterator(  );
    }

    public int indexOf(Object o) {
        java.util.Iterator<AnyType> it = this.iterator();
        int index = 0;
        AnyType current = it.next();
        while(it.hasNext()) {
            if(current.equals(o)) {
                return index;
            }
            current = it.next();
            index++;
        }
        return -1;
    }

    public void reverse() {
        Node<AnyType> temp = beginMarker;
        beginMarker = endMarker;
        endMarker = temp;
        Node<AnyType> current = beginMarker;
        while(current != null) {
            temp = current.next;
            current.next = current.prev;
            current.prev = temp;
            current = current.next;
        }
    }

    public void removeDuplicates() {
        HashSet<AnyType> visited = new HashSet<AnyType>();
        java.util.Iterator<AnyType> it = this.iterator(); 
        AnyType current = it.next();
        while(it != null) {
            if(visited.contains(current))
                it.remove();
            else 
                visited.add(current);

            if(it.hasNext())
                current = it.next();
            else
                it = null;
        }
    }

    public void interleave(MyLinkedList<AnyType> other) {
        LinkedListIterator it1 = (LinkedListIterator) this.iterator();
        LinkedListIterator it2 = (LinkedListIterator) other.iterator();
        Node<AnyType> p = it1.current;
        Node<AnyType> n = it1.current;

        while(it2.hasNext()) {
            if(it1.hasNext()) {
                it1.next();
                n = it1.current;
                Node<AnyType> tmp = new Node<AnyType>(it2.current.data, p, n);
                p.next = tmp;
                it2.next();
                p = n;
            }
            else {
                this.add(it2.current.data);
                it2.next();
            }
        }
    }

    private class LinkedListIterator implements java.util.Iterator<AnyType> {
        private Node<AnyType> current = beginMarker.next;
        private int expectedModCount = modCount;
        private boolean okToRemove = false;

        public boolean hasNext(  ) {
            return current != endMarker;
        }

        public AnyType next(  ) {
            if(modCount != expectedModCount)
                throw new java.util.ConcurrentModificationException();
            if(!hasNext())
                throw new java.util.NoSuchElementException(); 

            AnyType nextItem = current.data;
            current = current.next;
            okToRemove = true;
            return nextItem;
        }

        public void remove() {
            if(modCount != expectedModCount)
                throw new java.util.ConcurrentModificationException();
            if(!okToRemove)
                throw new IllegalStateException();

            MyLinkedList.this.remove(current.prev);
            expectedModCount++;
            okToRemove = false;       
        }
    }

    public static void main( String [  ] args  ) {
        MyLinkedList<Integer> lst = new MyLinkedList<>(  );

        for(int i = 0; i < 10; i++) {
            lst.add(i);
            lst.add(i);
        }

        System.out.println(lst);
        System.out.println("Index of 2: " + lst.indexOf(2));
        lst.removeDuplicates();
        System.out.println(lst);
        lst.reverse();
        System.out.println(lst);

        MyLinkedList<Integer> lstA = new MyLinkedList<>();
        MyLinkedList<Integer> lstB = new MyLinkedList<>();

        for(int i = 0; i <= 3; i ++) {
            lstA.add(i*2);
        }

        for(int i = 0; i <= 5; i ++) {
            lstB.add(i*2 + 1);
        }

        System.out.println("LstA: " + lstA);
        System.out.println("LstB: " + lstB);
        lstA.interleave(lstB);
        System.out.println("After interleave: " + lstA);

        lstA = new MyLinkedList<>();
        lstB = new MyLinkedList<>();

        for(int i = 0; i <= 5; i ++) {
            lstA.add(i*2);
        }

        for(int i = 0; i <= 3; i ++) {
            lstB.add(i*2 + 1);
        }

        System.out.println("LstA: " + lstA);
        System.out.println("LstB: " + lstB);
        lstA.interleave(lstB);
        System.out.println("After interleave: " + lstA);
        System.out.println("LstB: " + lstB);
    }
}
