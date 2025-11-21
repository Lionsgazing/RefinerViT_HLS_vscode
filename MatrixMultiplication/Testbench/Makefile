TARGET_EXEC := main.exe

BUILD_DIR := ./build
SRC_DIRS := ./src

# Compiler flags
COMPILER_FLAGS := -MMD -MP -std=c++17 -g -Wall  -Wno-long-long -Wno-unknown-pragmas -Wno-template-id-cdtor -Wno-comment -Wno-misleading-indentation -Wno-unused-label -Wno-sign-compare
#-pedantic
# VITIS location
VITIS_BASE := D:\\Xilinx\\2025.1\\Vitis

# Include dirs
VITIS_INCLUDE_BASE := $(VITIS_BASE)\\include
VITIS_INCLUDE_ETC := $(VITIS_BASE)\\include\\etc
VITIS_INCLUDE_AP_SYSC := $(VITIS_BASE)\\include\\ap_sysc
VITIS_INCLUDE_AUTO_CC := $(VITIS_BASE)\\win64\\tools\\auto_cc\\include
VITIS_INCLUDE_SYSTEMC := $(VITIS_BASE)\\win64\\tools\\systemc\\include

# Include HLS code
CUSTOM_HLS_CODE_INCLUDE := ../HLS/src

# Library dirs

# Find all C/C++ files from SRC_DIRS and add them to SRCS. Here all object and deps files are also defined.
SRCS := $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c' -or -name '*.s')
OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)
DEPS := $(OBJS:.o=.d)

LDFLAGS :=

# Turn include dirs into include flags the compiler understands.
INC_DIRS := $(shell find $(SRC_DIRS) -type d)
INC_FLAGS := $(addprefix -I,$(INC_DIRS)) $(addprefix -I,$(VITIS_INCLUDE_BASE)) $(addprefix -I,$(VITIS_INCLUDE_ETC)) $(addprefix -I,$(VITIS_INCLUDE_AP_SYSC)) $(addprefix -I,$(VITIS_INCLUDE_AUTO_CC)) $(addprefix -I,$(VITIS_INCLUDE_SYSTEMC)) $(addprefix -I,$(CUSTOM_HLS_CODE_INCLUDE))

# The -MMD and -MP flags together generate Makefiles for us!
# These files will have .d instead of .o as the output.
CPPFLAGS := $(INC_FLAGS) $(COMPILER_FLAGS)



# The final build step.
$(BUILD_DIR)/$(TARGET_EXEC): $(OBJS)
	echo $(CPPFLAGS)
	$(CXX) $(OBJS) -o $@ $(LDFLAGS)

# Build step for C source
$(BUILD_DIR)/%.c.o: %.c
	mkdir -p $(dir $@)
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

# Build step for C++ source
$(BUILD_DIR)/%.cpp.o: %.cpp
	mkdir -p $(dir $@)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@


.PHONY: clean
clean:
	rm -r $(BUILD_DIR)

# Include the .d makefiles. The - at the front suppresses the errors of missing
# Makefiles. Initially, all the .d files will be missing, and we don't want those
# errors to show up.
-include $(DEPS)