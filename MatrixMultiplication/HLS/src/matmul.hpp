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
    #pragma HLS ARRAY_PARTITION variable=A dim=2 type=complete
    #pragma HLS ARRAY_PARTITION variable=B dim=1 type=complete

    loopM: for (ap_uint<32> m = 0; m < M; m++) {
        #pragma HLS PIPELINE off
        loopP: for (ap_uint<32> p = 0; p < P; p++) {
            #pragma HLS PIPELINE //II=2
            
            static CType mulValue[N] = {};
            loopNMulParrallel: for (ap_uint<32> n = 0; n < N; n++) {
                //#pragma HLS PIPELINE II=2
                #pragma HLS UNROLL
                //#pragma HLS BIND_OP variable=sum op=add impl=dsp
                //#pragma HLS BIND_OP variable=A op=mul impl=dsp
                //#pragma HLS BIND_OP variable=B op=mul impl=dsp
                mulValue[n] = A[m][n] * B[n][p]; // Ensuring fast access of A and B is important!
            }
            //Using much optimized summation method. Without this the MatMul would be VERY slow.
            SummationTree<CType, CType, N>(mulValue, &C[m][p]); 
            //C[m][p] = sum;
        }
    }
}


