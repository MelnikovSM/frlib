import frlib

templatedir='./templates/myface'
out='/template.xml'

print('Generating Face Recognizer template..')
frlib.genTemplate(templatedir, templatedir+out)
print('Complete!')