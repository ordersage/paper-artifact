"""This profile is to be used to run OrderSage, a tool for detecting and mitigating ordering effects in systems performance experiment.

It is specifically set up to help the user run experiments from the paper "Avoiding the Ordering Trap in Systems Performance Measurement" by Duplyakin et. al in USENIX ATC 20203

Instructions:

This profile creates two nodes, `controller` and `worker`. You will do all your work by logging into the controller node.

A file containing the hostname of the woker node can be found as `/tmp/worker-node`

To use this profile, you will want to:

* `ssh` into the controller node
* Test that ssh - as root - works from the controller node to the worker node by running ``sudo ssh `cat /tmp/worker-node` -C hostname``. Make sure to accept the host key for the worker node
* Clone ordersage onto the controller node with `git clone https://github.com/ordersage/ordersage.git`
* Follow the instructions for the particular experiment you are working to reproduce
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Load Emulab extensions
import geni.rspec.emulab

# Create a portal context.
pc = portal.Context()

DISKIMAGE = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD"
SCRIPT = "/local/repository/profile-scripts/install-deps.sh"

# We force both nodes to be at Utah in this profile; the worker node types
# require that site, so we make sure the controller is there too 
CM_ID = "urn:publicid:IDN+utah.cloudlab.us+authority+cm" 

pc.defineParameter("hwtype","Worker hardware type",
                   portal.ParameterType.STRING, "xl170",["xl170","c6525-100g"],
                   longDescription="Use the default value for Table 3 and 4; use '6525-100g' for Table 5 (the uFS experiment) to get special hardware that it requires")

params = pc.bindParameters();

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# This node will be used as the controller
controller = request.RawPC("contoller")

# ... and this one will be used as the worker
worker = request.RawPC("worker")

# The worker is allowed to be any type of PC, but for the paper, we use a specific type for the
# worker
worker.hardware_type = params.hwtype;

# Force both nodes to be at Utah
controller.component_manager_id = CM_ID
worker.component_manager_id = CM_ID

# Use a specific disk image that is known to work with the required software
worker.disk_image = controller.disk_image = DISKIMAGE

# Set up passwordless root ssh between the controller and worker
controller.installRootKeys(private = True, public = False)
worker.installRootKeys(private = False, public = True)

# Update both nodes and install dependencies
controller.addService(pg.Execute(shell="sh", command=SCRIPT))
worker.addService(pg.Execute(shell="sh", command=SCRIPT))


# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
