import pandas as pd
from transformers import AutoTokenizer, AutoModel
from transformers import DistilBertTokenizerFast
from Core.profile_builder import build_profile
import ast


model_path = r"E:\Projects\Emo_LexiBERTa\Finetuned_Langue_Models\DistilBERT_GoEmotions_Finetuned"
vocab_path = r"E:\Projects\Emo_LexiBERTa\Vocabularies\goemotion_vocabulary.csv"
# vocab_path = r"E:\Projects\emo_detector_new\vocabs\senti4sd_vocabulary.csv"
dff = pd.read_csv(r"E:\Projects\emo_detector_new\datasets\test_senti4sd.csv")

tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path)

df = pd.read_csv(vocab_path)
df = df.dropna()
df['embedding'] = [ast.literal_eval(i) for i in df['embedding'].values.tolist()]




print(len(dff))
print(dff.columns)
# print(sas)
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

dff.to_csv(r"E:\Projects\emo_detector_new\software_development\emo_preds.csv")