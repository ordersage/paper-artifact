# Artifact evaluation for the paper "Avoiding the Ordering Trap in Systems Performance Measurement"

This repository contains the instructions for reproducing the paper by Duplyakin
et al. at ATC '23. Some code and data are contained in other repositories,
linked here; the purpose of this document is to collect all information for
evaluating the artifacts in one place. 

## Getting Started

We offer data that can be directly checked against that reported in the paper,
as well as instructions for running the Case Studies reported in the paper.

Checking the numbers is generally simple, and can be done by examining data
presented in this repository and examining a Jupyter notebook that we provide.
This Jupyter nodebook can be re-executed either by using the evaluator's own
installation of Jupyter or by running it using a link we provide to Google
Colab, which only requires a Google account.

Re-executing the Case Study experiments is considerably more involved. The
preferred way to do this is to have a CloudLab account; we provide a profile on
CloudLab that automates the set up of the experiment, and running on the same
hardware used for the paper is likely to reproduce the same ordering effects.

It can take a few days for CloudLab accounts to be approved, and each of the
three Case Studies can take a day or more to run, so we **encourage evaluators to
leave plenty of time**. We do not provide instructions for using CloudLab here;
we assume that the evaluator is either already familiar with it or can learn
by reading the CloudLab documentation.

CloudLab is free for academic use, and can be found at https://cloudlab.us 

## Data, Code, And Other Artifacts Used in This Document

This README refers to code, data, and other resources located in several
places. We begin by listing all of them here.

#### Files In This Repository

Directories with `*_results` in the name contain data files from the case studies, as well as other experiments we ran that were not included in the paper. The key files in these directories are described below.

`Analysis_of_long_term_CloudLab_dataset.ipynb` is the Jupyter notebook used to analyze our long-term dataset; the dataset, and an alternative way to run the notebook on Google Colab are described below.

`ExperimentOrder-Survey-Spreadsheet-Artifact.xlsx` is the spreadsheet used for our literature and artifact survey.

`profile.py` is the definition of our CloudLab profile, whose use is documented below. `profile-scripts` contains scripts used by this profile.

#### OrderSage Code

https://github.com/ordersage/ordersage

This repository contains the code for OrderSage, our tool for identifying order-dependent performance effects in systems benchmarks. This is a stand-alone project that can be applied to systems benchmarking tasks on its own; in this document, it is used to run experiments the Case Studies.

#### OrderSage Profile on CloudLab

https://www.cloudlab.us/p/ordersage/paper-artifact

This link allows anyone with a CloudLab account to quickly get an environment suitable for running OrderSage; it requests one node to be the ordersage controller and another to be the worker. It also installs some dependencies and sets up a few convenience options to make the process smooth.

All code and data for this profile is actually contained in the same repository as this README; see `profile.py` in this repository for the profile definition.

#### Long-term CloudLab Performance Dataset

https://zenodo.org/record/7903144 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7903144.svg)](https://doi.org/10.5281/zenodo.7903144)

This dataset was collected over a period of more than nine months on CloudLab, and represents nearly 2.3 executions of 25 benchmarks on 1,700 machines. It is used to make many of the claims in the paper regarding the overall prevalence of order-dependent effects.

We note that this is a large file; it is 162 MB compressed, and 8.3 GB decompressed.

#### Google Colab Version of Our Jupyter Notebook

https://colab.research.google.com/drive/1JSgLaILACBGWKQW4X0I6xxFgwpe4-yuN 

The data from our long-term dataset is analyzed with a Jupyter notebook. The main copy of this notebook is stored in this repository as `Analysis_of_long_term_CloudLab_dataset.ipynb`. For convenience, we have a copy of the notebook available on Google Colab at the above URL so that the evaluator does not need to have their own instance of Jupyter.

### Experiment Repositories For OrderSage Case Studies

* https://gitlab.flux.utah.edu/gtw/memcached_testapp
* https://gitlab.flux.utah.edu/hamzalsh/test-experiments
* https://gitlab.flux.utah.edu/ptflx/ufs-test-experiments

These repositories contain the OrderSage configurations for our case studies, as well as additional scripts that wrap individual tests and runs. The use of these repositories is described later.
 
## Reproducing The Paper

This section is organized according to the figures and tables in the paper.

### Table 1:

**Requirements: Software to read `.xslx` files**

This table was produced from our survey of artifacts and evaluations as
described in Section 2 of the paper. This data was tablulated from a
spreadsheet that can be found in this repository in
`ExperimentOrder-Survey-Spreadsheet-Artifact.xlsx`

### Figures 2--6 and Table 2:

**Requirements: Jupyter notebook, either local or hosted on a public platform**

These results came from the long-term dataset described in Section 4 of the
paper. The dataset itself is available at https://zenodo.org/record/7903144

The figures can be reproduced from the dataset using the Jupyter notebook that
can be found at
https://colab.research.google.com/drive/1JSgLaILACBGWKQW4X0I6xxFgwpe4-yuN . You
can either run this notebook "in place" on Google Colab, or run the notebook
checked into this repository as `Analysis_of_long_term_CloudLab_dataset.ipynb`
in your own installation of Jupyter.

Instructions for running the notebook in Google Colab can be found at the top
of the document.

* Figures 2-4 are labeled in the titles of the plots under the heading "Visualizations for the paper"
* Figure 5 is used only for illustration purposes, and does not need to be reproduced
* Figure 6 is labeled in the titles of the plots under the heading "Visualizations for the paper"
* Table 2 uses numbers under the heading "Values for Table 2 in the paper"

### Tables 3--5:

These tables were generated via experiments run by OrderSage. We offer two ways
of reproducing the tables: comparing them to the data we collected, and
re-running the experiments and collecting your own data.

#### Checking against our data

**Requirements: software to read `.csv` files**

The data collected in the experiments described in Section 7 of the paper can
be found in subdirectories of this repository. Each directory contains files
describing the configuration of OrderSage, the environments gathered from the
node(s) the experiments were run on. The data used to produce the tables came
from:

* Test name: column `test_command`
* KW p-value: cloumn `KW_p-value`
* KW test: column `kw_dist_type`
* delta %: column `percent_diff`
* CI case: column `ci_case`

Data for the tables can be found in the files:

* Table 3: `20211012_21:02:01_results/20211012_21:02:01_node_stats.csv`
* Table 4: `npbench_and_npb_results/20221005_12_13_03_node_stats.csv`
* Table 5: `20221012_19:59:50_results/20221012_19:59:50_node_stats.csv`

Other files of interest in the data directories include:

* `*_all_env_out.csv`: information about the worker the tests were run on
* `*_all_test_results.csv`: raw results from all individual tests
* `*_stats_summary.csv`: summary statistics regarding normality, etc.

Several other data directories are included; these were from experiments that were cut from the final paper.

#### Re-running experiments on CloudLab

**Requirements: CloudLab account; multiple days of runtime**

If you wish to run your own experiments to collect data like the above, we
highly recommend doing so on CloudLab for two reasons. First, we have provided
a "profile" that makes the process simple. Second, because ordering effects can
be highly dependent on hardware, operating system, and other software
differences (as described in the paper), we would not necessarily expect to get
similar results in a different environment.

Our CloudLab profile is available at https://www.cloudlab.us/p/ordersage/paper-artifact

To run experiments for each table, you will:

* Instantiate the profile
* *Wait for startup services to finish running*: The CloudLab user interface will first report that all nodes are booted, but the scripts installing dependencies may be running. ("State: booted (startup services are still running)" in the experiment status page). Wait until the status page reports "State: Ready". This may take a few minutes.
* Log in to the "controller" node via `ssh`
* Clone the OrderSage profile via `git clone https://github.com/ordersage/ordersage`
* `cd` into the OrderSage directory (`cd ordersage`)
* Download the configuration file for the experiment you will run; the specific repositories and command lines can be found in the list below. Run the `wget` command for the experiment you are running.
* Run the experiment (`python controller.py`): **Important: this step can take more than 24 hours, depending on the experiment** . You may want to run this step inside of `screen` or `tmux` to make the experiment resilient to your client disconnecting.
* Results will be placed in a subdirectory with a timestamp in the name. Interpret the results in ``*_results/*node_stats.csv`` as described in the "checking against our data" section of this document
* Terminate your CloudLab experiment

Specific instructions for:

* Table 3:
  * When instantiating the profile, leave the value for "Worker hardware type" at its default (`xl170`) 
  * The experiment repository is https://gitlab.flux.utah.edu/gtw/memcached_testapp
  * To get the configuration file `mv -n config.py config.py.orig && wget https://gitlab.flux.utah.edu/gtw/memcached_testapp/-/raw/main/config.py`
* Table 4:
  * When instantiating the profile, leave the value for "Worker hardware type" at its default (`xl170`) 
  * The experiment repository is https://gitlab.flux.utah.edu/hamzalsh/test-experiments
  * To get the configuration file: `mv -n config.py config.py.orig && wget https://gitlab.flux.utah.edu/hamzalsh/test-experiments/-/raw/master/config.py`.  Please note the configuration of `n_runs` in this file (see the comments near line 30): a value of 3 should require under an hour of computation; increasing the number of iterations to 300 was used for the Table 3 results in the paper but requires ~24 hours to complete.

* Table 5:
  * When instantiating the profile, *change* the value for "Worker hardware type" to `6525-100g`, because this experiment requires different hardware
  * The experiment repository is https://gitlab.flux.utah.edu/ptflx/ufs-test-experiments
  * To get the configuration file:`mv -n config.py config.py.orig && wget https://gitlab.flux.utah.edu/ptflx/ufs-test-experiments/-/raw/main/config.py`


Each of these experiment repositories contains additional code and scripts that
are used to run the experiments; OrderSage automatically clones them on the worker
node, but if you wish to examine them, you can visit the URL and/or clone them 
yourself.

We note that you are *not* expected to get results that are *identical* to the
ones we reported in the paper; there is enough randomness in this process that
results are not identical every time (which is indeed the main point of the
paper). What we do expect is that you should be get results that reach the same
conclusion as our paper.

#### Re-running experiments in other environments

**Requirements: At least two machines (you must have root on one and be able to reboot it frequently); dedicated NVMe drive required for Table 5; multiple days of runtime**

If you wish to run our experiments with OrderSage on your own environment, you will need two machines:

* A "controller" that will remain on and connected to the network for the duration of the experiment
* A "worker" that will be used to run tests. You must have root access on this worker, it must not be running other workloads, and the worker will get rebooted frequently during the process. To run the experiments for Table 5, the worker must have an NVMe drive that is dedicated to the experiment (ie. has no filesystem on it, and will be re-written as part of the experiment)

We note that you are *not* likely to get the same results as we did; a major
motivator for the paper was that different hardware, software, etc. can have 
different ordering effects.

You will need to set up OrderSage and its dependencies (including passwordless
ssh to the worker) as described in its repository: [https://github.com/ordersage/ordersage](https://github.com/ordersage/ordersage). Use the
OrderSage configuration files as described in the CloudLab section above, and
interpret results as described in the "checking against our data" section
above.

