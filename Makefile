EXEC = csvproc

.PHONY: all clean

all: $(EXEC)

clean:
	rm -f *.o *~ $(EXEC)

$(EXEC): main.o
	g++ main.o -o $(EXEC)

main.o: main.cpp
	g++ -c main.cpp -o main.o