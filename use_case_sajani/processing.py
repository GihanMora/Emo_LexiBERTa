import pandas as pd
import ast
df = pd.read_csv(r"E:\Projects\Emo_LexiBERTa\use_case_sajani\paragraphs_out.csv")

print(df.columns)
binary_emos = {'sadness':[], 'anger':[], 'anticipation':[], 'fear':[], 'surprise':[], 'disgust':[], 'joy':[], 'trust':[]}
for i,row in df.iterrows():
    emo = ast.literal_eval(row['emotion_profile'])
    for k in (emo.keys()):
        if(emo[k]>0):
            binary_emos[k].append(1)
        elif (emo[k] == 0):
            binary_emos[k].append(0)

    # print(emo['anger'])
df_out = df.drop(['emotion_profile', 'emotion_keywords'], axis = 1)


for k in (binary_emos.keys()):
    print(len(binary_emos[k]))
    df_out[k] = binary_emos[k]

df_out.to_csv(r"E:\Projects\Emo_LexiBERTa\use_case_sajani\paragraphs_binary.csv")