'''
(8p.) Napisz program, który:
    *wykona mapowanie obszaru pamięci do pliku na dysku (funkcja mmap), w taki sposób, aby zapisy do pamięci były widoczne w pliku,
    *będzie wykonywał w pętli nieskończonej następujące operacje na plikach tekstowych:
        -odpyta użytkownika o nazwę pliku,
        -obliczy długość pliku i zmieni odpowiednio wielkość obszaru pamięci wspólnej i zmapowanego pliku (funkcje stat, mmap, ftruncate),
        -wczyta podany plik do zmapowanego obszaru pamięci.
'''


from mmap import mmap
import os

while True:
    file = input("Podaj plik: ")
    with open(file, "r+b") as f:

        memory = mmap(f.fileno(), 0)
        print(memory.read())  # prints the file
        pause = input()
        memory.seek(0)
        print(memory.read())
