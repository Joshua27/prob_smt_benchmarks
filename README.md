# SMT Solver Integrations for the Validation of B and Event-B Models

We use a subset of TLA+ benchmarks compiled by Igor Konnov, Jure Kukovec, and Thanh-Hai Tran which they used to test their symbolic model checker [Apalache](https://dl.acm.org/doi/10.1145/3360549).
The benchmarks are publicly available [here](https://zenodo.org/record/3370071#.YFMd2y1Q1Zc).
We use the translation from TLA+ to B by Dominik Hansen and Michael Leuschel [[1]](https://dl.acm.org/doi/10.1007/978-3-642-30729-4_3) to load TLA+ models in ProB.

The benchmarks named LargeBranching and SearchEvents were compiled by Sebastian Krings to evaluate the performance of symbolic model checking for B and Event-B [[2]](https://docserv.uni-duesseldorf.de/servlets/DocumentServlet?id=43261).
The remaining B machines were compiled by Sebastian Krings and Michael Leuschel [[3]](https://dl.acm.org/doi/abs/10.1007/978-3-319-33693-0_23) and are taken from a submission to the ABZ 2016 case study by Hoang et al. [[4]](https://dl.acm.org/doi/10.1007/978-3-319-33600-8_31),
from a submission to the ABZ 2014 landing gear case study by Hansen et al. [[5]](https://dl.acm.org/doi/10.1007/s10009-015-0395-9), as well as from a model of a pacemaker by Dominique Méry and Neeraj Kumar Singh [[6]](https://dl.acm.org/doi/10.1145/2406336.2406351). The models were provided by the authors and are publicly available in ProB's [public examples repository](https://github.com/hhu-stups/specifications).

You can either use the prebuild Linux version of `probcli` or download the latest version of ProB from [here](https://prob.hhu.de/w/index.php?title=Download).

First unzip benchmarks.zip

`python3 -i smt_benchmarks.py`
`run_z3_benchmarks()`
`run_dpllt_bmc_benchmarks()`
`run_dpllt_cbc_deadlock_benchmarks()`
`run_dpllt_cbc_invariant_benchmarks()`

Bounded model checking results are stored in `benchmarks_z3_journal/` or `benchmarks_dpllt_journal/`.
Constraint based checking results are stored in `benchmarks_cbc_deadlock/` or `benchmarks_inductive_inv/` along the corresponding benchmark files.
