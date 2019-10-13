import pandas as pd
from main import compare, get_frames_from_dir
from pandas.testing import assert_frame_equal
import pytest


@pytest.fixture
def sample_data():
    data1 = pd.read_csv("data/input/companyA.csv", index_col="part")
    data2 = pd.read_csv("data/input/companyB.csv", index_col="part")
    return data1, data2


def test_compare(sample_data):
    output = compare(sample_data[0], sample_data[1])
    expected = pd.read_csv("data/compare.csv", index_col="part")
    assert_frame_equal(expected, output)


def test_get_names_from_dir(sample_data):
    folder = "data/input"
    expected = [("companyA", sample_data[0]), ("companyB", sample_data[1])]
    output = get_frames_from_dir(folder)
    print(output)
    assert list(map(lambda x: x[0], output)) == list(
        map(lambda x: x[0], expected)
    )
    for i in range(len(output)):
        assert_frame_equal(output[i][1], expected[i][1])
