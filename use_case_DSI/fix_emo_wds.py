import pandas as pd
import ast
# df = pd.read_csv(r"E:\Projects\EmoLexiBerta_Gihan\Emo_LexiBERTa\use_case_DSI\processed_trump_biden_emo_all.csv")
df = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_DSI\processed_trump_biden_emo_all_eight.csv")

print(df.columns)
max_emo = []
max_emo_stre = []


for i,row in df.iterrows():
    # emo_prf = ast.literal_eval(row['emo_profiles'])
    emo_prf = ast.literal_eval(row['eight_emo_profiles'])
    print(emo_prf)
    emo_prf = {k: v for k, v in sorted(emo_prf.items(), key=lambda item: item[1])}
    emo_list = list(emo_prf.keys())
    print(emo_list)

    mx_em = emo_list[-1]
    max_emo.append(emo_list[-1])
    max_emo_stre.append(emo_prf[mx_em])

#
df['max_emo'] = max_emo
df['max_emo_str'] = max_emo_stre
#
# df.to_csv(r"E:\Projects\EmoLexiBerta_Gihan\Emo_LexiBERTa\use_case_DSI\processed_trump_biden_emo_wd_str.csv")
df.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_DSI\processed_trump_biden_emo_wd_str_eight.csv")
print("#done")