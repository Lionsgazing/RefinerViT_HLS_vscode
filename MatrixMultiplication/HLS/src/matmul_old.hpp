#include <ap_int.h>
#include <cstddef>
#include "constexprMath.hpp"


template<typename InputType, typename OutputType, size_t N>
void SummationTreeBased(InputType Input[N], OutputType *Output) {
    constexpr int TotalReductionSteps = constexprMath::Log2_v<N>;
    constexpr bool IsDivisableBy2 = constexprMath::DivisableBy_V<N, 2>;
    constexpr int DivisableRemainder = constexprMath::DivisableRemainder_V<N, 2>;
    std::cout << "ReductionSteps: " << TotalReductionSteps << std::endl;
    std::cout << "IsDivisableBy2: " << IsDivisableBy2 << std::endl;
    std::cout << "DivisableRemainder: " << DivisableRemainder << std::endl;

    // Offset N by divisable remainder to get the correct amount of summation tree splits
    constexpr size_t NMax = N - DivisableRemainder;
    constexpr size_t NOffset = NMax;
    
    //for (int n = 1; n < N; n++) {
    //    Input[0] = Input[0] + Input[n];
    //}

    ap_uint<32> NLimit = NMax; // Initial loop iteration count.
    std::cout << "N: " << N << std::endl;
    std::cout << "NLimit: " << NLimit << std::endl;
    for (ap_uint<32> r = 0; r < TotalReductionSteps; r++) {
        #pragma HLS UNROLL
        NLimit = NLimit / 2; // Update loop iteration count.
        for (ap_uint<32> n = 0; n < NLimit; n++) {
            #pragma HLS UNROLL
            Input[n] = Input[2*n] + Input[2*n+1]; // Do partial summations (Using input as storage)
            std::cout << "n: " << n << " | " << Input[n] << std::endl;
        }
    }
    
    *Output = Input[0];
}

template<typename InputType, typename OutputType, size_t N, size_t NStart, size_t NEnd>
void SummationTreeUnGuarded(InputType (&Input)[N], OutputType* Output) {
    constexpr int TotalReductionSteps = constexprMath::Log2_v<N>;
    std::cout << "ReductionSteps: " << TotalReductionSteps << std::endl;
    std::cout << "N: " << N << std::endl;
    std::cout << "NStart: " << NStart << std::endl;
    std::cout << "NEnd: " << NEnd << std::endl << std::endl;
    
    ap_uint<32> NLimit = NStart; // Initial loop iteration count.
    for (ap_uint<32> r = 0; r < TotalReductionSteps; r++) {
        #pragma HLS UNROLL
        NLimit = NLimit / 2; // Update loop iteration count.
        std::cout << "NLimit: " << NLimit << std::endl;
        for (ap_uint<32> n = NEnd; n < NLimit; n++) {
            #pragma HLS UNROLL
            Input[n] = Input[2*n] + Input[2*n+1]; // Do partial summations (Using input as storage)
            std::cout << "n: " << n << " | " << Input[n] << std::endl;
        }
    }
    
    *Output = Input[NEnd];
}

template<typename InputType, typename OutputType, size_t N>
void SummationTree(InputType (&Input)[N], OutputType* Output) {
    constexpr bool IsDivisableBy2 = constexprMath::DivisableBy_V<N, 2>;
    constexpr int DivisableRemainder = constexprMath::DivisableRemainder_V<N, 2>;
    std::cout << "IsDivisableBy2: " << IsDivisableBy2 << std::endl;
    std::cout << "DivisableRemainder: " << DivisableRemainder << std::endl;

    constexpr size_t NOffset = N - DivisableRemainder - 1;

    std::cout << "<<Before>>" << std::endl;
    for (int i = 0; i < N; i++) {
        std::cout << Input[i] << ", ";
    }
    std::cout << std::endl;

    SummationTreeUnGuarded<InputType, OutputType, N, N, NOffset>(Input, Output);
    std::cout << "<<NOffset>>" << std::endl;
    for (int i = 0; i < N; i++) {
        std::cout << Input[i] << ", ";
    }
    std::cout << std::endl;


    SummationTreeUnGuarded<InputType, OutputType, N, NOffset, 0>(Input, Output);
    std::cout << "<<N>>" << std::endl;
    for (int i = 0; i < N; i++) {
        std::cout << Input[i] << ", ";
    }
    std::cout << std::endl << std::endl;
}



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


