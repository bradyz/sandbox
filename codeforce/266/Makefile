CC = g++ -O2
CFLAGS = -Wall 
DEPS = stone.cpp
OBJ = stone.o
BIN = stone.out 
TESTS = input1.txt input2.txt input3.txt

all: $(BIN)

stone.o: stone.cpp
	$(CC) $(GFLAGS) -c stone.cpp

stone.out: stone.o $(DEPS)
	$(CC) $(GFLAGS) stone.o -o stone.out

test: stone.out 
	@echo "Test 1"
	@cat input1.txt
	@./stone.out < input1.txt
	@echo "\nTest 2"
	@cat input2.txt
	@./stone.out < input2.txt
	@echo "\nTest 3"
	@cat input3.txt
	@./stone.out < input3.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
