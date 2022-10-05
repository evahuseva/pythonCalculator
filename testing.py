#from main import
import re


def testing_match(line, q):
    match = re.search(r'^\d+(?:[+*-]\d+)*$', line)
    if match:
        return match and match.groupdict()['q'] == q
    else:
        assert "example doesn't match the conditions"


# def test_process_input_divide_raised_exception():
#     """
#     check dision by zero
#     :return:
#     """
#     import pytest
#     err = None
# with pytest.raises(Exception) as exc:
#         err = exc
#         process_input(10, 0, 'divide')
#     print(err.value)
