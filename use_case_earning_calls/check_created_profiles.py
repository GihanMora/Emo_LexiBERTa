import pandas as pd
import ast

# df1 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\results_unprocessed_lnm_transcripts_2020 Jul to Dec_0_1_sentence.csv")
# print(df1.columns)
# print(df1['presentation_CEO_segs'])

def sum_up_dicts(emo_dicts):
    sum_dict = {
        'negative': 0,
        'positive': 0,
        'uncertainty': 0,
        'litigious': 0,
        'model_strong': 0,
        'model_weak': 0,
        'anticipation': 0,
        'anger': 0,
        'fear': 0,
        'sadness': 0,
        'trust': 0,
        'senerity': 0,
        'joy_ecstasy': 0,
        'joy': 0,
        'sad': 0,
        'admire': 0,
        'acceptance': 0,
        'amazement_surprise': 0,
        'surprise': 0,
        'distraction': 0,
        'boredom': 0,
        'disgust_loathing': 0,
        'disgust': 0,
        'interest_vigilance': 0}

    for each_dict in emo_dicts:
        for each_k in each_dict.keys():
            sum_dict[each_k] = sum_dict[each_k] + each_dict[each_k]
    final_sum_dict = sum_dict.copy()
    for k in sum_dict.keys():
        if sum_dict[k] == 0:
            del final_sum_dict[k]
    print(final_sum_dict)
    return final_sum_dict

def avg_up_dicts(emo_dicts):
    sum_dict = {
        'negative': 0,
        'positive': 0,
        'uncertainty': 0,
        'litigious': 0,
        'model_strong': 0,
        'model_weak': 0,
        'anticipation': 0,
        'anger': 0,
        'fear': 0,
        'sadness': 0,
        'trust': 0,
        'senerity': 0,
        'joy_ecstasy': 0,
        'joy': 0,
        'sad': 0,
        'admire': 0,
        'acceptance': 0,
        'amazement_surprise': 0,
        'surprise': 0,
        'distraction': 0,
        'boredom': 0,
        'disgust_loathing': 0,
        'disgust': 0,
        'interest_vigilance': 0}

    for each_dict in emo_dicts:
        for each_k in each_dict.keys():
            sum_dict[each_k] = sum_dict[each_k] + each_dict[each_k]
    final_sum_dict = sum_dict.copy()
    for k in sum_dict.keys():
        if sum_dict[k] == 0:
            del final_sum_dict[k]
    print('sum',final_sum_dict)

    for kk in final_sum_dict.keys():
        final_sum_dict[kk] = final_sum_dict[kk]/len(emo_dicts)

    return final_sum_dict


# df1 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\results_unprocessed_lnm_transcripts_2020 Jul to Dec_0_1.csv")
# print(df1.columns)

# preds_segs = df1['presentation_segments']
# for it in preds_segs:
#     it = ast.literal_eval(it)
#     for iit in it:
#         print('*****')
#         print(iit)
#         chunks = ast.literal_eval(iit[2][1])
#         print(chunks[:10])
#         print(avg_up_dicts(chunks[:10]))
#         print(chunks[10:20])
#         print(avg_up_dicts(chunks[10:20]))
#         print(chunks[20:])
#         print(avg_up_dicts(chunks[20:]))
#         print(len(chunks))

# print('>>>>>>>>>>>>>>>')
# df1 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\results_unprocessed_lnm_transcripts_2020 Jul to Dec_0_1_chunked.csv")
# # print(df1.columns)
#
# preds_segs = df1['presentation_segments']
# for it in preds_segs:
#     it = ast.literal_eval(it)
#     for iit in it:
#         print('*****')
#         for k in iit:
#             print(k)

# eedd = [{'negative': 0.063, 'positive': 0.2731, 'uncertainty': 0.3222, 'litigious': 0.30800000000000005, 'model_strong': 0.0172, 'model_weak': 0.0167},{'negative': 0.07720000000000002, 'positive': 0.40569999999999995, 'uncertainty': 0.21820000000000003, 'litigious': 0.2604, 'model_strong': 0.0305, 'model_weak': 0.0083},{'negative': 0.056, 'positive': 0.156, 'uncertainty': 0.58, 'litigious': 0.189, 'model_weak': 0.019}
# ]
# print(sum_up_dicts(eedd))


# df1 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\default_lnm\results_unprocessed_lnm_transcripts_2020 Jul to Dec_0_1.csv")
# print(df1.columns)
#
# preds_segs = ast.literal_eval(df1['qa_CEO_segs'][0])
#
# for i in preds_segs:
#     emosi = i[2]
#     emosi  = sorted(emosi.items(), key=lambda x: x[1])
#     print(emosi)


# df1 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\even_voc\results_unprocessed_lnm_transcripts_2020 Jul to Dec_0_1.csv")
# print(df1.columns)
#
# preds_segs = ast.literal_eval(df1['qa_CEO_segs'][0])
#
# for i in preds_segs:
#     emosi = i[2]
#     emosi  = sorted(emosi.items(), key=lambda x: x[1])
#     print(emosi)
#
df1 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\new\results_unprocessed_lnm_transcripts_2020 Jan to Jun_300_800.csv")
# df1.columns = ['pdf', 'company_ticker', 'event_date', 'presentation_CEO_segs',
#        'presentation_other_man_segs', 'presentation_CEO',
#        'presentation_other_man', 'qa_CEO_segs', 'qa_analyst_segs',
#        'qa_other_man_segs', 'qa_CEO', 'qa_analyst', 'qa_other_man',
#        'participants', '#presentation_body', '#qa_body',
#        'presentation_all_e_p', 'qa_all_e_p', '#presentation_segments',
#        '#qa_segments', 'presentation_segments', 'qa_segments', 'e_p_pres',
#        'e_p_qa', 'year', 'quarter', 'comp_name']

print(df1.columns)
print(len(df1))
preds_segs = ast.literal_eval(df1['qa_segments'][0])

for i in df1.columns:
    print(df1[i])
    # emosi = i[2]
    # emosi  = sorted(emosi.items(), key=lambda x: x[1])
    # print(emosi)