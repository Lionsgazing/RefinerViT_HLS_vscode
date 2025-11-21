#include <ap_int.h>

//A[m, n], B[n, p], C[m, p]
template<typename AType, typename BType, typename CType, int M, int N, int P>
void _MatMul(AType (&A)[M][N], BType (&B)[N][P], CType (&C)[M][P]) {
    loopM: for (ap_int<32> m = 0; m < M; m++) {
        #pragma HLS PIPELINE off
        loopP: for (ap_int<32> p = 0; p < P; p++) {
            #pragma HLS PIPELINE off
            C[m][p] = 0;

            loopN: for (ap_int<32> n = 0; n < N; n++) {
                #pragma HLS PIPELINE off
                CType temp = A[m][n] * B[n][p];
                C[m][p] += temp;
            }
        }
    }
}

