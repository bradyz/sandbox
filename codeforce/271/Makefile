CC = g++ -O2
CFLAGS = -Wall 
DEPS = year.cpp
OBJ = year.o
BIN = year.out 
TESTS = input1.txt input2.txt

all: $(BIN)

year.o: year.cpp
	$(CC) $(GFLAGS) -c year.cpp

year.out: year.o $(DEPS)
	$(CC) $(GFLAGS) year.o -o year.out

test: year.out 
	@echo "Test 1"
	@cat input1.txt
	@./year.out < input1.txt
	@echo "Test 2"
	@cat input2.txt
	@./year.out < input2.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
