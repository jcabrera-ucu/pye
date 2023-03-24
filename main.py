#!/usr/bin/env python3

def prob_A(A, o):
    return A / o

if __name__ == "__main__":
    A = 3
    O = 6

    print(f'Menor que 3: {prob_A(A, O)}')
    print(f'Impar: {prob_A(3, 6)}')
    print(f'Menor que tres | Impar: {prob_A(2, 3)}')
