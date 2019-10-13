"""Program entry point."""
import pandas as pd
import glob
import os


def compare(df_1, df_2):
    """Join two dataframes to give a comparison of all prices."""
    df = pd.merge(df_1, df_2, on="part", how="outer")
    return df.sort_values("part")


def get_frames_from_dir(path="data/input"):
    """Return a dictionary of name: dataframe from a directory."""
    all_files = glob.glob(os.path.join(path, "*.csv"))
    data_dict = {
        os.path.basename(filename).split(".")[0]: pd.read_csv(
            filename, index_col="part"
        )
        for filename in all_files
    }
    return data_dict


if __name__ == "__main__":
    a = pd.read_csv("data/input/companyA.csv", index_col="part")
    b = pd.read_csv("data/input/companyB.csv", index_col="part")
    # print(compare(a, b))
