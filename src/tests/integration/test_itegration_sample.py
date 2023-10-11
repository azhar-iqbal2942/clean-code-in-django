import pytest

pytestmark = pytest.mark.integration


def test_will_invoke_with_integration_flag():
    print("Integration test invoked...!!")
    assert True
