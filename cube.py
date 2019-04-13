F = 0
B = 1
R = 2
L = 3
U = 4
D = 5
M = 6
S = 7
E = 8
FW = 9
BW = 10
RW = 11
LW = 12
UW = 13
DW = 14
X = 15
Y = 16
Z = 17

N = 0
P = 1
T = 2

to_num = {
    'F': F,
    'B': B,
    'R': R,
    'L': L,
    'U': U,
    'D': D,
    'M': M,
    'S': S,
    'E': E,
    'Fw': FW,
    'Bw': BW,
    'Rw': RW,
    'Lw': LW,
    'Uw': UW,
    'Dw': DW,
    'x': X,
    'y': Y,
    'z': Z,
    ' ': N,
    "'": P,
    "2": T
}

WHITE = 0
YELLOW = 1
RED = 2
ORANGE = 3
BLUE = 4
GREEN = 5

import re
import sys

def main():
    while True:
        face = init()
        count = 0
        sign_list = handle_input()
        while True:
            for sign in sign_list:
                face = rotate(face, sign[0], sign[1])
            count+=1
            if isComplete(face): break
        print('-> {}'.format(count))
    
def init():
    face = [[None for __ in range(3)] for _ in range(6)]
    face[F][0]=[WHITE, WHITE, WHITE]    #R(D, E, U)
    face[F][1]=[WHITE, WHITE, WHITE]    #M(D, E, U)
    face[F][2]=[WHITE, WHITE, WHITE]    #L(D, E, U)
    face[B][0]=[YELLOW, YELLOW, YELLOW] #L(U, E, D)
    face[B][1]=[YELLOW, YELLOW, YELLOW] #M(U, E, D)
    face[B][2]=[YELLOW, YELLOW, YELLOW] #R(U, E, D)
    face[R][0]=[RED, RED, RED]          #U(B, S, F)
    face[R][1]=[RED, RED, RED]          #E(B, S, F)
    face[R][2]=[RED, RED, RED]          #D(B, S, F)
    face[L][0]=[ORANGE, ORANGE, ORANGE] #D(F, S, B)
    face[L][1]=[ORANGE, ORANGE, ORANGE] #E(F, S, B)
    face[L][2]=[ORANGE, ORANGE, ORANGE] #U(F, S, B)
    face[U][0]=[BLUE, BLUE, BLUE]       #F(L, M, R)
    face[U][1]=[BLUE, BLUE, BLUE]       #S(L, M, R)
    face[U][2]=[BLUE, BLUE, BLUE]       #B(L, M, R)
    face[D][0]=[GREEN, GREEN, GREEN]    #B(R, M, L)
    face[D][1]=[GREEN, GREEN, GREEN]    #S(R, M, L)
    face[D][2]=[GREEN, GREEN, GREEN]    #F(R, M, L)
    return face

def handle_input():
    while True:
        try:
            sign_list = []
            sign_list_input = input()
            sign_str_list = re.findall(r'[A-Zwxyz\'2]+',sign_list_input)
            for sign_str in sign_str_list:
                sign1 = to_num[re.findall(r'[FFRLUDMSEwxyz]+',sign_str)[0]]
                sign2_str = re.findall(r'[\'2]',sign_str)[0] if re.findall(r'[\'2]',sign_str) else ' '
                sign2 = to_num[sign2_str]
                sign_list.append([sign1, sign2])
            return sign_list
        except:
            sys.exit()
            

def rotate(face, sign1, sign2):
    if   sign1 == F:
        if   sign2 == N:
            face[D][2], [face[L][0][0], face[L][1][0], face[L][2][0]], face[U][0], [face[R][0][2], face[R][1][2], face[R][2][2]] = [face[R][0][2], face[R][1][2], face[R][2][2]], face[D][2], [face[L][0][0], face[L][1][0], face[L][2][0]], face[U][0]
            face[F][2][0], face[F][2][1], face[F][2][2], face[F][1][2], face[F][0][2], face[F][0][1], face[F][0][0], face[F][1][0] = face[F][0][0], face[F][1][0], face[F][2][0], face[F][2][1], face[F][2][2], face[F][1][2], face[F][0][2], face[F][0][1]
        elif sign2 == P:
            face[U][0], [face[R][0][2], face[R][1][2], face[R][2][2]], face[D][2], [face[L][0][0], face[L][1][0], face[L][2][0]] = [face[R][0][2], face[R][1][2], face[R][2][2]], face[D][2], [face[L][0][0], face[L][1][0], face[L][2][0]], face[U][0]
            face[F][0][2], face[F][0][1], face[F][0][0], face[F][1][0], face[F][2][0], face[F][2][1], face[F][2][2], face[F][1][2] = face[F][0][0], face[F][1][0], face[F][2][0], face[F][2][1], face[F][2][2], face[F][1][2], face[F][0][2], face[F][0][1]
        elif sign2 == T:
            [face[L][0][0], face[L][1][0], face[L][2][0]], face[U][0], [face[R][0][2], face[R][1][2], face[R][2][2]], face[D][2] = [face[R][0][2], face[R][1][2], face[R][2][2]], face[D][2], [face[L][0][0], face[L][1][0], face[L][2][0]], face[U][0]
            face[F][2][2], face[F][1][2], face[F][0][2], face[F][0][1], face[F][0][0], face[F][1][0], face[F][2][0], face[F][2][1] = face[F][0][0], face[F][1][0], face[F][2][0], face[F][2][1], face[F][2][2], face[F][1][2], face[F][0][2], face[F][0][1]
    elif sign1 == B:
        if   sign2 == N:
            face[D][0], [face[R][0][0], face[R][1][0], face[R][2][0]], face[U][2], [face[L][0][2], face[L][1][2], face[L][2][2]] = [face[L][0][2], face[L][1][2], face[L][2][2]], face[D][0], [face[R][0][0], face[R][1][0], face[R][2][0]], face[U][2]
            face[B][0][2], face[B][1][2], face[B][2][2], face[B][2][1], face[B][2][0], face[B][1][0], face[B][0][0], face[B][0][1] = face[B][0][0], face[B][0][1], face[B][0][2], face[B][1][2], face[B][2][2], face[B][2][1], face[B][2][0], face[B][1][0]
        elif sign2 == P:
            face[U][2], [face[L][0][2], face[L][1][2], face[L][2][2]], face[D][0], [face[R][0][0], face[R][1][0], face[R][2][0]] = [face[L][0][2], face[L][1][2], face[L][2][2]], face[D][0], [face[R][0][0], face[R][1][0], face[R][2][0]], face[U][2]
            face[B][2][0], face[B][1][0], face[B][0][0], face[B][0][1], face[B][0][2], face[B][1][2], face[B][2][2], face[B][2][1] = face[B][0][0], face[B][0][1], face[B][0][2], face[B][1][2], face[B][2][2], face[B][2][1], face[B][2][0], face[B][1][0]
        elif sign2 == T:
            [face[R][0][0], face[R][1][0], face[R][2][0]], face[U][2], [face[L][0][2], face[L][1][2], face[L][2][2]], face[D][0] = [face[L][0][2], face[L][1][2], face[L][2][2]], face[D][0], [face[R][0][0], face[R][1][0], face[R][2][0]], face[U][2]
            face[B][2][2], face[B][2][1], face[B][2][0], face[B][1][0], face[B][0][0], face[B][0][1], face[B][0][2], face[B][1][2] = face[B][0][0], face[B][0][1], face[B][0][2], face[B][1][2], face[B][2][2], face[B][2][1], face[B][2][0], face[B][1][0]
    elif sign1 == R:
        if   sign2 == N:
            face[B][2], [face[D][0][0], face[D][1][0], face[D][2][0]], face[F][0], [face[U][0][2], face[U][1][2], face[U][2][2]] = [face[U][0][2], face[U][1][2], face[U][2][2]], face[B][2], [face[D][0][0], face[D][1][0], face[D][2][0]], face[F][0]
            face[R][2][0], face[R][2][1], face[R][2][2], face[R][1][2], face[R][0][2], face[R][0][1], face[R][0][0], face[R][1][0] = face[R][0][0], face[R][1][0], face[R][2][0], face[R][2][1], face[R][2][2], face[R][1][2], face[R][0][2], face[R][0][1]
        elif sign2 == P:
            face[F][0], [face[U][0][2], face[U][1][2], face[U][2][2]], face[B][2], [face[D][0][0], face[D][1][0], face[D][2][0]] = [face[U][0][2], face[U][1][2], face[U][2][2]], face[B][2], [face[D][0][0], face[D][1][0], face[D][2][0]], face[F][0]
            face[R][0][2], face[R][0][1], face[R][0][0], face[R][1][0], face[R][2][0], face[R][2][1], face[R][2][2], face[R][1][2] = face[R][0][0], face[R][1][0], face[R][2][0], face[R][2][1], face[R][2][2], face[R][1][2], face[R][0][2], face[R][0][1]
        elif sign2 == T:
            [face[D][0][0], face[D][1][0], face[D][2][0]], face[F][0], [face[U][0][2], face[U][1][2], face[U][2][2]], face[B][2] = [face[U][0][2], face[U][1][2], face[U][2][2]], face[B][2], [face[D][0][0], face[D][1][0], face[D][2][0]], face[F][0]
            face[R][2][2], face[R][1][2], face[R][0][2], face[R][0][1], face[R][0][0], face[R][1][0], face[R][2][0], face[R][2][1] = face[R][0][0], face[R][1][0], face[R][2][0], face[R][2][1], face[R][2][2], face[R][1][2], face[R][0][2], face[R][0][1]
    elif sign1 == L:
        if   sign2 == N:
            face[B][0], [face[U][0][0], face[U][1][0], face[U][2][0]], face[F][2], [face[D][0][2], face[D][1][2], face[D][2][2]] = [face[D][0][2], face[D][1][2], face[D][2][2]], face[B][0], [face[U][0][0], face[U][1][0], face[U][2][0]], face[F][2]
            face[L][0][2], face[L][1][2], face[L][2][2], face[L][2][1], face[L][2][0], face[L][1][0], face[L][0][0], face[L][0][1] = face[L][0][0], face[L][0][1], face[L][0][2], face[L][1][2], face[L][2][2], face[L][2][1], face[L][2][0], face[L][1][0]
        elif sign2 == P:
            face[F][2], [face[D][0][2], face[D][1][2], face[D][2][2]], face[B][0], [face[U][0][0], face[U][1][0], face[U][2][0]] = [face[D][0][2], face[D][1][2], face[D][2][2]], face[B][0], [face[U][0][0], face[U][1][0], face[U][2][0]], face[F][2]
            face[L][2][0], face[L][1][0], face[L][0][0], face[L][0][1], face[L][0][2], face[L][1][2], face[L][2][2], face[L][2][1] = face[L][0][0], face[L][0][1], face[L][0][2], face[L][1][2], face[L][2][2], face[L][2][1], face[L][2][0], face[L][1][0]
        elif sign2 == T:
            [face[U][0][0], face[U][1][0], face[U][2][0]], face[F][2], [face[D][0][2], face[D][1][2], face[D][2][2]], face[B][0] = [face[D][0][2], face[D][1][2], face[D][2][2]], face[B][0], [face[U][0][0], face[U][1][0], face[U][2][0]], face[F][2]
            face[L][2][2], face[L][2][1], face[L][2][0], face[L][1][0], face[L][0][0], face[L][0][1], face[L][0][2], face[L][1][2] = face[L][0][0], face[L][0][1], face[L][0][2], face[L][1][2], face[L][2][2], face[L][2][1], face[L][2][0], face[L][1][0]
    elif sign1 == U:
        if   sign2 == N:
            face[L][2], [face[B][0][0], face[B][1][0], face[B][2][0]], face[R][0], [face[F][0][2], face[F][1][2], face[F][2][2]] = [face[F][0][2], face[F][1][2], face[F][2][2]], face[L][2], [face[B][0][0], face[B][1][0], face[B][2][0]], face[R][0]
            face[U][2][0], face[U][2][1], face[U][2][2], face[U][1][2], face[U][0][2], face[U][0][1], face[U][0][0], face[U][1][0] = face[U][0][0], face[U][1][0], face[U][2][0], face[U][2][1], face[U][2][2], face[U][1][2], face[U][0][2], face[U][0][1]
        elif sign2 == P:
            face[R][0], [face[F][0][2], face[F][1][2], face[F][2][2]], face[L][2], [face[B][0][0], face[B][1][0], face[B][2][0]] = [face[F][0][2], face[F][1][2], face[F][2][2]], face[L][2], [face[B][0][0], face[B][1][0], face[B][2][0]], face[R][0]
            face[U][0][2], face[U][0][1], face[U][0][0], face[U][1][0], face[U][2][0], face[U][2][1], face[U][2][2], face[U][1][2] = face[U][0][0], face[U][1][0], face[U][2][0], face[U][2][1], face[U][2][2], face[U][1][2], face[U][0][2], face[U][0][1]
        elif sign2 == T:
            [face[B][0][0], face[B][1][0], face[B][2][0]], face[R][0], [face[F][0][2], face[F][1][2], face[F][2][2]], face[L][2] = [face[F][0][2], face[F][1][2], face[F][2][2]], face[L][2], [face[B][0][0], face[B][1][0], face[B][2][0]], face[R][0]
            face[U][2][2], face[U][1][2], face[U][0][2], face[U][0][1], face[U][0][0], face[U][1][0], face[U][2][0], face[U][2][1] = face[U][0][0], face[U][1][0], face[U][2][0], face[U][2][1], face[U][2][2], face[U][1][2], face[U][0][2], face[U][0][1]
    elif sign1 == D:
        if   sign2 == N:
            face[L][0], [face[F][0][0], face[F][1][0], face[F][2][0]], face[R][2], [face[B][0][2], face[B][1][2], face[B][2][2]] = [face[B][0][2], face[B][1][2], face[B][2][2]], face[L][0], [face[F][0][0], face[F][1][0], face[F][2][0]], face[R][2]
            face[D][0][2], face[D][1][2], face[D][2][2], face[D][2][1], face[D][2][0], face[D][1][0], face[D][0][0], face[D][0][1] = face[D][0][0], face[D][0][1], face[D][0][2], face[D][1][2], face[D][2][2], face[D][2][1], face[D][2][0], face[D][1][0]
        elif sign2 == P:
            face[R][2], [face[B][0][2], face[B][1][2], face[B][2][2]], face[L][0], [face[F][0][0], face[F][1][0], face[F][2][0]] = [face[B][0][2], face[B][1][2], face[B][2][2]], face[L][0], [face[F][0][0], face[F][1][0], face[F][2][0]], face[R][2]
            face[D][2][0], face[D][1][0], face[D][0][0], face[D][0][1], face[D][0][2], face[D][1][2], face[D][2][2], face[D][2][1] = face[D][0][0], face[D][0][1], face[D][0][2], face[D][1][2], face[D][2][2], face[D][2][1], face[D][2][0], face[D][1][0]
        elif sign2 == T:
            [face[F][0][0], face[F][1][0], face[F][2][0]], face[R][2], [face[B][0][2], face[B][1][2], face[B][2][2]], face[L][0] = [face[B][0][2], face[B][1][2], face[B][2][2]], face[L][0], [face[F][0][0], face[F][1][0], face[F][2][0]], face[R][2]
            face[D][2][2], face[D][2][1], face[D][2][0], face[D][1][0], face[D][0][0], face[D][0][1], face[D][0][2], face[D][1][2] = face[D][0][0], face[D][0][1], face[D][0][2], face[D][1][2], face[D][2][2], face[D][2][1], face[D][2][0], face[D][1][0]
    elif sign1 == M:
        if   sign2 == N:
            face[F][1], [face[D][0][1], face[D][1][1], face[D][2][1]], face[B][1], [face[U][0][1], face[U][1][1], face[U][2][1]] = [face[U][0][1], face[U][1][1], face[U][2][1]], face[F][1], [face[D][0][1], face[D][1][1], face[D][2][1]], face[B][1]
        elif sign2 == P:
            face[B][1], [face[U][0][1], face[U][1][1], face[U][2][1]], face[F][1], [face[D][0][1], face[D][1][1], face[D][2][1]] = [face[U][0][1], face[U][1][1], face[U][2][1]], face[F][1], [face[D][0][1], face[D][1][1], face[D][2][1]], face[B][1]
        elif sign2 == T:
            [face[D][0][1], face[D][1][1], face[D][2][1]], face[B][1], [face[U][0][1], face[U][1][1], face[U][2][1]], face[F][1] = [face[U][0][1], face[U][1][1], face[U][2][1]], face[F][1], [face[D][0][1], face[D][1][1], face[D][2][1]], face[B][1]
    elif sign1 == S:
        if   sign2 == N:
            face[D][1], [face[L][0][1], face[L][1][1], face[L][2][1]], face[U][1], [face[R][0][1], face[R][1][1], face[R][2][1]] = [face[R][0][1], face[R][1][1], face[R][2][1]], face[D][1], [face[L][0][1], face[L][1][1], face[L][2][1]], face[U][1]
        elif sign2 == P:
            face[U][1], [face[R][0][1], face[R][1][1], face[R][2][1]], face[D][1], [face[L][0][1], face[L][1][1], face[L][2][1]] = [face[R][0][1], face[R][1][1], face[R][2][1]], face[D][1], [face[L][0][1], face[L][1][1], face[L][2][1]], face[U][1]
        elif sign2 == T:
            [face[L][0][1], face[L][1][1], face[L][2][1]], face[U][1], [face[R][0][1], face[R][1][1], face[R][2][1]], face[D][1] = [face[R][0][1], face[R][1][1], face[R][2][1]], face[D][1], [face[L][0][1], face[L][1][1], face[L][2][1]], face[U][1]
    elif sign1 == E:
        if   sign2 == N:
            face[R][1], [face[B][0][1], face[B][1][1], face[B][2][1]], face[L][1], [face[F][0][1], face[F][1][1], face[F][2][1]] = [face[F][0][1], face[F][1][1], face[F][2][1]], face[R][1], [face[B][0][1], face[B][1][1], face[B][2][1]], face[L][1]
        elif sign2 == P:
            face[L][1], [face[F][0][1], face[F][1][1], face[F][2][1]], face[R][1], [face[B][0][1], face[B][1][1], face[B][2][1]] = [face[F][0][1], face[F][1][1], face[F][2][1]], face[R][1], [face[B][0][1], face[B][1][1], face[B][2][1]], face[L][1]
        elif sign2 == T:
            [face[B][0][1], face[B][1][1], face[B][2][1]], face[L][1], [face[F][0][1], face[F][1][1], face[F][2][1]], face[R][1] = [face[F][0][1], face[F][1][1], face[F][2][1]], face[R][1], [face[B][0][1], face[B][1][1], face[B][2][1]], face[L][1]
    elif sign1 == FW:
        if   sign2 == N:
            face = rotate(face, F, N)
            face = rotate(face, S, N)
        elif sign2 == P:
            face = rotate(face, F, P)
            face = rotate(face, S, P)
        elif sign2 == T:
            face = rotate(face, F, T)
            face = rotate(face, S, T)
    elif sign1 == BW:
        if   sign2 == N:
            face = rotate(face, B, N)
            face = rotate(face, S, P)
        elif sign2 == P:
            face = rotate(face, B, P)
            face = rotate(face, S, N)
        elif sign2 == T:
            face = rotate(face, B, T)
            face = rotate(face, S, T)
    elif sign1 == RW:
        if   sign2 == N:
            face = rotate(face, R, N)
            face = rotate(face, M, P)
        elif sign2 == P:
            face = rotate(face, R, P)
            face = rotate(face, M, N)
        elif sign2 == T:
            face = rotate(face, R, T)
            face = rotate(face, M, T)
    elif sign1 == LW:
        if   sign2 == N:
            face = rotate(face, L, N)
            face = rotate(face, M, N)
        elif sign2 == P:
            face = rotate(face, L, P)
            face = rotate(face, M, P)
        elif sign2 == T:
            face = rotate(face, L, T)
            face = rotate(face, M, T)
    elif sign1 == UW:
        if   sign2 == N:
            face = rotate(face, U, N)
            face = rotate(face, E, P)
        elif sign2 == P:
            face = rotate(face, U, P)
            face = rotate(face, E, N)
        elif sign2 == T:
            face = rotate(face, U, T)
            face = rotate(face, E, T)
    elif sign1 == DW:
        if   sign2 == N:
            face = rotate(face, D, N)
            face = rotate(face, E, N)
        elif sign2 == P:
            face = rotate(face, D, P)
            face = rotate(face, E, P)
        elif sign2 == T:
            face = rotate(face, D, T)
            face = rotate(face, E, T)
    elif sign1 == X:
        if   sign2 == N:
            face = rotate(face, RW, N)
            face = rotate(face, L, P)
        elif sign2 == P:
            face = rotate(face, RW, P)
            face = rotate(face, L, N)
        elif sign2 == T:
            face = rotate(face, RW, T)
            face = rotate(face, L, T)
    elif sign1 == Y:
        if   sign2 == N:
            face = rotate(face, UW, N)
            face = rotate(face, D, P)
        elif sign2 == P:
            face = rotate(face, UW, P)
            face = rotate(face, D, N)
        elif sign2 == T:
            face = rotate(face, UW, T)
            face = rotate(face, D, T)
    elif sign1 == Z:
        if   sign2 == N:
            face = rotate(face, FW, N)
            face = rotate(face, B, P)
        elif sign2 == P:
            face = rotate(face, FW, P)
            face = rotate(face, B, N)
        elif sign2 == T:
            face = rotate(face, FW, T)
            face = rotate(face, B, T)
    return face

def isComplete(face):
    if   len(set(sum(face[F],[])))>=2: return False
    elif len(set(sum(face[B],[])))>=2: return False
    elif len(set(sum(face[R],[])))>=2: return False
    elif len(set(sum(face[L],[])))>=2: return False
    elif len(set(sum(face[U],[])))>=2: return False
    elif len(set(sum(face[D],[])))>=2: return False
    else: return True

if __name__=='__main__':
    main()

"""
O 1
U 8
A 8
Z 2
H 1
E 2
T 4
V 4
F 4
R 8
J 8
Y 4
G 16
N 2
"""