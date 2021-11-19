import pandas as pd

path1 = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\line_out_fixed\results_unprocessed_lnm_transcripts_left_0_20.csv"
path2 = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\line_out_fixed\results_unprocessed_lnm_transcripts_left_20_40.csv"
path3 = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\line_out_fixed\results_unprocessed_lnm_transcripts_left_40_60.csv"
path4 = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\line_out_fixed\results_unprocessed_lnm_transcripts_left_60_90.csv"


df1 = pd.read_csv(path1)
df2 = pd.read_csv(path2)
df3 = pd.read_csv(path3)
df4 = pd.read_csv(path4)

dfs_list = [df1, df2, df3, df4]

dddf = pd.concat(dfs_list, ignore_index=True)

dddf.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\line_out_fixed\results_unprocessed_lnm_transcripts_left.csv", index=False)

