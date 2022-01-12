import pandas as pd

dir_list = ['2010 Jan to Jun', '2010 Jul to Dec', '2011 Jan to Jun', '2011 Jul to Dec', '2012 Jan to Jun', '2012 Jul to Dec', '2013 Jan to Jun', '2013 Jul to Dec', '2014 Jan to Jun', '2014 Jul to Dec', '2015 Jan to Jun', '2015 Jul to Dec', '2016 Jan to Jun', '2016 Jul to Dec', '2017 Jan to Jun', '2017 Jul to Dec', '2018 Jan to Jun', '2019 Jan to Jun', '2019 Jul to Dec', '2020 Jan to Jun', '2020 Jul to Dec']
# run_main('left','0_20')
splits = ['0_300','300_800']
print(dir_list)
# run_main('2010 Jan to Jun','0_5')

for i in dir_list:
    for j in splits:
        print(i,j)
        s_e_f = i
        s_e = j
        s_e = s_e.split('_')
        dffff = pd.read_csv(
            r'E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks/results_unprocessed_lnm_transcripts_' + str(
                s_e_f) + '_' + str(s_e[0]) + '_' + str(s_e[1]) + '.csv')
        cols = dffff.columns
        print(len(cols))
        try:
            completed_pdfs = dffff['pdf'].to_list()
            # print(completed_pdfs)
            # print(len(completed_pdfs))
        except KeyError:
            cols_l =  ['pdf', 'company_ticker', 'event_date', 'presentation_CEO_segs',
       'presentation_other_man_segs', 'presentation_CEO',
       'presentation_other_man', 'qa_CEO_segs', 'qa_analyst_segs',
       'qa_other_man_segs', 'qa_CEO', 'qa_analyst', 'qa_other_man',
       'participants', '#presentation_body', '#qa_body',
       'presentation_all_e_p', 'qa_all_e_p', '#presentation_segments',
       '#qa_segments', 'presentation_segments', 'qa_segments', 'e_p_pres',
       'e_p_qa', 'year', 'quarter', 'comp_name']
            dffff.columns = cols_l
            print(len(cols_l))
            print(dffff.iloc[:, 0])
            print(r'E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks/results_unprocessed_lnm_transcripts_' + str(
                s_e_f) + '_' + str(s_e[0]) + '_' + str(s_e[1]) + '.csv')
            dffff.to_csv(r'E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks/results_unprocessed_lnm_transcripts_' + str(
                s_e_f) + '_' + str(s_e[0]) + '_' + str(s_e[1]) + '.csv', index=False)