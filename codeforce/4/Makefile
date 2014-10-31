CC = g++
CFLAGS = -Wall 
DEPS = watermelon.cpp
OBJ = watermelon.o
BIN = watermelon.out 

all: $(BIN)

watermelon.o: watermelon.cpp
	$(CC) $(GFLAGS) -c watermelon.cpp

watermelon.out: watermelon.o $(DEPS)
	$(CC) $(GFLAGS) watermelon.o -o watermelon.out

clean: 
	clear
	rm -f *.o
	rm -f *.out
