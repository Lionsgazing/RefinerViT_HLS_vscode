#include "top.hpp"

void MatMul(AType (&A)[M][N], BType (&B)[N][P], CType (&C)[M][P]) {
    _MatMul<AType, BType, CType, M, N, P>(A, B, C);
}