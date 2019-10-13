import pandas as pd
from main import compare, get_frames_from_dir
from pandas.testing import assert_frame_equal
import pytest


@pytest.fixture
def sample_data():
    data1 = pd.read_csv("data/input/companyA.csv", index_col="part")
    data2 = pd.read_csv("data/input/companyB.csv", index_col="part")
    frame_list = [("companyA", data1), ("companyB", data2)]
    return data1, data2, frame_list


def test_compare(sample_data):
    output = compare(sample_data[0], sample_data[1])
    expected = pd.read_csv("data/compare.csv", index_col="part")
    assert_frame_equal(expected, output)


def test_get_names_from_dir(sample_data):
    folder = "data/input"
    output = get_frames_from_dir(folder)
    print(output)
    assert list(map(lambda x: x[0], output)) == list(
        map(lambda x: x[0], sample_data[2])
    )
    for i in range(len(output)):
        assert_frame_equal(output[i][1], sample_data[2][i][1])


def test_merge_list(sample_data):
    pass
