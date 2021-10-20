import pandas as pd
import ast
df = pd.read_csv(r"E:\Projects\EmoLexiBerta_Gihan\Emo_LexiBERTa\use_case_DSI\processed_trump_biden_emo_all.csv")

print(df.columns)
HS_keys = []
emo_keys = []


for i,row in df.iterrows():
    hs_k_st = ''
    em_k_st = ''
    for hk in ast.literal_eval(row['keywords']):
        hs_k_st+=str(hk)+', '
    for ek in ast.literal_eval(row['emo_kwds']):
        em_k_st+=str(ek)+', '
    print(hs_k_st)
    HS_keys.append(hs_k_st)
    emo_keys.append(em_k_st)

df['HS_keys'] = HS_keys
df['emo_keys'] = emo_keys

df.to_csv(r"E:\Projects\EmoLexiBerta_Gihan\Emo_LexiBERTa\use_case_DSI\processed_trump_biden_emo_all_topivot.csv")