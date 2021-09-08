import nltk
import pandas as pd
from transformers import AutoTokenizer, AutoModel
from Core.profile_builder import build_profile
import ast


model_path = r"E:\Projects\Emo_LexiBERTa\Finetuned_Langue_Models\DistilBERT_GoEmotions_Finetuned"
vocab_path = r"E:\Projects\Emo_LexiBERTa\Vocabularies\goemotion_vocabulary.csv"



def ft_to_et(emo_dict):

    eight_dict = {'sadness': 0, 'anger': 0, 'joy': 0, 'anticipation': 0, 'fear': 0, 'surprise': 0, 'disgust': 0,
                  'trust': 0}

    if ('anticipation' in emo_dict.keys()):
        eight_dict['anticipation'] += emo_dict['anticipation']
    if ('amazement_surprise' in emo_dict.keys()):
        eight_dict['surprise'] += emo_dict['amazement_surprise']
    if ('distraction' in emo_dict.keys()):
        eight_dict['surprise'] += emo_dict['distraction']
    if ('fear' in emo_dict.keys()):
        eight_dict['fear'] += emo_dict['fear']
    if ('trust' in emo_dict.keys()):
        eight_dict['trust'] += emo_dict['trust']
    if ('interest_vigilance' in emo_dict.keys()):
        eight_dict['anticipation'] += emo_dict['interest_vigilance']
    if ('anger' in emo_dict.keys()):
        eight_dict['anger'] += emo_dict['anger']
    if ('disgust_loathing' in emo_dict.keys()):
        eight_dict['disgust'] += emo_dict['disgust_loathing']
    if ('senerity' in emo_dict.keys()):
        eight_dict['joy'] += emo_dict['senerity']
    if ('boredom' in emo_dict.keys()):
        eight_dict['disgust'] += emo_dict['boredom']
    if ('acceptance' in emo_dict.keys()):
        eight_dict['trust'] += emo_dict['acceptance']
    if ('joy_ecstasy' in emo_dict.keys()):
        eight_dict['joy'] += emo_dict['joy_ecstasy']
    if ('admire' in emo_dict.keys()):
        eight_dict['trust'] += emo_dict['admire']
    if ('sadness' in emo_dict.keys()):
        eight_dict['sadness'] += emo_dict['sadness']

    # print(eight_dict)

    eight_dict = {k: v for k, v in sorted(eight_dict.items(), key=lambda item: item[1])}
    return eight_dict


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
        pred = build_profile(text,1,df,tokenizer,model,keyword_extraction=True,modifier_detection=True)
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
    # sentence = "Muslims are so disgusting"
    # pred = build_profile(sentence, 1, df, tokenizer, model, keyword_extraction=True, modifier_detection=True)
    # print(pred)
    #
    # sentence = "Muslims are very friendly"
    # pred = build_profile(sentence, 1, df, tokenizer, model, keyword_extraction=True, modifier_detection=True)
    # print(pred)
    #
    # sentence = "muslims are not friendly"
    # pred = build_profile(sentence, 1, df, tokenizer, model, keyword_extraction=True, modifier_detection=True)
    # print(pred)

    inp_df = pd.read_csv(r"E:\Projects\Emo_LexiBERTa\use_case_sajani\sentences.csv")
    profiles = []
    keywords = []
    for i,row in inp_df.iterrows():
        print(row['sentence'])
        text = row['sentence']
        pred = build_profile(text, 1, df, tokenizer, model, keyword_extraction=True, modifier_detection=True)
        print(pred)
        profiles.append(ft_to_et(pred[0]))
        keywords.append(pred[1])
        # if(i==10):break


    df_out = inp_df
    df_out['emotion_profile'] = profiles
    df_out['emotion_keywords'] = keywords


    df_out.to_csv(r"E:\Projects\Emo_LexiBERTa\use_case_sajani\sentences_out.csv")