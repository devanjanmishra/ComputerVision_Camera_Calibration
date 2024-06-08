# Camera Calibration using ComputerVision & Chessboard Images
Calculate Camera intrinsic parameter including intrinsic and distortion matrix using Chessboard Images

## Prepare a Chessboard Image:  
1) Use a standard chessboard image for calibration. Typically, an 8x6 or 9x6 chessboard is used, where 8 and 9 are the number of squares along row and 6 is the number of square along column.[Reference Image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/b61d375f-1170-4c86-afd9-a0661ddb442d) has 9 square along rows and 6 along columns.
2) Ensure that the chessboard squares are of equal size and the image is clear and well-lit. You can use [chessboard_creation](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/blob/main/create_sample_chessboard_image.py) script to create your own image.  
3) Print the chessboard pattern on paper and capture images of it using your camera from different angles. Sample images are stored in [chessboard_image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/tree/main/chessboard_images) folder.  


## Calibration Matrix Calculation from Chessboard Images
Code walkthrough and all the important steps are covered in [camera_calibration.md](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/blob/main/camera_calibration.md)

## Undistorting Remapping Internal-Vetices-Drawn Images
Calculate the undistorted, remapped images using the previously calculated Camera Matrix and Distortion Coefficients. The sample [output](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/tree/main/undistorted_chessboard_images) is produced from undistorted [script](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/blob/main/camera_image_distortion.py) .  

Here is the sample of input chessboard images, their corresponnding internal-vertices-drawn images and corresponding undistorted remapped images.  
![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/b402ecad-83e8-42d6-9dd3-a57b3b957a58)
![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/e4e723d2-3f6a-495c-ae9c-20065c16b7fb)
![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/a1e84de8-cb58-438c-b9bc-b9feaa7c89d5)
![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/a2eeba76-15e3-468b-aeca-5bb63514ce6d)
![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/3de60ca6-95fd-45a4-a362-18ad7ca874c4)
![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/521250f5-1d7f-404e-9b94-1a7cd98485af)
![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/c134e89d-6aff-4ac8-a502-0086e26bac62)
![image](https://github.com/devanjanmishra/ComputerVision_Camera_Calibration/assets/50066136/edf8916d-75b3-4765-a5f0-76cf3250057a)

