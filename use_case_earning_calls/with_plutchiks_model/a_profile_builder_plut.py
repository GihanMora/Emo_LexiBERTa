import csv
import os
import re

import pandas
import pandas as pd
from transformers import AutoTokenizer, AutoModel
from transformers import DistilBertTokenizerFast
from Core.profile_builder import build_profile
import ast
import pdfplumber

def summon_profiles(prof_list):
    output_emo_dict = {
        # 'negative': 0,
        # 'positive': 0,
        # 'uncertainty': 0,
        # 'litigious': 0,
        # 'model_strong': 0,
        # 'model_weak': 0,
        'anticipation': 0,
        'anger': 0,
        'fear': 0,
        'joy': 0,
        'sad': 0,
        'disgust': 0,
        'surprise': 0,
        'trust': 0,
    }
    for pred in prof_list:

        for each_k in pred.keys():
            output_emo_dict[each_k] = output_emo_dict[each_k] + pred[each_k]

    print(output_emo_dict)
    return output_emo_dict

import nltk
from datetime import datetime
nltk.download('punkt')

def sum_up_dicts(emo_dicts):
    sum_dict = {
        # 'negative': 0,
        # 'positive': 0,
        # 'uncertainty': 0,
        # 'litigious': 0,
        # 'model_strong': 0,
        # 'model_weak': 0,
        'anticipation': 0,
        'anger': 0,
        'fear': 0,
        'joy': 0,
        'sad': 0,
        'disgust': 0,
        'surprise': 0,
        'trust': 0,
        # 'sadness': 0,

        # 'senerity': 0,
        # 'joy_ecstasy': 0,

        # 'admire': 0,
        # 'acceptance': 0,
        # 'amazement_surprise': 0,

        # 'distraction': 0,
        # 'boredom': 0,
        # 'disgust_loathing': 0,

        # 'interest_vigilance': 0
    }

    for each_dict in emo_dicts:
        for each_k in each_dict.keys():
            sum_dict[each_k] = sum_dict[each_k] + each_dict[each_k]
    final_sum_dict = sum_dict.copy()
    for k in sum_dict.keys():
        if sum_dict[k] == 0:
            del final_sum_dict[k]
    print(final_sum_dict)
    return final_sum_dict
def emo_detect_document_lnm(text, tokenizer, model, step, df):
    t_eddl1 = datetime.now()
    output_emo_dict = {
        # 'negative': 0,
        # 'positive': 0,
        # 'uncertainty': 0,
        # 'litigious': 0,
        # 'model_strong': 0,
        # 'model_weak': 0,
        'anticipation': 0,
        'anger': 0,
        'fear': 0,
        'joy': 0,
        'sad': 0,
        'disgust': 0,
        'surprise': 0,
        'trust': 0,
    }
    a_list = nltk.tokenize.sent_tokenize(text)
    sentence_chunks = [(' ').join(a_list[i:i + step]) for i in range(0, len(a_list), step)]
    print(len(sentence_chunks))
    print('sen_chunks',sentence_chunks)
    chunk_profiles = []
    chunk_keywords = []
    # for each_s in a_list:
    for sentence_chunk in sentence_chunks:
        # print(each_s)
        # pred = emotion_candidates_recognition(each_s,1,df,tokenizer,model)
        pred_out = build_profile(sentence_chunk, 1, df, tokenizer, model, keyword_extraction=True, modifier_detection=True)
        pred = pred_out[0]
        chunk_profiles.append(pred)
        chunk_keywords.append([pred_out[1]])

        for each_k in pred.keys():
            output_emo_dict[each_k] = output_emo_dict[each_k] + pred[each_k]

    print('out_dict_summon',output_emo_dict)

    #normalizing
    if(len(sentence_chunks)):
        for kk in output_emo_dict.keys():
            output_emo_dict[kk] = output_emo_dict[kk]/len(sentence_chunks)

    print('chunk emos dicts',chunk_profiles)
    t_eddl2 = datetime.now()
    diff_eddl = t_eddl2 - t_eddl1
    print('time for emotion_document_lnm', diff_eddl)

    return [output_emo_dict,len(sentence_chunks),str(chunk_profiles),str(chunk_keywords)]

def process_pdf(f_path,df,tokenizer,model):
    presentation_body = ''
    qa_body = ''
    pres_segments = []
    qa_segments = []
    all_participants = []
    keyphrases_pb = []
    keyphrases_qab = []
    emotion_profiles_for_presentation_segments = []
    emotion_profiles_for_qa_segments = []
    e_p_presentation_body = []
    e_p_qa = []
    processed_data = {}
    pdf = pdfplumber.open(f_path)
    full_text = ''
    total_pages = len(pdf.pages)

    cover_page = pdf.pages[0].extract_text()
    try:
        cv_text_a = cover_page.split('PLACEHOLDER TRANSCRIPT')[1]
    except:
        cv_text_a = cover_page.split('EDITED TRANSCRIPT')[1]
    cv_text_b = cv_text_a.split('Earnings')[0]
    cv_text_b_splits = cv_text_b.split(' ')

    year_cv = cv_text_b_splits[1].strip()
    qtr_cv = cv_text_b_splits[0].strip()
    # print(year_cv,qtr_cv)
    comp_name = (" ").join(cv_text_b_splits[2:])
    print("year",year_cv)
    print("quater",qtr_cv)
    print("comp_name",comp_name)
    print('********************')

    for each_page in range(1,total_pages):
        page = pdf.pages[each_page]
        text = page.extract_text()
        text+='\n\n\n'
        full_text+=text

    # print(full_text)

    participants = []
    second_page = pdf.pages[1]
    participant_text = second_page.extract_text()
    all_participants = ['Operator']
    # print('processing participants')
    if('CORPORATE PARTICIPANTS' in participant_text and 'PRESENTATION' in participant_text):
        try:
            part_a = participant_text.split('CORPORATE PARTICIPANTS')[1]
            part_b = part_a.split('CONFERENCE CALL PARTICIPANTS')
            cop_parti = part_b[0].strip()
            conf_parti = part_b[1].split('PRESENTATION')[0].strip()
            # print('CORPORATE PARTICIPANTS')
            # print(cop_parti)
            # print('CONFERENCE CALL PARTICIPANTS')
            # print(conf_parti)
            cop_parti_list = cop_parti.split('\n')
            conf_parti_list = conf_parti.split('\n')
            # print(cop_parti_list)
            # print(conf_parti_list)
            all_participants.extend(cop_parti_list)
            all_participants.extend(conf_parti_list)
        except:
            part_a = participant_text.split('CORPORATE PARTICIPANTS')[1]
            part_b = part_a.split('PRESENTATION')
            cop_parti = part_b[0].strip()

            # print('CORPORATE PARTICIPANTS')
            # print(cop_parti)
            # print('CONFERENCE CALL PARTICIPANTS')
            # print(conf_parti)
            cop_parti_list = cop_parti.split('\n')

            # print(cop_parti_list)
            # print(conf_parti_list)
            all_participants.extend(cop_parti_list)




    if('PRESENTATION' in full_text and 'QUESTIONS AND ANSWERS' in full_text):
        presentation_first = full_text.split('PRESENTATION')[1]
        body = presentation_first.split('QUESTIONS AND ANSWERS')
        presentation_body= body[0]
        pb = presentation_body

        # emotion_profile_pb = emo_detecct_document(pb)

        # e_p_presentation_body = emotion_profile_pb
        qa_body = body[1].split('DISCLAIMER')[0]
        qab = qa_body

        # emotion_profile_qab = emo_detecct_document(qab)

        # e_p_qa = emotion_profile_qab
        print('presentation body>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(presentation_body[:20])
        print('qa body>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(qa_body[:20])

        print('locating people in the presentation body')
        occurances = []
        for p in all_participants:
            # print(p)
            if p in presentation_body:
                # print(p)
                occ_list = [m.start() for m in re.finditer(p, presentation_body)]
                # print(presentation_body.find(p))
                if (p == 'Operator'):
                    occurances.append([occ_list[0],p])
                else:
                    for each_o in occ_list:
                        occurances.append([each_o,p])
        occurances = sorted(occurances, key=lambda x: x[0])
        occurances.append([len(presentation_body),'End'])


        for i in range(len(occurances)-1):
            # print('>>>>>>>>>>>>>>>>>')
            # print(occurances[i],occurances[i+1])
            body_part = presentation_body[occurances[i][0]:occurances[i+1][0]]
            # print(body_part)
            text_1 = body_part

            emotion_profile_out= emo_detect_document_lnm(text_1,tokenizer,model,1,df)
            emotion_profile = emotion_profile_out[0]

            # emotion_profile = emo_detecct_document(text_1)
            print('#segs,segs',emotion_profile_out[1:])
            pres_segments.append([occurances[i][1]]+[[emotion_profile]]+[emotion_profile_out[1:]])
            emotion_profiles_for_presentation_segments.append(emotion_profile)



        # print(occurances)

        print('locating people in the qa body')
        qa_occurances = []
        for p in all_participants:
            # print(p)
            if p in qa_body:
                # print(p)
                qa_occ_list = [m.start() for m in re.finditer(p, qa_body)]
                # print(presentation_body.find(p))
                if (p == 'Operator'):
                    continue
                else:
                    for each_o in qa_occ_list:
                        qa_occurances.append([each_o, p])
        qa_occurances = sorted(qa_occurances, key=lambda x: x[0])
        qa_occurances.append([len(qa_body), 'End'])


        for i in range(len(qa_occurances) - 1):
            # print('>>>>>>>>>>>>>>>>>')
            # print(qa_occurances[i], qa_occurances[i + 1])
            qa_body_part = qa_body[qa_occurances[i][0]:qa_occurances[i + 1][0]]
            # print(qa_body_part)
            text_1 = qa_body_part

            emotion_profile_out = emo_detect_document_lnm(text_1,tokenizer,model,1,df)
            emotion_profile = emotion_profile_out[0]
            # emotion_profile = emo_detecct_document(text_1)
            qa_segments.append(qa_occurances[i] + [emotion_profile] + [emotion_profile_out[1:]])




            emotion_profiles_for_qa_segments.append(emotion_profile)
    elif('PRESENTATION' in full_text):
        presentation_first = full_text.split('PRESENTATION')[1]
        body = presentation_first.split('DISCLAIMER')
        presentation_body = body[0]
        pb = presentation_body

        # emotion_profile_pb = emo_detecct_document(pb)

        # e_p_presentation_body = emotion_profile_pb
        qa_body = ''
        qab = qa_body

        # emotion_profile_qab = emo_detecct_document(qab)

        # e_p_qa = emotion_profile_qab
        print('presentation body>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(presentation_body[:20])
        print('qa body>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(qa_body[:20])

        print('locating people in the presentation body')
        occurances = []
        for p in all_participants:
            # print(p)
            if p in presentation_body:
                # print(p)
                occ_list = [m.start() for m in re.finditer(p, presentation_body)]
                # print(presentation_body.find(p))
                if (p == 'Operator'):
                    occurances.append([occ_list[0], p])
                else:
                    for each_o in occ_list:
                        occurances.append([each_o, p])
        occurances = sorted(occurances, key=lambda x: x[0])
        occurances.append([len(presentation_body), 'End'])

        for i in range(len(occurances) - 1):
            # print('>>>>>>>>>>>>>>>>>')
            # print(occurances[i],occurances[i+1])
            body_part = presentation_body[occurances[i][0]:occurances[i + 1][0]]
            # print(body_part)
            text_1 = body_part

            emotion_profile_out = emo_detect_document_lnm(text_1, tokenizer, model, 1, df)
            emotion_profile = emotion_profile_out[0]

            # emotion_profile = emo_detecct_document(text_1)
            print('#segs,segs', emotion_profile_out[1:])
            pres_segments.append([occurances[i][1]] + [[emotion_profile]] + [emotion_profile_out[1:]])
            emotion_profiles_for_presentation_segments.append(emotion_profile)

        # print(occurances)

        print('locating people in the qa body')
        qa_occurances = []
        for p in all_participants:
            # print(p)
            if p in qa_body:
                # print(p)
                qa_occ_list = [m.start() for m in re.finditer(p, qa_body)]
                # print(presentation_body.find(p))
                if (p == 'Operator'):
                    continue
                else:
                    for each_o in qa_occ_list:
                        qa_occurances.append([each_o, p])
        qa_occurances = sorted(qa_occurances, key=lambda x: x[0])
        qa_occurances.append([len(qa_body), 'End'])

        for i in range(len(qa_occurances) - 1):
            # print('>>>>>>>>>>>>>>>>>')
            # print(qa_occurances[i], qa_occurances[i + 1])
            qa_body_part = qa_body[qa_occurances[i][0]:qa_occurances[i + 1][0]]
            # print(qa_body_part)
            text_1 = qa_body_part

            emotion_profile_out = emo_detect_document_lnm(text_1, tokenizer, model, 1, df)
            emotion_profile = emotion_profile_out[0]
            # emotion_profile = emo_detecct_document(text_1)
            qa_segments.append(qa_occurances[i] + [emotion_profile] + [emotion_profile_out[1:]])

            emotion_profiles_for_qa_segments.append(emotion_profile)
    pdf.close()
    # 2010 - Apr - 01 - DG.N - 139524928291 - transcript
    pdf_f_name = f_path.split('//')[-1]
    fname_meta = pdf_f_name.split('-')
    company_ticker = fname_meta[3]
    event_date =('-').join(fname_meta[:3])



    ceo_presentation = []
    other_man_presentation = []

    for each_seg_p in pres_segments:
        if('operator' in each_seg_p[0].lower()):continue
        elif(('ceo' in each_seg_p[0].lower()) or ('chairman' in each_seg_p[0].lower())):
            ceo_presentation.append(each_seg_p)
        else:
            other_man_presentation.append(each_seg_p)
    # print('ceo_pres',ceo_presentation)
    ceo_pp_ep = summon_profiles([i[1][0] for i in ceo_presentation])
    other_man_pp_ep = summon_profiles([i[1][0] for i in other_man_presentation])

    ceo_qna = []
    analyst_qna = []
    other_man_qna = []
    for each_seg_qna in qa_segments:
        if ('operator' in each_seg_qna[1].lower()):
            continue
        elif (('ceo' in each_seg_qna[1].lower()) or ('chairman' in each_seg_qna[1].lower())):
            ceo_qna.append(each_seg_qna)
        if ('analyst' in each_seg_qna[1].lower()):
            analyst_qna.append(each_seg_qna)
        else:
            other_man_qna.append(each_seg_qna)
    # print('ceo_qa',ceo_qna)
    ceo_qa_ep = summon_profiles([i[2] for i in ceo_qna])
    analyst_qa_ep = summon_profiles([i[2] for i in analyst_qna])
    other_man_qa_ep = summon_profiles([i[2] for i in other_man_qna])

    processed_data['pdf'] = pdf_f_name
    processed_data['company_ticker'] = company_ticker
    processed_data['event_date'] = event_date
    processed_data['full_text'] = full_text
    processed_data['participants'] = all_participants
    processed_data['presentation_body'] = presentation_body
    processed_data['qa_body'] = qa_body
    processed_data['presentation_segments'] = pres_segments
    processed_data['presentation_CEO_segs'] = ceo_presentation
    processed_data['presentation_other_man_segs'] = other_man_presentation
    processed_data['presentation_CEO'] = ceo_pp_ep
    processed_data['presentation_other_man'] = other_man_pp_ep
    processed_data['e_p_pb'] = sum_up_dicts(emotion_profiles_for_presentation_segments)
    processed_data['e_p_qa'] = sum_up_dicts(emotion_profiles_for_qa_segments)
    processed_data['qa_segments'] = qa_segments
    processed_data['qa_CEO_segs'] = ceo_qna
    processed_data['qa_analyst_segs'] = analyst_qna
    processed_data['qa_other_man_segs'] = other_man_qna
    processed_data['qa_CEO'] = ceo_qa_ep
    processed_data['qa_analyst'] = analyst_qa_ep
    processed_data['qa_other_man'] = other_man_qa_ep
    processed_data['emotion_profiles_pres'] = emotion_profiles_for_presentation_segments
    processed_data['emotion_profiles_qa'] = emotion_profiles_for_qa_segments
    processed_data['comp_name']= comp_name
    processed_data['year'] = year_cv
    processed_data['quarter'] = qtr_cv
    print(processed_data)
    return processed_data

def run_main(subfolder,start_and_end):
    import pandas as pd
    model_path = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\Finetuned_Langue_Models\DistilBERT_GoEmotions_Finetuned"
    # vocab_path = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\Vocabularies\lnm_vocab_even.csv"
    # vocab_path = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\Vocabularies\lnm_default_vocab.csv"
    # vocab_path = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\Vocabularies\lnm_stemmed_vocab.csv"
    # vocab_path = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\Vocabularies\lnm_vocab_even_new.csv"
    vocab_path = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\Vocabularies\plutchik_with_emobert_vocab.csv"
    tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
    model = AutoModel.from_pretrained(model_path)

    df = pd.read_csv(vocab_path)
    df = df.dropna()
    df['embedding'] = [ast.literal_eval(i) for i in df['embedding'].values.tolist()]

    # print(
    #     build_profile('This person is good', 1, df, tokenizer, model, keyword_extraction=True, modifier_detection=True))
    # print(build_profile('This person very is good', 1, df, tokenizer, model, keyword_extraction=True,
    #                     modifier_detection=True))

    s_e_f = subfolder
    # pdf_list = os.listdir("/content/drive/MyDrive/Earning Calls/2011 Jul to Dec")
    pdf_list = os.listdir(r"E:\Data\Emotion_detection_gihan\CEO emotions projects//" + s_e_f + "//")
    pdf_list = sorted(pdf_list)
    print(len(pdf_list))

    fil = pd.read_csv(
        r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\filtered_reports\filtered_reports.csv")
    filtered_pdf_list = fil['pdf'].tolist()

    f = open('errors.txt', 'w')
    s_e = start_and_end
    s_e = s_e.split('_')

    # s_e = s_e.split('_')
    import pandas as pd

    is_file_already = os.path.isfile(
        r'E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks/results_unprocessed_lnm_transcripts_' + str(
            s_e_f) + '_' + str(s_e[0]) + '_' + str(s_e[1]) + '.csv')
    completed_pdfs = []
    if (is_file_already):
        print('file is already there..')
        print('existing file name'+' '+r'E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks/results_unprocessed_lnm_transcripts_' + str(
                    s_e_f) + '_' + str(s_e[0]) + '_' + str(s_e[1]) + '.csv')
        try:
            dffff = pd.read_csv(
                r'E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks/results_unprocessed_lnm_transcripts_' + str(
                    s_e_f) + '_' + str(s_e[0]) + '_' + str(s_e[1]) + '.csv')
            completed_pdfs = dffff['pdf'].to_list()
            print(completed_pdfs)
            print(len(completed_pdfs))
        except pandas.errors.EmptyDataError:
            print('dataframe is still empty')

    with open(
            r'E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks//results_unprocessed_lnm_transcripts_' + str(
                    s_e_f) + '_' + str(s_e[0]) + '_' + str(s_e[1]) + '.csv', mode='a+', newline='',
            encoding='utf-8') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if (not is_file_already):
            employee_writer.writerow(['pdf',
                                      'company_ticker',
                                      'event_date',
                                      'presentation_CEO_segs',
                                      'presentation_other_man_segs',
                                      'presentation_CEO',
                                      'presentation_other_man',
                                      'qa_CEO_segs',
                                      'qa_analyst_segs',
                                      'qa_other_man_segs',
                                      'qa_CEO',
                                      'qa_analyst',
                                      'qa_other_man',
                                      'participants', '#presentation_body', '#qa_body', 'presentation_all_e_p',
                                      'qa_all_e_p', '#presentation_segments', '#qa_segments', 'presentation_segments',
                                      'qa_segments', 'e_p_pres', 'e_p_qa', "year", "quarter", "comp_name"])

        i = 0
        pdf_list = [i for i in pdf_list[int(s_e[0]):int(s_e[1])] if i not in completed_pdfs]
        print(len(pdf_list))
        for each_file in pdf_list:

            if(each_file not in filtered_pdf_list):
                print(each_file,'not in filtered list')
                continue
            else:
                print(each_file, 'in filtered list')


            tt1 = datetime.now()
            i = i + 1
            print(str(i) + ' out of ' + str(len(pdf_list)))
            if (each_file in ['2011-Aug-03-BEN.N-140511442202-transcript.pdf',
                              '2011-Aug-05-ATO.N-137689101588-transcript.pdf',
                             ]): continue
            path_pdf = os.path.join(
                r"E:\Data\Emotion_detection_gihan\CEO emotions projects//" + s_e_f + "//", each_file)
            print(path_pdf)
            try:
                output = process_pdf(path_pdf, df, tokenizer,model)
                # employee_writer.writerow([str(output['pdf']),str(output['participants']),str(output['presentation_body']),str(output['qa_body']),str(output['presentation_segments']),str(output['qa_segments'])])

                employee_writer.writerow([str(output['pdf']),
                                          str(output['company_ticker']),
                                          str(output['event_date']),
                                          str(output['presentation_CEO_segs']),
                                          str(output['presentation_other_man_segs']),
                                          str(output['presentation_CEO']),
                                          str(output['presentation_other_man']),
                                          str(output['qa_CEO_segs']),
                                          str(output['qa_analyst_segs']),
                                          str(output['qa_other_man_segs']),
                                          str(output['qa_CEO']),
                                          str(output['qa_analyst']),
                                          str(output['qa_other_man']),
                                          str(output['participants']), [len(output['presentation_body'])],
                                          [len(output['qa_body'])], output['e_p_pb'], output['e_p_qa'],
                                          [len(output['presentation_segments'])], [len(output['qa_segments'])],
                                          output['presentation_segments'], output['qa_segments'],
                                          output['emotion_profiles_pres'], output['emotion_profiles_qa'],
                                          output["year"], output["quarter"], output["comp_name"]])
            # except Exception as e:
            #     print(e)
            #     f.write(str(path_pdf) + '\n')
            except SyntaxError:
              print('s')
            tt2 = datetime.now()
            diff = tt2 - tt1
            print('time', diff)

            # if(i==1):break

    employee_file.close()
    f.close()
if __name__ == '__main__':

    # df = pd.read_csv(r"E:\Projects\emo_detector_new\vocabs\lnm_vocab_final.csv")
    # df = pd.read_csv(r"E:\Projects\emo_detector_new\vocabs\lnm_vocab_even.csv")

    model_path = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\Finetuned_Langue_Models\DistilBERT_GoEmotions_Finetuned"
    # vocab_path = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\Vocabularies\lnm_vocab_even.csv"
    vocab_path = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\Vocabularies\plutchik_with_emobert_vocab.csv"

    tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
    model = AutoModel.from_pretrained(model_path)

    df = pd.read_csv(vocab_path)
    df = df.dropna()
    df['embedding'] = [ast.literal_eval(i) for i in df['embedding'].values.tolist()]

    # print(
    #     build_profile('This person is good', 1, df, tokenizer, model, keyword_extraction=True, modifier_detection=True))
    # print(build_profile('This person very is good', 1, df, tokenizer, model, keyword_extraction=True,
    #                     modifier_detection=True))

    s_e_f = input('subfolder: ')
    # pdf_list = os.listdir("/content/drive/MyDrive/Earning Calls/2011 Jul to Dec")
    pdf_list = os.listdir(r"E:\Data\Emotion_detection_gihan\CEO emotions projects//" + s_e_f + "//")
    pdf_list = sorted(pdf_list)
    print(len(pdf_list))
    f = open('errors.txt', 'w')
    s_e = input('start and end: ')
    s_e = s_e.split('_')

    # s_e = s_e.split('_')
    import pandas as pd

    is_file_already = os.path.isfile(
        r'E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks/results_unprocessed_lnm_transcripts_' + str(
            s_e_f) + '_' + str(s_e[0]) + '_' + str(s_e[1]) + '.csv')
    completed_pdfs = []
    if (is_file_already):
        print('file is already there..')
        dffff = pd.read_csv(
            r'E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks/results_unprocessed_lnm_transcripts_' + str(
                s_e_f) + '_' + str(s_e[0]) + '_' + str(s_e[1]) + '.csv')
        completed_pdfs = dffff['pdf'].to_list()
        print(completed_pdfs)
        print(len(completed_pdfs))

    with open(r'E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks/results_unprocessed_lnm_transcripts_' + str(
            s_e_f) + '_' + str(s_e[0]) + '_' + str(s_e[1]) + '.csv', mode='a+', newline='',
              encoding='utf-8') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if (not is_file_already):
            employee_writer.writerow(['pdf',
                                      'company_ticker',
                                      'event_date',
                                      'presentation_CEO_segs',
                                      'presentation_other_man_segs',
                                      'presentation_CEO',
                                      'presentation_other_man',
                                      'qa_CEO_segs',
                                      'qa_analyst_segs',
                                      'qa_other_man_segs',
                                      'qa_CEO',
                                      'qa_analyst',
                                      'qa_other_man',
                                      'participants', '#presentation_body', '#qa_body', 'presentation_all_e_p',
                                      'qa_all_e_p', '#presentation_segments', '#qa_segments', 'presentation_segments',
                                      'qa_segments', 'e_p_pres', 'e_p_qa', "year", "quarter", "comp_name"])

        i = 0
        pdf_list = [i for i in pdf_list[int(s_e[0]):int(s_e[1])] if i not in completed_pdfs]
        print(len(pdf_list))
        for each_file in pdf_list:
            tt1 = datetime.now()
            i = i + 1
            print(str(i) + ' out of ' + str(len(pdf_list)))
            if (each_file in ['2011-Aug-03-BEN.N-140511442202-transcript.pdf',
                              '2011-Aug-05-ATO.N-137689101588-transcript.pdf',
                              '2011-Aug-16-WMT.N-139819905465-transcript.pdf']): continue
            path_pdf = os.path.join(
                r"E:\Data\Emotion_detection_gihan\CEO emotions projects//" + s_e_f + "//", each_file)
            print(path_pdf)
            try:
                output = process_pdf(path_pdf, df, tokenizer,model)
                # employee_writer.writerow([str(output['pdf']),str(output['participants']),str(output['presentation_body']),str(output['qa_body']),str(output['presentation_segments']),str(output['qa_segments'])])

                employee_writer.writerow([str(output['pdf']),
                                          str(output['company_ticker']),
                                          str(output['event_date']),
                                          str(output['presentation_CEO_segs']),
                                          str(output['presentation_other_man_segs']),
                                          str(output['presentation_CEO']),
                                          str(output['presentation_other_man']),
                                          str(output['qa_CEO_segs']),
                                          str(output['qa_analyst_segs']),
                                          str(output['qa_other_man_segs']),
                                          str(output['qa_CEO']),
                                          str(output['qa_analyst']),
                                          str(output['qa_other_man']),
                                          str(output['participants']), [len(output['presentation_body'])],
                                          [len(output['qa_body'])], output['e_p_pb'], output['e_p_qa'],
                                          [len(output['presentation_segments'])], [len(output['qa_segments'])],
                                          output['presentation_segments'], output['qa_segments'],
                                          output['emotion_profiles_pres'], output['emotion_profiles_qa'],
                                          output["year"], output["quarter"], output["comp_name"]])
            except Exception:
                f.write(str(path_pdf) + '\n')
            # except SyntaxError:
            #   print('s')
            tt2 = datetime.now()
            diff = tt2 - tt1
            print('time', diff)

            # if(i==1):break

    employee_file.close()
    f.close()