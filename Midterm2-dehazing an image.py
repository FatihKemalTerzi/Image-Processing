
import image_dehazer
import 	cv2									# Load the library

#HazeImg = cv2.imread('C:/Users/Fatih Kemal Terzi/.spyder-py3/fog.png')		
HazeImg = cv2.imread('haze.png')
HazeCorrectedImg, HazeMap = image_dehazer.remove_haze(HazeImg)		# Remove Haze

cv2.imshow('input image', HazeImg);						# display the original hazy image
cv2.imshow('enhanced_image', HazeCorrectedImg);			# display the result
cv2.imshow('HazeMap', HazeMap);							# display the HazeMap
cv2.waitKey(0)											# hold the display window


### user controllable parameters (with their default values):
airlightEstimation_windowSze=15
boundaryConstraint_windowSze=3
C0=20
C1=300
regularize_lambda=0.1
sigma=0.5
delta=0.85
showHazeTransmissionMap=True
