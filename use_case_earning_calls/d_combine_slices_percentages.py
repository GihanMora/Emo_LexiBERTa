import pandas as pd
import os
root_dir = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\sentence_level_with_percentages_templated"
f_names_list = os.listdir(root_dir)
dfs_list = []
for k in f_names_list:
    dfs_list.append(pd.read_csv(os.path.join(root_dir,k)))
    print(os.path.join(root_dir,k))

dfg = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\sentence_level_with_percentages_templated\results_unprocessed_lnm_transcripts_left.csv")
dfs_list.append(dfg)
dddf = pd.concat(dfs_list, ignore_index=True)
dddf.drop_duplicates(subset=['pdf'], keep='first', inplace=True)
dddf.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\all_transcripts_sentence_level_percentages.csv", index=False)

