"""Program entry point."""
import pandas as pd


def compare(df_1, df_2):
    return pd.merge(pd.merge(df_1, df_2))
