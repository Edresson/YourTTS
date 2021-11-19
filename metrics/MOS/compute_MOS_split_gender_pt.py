import os
import json
import numpy as np
import pandas as pd
import scipy.stats as st
from tqdm import tqdm
import random
import argparse


PT_M_speakers = ["12287", "4367", "12710", "5677", "9351"]
PT_F_speakers = ["3050", "7925", "12249", "11995", "13069"]

def compute_MOS(csv_file="Sim-MOS.csv", confience_interval=0.95):
    # load the CSV
    df = pd.read_csv(csv_file, sep=',')

    # compute the mean and the confidence intervals using scipy
    def compute_confidence_intervals(mos_exps, exp):
        for key in sorted(mos_exps.keys()):
            values = mos_exps[key]
            mos = np.array(values).mean()
            low_b, high_b = st.t.interval(confience_interval, len(values)-1, loc=mos, scale=st.sem(values))
            confience_interval_more_less = mos-low_b
            # print the result with 2 decimal cases
            print(key, "MOS:", float(format(mos, '.2f')), "$\pm$",float(format(confience_interval_more_less, '.2f')))


    # group the scores by experiment
    mos_exps = {}
    for index, line in df.iterrows():

        line["audio_path"] = line["audio_path"].replace("/model", "_model")
        audio_path = line["audio_path"]
        score = line["score"]
        
        exp_name = audio_path.split("/")[0]
        
        data = [audio_path, score]
        
        if exp_name not in mos_exps.keys():
            mos_exps[exp_name] = [data]
        else:
            mos_exps[exp_name].append(data)

    # for in all experiments
    for exp in sorted(mos_exps.keys()):
        mos_dict = {}
        # for in all scores to adjust the exp path
        for item in mos_exps[exp]:
            key_name_all_exp_VC = None
            path_name = item[0]
            score = item[1]
            splits = path_name.split(",")[0].split("/")

            # default exp+dataset
            key_name = splits[0]+"_"+splits[1]

            # show separated male and female results in Portuguese            
            if "Portuguese_MLS_SECS" in path_name:
                speaker_name = splits[-1].split("_")[0]
                gender = None
                if speaker_name in PT_M_speakers:
                    gender = "Male"
                elif speaker_name in PT_F_speakers:
                    gender = "Female"
                else:
                    print("Invalid Speaker name: ", speaker_name)
                    exit()

                key_name_gender = splits[0]+"_"+splits[1]+"_"+gender
                if key_name_gender not in mos_dict.keys():
                    mos_dict[key_name_gender] = [score]
                else:
                    mos_dict[key_name_gender] += [score]
            else:
                key_name_gender = None


            # GT speaker adaptation by speaker name
            if "GT" in exp  and "Speaker_Adaptation" in path_name:
                key_name = splits[0]+"_"+splits[1] + "_" + splits[2]
            # exp 5
            if "Exp.5" in exp:
                key_name = splits[0]+"_"+splits[1] + "_" +  splits[2] +  "_" + splits[3]
                if "Zero-shot" in path_name:
                    key_name = splits[0]+"_"+splits[1] + "_" +  splits[2] +  "_" + splits[3].split(".wav_")[0]
            # exp 6
            if "Exp.6" in exp:
                key_name = splits[0]+"_"+splits[1] + "_" + splits[2]
                # In exp 6 (voice conversion exp) we need the MOS for all the part not just for m-m, m-f, f-f, m-f individually
                key_name_all_exp_VC = splits[0]+"_"+splits[1]
                if key_name_all_exp_VC not in mos_dict.keys():
                    mos_dict[key_name_all_exp_VC] = [score]
                else:
                    mos_dict[key_name_all_exp_VC] += [score]

            if key_name not in mos_dict.keys():
                mos_dict[key_name] = [score]
            else:
                mos_dict[key_name] += [score]

            
        compute_confidence_intervals(mos_dict, exp)

if __name__ == "__main__":
    """
    
    Usage:
    For Similarity  MOS: 
        python3 compute_similarity_MOS.py --csv_path EN/Sim-MOS.csv 
    For Naturalness MOS:
        python3 compute_similarity_MOS.py --csv_path EN/naturalness-MOS.csv

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--csv_path', type=str, default="PT/Sim-MOS.csv",
                        help='The CSV file path')
    parser.add_argument('-i', '--confidence_level', type=float, default=0.95,
                        help='set the confidence level for the confience interval calculation. Default: 0.95')
    args = parser.parse_args()

    compute_MOS(args.csv_path, args.confidence_level)