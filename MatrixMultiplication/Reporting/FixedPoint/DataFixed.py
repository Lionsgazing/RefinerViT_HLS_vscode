from .DataHelpersFixed import *

def GetReports():
    reports: list[HLSReport] = []

    reports.append(HLSReport(
        reportName="Optimization 0",
        latency_ns=41300,
        bram=0,
        dsp=4,
        ff=199,
        lut=395,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 1",
        latency_ns=41300,
        bram=0,
        dsp=4,
        ff=192,
        lut=417,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 2",
        latency_ns=5150,
        bram=0,
        dsp=8,
        ff=113,
        lut=485,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=False)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 3",
        latency_ns=8340,
        bram=0,
        dsp=8,
        ff=402,
        lut=395,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 4",
        latency_ns=2590,
        bram=0,
        dsp=16,
        ff=33,
        lut=366,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=False)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 5",
        latency_ns=3060,
        bram=0,
        dsp=32,
        ff=259,
        lut=466,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=2, type=ArrayPartitionTypes.cyclic, factor=2)),
                MemoryOptimization(ArrayPartition(variable="C", dim=2, type=ArrayPartitionTypes.cyclic, factor=2)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True), unroll=Unroll(off=False, factor=2)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 6",
        latency_ns=1310,
        bram=0,
        dsp=32,
        ff=31,
        lut=518,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=2, type=ArrayPartitionTypes.cyclic, factor=2)),
                MemoryOptimization(ArrayPartition(variable="C", dim=2, type=ArrayPartitionTypes.cyclic, factor=2)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=False), unroll=Unroll(off=False, factor=2)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 7",
        latency_ns=1780,
        bram=0,
        dsp=64,
        ff=258,
        lut=832,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=2, type=ArrayPartitionTypes.cyclic, factor=4)),
                MemoryOptimization(ArrayPartition(variable="C", dim=2, type=ArrayPartitionTypes.cyclic, factor=4)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True), unroll=Unroll(off=False, factor=4)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 8",
        latency_ns=670,
        bram=0,
        dsp=64,
        ff=29,
        lut=882,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=2, type=ArrayPartitionTypes.cyclic, factor=4)),
                MemoryOptimization(ArrayPartition(variable="C", dim=2, type=ArrayPartitionTypes.cyclic, factor=4)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=False), unroll=Unroll(off=False, factor=4)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 9",
        latency_ns=1140,
        bram=0,
        dsp=128,
        ff=257,
        lut=1564,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=2, type=ArrayPartitionTypes.cyclic, factor=8)),
                MemoryOptimization(ArrayPartition(variable="C", dim=2, type=ArrayPartitionTypes.cyclic, factor=8)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True), unroll=Unroll(off=False, factor=8)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 10",
        latency_ns=340,
        bram=0,
        dsp=256,
        ff=5647,
        lut=2996,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="C", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 11",
        latency_ns=190,
        bram=0,
        dsp=256,
        ff=5664,
        lut=3005,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="C", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=False)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))

    
    reports.append(HLSReport(
        reportName="Optimization 12",
        latency_ns=110,
        bram=0,
        dsp=512,
        ff=5681,
        lut=5920,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="C", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="A", dim=1, type=ArrayPartitionTypes.cyclic, factor=2)),
                MemoryOptimization(ArrayPartition(variable="C", dim=1, type=ArrayPartitionTypes.cyclic, factor=2)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=False), unroll=Unroll(off=False, factor=2)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 13",
        latency_ns=100,
        bram=0,
        dsp=1024,
        ff=5647,
        lut=11767,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="C", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="A", dim=1, type=ArrayPartitionTypes.cyclic, factor=4)),
                MemoryOptimization(ArrayPartition(variable="C", dim=1, type=ArrayPartitionTypes.cyclic, factor=4)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True), unroll=Unroll(off=False, factor=4)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 14",
        latency_ns=70,
        bram=0,
        dsp=1024,
        ff=5712,
        lut=11776,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="C", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="A", dim=1, type=ArrayPartitionTypes.cyclic, factor=4)),
                MemoryOptimization(ArrayPartition(variable="C", dim=1, type=ArrayPartitionTypes.cyclic, factor=4)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=False), unroll=Unroll(off=False, factor=4)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))
    
    reports.append(HLSReport(
        reportName="Optimization 15",
        latency_ns=60,
        bram=0,
        dsp=2048,
        ff=5646,
        lut=23479,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="C", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="A", dim=1, type=ArrayPartitionTypes.cyclic, factor=8)),
                MemoryOptimization(ArrayPartition(variable="C", dim=1, type=ArrayPartitionTypes.cyclic, factor=8)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True), unroll=Unroll(off=False, factor=8)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 16",
        latency_ns=50,
        bram=0,
        dsp=2048,
        ff=5775,
        lut=23488,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="C", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="A", dim=1, type=ArrayPartitionTypes.cyclic, factor=8)),
                MemoryOptimization(ArrayPartition(variable="C", dim=1, type=ArrayPartitionTypes.cyclic, factor=8)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=False), unroll=Unroll(off=False, factor=8)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))

    reports.append(HLSReport(
        reportName="Optimization 17",
        latency_ns=0, # This is not a mistake btw it read 0!
        bram=0,
        dsp=4096,
        ff=0,
        lut=46848,
        uram=0,
        taskSpecificInfo={
            "M": 16,
            "N": 4,
            "P": 16,
        },
        optimizations=OptimizationStrategy(
            memory=[
                MemoryOptimization(ArrayPartition(variable="A", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="B", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="C", dim=2, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="A", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="C", dim=1, type=ArrayPartitionTypes.complete)),
                MemoryOptimization(ArrayPartition(variable="mulValue", dim=1, type=ArrayPartitionTypes.complete))
            ],
            structure=[
                StructureOptimization(
                    label="Function Base", pipeline=Pipeline(off=True)
                ),
                StructureOptimization(
                    label="LoopM", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                ),
                StructureOptimization(
                    label="LoopP", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                ),
                StructureOptimization(
                    label="LoopN", pipeline=Pipeline(off=True), unroll=Unroll(off=False)
                )
            ]
        )
    ))
    return reports