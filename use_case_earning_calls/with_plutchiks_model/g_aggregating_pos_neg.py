import pandas as pd
import os
root_dir = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_templated"
f_names_list = os.listdir(root_dir)



def aggregate_plutchiks(df,feature):
    pos = []
    neg = []
    print(df.columns)
    for i,row in df.iterrows():
        pos_sum = row[feature+'_joy']+row[feature+'_trust']+row[feature+'_anticipation']+row[feature+'_surprise']
        pos_sum = round(pos_sum,2)
        print(pos_sum)
        pos.append(pos_sum)
        neg_sum = row[feature + '_sad'] + row[feature + '_anger'] + row[feature + '_disgust'] + row[
            feature + '_fear']
        neg_sum = round(neg_sum, 2)
        print(neg_sum)
        neg.append(neg_sum)
        print('***')
    return [pos,neg]




for k in f_names_list:
    df = pd.read_csv(os.path.join(root_dir,k))
    print(os.path.join(root_dir,k))
    features = ['Total_Presentation','CEO_Presentation','OtherManagers_Presentation','Total_Q&A','CEO_Q&A','OtherManagers_Q&A','AllAnalysts_Q&A']
    for f in features:
        tp = aggregate_plutchiks(df,f)
        df[f+'_Positive'] = tp[0]
        df[f + '_Negative'] = tp[1]
    df.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\with_plutchiks_templated_pos_neg_agg\\"+k, index=False)



# dfg1 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_templated\results_unprocessed_lnm_transcripts_left_0_20.csv")
# dfs_list.append(dfg1)
# dfg2 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_templated\results_unprocessed_lnm_transcripts_left_20_40.csv")
# dfs_list.append(dfg2)
# dfg3 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_templated\results_unprocessed_lnm_transcripts_left_40_60.csv")
# dfs_list.append(dfg3)
# dfg4 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_templated\results_unprocessed_lnm_transcripts_left_60_80.csv")
# dfs_list.append(dfg4)
# dfg5 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_templated\results_unprocessed_lnm_transcripts_left_80_100.csv")
# dfs_list.append(dfg5)