def is_sator_square(tablet):
    #length of square
    n = len(tablet)

    #check if the matrix and its transpose is equal
    for i in range(n):
        if tablet[i][i] == tablet[n - i - 1][n - i - 1]:
            pass
        else:
            return False

        for j in range(n):
            if tablet[i][j] == tablet[j][i] and tablet[j][i] == tablet[n - i - 1][n - j - 1] and tablet[n - i - 1][n - j - 1] == tablet[n - j - 1][n - i - 1]:
                pass
            else:
                return False

    return True


import codewars_test as test
from solution import is_sator_square

@test.describe("is_sator_square")
def tester():
    read = lambda tablet: 'Testing result for this square:\n\n' + '\n'.join(' '.join(row) for row in tablet) + '\n\nArepo says'
    @test.it("Sample Tests")
    def sample_tests():
        tablet = [['T', 'E', 'N'],
                  ['E', 'Y', 'E'],
                  ['N', 'E', 'T']]
        test.assert_equals(is_sator_square(tablet), True, read(tablet))

        tablet = [['N', 'O', 'T'],
                  ['O', 'V', 'O'],
                  ['N', 'O', 'T']]
        test.assert_equals(is_sator_square(tablet), False, read(tablet))

        tablet = [['B', 'A', 'T', 'S'],
                  ['A', 'B', 'U', 'T'],
                  ['T', 'U', 'B', 'A'],
                  ['S', 'T', 'A', 'B']]
        test.assert_equals(is_sator_square(tablet), True, read(tablet))

        tablet = [['P', 'A', 'R', 'T'],
                  ['A', 'G', 'A', 'R'],
                  ['R', 'A', 'G', 'A'],
                  ['T', 'R', 'A', 'M']]
        test.assert_equals(is_sator_square(tablet), False, read(tablet))

        tablet = [['S', 'A', 'T', 'O', 'R'],
                  ['A', 'R', 'E', 'P', 'O'],
                  ['T', 'E', 'N', 'E', 'T'],
                  ['O', 'P', 'E', 'R', 'A'],
                  ['R', 'O', 'T', 'A', 'S']]
        test.assert_equals(is_sator_square(tablet), True, read(tablet))

        tablet = [['S', 'A', 'L', 'A', 'S'],
                  ['A', 'R', 'E', 'N', 'A'],
                  ['L', 'E', 'V', 'E', 'L'],
                  ['A', 'R', 'E', 'N', 'A'],
                  ['S', 'A', 'L', 'A', 'S']]
        test.assert_equals(is_sator_square(tablet), False, read(tablet))
