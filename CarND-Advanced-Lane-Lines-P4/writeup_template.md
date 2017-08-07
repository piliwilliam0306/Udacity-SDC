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


## [Rubric](https://review.udacity.com/#!/rubrics/571/view) Points

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  [Here](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/writeup_template.md) is my writeup for this project.  

You're reading it!

### Camera Calibration

#### 1. Briefly state how you computed the camera matrix and distortion coefficients. Provide an example of a distortion corrected calibration image.

The code for this step is contained in the Camera Calibration section of the IPython notebook located [here](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/P4.ipynb)

I start by preparing "object points", which will be the (x, y, z) coordinates of the chessboard corners in the world. Here I am assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image.  Thus, `objp` is just a replicated array of coordinates, and `objpoints` will be appended with a copy of it every time I successfully detect all chessboard corners in a test image.  `imgpoints` will be appended with the (x, y) pixel position of each of the corners in the image plane with each successful chessboard detection.  

I then used the output `objpoints` and `imgpoints` to compute the camera calibration and distortion coefficients using the `cv2.calibrateCamera()` function.  I applied this distortion correction to the test image using the `cv2.undistort()` function and obtained this result: 

![alt text][image1]

### Pipeline (single images)

#### 1. Provide an example of a distortion-corrected image.

To demonstrate this step, I will describe how I apply the distortion correction to one of the test images like this one:


#### 2. Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image.  Provide an example of a binary image result.

* First I took the derivative in x and y and took the absolute value of the derivative or gradient, then return the binary image with the threshold range 20-100. Below is the result:
![alt text][image2]

* Second, I computed the direction and the magnitude of the gradient and experiment with different sobel_kernel and threshold:
![alt text][image3]

* After fine tuning the threshold, I could filter out white color from RGB color space and yellow color from HSV color space. By combing them, we get a pretty clear image of the lanes.
![alt text][image4]

* Finally, I have decided only use color filter since it does a decent job to filter the lanes and require less computation and time for tuning the parameters.

#### 3. Describe how (and identify where in your code) you performed a perspective transform and provide an example of a transformed image.

The code for my perspective transform includes a function called `warper()`, which appears in lines 1 through 8 in the file `example.py` (output_images/examples/example.py) (or, for example, in the 3rd code cell of the IPython notebook).  The `warper()` function takes as inputs an image (`img`), as well as source (`src`) and destination (`dst`) points.  I chose the hardcode the source and destination points in the following manner:

This resulted in the following source and destination points:

| Source        | Destination   | 
|:-------------:|:-------------:| 
| 581, 477      | 384, 0        | 
| 699, 477      | 896, 0        |
| 896, 675      | 896, 720      |
| 384, 675      | 384, 720      |

I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image.

![alt text][image5]

#### 4. Describe how (and identify where in your code) you identified lane-line pixels and fit their positions with a polynomial?

Then I did some other stuff and fit my lane lines with a 2nd order polynomial kinda like this:

![alt text][image6]

![alt text][image7]

#### 5. Describe how (and identify where in your code) you calculated the radius of curvature of the lane and the position of the vehicle with respect to center.



#### 6. Provide an example image of your result plotted back down onto the road such that the lane area is identified clearly.

I implemented this step in lines # through # in my code in `yet_another_file.py` in the function `map_lane()`.  Here is an example of my result on a test image:

![alt text][image8]

---

### Pipeline (video)

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (wobbly lines are ok but no catastrophic failures that would cause the car to drive off the road!).
<!--
Here's a [link to my video result](./project_video.mp4)
-->
Below is the link to my video result.

[![IMAGE ALT TEXT HERE](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Advanced-Lane-Lines-P4/output_images/project_video.gif)](https://youtu.be/oSamJ6EsAiU)

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

Here I'll talk about the approach I took, what techniques I used, what worked and why, where the pipeline might fail and how I might improve it if I were going to pursue this project further.  
