"""Program entry point."""
import pandas as pd


def compare(df_1, df_2):
    """Join two dataframes to give a comparison of all prices."""
    df = pd.merge(df_1, df_2, on="part", how="outer")
    return df.sort_values("part")


if __name__ == "__main__":
    a = pd.read_csv("data/companyA.csv")
    b = pd.read_csv("data/companyB.csv")
    print(compare(a, b))
