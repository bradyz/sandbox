CC = g++
CFLAGS = -Wall 
DEPS = util.o
OBJ = insertionSort.o mergeSort.o
BIN = insertionSort.out mergeSort.out

all: $(BIN)

util.o: util.cpp
	$(CC) $(GFLAGS) -c util.cpp

mergeSort.o: mergeSort.cpp 
	$(CC) $(GFLAGS) -c mergeSort.cpp

mergeSort.out: mergeSort.o $(DEPS)
	$(CC) $(GFLAGS) $(DEPS) mergeSort.o -o mergeSort.out

insertionSort.o: insertionSort.cpp 
	$(CC) $(GFLAGS) -c insertionSort.cpp

insertionSort.out: insertionSort.o $(DEPS)
	$(CC) $(GFLAGS) $(DEPS) insertionSort.o -o insertionSort.out

clean: 
	clear
	rm -f *.o
	rm -f $(BIN)
	rm -f *.out
	rm -rf *.dSYM
