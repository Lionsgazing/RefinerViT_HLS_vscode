#include <ap_int.h>
#include <cstddef>
#include "summationTree.hpp"


//A[m, n], B[n, p], C[m, p]
template<typename AType, typename BType, typename CType, int M, int N, int P>
void _MatMul(AType (&A)[M][N], BType (&B)[N][P], CType (&C)[M][P]) {
    // Operation bindings to hardware
    //#pragma HLS BIND_OP variable=A op=mul impl=dsp
    //#pragma HLS BIND_OP variable=A op=add impl=dsp
    //#pragma HLS BIND_OP variable=B op=mul impl=dsp
    //#pragma HLS BIND_OP variable=B op=add impl=dsp

    // Array memory layout (optimized access)
    // Required for effective UNROLLING of LoopN (use complete because of complete unroll)
    #pragma HLS ARRAY_PARTITION variable=A dim=2 type=complete
    #pragma HLS ARRAY_PARTITION variable=B dim=1 type=complete 

    // Required for effective UNROLLING of LoopP (cyclic because of partial unrolling)
    //#pragma HLS ARRAY_PARTITION variable=B dim=2 type=cyclic factor=4
    //#pragma HLS ARRAY_PARTITION variable=C dim=2 type=cyclic factor=4

    // Required for effective UNROLLING of LoopM
    //#pragma HLS ARRAY_PARTITION variable=A dim=1 type=complete
    //#pragma HLS ARRAY_PARTITION variable=C dim=1 type=complete

    #pragma HLS PIPELINE OFF
    loopM: for (size_t m = 0; m < M; m++) {
        #pragma HLS PIPELINE OFF

        loopP: for (size_t p = 0; p < P; p++) {
            #pragma HLS PIPELINE

            CType mulValue[N] = {};
            #pragma HLS ARRAY_PARTITION variable=mulValue dim=1 type=complete
            loopN: for (size_t n = 0; n < N; n++) {
                #pragma HLS UNROLL
                #pragma HLS PIPELINE OFF
                mulValue[n] = A[m][n] * B[n][p]; // Ensuring fast access of A and B is important!
            }
            //Using much optimized summation method. Without this the MatMul would be VERY slow.
            SummationTree<CType, CType, N>(mulValue, &C[m][p]); 
        }
    }
}