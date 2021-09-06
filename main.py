import pandas as pd
from transformers import AutoTokenizer, AutoModel
from Core.profile_builder import build_profile
import ast


model_path = r"E:\Projects\Emo_LexiBERTa\Finetuned_Langue_Models\DistilBERT_GoEmotions_Finetuned"
vocab_path = r"E:\Projects\Emo_LexiBERTa\Vocabularies\goemotion_vocabulary.csv"



tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path)


df = pd.read_csv(vocab_path)
df = df.dropna()
df['embedding'] = [ast.literal_eval(i) for i in df['embedding'].values.tolist()]

# sentence = "always thought that nigger was a faggot"
sentence = "Muslims are so disgusting"
# sentence = "muslims are very friendly"
pred = build_profile(sentence,1,df,tokenizer,model,keyword_extraction=True,modifier_detection=False)

print(pred)