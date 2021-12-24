import pandas as pd
import ast



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
    return eight_dict


df = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_DSI\processed_trump_biden_emo_all.csv")

et_emo_prs = []
max_emos = []
max_emos_lb = []
for i, row in df.iterrows():
    prf = ast.literal_eval(row['emo_profiles'])
    eight_pr =  ft_to_et(prf)

    et_emo_prs.append(eight_pr)
    emo_prf = {k: v for k, v in sorted(eight_pr.items(), key=lambda item: item[1])}
    # print(prf)
    print(emo_prf)
    max_emos.append(emo_prf[[*emo_prf][-1]])
    max_emos_lb.append([*emo_prf][-1])
    # break
df['eight_emo_profiles'] = et_emo_prs
df['max_emo_lb'] = max_emos_lb
df['max_emo_val'] = max_emos
df.to_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_DSI\processed_trump_biden_emo_all_eight.csv")