import cv2
import numpy as np
import matplotlib.pyplot as plt



def printArucoDict(image):
    #Detect aruco dictionary used; Guideline: use as low number as possible
    ARUCO_DICT = {
    	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
    	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
    	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
    	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
    	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
    	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
    	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
    	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
    	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
    	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
    	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
    	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
    	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
    	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
    	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
    	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
    	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
    	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
    	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
    	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
    	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
    }

    for (arucoName, arucoDict) in ARUCO_DICT.items():
        # load the ArUCo dictionary, grab the ArUCo parameters, and
    	# attempt to detect the markers for the current dictionary
        arucoDict = cv2.aruco.getPredefinedDictionary(arucoDict)
        arucoParams = cv2.aruco.DetectorParameters()
        (corners, ids, rejected) = cv2.aruco.detectMarkers(
            image, arucoDict, parameters=arucoParams)
        # if at least one ArUco marker was detected display the ArUco
    	# name to our terminal
        if len(corners) > 0:
            print("[INFO] detected {} markers for '{}'".format(
    			len(corners), arucoName))

def showMarkers(image, corners, channel = 3):
    '''Display marker on iamge'''
    image_copy = image.copy()
    for corner in corners:
        topLeft = corner.squeeze(0)[0].astype('int')
        topRight = corner.squeeze(0)[1].astype('int')
        bottomRight = corner.squeeze(0)[2].astype('int')
        bottomLeft = corner.squeeze(0)[3].astype('int')
        cv2.line(image_copy, topLeft, bottomLeft, (0,0,255), 10)
        cv2.line(image_copy, topLeft, topRight, (0,0,255), 10)
        cv2.line(image_copy, bottomLeft, bottomRight, (0,0,255), 10)
        cv2.line(image_copy, bottomRight, topRight, (0,0,255), 10)
        plt.imshow(image_copy[:,:,::-1]) if channel == 3 else plt.imshow(image_copy, cmap='gray')

def crop_image(image, remove_markers = False, dict_used = cv2.aruco.DICT_4X4_50, show=False):
    '''
    return a new cropped image with marker outer bounds
    expect image channel: 3
    expected corner structure: tuple with each element shaped (1,4,2)
    '''
    arucoDict = cv2.aruco.getPredefinedDictionary(dict_used)
    
    corners, ids, rejected = cv2.aruco.detectMarkers(
		image, arucoDict, parameters=cv2.aruco.DetectorParameters())

    edge = np.array(corners).squeeze(1) #shape = (?, 4, 2)
    
    if edge.shape[0] != 4:
        print('must have 4 markers, only {} was detected. Try to downsample image or change dictionary'.format(edge.shape[0]))
        return
    
    edge = edge.reshape((16,2))
    min_x = min(edge[:, 0]).astype('int')
    max_x = max(edge[:, 0]).astype('int')
    min_y = min(edge[:, 1]).astype('int')
    max_y = max(edge[:, 1]).astype('int')
    
    #################################################################################
    ########### TODO: Estimate background to find color to fill in!! ################
    #################################################################################
    
    image_copy = image.copy()
    if remove_markers is True:
        for corner in corners:
            background_color = (255,255,255)
            cv2.fillPoly(image_copy, np.array(corner.astype('int')), background_color, cv2.LINE_AA)
            
    crop_image = image_copy[min_y:max_y, min_x:max_x]
    
    if show is True:
        image_copy = image.copy()
        cv2.line(image_copy, (min_x,min_y), (min_x,max_y), (0,0,255), 10)
        cv2.line(image_copy, (min_x,min_y), (max_x,min_y), (0,0,255), 10)
        cv2.line(image_copy, (max_x,min_y), (max_x,max_y), (0,0,255), 10)
        cv2.line(image_copy, (min_x,max_y), (max_x,max_y), (0,0,255), 10)
        plt.figure(figsize=(25,25))
        plt.subplot(1,2,1)
        plt.imshow(image_copy[:,:,::-1])
        plt.subplot(1,2,2)
        plt.imshow(crop_image[:,:,::-1])
        

    return crop_image