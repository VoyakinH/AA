KEY = -Wall -Werror -pedantic
app.exe: kmp.o main.o
	g++ -o app.exe main.o kmp.o $(KEY)
clean:
	rm *.exe *.o
%.o: %.cpp
	g++ -c $< -o $@ $(KEY)