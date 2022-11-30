# import warnings


# def test_hello(recwarn):
#     warnings.warn("hello", UserWarning)
#     assert len(recwarn) == 1
#     w = recwarn.pop(UserWarning)
#     assert issubclass(w.category, UserWarning)
#     assert str(w.message) == "hello"
#     assert w.filename
#     assert w.lineno
import warnings


def api_v1():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    return 1


def test_one():
    assert api_v1() == 1
    