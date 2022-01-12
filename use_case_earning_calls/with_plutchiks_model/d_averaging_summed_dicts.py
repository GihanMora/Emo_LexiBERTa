
import ast

import math
import numpy as np
import pandas as pd


def average_summed(profile,divider):
    print(['input',profile,divider])
    sum_t = 0
    for k in profile.keys():
        sum_t=sum_t+profile[k]
    if(divider==round(sum_t)):
        if(divider==0):
            # print('divider 0')
            return profile
        for ky in profile.keys():
            profile[ky] = round((profile[ky]/sum_t),3)
        print(profile)
        sum_t = 0
        for k in profile.keys():
            sum_t = sum_t + profile[k]
        print(round(sum_t))
        return profile
    else:
        print(divider,sum_t,round(sum_t))
        print([profile,divider])
        for ky in profile.keys():
            profile[ky] = round((profile[ky]/sum_t),3)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>err')
        return profile



input_path_root = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks\\"
out_path_root = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_averaged\\"

def scaling(f_name):

    df = pd.read_csv(input_path_root+f_name)

    presentation_all_e_p_l = []
    qa_all_e_p_l = []
    presentation_CEO_l = []
    presentation_other_man_l = []
    qa_CEO_l = []
    qa_other_man_l = []
    qa_analyst_l = []





    for i,row in df.iterrows():
        # print(row)
        # print('*****')
        # print(row['pdf'],row['presentation_all_e_p'])

        # print(row['presentation_all_e_p'])
        # if(row['presentation_all_e_p']!=row['presentation_all_e_p']):
        #     row['presentation_all_e_p'] = "{'negative': 0, 'positive': 0, 'uncertainty': 0, 'litigious': 0, 'model_strong': 0, 'model_weak': 0}"
        #     print('HHHHHHHHHH')
        # if (row['presentation_all_e_p']=='{}'):
        #     row[
        #         'presentation_all_e_p'] = "{'negative': 0, 'positive': 0, 'uncertainty': 0, 'litigious': 0, 'model_strong': 0, 'model_weak': 0}"
        #     print('empHHHHHHHHHH')

        # if (not ast.literal_eval(row['qa_all_e_p'])):
        #     row[
        #         'qa_all_e_p'] = "{'negative': 0, 'positive': 0, 'uncertainty': 0, 'litigious': 0, 'model_strong': 0, 'model_weak': 0}"
            # print('HHHHHHHHHH')
        # print(row['#presentation_segments'])
        # row['presentation_all_e_p'] = average_summed(ast.literal_eval(row['presentation_all_e_p']),ast.literal_eval(row['#presentation_segments'])[0])
        # df.loc[i, 'presentation_all_e_p'] = average_summed(ast.literal_eval(row['presentation_all_e_p']),ast.literal_eval(row['#presentation_segments'])[0])
        # df.at[i, 'presentation_all_e_p']= average_summed(ast.literal_eval(row['presentation_all_e_p']),ast.literal_eval(row['#presentation_segments'])[0])
        # print('out',average_summed(ast.literal_eval(row['presentation_all_e_p']),ast.literal_eval(row['#presentation_segments'])[0]))        # print(row['presentation_all_e_p'])
        presentation_all_e_p_l.append(average_summed(ast.literal_eval(row['presentation_all_e_p']),ast.literal_eval(row['#presentation_segments'])[0]))
        # if (row['presentation_all_e_p'] != row['presentation_all_e_p']):
        #     print('aftHHHHHHHHHH')
        # print(row['qa_all_e_p'])
        # print(row['#qa_segments'])
        # row['qa_all_e_p'] = average_summed(ast.literal_eval(row['qa_all_e_p']), ast.literal_eval(row['#qa_segments'])[0])
        # df.at[i, 'qa_all_e_p'] = average_summed(ast.literal_eval(row['qa_all_e_p']), ast.literal_eval(row['#qa_segments'])[0])
        qa_all_e_p_l.append(average_summed(ast.literal_eval(row['qa_all_e_p']), ast.literal_eval(row['#qa_segments'])[0]))
        # print(row['presentation_CEO_segs'])
        # print(row['presentation_CEO'])
        # row['presentation_CEO'] = average_summed(ast.literal_eval(row['presentation_CEO']), len(ast.literal_eval(row['presentation_CEO_segs'])))
        # df.at[i, 'presentation_CEO'] = average_summed(ast.literal_eval(row['presentation_CEO']),
        #                                          len(ast.literal_eval(row['presentation_CEO_segs'])))
        presentation_CEO_l.append( average_summed(ast.literal_eval(row['presentation_CEO']), len(ast.literal_eval(row['presentation_CEO_segs']))))

        # print(row['presentation_other_man'])
        # print(row['presentation_other_man_segs'])
        # row['presentation_other_man'] = average_summed(ast.literal_eval(row['presentation_other_man']), len(ast.literal_eval(row['presentation_other_man_segs'])))
        # df.at[i, 'presentation_other_man'] = average_summed(ast.literal_eval(row['presentation_other_man']),  len(ast.literal_eval(row['presentation_other_man_segs'])))
        presentation_other_man_l.append(average_summed(ast.literal_eval(row['presentation_other_man']),  len(ast.literal_eval(row['presentation_other_man_segs']))))
        # print(row['qa_CEO'])
        # print(row['qa_CEO_segs'])
        # row['qa_CEO'] = average_summed(ast.literal_eval(row['qa_CEO']), len(ast.literal_eval(row['qa_CEO_segs'])))
        # df.at[i, 'qa_CEO'] = average_summed(ast.literal_eval(row['qa_CEO']), len(ast.literal_eval(row['qa_CEO_segs'])))
        qa_CEO_l.append(average_summed(ast.literal_eval(row['qa_CEO']), len(ast.literal_eval(row['qa_CEO_segs']))))
        # print(row['qa_other_man'])
        # print(row['qa_other_man_segs'])
        # row['qa_other_man'] = average_summed(ast.literal_eval(row['qa_other_man']), len(ast.literal_eval(row['qa_other_man_segs'])))
        # df.at[i, 'qa_other_man'] = average_summed(ast.literal_eval(row['qa_other_man']),
        #                                      len(ast.literal_eval(row['qa_other_man_segs'])))
        qa_other_man_l.append(average_summed(ast.literal_eval(row['qa_other_man']), len(ast.literal_eval(row['qa_other_man_segs']))))
        # print(row['qa_analyst'])
        # print(row['qa_analyst_segs'])
        # row['qa_analyst'] = average_summed(ast.literal_eval(row['qa_analyst']), len(ast.literal_eval(row['qa_analyst_segs'])))
        # df.at[i, 'qa_analyst'] = average_summed(ast.literal_eval(row['qa_analyst']),
        #                                    len(ast.literal_eval(row['qa_analyst_segs'])))

        qa_analyst_l.append(average_summed(ast.literal_eval(row['qa_analyst']),
                                           len(ast.literal_eval(row['qa_analyst_segs']))))


    df['presentation_all_e_p'] =presentation_all_e_p_l
    df['qa_all_e_p'] = qa_all_e_p_l
    df['presentation_CEO'] = presentation_CEO_l
    df['presentation_other_man'] = presentation_other_man_l
    df['qa_CEO'] = qa_CEO_l
    df['qa_other_man'] = qa_other_man_l
    df['qa_analyst'] = qa_analyst_l
    df.to_csv(out_path_root+f_name, index=False)

# scaling("results_unprocessed_lnm_transcripts_2010 Jan to Jun_0_300.csv")

dir_list = ['2010 Jan to Jun', '2010 Jul to Dec', '2011 Jan to Jun', '2011 Jul to Dec', '2012 Jan to Jun', '2012 Jul to Dec', '2013 Jan to Jun', '2013 Jul to Dec', '2014 Jan to Jun', '2014 Jul to Dec', '2015 Jan to Jun', '2015 Jul to Dec', '2016 Jan to Jun', '2016 Jul to Dec', '2017 Jan to Jun', '2017 Jul to Dec', '2018 Jan to Jun', '2019 Jan to Jun', '2019 Jul to Dec', '2020 Jan to Jun', '2020 Jul to Dec']
splits = ['0_300','300_800']
print(dir_list)


# i='2017 Jul to Dec'
# j = "0_300"
# scaling("results_unprocessed_lnm_transcripts_"+str(i)+"_"+str(j)+".csv")
scaling("results_unprocessed_lnm_transcripts_left_80_100.csv")
# for i in dir_list:
#     for j in splits:
#
#         f_name = "results_unprocessed_lnm_transcripts_"+str(i)+"_"+str(j)+".csv"
#         print(f_name)
#         scaling(f_name)


