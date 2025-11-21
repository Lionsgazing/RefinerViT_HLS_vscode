#pragma once
#include <ap_int.h>
#include <cstddef>
#include "constexprMath.hpp"

/* Compiletime Array Fillers Implementation */

// Array type for creating compiletime arrays with custom content.
template<size_t... elements>
struct ArrayType {
    static constexpr size_t data[sizeof...(elements)] = {elements...};
};

// Generate compiletime divide2 array
template<size_t N, size_t Value, size_t... elements>
struct GeneratorDivide2Inner {
    static constexpr size_t nextValue = Value / 2;
    using type = typename GeneratorDivide2Inner<N-1, nextValue, elements..., nextValue>::type;
};

template<size_t Value, size_t... elements>
struct GeneratorDivide2Inner<0, Value, elements...> {
    using type = ArrayType<elements...>;
};


template<size_t Value>
struct GeneratorDivide2 {
    using type = typename GeneratorDivide2Inner<constexprMath::Log2_v<Value>, Value>::type;
};


// Generate compiletime remainder2 array
template<size_t N, size_t Value, size_t... elements>
struct GeneratorRemainder2Inner {
    static constexpr size_t nextValue = Value / 2;
    using type = typename GeneratorRemainder2Inner<N-1, nextValue, elements..., Value % 2>::type;
};

template<size_t Value, size_t... elements>
struct GeneratorRemainder2Inner<0, Value, elements...> {
    using type = ArrayType<elements...>;
};


template<size_t Value>
struct GeneratorRemainder2 {
    using type = typename GeneratorRemainder2Inner<constexprMath::Log2_v<Value>, Value>::type;
};



/* Summation Tree Implementation */
template<typename InputType, typename OutputType, size_t N>
constexpr void SummationTree(InputType input[N], OutputType* output) {
    constexpr size_t TotalReductions = constexprMath::Log2_v<N>;
    using ArrayReductionSteps = typename GeneratorDivide2<N>::type;
    using ArrayRemaindingReductionSteps = typename GeneratorRemainder2<N>::type;

    for (ap_uint<32> reductionStep = 0; reductionStep < TotalReductions; reductionStep++) {
        #pragma HLS UNROLL
        // If a extra step is needed do this.
        if (ArrayRemaindingReductionSteps::data[reductionStep]) {
            input[ArrayReductionSteps::data[reductionStep]] += input[ArrayReductionSteps::data[reductionStep] * 2];
        }

        for (ap_uint<32> storageIndex = 0; storageIndex < ArrayReductionSteps::data[reductionStep]; storageIndex++) {
            #pragma HLS UNROLL
            input[storageIndex] = input[2*storageIndex] + input[2*storageIndex + 1];
        }
    }

    *output = input[0];
}