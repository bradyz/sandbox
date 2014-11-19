CC = g++ -O2
CFLAGS = -Wall 
DEPS = flipgame.cpp
OBJ = flipgame.o
BIN = flipgame.out 
TESTS = input1.txt input2.txt input3.txt input4.txt 

all: $(BIN)

flipgame.o: flipgame.cpp
	$(CC) $(GFLAGS) -c flipgame.cpp

flipgame.out: flipgame.o $(DEPS)
	$(CC) $(GFLAGS) flipgame.o -o flipgame.out

test: flipgame.out 
	@echo "Test 1"
	@cat input1.txt
	@./flipgame.out < input1.txt
	@echo "Test 2"
	@cat input2.txt
	@./flipgame.out < input2.txt
	@echo "Test 3"
	@cat input3.txt
	@./flipgame.out < input3.txt
	@echo "Test 4"
	@cat input4.txt
	@./flipgame.out < input4.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
