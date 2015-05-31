CC = g++ -O2
CFLAGS = -Wall 
DEPS = puzzles.cpp
OBJ = puzzles.o
BIN = puzzles.out 
TESTS = input1.txt 

all: $(BIN)

puzzles.o: puzzles.cpp
	$(CC) $(GFLAGS) -c puzzles.cpp

puzzles.out: puzzles.o $(DEPS)
	$(CC) $(GFLAGS) puzzles.o -o puzzles.out

test: puzzles.out 
	@echo "Test 1"
	@cat input1.txt
	@./puzzles.out < input1.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
