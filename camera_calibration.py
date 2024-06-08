import os
import numpy as np
import cv2
import pickle



################ FIND CHESSBOARD CORNERS - OBJECT POINTS AND IMAGE POINTS #############################

chessboardSize = (8,5)

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)


# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)

size_of_chessboard_squares_mm = 13
objp = objp * size_of_chessboard_squares_mm


# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

parent_dir='chessboard_images/'
images = os.listdir(parent_dir)


for image in images:
    # img= cv.imread("new_chessboard_images/WIN_20240607_11_39_48_Pro.jpg")
    # img= cv.imread("C:\camera_computer_vision\corrected_chessboard_images\IMG20240601210906_2.jpg")
    img = cv2.imread(parent_dir+image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    frameSize = gray.shape
    # n1=cv.imwrite("chessboard_images/check12.jpg",gray)
    # # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, chessboardSize,None,)
    print(f"{image}: {ret}: Framesize: {frameSize}")
    # If found, add object points, image points (after refining them)
    if ret == True:

        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(img, chessboardSize, corners2, ret)
        if os.path.exists("drawn_chessboard/") is False:
            os.makedirs("drawn_chessboard/")
        # cv2.imshow(f'{image}', img)  #to showcase the drawn chessboard
        cv2.imwrite(f'drawn_chessboard/{image}', img)
        cv2.waitKey(1000)


cv2.destroyAllWindows()


############## CALIBRATION #######################################################

ret, cameraMatrix, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, frameSize, None, None)

#saving the output
if os.path.exists("Camera_Calibration_output/") is False:
    os.makedirs("Camera_Calibration_output/")
# Save the camera calibration result for later use (we won't worry about rvecs / tvecs)
pickle.dump((cameraMatrix, dist), open( "Camera_Calibration_output/calibration.pkl", "wb" ))
pickle.dump(cameraMatrix, open( "Camera_Calibration_output/cameraMatrix.pkl", "wb" ))
pickle.dump(dist, open( "Camera_Calibration_output/dist.pkl", "wb" ))

