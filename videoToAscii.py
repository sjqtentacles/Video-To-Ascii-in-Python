import cv2

def transform(img):
	transformedAscii = []
	for i in img:
		temp = []
		for j in i:
			temp.append(asciiToNum[j])
		transformedAscii.append(temp)
	return transformedAscii

def setupAsciiMapping():
	asciiToNum = {}
	characterSet = list('  ..,,::;;ii11ttffLL;;::..ii11ttL')
	#characterSet = list('   .....//ii11tt   ...    ii11ttL')
	#characterSet = list((' '*2)+('n'*2)+('n'*1)+('/'*3)+('.'*2)+(' '*23))
	#characterSet = list((' '*2)+('n'*2)+('n'*1)+('/'*3)+('.'*6)+(' '*23))
					
	#characterSet = characterSet[::-1]
	
	for i in range(26):
		for j in range(10):
			asciiToNum[i*10+j]=characterSet[i]
	return asciiToNum
    
def arrayToString(arr):
	ascii = ''
	for i in transformedAscii:
		ascii+= ' '.join(i)
		ascii+='\n'
	return ascii
            
asciiToNum = setupAsciiMapping()

width,height = 80,60

cap = cv2.VideoCapture(0)
ret = cap.set(3,width)
ret = cap.set(4,height)


while True:
	ret,frame = cap.read()
	img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	transformedAscii = transform(img)	
	print arrayToString(transformedAscii)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()