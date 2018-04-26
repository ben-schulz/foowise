import Cla as C
import Validity as V
import InfomorphismConstraintError as IE

class Infomorphism:

    def __init__(self):
        self.dom = None

    def create(c_Left, c_Right, f_Up, f_Down):
        raise IE.InfomorphismConstraintError

class InfomorphismConstaintError(Exception):
    pass
