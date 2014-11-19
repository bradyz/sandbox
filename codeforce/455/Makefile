CC = g++ -O2
CFLAGS = -Wall 
DEPS = boredom.cpp
OBJ = boredom.o
BIN = boredom.out 
TESTS = input1.txt input2.txt input3.txt input4.txt 

all: $(BIN)

boredom.o: boredom.cpp
	$(CC) $(GFLAGS) -c boredom.cpp

boredom.out: boredom.o $(DEPS)
	$(CC) $(GFLAGS) boredom.o -o boredom.out

test: boredom.out 
	@echo "Test 1"
	@cat input1.txt
	@./boredom.out < input1.txt
	@echo "Test 2"
	@cat input2.txt
	@./boredom.out < input2.txt
	@echo "Test 3"
	@cat input3.txt
	@./boredom.out < input3.txt
	@echo "Test 4"
	@cat input4.txt
	@./boredom.out < input4.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
