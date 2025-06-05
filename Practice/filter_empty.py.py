"""
        Написати фільтр, filter_empty.py який видаляє порожні рядки таким чином, щоб виклик
    cat somefile.txt | python filter_empty.py 
    не виводив пусті рядки, які містить файл somefile.txt

"""

import sys

for line in sys.stdin:
    if line.strip():  
        sys.stdout.write(line)


