def test_exit_outcome():
    testdir.makepyfile(
        test_foo="""
        import pytest
        import unittest

        class MyTestCase(unittest.TestCase):
            def test_exit_outcome(self):
                pytest.exit("pytest_exit called")

            def test_should_not_run(self):
                pass
    """
    )
    result = testdir.runpytest()
    result.stdout.fnmatch_lines(["*Exit: pytest_exit called*", "*= no tests ran in *"]) 

    