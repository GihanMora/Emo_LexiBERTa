import pandas as pd

df = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\all_transcripts_sentence_level.csv")
print(df.columns)

#ceo and other man presentation
pos_diff_ceo_l=[]
neg_diff_ceo_l=[]

pos_diff_oman_l=[]
neg_diff_oman_l=[]



for i,row in df.iterrows():
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


df['pos_diff_ceo_l'] = pos_diff_ceo_l
df['neg_diff_ceo_l'] = neg_diff_ceo_l
df['pos_diff_oman_l'] = pos_diff_oman_l
df['neg_diff_oman_l'] = neg_diff_oman_l

print(df.columns)

df.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\all_transcripts_sentence_level_with_diff_qna_pres.csv", index=False)