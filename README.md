# MelnikovSM's FaceRecognizer Library
Example programs sources are included in dir: capturePositive.py gentemplate.py recogn.py
Main library file: frlib.py

Library (or, hope be honest, just case of functions) wroten by Melnikov Sergey, 14 full years after birth. Library wroten to simplificate my program for my project "Wonderful Creature Recognizer and Just Self-Wroten Song Player" (at the moment of library publication project not completed).

FR Lib - image library for Python, containing the basic functions needed for face recognition using OpenCV (just simplified OpenCV functions call, nothing more)..
The requirements for the operation: Python 2.7.X with a working module CV2 + Haar cascades (requires a file that was originally sought in the /usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml, it can be corrected on the 15th line).

# Describtion of functions:

captureFrame([device]) - returns image CV2 and a string date snapshot, on input can accept video device number (default value 0)
Example of use: img, timestamp = frlib.captureFrame()
Example of use: img, timestamp = frlib.captureFrame(1)

cropFaces(img, [cascadePath]) - takes the input image CV2, looking at him face using an algorithm Haar Cascades (the second argument you can specify the path to another file) (default path can be changed on the 15th line), returns a list (array) with the cut from the image faces, if not find a single person returns None ..
Example of use: faces = frlib.cropFaces(img)
Example of use: faces = frlib.cropFaces(img, custom_haarcascade_path)

genTemplate (dir, file) - generates a template file (the file contain model, but I'm too lazy to rename all varribles, so what's important: It just works!) to recognize individuals at the input .. must be the path to the templates directory, as well as being the way in which the file will be saved template ..
Note: the path of the directory template should be cataloged as templates/DEFAULT, with "positive" individuals in the files of the $PATH/positive/positive_XXX.pgm, where XXX - number in the string in the value from 000 to 999
Example of use: frlib.genTemplate('templates/myface', 'templates/myface/template.xml')

createRecognizer(template) - creates and returns a function of facial recognition using template file template, let's say the function is written in the variable recogn:
recogn (face) - at input gets a picture CV2, returns uncertainty number (what the number is higher, then the more different the face of the template) in the type float, and the number of persons according to the pattern (in the generation using genTemplate "positive" person has the FID = 0) in the int
Example of use:
recogn = fr.createRecognizer('templates/myface/template.xml')
inconfidence, fid = recogn(face)
