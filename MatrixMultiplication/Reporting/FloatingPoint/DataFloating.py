from .DataHelpersFloating import *

def GetReports():
    reports: list[HLSReport] = []

    reports.append(HLSReport(
        reportName="Optimization 0",
        latency_ns=46420,
        bram=0,
        dsp=0,
        ff=225,
        lut=2196,
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
        latency_ns=46420,
        bram=0,
        dsp=0,
        ff=226,
        lut=2218,
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
        latency_ns=5170,
        bram=0,
        dsp=0,
        ff=220,
        lut=2479,
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
        latency_ns=10740,
        bram=0,
        dsp=0,
        ff=334,
        lut=2324,
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
        latency_ns=2610,
        bram=0,
        dsp=0,
        ff=261,
        lut=2399,
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
        latency_ns=5620,
        bram=0,
        dsp=0,
        ff=485,
        lut=4480,
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
        latency_ns=1330,
        bram=0,
        dsp=0,
        ff=483,
        lut=4584,
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
        latency_ns=3060,
        bram=0,
        dsp=0,
        ff=804,
        lut=8848,
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
        latency_ns=690,
        bram=0,
        dsp=0,
        ff=801,
        lut=8950,
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
        latency_ns=2100,
        bram=0,
        dsp=0,
        ff=1467,
        lut=17684,
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
        latency_ns=500,
        bram=0,
        dsp=0,
        ff=4112,
        lut=35018,
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
        latency_ns=200,
        bram=0,
        dsp=0,
        ff=4135,
        lut=35021,
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
        latency_ns=120,
        bram=0,
        dsp=0,
        ff=6201,
        lut=69952,
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
        latency_ns=140,
        bram=0,
        dsp=0,
        ff=10256,
        lut=139837,
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
        latency_ns=80,
        bram=0,
        dsp=0,
        ff=10327,
        lut=139840,
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
        latency_ns=80,
        bram=0,
        dsp=0,
        ff=18447,
        lut=279613,
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
        latency_ns=60,
        bram=0,
        dsp=0,
        ff=18581,
        lut=279616,
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
        latency_ns=20,
        bram=0,
        dsp=0,
        ff=36869,
        lut=559132,
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