import pytest

pytestmark = pytest.mark.smoke

def test_case01(setup_smoke):
    print('\n')
    print(setup_smoke[1:3])
    assert setup_smoke[0] == 'New York'
    assert setup_smoke[::2] == ['New York','Berlin','Singapor','Pekin']