import ast

import pandas as pd


def check_p_n(profile):
    try:
        pos = profile['positive']
    except KeyError:
        pos = 0
    try:
        neg = profile['negative']
    except KeyError:
        neg = 0
    if(pos>neg):
        return 'p'
    else:
        return 'n'



def sent_to_perc(sents):
    positive_sentence_count = 0
    negative_sentence_count = 0
    for k in sents:
        # print(k)
        if 'p' == check_p_n(k):
            positive_sentence_count += 1
        elif 'n' == check_p_n(k):
            negative_sentence_count += 1

    out_perc = [round(((positive_sentence_count / len(sents)) * 100), 2),
                                       round(((negative_sentence_count / len(sents)) * 100), 2)]
    return out_perc



input_path_root = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\sentence_level_averaged\\"
out_path_root = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\\sentence_level_with_percentages\\"


dir_list = ['2010 Jan to Jun', '2010 Jul to Dec', '2011 Jan to Jun', '2011 Jul to Dec', '2012 Jan to Jun', '2012 Jul to Dec', '2013 Jan to Jun', '2013 Jul to Dec', '2014 Jan to Jun', '2014 Jul to Dec', '2015 Jan to Jun', '2015 Jul to Dec', '2016 Jan to Jun', '2016 Jul to Dec', '2017 Jan to Jun', '2017 Jul to Dec', '2018 Jan to Jun', '2019 Jan to Jun', '2019 Jul to Dec', '2020 Jan to Jun', '2020 Jul to Dec']
splits = ['0_300','300_800']
print(dir_list)

for i in dir_list:
    for j in splits:
        if(i=='2010 Jan to Jun'):
            f_name = "results_unprocessed_lnm_transcripts_left.csv"
            print(f_name)
            df = pd.read_csv(input_path_root + f_name)
            print(df.columns)
            sent_perc_presentation_CEO = []
            sent_perc_presentation_O_man = []
            sent_perc_qna_CEO = []
            sent_perc_qna_O_man = []
            sent_perc_qna_Anl = []
            sent_perc_qna_total = []
            sent_perc_pres_total = []
            qa_ceo_list = []
            for it, row in df.iterrows():
                presentation_CEO_segs = ast.literal_eval(row['presentation_CEO_segs'])
                presentation_other_man_segs = ast.literal_eval(row['presentation_other_man_segs'])
                qa_CEO_segs = ast.literal_eval(row['qa_CEO_segs'])
                qa_ceo_profile_list = []
                qa_anl_segs = ast.literal_eval(row['qa_analyst_segs'])
                qa_anl_profile_list = []
                qa_o_man_segs = ast.literal_eval(row['qa_other_man_segs'])
                qa_o_man_profile_list = []
                # print(qa_CEO_segs)
                # print('#pres #',row['#presentation_segments'])
                # print('#qa #', row['#qa_segments'])
                for ssc in qa_CEO_segs:
                    # print('ss',ss[3][1])
                    qa_ceo_profile_list.extend(ast.literal_eval(ssc[3][1]))
                for ssa in qa_anl_segs:
                    # print('ss',ss[3][1])
                    qa_anl_profile_list.extend(ast.literal_eval(ssa[3][1]))
                for sso in qa_o_man_segs:
                    # print('ss',ss[3][1])
                    qa_o_man_profile_list.extend(ast.literal_eval(sso[3][1]))

                total_qa_profile_list = qa_anl_profile_list + qa_ceo_profile_list + qa_o_man_profile_list
                if (len(presentation_CEO_segs)):
                    pres_ceo_profile_list = ast.literal_eval(presentation_CEO_segs[0][2][1])
                else:
                    pres_ceo_profile_list = []

                if (len(presentation_other_man_segs)):
                    pres_oman_profile_list = ast.literal_eval(presentation_other_man_segs[0][2][1])
                else:
                    pres_oman_profile_list = []
                total_pres_profile_list = pres_ceo_profile_list + pres_oman_profile_list
                # print(['ceo',len(ast.literal_eval(presentation_CEO_segs[0][2][1])),ast.literal_eval(presentation_CEO_segs[0][2][1])])
                # print(['oman', len(ast.literal_eval(presentation_other_man_segs[0][2][1])), ast.literal_eval(presentation_other_man_segs[0][2][1])])
                # print('anl',len(qa_anl_profile_list))
                # print('ceo',len(qa_ceo_profile_list))
                # print('oman',len(qa_o_man_profile_list))
                # print('ok')
                # print(len(presentation_CEO_segs))
                # print(presentation_CEO_segs)
                if (len(presentation_CEO_segs)):
                    # print(presentation_CEO_segs[0])
                    sents = ast.literal_eval(presentation_CEO_segs[0][2][1])
                    if (len(sents)):
                        perc = sent_to_perc(sents)
                        sent_perc_presentation_CEO.append(perc)
                    else:
                        sent_perc_presentation_CEO.append([0, 0])
                else:
                    sent_perc_presentation_CEO.append([0, 0])

                if (len(presentation_other_man_segs)):
                    # print(presentation_CEO_segs[0])
                    sents = ast.literal_eval(presentation_other_man_segs[0][2][1])
                    if (len(sents)):
                        perc = sent_to_perc(sents)
                        sent_perc_presentation_O_man.append(perc)
                    else:
                        sent_perc_presentation_O_man.append([0, 0])
                else:
                    sent_perc_presentation_O_man.append([0, 0])

                if (len(qa_ceo_profile_list)):
                    # print(presentation_CEO_segs[0])
                    sents = qa_ceo_profile_list
                    if (len(sents)):
                        perc = sent_to_perc(sents)
                        sent_perc_qna_CEO.append(perc)
                    else:
                        sent_perc_qna_CEO.append([0, 0])
                else:
                    sent_perc_qna_CEO.append([0, 0])

                if (len(qa_anl_profile_list)):
                    # print(presentation_CEO_segs[0])
                    sents = qa_anl_profile_list
                    if (len(sents)):
                        perc = sent_to_perc(sents)
                        sent_perc_qna_Anl.append(perc)
                    else:
                        sent_perc_qna_Anl.append([0, 0])
                else:
                    sent_perc_qna_Anl.append([0, 0])

                if (len(qa_o_man_profile_list)):
                    # print(presentation_CEO_segs[0])
                    sents = qa_o_man_profile_list
                    if (len(sents)):
                        perc = sent_to_perc(sents)
                        sent_perc_qna_O_man.append(perc)
                    else:
                        sent_perc_qna_O_man.append([0, 0])
                else:
                    sent_perc_qna_O_man.append([0, 0])

                if (len(total_pres_profile_list)):
                    # print(presentation_CEO_segs[0])
                    sents = total_pres_profile_list
                    if (len(sents)):
                        perc = sent_to_perc(sents)
                        sent_perc_pres_total.append(perc)
                    else:
                        sent_perc_pres_total.append([0, 0])
                else:
                    sent_perc_pres_total.append([0, 0])

                if (len(total_qa_profile_list)):
                    # print(presentation_CEO_segs[0])
                    sents = total_qa_profile_list
                    if (len(sents)):
                        perc = sent_to_perc(sents)
                        sent_perc_qna_total.append(perc)
                    else:
                        sent_perc_qna_total.append([0, 0])
                else:
                    sent_perc_qna_total.append([0, 0])
                # print(len(row['presentation_CEO_segs']))
                # print(type(row['presentation_CEO_segs']))
                # print(len(row['presentation_other_man_segs']))
                # print(row['presentation_other_man_segs'])
                # print(len(row['qa_analyst_segs']))
                # print(len(row['qa_other_man_segs']))
                # print(row)
                # # break
                # print(len(ast.literal_eval(presentation_CEO_segs[0][2][1])))
                # print(len(ast.literal_eval(presentation_other_man_segs[0][2][1])))
                # print(len(qa_ceo_profile_list))
                # print(len(qa_anl_profile_list))
                # print(len(qa_o_man_profile_list))
            print(sent_perc_presentation_CEO)
            print(sent_perc_presentation_O_man)
            print(sent_perc_qna_CEO)
            print(sent_perc_qna_O_man)
            print(sent_perc_qna_Anl)
            print(sent_perc_qna_total)
            print(sent_perc_pres_total)
            df['sent_perc_presentation_CEO'] = sent_perc_presentation_CEO
            df['sent_perc_presentation_O_man'] = sent_perc_presentation_O_man
            df['sent_perc_qna_CEO'] = sent_perc_qna_CEO
            df['sent_perc_qna_Anl'] = sent_perc_qna_Anl
            df['sent_perc_qna_O_man'] = sent_perc_qna_O_man
            df['sent_perc_qna_total'] = sent_perc_qna_total
            df['sent_perc_pres_total'] = sent_perc_pres_total

            df.to_csv(out_path_root + f_name, index=False)

        f_name = "results_unprocessed_lnm_transcripts_"+str(i)+"_"+str(j)+".csv"
        print(f_name)
        df = pd.read_csv(input_path_root + f_name)
        print(df.columns)
        sent_perc_presentation_CEO = []
        sent_perc_presentation_O_man = []
        sent_perc_qna_CEO = []
        sent_perc_qna_O_man = []
        sent_perc_qna_Anl = []
        sent_perc_qna_total = []
        sent_perc_pres_total = []
        qa_ceo_list = []
        for it,row in df.iterrows():
            presentation_CEO_segs = ast.literal_eval(row['presentation_CEO_segs'])
            presentation_other_man_segs = ast.literal_eval(row['presentation_other_man_segs'])
            qa_CEO_segs = ast.literal_eval(row['qa_CEO_segs'])
            qa_ceo_profile_list = []
            qa_anl_segs = ast.literal_eval(row['qa_analyst_segs'])
            qa_anl_profile_list = []
            qa_o_man_segs = ast.literal_eval(row['qa_other_man_segs'])
            qa_o_man_profile_list = []
            # print(qa_CEO_segs)
            # print('#pres #',row['#presentation_segments'])
            # print('#qa #', row['#qa_segments'])
            for ssc in qa_CEO_segs:
                # print('ss',ss[3][1])
                qa_ceo_profile_list.extend(ast.literal_eval(ssc[3][1]))
            for ssa in qa_anl_segs:
                # print('ss',ss[3][1])
                qa_anl_profile_list.extend(ast.literal_eval(ssa[3][1]))
            for sso in qa_o_man_segs:
                # print('ss',ss[3][1])
                qa_o_man_profile_list.extend(ast.literal_eval(sso[3][1]))

            total_qa_profile_list = qa_anl_profile_list+qa_ceo_profile_list+qa_o_man_profile_list
            if (len(presentation_CEO_segs)):
                pres_ceo_profile_list = ast.literal_eval(presentation_CEO_segs[0][2][1])
            else:pres_ceo_profile_list = []

            if(len(presentation_other_man_segs)):
                pres_oman_profile_list = ast.literal_eval(presentation_other_man_segs[0][2][1])
            else:pres_oman_profile_list = []
            total_pres_profile_list = pres_ceo_profile_list+pres_oman_profile_list
            # print(['ceo',len(ast.literal_eval(presentation_CEO_segs[0][2][1])),ast.literal_eval(presentation_CEO_segs[0][2][1])])
            # print(['oman', len(ast.literal_eval(presentation_other_man_segs[0][2][1])), ast.literal_eval(presentation_other_man_segs[0][2][1])])
            # print('anl',len(qa_anl_profile_list))
            # print('ceo',len(qa_ceo_profile_list))
            # print('oman',len(qa_o_man_profile_list))
            # print('ok')
            # print(len(presentation_CEO_segs))
            # print(presentation_CEO_segs)
            if(len(presentation_CEO_segs)):
                # print(presentation_CEO_segs[0])
                sents = ast.literal_eval(presentation_CEO_segs[0][2][1])
                if(len(sents)):
                    perc = sent_to_perc(sents)
                    sent_perc_presentation_CEO.append(perc)
                else:
                    sent_perc_presentation_CEO.append([0, 0])
            else:sent_perc_presentation_CEO.append([0,0])


            if (len(presentation_other_man_segs)):
                # print(presentation_CEO_segs[0])
                sents = ast.literal_eval(presentation_other_man_segs[0][2][1])
                if (len(sents)):
                    perc = sent_to_perc(sents)
                    sent_perc_presentation_O_man.append(perc)
                else:
                    sent_perc_presentation_O_man.append([0, 0])
            else:
                sent_perc_presentation_O_man.append([0, 0])

            if (len(qa_ceo_profile_list)):
                # print(presentation_CEO_segs[0])
                sents = qa_ceo_profile_list
                if (len(sents)):
                    perc = sent_to_perc(sents)
                    sent_perc_qna_CEO.append(perc)
                else:
                    sent_perc_qna_CEO.append([0, 0])
            else:
                sent_perc_qna_CEO.append([0, 0])

            if (len(qa_anl_profile_list)):
                # print(presentation_CEO_segs[0])
                sents = qa_anl_profile_list
                if (len(sents)):
                    perc = sent_to_perc(sents)
                    sent_perc_qna_Anl.append(perc)
                else:
                    sent_perc_qna_Anl.append([0, 0])
            else:
                sent_perc_qna_Anl.append([0, 0])

            if (len(qa_o_man_profile_list)):
                # print(presentation_CEO_segs[0])
                sents = qa_o_man_profile_list
                if (len(sents)):
                    perc = sent_to_perc(sents)
                    sent_perc_qna_O_man.append(perc)
                else:
                    sent_perc_qna_O_man.append([0, 0])
            else:
                sent_perc_qna_O_man.append([0, 0])


            if (len(total_pres_profile_list)):
                # print(presentation_CEO_segs[0])
                sents = total_pres_profile_list
                if (len(sents)):
                    perc = sent_to_perc(sents)
                    sent_perc_pres_total.append(perc)
                else:
                    sent_perc_pres_total.append([0, 0])
            else:
                sent_perc_pres_total.append([0, 0])

            if (len(total_qa_profile_list)):
                # print(presentation_CEO_segs[0])
                sents = total_qa_profile_list
                if (len(sents)):
                    perc = sent_to_perc(sents)
                    sent_perc_qna_total.append(perc)
                else:
                    sent_perc_qna_total.append([0, 0])
            else:
                sent_perc_qna_total.append([0, 0])
            # print(len(row['presentation_CEO_segs']))
            # print(type(row['presentation_CEO_segs']))
            # print(len(row['presentation_other_man_segs']))
            # print(row['presentation_other_man_segs'])
            # print(len(row['qa_analyst_segs']))
            # print(len(row['qa_other_man_segs']))
            # print(row)
            # # break
            # print(len(ast.literal_eval(presentation_CEO_segs[0][2][1])))
            # print(len(ast.literal_eval(presentation_other_man_segs[0][2][1])))
            # print(len(qa_ceo_profile_list))
            # print(len(qa_anl_profile_list))
            # print(len(qa_o_man_profile_list))
        print(sent_perc_presentation_CEO)
        print(sent_perc_presentation_O_man)
        print(sent_perc_qna_CEO)
        print(sent_perc_qna_O_man)
        print(sent_perc_qna_Anl)
        print(sent_perc_qna_total)
        print(sent_perc_pres_total)
        df['sent_perc_presentation_CEO'] = sent_perc_presentation_CEO
        df['sent_perc_presentation_O_man'] = sent_perc_presentation_O_man
        df['sent_perc_qna_CEO'] = sent_perc_qna_CEO
        df['sent_perc_qna_Anl'] = sent_perc_qna_Anl
        df['sent_perc_qna_O_man'] = sent_perc_qna_O_man
        df['sent_perc_qna_total'] = sent_perc_qna_total
        df['sent_perc_pres_total'] = sent_perc_pres_total

        df.to_csv(out_path_root+f_name,index=False)


    #     break
    # break
# [[76.92, 23.08], [69.63, 30.37], [83.33, 16.67], [0, 0], [74.58, 25.42], [80.43, 19.57], [67.38, 32.62], [72.92, 27.08], [90.2, 9.8], [71.82, 28.18], [90.74, 9.26], [63.54, 36.46], [50.0, 50.0], [73.68, 26.32], [71.43, 28.57], [75.15, 24.85], [92.47, 7.53], [83.76, 16.24], [76.0, 24.0], [75.86, 24.14], [75.51, 24.49], [64.0, 36.0], [69.49, 30.51], [73.33, 26.67], [58.16, 41.84], [83.33, 16.67], [77.03, 22.97], [72.73, 27.27], [70.0, 30.0], [73.44, 26.56], [66.67, 33.33], [74.68, 25.32], [81.01, 18.99], [73.44, 26.56], [71.58, 28.42], [66.67, 33.33], [76.09, 23.91], [64.95, 35.05], [80.0, 20.0], [50.0, 50.0], [68.09, 31.91], [80.0, 20.0], [100.0, 0.0], [85.71, 14.29], [76.92, 23.08], [69.35, 30.65], [86.79, 13.21], [66.67, 33.33], [100.0, 0.0], [63.89, 36.11], [72.86, 27.14], [0, 0], [79.41, 20.59], [81.13, 18.87], [0, 0], [78.26, 21.74], [82.0, 18.0], [80.56, 19.44], [84.13, 15.87], [0, 0], [65.52, 34.48], [83.9, 16.1], [78.95, 21.05], [87.3, 12.7], [65.38, 34.62], [72.73, 27.27], [74.26, 25.74], [82.81, 17.19], [62.67, 37.33], [72.22, 27.78], [93.18, 6.82], [84.8, 15.2], [0, 0], [86.3, 13.7], [72.5, 27.5], [74.34, 25.66], [80.0, 20.0], [82.5, 17.5], [91.8, 8.2], [80.0, 20.0], [76.84, 23.16], [100.0, 0.0], [83.33, 16.67], [67.86, 32.14], [78.12, 21.88], [72.73, 27.27], [0, 0], [74.19, 25.81], [81.58, 18.42], [86.27, 13.73], [60.0, 40.0], [81.69, 18.31], [100.0, 0.0], [78.87, 21.13], [74.31, 25.69], [100.0, 0.0], [74.47, 25.53], [88.24, 11.76], [84.16, 15.84], [78.95, 21.05], [75.44, 24.56], [72.26, 27.74], [70.77, 29.23], [72.86, 27.14], [80.0, 20.0], [85.29, 14.71], [0, 0], [75.0, 25.0], [58.54, 41.46], [78.38, 21.62], [62.89, 37.11], [82.65, 17.35], [75.41, 24.59], [82.93, 17.07], [74.42, 25.58], [89.8, 10.2], [80.7, 19.3], [75.68, 24.32], [86.11, 13.89], [75.68, 24.32], [74.58, 25.42], [63.11, 36.89], [78.72, 21.28], [0, 0], [0, 0], [89.36, 10.64], [81.25, 18.75], [73.47, 26.53], [92.16, 7.84], [50.0, 50.0], [0, 0], [80.0, 20.0], [0, 0], [85.0, 15.0], [81.25, 18.75], [81.4, 18.6], [79.49, 20.51], [75.6, 24.4]]
