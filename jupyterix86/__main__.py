from ipykernel.kernelapp import IPKernelApp
from .kernel import KerneliX86

IPKernelApp.launch_instance(kernel_class=KerneliX86)
