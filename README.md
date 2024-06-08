# Camera Calibration using ComputerVision & Chessboard Images
Calculate Camera intrinsic parameter including intrinsic and distortion matrix using Chessboard Images

## Prepare a Chessboard Image:  
1) Use a standard chessboard image for calibration. Typically, an 8x6 or 9x6 chessboard is used, where 8 and 9 are the number of squares along row and 6 is the number of square along column.[Reference Image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/b61d375f-1170-4c86-afd9-a0661ddb442d) has 9 square along rows and 6 along columns.
2) Ensure that the chessboard squares are of equal size and the image is clear and well-lit. You can use [chessboard_creation](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/blob/main/create_sample_chessboard_image.py) script to create your own image.  
3) Print the chessboard pattern on paper and capture images of it using your camera from different angles. Sample images are stored in [chessboard_image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/tree/main/chessboard_images) folder.  


## Calibration Important Parameters
The code being referred is present at [camera_calibration](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/blob/main/camera_calibration.py).  
1) Calculalte the internal vertices along row and column for your chessboard image.  
```
################ FIND CHESSBOARD CORNERS - OBJECT POINTS AND IMAGE POINTS #############################
chessboardSize = (8,5)
```
   Example is shown below:    
  There are 8 internal vertices along row (marked blue) and 5 internal vertices along column (marked blue).  
  ![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/49c6b02a-3e3f-4eac-8f23-3dae84d6b29f)
  
  
2) Calculate the actual length of square on **paper**. All **units** in further measurements will be the same (mm).  
```
size_of_chessboard_squares_mm = 13
```
![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/c1163ca2-9d2c-4dd2-894d-d1d56005892c)
  


3) objp are all the internal vertices along chessboard distanced at the same distance on paper as in real world, representing the co-ordinates(x,y,z) in real world.  
![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/5a629989-7a85-4e1b-8c08-0abf7d96fb6a)
```
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)

size_of_chessboard_squares_mm = 13
objp = objp * size_of_chessboard_squares_mm
```
  
  
4) Loop through all input images.
   - Convert rgb image to gray.  
   - Calculate coarse corners from chessboard corners (input gray image and internal vertices tuple) using [findChessboardCorners](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html#ga93efa9b0aa890de240ca32b11253dd4a).  
   - If corners are found (ret==True), add the 3d points **obpj** to obpj list.  
   - Calculate the finer corners from initial gray image and coarse corners, using [cornerSubPix](https://docs.opencv.org/4.x/dd/d92/tutorial_corner_subpixels.html).  
   - Add the finer corners to corners list.  
   - Draw the finer corners on the image and save the re-drawn image and save them.  

```
for image in images:
    img = cv2.imread(parent_dir+image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    frameSize = gray.shape
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
        cv2.imwrite(f'drawn_chessboard/{image}', img)
        cv2.waitKey(1000)
```
5) Calculate all the calibration matrix using [calibrateCamera](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html#ga3207604e4b1a1758aa66acb6ed5aa65d).
   - Input  
     - List of list of arrays of 3D points in real-world coordinates. Each array corresponds to the chessboard corners in one image. **obpj list**.  
     - List of list of arrays of finer detected corners 2D points in image coordinates. Each array corresponds to the detected corners in one image.  
     - Tuple of internal vertices along row and column for your chessboard image.  
   - Output
      - **ret**: The root mean square (RMS) re-projection error. It gives a good estimation of the precision of the calibration. Lower values are better.
      - **cameraMatrix** : A 3x3 matrix containing the intrinsic parameters of the camera.  
         ![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/d64b69ee-d2ab-47ef-8040-13539906688b)
      - **dist** : Distortion Coefficients Format: [k1, k2, p1, p2, k3], where:  
           - k1, k2, k3 are the radial distortion coefficients.
           - p1, p2 are the tangential distortion coefficients.
           - If the vector contains more elements, it includes higher-order radial and tangential distortion coefficients.  
      -  **rvecs** : Rotation Vectors- A list of rotation vectors (one for each calibration image) that describe the rotation of the camera relative to the calibration pattern. It can be converted to rotation matrix.
      -  **tvecs** : Translation Vectors- A list of translation vectors (one for each calibration image) that describe the translation of the camera relative to the calibration pattern.

6) Save **cameraMatrix** and **dist** as pkl file for further use in Camera_Calibration_output.  


