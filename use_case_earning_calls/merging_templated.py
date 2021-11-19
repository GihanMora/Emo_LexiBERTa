

path = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\sentence_level_averaged_templated"
import pandas as pd
import os

files_list = os.listdir(path)
print(files_list)
dfs_list = []
for each_f in files_list:
  if(each_f.endswith(".csv")):
    f_name = os.path.join(path,each_f)
    df = pd.read_csv(f_name)
    dfs_list.append(df)

  # print()
dfg = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\line_out_fixed\results_unprocessed_lnm_transcripts_left.csv")
dfs_list.append(dfg)
dddf = pd.concat(dfs_list, ignore_index=True)
print(len(dddf))
dddf.drop_duplicates(subset=['pdf'], keep='first', inplace=True)
print(len(dddf))

pdfs_list = dddf['pdf'].to_list()
fil = pd.read_csv( r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\filtered_reports\filtered_reports.csv")
filtered_pdf_list = fil['pdf'].tolist()
left = list(set(filtered_pdf_list)-set(pdfs_list))
print(len(left))
print(left)
# print(dddf['predictions'].unique())

dddf.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled/all_transcripts_sentence_level.csv")