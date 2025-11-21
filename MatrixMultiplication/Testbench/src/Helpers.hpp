#pragma once
#include <iostream>
#include <cmath>
#include <iomanip>

template<typename MatrixType, size_t Rows, size_t Cols>
void Print(MatrixType (&matrix)[Rows][Cols]) {
    std::cout << "[" << std::endl;
    for (size_t r = 0; r < Rows; r++) {
        for (size_t c = 0; c < Cols; c++) {
            if (c == 0) {
                std::cout << "  [";
            }
            if (c != Cols - 1) {
                std::cout << matrix[r][c] << ", ";
            }
            else {
                std::cout << matrix[r][c] << "]";
            }
        }
        std::cout << std::endl;
    }
    std::cout << "]" << std::endl;
}


template<typename MatrixType, size_t Rows, size_t Cols>
size_t Compare(MatrixType (&matrix0)[Rows][Cols], MatrixType (&matrix1)[Rows][Cols], double epsilon = 1e-05, bool printDifference = false) {
    size_t mismatches = 0;
    MatrixType minDiff = 1000000; //Big number
    MatrixType maxDiff = 0; //Low number
    MatrixType avgDiff = 0;
    long int nCurrent = 0; //Overflow possibility if size_t since it can go negative in some cases!

    for (size_t r = 0; r < Rows; r++) {
        for (size_t c = 0; c < Cols; c++) {
            MatrixType diff = std::fabs(matrix0[r][c] - matrix1[r][c]);
            
            if (diff < minDiff) {
                minDiff = diff;
            }

            if (diff > maxDiff) {
                maxDiff = diff;
            }
            if (nCurrent) {
                avgDiff = ((avgDiff * (float) (nCurrent - 1)) + diff) / nCurrent;
            }
            else {
                avgDiff = ((avgDiff * (float) (nCurrent - 1)) + diff);
            }
            std::cout << "AvgDiff: " << avgDiff << std::endl;

            if (printDifference) {
                //std::cout << "Diff: " << std::fixed << std::setprecision(floor(abs(log10(epsilon)))) << diff << std::endl;
            }
            if (diff >= epsilon) {
                mismatches++;
            }

            nCurrent++;
        }
    }

    std::cout << "Difference stats:\n";
    std::cout << "- Min: " << minDiff << "\n";
    std::cout << "- Max: " << maxDiff << "\n";
    std::cout << "- Average: " << avgDiff << "\n";
    std::cout << "- N Elements: " << nCurrent << std::endl;

    return mismatches;
}