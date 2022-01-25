import pandas as pd

df1 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\all_transcripts_sentence_level_with_diff.csv",
                  usecols = ['pdf', 'company_ticker', 'year', 'quarter', 'event_date','pres_pos_diff_ceo_oman_l',
       'pres_neg_diff_ceo_oman_l', 'qa_pos_diff_ceo_oman_l',
       'qa_neg_diff_ceo_oman_l', ])
df2 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\all_transcripts_sentence_level_with_diff_qna_pres.csv",usecols = ['pdf', 'company_ticker', 'year', 'quarter', 'event_date',
       'pos_diff_ceo_l', 'neg_diff_ceo_l',
       'pos_diff_oman_l', 'neg_diff_oman_l'])

df3 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\with_plutchiks_model\all_transcripts_with_plutchik_work.csv")

dff = pd.merge(df1,df2,left_on=['pdf', 'company_ticker', 'year', 'quarter', 'event_date'],right_on=['pdf', 'company_ticker', 'year', 'quarter', 'event_date'])
dfz = pd.merge(dff,df3,left_on=['pdf', 'company_ticker', 'year', 'quarter', 'event_date'],right_on=['pdf', 'company_ticker', 'year', 'quarter', 'event_date'])
dfz = dfz.rename(columns=
                 {
                  'pos_diff_ceo_l': 'CEO positive emotion variation',
                  'pos_diff_oman_l': 'Other managers (OM) positive emotion variation',
                  'neg_diff_ceo_l':'CEO negative emotion variation',
'neg_diff_oman_l':'Other managers (OM) negative emotion variation',
'pres_pos_diff_ceo_oman_l':'Positive emotion variation Presentation',
'qa_pos_diff_ceo_oman_l':'Positive emotion variation Q&A',
'pres_neg_diff_ceo_oman_l':'Negative emotion variation Presentation',
'qa_neg_diff_ceo_oman_l':'Negative emotion variation Q&A',

                 })
print(df1.columns)
print(df2.columns)
print(dfz.columns)

dfz = dfz[['pdf', 'company_ticker', 'year', 'quarter', 'event_date','CEO positive emotion variation','Other managers (OM) positive emotion variation',
           'CEO negative emotion variation','Other managers (OM) negative emotion variation', 'Positive emotion variation Presentation','Positive emotion variation Q&A',
           'Negative emotion variation Presentation','Negative emotion variation Q&A','Plutchik Total_Presentation_Positive',
       'Plutchik Total_Presentation_Negative', 'Plutchik Total_Q&A_Positive',
       'Plutchik Total_Q&A_Negative',
       'Plutchik CEO positive emotion presentation',
       'Plutchik CEO negative emotion presentation',
       'Plutchik CEO positive emotion Q&A',
       'Plutchik CEO negative emotion Q&A',
       'Plutchik Other managers positive emotion presentation',
       'Plutchik Other managers negative emotion presentation',
       'Plutchik Other managers positive emotion Q&A',
       'Plutchik Other managers negative emotion Q&A',
       'Plutchik All analysts positive emotion Q&A',
       'Plutchik All analysts negative emotion Q&A','Plutchik CEO positive emotion variation','Plutchik Other managers positive emotion variation', 'Plutchik CEO negative emotion variation',
           'Plutchik Other managers negative emotion variation',
           'Plutchik Positive emotion variation Presentation','Plutchik Positive emotion variation Q&A',
           'Plutchik Negative emotion variation Presentation','Plutchik Negative emotion variation Q&A']]

dfz.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\with_plutchiks_model\all_transcripts_plutchiks_final_template.csv", index=False)