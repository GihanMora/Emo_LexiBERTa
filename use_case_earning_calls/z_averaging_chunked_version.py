import ast

import pandas as pd

df = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\chunked\all_transcripts_19_20.csv")
fil = pd.read_csv( r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\filtered_reports\filtered_reports.csv")
filtered_pdf_list = fil['pdf'].tolist()
print(len(df))

filterd_df= df[df.pdf.isin(filtered_pdf_list)]

print(len(filterd_df))
filterd_df.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\chunked\non_scaled.csv")

# print(filterd_df.columns)
# cols_set = [ 'Total_Presentation_Positive',
#        'Total_Presentation_Negative', 'Total_Presentation_Litigious',
#        'Total_Presentation_Uncertainty', 'Total_Presentation_MStrong',
#        'Total_Presentation_MWeak', 'CEO_Presentation_Positive',
#        'CEO_Presentation_Negative', 'CEO_Presentation_Litigious',
#        'CEO_Presentation_Uncertainty', 'CEO_Presentation_MStrong',
#        'CEO_Presentation_MWeak', 'OtherManagers_Presentation_Positive',
#        'OtherManagers_Presentation_Negative',
#        'OtherManagers_Presentation_Litigious',
#        'OtherManagers_Presentation_Uncertainty',
#        'OtherManagers_Presentation_MStrong',
#        'OtherManagers_Presentation_MWeak', 'Total_Q&A_Positive',
#        'Total_Q&A_Negative', 'Total_Q&A_Litigious', 'Total_Q&A_Uncertainty',
#        'Total_Q&A_MStrong', 'Total_Q&A_MWeak', 'CEO_Q&A_Positive',
#        'CEO_Q&A_Negative', 'CEO_Q&A_Litigious', 'CEO_Q&A_Uncertainty',
#        'CEO_Q&A_MStrong', 'CEO_Q&A_MWeak', 'OtherManagers_Q&A_Positive',
#        'OtherManagers_Q&A_Negative', 'OtherManagers_Q&A_Litigious',
#        'OtherManagers_Q&A_Uncertainty', 'OtherManagers_Q&A_MStrong',
#        'OtherManagers_Q&A_MWeak', 'AllAnalysts_Q&A_Positive',
#        'AllAnalysts_Q&A_Negative', 'AllAnalysts_Q&A_Litigious',
#        'AllAnalysts_Q&A_Uncertainty', 'AllAnalysts_Q&A_MStrong',
#        'AllAnalysts_Q&A_MWeak']
#
#
# out_lists = {}
# for ll in cols_set:
#     out_lists[ll] = []
#
# for i,row in filterd_df.iterrows():
#    for k in [0,6,12,18,24,30,36]:
#        col_subs = cols_set[k:k+6]
#        s_sum = 0
#        for s_c in col_subs:
#            s_sum = s_sum +row[s_c]
#        if((s_sum!=s_sum) or (s_sum ==0)):
#            for s_v in col_subs:
#                out_lists[s_v].append(row[s_v])
#        else:
#            divider = round(s_sum)
#            for s_v in col_subs:
#                out_lists[s_v].append(round((row[s_v]/divider),3))
#
# print(out_lists)
#
# for kk in out_lists.keys():
#     filterd_df[kk] = out_lists[kk]
#
# filterd_df.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\chunked\\filtered_reports_scaled.csv", index=False)
#
