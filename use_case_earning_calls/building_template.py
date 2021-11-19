# from google.colab import drive
import os
# drive.mount('/content/drive')
import pandas as pd

# slice_unit = "2013 Jan to Jun"
# slice_unit = "2020 Jul to Dec"

# path = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\results_unprocessed_lnm_transcripts_2010 Jan to Jun_0_300.csv"
# col_list= ['pdf', 'company_ticker', 'event_date', 'presentation_CEO_segs',
#        'presentation_other_man_segs', 'presentation_CEO',
#        'presentation_other_man', 'qa_CEO_segs', 'qa_analyst_segs',
#        'qa_other_man_segs', 'qa_CEO', 'qa_analyst', 'qa_other_man','participants',
#        '#presentation_body', '#qa_body', 'presentation_all_e_p', 'qa_all_e_p',
#        '#presentation_segments', '#qa_segments', 'presentation_segments',
#        'qa_segments', 'e_p_pres', 'e_p_qa', 'year', 'quarter', 'comp_name']
# df = pd.read_csv(path)
# df = df.iloc[1:]
# df.to_csv(path)
# df = pd.read_csv(path,header=None)
# df.columns = ['pdf', 'company_ticker', 'event_date', 'presentation_CEO_segs',
#        'presentation_other_man_segs', 'presentation_CEO',
#        'presentation_other_man', 'qa_CEO_segs', 'qa_analyst_segs',
#        'qa_other_man_segs', 'qa_CEO', 'qa_analyst', 'qa_other_man','participants',
#        '#presentation_body', '#qa_body', 'presentation_all_e_p', 'qa_all_e_p',
#        '#presentation_segments', '#qa_segments', 'presentation_segments',
#        'qa_segments', 'e_p_pres', 'e_p_qa', 'year', 'quarter', 'comp_name']
# print(df.head())
# print(df.columns)
# completed_pdfs =  df.index.to_list()
# completed_pdfs =  df['pdf'].to_list()
# for k in completed_pdfs:
#   print(k)
# dir_path = r"/content/drive/Shareddrives/Earning_calls/CEO emotions projects/"+str(slice_unit)
# files_list = os.listdir(dir_path)

# newlist = []
# for names in files_list:
#     if names.endswith(".pdf"):
#         newlist.append(names)
# files_list = newlist
#
# print(files_list)
# print(completed_pdfs)
#
# left_pdfs = [i for i in files_list if i not in completed_pdfs]
# print(len(left_pdfs))
# print(left_pdfs)


# df.head()



# print(df.columns)
import ast

def split_to_cols(feature,df):

  pos,neg,st,wk,lit,unc = [],[],[],[],[],[]
  for i,row in df.iterrows():

    total_pr  = ast.literal_eval(row[feature])
    print(total_pr)

    if ( len(total_pr.keys() ) == 0 ):
      pos.append(0)
      neg.append(0)
      st.append(0)
      wk.append(0)
      lit.append(0)
      unc.append(0)

    else:
      if('positive' in total_pr.keys()):
        pos.append(total_pr['positive'])
      else:pos.append(0)

      if('negative' in total_pr.keys()):
        neg.append(total_pr['negative'])
      else:neg.append(0)

      if('model_strong' in total_pr.keys()):
        st.append(total_pr['model_strong'])
      else:st.append(0)

      if('model_weak' in total_pr.keys()):
        wk.append(total_pr['model_weak'])
      else:wk.append(0)

      if('litigious' in total_pr.keys()):
        lit.append(total_pr['litigious'])
      else:lit.append(0)

      if('uncertainty' in total_pr.keys()):
        unc.append(total_pr['uncertainty'])
      else:unc.append(0)




      # neg.append(total_pr['negative'])
      # st.append(total_pr['model_strong'])
      # wk.append(total_pr['model_weak'])
      # lit.append(total_pr['litigious'])
      # unc.append(total_pr['uncertainty'])

  return {'pos':pos,'neg':neg,'lit':lit,'wk':wk,'st':st,'unc':unc}


def make_template(f_name,in_root,out_root):
  df = pd.read_csv(in_root+f_name)
  new_df = df[['pdf','company_ticker', 'year','quarter','event_date']]


  try:
    print('sss')
    for s in df['presentation_all_e_p'].to_list():
      print(s)
    print('sss')

    total_pr = split_to_cols('presentation_all_e_p',df)

  except  SyntaxError:
    total_pr = {'pos':'','neg':'','lit':'','unc':'','st':'','wk':''}
  new_df['Total_Presentation_Positive'] = total_pr['pos']
  new_df['Total_Presentation_Negative'] = total_pr['neg']
  new_df['Total_Presentation_Litigious'] = total_pr['lit']
  new_df['Total_Presentation_Uncertainty'] = total_pr['unc']
  new_df['Total_Presentation_MStrong'] = total_pr['st']
  new_df['Total_Presentation_MWeak'] = total_pr['wk']

  try:
    total_pr = split_to_cols('presentation_CEO',df)
  except  Exception:
    total_pr = {'pos':'','neg':'','lit':'','unc':'','st':'','wk':''}
  new_df['CEO_Presentation_Positive'] = total_pr['pos']
  new_df['CEO_Presentation_Negative'] = total_pr['neg']
  new_df['CEO_Presentation_Litigious'] = total_pr['lit']
  new_df['CEO_Presentation_Uncertainty'] = total_pr['unc']
  new_df['CEO_Presentation_MStrong'] = total_pr['st']
  new_df['CEO_Presentation_MWeak'] = total_pr['wk']

  try:
    total_pr = split_to_cols('presentation_other_man',df)
  except  Exception:
    total_pr = {'pos': '', 'neg': '', 'lit': '', 'unc': '', 'st': '', 'wk': ''}
  new_df['OtherManagers_Presentation_Positive'] = total_pr['pos']
  new_df['OtherManagers_Presentation_Negative'] = total_pr['neg']
  new_df['OtherManagers_Presentation_Litigious'] = total_pr['lit']
  new_df['OtherManagers_Presentation_Uncertainty'] = total_pr['unc']
  new_df['OtherManagers_Presentation_MStrong'] = total_pr['st']
  new_df['OtherManagers_Presentation_MWeak'] = total_pr['wk']

  try:
    total_pr = split_to_cols('qa_all_e_p',df)
    print('sss',total_pr)
  except  Exception:
    print('error')
    total_pr = {'pos': '', 'neg': '', 'lit': '', 'unc': '', 'st': '', 'wk': ''}
  new_df['Total_Q&A_Positive'] = total_pr['pos']
  new_df['Total_Q&A_Negative'] = total_pr['neg']
  new_df['Total_Q&A_Litigious'] = total_pr['lit']
  new_df['Total_Q&A_Uncertainty'] = total_pr['unc']
  new_df['Total_Q&A_MStrong'] = total_pr['st']
  new_df['Total_Q&A_MWeak'] = total_pr['wk']

  try:
    total_pr = split_to_cols('qa_CEO',df)
  except  Exception:
    total_pr = {'pos': '', 'neg': '', 'lit': '', 'unc': '', 'st': '', 'wk': ''}
  new_df['CEO_Q&A_Positive'] = total_pr['pos']
  new_df['CEO_Q&A_Negative'] = total_pr['neg']
  new_df['CEO_Q&A_Litigious'] = total_pr['lit']
  new_df['CEO_Q&A_Uncertainty'] = total_pr['unc']
  new_df['CEO_Q&A_MStrong'] = total_pr['st']
  new_df['CEO_Q&A_MWeak'] = total_pr['wk']

  try:
    total_pr = split_to_cols('qa_other_man',df)
  except  Exception:
    total_pr = {'pos': '', 'neg': '', 'lit': '', 'unc': '', 'st': '', 'wk': ''}
  new_df['OtherManagers_Q&A_Positive'] = total_pr['pos']
  new_df['OtherManagers_Q&A_Negative'] = total_pr['neg']
  new_df['OtherManagers_Q&A_Litigious'] = total_pr['lit']
  new_df['OtherManagers_Q&A_Uncertainty'] = total_pr['unc']
  new_df['OtherManagers_Q&A_MStrong'] = total_pr['st']
  new_df['OtherManagers_Q&A_MWeak'] = total_pr['wk']

  try:
    total_pr = split_to_cols('qa_analyst',df)
  except  Exception:
    total_pr = {'pos': '', 'neg': '', 'lit': '', 'unc': '', 'st': '', 'wk': ''}
  new_df['AllAnalysts_Q&A_Positive'] = total_pr['pos']
  new_df['AllAnalysts_Q&A_Negative'] = total_pr['neg']
  new_df['AllAnalysts_Q&A_Litigious'] = total_pr['lit']
  new_df['AllAnalysts_Q&A_Uncertainty'] = total_pr['unc']
  new_df['AllAnalysts_Q&A_MStrong'] = total_pr['st']
  new_df['AllAnalysts_Q&A_MWeak'] = total_pr['wk']

  print(new_df.columns)
  new_df.to_csv(out_root+f_name, index=False)


dir_list = ['2010 Jan to Jun', '2010 Jul to Dec', '2011 Jan to Jun', '2011 Jul to Dec', '2012 Jan to Jun', '2012 Jul to Dec', '2013 Jan to Jun', '2013 Jul to Dec', '2014 Jan to Jun', '2014 Jul to Dec', '2015 Jan to Jun', '2015 Jul to Dec', '2016 Jan to Jun', '2016 Jul to Dec', '2017 Jan to Jun', '2017 Jul to Dec', '2018 Jan to Jun', '2019 Jan to Jun', '2019 Jul to Dec', '2020 Jan to Jun', '2020 Jul to Dec']
splits = ['0_300','300_800']
print(dir_list)

in_root = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\sentence_level_averaged\\"
out_root = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\scaled\sentence_level_averaged_templated\\"


# i='2017 Jul to Dec'
# j = "0_300"
# make_template("results_unprocessed_lnm_transcripts_"+str(i)+"_"+str(j)+".csv", in_root, out_root)
make_template("results_unprocessed_lnm_transcripts_left.csv", in_root, out_root)

# for i in dir_list:
#     for j in splits:
#
#         f_name = "results_unprocessed_lnm_transcripts_"+str(i)+"_"+str(j)+".csv"
#         print(f_name)
#         make_template(f_name, in_root, out_root)
