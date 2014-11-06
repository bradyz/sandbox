CC = g++
CFLAGS = -Wall 
DEPS = taxi.cpp
OBJ = taxi.o
BIN = taxi.out 

all: $(BIN)

taxi.o: taxi.cpp
	$(CC) $(GFLAGS) -c taxi.cpp

taxi.out: taxi.o $(DEPS)
	$(CC) $(GFLAGS) taxi.o -o taxi.out

test: taxi.out
	@echo "Test 1"
	@cat input1.txt
	@./taxi.out < input1.txt
	@echo "\nTest 2"
	@cat input2.txt
	@./taxi.out < input2.txt
	@echo "\nTest 3"
	@cat input3.txt
	@./taxi.out < input3.txt
	@echo "\nTest 4"
	@cat input4.txt
	@./taxi.out < input4.txt
	@echo "\nTest 5"
	@cat input5.txt
	@./taxi.out < input5.txt
	@echo "\nTest 6"
	@cat input6.txt
	@./taxi.out < input6.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
