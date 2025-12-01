# Setup
For this custom environment to be able to use the current installation of Vitis 2025.1 it needs to know where it's located. Since there are several things that needs to know the Vitis location like the Makefiles, Intellisense and more this is just much easier to do by setting a global environment path variable. To set the system environment value needed open the "System Environment Variables" in Windows and add the following variable named:

`XILINX_BASE_DIR`: `<your directory for Xilinx install>`

Example:

`XILINX_BASE_DIR`: `D:\\Xilinx`

Note in this project im not using the included Clang compiler but instead gcc from MSYS2 UCRT64 since this generally seems to work better.