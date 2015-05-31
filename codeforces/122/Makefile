CC = g++ -O2
CFLAGS = -Wall 
DEPS = lexico.cpp
OBJ = lexico.o
BIN = lexico.out 
TESTS = input1.txt input2.txt input3.txt

all: $(BIN)

lexico.o: lexico.cpp
	$(CC) $(GFLAGS) -c lexico.cpp

lexico.out: lexico.o $(DEPS)
	$(CC) $(GFLAGS) lexico.o -o lexico.out

test: lexico.out 
	@echo "Test 1"
	@cat input1.txt
	@./lexico.out < input1.txt
	@echo "\nTest 2"
	@cat input2.txt
	@./lexico.out < input2.txt
	@echo "\nTest 3"
	@cat input3.txt
	@./lexico.out < input3.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
