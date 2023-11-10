# -*- coding: utf-8 -*-

import pandas as pd


def main():
    df = pd.read_csv("./resources/calender_sample.csv")
    print(df.head())

if __name__ == "__main__":
    main()
