all: tests hack

tests: tests.c
	gcc -o $@ $^

hack: hack.c
	gcc -o $@ $^ 

clean:
	rm -f tests hack