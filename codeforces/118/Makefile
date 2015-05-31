CC = g++ -O2
CFLAGS = -Wall 
DEPS = stringtask.cpp
OBJ = stringtask.o
BIN = stringtask.out 
TESTS = input1.txt input2.txt input3.txt

all: $(BIN)

stringtask.o: stringtask.cpp
	$(CC) $(GFLAGS) -c stringtask.cpp

stringtask.out: stringtask.o $(DEPS)
	$(CC) $(GFLAGS) stringtask.o -o stringtask.out

test: stringtask.out 
	@echo "Test 1"
	@cat input1.txt
	@./stringtask.out < input1.txt
	@echo "\nTest 2"
	@cat input2.txt
	@./stringtask.out < input2.txt
	@echo "\nTest 3"
	@cat input3.txt
	@./stringtask.out < input3.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
