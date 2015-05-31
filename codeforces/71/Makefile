CC = g++ -O2
CFLAGS = -Wall 
DEPS = waytoolong.cpp
OBJ = waytoolong.o
BIN = waytoolong.out 
TESTS = input1.txt input2.txt 

all: $(BIN)

waytoolong.o: 
	$(CC) $(GFLAGS) -c waytoolong.cpp

waytoolong.out: waytoolong.o $(DEPS)
	$(CC) $(GFLAGS) waytoolong.o -o waytoolong.out

test: waytoolong.out 
	@echo "Test 1"
	@cat input1.txt
	@./waytoolong.out < input1.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
