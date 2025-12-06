# Directories
BUILD_DIR = ./build
SRC_DIR = ./src
CONFIG_DIR = ./hls_config.cfg

# Xilinx version
XILINX_VERSION = 2025.1

# Xilinx / Vitis directories (Note XILINX_BASE_DIR is custom so look at the readme.md file!)
VITIS_BASE_DIR = $(XILINX_BASE_DIR)\\$(XILINX_VERSION)\\Vitis
VITIS_BIN_DIR = $(VITIS_BASE_DIR)\\bin

make:
	$(VITIS_BIN_DIR)\\v++.bat -c --mode hls --config $(CONFIG_DIR) --work_dir $(BUILD_DIR)

.PHONY: ide
ide:
	$(VITIS_BIN_DIR)\\vitis.bat -w ../HLS

.PHONY: clean clean-hls clean-vitis-ide
clean: clean-hls clean-ide

clean-hls:
	rm -rf .Xil
	rm -f dfx_runtime.txt
	rm -rf $(BUILD_DIR)

clean-ide:
	rm -rf _ide
	rm -rf .cache