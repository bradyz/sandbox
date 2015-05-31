CC = g++ -O2
CFLAGS = -Wall 
DEPS = boredomrevised.cpp
OBJ = boredomrevised.o
BIN = boredomrevised.out 
TESTS = input1.txt input2.txt input3.txt

all: $(BIN)

boredomrevised.o: boredomrevised.cpp
	$(CC) $(GFLAGS) -c boredomrevised.cpp

boredomrevised.out: boredomrevised.o $(DEPS)
	$(CC) $(GFLAGS) boredomrevised.o -o boredomrevised.out

test: boredomrevised.out 
	@echo "Test 1"
	@cat input1.txt
	@./boredomrevised.out < input1.txt
	@echo "Test 2"
	@cat input2.txt
	@./boredomrevised.out < input2.txt
	@echo "Test 3"
	@cat input3.txt
	@./boredomrevised.out < input3.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
