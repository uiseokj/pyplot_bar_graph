import sys

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, savefig


def main(fileName):
	imgName = fileName.replace('csv', 'png')

	df = pd.read_csv(fileName, names=['YEAR', 'SEASON', 'BASIN_CD', 'BASIN_MAP', 'STN_CD', 'STN_MAP'])
	
	df['SEASON'].replace(r'^S', '',inplace=True, regex=True)
	df['SEASON'].astype(float)

	startYear = min(df.YEAR)
	endYear = max(df.YEAR)

	yearCount = 0

	columns = 9
	rows = 5

	fig, ax_array = plt.subplots(rows, columns, figsize=(55,30))
	for i, ax_row in enumerate(ax_array):
		for j, axes in enumerate(ax_row):
			currentYear = str(startYear + yearCount)
			axes.set_title('Year: ' + currentYear)

			df2 = df.query('YEAR==' + str(currentYear))
			basinCd = df2.BASIN_CD[yearCount * len(df2)]
			stnCd = df2.STN_CD[yearCount * len(df2)]

			basinLegend = 'BASIN(' + str(basinCd) + ')'
			stnLegend = 'STN(' + str(stnCd) + ')'

			seasonList = pd.Series([1, 2, 3, 4], dtype='float')

			axes.bar(seasonList + 0.14, df2.BASIN_MAP, color = 'b', width = 0.25)
			axes.bar(seasonList - 0.14, df2.STN_MAP, color = 'r', width = 0.25)
			axes.legend([basinLegend, stnLegend])
			axes.set_xlabel('Season', size=12)
			axes.set_ylabel('Prcp(mm)', size=12)
			axes.set_xticks(range(int(1), int(4) + 1, 1))
			axes.set_xticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])
			#axes.grid(True)

			yearCount = yearCount + 1

	savefig('graph_season/' + imgName)

	
if __name__ == "__main__":
	if ( len(sys.argv) < 2 ):
		print("Usage python3 graph_season.py filename")
		sys.exit()

	main(sys.argv[1])
