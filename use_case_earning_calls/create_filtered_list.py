import pandas as pd
from dateutil import parser
# df = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\filtered_reports\List of firms and dates used in the sample.csv", parse_dates=True)
# df1 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\filtered_reports\all_transcripts_19_20.csv", parse_dates=True)
# print(df.columns)
# print(df1.columns)
#
# # df =df.style.format({"event_date": lambda t: t.strftime("%d/%m/%Y")})
# # df1 = df1.style.format({"event_date": lambda t: t.strftime("%d/%m/%Y")})
# # df['event_date'] = df['event_date'].dt.strftime('%d/%m/%Y')
# # df1['event_date'] = df1['event_date'].dt.strftime('%d/%m/%Y')
# df1['event_date']=[parser.parse(i) for i in df1['event_date'].tolist()]
# df['event_date']=[parser.parse(i) for i in df['event_date'].tolist()]
# df['event_date'] = df['event_date'].dt.strftime('%d/%m/%Y')
# df1['event_date'] = df1['event_date'].dt.strftime('%d/%m/%Y')
# print(df['event_date'])
# print(df1['event_date'])
#
# df.to_csv(r'E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\filtered_reports\\abbr.csv')
# df1.to_csv(r'E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\filtered_reports\\detl.csv')
# df1['company_ticker'] =[i.split('.')[0] for i in  df1['company_ticker']]
# combined_df = pd.merge(left=df, right=df1, how='left',
#                                    left_on=['company_ticker', 'event_date'],
#                                    right_on=['company_ticker', 'event_date'])
# combined_df = combined_df.drop_duplicates(subset=['pdf'])
# combined_df.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\filtered_reports\\filtered_reports.csv")

abb = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\filtered_reports\abbr.csv")
fil = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\filtered_reports\filtered_reports.csv")
print(len(fil['pdf'].tolist()))
print(fil['pdf'].tolist())
# abbs = []
# fils = []
# for i,row in abb.iterrows():
#     abbs.append(row['event_date']+'_'+row['company_ticker'])
#
# for i,row in fil.iterrows():
#     fils.append(row['event_date']+'_'+row['company_ticker'])
#
# print(len(abbs))
# print(len(fils))
# print(list(set(fils)-set(abbs)))
#
# a = fils
# import collections
# print([item for item, count in collections.Counter(a).items() if count > 1])