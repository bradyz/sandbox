CC = g++ -O2
CFLAGS = -Wall 
DEPS = domino.cpp
OBJ = domino.o
BIN = domino.out 
TESTS = input1.txt input2.txt 

all: $(BIN)

domino.o: 
	$(CC) $(GFLAGS) -c domino.cpp

domino.out: domino.o $(DEPS)
	$(CC) $(GFLAGS) domino.o -o domino.out

test: domino.out 
	@echo "Test 1"
	@cat input1.txt
	@./domino.out < input1.txt
	@echo "\nTest 2"
	@cat input2.txt
	@./domino.out < input2.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
