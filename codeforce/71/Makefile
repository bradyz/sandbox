CC = g++
CFLAGS = -Wall 
DEPS = waytoolong.cpp
OBJ = waytoolong.o
BIN = waytoolong.out 

all: $(BIN)

waytoolong.o: waytoolong.cpp
	$(CC) $(GFLAGS) -c waytoolong.cpp

waytoolong.out: waytoolong.o $(DEPS)
	$(CC) $(GFLAGS) waytoolong.o -o waytoolong.out

clean: 
	clear
	rm -f *.o
	rm -f *.out
