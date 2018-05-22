import enum as e
import functools as f


class InfomorphismErrorReason(e.Enum):
    INFO_AXIOM_VIOLATED = 0
    BAD_RANGE_F_UP = 1,
    BAD_RANGE_F_DOWN =2


class InfomorphismConstraintError(Exception):

    def __init__(self, reason, violations=[]):

        messages = {
            
            InfomorphismErrorReason.INFO_AXIOM_VIOLATED :\
            'The given mappings violate the fundamental '\
            'infomorphism constraint.',

            InfomorphismErrorReason.BAD_RANGE_F_UP :\
            'The image of \'f_up\' must be a subset of the '\
            'distal classifcation\'s type set.',

            InfomorphismErrorReason.BAD_RANGE_F_DOWN :\
            'The image of \'f_down\' must be a subset of the '\
            'proximal classifcation\'s token set.'
        }


        def format_reason(reason, cases=[]):

            if not reason in messages:
                raise ValueError

            message = messages[reason]

            if InfomorphismErrorReason.INFO_AXIOM_VIOLATED == reason:

                case_count = min(5, len(cases))

                message += 'First ' + str(case_count)\
                           + ' violations: \n'

                message += f.reduce(lambda l,v: str(v)+'\n'+l,\
                                    cases, '')

                return message

        
        self.violations = violations

        self.message = format_reason(reason, cases=violations)
