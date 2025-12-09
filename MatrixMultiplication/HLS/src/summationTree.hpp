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
void SummationTree(InputType input[N], OutputType* output) {
    // Values generated at compiletime so no logic should be implemented here other than pure constants and constant arrays!
    constexpr size_t TotalReductions = constexprMath::Log2_v<N>;
    using ArrayReductionSteps = typename GeneratorDivide2<N>::type; // Compiletime generates an array of the needed reduction steps for each step into the summation tree.
    using ArrayRemaindingReductionSteps = typename GeneratorRemainder2<N>::type; // Compiletime generates an array of the needed extra steps for each step into the summation tree.

    // Iterate through all reduction steps.
    for (size_t reductionStep = 0; reductionStep < TotalReductions; reductionStep++) {
        #pragma HLS UNROLL
        // Handles the edge cases when the input size does not give a clean Log2 value.
        if (ArrayRemaindingReductionSteps::data[reductionStep]) {
            input[ArrayReductionSteps::data[reductionStep]] += input[ArrayReductionSteps::data[reductionStep] * 2];
        }

        // Creates the summation tree from the compiletime generated reduction steps.
        for (size_t storageIndex = 0; storageIndex < ArrayReductionSteps::data[reductionStep]; storageIndex++) {
            #pragma HLS UNROLL
            input[storageIndex] = input[2*storageIndex] + input[2*storageIndex + 1];
        }
    }

    // Assign final result to output
    *output = input[0];
}