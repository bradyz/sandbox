CC = g++
CFLAGS = -Wall 
DEPS = nextround.cpp
OBJ = nextround.o
BIN = nextround.out 

all: $(BIN)

nextround.o: nextround.cpp
	$(CC) $(GFLAGS) -c nextround.cpp

nextround.out: nextround.o $(DEPS)
	$(CC) $(GFLAGS) nextround.o -o nextround.out

clean: 
	clear
	rm -f *.o
	rm -f *.out
