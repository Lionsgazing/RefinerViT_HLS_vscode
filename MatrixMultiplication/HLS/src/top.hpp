#pragma once
#include "matmul.hpp"
#include <ap_float.h>
#include <ap_fixed.h>

// Fixed point
//using AType = ap_fixed<32, 24>;
//using BType = ap_fixed<32, 24>; 
//using CType = ap_fixed<32, 24>; 

// Floating point
using AType = ap_float_single;
using BType = ap_float_single;
using CType = ap_float_single;

//constexpr size_t M = 197;
//constexpr size_t N = 32;
//constexpr size_t P = 197;

constexpr size_t M = 197;
constexpr size_t N = 32;
constexpr size_t P = 197;

void MatMul(AType A[M][N], BType B[N][P], CType C[M][P]);