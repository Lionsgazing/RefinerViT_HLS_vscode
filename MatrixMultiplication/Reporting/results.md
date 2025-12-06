# Results


## Baseline - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
- A: ARRAY_PARTITION variable=A dim=2 type=complete
- B: ARRAY_PARTITION variable=B dim=1 type=complete
- C: ARRAY_PARTITION variable=C dim=2 type=complete

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE OFF
- LoopP: PIPELINE OFF
- LoopN: PIPELINE OFF

![alt text](image.png)

## Optimization try 1 - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
- A: ARRAY_PARTITION variable=A dim=2 type=complete
- B: ARRAY_PARTITION variable=B dim=1 type=complete
- C: ARRAY_PARTITION variable=C dim=2 type=complete

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE OFF
- LoopP: PIPELINE OFF
- LoopN: UNROLL

![alt text](image-1.png)

## Optimization try 2 - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
- A: ARRAY_PARTITION variable=A dim=2 type=complete
- B: ARRAY_PARTITION variable=B dim=1 type=complete
- C: ARRAY_PARTITION variable=C dim=2 type=complete

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE OFF
- LoopP: PIPELINE ON
- LoopN: UNROLL

![alt text](image-2.png)

## Optimization try 3 - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
- A: ARRAY_PARTITION variable=A dim=2 type=complete
- B: ARRAY_PARTITION variable=B dim=1 type=complete
- C: ARRAY_PARTITION variable=C dim=2 type=complete

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE ON
- LoopP: PIPELINE ON
- LoopN: UNROLL

![alt text](image-3.png)

## Optimization try 4 - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
- A: ARRAY_PARTITION variable=A dim=2 type=complete
- B: ARRAY_PARTITION variable=B dim=1 type=complete
- C: ARRAY_PARTITION variable=C dim=2 type=complete

Loop optimizations:
- Function base: DATAFLOW
- LoopM: PIPELINE ON
- LoopP: PIPELINE ON
- LoopN: UNROLL

![alt text](image-4.png)


## Optimization try 5 - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
- A: ARRAY_PARTITION variable=A dim=2 type=complete
- B: ARRAY_PARTITION variable=B dim=1 type=complete
- C: ARRAY_PARTITION variable=C dim=2 type=complete

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE OFF
- LoopP: UNROLL
- LoopN: UNROLL

![alt text](image-5.png)




## Optimization try 6 - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
- A: ARRAY_PARTITION variable=A dim=2 type=complete
- B: ARRAY_PARTITION variable=B dim=1 type=complete
- C: ARRAY_PARTITION variable=C dim=2 type=complete

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM:  PIPELINE STYLE=STP REWIND=TRUE
- LoopP: UNROLL
- LoopN: UNROLL

![alt text](image-6.png)