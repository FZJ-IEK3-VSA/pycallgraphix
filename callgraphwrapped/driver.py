"""Template for the Method Chart Generation.

In the PyCallGraphObject you can execute your code and generate a method pattern
containing all the functions you have decorated with the register_method.
Also a profile is generated that can be visualized with SnakeViz from the command line.
"""
import cProfile
from callgraphwrapped.wrapper import MethodChart

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
        """Define your execution here."""


run = PyCallGraphObject()
