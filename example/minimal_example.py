import sys
sys.path.append("..")

import cProfile
from pycallgraphix.wrapper import MethodChart, register_method


profiler = cProfile.Profile()
profiler.enable()

class PyCallGraphObject:

    """PyCallGraph Object Class."""

    def __init__(self) -> None:
        """Initializes the class."""

        self.execute()
        methodchart = MethodChart()
        methodchart.make_graphviz_chart(
            time_resolution=3, filename="Method_Pattern.png"
        )
        profiler.disable()

        profiler.dump_stats("profile.prof")

    def execute(self):
        self.sum_recursive(3, 4)

    @register_method
    def sum_recursive(self, a, b):
        if b > 0:
            a += 1
            b -= 1
            self.print_value(prefix='current', value=a)
            return self.sum_recursive(a, b)
        else:
            self.print_value(prefix='final', value=a)
            return a
    
    @register_method
    def print_value(self, prefix, value):
        print("{} value = {}".format(prefix,value))

run = PyCallGraphObject()