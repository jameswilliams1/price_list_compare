"""Program entry point."""
import pandas as pd
import glob
import os


def compare(df_1, df_2):
    """Join two dataframes to give a comparison of all prices."""
    df = pd.merge(df_1, df_2, on="part", how="outer")
    return df.sort_values("part")


def get_frames_from_dir(path="data/input"):
    """Return a list of (name, dataframe) tuples from a directory."""
    all_files = glob.glob(os.path.join(path, "*.csv"))
    data_list = [
        (
            os.path.basename(filename).split(".")[0],
            pd.read_csv(filename, index_col="part"),
        )
        for filename in all_files
    ]
    return sorted(data_list, key=lambda tup: tup[0])


def merge_frame_list(frame_list):
    """Merge a list of (name: frame) tuples using compare.

    Returns final processed    dataframe.
    """

    pass


if __name__ == "__main__":
    pass
