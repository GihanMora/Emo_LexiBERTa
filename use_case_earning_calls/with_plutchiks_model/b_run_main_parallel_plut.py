import sys
import pandas as pd
sys.path.append('E:\Projects\Emotion_work_Gihan\Emo_LexiBERTa')
from use_case_earning_calls.with_plutchiks_model.a_profile_builder_plut import run_main
import os
from multiprocessing import Process
import subprocess
# run_main('2010 Jul to Dec','0_300')
# run_main('2018 Jan to Jun','300_800')
# dir_list = os.listdir(r"E:\Data\Emotion_detection_gihan\CEO emotions projects//")

if __name__ == '__main__':
    # left_list = ['2016-Apr-18-GWW.N-138635018661-transcript.pdf', '2012-Feb-22-WMT.N-138457380287-transcript.pdf',
    #              '2010-Apr-15-GWW.N-140754456533-transcript.pdf', '2015-May-28-TIF.N-137649442751-transcript.pdf',
    #              '2014-Jul-18-GWW.N-137512538215-transcript.pdf', '2015-Nov-18-WMT.N-137282010147-transcript.pdf',
    #              '2017-Feb-22-WMT.N-139109306027-transcript.pdf', '2011-Apr-19-GWW.N-140042405792-transcript.pdf',
    #              '2011-Jul-20-GWW.N-139714656843-transcript.pdf', '2014-Aug-14-WMT.N-138280627913-transcript.pdf',
    #              '2016-Oct-19-GWW.N-139439265408-transcript.pdf', '2016-May-19-WMT.N-140731918822-transcript.pdf',
    #              '2015-Feb-20-WMT.N-137422955072-transcript.pdf', '2013-Aug-15-WMT.N-137888047380-transcript.pdf',
    #              '2014-Aug-28-TIF.N-137498617156-transcript.pdf', '2016-Nov-18-WMT.N-140326139488-transcript.pdf',
    #              '2012-Jan-26-GWW.N-139080102064-transcript.pdf', '2010-Feb-19-WMT.N-140058621054-transcript.pdf',
    #              '2012-Aug-16-WMT.N-138910019119-transcript.pdf', '2014-Oct-17-GWW.N-138568172202-transcript.pdf',
    #              '2014-Nov-26-TIF.N-137920095615-transcript.pdf', '2013-Nov-15-WMT.N-139778498892-transcript.pdf',
    #              '2013-Apr-17-GWW.N-139277044158-transcript.pdf', '2015-May-19-WMT.N-138551303383-transcript.pdf',
    #              '2011-Jan-26-GWW.N-138241420484-transcript.pdf', '2017-Aug-17-WMT.N-140416186909-transcript.pdf',
    #              '2011-Feb-23-WMT.N-139543702109-transcript.pdf', '2011-Nov-30-TIF.N-138495868390-transcript.pdf',
    #              '2017-May-25-TIF.N-140930623660-transcript.pdf', '2010-Oct-15-GWW.N-138994942372-transcript.pdf',
    #              '2010-May-18-WMT.N-140088179134-transcript.pdf', '2012-Aug-28-TIF.N-137737193903-transcript.pdf',
    #              '2013-Oct-17-GWW.N-137028901354-transcript.pdf', '2011-Nov-16-WMT.N-139819959512-transcript.pdf',
    #              '2011-Oct-19-GWW.N-140375551248-transcript.pdf', '2013-Feb-06-CHD.N-140541828842-transcript.pdf',
    #              '2010-Feb-10-CHD.N-137236099964-transcript.pdf', '2015-Aug-28-TIF.N-140672860536-transcript.pdf',
    #              '2010-Nov-17-WMT.N-137700798672-transcript.pdf', '2013-Jan-25-GWW.N-137033069089-transcript.pdf',
    #              '2011-Aug-16-WMT.N-139819905465-transcript.pdf', '2014-Apr-17-GWW.N-138967048132-transcript.pdf',
    #              '2016-Jul-19-GWW.N-140454355475-transcript.pdf', '2010-Jan-27-GWW.N-137946061434-transcript.pdf',
    #              '2016-Aug-18-WMT.N-140599524318-transcript.pdf', '2013-May-16-WMT.N-139731208115-transcript.pdf',
    #              '2016-Nov-30-TIF.N-137267124688-transcript.pdf', '2017-Nov-17-WMT.N-138270315960-transcript.pdf',
    #              '2015-Jul-17-GWW.N-138650579075-transcript.pdf', '2010-Mar-23-TIF.N-138843493305-transcript.pdf',
    #              '2012-May-17-WMT.N-138924922949-transcript.pdf', '2012-May-25-TIF.N-140998138134-transcript.pdf',
    #              '2017-Dec-20-FDX.N-137363822335-transcript.pdf', '2012-Nov-30-TIF.N-136998505341-transcript.pdf',
    #              '2017-Sep-20-FDX.N-140726000072-transcript.pdf', '2017-Jun-21-FDX.N-137822397843-transcript.pdf',
    #              '2010-Aug-17-WMT.N-139333071754-transcript.pdf', '2016-Feb-19-WMT.N-139303518913-transcript.pdf',
    #              '2013-Jul-18-GWW.N-139240997923-transcript.pdf', '2016-Jan-27-GWW.N-139315578557-transcript.pdf',
    #              '2013-Feb-22-WMT.N-140987534315-transcript.pdf', '2012-Nov-16-WMT.N-139683751608-transcript.pdf',
    #              '2017-Nov-30-TIF.N-137241598555-transcript.pdf', '2010-Jul-16-GWW.N-137397607465-transcript.pdf',
    #              '2014-Feb-21-WMT.N-139563300083-transcript.pdf', '2012-Mar-21-TIF.N-138450088731-transcript.pdf',
    #              '2016-May-26-TIF.N-137999912147-transcript.pdf', '2011-Mar-22-TIF.N-137839290093-transcript.pdf',
    #              '2013-May-29-TIF.N-139437306801-transcript.pdf', '2014-Nov-14-WMT.N-137778501478-transcript.pdf',
    #              '2013-Nov-27-TIF.N-140325660127-transcript.pdf', '2012-Oct-17-GWW.N-137845926745-transcript.pdf',
    #              '2015-Apr-16-GWW.N-138049952622-transcript.pdf', '2014-May-22-TIF.N-139628391300-transcript.pdf',
    #              '2017-Aug-25-TIF.N-140040978412-transcript.pdf', '2012-Jul-19-GWW.N-140222347532-transcript.pdf',
    #              '2012-Apr-18-GWW.N-140643095232-transcript.pdf', '2017-May-18-WMT.N-139822610589-transcript.pdf',
    #              '2013-Aug-28-TIF.N-138961881188-transcript.pdf', '2016-Aug-26-TIF.N-139857956107-transcript.pdf',
    #              '2010-May-28-TIF.N-140893783901-transcript.pdf', '2015-Nov-25-TIF.N-138678711336-transcript.pdf',
    #              '2014-May-15-WMT.N-136998521654-transcript.pdf', '2011-May-17-WMT.N-137895566536-transcript.pdf',
    #              '2015-Aug-18-WMT.N-139990360757-transcript.pdf', '2015-Jan-27-GWW.N-140342661104-transcript.pdf']

    all_pdf_list = []
    dir_list = ['2010 Jan to Jun', '2010 Jul to Dec', '2011 Jan to Jun', '2011 Jul to Dec', '2012 Jan to Jun', '2012 Jul to Dec', '2013 Jan to Jun', '2013 Jul to Dec', '2014 Jan to Jun', '2014 Jul to Dec', '2015 Jan to Jun', '2015 Jul to Dec', '2016 Jan to Jun', '2016 Jul to Dec', '2017 Jan to Jun', '2017 Jul to Dec', '2018 Jan to Jun', '2019 Jan to Jun', '2019 Jul to Dec', '2020 Jan to Jun', '2020 Jul to Dec']
    run_main('left','80_100')
    # splits = ['0_300','300_800']
    # print(dir_list)
    # run_main('2017 Jul to Dec','0_300')
    # run_main('2014 Jan to Jun','0_300')

    # for i in dir_list[20:]:
    #     for j in splits:
    #         print(i,j)
    #         p0 = Process(target=run_main, args=(i,j,))
    #         p0.start()
    from shutil import copyfile


    # for s_e_f in dir_list:
    #     root_path = r"E:\Data\Emotion_detection_gihan\CEO emotions projects//" + s_e_f + "//"
    #     pdf_list = os.listdir(root_path)
    #     pdf_list = sorted(pdf_list)
    #     print(len(pdf_list))
    #     print(pdf_list[0])
    #     for pp in pdf_list:
    #         if(pp in left_list):
    #             all_pdf_list.append(root_path+pp)
    #             copyfile(root_path+pp, r'E:\Data\Emotion_detection_gihan\CEO emotions projects\left\\'+pp)
    #             # df = pd.read_csv(root_path+pp, encoding = 'unicode_escape')
    #             # df.to_csv(r'E:\Data\Emotion_detection_gihan\CEO emotions projects\left\\'+pp,index=False)
    #
    # print(all_pdf_list)



