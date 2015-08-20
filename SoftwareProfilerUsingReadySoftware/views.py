from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# This version just use functions as the mini functional modules. Next, I plan to build separate python modules.

# This function is the entry point of the request service--software profiling
def profiler(request):
    pass
#endof profiler(request)

# This function is used to store the files sent from the frontend
def fileManagement():
    pass
#endof fileManager()

# This function is used to call the slave--ready software--and collect the results
def slaveCall():
    pass
#endof slaveCaller()

# This function is used to consolidate the returned results collected by the slaveCall function
# Currently, database is not involved. Next, I plan to
def consolidation():
    pass
#endof consolidation()


