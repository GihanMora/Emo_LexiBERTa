import pandas as pd

df_list = []
for i in [0,20000,40000,60000,80000]:
    df = pd.read_csv(r"E:\Projects\EmoLexiBerta_Gihan\Emo_LexiBERTa\use_case_DSI\processed_trump_biden_all_maxes_with_emo_%s_%s.csv"%(i,i+20000))


    df_list.append(df)

out_df = pd.concat(df_list)


out_df.to_csv(r"E:\Projects\EmoLexiBerta_Gihan\Emo_LexiBERTa\use_case_DSI\\processed_trump_biden_emo_all.csv")