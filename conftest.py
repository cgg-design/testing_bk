import pytest


@pytest.fixture()
def setup_smoke():
    print("\n Smoke test has started! \n")
    city = ["New York", "London", "Berlin", "Paris", "Singapor", "Riyadh", "Pekin"]
    return city