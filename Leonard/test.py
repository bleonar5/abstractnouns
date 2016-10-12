
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

with open(sys.argv[1],'rb') as file:
	csvReader = csv.reader(file)
	reader = list(csvReader)

	pandas2ri.activate()

	ofObjCol = []
	objectCol = []
	detCol= []
	possCol = []

	count = 1

	for line in reader[1:]:
		if '[]' not in line[17]:
			reader.pop(count)
			continue


		if '[]' in line[15]:
			ofObjCol.append(-1)
		else:
			ofObjCol.append(1)

		if '[]' in line[22]:
			detCol.append(-1)
		else:
			detCol.append(1)

		if '[]' in line[27]:
			possCol.append(-1)
		else:
			possCol.append(1)

		
		count += 1
	d = {'ofObj': pd.Series(ofObjCol,name='ofObj'),
		'detCol':pd.Series(detCol,name='detCol'),
		'possCol':pd.Series(possCol,name='possCol')}

	#dF = pd.DataFrame({'ofObj': ofObjCol, 'detCol' : detCol, 'possCol' : possCol})

	dF = pd.DataFrame.from_dict(data=d,orient='columns')
	r_dF = pandas2ri.py2ri(dF)
	dF.ofObj.hist()
	plt.show()
	

