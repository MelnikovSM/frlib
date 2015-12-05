import os, glob, cv2
import frlib
SRC=None
#Uncomment to read img from file
#SRC='in.pgm'

POSITIVE_FILE_DIR="./templates/myface/positive"

files = sorted(glob.glob(os.path.join(POSITIVE_FILE_DIR, 
'positive_' + '[0-9][0-9][0-9].pgm')))
count = 0
if len(files) > 0:
	count = int(files[-1][-7:-4])+1

if SRC==None:
	print('Notice: Only 1st detected face will be handled!')
	print('Capturing frame from WebCam..')
	img, timestamp = frlib.captureFrame()
else:
	img = cv2.imread(SRC, cv2.IMREAD_GRAYSCALE)

faces=frlib.cropFaces(img)
if not faces==None:
	print('Successfuly captured!')
	img=faces[0]
	path=os.path.join(POSITIVE_FILE_DIR, 'positive_' + '%03d.pgm' % count)
	cv2.imwrite(path, img)
else:
	print('No faces detected!')