from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
pylab.rcParams['figure.figsize'] = (10.0, 8.0)


dataDir ='..'

trainDataType = 'train2014'
trainAnnFile = '%s/annotations/instances_%s.json'%(dataDir, trainDataType)


train = COCO(trainAnnFile)

cats = train.loadCats(train.getCatIds())

catIds = train.getCatIds(catNms=['person', 'bus', 'car', 'motorcycle', 'truck', 'knife', 'vehicle' ])
imgIds = train.getImgIds(catIds=catIds)


for i in range(0, 80000):
	img = train.loadImgs(imgIds[np.random.randint(0, len(imgIds))])[0]
	I = io.imread('%s/images/%s/%s'%(dataDir, trainDataType, img['file_name']))
	print '%s/images/%s/%s'%(dataDir, trainDataType, img['file_name'])
	plt.figure()
	plt.imshow(I)
	plt.show()

plt.imshow(I)

annIds = train.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
anns = train.loadAnns(annIds)
train.showAnns(anns)


annFile = '%s/annotations/captions_%s.json'%(dataDir, trainDataType)
caps = COCO(annFile)

annIds = caps.getAnnIds(imgIds=img['id'])
anns = caps.loadAnns(annIds)
caps.showAnns(anns)
plt.imshow(I)
plt.show()


