
import os
import cv2
import pickle

with open("Camera_Calibration_output/calibration.pkl","rb") as file:
    cameraMatrix, dist= pickle.load(file)

parent_dir='drawn_chessboard/'
images = os.listdir(parent_dir)

############## UNDISTORTION #####################################################

img = cv2.imread(os.path.join(parent_dir,images[0]))
h,  w = img.shape[:2]
newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(cameraMatrix, dist, (w,h), 1, (w,h))

if os.path.exists("undistorted_chessboard_images/") is False:
    os.makedirs("undistorted_chessboard_images/")

for image in images:
    img = cv2.imread(os.path.join(parent_dir, image))

    # Undistort
    dst = cv2.undistort(img, cameraMatrix, dist, None, newCameraMatrix)

    # crop the image
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    cv2.imwrite(os.path.join("undistorted_chessboard_images", image[:-4]+"_undistorted.jpg"), dst)

    # Undistort with Remapping
    mapx, mapy = cv2.initUndistortRectifyMap(cameraMatrix, dist, None, newCameraMatrix, (w,h), 5)
    dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

    # crop the image
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    cv2.imwrite(os.path.join("undistorted_chessboard_images", image[:-4]+"_undistorted_remapped.jpg"), dst)

