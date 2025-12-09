#include <ap_int.h>
#include "summationTree.hpp"

//A[m, n], B[n, p], C[m, p]
template<typename AType, typename BType, typename CType, int M, int N, int P>
void _MatMul(AType (&A)[M][N], BType (&B)[N][P], CType (&C)[M][P]) {
    // Required for effective UNROLLING of LoopN (use complete because of complete unroll)
    #pragma HLS ARRAY_PARTITION variable=A dim=2 type=complete
    #pragma HLS ARRAY_PARTITION variable=B dim=1 type=complete 


    #pragma HLS PIPELINE off
    loopM: for (ap_int<32> m = 0; m < M; m++) {
        #pragma HLS PIPELINE off
        loopP: for (ap_int<32> p = 0; p < P; p++) {
            #pragma HLS PIPELINE OFF
            C[m][p] = 0;
            loopN: for (size_t n = 0; n < N; n++) {
                #pragma HLS UNROLL
                CType temp = A[m][n] * B[n][p]; // Ensuring fast access of A and B is important!
                C[m][p] += temp;
            }
        }
    }
}

