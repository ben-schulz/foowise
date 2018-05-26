import os
import sys

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '../channels')))

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '../matrices')))


import Cla
import Validity
import Infomorphism
import InfomorphismError
import InfoPair
import InfoTetrad
import Theory
import JudgeSet
import Sequent

import ClaTable
