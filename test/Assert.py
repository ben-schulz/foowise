import functools as f

class SetAssertionError(AssertionError):
    def __init__(self, msg=None):

        if msg:
            super(AssertionError, self)
        else:
            super(AssertionError, self, msg)


def sets_equal(left, right):

    missing_left = [str(l) for l in left if l not in right]
    missing_right = [str(r) for r in right if r not in left]

    msg = '\nSets expected equal were unequal;' \
          + '\n\nleft=' + str(left) + '\n\nright=' + str(right)

    if missing_left:

        formatted_left = f.reduce(lambda x,y: y + ', ' + x,
                                  missing_left, '\n')

        msg += '\n\nIn the left but missing on the right: ' \
               + formatted_left

    if missing_right:

        formatted_right = f.reduce(lambda x,y: y + ', ' + x,
                                   missing_right, '\n')
        msg += '\n\nIn the right but not expected: ' \
               + formatted_right


    if not (left.issubset(right) and right.issubset(left)):
        raise SetAssertionError(msg)

