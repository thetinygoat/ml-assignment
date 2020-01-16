import pandas as pd
import numpy as np
import argparse
import os
import csv

parser = argparse.ArgumentParser()
parser.add_argument("--window", help="specify window size", type=int)
parser.add_argument("input", help="specify input file")
args = parser.parse_args()
if not args.window:
    print("required argument window size!")
    os._exit(-1)

data = pd.read_csv(args.input)
data.drop(["No", "year", "month", "day", "hour",], axis=1, inplace=True)
anslist = []
window_size = args.window
for i in range(window_size):
    lst = data.shift(-i).iloc[0].values.tolist()
    anslist.append(lst)
pred = data.shift(-window_size).iloc[0]["TEMP"]

fields = ["Time Series", "Next Hour Predicted_Temprature"]

with open("output.csv", "w+") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerow({"Time Series": anslist, "Next Hour Predicted_Temprature": pred})

