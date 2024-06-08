# Camera_Calibration using ComputerVision
Calculate Camera intrinsic parameter including intrinsic and distortion matrix using Chessboard Images

## Prepare a Chessboard Image:  
1) Use a standard chessboard image for calibration. Typically, an 8x6 or 9x6 chessboard is used, where 8 and 9 are the number of squares along row and 6 is the number of square along column.[Reference Image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/b61d375f-1170-4c86-afd9-a0661ddb442d) has 9 square along rows and 6 along columns.
2) Ensure that the chessboard squares are of equal size and the image is clear and well-lit. You can use [chessboard_creation](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/blob/main/create_sample_chessboard_image.py) script to create your own image.  
3) Print the chessboard pattern on paper and capture images of it using your camera from different angles. Sample images are stored in [chessboard_image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/tree/main/chessboard_images) folder.  


## Calibration Important Parameters
The code being referred is present at [camera_calibration](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/blob/main/camera_calibration.py).  
```
################ FIND CHESSBOARD CORNERS - OBJECT POINTS AND IMAGE POINTS #############################

chessboardSize = (8,5)
```
1) Calculalte the internal vertices along row and column for your chessboard image.  
   Example is shown below:    
  There are 8 internal vertices along row (marked blue) and 5 internal vertices along column (marked blue).  
  ![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/49c6b02a-3e3f-4eac-8f23-3dae84d6b29f)


```
size_of_chessboard_squares_mm = 13
```
2) Calculate the actual length of square on paper.  
![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/c1163ca2-9d2c-4dd2-894d-d1d56005892c)


```
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)

size_of_chessboard_squares_mm = 13
objp = objp * size_of_chessboard_squares_mm
```
3) objp are all the internal vertices along chessboard distanced at the same distance on paper as in real world, representing the co-ordinates(x,y,z) in real world.  
![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/8f884df5-211f-492e-bd8c-0a3e6af085ec)



```
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
```
4) 


