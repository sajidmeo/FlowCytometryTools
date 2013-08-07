from _version import version as __version__
from _doc import __doc__

from IO.fcsreader import parse_fcs
from core.containers import FCSample, FCPlate, FCSampleCollection, FCOrderedCollection
import core.graph as graph
from core.graph import plotFCM, plot_histogram2d
from core.util import build_FCplate_collection

from GUI import flowGUI


