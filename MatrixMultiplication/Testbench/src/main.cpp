#include "ModelParameters.hpp"
#include "Helpers.hpp"
#include "matmul.hpp"
#include <complex>
#include <math.h>
#include "constexprMath.hpp"


void test() {
    float QHead0[197][32];
    ModelParameters<float, 197, 32>("./ModelParameters/MatMulQKHead/QHead0.txt", QHead0);
    
    float KheadTransposed0[32][197];
    ModelParameters<float, 32, 197>("./ModelParameters/MatMulQKHead/KHeadTransposed0.txt", KheadTransposed0);

    float Y0[197][197];
    ModelParameters<float, 197, 197>("./ModelParameters/MatMulQKHead/Y0.txt", Y0);


    float YCalc[197][197];
    _MatMul(QHead0, KheadTransposed0, YCalc);

    std::cout << "Mismatches: " << Compare(YCalc, Y0, 1e-05, true) << std::endl;
}

void dummy() {
    float A[8][3];
    ModelParameters<float, 8, 3>("./ModelParameters/Test/A0.txt", A);
    

    float B[3][5];
    ModelParameters<float, 3, 5>("./ModelParameters/Test/B0.txt", B);
    

    float Y_real[8][5];
    ModelParameters<float, 8, 5>("./ModelParameters/Test/Y0.txt", Y_real);

    float Y_calc[8][5] = {};

    _MatMul(A, B, Y_calc);

    Print(A);
    Print(B);
    Print(Y_real);
    Print(Y_calc);

    std::cout << "Mismatches: \n" << Compare(Y_real, Y_calc) << std::endl;
}

void dummy2() {
    float A[8][3] = {
        1, 2, 3,
        4, 5, 6,
        7, 8, 9,
        10, 11, 12,
        13, 14, 15,
        16, 17, 18,
        19, 20, 21,
        22, 23, 24
    };

    float B[3][5] = {
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15
    };

    float Y_real[8][5] = {
        46, 52, 58, 64, 70,
        100, 115, 130, 145, 160,
        154, 178, 202, 226, 250,
        208, 241, 274, 307, 340,
        262, 304, 346, 388, 430,
        316, 367, 418, 469, 520,
        370, 430, 490, 550, 610,
        424, 493, 562, 631, 700
    };

    float Y_calc[8][5] = {};

    _MatMul(A, B, Y_calc);

    Print(A);
    Print(B);
    Print(Y_real);
    Print(Y_calc);

    std::cout << "Mismatches: \n" << Compare(Y_real, Y_calc, 1e-05, true) << std::endl;
}



int main() {
    test();


    /*constexpr size_t N = 267;
    using ArrayDivide2 = GeneratorDivide2<N>::type;
    using ArrayRemainder2 = GeneratorRemainder2<N>::type;
    ArrayDivide2::data[0];

    //dummy();
    //int num = 196;
    //std::cout << num % 2 << std::endl;
    //std::cout << log2(num) << std::endl;
//
    size_t temp = 197;
    for (int i = 0; i < int(log2(197)); i++) {
        std::cout << "Divided: " << temp / 2 << "| Remainder: " << temp % 2 << std::endl;
        temp = temp / 2;
    }*/
    /*ModelParameters<float> QHead("./ModelParameters/MatMulQKHead/QHead0.txt");
    ModelParameters<float> KHead_T("./ModelParameters/MatMulQKHead/KHeadTransposed0.txt");
    ModelParameters<float> Y("./ModelParameters/MatMulQKHead/Y0.txt");

    size_t M, N, P;
    QHead.GetShape(&M, &N);
    KHead_T.GetShape(&N, &P);


    Matrix<float> C(M, P);

    std::cout << "M: " << M << " | N: " << N << " | P: " << P << std::endl;

    C.Print();

    //_MatMul<float, float, float, M, N, P>(QHead, KHead_T, C);

    //std::cout << qkv_X[0][0] << std::endl;*/

    return 0;
}