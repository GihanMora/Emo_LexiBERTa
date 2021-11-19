import os
import pandas as pd
import csv
df1 = pd.read_csv(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\new\results_unprocessed_lnm_transcripts_2020 Jan to Jun_300_800.csv")


dir_list = ['2010 Jan to Jun', '2010 Jul to Dec', '2011 Jan to Jun', '2011 Jul to Dec', '2012 Jan to Jun', '2012 Jul to Dec', '2013 Jan to Jun', '2013 Jul to Dec', '2014 Jan to Jun', '2014 Jul to Dec', '2015 Jan to Jun', '2015 Jul to Dec', '2016 Jan to Jun', '2016 Jul to Dec', '2017 Jan to Jun', '2017 Jul to Dec', '2018 Jan to Jun', '2019 Jan to Jun', '2019 Jul to Dec', '2020 Jan to Jun', '2020 Jul to Dec']
splits = ['0_300','300_800']
print(dir_list)

for fn in dir_list:
    for j in splits:
        print(fn,j)
        # print(r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\new\results_unprocessed_lnm_transcripts_"+str(i)+"_"+str(j)+".csv")
        # path = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\new\results_unprocessed_lnm_transcripts_"+str(fn)+"_"+str(j)+".csv"
        out_path = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\line_out_fixed\results_unprocessed_lnm_transcripts_"+str(fn)+"_"+str(j)+".csv"

        df = pd.read_csv(out_path)

        cols = df.columns
        # print(out_path)
        # print(len(cols))
        # print(df.columns)
        # print(df.index.name)

        if(len(cols)==28):
            # df.rename( columns={'Unnamed: 0':'id'}, inplace=True )
            # print(df.columns)
            print(out_path)
            # df.drop('id',axis=1,inplace=True)
            # df.to_csv(out_path, index=False)
            # print(df[df.columns[0]])

            # print(df)
            # print(len(list(set(df['pdf']))))

            # for i,row in df.iterrows():
            #     # print(row[0])
            #     if('.pdf' in row[0]):
            #         # print(len(row))
            #         df.loc[i,:] = [i]+row.to_list()[:27]
            #     # print(row[0])
    #         break
    # break

        # df.to_csv(out_path, index=False)
        # if(cols[0:2]!='pdf'):
            # print(cols[0])
            # print(len(cols))

       #      print(len(['pdf', 'company_ticker', 'event_date', 'presentation_CEO_segs',
       # 'presentation_other_man_segs', 'presentation_CEO',
       # 'presentation_other_man', 'qa_CEO_segs', 'qa_analyst_segs',
       # 'qa_other_man_segs', 'qa_CEO', 'qa_analyst', 'qa_other_man',
       # 'participants', '#presentation_body', '#qa_body',
       # 'presentation_all_e_p', 'qa_all_e_p', '#presentation_segments',
       # '#qa_segments', 'presentation_segments', 'qa_segments', 'e_p_pres',
       # 'e_p_qa', 'year', 'quarter', 'comp_name']))

       #      df.columns = ['pdf', 'company_ticker', 'event_date', 'presentation_CEO_segs',
       # 'presentation_other_man_segs', 'presentation_CEO',
       # 'presentation_other_man', 'qa_CEO_segs', 'qa_analyst_segs',
       # 'qa_other_man_segs', 'qa_CEO', 'qa_analyst', 'qa_other_man',
       # 'participants', '#presentation_body', '#qa_body',
       # 'presentation_all_e_p', 'qa_all_e_p', '#presentation_segments',
       # '#qa_segments', 'presentation_segments', 'qa_segments', 'e_p_pres',
       # 'e_p_qa', 'year', 'quarter', 'comp_name']
            # print(df.head())


            # df.to_csv(path)
            # with open(path, mode='a+', newline='', encoding='utf-8') as employee_file:
            #     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
