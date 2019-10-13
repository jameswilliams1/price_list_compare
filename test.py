import pandas as pd
from main import compare
from pandas.testing import assert_frame_equal


def test_compare():
    data1 = pd.read_csv("data/input/companyA.csv")
    data2 = pd.read_csv("data/input/companyB.csv")
    output = compare(data1, data2).reset_index(drop=True)
    expected = pd.read_csv("data/compare.csv")
    assert_frame_equal(expected, output)
