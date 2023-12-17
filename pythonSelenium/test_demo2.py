import pytest

# @pytest.mark.skip
# @pytest.mark.xfail
# def test_case3():
#     name="chandradeep"
#     assert name == "radhe"
def test_case3():
    name="chandradeep"
    assert name == "chandradeep"

@pytest.mark.smoke
def test_case4():
    print("pytest training")

