CC = g++ -O2
CFLAGS = -Wall 
DEPS = tram.cpp
OBJ = tram.o
BIN = tram.out 
TESTS = input1.txt 

all: $(BIN)

tram.o: 
	$(CC) $(GFLAGS) -c tram.cpp

tram.out: tram.o $(DEPS)
	$(CC) $(GFLAGS) tram.o -o tram.out

test: tram.out 
	@echo "Test 1"
	@cat input1.txt
	@./tram.out < input1.txt

clean: 
	clear
	rm -f *.o
	rm -f *.out
