import pandas as pd
from main import compare
from pandas.testing import assert_frame_equal
import pytest


@pytest.fixture
def sample_data():
    data1 = pd.read_csv("data/input/companyA.csv")
    data2 = pd.read_csv("data/input/companyB.csv")
    return data1, data2


def test_compare(sample_data):
    output = compare(sample_data[0], sample_data[1]).reset_index(drop=True)
    expected = pd.read_csv("data/compare.csv")
    assert_frame_equal(expected, output)


def test_get_names_from_dir():
    folder = "data/input"
    expected = {"CompanyA": None, "CompanyB": None}
