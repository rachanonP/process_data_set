import numpy as np
import cv2
from matplotlib import pyplot as plt
import xlsxwriter

# img = cv2.imread('D:/python/Image Minning/color_segmentation-master/nodules_cheek_1.png')
# img2 = cv2.imread('D:/python/Image Minning/color_segmentation-master/nodules_cheek_3.png')
# img3 = cv2.imread('D:/python/Image Minning/color_segmentation-master/cryst_2.png')

# im = [img,img2,img3]
# im = [img3,img2,img]

workbook = xlsxwriter.Workbook('D:/python/Image Minning/color_segmentation-master/demo_white.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})


for m in range(12):
	a = plt
	fname = "D:/python/Image Minning/color_segmentation-master/image/white/"+str(m+1)+".jpg"
	img = cv2.imread(fname)
	print (fname)
	worksheet.write(0,0,'yred')
	worksheet.write(0,1,'xred')
	worksheet.write(0,2,'ygreen')
	worksheet.write(0,3,'xgreen')
	worksheet.write(0,4,'yblue')
	worksheet.write(0,5,'xblue')
	color = ('b','g','r')
	for i,col in enumerate(color):
		histr = cv2.calcHist([img],[i],None,[256],[0,256])
		# row/ xred yred xgreen ygreen xblue yblue  
		worksheet.write(m+1, ((i+1)*2)-2, max(histr))
		indexH = histr.tolist()
		worksheet.write(m+1, ((i+1)*2)-1, indexH.index(max(histr)))
		# worksheet.write(m+1, (i+1)*2, sum(histr)/len(histr))
		print (type(max(histr)))
		a.plot(histr,color = col)
		a.xlim([0,256])
	name = "D:/python/Image Minning/color_segmentation-master/his/white/backHis_"+str(m+1)+".png"
	a.savefig(name)
	a.cla()

workbook.close()
