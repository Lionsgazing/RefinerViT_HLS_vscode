import copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataclasses import dataclass, asdict
from enum import Enum


class ArrayPartitionTypes(Enum):
    complete = "complete"
    block = "block"
    cyclic = "cyclic"

@dataclass(frozen=True)
class ArrayPartition:
    variable: str
    dim: int
    type: ArrayPartitionTypes
    factor: int | None = None

@dataclass(frozen=True)
class MemoryOptimization:
    arrayPartition: ArrayPartition

class PipelineStyle(Enum):
    stp = "stp"
    flp = "flp"
    frp = "frp"

@dataclass(frozen=True)
class Pipeline:
    off: bool
    II: int | None = None
    rewind: bool | None = None
    style: PipelineStyle | None = None

@dataclass(frozen=True)
class Unroll:
    off: bool
    factor: int | None = None
    skip_exit_check: bool | None = None

@dataclass(frozen=True)
class Dataflow:
    pass


@dataclass(frozen=True)
class StructureOptimization:
    label: str
    pipeline: Pipeline | None = None
    unroll: Unroll | None = None
    dataflow: Dataflow | None = None


@dataclass(frozen=True)
class OptimizationStrategy:
    memory: list[MemoryOptimization]
    structure: list[StructureOptimization]

@dataclass(frozen=True)
class HLSReport:
    reportName: str
    latency_ns: int
    bram: int
    dsp: int
    ff: int
    lut: int
    uram: int
    taskSpecificInfo: dict[str, any]
    optimizations: OptimizationStrategy

def toDictRepresentation(report: HLSReport):
    result = {
        "ReportName": [report.reportName],
        "M": [report.taskSpecificInfo["M"]],
        "P": [report.taskSpecificInfo["P"]],
        "N": [report.taskSpecificInfo["N"]],
        "Latency_ns": [report.latency_ns],
        "BRAM": [report.bram],
        "DSP": [report.dsp],
        "FF": [report.ff],
        "LUT": [report.lut],
        "URAM": [report.uram],
    }

    variables: list[str] = []
    dim: list[int] = []
    type: list[ArrayPartitionTypes] = []
    factor: list[int | None] = []
    for m in report.optimizations.memory:
        variables.append(m.arrayPartition.variable)
        dim.append(m.arrayPartition.dim)
        type.append(m.arrayPartition.type.name)
        factor.append(m.arrayPartition.factor)

    memory = {
        "ReportName": [report.reportName for i in range(len(variables))],
        "Variables": variables,
        "Dim": dim,
        "Type": type,
        "Factor": factor
    }


    labels: list[str] = []
    optimizationTechniques: list[str] = []
    
    pipelineOff: list[bool | None] = []
    pipelineII: list[int | None] = []
    pipelineRewind: list[bool | None] = []
    pipelineStyle: list[str | None] = []

    unrollOff: list[bool | None] = []
    unrollFactor: list[int | None] = []
    unrollSkipExitCheck: list[bool | None] = []

    for s in report.optimizations.structure:
        labels.append(s.label)

        usedOptimizations: list[str] = []

        if s.dataflow != None:
            usedOptimizations.append("Dataflow")
        if s.pipeline != None:
            usedOptimizations.append("Pipeline")
            pipelineOff.append(s.pipeline.off)
            pipelineII.append(s.pipeline.II)
            pipelineRewind.append(s.pipeline.rewind)
            pipelineStyle.append(s.pipeline.style)
        else:
            pipelineOff.append(None)
            pipelineII.append(None)
            pipelineRewind.append(None)
            pipelineStyle.append(None)


        if s.unroll != None:
            usedOptimizations.append("Unroll")
            unrollOff.append(s.unroll.off)
            unrollFactor.append(s.unroll.factor)
            unrollSkipExitCheck.append(s.unroll.skip_exit_check)
        else:
            unrollOff.append(None)
            unrollFactor.append(None)
            unrollSkipExitCheck.append(None)

        optimizationTechniques.append(str(usedOptimizations))



    optimizations = {
        "ReportName": [report.reportName for i in range(len(labels))],
        "Label": labels,
        "Techniques": optimizationTechniques,
        "Pipeline - Off": pipelineOff,
        "Pipeline - II": pipelineII,
        "Pipeline - Style": pipelineStyle,
        "Pipeline - Rewind": pipelineRewind,
        "Unroll - Off": unrollOff,
        "Unroll - Factor": unrollFactor,
        "Unroll - SkipExitCheck": unrollSkipExitCheck,
    }


    return result, memory, optimizations

def concatDictRepresentation(result0: dict[str, list[any]], memory0: dict[str, list[any]], optimizations0: dict[str, list[any]], result1: dict[str, list[any]], memory1: dict[str, list[any]], optimizations1: dict[str, list[any]]):
    for key, value in result0.items():
        result0[key].extend(result1[key])

    for key, value in memory0.items():
        memory0[key].extend(memory1[key])
    
    for key, value in optimizations0.items():
        optimizations0[key].extend(optimizations1[key])

    return result0, memory0, optimizations0

def PreprocessReport(reports: list[HLSReport]):
    prevResult = {}
    prevMemory = {}
    prevOptimizations = {}

    for i in range(len(reports)):
        report = reports[i]

        newResult, newMemory, newOptimizations = toDictRepresentation(report)

        if (i < 1):
            prevResult = newResult
            prevMemory = newMemory
            prevOptimizations = newOptimizations
        else:
            prevResult, prevMemory, prevOptimizations, concatDictRepresentation(prevResult, prevMemory, prevOptimizations, newResult, newMemory, newOptimizations)

    return prevResult, prevMemory, prevOptimizations


def CreateReportDataframes(reports: list[HLSReport]):
    prevResult, prevMemory, prevOptimizations = PreprocessReport(reports)

    ReportNameCollection = prevResult["ReportName"]
    Result = copy.deepcopy(prevResult)
    Result.pop("ReportName")

    dfResults = pd.DataFrame(Result, index=ReportNameCollection)

    ReportNameCollection = prevMemory["ReportName"]
    Memory = copy.deepcopy(prevMemory)
    Memory.pop("ReportName")

    dfMemory = pd.DataFrame(Memory, index=ReportNameCollection)

    ReportNameCollection = prevOptimizations["ReportName"]
    Optimizations = copy.deepcopy(prevOptimizations)
    Optimizations.pop("ReportName")

    dfOptimizations = pd.DataFrame(Optimizations, index=ReportNameCollection)

    return dfResults, dfMemory, dfOptimizations