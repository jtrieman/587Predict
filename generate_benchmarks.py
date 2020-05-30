# Used to generate all benchmarks with the sim-outorder

import os

simulator_loc = "/home/emmasmith/simulator/ss3/"
benchmarks = ["gcc", "perl", "go", "li", "vortex"]
branch_preds = ["taken", "nottaken", "bimod"]

sim_out_order_cmd = '../Run.pl -db ../bench.db -dir ../results/{}_{} -benchmark {} -sim {}sim-outorder -args \"-fastfwd 50000000 -max:inst 10000000  -bpred {}\" > ../results/project/{}_{}.out 2>&1'

for benchmark in benchmarks:
    for branch_pred in branch_preds:
        os.system(sim_out_order_cmd.format(benchmark, branch_pred, benchmark, simulator_loc, branch_pred, benchmark, branch_pred))
        print ("Executing: " + sim_out_order_cmd.format(benchmark, branch_pred, benchmark, simulator_loc, branch_pred, benchmark, branch_pred))
