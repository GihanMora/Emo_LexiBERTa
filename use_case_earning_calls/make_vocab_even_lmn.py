
import pandas as pd
df = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\Vocabularies\lnm_stemmed_vocab.csv")
print(len(df))
print(len(df.loc[df['eight_label'] == 'negative']))
for i,row in df.iterrows():
    if((i%2==0 or i%3==0 or i%5==0) and (row['eight_label'] == 'negative')):
        df.drop(i, inplace=True)
    if ((i % 2 == 0) and (row['eight_label'] == 'litigious')):
        df.drop(i, inplace=True)

print(len(df.loc[df['eight_label'] == 'positive']))
print(len(df.loc[df['eight_label'] == 'negative']))
print(len(df.loc[df['eight_label'] == 'uncertainty']))
print(len(df.loc[df['eight_label'] == 'litigious']))
print(len(df.loc[df['eight_label'] == 'model_strong']))
print(len(df.loc[df['eight_label'] == 'model_weak']))

df.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\Vocabularies\lnm_vocab_even_new.csv")