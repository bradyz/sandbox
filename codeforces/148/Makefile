CC = g++ -O2
CFLAGS = -Wall 
DEPS = insomnia.cpp
OBJ = insomnia.o
BIN = insomnia.out 
TESTS = input1.txt input2.txt

all: $(BIN)

insomnia.o: insomnia.cpp
	$(CC) $(GFLAGS) -c insomnia.cpp

insomnia.out: insomnia.o $(DEPS)
	$(CC) $(GFLAGS) insomnia.o -o insomnia.out

test: insomnia.out 
	@echo "Test 1"
	@cat input1.txt
	@./insomnia.out < input1.txt
	@echo "\nTest 2"
	@cat input2.txt
	@./insomnia.out < input2.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
