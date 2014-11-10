CC = g++ -O2
CFLAGS = -Wall 
DEPS = capslock.cpp
OBJ = capslock.o
BIN = capslock.out 
TESTS = input1.txt input2.txt input3.txt

all: $(BIN)

capslock.o: capslock.cpp
	$(CC) $(GFLAGS) -c capslock.cpp

capslock.out: capslock.o $(DEPS)
	$(CC) $(GFLAGS) capslock.o -o capslock.out

test: capslock.out 
	@echo "Test 1"
	@cat input1.txt
	@./capslock.out < input1.txt
	@echo "\nTest 2"
	@cat input2.txt
	@./capslock.out < input2.txt
	@echo "\nTest 3"
	@cat input3.txt
	@./capslock.out < input3.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
