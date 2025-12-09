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
- LoopM: PIPELINE STYLE=STP REWIND=TRUE
- LoopP: UNROLL
- LoopN: UNROLL

![alt text](image-6.png)

## Optimization try 7 - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
- A: ARRAY_PARTITION variable=A dim=2 type=complete
- B: ARRAY_PARTITION variable=B dim=1 type=complete
- C: ARRAY_PARTITION variable=C dim=2 type=complete

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE STYLE=STP REWIND=TRUE
- LoopP: PIPELINE STYLE=STP REWIND=TRUE
- LoopN: UNROLL

![alt text](image-7.png)


## Optimization optimal design 0 - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
Required for effective UNROLLING of LoopN (use complete because of complete unroll)
- ARRAY_PARTITION variable=A dim=2 type=complete
- ARRAY_PARTITION variable=B dim=1 type=complete 

Required for effective UNROLLING of LoopP (cyclic because of partial unrolling)
- ARRAY_PARTITION variable=C dim=2 type=cyclic factor=1
- ARRAY_PARTITION variable=B dim=2 type=cyclic factor=1

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE OFF
- LoopP: PIPELINE OFF
- LoopN: UNROLL

![alt text](image-9.png)


## Optimization optimal design 1 - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
Required for effective UNROLLING of LoopN (use complete because of complete unroll)
- ARRAY_PARTITION variable=A dim=2 type=complete
- ARRAY_PARTITION variable=B dim=1 type=complete 

Required for effective UNROLLING of LoopP (cyclic because of partial unrolling)
- ARRAY_PARTITION variable=C dim=2 type=cyclic factor=2
- ARRAY_PARTITION variable=B dim=2 type=cyclic factor=2

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE OFF
- LoopP: UNROLL factor=2 & PIPELINE
- LoopN: UNROLL

![alt text](image-10.png)

## Optimization optimal design 2 - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
Required for effective UNROLLING of LoopN (use complete because of complete unroll)
- ARRAY_PARTITION variable=A dim=2 type=complete
- ARRAY_PARTITION variable=B dim=1 type=complete 

Required for effective UNROLLING of LoopP (cyclic because of partial unrolling)
- ARRAY_PARTITION variable=C dim=2 type=cyclic factor=4
- ARRAY_PARTITION variable=B dim=2 type=cyclic factor=4

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE OFF
- LoopP: UNROLL factor=4 & PIPELINE
- LoopN: UNROLL

![alt text](image-11.png)

## Optimization optimal design 3 - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
Required for effective UNROLLING of LoopN (use complete because of complete unroll)
- ARRAY_PARTITION variable=A dim=2 type=complete
- ARRAY_PARTITION variable=B dim=1 type=complete 

Required for effective UNROLLING of LoopP (cyclic because of partial unrolling)
- ARRAY_PARTITION variable=C dim=2 type=cyclic factor=8
- ARRAY_PARTITION variable=B dim=2 type=cyclic factor=8

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE OFF
- LoopP: UNROLL factor=8 & PIPELINE
- LoopN: UNROLL

![alt text](image-12.png)

## Optimization optimal design 4 - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
Required for effective UNROLLING of LoopN (use complete because of complete unroll)
- ARRAY_PARTITION variable=A dim=2 type=complete
- ARRAY_PARTITION variable=B dim=1 type=complete 

Required for effective UNROLLING of LoopP (cyclic because of partial unrolling)
- ARRAY_PARTITION variable=C dim=2 type=complete
- ARRAY_PARTITION variable=B dim=2 type=complete

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE OFF
- LoopP: UNROLL & PIPELINE
- LoopN: UNROLL

![alt text](image-14.png)

## Optimization optimal design 5 - Summation tree based
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
Required for effective UNROLLING of LoopN (use complete because of complete unroll)
- ARRAY_PARTITION variable=A dim=2 type=complete
- ARRAY_PARTITION variable=B dim=1 type=complete 

Required for effective UNROLLING of LoopP (cyclic because of partial unrolling)
- ARRAY_PARTITION variable=C dim=2 type=cyclic factor=8
- ARRAY_PARTITION variable=B dim=2 type=cyclic factor=8

Required for effective UNROLLING of LoopM
- ARRAY_PARTITION variable=A dim=1 type=cyclic factor=2
- ARRAY_PARTITION variable=C dim=1 type=cyclic factor=2

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE OFF
- LoopP: UNROLL factor=8 & PIPELINE
- LoopN: UNROLL

![alt text](image-13.png)

## Optimization optimal design 6 - Summation tree based 
NOTE Compilation time was 6 minutes!

LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
Required for effective UNROLLING of LoopN (use complete because of complete unroll)
- ARRAY_PARTITION variable=A dim=2 type=complete
- ARRAY_PARTITION variable=B dim=1 type=complete 

Required for effective UNROLLING of LoopP (cyclic because of partial unrolling)
- ARRAY_PARTITION variable=C dim=2 type=complete
- ARRAY_PARTITION variable=B dim=2 type=complete

Required for effective UNROLLING of LoopM
- ARRAY_PARTITION variable=A dim=1 type=complete
- ARRAY_PARTITION variable=C dim=1 type=complete

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: UNROLL FACTOR=4 & PIPELINE
- LoopP: UNROLL
- LoopN: UNROLL

![alt text](image-15.png)

## Optimization optimal design COMPLETE UNROLL - Summation tree based 
NOTE Compilation time was 35 minutes!

LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
Required for effective UNROLLING of LoopN (use complete because of complete unroll)
- ARRAY_PARTITION variable=A dim=2 type=complete
- ARRAY_PARTITION variable=B dim=1 type=complete 

Required for effective UNROLLING of LoopP (cyclic because of partial unrolling)
- ARRAY_PARTITION variable=C dim=2 type=complete
- ARRAY_PARTITION variable=B dim=2 type=complete

Required for effective UNROLLING of LoopM
- ARRAY_PARTITION variable=A dim=1 type=complete
- ARRAY_PARTITION variable=C dim=1 type=complete

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: UNROLL
- LoopP: UNROLL
- LoopN: UNROLL

![alt text](image-16.png)

## Optimization optimal design - Summation tree based 
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
Required for effective UNROLLING of LoopN (use complete because of complete unroll)
- ARRAY_PARTITION variable=A dim=2 type=complete
- ARRAY_PARTITION variable=B dim=1 type=complete 

Required for effective UNROLLING of LoopP (cyclic because of partial unrolling)
- ARRAY_PARTITION variable=C dim=2 type=cyclic factor=8
- ARRAY_PARTITION variable=B dim=2 type=cyclic factor=8

Required for effective UNROLLING of LoopM
- ARRAY_PARTITION variable=A dim=1 type=complete
- ARRAY_PARTITION variable=C dim=1 type=complete

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE
- LoopP: UNROLL factor=8 & PIPELINE
- LoopN: UNROLL

![alt text](image-17.png)

## Optimization optimal design - Summation tree based 
LoopM iterations: 16
LoopP iterations: 4
LoopN iterations: 16

Array optimizations:
Required for effective UNROLLING of LoopN (use complete because of complete unroll)
- ARRAY_PARTITION variable=A dim=2 type=complete
- ARRAY_PARTITION variable=B dim=1 type=complete 

Required for effective UNROLLING of LoopP (cyclic because of partial unrolling)
- ARRAY_PARTITION variable=C dim=2 type=cyclic factor=8
- ARRAY_PARTITION variable=B dim=2 type=cyclic factor=8

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE
- LoopP: UNROLL factor=8 & PIPELINE
- LoopN: UNROLL

![alt text](image-18.png)



## BIG DESIGN UNROLL - Summation tree based 
LoopM iterations: 197
LoopP iterations: 32
LoopN iterations: 197

Array optimizations:
Required for effective UNROLLING of LoopN (use complete because of complete unroll)
- ARRAY_PARTITION variable=A dim=2 type=complete
- ARRAY_PARTITION variable=B dim=1 type=complete 

Required for effective UNROLLING of LoopP (cyclic because of partial unrolling)
- ARRAY_PARTITION variable=C dim=2 type=cyclic factor=4
- ARRAY_PARTITION variable=B dim=2 type=cyclic factor=4

Loop optimizations:
- Function base: PIPELINE OFF
- LoopM: PIPELINE
- LoopP: UNROLL factor=4 & PIPELINE
- LoopN: UNROLL

![alt text](image-19.png)


JESUS FUCK
![alt text](image-20.png)