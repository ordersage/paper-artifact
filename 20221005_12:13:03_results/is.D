

 NAS Parallel Benchmarks 4.1 Parallel C++ version with OpenMP - IS Benchmark

 Size:  2147483648  (class D)
 Iterations:   10


   iteration
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10


 IS Benchmark Completed
 class_npb       =                        D
 Size            =               2147483648
 Total threads   =                        1
 Iterations      =                       10
 Time in seconds =                    41.51
 Mop/s total     =                   517.37
 Operation type  =              keys ranked
 Verification    =               SUCCESSFUL
 Version         =                      4.1
 Compile date    =              05 Oct 2022
 Compiler ver    =                    9.4.0
 OpenMP version  =                   201511

 Compile options:
    CC           = g++ -std=c++14
    CLINK        = $(CC)
    C_LIB        = -lm
    C_INC        = -I../common 
    CFLAGS       = -O3 -fopenmp -mcmodel=medium
    CLINKFLAGS   = -O3 -fopenmp -mcmodel=medium
    RAND         = randdp


----------------------------------------------------------------------
    NPB-CPP is developed by: 
        Dalvan Griebler
        Gabriell Araujo (Sequential Porting)
        Júnior Löff (Parallel Implementation)

    In case of questions or problems, please send an e-mail to us:
        dalvan.griebler; gabriell.araujo; junior.loff@edu.pucrs.br
----------------------------------------------------------------------

