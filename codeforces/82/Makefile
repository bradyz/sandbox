CC = g++ -O2
CFLAGS = -Wall 
DEPS = cola.cpp
OBJ = cola.o
BIN = cola.out 
TESTS = input1.txt input2.txt input3.txt input4.txt

all: $(BIN)

cola.o: cola.cpp
	$(CC) $(GFLAGS) -c cola.cpp

cola.out: cola.o $(DEPS)
	$(CC) $(GFLAGS) cola.o -o cola.out

test: cola.out 
	@echo "Test 1"
	@cat input1.txt
	@./cola.out < input1.txt
	@echo "\nTest 2"
	@cat input2.txt
	@./cola.out < input2.txt
	@echo "\nTest 3"
	@cat input3.txt
	@./cola.out < input3.txt
	@echo "\nTest 4"
	@cat input4.txt
	@./cola.out < input4.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
