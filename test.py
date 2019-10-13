import pandas as pd
from main import *
from pandas.testing import assert_frame_equal
import pytest


@pytest.fixture
def sample_data():
    data1 = pd.read_csv("data/input/companyA.csv", index_col="part")
    data2 = pd.read_csv("data/input/companyB.csv", index_col="part")
    data3 = pd.read_csv("data/input/companyC.csv", index_col="part")
    frame_list_2 = [("companyA", data1), ("companyB", data2)]
    frame_list_3 = frame_list_2.copy()
    frame_list_3.append(("companyC", data3))
    compare = pd.read_csv("data/compare.csv", index_col="part")
    return data1, data2, frame_list_2, frame_list_3, compare


def test_compare(sample_data):
    output = compare(sample_data[0], sample_data[1])
    expected = sample_data[4]
    assert_frame_equal(expected, output)


def test_get_names_from_dir(sample_data):
    folder = "data/input"
    output = get_frames_from_dir(folder)
    print(output)
    assert list(map(lambda x: x[0], output)) == list(
        map(lambda x: x[0], sample_data[3])
    )
    for i in range(len(output)):
        assert_frame_equal(output[i][1], sample_data[3][i][1])


def test_merge_list(sample_data):
    frame_list = sample_data[2]
    output = merge_frame_list(frame_list)
    expected = sample_data[4]
    assert_frame_equal(output, expected)


def test_main(sample_data):
    main("")  # Look in current dir
    expected = pd.read_csv("data/final.csv", index_col="part")
    output = pd.read_csv("output.csv", index_col="part")  # file created
    assert_frame_equal(output, expected)
