hello: hellomake.o hellofunc.o
	$(CC) hellomake.o hellofunc.o -o hello
hellomake.o: hellomake.c hellomake.h
	$(CC) -c hellomake.c
hellofunc.o: hellofunc.c hellomake.h
	$(CC) -c hellofunc.c