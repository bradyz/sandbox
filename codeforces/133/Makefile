CC = g++ -O2
CFLAGS = -Wall 
DEPS = hq9.cpp
OBJ = hq9.o
BIN = hq9.out 
TESTS = input1.txt input2.txt

all: $(BIN)

hq9.o: hq9.cpp
	$(CC) $(GFLAGS) -c hq9.cpp

hq9.out: hq9.o $(DEPS)
	$(CC) $(GFLAGS) hq9.o -o hq9.out

test: hq9.out 
	@echo "Test 1"
	@cat input1.txt
	@./hq9.out < input1.txt
	@echo "Test 2"
	@cat input2.txt
	@./hq9.out < input2.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
