import sys

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, savefig

def main(fileName):
	imgName = fileName.replace('csv', 'png')

	df = pd.read_csv(fileName, names=['YEAR', 'BASIN_CD', 'BASIN_MAP', 'STN_CD', 'STN_MAP'])
	#print(df.YEAR)
	basinCd = df.BASIN_CD[0]
	stnCd = df.STN_CD[0]
	startYear = min(df.YEAR)
	endYear = max(df.YEAR)

	basinLegend = 'BASIN(' + str(basinCd) + ')'
	stnLegend = 'STN(' + str(stnCd) + ')'

	plt.figure(figsize=(14,8))
	plt.bar(df.YEAR + 0.2, df.BASIN_MAP, color = 'b', width = 0.25)
	plt.bar(df.YEAR - 0.2, df.STN_MAP, color = 'r', width = 0.25)
	plt.legend([basinLegend, stnLegend])
	plt.xlabel('Year', size=15)
	plt.ylabel('Prcp(mm)', size=15)
	plt.xticks(range(int(startYear), int(endYear) + 2, 2))
	plt.grid(True)
	#plt.show()
	savefig('graph_year/' + imgName)

if __name__ == "__main__":
	if ( len(sys.argv) < 2 ):
		print("Usage python3 graph_year.py filename")
		sys.exit()

	main(sys.argv[1])
