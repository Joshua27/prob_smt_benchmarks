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

# Parameter Configurations

We used the following parameter configurations for the different constraint solving backends:

ProB's constraint solver:
- the exact preferences can be found in `ProB_Preferences.pl`
- in particular, `optimize_ast` is true
- ProB uses these preferences if the file is placed in your home directory
- in the REPL, you are able to set a preference using `-p time_out 2500`, where `time_out` is an exemplary preference's name

ProB's SMT solver:
- regarding the use of ProB's constraint solver as a theory solver, we use the same settings as in `ProB_Preferences.pl` but with the following adaptions
    - randomise\_enumeration\_order: false
    - unsat\_core\_algorithm: divide\_and\_conquer
    - use\_smt\_mode: true
    - use\_chr\_solver: false
    - use\_clpfd\_solver: true
    - optimize\_ast: true
    - use\_common\_subexpression\_elimination: false
    - normalize\_ast\_sort\_commutative: false
    - normalize\_ast: false
- the SMT solver's configurations are the following:
    - decision heuristic: EVSIDS
        - bump\_scores\_for\_bj\_clause\_only(true). % do not bump scores for all variables that occured during conflict analysis
        - vsids\_decay\_value(2). % Decision score s is updated by s/v.
        - vsids\_decay\_frequency(128). % Amount of found conflicts when to decay scores.
        - evsids\_f\_value(0.9). % A value between 0 and 1. Decision score is updated by s + f^(-k).
    - restart policy: glucose restarts
        - glucose\_restart\_recent\_lbds\_threshold(50). % The amount of conflict clauses to be considered "recent" in Glucose restarts. Small value leads to more restarts.
        - glucose\_restart\_margin\_ratio(0.8). % Do restart if defined proportion of recent LBDs average is greater than total average. Large value leads to less restarts.
        - glucose\_restart\_trail\_threshold(5000). % The amount of conflicts to enable possible emptying of the recent LBD queue to favor SAT instances too.
        - glucose\_restart\_stack\_avg\_factor(1.4). % For factor f, the last stack size needs to be larger than f * recentSizes.avg() to empty the recent LBD queue.
    - reduction of learned clauses:
        - discard\_clause\_greater\_lbd(5). % Maximum LBD score for learned clauses to not be dropped.
        - discard\_learned\_clauses\_frequency\_constant(20000).
        - discard\_learned\_clauses\_constant\_factor(500). % Remove half of the learned clauses every "frequency\_constant + constant\_factor * x" conflicts.
- Integration of Z3 in ProB
    - we use the same settings as in `ProB_Preferences.pl`
    - for Z3 itself we set the following parameters:
```
        std::shared_ptr<z3::context> ctx = ctx_data->get_context();
        params p(*ctx);

        p.set("compact", true);
        p.set("completion", true);
        p.set("timeout", (unsigned int)timeout);
        p.set("mbqi", true);
        // There was a bug in Z3 when using Lambda functions with an existential quantifier at the top-level and the option pull_nested_quantifiers (https://github.com/Z3Prover/z3/issues/5382)
        // Although this was fixed, this option still makes problems. It is extremely slow for some large constraints and does not respond to interrupts.
        // This also applies when no lambda functions are used.
        p.set("pull_nested_quantifiers",false);
        ctx_data->set_solver_params(p);
```