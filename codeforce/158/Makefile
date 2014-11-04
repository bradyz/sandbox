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

clean: 
	clear
	rm -f *.o
	rm -f *.out
