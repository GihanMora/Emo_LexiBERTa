import pandas as pd
import os
root_dir = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_templated"
f_names_list = os.listdir(root_dir)
dfs_list = []
for k in f_names_list:
    dfs_list.append(pd.read_csv(os.path.join(root_dir,k)))
    print(os.path.join(root_dir,k))

dfg1 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_templated\results_unprocessed_lnm_transcripts_left_0_20.csv")
dfs_list.append(dfg1)
dfg2 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_templated\results_unprocessed_lnm_transcripts_left_20_40.csv")
dfs_list.append(dfg2)
dfg3 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_templated\results_unprocessed_lnm_transcripts_left_40_60.csv")
dfs_list.append(dfg3)
dfg4 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_templated\results_unprocessed_lnm_transcripts_left_60_80.csv")
dfs_list.append(dfg4)
dfg5 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_templated\results_unprocessed_lnm_transcripts_left_80_100.csv")
dfs_list.append(dfg5)
dddf = pd.concat(dfs_list, ignore_index=True)
dddf.drop_duplicates(subset=['pdf'], keep='first', inplace=True)
dddf.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\with_plutchiks_model\all_transcripts_plutchiks_averaged.csv", index=False)

