import nltk as nltk
import pandas as pd
from transformers import AutoTokenizer, AutoModel
from Core.profile_builder import build_profile
import ast


model_path = r"E:\Projects\Emo_LexiBERTa\Finetuned_Langue_Models\DistilBERT_GoEmotions_Finetuned"
vocab_path = r"E:\Projects\Emo_LexiBERTa\Vocabularies\goemotion_vocabulary.csv"



def emo_detecct_document(text):
    df = pd.read_csv(vocab_path)
    df = df.dropna()
    df['embedding'] = [ast.literal_eval(i) for i in df['embedding'].values.tolist()]
    output_emo_dict = {
              'anticipation':0,
              'anger':0,
              'fear':0,
              'sadness':0,
              'trust':0,
              'senerity':0,
              'joy_ecstasy':0,
              'admire':0,
              'acceptance':0,
              'amazement_surprise':0,
              'distraction':0,
              'boredom':0,
              'disgust_loathing':0,
              'interest_vigilance':0}
    a_list = nltk.tokenize.sent_tokenize(text)

    for each_s in a_list:
        # print(each_s)
        pred = build_profile(sentence,1,df,tokenizer,model,keyword_extraction=True,modifier_detection=True)
        for each_k in pred[0].keys():
            output_emo_dict[each_k]=output_emo_dict[each_k]+pred[0][each_k]

    # print(output_emo_dict)
    return output_emo_dict



if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModel.from_pretrained(model_path)


    df = pd.read_csv(vocab_path)
    df = df.dropna()
    df['embedding'] = [ast.literal_eval(i) for i in df['embedding'].values.tolist()]

    # sentence = "always thought that nigger was a faggot"
    sentence = "Muslims are so disgusting"
    pred = build_profile(sentence,1,df,tokenizer,model,keyword_extraction=True,modifier_detection=True)
    print(pred)

    # sentence = "muslims are very friendly"
    # pred = build_profile(sentence, 1, df, tokenizer, model, keyword_extraction=True, modifier_detection=True)
    # print(pred)
    #
    # sentence = "muslims are not friendly"
    # pred = build_profile(sentence, 1, df, tokenizer, model, keyword_extraction=True, modifier_detection=True)
    # print(pred)