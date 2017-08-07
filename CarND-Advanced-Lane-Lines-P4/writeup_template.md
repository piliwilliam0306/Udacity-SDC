## Writeup Template

---

**Advanced Lane Finding Project**

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[image1]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/output_images/calibrate.png "Calibrate"
[image2]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/output_images/abs.png "Abosolute"
[image3]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/output_images/mag_dir.png "Magnitude"
[image4]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/output_images/color_thresh.png "Color"
[image5]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/output_images/binary_warped.png "Warped"
[image6]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/output_images/sliding_window.png "Window"
[image7]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/output_images/margin_search.png "Margin"
[image8]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/output_images/final.png "Final"
[image9]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/output_images/undistorted.png "Undistorted"


## [Rubric](https://review.udacity.com/#!/rubrics/571/view) Points

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  [Here](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/writeup_template.md) is my writeup for this project.  

You're reading it!

### Camera Calibration

#### 1. Briefly state how you computed the camera matrix and distortion coefficients. Provide an example of a distortion corrected calibration image.

The code for this step is contained in the Camera Calibration section of the IPython notebook located [here](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/P4.ipynb)

* I start by preparing "object points", which will be the (x, y, z) coordinates of the chessboard corners in the world. Here I am assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image.  Thus, `objp` is just a replicated array of coordinates, and `objpoints` will be appended with a copy of it every time I successfully detect all chessboard corners in a test image.  `imgpoints` will be appended with the (x, y) pixel position of each of the corners in the image plane with each successful chessboard detection.  

* I then used the output `objpoints` and `imgpoints` to compute the camera calibration and distortion coefficients using the `cv2.calibrateCamera()` function.  I applied this distortion correction to the test image using the `cv2.undistort()` function: 

![alt text][image1]

### Pipeline (single images)

#### 1. Provide an example of a distortion-corrected image.

* I applied the camera calibration and distortion coefficients we computed earlier and use `cv2.undistort()` function to undistort the image:
![alt text][image9]

#### 2. Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image.  Provide an example of a binary image result.

* First I took the derivative in x and y and took the absolute value of the derivative or gradient, then return the binary image with the threshold range 20-100. Below is the result:
![alt text][image2]

* Second, I computed the direction and the magnitude of the gradient and experiment with different sobel_kernel and threshold:
![alt text][image3]

* After fine tuning the threshold, I could filter out white color from RGB color space and yellow color from HSV color space. By combing them, we get a pretty clear image of the lanes.
![alt text][image4]

* Finally, I have decided only use color filter since it does a decent job to filter the lanes and require less computation and time for tuning the parameters.

#### 3. Describe how (and identify where in your code) you performed a perspective transform and provide an example of a transformed image.

* I manually pin-pointed the source and destination points in the image, here are the coordinates I chose:

| Source        | Destination   | 
|:-------------:|:-------------:| 
| 581, 477      | 384, 0        | 
| 699, 477      | 896, 0        |
| 896, 675      | 896, 720      |
| 384, 675      | 384, 720      |

* First I used `cv2.getPerspectiveTransform()` function to find perspective transform matrix.

* The code for my perspective transform includes a function called `perspect_tf()`, which can be used to warp the image to bird-eye view with the perspective transform matrix we got.

* I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image.

![alt text][image5]

#### 4. Describe how (and identify where in your code) you identified lane-line pixels and fit their positions with a polynomial?

* We then scan the resulting frame from bottom to top trying to isolate pixels that could be representing lane boundaries. What we are trying to detect is two lines that would make up lane boundaries. For each of those lines we have a set of windows. We scan the frame with those windows, collecting non-zero pixels within window bounds. Once we reach the top, we try to fit a second order polynomial into collected points. This polynomial coefficients would represent a single lane boundary.

![alt text][image6]

* Once the lane was detected through the sliding window approach, we know where the lines are in one frame of video. We can then search in a margin around the previous line position in stead of blind search again.

![alt text][image7]

#### 5. Describe how (and identify where in your code) you calculated the radius of curvature of the lane and the position of the vehicle with respect to center.



#### 6. Provide an example image of your result plotted back down onto the road such that the lane area is identified clearly.

* Using 'perspect_tf()' and the inverse matrix we got earlier, we can warp back from bird-eye view to first-person view

![alt text][image8]

---

### Pipeline (video)

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (wobbly lines are ok but no catastrophic failures that would cause the car to drive off the road!).

Below is the link to my video result.

[![IMAGE ALT TEXT HERE](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/output_images/project_video.gif)](https://youtu.be/oSamJ6EsAiU)

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

The biggest challenge for this project is to fine tune the threshold which can generalize for different weather condition or very sharp curves. For computer vision method, a better tuned parameter could help to make it more robust. However, I would love to try a deep learning approach inverted by Ford called [DeepLanes](https://news.developer.nvidia.com/ford-research-using-deep-learning-for-lane-detection/) to improve the robustness.

