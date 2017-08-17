## Vehicle Detection Project

---

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector. 
* Note: for those first two steps don't forget to normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

[//]: # (Image References)
[image1]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Vehicle-Detection-P5/writeup_images/vis.png
[image2]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Vehicle-Detection-P5/writeup_images/HOG.png
[image3]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Vehicle-Detection-P5/writeup_images/ROI.png
[image4]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Vehicle-Detection-P5/writeup_images/scale.png
[image5]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Vehicle-Detection-P5/writeup_images/heat.png

[video1]: ./project_video.mp4

## [Rubric](https://review.udacity.com/#!/rubrics/513/view) Points
### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---
### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  [Here](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Vehicle-Detection-P5/writeup_template.md) is the link for my writeup.

You're reading it!

### Histogram of Oriented Gradients (HOG)

#### 1. Explain how (and identify where in your code) you extracted HOG features from the training images.

* The code for this step is contained in the first code cell of the [IPython notebook](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Vehicle-Detection-P5/P5.ipynb).

* I started by reading in all the `vehicle` and `non-vehicle` images.  Here is an example of 10 random images of the `vehicle` and `non-vehicle` classes:

![alt text][image1]

* I then explored  different `skimage.hog()` parameters (`orientations`, `pixels_per_cell`, and `cells_per_block`).  I grabbed 10 random images from each of the two classes and displayed them to get a feel for what the `skimage.hog()` output looks like.

* Here is an example using the `YUV` color space and HOG parameters of `orientations=11`, `pixels_per_cell=(16, 16)` and `cells_per_block=(2, 2)`:

![alt text][image2]

#### 2. Explain how you settled on your final choice of HOG parameters.

* Since the final goal is to detect the cars in real time, the final choice of HOG parameters I chose was based on the time take for the classifier to make prediction and the accuracy of the classifier. Using `YUV` color space and HOG parameters of `orientations=11`, `pixels_per_cell=(16, 16)` and `cells_per_block=(2, 2)` was the best result which required least time while maintaining high accuracy.

#### 3. Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them).

* In the `HOG Classify` section, I splitted the data into training and test set to prevent overfitting and to test accuracy. With the parameters mention above and default parameters of SVM classifier, the classifier was able to achieve accuracy of 98.17%.

### Sliding Window Search

#### 1. Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows?

* Here is an example of sliding window with size of 64X64 and 50% overlapping:
![alt text][image3]

* However, since the size of the cars varys when they are far away or closer, I decided to use various scale size to search to make sure the vehicles could be found.

#### 2. Show some examples of test images to demonstrate how your pipeline is working.  What did you do to optimize the performance of your classifier?

* In order to reduce the search time and the possibility of false positives, I used different size of scale to scan specific region rather than searching the entire image.

![alt text][image4]
---

### Video Implementation

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (somewhat wobbly or unstable bounding boxes are ok as long as you are identifying the vehicles most of the time with minimal false positives.)

* Here is the result for vehicle detection:

[![IMAGE ALT TEXT HERE](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Vehicle-Detection-P5/writeup_images/car_detect.gif)](https://youtu.be/TfBQNnJpf-U)

* Here is the result detecting both lanes and vehicles:

[![IMAGE ALT TEXT HERE](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-Vehicle-Detection-P5/writeup_images/car_lane_detect.gif)](https://youtu.be/PUkIQ6nfKlk)


#### 2. Describe how (and identify where in your code) you implemented some kind of filter for false positives and some method for combining overlapping bounding boxes.

* I recorded the positions of positive detections in each frame of the video.  From the positive detections I created a heatmap and then thresholded that map to identify vehicle positions.  I then used `scipy.ndimage.measurements.label()` to identify individual blobs in the heatmap.  I then assumed each blob corresponded to a vehicle.  I constructed bounding boxes to cover the area of each blob detected.   
* Here's an example result showing the heatmap from a series of frames of video, the result of `scipy.ndimage.measurements.label()` and the bounding boxes then overlaid on the last frame of video:
![alt text][image5]

* I also used `Track_Rectangle` class to record previous 15 frame of images in order to filter out the false positives.

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

* The problems I faced were mostly about finetuning HOG parameters, search window size, overlapping range, and which color space to use.
Moreover, it required lots of time to process images since I'm using serial programming.

* The pipeline would likely to fail if the vehicles were not in the training set or search window did not cover enough regions.

* Trainning better classifier or better coverage of search window could help making the vehicle detection more robust. Moreover, I would love to try out deep learning techniques such as [SqueezeDet](https://arxiv.org/pdf/1612.01051) or [SSD](https://arxiv.org/pdf/1512.02325) to detect the vehicles.
