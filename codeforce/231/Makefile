CC = g++ -O2
CFLAGS = -Wall 
DEPS = team.cpp
OBJ = team.o
BIN = team.out 
TESTS = input1.txt input2.txt 

all: $(BIN)

team.o: 
	$(CC) $(GFLAGS) -c team.cpp

team.out: team.o $(DEPS)
	$(CC) $(GFLAGS) team.o -o team.out

test: team.out 
	@echo "Test 1"
	@cat input1.txt
	@./team.out < input1.txt
	@echo "\nTest 2"
	@cat input2.txt
	@./team.out < input2.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
