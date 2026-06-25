from typing import List

def read_integers() -> List[int]:
    inputs = input()
    return [int(n) for n in inputs.split(',')]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
