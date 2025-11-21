#pragma once
#include <exception>
#include <iostream>
#include <string>
#include <fstream>
#include <cstddef>

template<typename MatrixType, int Rows, int Cols>
class ModelParameters{
public:
    ModelParameters(std::string filepath, MatrixType (&matrix)[Rows][Cols]) {
        std::ifstream file(filepath);

        if (!file) {
            std::cerr << "Error opening model parameters file!" << std::endl;
            exit(1);
        }

        // Line storage
        std::string readLine;
        
        // Process each line and store it in the allocated array.
        size_t currentRow = 0;
        while(std::getline(file, readLine)) {
            ProcessLine(readLine, currentRow, matrix);
            currentRow++;
        }

        file.close();
    }

private:
    void ProcessLine(std::string line, size_t row, MatrixType (&matrix)[Rows][Cols]) {
        constexpr char seperator = ',';
        size_t columnCounter = 0;
        // Isolate numbers
        std::basic_string<char>::iterator itInnerBegin = line.begin();


        std::basic_string<char>::iterator itOuter = line.begin();
        do {
            // When seperator is found go back and extract number in the defined range.
            if (*itOuter == seperator || itOuter == std::prev(line.end())){//itOuter == std::prev(std::prev(line.end()))) {
                std::string numberStr; // Define empty string
                std::basic_string<char>::iterator itInnerStop = itOuter;
                ++itInnerStop;

                for (std::basic_string<char>::iterator itInner = itInnerBegin; itInner != itInnerStop; itInner++) {
                    //Add char that defines a part of a number to the back.
                    numberStr.push_back(*itInner);
                }

                // Check that we are in the bounds of the given array
                if (row >= Rows) {
                    std::cerr << "More rows than storage can hold!" << std::endl;
                    exit(1);
                }

                if (columnCounter >= Cols) {
                    std::cerr << "More columns than storage can hold!" << std::endl;
                    exit(1);
                }

                // Convert number from string to MatrixType and store it.
                matrix[row][columnCounter] = ConvertStringToNumber(numberStr);

                // Update begin location to be 1 past the last seperator location (this is done because the seperator is not a part of the number!).
                itInnerBegin = itOuter;
                ++itInnerBegin;
                

                // Update column counter.
                columnCounter++;
            }

            itOuter++;
        } while(itOuter != line.end());
    }

    float ConvertStringToNumber(std::string number) {
        return std::stof(number);
    }
};