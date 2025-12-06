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
    #pragma HLS ARRAY_PARTITION variable=A dim=2 type=complete //block factor=4
    #pragma HLS ARRAY_PARTITION variable=B dim=1 type=complete //block factor=4
    #pragma HLS ARRAY_PARTITION variable=C dim=2 type=complete //block factor=4


    //#pragma HLS DATAFLOW
    #pragma HLS PIPELINE OFF
    loopM: for (size_t m = 0; m < M; m++) {
        #pragma HLS PIPELINE STYLE=STP REWIND=TRUE
        //#pragma HLS UNROLL FACTOR=4
        loopP: for (size_t p = 0; p < P; p++) {
            //#pragma HLS PIPELINE II=1 STYLE=STP REWIND=FALSE
            //#pragma HLS PIPELINE ON II=1 STYLE=STP REWIND=TRUE
            #pragma HLS PIPELINE STYLE=STP REWIND=TRUE
            CType mulValue[N] = {};
            loopNMulParrallel: for (size_t n = 0; n < N; n++) {
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


