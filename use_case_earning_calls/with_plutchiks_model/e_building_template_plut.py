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

  joy,sad,anger,trust,anticipation,fear,surprise,disgust = [],[],[],[],[],[],[],[]
  for i,row in df.iterrows():

    total_pr  = ast.literal_eval(row[feature])
    print(total_pr)

    if ( len(total_pr.keys() ) == 0 ):
      joy.append(0)
      sad.append(0)
      anger.append(0)
      trust.append(0)
      anticipation.append(0)
      disgust.append(0)
      surprise.append(0)
      fear.append(0)

    else:
      if('joy' in total_pr.keys()):
        joy.append(total_pr['joy'])
      else:joy.append(0)

      if('sad' in total_pr.keys()):
        sad.append(total_pr['sad'])
      else:sad.append(0)

      if('fear' in total_pr.keys()):
        fear.append(total_pr['fear'])
      else:fear.append(0)

      if('anticipation' in total_pr.keys()):
        anticipation.append(total_pr['anticipation'])
      else:anticipation.append(0)

      if('disgust' in total_pr.keys()):
        disgust.append(total_pr['disgust'])
      else:disgust.append(0)

      if('surprise' in total_pr.keys()):
        surprise.append(total_pr['surprise'])
      else:surprise.append(0)

      if ('anger' in total_pr.keys()):
        anger.append(total_pr['anger'])
      else:
        anger.append(0)

      if ('trust' in total_pr.keys()):
        trust.append(total_pr['trust'])
      else:
        trust.append(0)




      # neg.append(total_pr['negative'])
      # st.append(total_pr['model_strong'])
      # wk.append(total_pr['model_weak'])
      # lit.append(total_pr['litigious'])
      # unc.append(total_pr['sad'])

  return {'anger':anger,'trust':trust,'joy':joy,'sad':sad,'fear':fear,'anticipation':anticipation,'disgust':disgust,'surprise':surprise}


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
    total_pr = {'anger':'','trust':'','joy':'','sad':'','fear':'','anticipation':'','disgust':'','surprise':''}
  new_df['Total_Presentation_anger'] = total_pr['anger']
  new_df['Total_Presentation_trust'] = total_pr['trust']
  new_df['Total_Presentation_joy'] = total_pr['joy']
  new_df['Total_Presentation_sad'] = total_pr['sad']
  new_df['Total_Presentation_fear'] = total_pr['fear']
  new_df['Total_Presentation_anticipation'] = total_pr['anticipation']
  new_df['Total_Presentation_disgust'] = total_pr['disgust']
  new_df['Total_Presentation_surprise'] = total_pr['surprise']

  try:
    total_pr = split_to_cols('presentation_CEO',df)
  except  Exception:
    total_pr = {'anger':'','trust':'','joy':'','sad':'','fear':'','anticipation':'','disgust':'','surprise':''}
  new_df['CEO_Presentation_anger'] = total_pr['anger']
  new_df['CEO_Presentation_trust'] = total_pr['trust']
  new_df['CEO_Presentation_joy'] = total_pr['joy']
  new_df['CEO_Presentation_sad'] = total_pr['sad']
  new_df['CEO_Presentation_fear'] = total_pr['fear']
  new_df['CEO_Presentation_anticipation'] = total_pr['anticipation']
  new_df['CEO_Presentation_disgust'] = total_pr['disgust']
  new_df['CEO_Presentation_surprise'] = total_pr['surprise']

  try:
    total_pr = split_to_cols('presentation_other_man',df)
  except  Exception:
    total_pr = {'anger':'','trust':'','joy':'','sad':'','fear':'','anticipation':'','disgust':'','surprise':''}
  new_df['OtherManagers_Presentation_anger'] = total_pr['anger']
  new_df['OtherManagers_Presentation_trust'] = total_pr['trust']
  new_df['OtherManagers_Presentation_joy'] = total_pr['joy']
  new_df['OtherManagers_Presentation_sad'] = total_pr['sad']
  new_df['OtherManagers_Presentation_fear'] = total_pr['fear']
  new_df['OtherManagers_Presentation_anticipation'] = total_pr['anticipation']
  new_df['OtherManagers_Presentation_disgust'] = total_pr['disgust']
  new_df['OtherManagers_Presentation_surprise'] = total_pr['surprise']

  try:
    total_pr = split_to_cols('qa_all_e_p',df)
    print('sss',total_pr)
  except  Exception:
    print('error')
    total_pr = {'anger':'','trust':'','joy':'','sad':'','fear':'','anticipation':'','disgust':'','surprise':''}
  new_df['Total_Q&A_anger'] = total_pr['anger']
  new_df['Total_Q&A_trust'] = total_pr['trust']
  new_df['Total_Q&A_joy'] = total_pr['joy']
  new_df['Total_Q&A_sad'] = total_pr['sad']
  new_df['Total_Q&A_fear'] = total_pr['fear']
  new_df['Total_Q&A_anticipation'] = total_pr['anticipation']
  new_df['Total_Q&A_disgust'] = total_pr['disgust']
  new_df['Total_Q&A_surprise'] = total_pr['surprise']

  try:
    total_pr = split_to_cols('qa_CEO',df)
  except  Exception:
    total_pr = {'anger':'','trust':'','joy':'','sad':'','fear':'','anticipation':'','disgust':'','surprise':''}
  new_df['CEO_Q&A_anger'] = total_pr['anger']
  new_df['CEO_Q&A_trust'] = total_pr['trust']
  new_df['CEO_Q&A_joy'] = total_pr['joy']
  new_df['CEO_Q&A_sad'] = total_pr['sad']
  new_df['CEO_Q&A_fear'] = total_pr['fear']
  new_df['CEO_Q&A_anticipation'] = total_pr['anticipation']
  new_df['CEO_Q&A_disgust'] = total_pr['disgust']
  new_df['CEO_Q&A_surprise'] = total_pr['surprise']

  try:
    total_pr = split_to_cols('qa_other_man',df)
  except  Exception:
    total_pr = {'anger':'','trust':'','joy':'','sad':'','fear':'','anticipation':'','disgust':'','surprise':''}
  new_df['OtherManagers_Q&A_anger'] = total_pr['anger']
  new_df['OtherManagers_Q&A_trust'] = total_pr['trust']
  new_df['OtherManagers_Q&A_joy'] = total_pr['joy']
  new_df['OtherManagers_Q&A_sad'] = total_pr['sad']
  new_df['OtherManagers_Q&A_fear'] = total_pr['fear']
  new_df['OtherManagers_Q&A_anticipation'] = total_pr['anticipation']
  new_df['OtherManagers_Q&A_disgust'] = total_pr['disgust']
  new_df['OtherManagers_Q&A_surprise'] = total_pr['surprise']

  try:
    total_pr = split_to_cols('qa_analyst',df)
  except  Exception:
    total_pr = {'anger':'','trust':'','joy':'','sad':'','fear':'','anticipation':'','disgust':'','surprise':''}
  new_df['AllAnalysts_Q&A_anger'] = total_pr['anger']
  new_df['AllAnalysts_Q&A_trust'] = total_pr['trust']
  new_df['AllAnalysts_Q&A_joy'] = total_pr['joy']
  new_df['AllAnalysts_Q&A_sad'] = total_pr['sad']
  new_df['AllAnalysts_Q&A_fear'] = total_pr['fear']
  new_df['AllAnalysts_Q&A_anticipation'] = total_pr['anticipation']
  new_df['AllAnalysts_Q&A_disgust'] = total_pr['disgust']
  new_df['AllAnalysts_Q&A_surprise'] = total_pr['surprise']

  print(new_df.columns)
  new_df.to_csv(out_root+f_name, index=False)


dir_list = ['2010 Jan to Jun', '2010 Jul to Dec', '2011 Jan to Jun', '2011 Jul to Dec', '2012 Jan to Jun', '2012 Jul to Dec', '2013 Jan to Jun', '2013 Jul to Dec', '2014 Jan to Jun', '2014 Jul to Dec', '2015 Jan to Jun', '2015 Jul to Dec', '2016 Jan to Jun', '2016 Jul to Dec', '2017 Jan to Jun', '2017 Jul to Dec', '2018 Jan to Jun', '2019 Jan to Jun', '2019 Jul to Dec', '2020 Jan to Jun', '2020 Jul to Dec']
splits = ['0_300','300_800']
print(dir_list)

in_root = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_averaged\\"
out_root = r"E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa\use_case_earning_calls\unprocessed_results\with_plutchiks_templated\\"


# i='2017 Jul to Dec'
# j = "0_300"
# make_template("results_unprocessed_lnm_transcripts_"+str(i)+"_"+str(j)+".csv", in_root, out_root)
make_template("results_unprocessed_lnm_transcripts_left_0_20.csv", in_root, out_root)

# for i in dir_list:
#     for j in splits:
#
#         f_name = "results_unprocessed_lnm_transcripts_"+str(i)+"_"+str(j)+".csv"
#         print(f_name)
#         make_template(f_name, in_root, out_root)
