#!/usr/bin/env python3

def prob_A(A, o):
    return A / o

def prob_A_dado_B(prob_B, prob_A_y_B):
    return prob_A_y_B / prob_B

if __name__ == "__main__":
    A = 3
    O = 6

    print(f'<= 3: {prob_A(A, O)}')
    print(f'Impar: {prob_A(3, 6)}')
    print(f'<= 3 | Impar: {prob_A(2, 3)}')

    print(f'Impar | <= 3: {prob_A_dado_B(3, 2)}')
