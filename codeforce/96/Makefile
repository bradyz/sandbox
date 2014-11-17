CC = g++ -O2
CFLAGS = -Wall 
DEPS = football.cpp
OBJ = football.o
BIN = football.out 
TESTS = input1.txt input2.txt input3.txt

all: $(BIN)

football.o: football.cpp
	$(CC) $(GFLAGS) -c football.cpp

football.out: football.o $(DEPS)
	$(CC) $(GFLAGS) football.o -o football.out

test: football.out 
	@echo "Test 1"
	@cat input1.txt
	@./football.out < input1.txt
	@echo "\nTest 2"
	@cat input2.txt
	@./football.out < input2.txt
	@echo "\nTest 3"
	@cat input3.txt
	@./football.out < input3.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
