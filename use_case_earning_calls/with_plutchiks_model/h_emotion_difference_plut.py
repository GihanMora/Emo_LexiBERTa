import pandas as pd

df = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\with_plutchiks_model\all_transcripts_plutchiks_pos_neg_agg.csv")
print(df.columns)

#ceo and other man presentation
pres_pos_diff_ceo_oman_l=[]
pres_neg_diff_ceo_oman_l=[]
qa_pos_diff_ceo_oman_l=[]
qa_neg_diff_ceo_oman_l=[]

pos_diff_ceo_l=[]
neg_diff_ceo_l=[]
pos_diff_oman_l=[]
neg_diff_oman_l=[]



for i,row in df.iterrows():
    pres_pos_diff_ceo_oman = row['CEO_Presentation_Positive'] - row['OtherManagers_Presentation_Positive']
    pres_pos_diff_ceo_oman_l.append(pres_pos_diff_ceo_oman)
    pres_neg_diff_ceo_oman = row['CEO_Presentation_Negative'] - row['OtherManagers_Presentation_Negative']
    pres_neg_diff_ceo_oman_l.append(pres_neg_diff_ceo_oman)
    qa_pos_diff_ceo_oman = row['CEO_Q&A_Positive'] - row['OtherManagers_Q&A_Positive']
    qa_pos_diff_ceo_oman_l.append(qa_pos_diff_ceo_oman)
    qa_neg_diff_ceo_oman = row['CEO_Q&A_Negative'] - row['OtherManagers_Q&A_Negative']
    qa_neg_diff_ceo_oman_l.append(qa_neg_diff_ceo_oman)


    try:
        pos_diff_ceo = ((row['CEO_Q&A_Positive'] - row['CEO_Presentation_Positive'])/row['CEO_Presentation_Positive'])*100
        pos_diff_ceo_l.append(round(pos_diff_ceo,2))
    except ZeroDivisionError:
        pos_diff_ceo_l.append(0)
    try:
        neg_diff_ceo = ((row['CEO_Q&A_Negative'] - row['CEO_Presentation_Negative'])/row['CEO_Presentation_Negative'])*100
        neg_diff_ceo_l.append(round(neg_diff_ceo,2))
    except ZeroDivisionError:
        neg_diff_ceo_l.append(0)

    try:
        pos_diff_oman =  ((row['OtherManagers_Q&A_Positive'] - row['OtherManagers_Presentation_Positive'])/row['OtherManagers_Presentation_Positive'])*100
        pos_diff_oman_l.append(round(pos_diff_oman,2))
    except ZeroDivisionError:
        pos_diff_oman_l.append(0)
    try:
        neg_diff_oman =  ((row['OtherManagers_Q&A_Negative'] - row['OtherManagers_Presentation_Negative'])/row['OtherManagers_Presentation_Negative'])*100
        neg_diff_oman_l.append(round(neg_diff_oman,2))
    except ZeroDivisionError:
        neg_diff_oman_l.append(0)

out_df = pd.DataFrame()
out_df['pdf'] = df['pdf']
out_df['company_ticker'] = df['company_ticker']
out_df['year'] = df['year']
out_df['quarter'] = df['quarter']
out_df['event_date'] = df['event_date']
out_df['Plutchik Total_Presentation_Positive'] = df['Total_Presentation_Positive']
out_df['Plutchik Total_Presentation_Negative'] = df['Total_Presentation_Negative']
out_df['Plutchik Total_Q&A_Positive'] = df['Total_Q&A_Positive']
out_df['Plutchik Total_Q&A_Negative'] = df['Total_Q&A_Negative']
out_df['Plutchik CEO positive emotion presentation'] = df['CEO_Presentation_Positive']
out_df['Plutchik CEO negative emotion presentation'] = df['CEO_Presentation_Negative']
out_df['Plutchik CEO positive emotion Q&A'] = df['CEO_Q&A_Positive']
out_df['Plutchik CEO negative emotion Q&A'] = df['CEO_Q&A_Negative']
out_df['Plutchik Other managers positive emotion presentation'] = df['OtherManagers_Presentation_Positive']
out_df['Plutchik Other managers negative emotion presentation'] = df['OtherManagers_Presentation_Negative']
out_df['Plutchik Other managers positive emotion Q&A'] = df['OtherManagers_Q&A_Positive']
out_df['Plutchik Other managers negative emotion Q&A'] = df['OtherManagers_Q&A_Negative']
out_df['Plutchik All analysts positive emotion Q&A'] = df['AllAnalysts_Q&A_Positive']
out_df['Plutchik All analysts negative emotion Q&A'] = df['AllAnalysts_Q&A_Negative']
out_df['Plutchik Positive emotion variation Presentation'] = pres_pos_diff_ceo_oman_l
out_df['Plutchik Negative emotion variation Presentation'] = pres_neg_diff_ceo_oman_l
out_df['Plutchik Positive emotion variation Q&A'] = qa_pos_diff_ceo_oman_l
out_df['Plutchik Negative emotion variation Q&A'] = qa_neg_diff_ceo_oman_l
out_df['Plutchik CEO positive emotion variation'] = pos_diff_ceo_l
out_df['Plutchik CEO negative emotion variation'] = neg_diff_ceo_l
out_df['Plutchik Other managers positive emotion variation'] = pos_diff_oman_l
out_df['Plutchik Other managers negative emotion variation'] = neg_diff_oman_l

print(df.columns)

out_df.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\with_plutchiks_model\all_transcripts_with_plutchik_work.csv", index=False)