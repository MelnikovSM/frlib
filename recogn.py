import frlib
recogn=frlib.createRecognizer('./templates/myface/template.xml')

print('Taking picture from WebCam..')
pic, timestamp = frlib.captureFrame()

faces=frlib.cropFaces(pic)
if not faces==None:
	fcount=0
	for face in faces:
		print('Handling face{face} via FaceRecognizer..'.format(face=fcount))
		confidence, fid = recogn(face)
		print('face{face}: FID: {fid}, Inconfidence level: {cnf}'.format(face=fcount, fid=fid, cnf=confidence))
		if fid==0 and confidence<=120:
			print('face{face}: Face recognized successfuly!'.format(face=fcount))
		else: print('face{face}: STOCK REJECTED!'.format(face=fcount))
		fcount=+1
else: print('No faces found!')
