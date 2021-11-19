import os
import json
import numpy as np
import pandas as pd
import scipy.stats as st
from tqdm import tqdm
import random
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--csv_path', type=str, default="metadata_sim-mos_bilingual.csv",
                        help='The CSV file path')
    args = parser.parse_args()

    df = pd.read_csv(args.csv_path, sep=',', names=["gen", "ref"])

    exp = "Exp.6"
    dict_exps = {}
    for index, line in df.iterrows():
        gen_path = line["gen"]
        ref_path = line["ref"]
        
        if exp not in gen_path:
            continue
        speaker_name = os.path.basename(ref_path).split("_")[0]
        splits = ref_path.split("/")
        exp_name = splits[1] + "_" + splits[2]
        key = exp_name + "_" + speaker_name
        if key not in dict_exps:
            dict_exps[key] = ["0__"+ref_path, gen_path]
        else:
            dict_exps[key].append(gen_path)
            

# print(dict_exps)

dict_exps = dict(sorted(dict_exps.items()))
for key in dict_exps:
    print(key)
    list_ = dict_exps[key]
    # list_.sort()
    print("  <tr><td>{}</td>".format(key.split("_")[-1]))
    for x in list_:
          
        print('    <td><audio controls style="width: 110px;" src="{}"></audio></td>'.format(os.path.join("audios_demo", x.replace("0__", "")).replace(" ", "")))

    print("  </tr>")



