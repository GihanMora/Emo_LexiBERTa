import pandas as pd

df = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\all_transcripts_sentence_level.csv")
print(df.columns)

#ceo and other man presentation
pres_pos_diff_ceo_oman_l=[]
pres_neg_diff_ceo_oman_l=[]
pres_lit_diff_ceo_oman_l=[]
pres_unc_diff_ceo_oman_l=[]
pres_st_diff_ceo_oman_l=[]
pres_wk_diff_ceo_oman_l=[]

qa_pos_diff_ceo_oman_l=[]
qa_neg_diff_ceo_oman_l=[]
qa_lit_diff_ceo_oman_l=[]
qa_unc_diff_ceo_oman_l=[]
qa_st_diff_ceo_oman_l=[]
qa_wk_diff_ceo_oman_l=[]

qa_pos_diff_ceo_anl_l=[]
qa_neg_diff_ceo_anl_l=[]
qa_lit_diff_ceo_anl_l=[]
qa_unc_diff_ceo_anl_l=[]
qa_st_diff_ceo_anl_l=[]
qa_wk_diff_ceo_anl_l=[]


for i,row in df.iterrows():
    pres_pos_diff_ceo_oman = row['CEO_Presentation_Positive'] - row['OtherManagers_Presentation_Positive']
    pres_pos_diff_ceo_oman_l.append(pres_pos_diff_ceo_oman)
    pres_neg_diff_ceo_oman = row['CEO_Presentation_Negative'] - row['OtherManagers_Presentation_Negative']
    pres_neg_diff_ceo_oman_l.append(pres_neg_diff_ceo_oman)
    pres_lit_diff_ceo_oman = row['CEO_Presentation_Litigious'] - row['OtherManagers_Presentation_Litigious']
    pres_lit_diff_ceo_oman_l.append(pres_lit_diff_ceo_oman)
    pres_unc_diff_ceo_oman = row['CEO_Presentation_Uncertainty'] - row['OtherManagers_Presentation_Uncertainty']
    pres_unc_diff_ceo_oman_l.append(pres_unc_diff_ceo_oman)
    pres_st_diff_ceo_oman = row['CEO_Presentation_MStrong'] - row['OtherManagers_Presentation_MStrong']
    pres_st_diff_ceo_oman_l.append(pres_st_diff_ceo_oman)
    pres_wk_diff_ceo_oman = row['CEO_Presentation_MWeak'] - row['OtherManagers_Presentation_MWeak']
    pres_wk_diff_ceo_oman_l.append(pres_wk_diff_ceo_oman)


    qa_pos_diff_ceo_oman = row['CEO_Q&A_Positive'] - row['OtherManagers_Q&A_Positive']
    qa_pos_diff_ceo_oman_l.append(qa_pos_diff_ceo_oman)
    qa_neg_diff_ceo_oman = row['CEO_Q&A_Negative'] - row['OtherManagers_Q&A_Negative']
    qa_neg_diff_ceo_oman_l.append(qa_neg_diff_ceo_oman)
    qa_lit_diff_ceo_oman = row['CEO_Q&A_Litigious'] - row['OtherManagers_Q&A_Litigious']
    qa_lit_diff_ceo_oman_l.append(qa_lit_diff_ceo_oman)
    qa_unc_diff_ceo_oman = row['CEO_Q&A_Uncertainty'] - row['OtherManagers_Q&A_Uncertainty']
    qa_unc_diff_ceo_oman_l.append(qa_unc_diff_ceo_oman)
    qa_st_diff_ceo_oman = row['CEO_Q&A_MStrong'] - row['OtherManagers_Q&A_MStrong']
    qa_st_diff_ceo_oman_l.append(qa_st_diff_ceo_oman)
    qa_wk_diff_ceo_oman = row['CEO_Q&A_MWeak'] - row['OtherManagers_Q&A_MWeak']
    qa_wk_diff_ceo_oman_l.append(qa_wk_diff_ceo_oman)

    qa_pos_diff_ceo_anl = row['CEO_Q&A_Positive'] - row['AllAnalysts_Q&A_Positive']
    qa_pos_diff_ceo_anl_l.append(qa_pos_diff_ceo_anl)
    qa_neg_diff_ceo_anl = row['CEO_Q&A_Negative'] - row['AllAnalysts_Q&A_Negative']
    qa_neg_diff_ceo_anl_l.append(qa_neg_diff_ceo_anl)
    qa_lit_diff_ceo_anl = row['CEO_Q&A_Litigious'] - row['AllAnalysts_Q&A_Litigious']
    qa_lit_diff_ceo_anl_l.append(qa_lit_diff_ceo_anl)
    qa_unc_diff_ceo_anl = row['CEO_Q&A_Uncertainty'] - row['AllAnalysts_Q&A_Uncertainty']
    qa_unc_diff_ceo_anl_l.append(qa_unc_diff_ceo_anl)
    qa_st_diff_ceo_anl = row['CEO_Q&A_MStrong'] - row['AllAnalysts_Q&A_MStrong']
    qa_st_diff_ceo_anl_l.append(qa_st_diff_ceo_anl)
    qa_wk_diff_ceo_anl = row['CEO_Q&A_MWeak'] - row['AllAnalysts_Q&A_MWeak']
    qa_wk_diff_ceo_anl_l.append(qa_wk_diff_ceo_anl)


df['pres_pos_diff_ceo_oman_l'] = pres_pos_diff_ceo_oman_l
df['pres_neg_diff_ceo_oman_l'] = pres_neg_diff_ceo_oman_l
df['pres_lit_diff_ceo_oman_l'] = pres_lit_diff_ceo_oman_l
df['pres_unc_diff_ceo_oman_l'] = pres_unc_diff_ceo_oman_l
df['pres_st_diff_ceo_oman_l'] = pres_st_diff_ceo_oman_l
df['pres_wk_diff_ceo_oman_l'] = pres_wk_diff_ceo_oman_l

df['qa_pos_diff_ceo_oman_l'] = qa_pos_diff_ceo_oman_l
df['qa_neg_diff_ceo_oman_l'] = qa_neg_diff_ceo_oman_l
df['qa_lit_diff_ceo_oman_l'] = qa_lit_diff_ceo_oman_l
df['qa_unc_diff_ceo_oman_l'] = qa_unc_diff_ceo_oman_l
df['qa_st_diff_ceo_oman_l'] = qa_st_diff_ceo_oman_l
df['qa_wk_diff_ceo_oman_l'] = qa_wk_diff_ceo_oman_l

df['qa_pos_diff_ceo_anl_l'] = qa_pos_diff_ceo_anl_l
df['qa_neg_diff_ceo_anl_l'] = qa_neg_diff_ceo_anl_l
df['qa_lit_diff_ceo_anl_l'] = qa_lit_diff_ceo_anl_l
df['qa_unc_diff_ceo_anl_l'] = qa_unc_diff_ceo_anl_l
df['qa_st_diff_ceo_anl_l'] = qa_st_diff_ceo_anl_l
df['qa_wk_diff_ceo_anl_l'] = qa_wk_diff_ceo_anl_l

print(df.columns)

df.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\all_transcripts_sentence_level_with_diff.csv", index=False)