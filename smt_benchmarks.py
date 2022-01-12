import os
import subprocess
import multiprocessing

probcli_executable = "./probcli"

z3_benchmarks = ["benchmarks/abz16_m4/", "benchmarks/abz16_m5/", "benchmarks/abz16_m6/", "benchmarks/abz16_m7/", "benchmarks/r0_geardoor/", "benchmarks/r1_valve/", "benchmarks/r2_outputs/", "benchmarks/r3_sensors/", "benchmarks/r4_handle/", "benchmarks/r5_switch/", "benchmarks/r6_lights", "benchmarks/pm_m0_aai/", "benchmarks/pm_m0_aat/", "benchmarks/pm_m0_aoo/", "benchmarks/pm_m0_voo/", "benchmarks/pm_m0_vvi", "benchmarks/pm_m0_vvt/", "benchmarks/pm_m1_aoor/", "benchmarks/pm_m1_voor/", "benchmarks/pm_m2_aai", "benchmarks/simple-two-phase/", "benchmarks/lightbot/", "benchmarks/travel_agency/", "benchmarks/search_events", "benchmarks/large_branching/", "benchmarks/prisoners-4/", "benchmarks/bakery/", "benchmarks/paxos-3/"]

dpllt_cbc_deadlock_benchmarks = ["benchmarks_cbc_deadlock/r0_geardoor", "benchmarks_cbc_deadlock/r1_valve", "benchmarks_cbc_deadlock/r2_outputs", "benchmarks_cbc_deadlock/r3_sensors", "benchmarks_cbc_deadlock/r4_handle", "benchmarks_cbc_deadlock/r5_switch/", "benchmarks_cbc_deadlock/abz16_m4", "benchmarks_cbc_deadlock/abz16_m5", "benchmarks_cbc_deadlock/abz16_m6", "benchmarks_cbc_deadlock/abz16_m7/", "benchmarks_cbc_deadlock/pm_m0_aai", "benchmarks_cbc_deadlock/pm_m0_aat", "benchmarks_cbc_deadlock/pm_m0_aoo", "benchmarks_cbc_deadlock/pm_m0_voo/", "benchmarks_cbc_deadlock/pm_m0_vvi", "benchmarks_cbc_deadlock/pm_m0_vvt", "benchmarks_cbc_deadlock/pm_m1_aoor", "benchmarks_cbc_deadlock/pm_m1_voor", "benchmarks_cbc_deadlock/pm_m2_aai/", "benchmarks_cbc_deadlock/simple-two-phase", "benchmarks_cbc_deadlock/prisoners-4", "benchmarks_cbc_deadlock/bakery", "benchmarks_cbc_deadlock/paxos-3/", "benchmarks_cbc_deadlock/lightbot", "benchmarks_cbc_deadlock/travel_agency", "benchmarks_cbc_deadlock/search_events", "benchmarks_cbc_deadlock/large_branching/"]

dpllt_cbc_invariant_benchmarks = ["benchmarks_inductive_inv/abz16_m4", "benchmarks_inductive_inv/abz16_m5", "benchmarks_inductive_inv/abz16_m6", "benchmarks_inductive_inv/abz16_m7/", "benchmarks_inductive_inv/r0_geardoor", "benchmarks_inductive_inv/r1_valve", "benchmarks_inductive_inv/r2_outputs", "benchmarks_inductive_inv/r3_sensors", "benchmarks_inductive_inv/r4_handle", "benchmarks_inductive_inv/r5_switch", "benchmarks_inductive_inv/r6_lights/", "benchmarks_inductive_inv/pm_m0_aai", "benchmarks_inductive_inv/pm_m0_aat", "benchmarks_inductive_inv/pm_m0_aoo", "benchmarks_inductive_inv/pm_m0_voo/", "benchmarks_inductive_inv/pm_m0_vvi", "benchmarks_inductive_inv/pm_m0_vvt", "benchmarks_inductive_inv/pm_m1_aoor", "benchmarks_inductive_inv/pm_m1_voor", "benchmarks_inductive_inv/pm_m2_aai/", "benchmarks_inductive_inv/prisoners-4", "benchmarks_inductive_inv/bakery", "benchmarks_inductive_inv/paxos-3/", "benchmarks_inductive_inv/lightbot", "benchmarks_inductive_inv/travel_agency", "benchmarks_inductive_inv/search_events", "benchmarks_inductive_inv/large_branching/"]

dpllt_bmc_benchmarks = ["benchmarks/abz16_m4/", "benchmarks/abz16_m5/", "benchmarks/abz16_m6/", "benchmarks/abz16_m7", "benchmarks/r0_geardoor/", "benchmarks/r1_valve/", "benchmarks/r2_outputs/", "benchmarks/r3_sensors/", "benchmarks/r4_handle/", "benchmarks/r5_switch/", "benchmarks/r6_lights", "benchmarks/pm_m0_aai/", "benchmarks/pm_m0_aat/", "benchmarks/pm_m0_aoo/", "benchmarks/pm_m0_voo/", "benchmarks/pm_m0_vvi", "benchmarks/pm_m0_vvt/", "benchmarks/pm_m1_aoor/", "benchmarks/pm_m1_voor/", "benchmarks/pm_m2_aai", "benchmarks/simple-two-phase/", "benchmarks/lightbot/", "benchmarks/travel_agency/", "benchmarks/search_events", "benchmarks/large_branching/", "benchmarks/prisoners-4/", "benchmarks/bakery/", "benchmarks/paxos-3/"]

def z3_worker(path):
    call = probcli_executable + " -bench_z3_bmc " + path
    subprocess.call(['/bin/bash', '-i', '-c', call])

def dpllt_cbc_worker(path):
    call = probcli_executable + " -bench_dpllt_cbc " + path
    subprocess.call(['/bin/bash', '-i', '-c', call])

def dpllt_bmc_worker(path):
    call = probcli_executable + " -bench_dpllt_bmc " + path
    subprocess.call(['/bin/bash', '-i', '-c', call])

def run_z3_benchmarks():
    with multiprocessing.Pool() as pool:
        pool.map_async(z3_worker, z3_benchmarks)
        pool.close()
        pool.join()

def run_dpllt_cbc_deadlock_benchmarks():
    with multiprocessing.Pool() as pool:
        pool.map_async(dpllt_cbc_worker, dpllt_cbc_deadlock_benchmarks)
        pool.close()
        pool.join()

def run_dpllt_cbc_invariant_benchmarks():
    with multiprocessing.Pool() as pool:
        pool.map_async(dpllt_cbc_worker, dpllt_cbc_invariant_benchmarks)
        pool.close()
        pool.join()

def run_dpllt_bmc_benchmarks():
    with multiprocessing.Pool() as pool:
        pool.map_async(dpllt_bmc_worker, dpllt_bmc_benchmarks)
        pool.close()
        pool.join()
