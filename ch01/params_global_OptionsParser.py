from optparse import OptionParser
from params_global_argparse import Parameters, view_parameters
import numpy

parser = OptionParser()
parser.add_option("--p1", dest="param1", help="parameter1")
parser.add_option("--p2", dest="param2", help="parameter2")
options, args = parser.parse_args()
input_parameters = Parameters(param1=options.param1, param2=options.param2)
view_parameters(input_parameters)

