#import pytest
import pytest
# import the function
from Square import square

def test_square():
    assert square(2) == 4, "Passed"
    assert square(2.0) == 4.0, "Passed"

    assert square(5) == 25, "Passed"
    assert square(5.0) == 25.0, "Passed"

    assert square(0) == 0, "Passed"
    assert square(-1) == 1, "Passed"

