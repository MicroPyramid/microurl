import unittest


def test_suite():
    test_loader = unittest.TestLoader()
    return test_loader.discover('tests', pattern='test_*.py')
