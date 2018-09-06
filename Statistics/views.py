from django.shortcuts import render
from django.views.generic import TemplateView
from flask import render_template
import mysql.connector
import datetime
import matplotlib.pyplot
from matplotlib import pylab
from pylab import *
import numpy as np
import seaborn as sns

conn = mysql.connector.connect(
        user='root',
        password='shubh123',
        host='localhost',
        database='sso_data')
cur = conn.cursor()

class first_page(TemplateView):
	template_name='firstpage_stats.html'

def parseDate(request):
    date_today = datetime.datetime.now().date().strftime('%Y-%m-%d')
    date_tomorrow = (datetime.datetime.now().date() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    date1 = request.GET.get('start_date', date_today)
    date2 = request.GET.get('end_date', date_tomorrow)
    start_date = datetime.datetime.strptime(date1, '%Y-%m-%d').strftime('%Y-%m-%d')
    end_date = datetime.datetime.strptime(date2, '%Y-%m-%d').strftime('%Y-%m-%d')

    return (start_date, end_date)

def fatal(request):
	arr = []

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Bhilai Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Bhilai in cur:
	    Bhilai = np.array(Bhilai)
	    
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Bokaro Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Bokaro in cur:
	    Bokaro = np.array(Bokaro)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Durgapur Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Durgapur in cur:
	    Durgapur = np.array(Durgapur)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Rourkela Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Rourkela in cur:
	    Rourkela = np.array(Rourkela)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "IISCO Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for IISCO in cur:
	    IISCO = np.array(IISCO)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Alloys Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Alloys in cur:
	    Alloys = np.array(Alloys)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Chandrapur Ferro Alloy Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Chandrapur in cur:
	    Chandrapur = np.array(Chandrapur)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Salem Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Salem in cur:
	    Salem = np.array(Salem)
	        
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Visvesvaraya Iron & Steel Limited" and accd_type = "Fatal"')
	cur.execute(query)
	for Visvesvaraya in cur:
	    Visvesvaraya = np.array(Visvesvaraya)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Central Marketing Organisation" and accd_type = "Fatal"')
	cur.execute(query)
	for Marketing in cur:
	    Marketing = np.array(Marketing)
	        
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Raw Material Division" and accd_type = "Fatal"')
	cur.execute(query)
	for Raw in cur:
	    Raw = np.array(Raw)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "BSP Mines" and accd_type = "Fatal"')
	cur.execute(query)
	for BSP in cur:
	    BSP = np.array(BSP)
	        
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Collieries" and accd_type = "Fatal"')
	cur.execute(query)
	for Collieries in cur:
	    Collieries = np.array(Collieries)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "SAIL Refractory Unit" and accd_type = "Fatal"')
	cur.execute(query)
	for Refractory in cur:
	    Refractory = np.array(Refractory)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "SWG Kulti" and accd_type = "Fatal"')
	cur.execute(query)
	for Kulti in cur:
	    Kulti = np.array(Kulti)

	arr = np.append(arr, (Bhilai, Bokaro, Durgapur, Rourkela, IISCO, Alloys, Chandrapur, Salem, Visvesvaraya, Marketing, Raw, BSP, Collieries, Refractory, Kulti))

	plants = ['Bhilai SP', 'Bokaro SP', 'DSP', 'RSP', 'IISCO SP', 'ASP', 'CFAP', 'SSP', 'VISL', 'CMO', 'RMD', 'BSPM', 'Collieries', 'RFU', 'SWG Kulti']
	pos = np.arange(len(plants))
	Steel_plants = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	Steel_plants = np.array(Steel_plants)
	plt.figure(figsize=(30, 17))
	sns.set_style('whitegrid')
	plt.bar(Steel_plants, arr, facecolor = 'r', width = 0.7, alpha = 0.7, edgecolor = 'blue', label ='Number of all fatals per plant')
	plt.xlabel('<-------------         Steel plants         ---------->', fontsize=24)
	plt.ylabel('<-------------         Number of fatals per plant         --------->', fontsize=24)
	plt.title('BAR GRAPH', fontsize = 40)
	plt.xticks(pos, plants, fontsize = 19)
	for x,y in zip(Steel_plants, arr):
	    plt.text(x-0.3, y+0.15 ,f'{y}', fontsize=25)
	plt.legend(fontsize=28)
	return render_template('test.html' , console_gave=[plt.show()])


def fatal_pie(request):
	arr = []

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Bhilai Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Bhilai in cur:
	    Bhilai = np.array(Bhilai)
	    
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Bokaro Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Bokaro in cur:
	    Bokaro = np.array(Bokaro)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Durgapur Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Durgapur in cur:
	    Durgapur = np.array(Durgapur)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Rourkela Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Rourkela in cur:
	    Rourkela = np.array(Rourkela)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "IISCO Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for IISCO in cur:
	    IISCO = np.array(IISCO)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Alloys Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Alloys in cur:
	    Alloys = np.array(Alloys)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Chandrapur Ferro Alloy Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Chandrapur in cur:
	    Chandrapur = np.array(Chandrapur)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Salem Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Salem in cur:
	    Salem = np.array(Salem)
	        
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Visvesvaraya Iron & Steel Limited" and accd_type = "Fatal"')
	cur.execute(query)
	for Visvesvaraya in cur:
	    Visvesvaraya = np.array(Visvesvaraya)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Central Marketing Organisation" and accd_type = "Fatal"')
	cur.execute(query)
	for Marketing in cur:
	    Marketing = np.array(Marketing)
	        
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Raw Material Division" and accd_type = "Fatal"')
	cur.execute(query)
	for Raw in cur:
	    Raw = np.array(Raw)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "BSP Mines" and accd_type = "Fatal"')
	cur.execute(query)
	for BSP in cur:
	    BSP = np.array(BSP)
	        
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Collieries" and accd_type = "Fatal"')
	cur.execute(query)
	for Collieries in cur:
	    Collieries = np.array(Collieries)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "SAIL Refractory Unit" and accd_type = "Fatal"')
	cur.execute(query)
	for Refractory in cur:
	    Refractory = np.array(Refractory)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "SWG Kulti" and accd_type = "Fatal"')
	cur.execute(query)
	for Kulti in cur:
	    Kulti = np.array(Kulti)

	arr = np.append(arr, (Bhilai, Bokaro, Durgapur, Rourkela, IISCO, Alloys, Chandrapur, Salem, Visvesvaraya, Marketing, Raw, BSP, Collieries, Refractory, Kulti))

	plants = ['Bhilai SP', 'Bokaro SP', 'DSP', 'RSP', 'IISCO SP', 'ASP', 'CFAP', 'SSP', 'VISL', 'CMO', 'RMD', 'BSPM', 'Collieries', 'RFU', 'SWG Kulti']
	pos = np.arange(len(plants))
	Steel_plants = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	Steel_plants = np.array(Steel_plants)
	plt.figure(figsize=(30, 17))
	sns.set_style('whitegrid')
	plt.bar(Steel_plants, arr, facecolor = 'r', width = 0.7, alpha = 0.7, edgecolor = 'blue', label ='Number of all fatals per plant')
	plt.xlabel('<-------------         Steel plants         ---------->', fontsize=24)
	plt.ylabel('<-------------         Number of fatals per plant         --------->', fontsize=24)
	plt.title('BAR GRAPH', fontsize = 40)
	plt.xticks(pos, plants, fontsize = 19)
	for x,y in zip(Steel_plants, arr):
	    plt.text(x-0.3, y+0.15 ,f'{y}', fontsize=25)
	plt.legend(fontsize=28)

	return render_template('test.html' , console_gave=[plt.show()])

def cause(request):
	arr = []

	query = ('select count(cause) from inputforms_allaccident where cause = "Fall of Material"')
	cur.execute(query)
	for Fall in cur:
	    Fall = np.array(Fall)
	    
	query = ('select count(cause) from inputforms_allaccident where cause = "Material handling"')
	cur.execute(query)
	for Material in cur:
	    Material = np.array(Material)
	    
	query = ('select count(cause) from inputforms_allaccident where cause = "Road incident"')
	cur.execute(query)
	for Road in cur:
	    Road = np.array(Road)
	    
	query = ('select count(cause) from inputforms_allaccident where cause = "Slip"')
	cur.execute(query)
	for Slip in cur:
	    Slip = np.array(Slip)
	    
	query = ('select count(cause) from inputforms_allaccident where cause = "Fall of person"')
	cur.execute(query)
	for person in cur:
	    person = np.array(person)
	    
	query = ('select count(cause) from inputforms_allaccident where cause = "Burn"')
	cur.execute(query)
	for Burn in cur:
	    Burn = np.array(Burn)
	    
	query = ('select count(cause) from inputforms_allaccident where cause = "Electrocution"')
	cur.execute(query)
	for Electrocution in cur:
	    Electrocution = np.array(Electrocution)
	    
	query = ('select count(cause) from inputforms_allaccident where cause = "Gas exposure"')
	cur.execute(query)
	for Gas in cur:
	    Gas = np.array(Gas)
	    
	query = ('select count(cause) from inputforms_allaccident where cause = "Hit/Caught/Pressed"')
	cur.execute(query)
	for Hit in cur:
	    Hit = np.array(Hit)
	    
	query = ('select count(cause) from inputforms_allaccident where cause = "Violation of SOPs"')
	cur.execute(query)
	for SOPs in cur:
	    SOPs = np.array(SOPs)
	    
	query = ('select count(cause) from inputforms_allaccident where cause = "Violation of SMPs"')
	cur.execute(query)
	for SMPs in cur:
	    SMPs = np.array(SMPs)
	    
	query = ('select count(cause) from inputforms_allaccident where cause = "BBS Aspects"')
	cur.execute(query)
	for BBS in cur:
	    BBS = np.array(BBS)
	    
	query = ('select count(cause) from inputforms_allaccident where cause = "Equipment Failure"')
	cur.execute(query)
	for Equipment in cur:
	    Equipment = np.array(Equipment)
	arr = np.append(arr, (Fall, Material, Road, Slip, person, Burn, Electrocution, Gas, Hit, SOPs, SMPs, BBS, Equipment))
	print(arr)

	labels = ['Fall of Material', 'Material handling', 'Road incident', 'Slip', 'Fall of person', 'Burn', 'Electrocution', 'Gas exposure', 'Hit/Caught/Pressed', 'Violation of SOPs', 'Violation of SMPs', 'BBS Aspects', 'Equipment Failure' ]
	colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'lightgreen', 'indigo','blue','red','orange', '#ff6666', '#ffcc99', 'Grey', '#66b3ff', '#c2c2f0']
	plt.figure(figsize=(8, 8))
	plt.title('Pie Chart - Cause Percentage Holder', fontsize = 30)
	plt.pie(arr, colors = colors, shadow = True, startangle = 90, autopct='%.1f%%')
	plt.legend(labels, bbox_to_anchor=(1.1, 1), fontsize = 17)
	plt.axis('equal')
	plt.tight_layout()
	
	return render_template('test.html' , console_gave=[plt.show()])

def manhours(request):
	arr = []
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Bhilai Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Bhilai in cur:
	    Bhilai = np.array(Bhilai)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Bhilai Steel Plant" and accd_type = "Reportable"')
	cur.execute(query)
	for rBhilai in cur:
	    rBhilai = np.array(rBhilai)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "Bhilai Steel Plant" and date = "2018-06-08"')
	cur.execute(query)
	for mBhilai in cur:
	    mBhilai = np.array(mBhilai)
	r1= ((Bhilai + rBhilai) * 1000000) / mBhilai
	r1 = np.around(r1, decimals=2)
	    
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Bokaro Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Bokaro in cur:
	    Bokaro = np.array(Bokaro)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Bokaro Steel Plant" and accd_type = "Reportable"')
	cur.execute(query)
	for rBokaro in cur:
	    rBokaro = np.array(rBokaro)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "Bokaro Steel Plant" and date = "2018-06-08"')
	cur.execute(query)
	for mBokaro in cur:
	    mBokaro = np.array(mBokaro)
	r2= ((Bokaro + rBokaro) * 1000000) / mBokaro
	r2 = np.around(r2, decimals=2)

	    
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Durgapur Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Durgapur in cur:
	    Durgapur = np.array(Durgapur)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Durgapur Steel Plant" and accd_type = "Reportable"')
	cur.execute(query)
	for rDurgapur in cur:
	    rDurgapur = np.array(rDurgapur)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "Durgapur Steel Plant" and date = "2018-06-08"')
	cur.execute(query)
	for mDurgapur in cur:
	    mDurgapur = np.array(mDurgapur)
	r3= ((Durgapur + rDurgapur) * 1000000) / mDurgapur
	r3 = np.around(r3, decimals=2)
	    
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Rourkela Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Rourkela in cur:
	    Rourkela = np.array(Rourkela)
	query = ('select count	(unit_name) from inputforms_allaccident where unit_name = "Rourkela Steel Plant" and accd_type = "Reportable"')
	cur.execute(query)
	for rRourkela in cur:
	    rRourkela = np.array(rRourkela)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "Rourkela Steel Plant" and date = "2018-06-08"')
	cur.execute(query)
	for mRourkela in cur:
	    mRourkela = np.array(mRourkela)
	r4= ((Rourkela + rRourkela) * 1000000) / mRourkela
	r4 = np.around(r4, decimals=2)
	    
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "IISCO Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for IISCO in cur:
	    IISCO = np.array(IISCO)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "IISCO Steel Plant" and accd_type = "Reportable"')
	cur.execute(query)
	for rIISCO in cur:
	    rIISCO = np.array(rIISCO)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "IISCO Steel Plant" and date = "2018-06-08"')
	cur.execute(query)
	for mIISCO in cur:
	    mIISCO = np.array(mIISCO)
	r5= ((IISCO + rIISCO) * 1000000) / mIISCO
	r5 = np.around(r5, decimals=2)
	    
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Alloys Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Alloys in cur:
	    Alloys = np.array(Alloys)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Alloys Steel Plant"  and accd_type = "Reportable"')
	cur.execute(query)
	for rAlloys in cur:
	    rAlloys = np.array(rAlloys)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "Alloys Steel Plant" and date = "2018-06-08"')
	cur.execute(query)
	for mAlloys in cur:
	    mAlloys = np.array(mAlloys)
	r6= ((Alloys + rAlloys) * 1000000) / mAlloys
	r6 = np.around(r6, decimals=2)
	    
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Chandrapur Ferro Alloy Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Chandrapur in cur:
	    Chandrapur = np.array(Chandrapur)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Chandrapur Ferro Alloy Plant" and accd_type = "Reportable"')
	cur.execute(query)
	for rChandrapur in cur:
	    rChandrapur = np.array(rChandrapur)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "Chandrapur Ferro Alloy Plant" and date = "2018-06-08"')
	cur.execute(query)
	for mChandrapur in cur:
	    mChandrapur = np.array(mChandrapur)
	r7= ((Chandrapur + rChandrapur) * 1000000) / mChandrapur
	r7 = np.around(r7, decimals=2)
	    
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Salem Steel Plant" and accd_type = "Fatal"')
	cur.execute(query)
	for Salem in cur:
	    Salem = np.array(Salem)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Salem Steel Plant" and accd_type = "Reportable"')
	cur.execute(query)
	for rSalem in cur:
	    rSalem = np.array(rSalem)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "Salem Steel Plant" and date = "2018-06-08"')
	cur.execute(query)
	for mSalem in cur:
	    mSalem = np.array(mSalem)
	r8= ((Salem + rSalem) * 1000000) / mSalem
	r8 = np.around(r8, decimals=2)
	            
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Visvesvaraya Iron & Steel Ltd" and accd_type = "Fatal"')
	cur.execute(query)
	for Visvesvaraya in cur:
	    Visvesvaraya = np.array(Visvesvaraya)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Visvesvaraya Iron & Steel Ltd" and accd_type = "Reportable"')
	cur.execute(query)
	for rVisvesvaraya in cur:
	    rVisvesvaraya = np.array(rVisvesvaraya)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "Visvesvaraya Iron & Steel Ltd" and date = "2018-06-08"')
	cur.execute(query)
	for mVisvesvaraya in cur:
	    mVisvesvaraya = np.array(mVisvesvaraya)
	r9= ((Visvesvaraya + rVisvesvaraya) * 1000000) / mVisvesvaraya
	r9 = np.around(r9, decimals=2)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Central Marketing Organisation" and accd_type = "Fatal"')
	cur.execute(query)
	for Marketing in cur:
	    Marketing = np.array(Marketing)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Central Marketing Organisation" and accd_type = "Reportable"')
	cur.execute(query)
	for rMarketing in cur:
	    rMarketing = np.array(rMarketing)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "Central Marketing Organisation" and date = "2018-06-08"')
	cur.execute(query)
	for mMarketing in cur:
	    mMarketing = np.array(mMarketing)
	r10= ((Marketing + rMarketing) * 1000000) / mMarketing
	r10 = np.around(r10, decimals=2)
	        
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Raw Material Division" and accd_type = "Fatal"')
	cur.execute(query)
	for Raw in cur:
	    Raw = np.array(Raw)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Raw Material Division" and accd_type = "Reportable"')
	cur.execute(query)
	for rRaw in cur:
	    rRaw = np.array(rRaw)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "Raw Material Division" and date = "2018-06-08"')
	cur.execute(query)
	for mRaw in cur:
	    mRaw = np.array(mRaw)
	r11= ((Raw + rRaw) * 1000000) / mRaw
	r11 = np.around(r11, decimals=2)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "BSP Mines" and accd_type = "Fatal"')
	cur.execute(query)
	for BSP in cur:
	    BSP = np.array(BSP)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "BSP Mines" and accd_type = "Reportable"')
	cur.execute(query)
	for rBSP in cur:
	    rBSP = np.array(rBSP)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "BSP Mines" and date = "2018-06-08"')
	cur.execute(query)
	for mBSP in cur:
	    mBSP = np.array(mBSP)
	r12= ((BSP + rBSP) * 1000000) / mBSP
	r12 = np.around(r12, decimals=2)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Collieries" and accd_type = "Fatal"')
	cur.execute(query)
	for Collieries in cur:
	    Collieries = np.array(Collieries)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "Collieries" and accd_type = "Reportable"')
	cur.execute(query)
	for rCollieries in cur:
	    rCollieries = np.array(rCollieries)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "Collieries" and date = "2018-06-08"')
	cur.execute(query)
	for mCollieries in cur:
	    mCollieries = np.array(mCollieries)
	r13= ((Collieries + rCollieries) * 1000000) / mCollieries
	r13 = np.around(r13, decimals=2)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "SAIL Refractory Unit" and accd_type = "Fatal"')
	cur.execute(query)
	for Refractory in cur:
	    Refractory = np.array(Refractory)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "SAIL Refractory Unit" and accd_type = "Reportable"')
	cur.execute(query)
	for rRefractory in cur:
	    rRefractory = np.array(rRefractory)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "SAIL Refractory Unit" and date = "2018-06-08"')
	cur.execute(query)
	for mRefractory in cur:
	    mRefractory = np.array(mRefractory)
	r14= ((Refractory + rRefractory) * 1000000) / mRefractory
	r14 = np.around(r14, decimals=2)

	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "SWG Kulti" and accd_type = "Fatal"')
	cur.execute(query)
	for Kulti in cur:
	    Kulti = np.array(Kulti)
	query = ('select count(unit_name) from inputforms_allaccident where unit_name = "SWG Kulti" and accd_type = "Reportable"')
	cur.execute(query)
	for rKulti in cur:
	    rKulti = np.array(rKulti)
	query = ('select (manhours_worked_regular + manhours_worked_contract) from inputforms_manhours where unit_name = "SWG Kulti" and date = "2018-06-08"')
	cur.execute(query)
	for mKulti in cur:
	    mKulti = np.array(mKulti)
	r15= ((Kulti + rKulti) * 1000000) / mKulti
	r15 = np.around(r15, decimals=2)
	arr = np.append(arr,(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15))

	plants = ['Bhilai SP', 'Bokaro SP', 'DSP', 'RSP', 'IISCO SP', 'ASP', 'CFAP', 'SSP', 'VISL', 'CMO', 'RMD', 'BSPM', 'Collieries', 'RFU', 'SWG Kulti']
	pos = np.arange(len(plants))
	Steel_plants = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	Steel_plants = np.array(Steel_plants)
	plt.figure(figsize=(30, 17))
	sns.set_style('whitegrid')
	plt.bar(Steel_plants, arr, facecolor = 'b' ,width = 0.7, alpha = 0.5, edgecolor = 'blue', label ='RLTIFR = Nos. of Fatal + Reportable Accidents X 1,000,000 / Man-Hours Worked')
	plt.xlabel('<-------------         Steel plants         ---------->', fontsize=24)
	plt.ylabel('<-------------         Plant / Unit wise RLTIFR         --------->', fontsize=24)
	plt.title('BarGraph', fontsize = 40)
	plt.xticks(pos, plants, fontsize = 19)
	for x,y in zip(Steel_plants, arr):
	    plt.text(x-0.3, y+0.5 ,f'{y}', fontsize=25)
	plt.legend(fontsize=28)
	return render_template('test.html' , console_gave=[plt.show()])





    
     
	

