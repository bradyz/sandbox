all: Node Run

Node: nodetoofar.cpp
	g++ nodetoofar.cpp -o nodetoofar

Run: Node
	./nodetoofar < input.txt

clean:
	rm -f nodetoofar
