#pragma once

namespace constexprMath {
    // Recursive case
    template<int N>
    struct Log2 {
        static constexpr int value = 1 + Log2<N / 2>::value;
    };

    // Base case
    template<>
    struct Log2<1> {
        static constexpr int value = 0;
    };

    template<int N>
    constexpr int Log2_v = Log2<N>::value;


    template<int N, int Divisor>
    struct DivisableBy {
        static constexpr bool value = (N % Divisor) == 0;
    };

    template<int N, int Divisor>
    constexpr bool DivisableBy_V = DivisableBy<N, Divisor>::value;

    template<int N, int Divisor>
    struct DivisableRemainder {
        static constexpr int value = N % Divisor;
    };

    template<int N, int Divisor>
    constexpr int DivisableRemainder_V = DivisableRemainder<N, Divisor>::value;
}

