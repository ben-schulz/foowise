import functools as f

class SetAssertion(AssertionError):
    def __init__(self, msg=None):

        if msg:
            Exception.__init__(self)
        else:
            Exception.__init__(self, msg)


class Assert:

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
            msg += 'In the right but not expected: ' \
                   + formatted_right
        

        if not (left.issubset(right) and right.issubset(left)):
            raise AssertionError(msg)

