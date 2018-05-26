import enum as e
import functools as f


class MorphismRangeError(Exception):

    def __init__(self, f_name=None, r_name=None):

        if not f_name:
            f_name = 'the given function'
        if not r_name:
            'the expected range'

        self.message = 'The image of ' + f_name \
                       + ' must be a subset of ' + r_name + '.'


class InfomorphismAxiomError(Exception):

    def __init__(self, violations=[]):
        
        self.violations = violations

        self.message = 'Given mappings violate the fundamental '\
                       'infomorphism axiom.'

        case_count = min(5, len(violations))

        if case_count > 0:
            self.message += 'First ' + str(case_count)\
                       + ' violations: \n'

            self.message += f.reduce(lambda l,v: str(v)+'\n'+l,\
                                     violations, '')

        
