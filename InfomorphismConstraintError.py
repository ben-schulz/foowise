from enum import Enum

class InfomorphismErrorReason(Enum):
    INFO_AXIOM_VIOLATED = 0
    BAD_RANGE_F_UP = 1,
    BAD_RANGE_F_DOWN =2

class InfomorphismConstraintError(Exception):

    def __init__(self, reason, constraintViolations=[]):

        self.constraintViolations = constraintViolations

        self.message = InfomorphismConstraintError.getErrorMessageByReason(reason, violations=constraintViolations)


    def getErrorMessageByReason(reason, violations=[]):

        if not reason in InfomorphismConstraintError.messages:
            raise ValueError

        message = InfomorphismConstraintError.messages[reason]

        if InfomorphismErrorReason.INFO_AXIOM_VIOLATED == reason:

            violationCount = len(violations)
            messageListingCount = min(5, violationCount)

            violationsList = InfomorphismConstraintError.violationsListToString(violations)

            message += 'First ' + str(messageListingCount)\
                       + ' violations: \n' + violationsList

        return message


    def violationsListToString(violations):

        message = ''
        for v in violations:
            message += InfomorphismConstraintError.violationToString(v) + '\n'

        return message


    def violationToString(v):
        ((x, f_Down_t), (f_Up_x, t)) = v

        return str(v)


    messages = {

        InfomorphismErrorReason.INFO_AXIOM_VIOLATED :\
        'The given mappings violate the fundamental '\
        'infomorphism constraint.',

        InfomorphismErrorReason.BAD_RANGE_F_UP :\
        'The image of \'f_Up\' must be a subset of the '\
        'distal classifcation\'s token set.',

        InfomorphismErrorReason.BAD_RANGE_F_DOWN :\
        'The image of \'f_Down\' must be a subset of the '\
        'proximal classifcation\'s type set.'
        }

        
