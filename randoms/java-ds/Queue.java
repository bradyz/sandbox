interface Queue<T> {
    /**
     * Insert a new item at the back of the queue 
     */
    public void enqueue(T x);
    /**
     * Remove and return the next item from the 
     * front of the queue.  
     */ 
    public T dequeue();

}