import pandas as pd
from transformers import AutoTokenizer, AutoModel
from transformers import DistilBertTokenizerFast
from Core.profile_builder import build_profile
import ast


model_path = r"E:\Projects\Emo_LexiBERTa\Finetuned_Langue_Models\DistilBERT_GoEmotions_Finetuned"
vocab_path = r"E:\Projects\Emo_LexiBERTa\Vocabularies\goemotion_vocabulary.csv"

dff = pd.read_csv(r"E:\Projects\DSI Gihan Prev\covid_experiments\processed_preds_2021_all_meta_maxes.csv")

tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path)

df = pd.read_csv(vocab_path)
df = df.dropna()
df['embedding'] = [ast.literal_eval(i) for i in df['embedding'].values.tolist()]




print(len(dff))

profiles = []
kwds = []
# dff = dff[80000:100000]
for i,row in dff.iterrows():
    # print(row['text'])
    print([i,len(dff)])
    sentence = row['text']
    pred = build_profile(sentence, 1, df, tokenizer, model, keyword_extraction=True, modifier_detection=True)
    profiles.append(pred[0])
    kwds.append(pred[1])

print(profiles)
print(kwds)

dff['emo_profiles'] = profiles
dff['emo_kwds'] = kwds

dff.to_csv(r"E:\Projects\EmoLexiBerta_Gihan\Emo_LexiBERTa\use_case_covid_vaccine\processed_preds_2021_all_meta_maxes_with_emo0.csv")