"""
SSH Configurations
"""
# pre-allocated worker nodes must be added here by hostname
workers = ["c220g2-010627.wisc.cloudlab.us"]
user = "dmdu"
keyfile = "~/.ssh/id_ed25519"
port_num = 22

"""
Experiemnt Repo
"""
repo = "https://gitlab.flux.utah.edu/hamzalsh/test-experiments.git"

"""
Filepaths and commands on worker node
"""
init_script_call = "cd test-experiments && bash initialize.sh"
exp_script_call = "cd test-experiments && python3 exp_config.py"
results_dir = "~/test-experiments/results"
results_file = "results.txt"

"""
Controller options
"""
# specifies the number of runs for both fixed and random order
n_runs = 100
# specifies if random and fixed runs should be interleaved or not
interleave = True
# prints STDOUT of workers to console
verbose = True
# Ignore reset command for debugging purposes
reset = True
# Set your own random seed
seed = None

"""
Instrumentation options, in the order they need to be added to the experiment
"""
instrumentation_modules = []
#["perf"]
