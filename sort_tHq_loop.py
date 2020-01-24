#programm for putting mc samples in subdirectories with respect to their event 
#run programm in directory with the root files of mc simulations
#python 3.7
#run with: python /cephfs/user/s6pinogg/PietBachelor/sort_tHq_loop.py

import os 
import re
import shutil

pathtomc = os.getcwd()

pathtZq = pathtomc + '/tZq/'
pathttbar = pathtomc + '/ttbar/'
pathdiboson = pathtomc + '/diboson/'
pathnBoson = pathtomc + '/nBoson/'
pathsingleTop = pathtomc + '/singleTop/'
pathtHq = pathtomc + '/tHq/'
pathttV = pathtomc + '/ttV/'
pathWJets = pathtomc + '/WJets/'
pathZJets = pathtomc + '/ZJets/'
pathttH = pathttV + 'ttH/'
pathtchannel = pathtomc + '/tchannel/'
doubleaf = pathtomc + '/AFII_FS_double/'
direcData = pathtomc + '/Data/'
pathtW = pathsingleTop + 'tW/'
pathttW = pathttV + 'ttW/'
pathttZ = pathttV + 'ttZ/'
pathtWZ = pathsingleTop + 'tWZ/'
pathtchannel = pathsingleTop + 'tchannel/'
pathschannel = pathtomc + '/schannel/' 
pathtt_2l = pathtomc + '/tt_2l/'
pathdilepton = pathtomc + '/diboson_ZqqZvv/'
path4top = pathsingleTop + '4_top/'

if not os.path.exists(pathZJets):
    os.makedirs(pathZJets)
if not os.path.exists(pathWJets):
    os.makedirs(pathWJets)
if not os.path.exists(pathtZq):
    os.makedirs(pathtZq)
if not os.path.exists(pathttV):
    os.makedirs(pathttV)
if not os.path.exists(pathttbar):
    os.makedirs(pathttbar)
if not os.path.exists(pathsingleTop):
    os.makedirs(pathsingleTop)
if not os.path.exists(pathtHq):
    os.makedirs(pathtHq)
if not os.path.exists(pathtHq):
    os.makedirs(pathtHq)
if not os.path.exists(pathnBoson):
    os.makedirs(pathnBoson)
if not os.path.exists(pathdiboson):
    os.makedirs(pathdiboson)
if not os.path.exists(pathttH):
    os.makedirs(pathttH)
if not os.path.exists(doubleaf):
    os.makedirs(doubleaf)
if not os.path.exists(direcData):
    os.makedirs(direcData)
if not os.path.exists(pathtW):
    os.makedirs(pathtW)
if not os.path.exists(pathttW):
    os.makedirs(pathttW)
if not os.path.exists(pathttZ):
    os.makedirs(pathttZ)
if not os.path.exists(pathtWZ):
    os.makedirs(pathtWZ)
if not os.path.exists(pathtchannel):
    os.makedirs(pathtchannel)
if not os.path.exists(pathschannel):
    os.makedirs(pathschannel)
if not os.path.exists(pathtt_2l):
    os.makedirs(pathtt_2l)
if not os.path.exists(pathdilepton):
    os.makedirs(pathdilepton)
if not os.path.exists(path4top):
    os.makedirs(path4top)



root_files = [f for f in os.listdir(os.getcwd()) if f.endswith('.root')]
root_files_af = [f for f in os.listdir(os.getcwd()) if f.endswith('.root') and 'AF' in f]
root_files_af_des = [f for f in os.listdir(doubleaf) if f.endswith('.root')]
        #if re.findall(r'\d+',morefiles)[1] == re.findall(r'\d+',files)[1]:

for files in root_files:

    ### Data samples
    if 'data' in files:
        shutil.move(files,direcData)
    ### tZq samples
    if '412063' in files:
        if not 'AF' in files:
            shutil.move(files,pathtZq)
    ## tHq samples
    if '346229' in files or '346230' in files:
        shutil.move(files,pathtHq)
    ## ttV samples
    if '410155' in files:
        shutil.move(files,pathttW)
    if '410218' in files or '410219' in files or '410220' in files or '410156' in files or '410157' in files:
        shutil.move(files,pathttZ)
    if '346343' in files or '346344' in files or '346345' in files:
        shutil.move(files,pathttH)
    ### diboson samples
    if '364250' in files or '364253' in files or '364254' in files or '364255' in files or '364288' in files or '364289' in files or '364290' in files: 
        shutil.move(files,pathdiboson)
    if '363356' in files or '363357' in files or '363358' in files or '363359' in files or '363360' in files or '363489' in files:
        shutil.move(files,pathdiboson)
    if '363355' in files:
        shutil.move(files,pathdilepton)
    ### ttbar 
    if '410470' in files or '410471' in files: 
        if not 'AF' in files:
            shutil.move(files,pathttbar)
    if '410472' in files:
        if not 'AF' in files: 
            shutil.move(files,pathtt_2l)
    
    ### W+Jets
    if '364170' in files or '364171' in files or '364172' in files or '364173' in files or '364174' in files or '364175' in files or '364176' in files or '364177' in files or '364178' in files or '364179' in files:
        shutil.move(files,pathWJets)
    if '364180' in files or '364181' in files or '364182' in files or '364183' in files:
        shutil.move(files,pathWJets)
    if '364156' in files or '364157' in files or '364158' in files or '364159' in files:
        shutil.move(files,pathWJets)
    if '364160' in files or '364161' in files or '364162' in files or '364163' in files or '364164' in files or '364165' in files or '364166' in files or '364167' in files or '364168' in files or '364169' in files:      
        shutil.move(files,pathWJets)
    if '364184' in files or '364185' in files or '364186' in files or '364187' in files or '364188' in files or '364189' in files:
        shutil.move(files,pathWJets)
    if '364190' in files or '364191' in files or '364192' in files or '364193' in files or '364194' in files or '364195' in files or '364196' in files or '364197' in files:
        shutil.move(files,pathWJets)
    ## Z+Jets
    if '36411' in files:
        shutil.move(files,pathZJets)
    if '36412' in files:
        shutil.move(files,pathZJets)
    if '36410' in files or '36413' in files:
        shutil.move(files,pathZJets)
    if '364140' in files or '364141' in files:
        shutil.move(files,pathZJets)
    ## Single Top
    if '410408' in files:
        shutil.move(files,pathtWZ)  
    if '410646' in files or '410647' in files or '410648' in files or '410649' in files:
        if not 'AF' in files:
            shutil.move(files,pathtW)  
    if '410644' in files or '410645' in files:
        shutil.move(files,pathschannel)
    if '412043' in files or '412045' in files:
        shutil.move(files,path4top)  
    ## nBosons
    if '36424' in files:
        shutil.move(files,pathnBoson)
    if '410658' in files or '410659' in files:
        if not 'AF' in files:
            shutil.move(files,pathtchannel) 
    ### 
root_files = [f for f in os.listdir(os.getcwd()) if f.endswith('.root')]
for filename in root_files:
    if 'AF' in filename:
        shutil.move(filename,doubleaf)
