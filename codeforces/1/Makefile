CC = g++
CFLAGS = -Wall 
DEPS = theatresq.cpp
OBJ = theatresq.o
BIN = theatresq.out 

all: $(BIN)

theatresq.o: theatresq.cpp
	$(CC) $(GFLAGS) -c theatresq.cpp

theatresq.out: theatresq.o $(DEPS)
	$(CC) $(GFLAGS) theatresq.o -o theatresq.out

clean: 
	clear
	rm -f *.o
	rm -f *.out
