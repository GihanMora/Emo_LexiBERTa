import math
import pandas as pd


# df = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\sentence_level_averaged\results_unprocessed_lnm_transcripts_2010 Jan to Jun_0_300.csv")
df = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\sentence_level_averaged\results_unprocessed_lnm_transcripts_2017 Jul to Dec_0_300.csv")

for i,row in df.iterrows():
    print(row['pdf'],row['presentation_all_e_p'])
    # if(row['presentation_all_e_p']!=row['presentation_all_e_p']):
    #     print(row['presentation_all_e_p'])