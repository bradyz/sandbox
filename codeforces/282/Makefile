CC = g++ -O2
CFLAGS = -Wall 
DEPS = bit.cpp
OBJ = bit.o
BIN = bit.out 
TESTS = input1.txt input2.txt input3.txt

all: $(BIN)

bit.o: bit.cpp
	$(CC) $(GFLAGS) -c bit.cpp

bit.out: bit.o $(DEPS)
	$(CC) $(GFLAGS) bit.o -o bit.out

test: bit.out 
	@echo "Test 1"
	@cat input1.txt
	@./bit.out < input1.txt
	@echo "\nTest 2"
	@cat input2.txt
	@./bit.out < input2.txt
	@echo "\nTest 3"
	@cat input3.txt
	@./bit.out < input3.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
