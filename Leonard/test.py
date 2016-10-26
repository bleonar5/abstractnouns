
import rpy2.robjects as R
import numpy as np
import pandas as pd
from rpy2.robjects import pandas2ri
import csv
import sys
import matplotlib.pyplot as plt

def deviation(string):
	if '[]' in string:
		return -1
	else:
		return 1

with open(sys.argv[1] + 'Out2.csv','rb') as file:
	csvReader = csv.reader(file)
	reader = list(csvReader)

	pandas2ri.activate()

	ofObjCol = []
	objectCol = []
	detCol= []
	possCol = []
	PROingCol = []
	bareCol = []
	POSSingCol= []
	POSSofingCol = []
	DETingCol = []
	DETofingCol = []
	ofingCol = []
	subjectCol = []
	dObjectCol = []
	adjCol = []
	advCol = []
	prepCol = []


	count = 1

	for line in reader[1:]:
		if '[]' not in line[17] or '[]' not in line[24]:
			reader.pop(count)
			continue



		if '[]' in line[15]:
			ofObjCol.append(0)
		else:
			ofObjCol.append(1)

		if '[]' in line[22]:
			detCol.append(0)
		else:
			detCol.append(1)

		if '[]' in line[27]:
			possCol.append(0)
		else:
			possCol.append(1)

		if '[]' in line[13]:
			objectCol.append(0)
		else:
			objectCol.append(1)

		if '[]' in line[25]:
			adjCol.append(0)
		else:
			adjCol.append(1)

		if '[]' in line[30]:
			advCol.append(0)
		else:
			advCol.append(1)

		if '[]' in line[36]:
			subjectCol.append(0)
		else:
			subjectCol.append(1)

		if '[]' in line[37]:
			dObjectCol.append(0)
		else:
			dObjectCol.append(1)

		bare = ofObjCol[count - 1] == 0 and detCol[count - 1] == 0 and possCol[count - 1] == 0 and objectCol[count - 1] == 0
		PROing = ofObjCol[count - 1] == 0 and detCol[count - 1] == 0 and possCol[count - 1] == 0 and objectCol[count - 1] == 1
		POSSing = ofObjCol[count - 1] == 0 and detCol[count - 1] == 0 and possCol[count - 1] == 1 and objectCol[count - 1] == 1
		POSSofing = ofObjCol[count - 1] == 1 and detCol[count - 1] == 0 and possCol[count - 1] == 1 and objectCol[count - 1] == 0
		DETing = ofObjCol[count - 1] == 0 and detCol[count - 1] == 1 and possCol[count - 1] == 0 and objectCol[count - 1] == 0
		DETofing = ofObjCol[count - 1] == 1 and detCol[count - 1] == 1 and possCol[count - 1] == 0 and objectCol[count - 1] == 0
		ofing = ofObjCol[count - 1] == 1 and detCol[count - 1] == 0 and possCol[count - 1] == 0 and objectCol[count - 1] == 0


		if PROing:
			PROingCol.append(1)
		else:
			PROingCol.append(0) 

		if bare:
			bareCol.append(1)
		else:
			bareCol.append(0)

		if POSSing:
			POSSingCol.append(1)
		else:
			POSSingCol.append(0)

		if POSSofing:
			POSSofingCol.append(1)
		else:
			POSSofingCol.append(0)

		if DETing:
			DETingCol.append(1)
		else:
			DETingCol.append(0)

		if DETofing:
			DETofingCol.append(1)
		else:
			DETofingCol.append(0)

		if ofing:
			ofingCol.append(1)
		else:
			ofingCol.append(0)
		
		count += 1
	#d = {'ofObj': pd.Series(ofObjCol,name='ofObj'),
	#	'detCol':pd.Series(detCol,name='detCol'),
	#	'possCol':pd.Series(possCol,name='possCol')}
	d = {'ofObj' : ofObjCol, 'detCol': detCol, 'possCol':possCol, 'objectCol':objectCol, 'PROingCol':PROingCol, 'bareCol':bareCol, 'POSSingCol':POSSingCol, 'POSSofingCol':POSSofingCol, 'DETingCol':DETingCol, 'DETofingCol':DETofingCol, 'ofingCol':ofingCol, 'adjCol':adjCol,'advCol':advCol,'subjectCol':subjectCol,'dObjectCol':dObjectCol}

	#dF = pd.DataFrame({'ofObj': ofObjCol, 'detCol' : detCol, 'possCol' : possCol})

	dF = pd.DataFrame.from_dict(data=d,orient='columns')
	r_dF = pandas2ri.py2ri(dF)
	print dF
	dF.to_csv(sys.argv[1] + '.csv')

