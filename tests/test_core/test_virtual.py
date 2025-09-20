# pylint: disable=C0111

import doctest
import unittest

from maliang.core import virtual


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str | None) -> unittest.TestSuite:
    del loader, pattern
    tests.addTests(doctest.DocTestSuite(virtual))
    return tests


if __name__ == "__main__":
    unittest.main()
