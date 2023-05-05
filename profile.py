"""
This profile is to be used to run OrderSage, a tool for detecting and mitigating ordering effects in systems performance experiment.

It is specifically set up to help the user run experiments from the paper "Avoiding the Ordering Trap in Systems Performance Measurement" by Duplyakin et. al in USENIX ATC 20203

Instructions:
TBD
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Load Emulab extensions
import geni.rspec.emulab

# Create a portal context.
pc = portal.Context()

# TODO: make these options
WORKER_HWTYPE = "xl170"
DISKIMAGE = " 	urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD:13"

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# This node will be used as the controller
controller = request.RawPC("contoller")

# ... and this one will be used as the worker
worker = request.RawPC("worker")

# The worker is allowed to be any type of PC, but for the paper, we use a specific type for the
# worker
worker.hardware_type = WORKER_HWTYPE

# Use a specific disk image that is known to work with the required software
worker.disk_image = controller.disk_image = DISKIMAGE

# Set up passwordless root ssh between the controller and worker
controller.installRootKeys(private = True, public = False)
worker.installRootKeys(private = False, public = True)

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
