# Directories
BUILD_DIR = ./build
SRC_DIR = ./src
CONFIG_DIR = ./hls_config.cfg

# Xilinx / Vitis directories
XILINX_VERSION = 2025.1
XILINX_BASE_DIR = D:\\Xilinx
VITIS_BASE_DIR = $(XILINX_BASE_DIR)\\$(XILINX_VERSION)\\Vitis
VITIS_BIN_DIR = $(VITIS_BASE_DIR)\\bin

make:
	$(VITIS_BIN_DIR)\\v++.bat -c --mode hls --config $(CONFIG_DIR) --work_dir $(BUILD_DIR)

.PHONY: ide
ide:
	$(VITIS_BIN_DIR)\\vitis.bat -w ../HLS

.PHONE: clean
	clean-hls
	clean-vitis-ide

.PHONY: clean-hls
clean:
	rm -r .Xil
	rm dfx_runtime.txt
	rm -r $(BUILD_DIR)

.PHONE: clean-vitis-ide
clean-vitis-ide:
	rm -r _ide
	rm -r .cache