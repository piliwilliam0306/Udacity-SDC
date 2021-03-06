# **Behavioral Cloning** 

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior.
* Build, a convolution neural network in Keras that predicts steering angles from images.
* Train and validate the model with a training and validation set.
* Test that the model successfully drives around track one without leaving the road.
* Summarize the results with a written report.


[//]: # (Image References)

[image1]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/original_data.png "Data Visualization"
[image2]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/preprocessed_data.png "Data Preprocessed"
[image3]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/model.png "Visualize Model"
[image4]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/loss.png "Loss plot"
[image5]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/original.png "Original Image"
[image6]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/flipped.png "Flipped Image"
[image7]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/left.png
[image8]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/center.png
[image9]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/right.png
[image11]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/sterring_angle.png "steering"
[image12]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/zeros.png "zeros"
[image13]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/shifted_data.png "shifted"


## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model.
* drive.py for driving the car in autonomous mode.
* model.h5 containing a trained convolution neural network.
* writeup_report.md or writeup_report.pdf summarizing the results.

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable
* Here is the link to my [project notebook](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/P3.ipynb), which shows the pipeline for data preprocess, image augmentation, and network training.
* The model.py file contains the code for loading pickle file, training, and saving the convolution neural network.

### Data Preprocessing

#### 1. Collecting Data 

* Getting training data from Udacity
```
$ wget -nc "https://d17h27t6h515a5.cloudfront.net/topher/2016/December/584f6edd_data/data.zip"
```
#### 2. Visualize Data Distribution
* Using df.hist() to plot:

![alt text][image1]

* From this plot, we can see that we have a lot more zero degree steering angle than others.
* In order to balance out the dataset, I have used df.sample() function to randomly choose 90% of the zero degree steering angle then drop them from the dataframe with df.drop():

![alt text][image12]

* Since Udacity provide 3 cameras on car, shifting the left image by 0.25 and right image by -0.25 allows us to extend the training data:

![alt text][image13]

* We can further extend the data by flipping the images and steering angle.
* Eventually we drop any steering angle has more than 400 counts to balance the data which gives us total 23125 images for training:

![alt text][image2]

#### 3. Image augmentation
* Visualize images with their corresponding angle:

![alt text][image11]

* Our main task is to keep the car in the track in the simulator which is much simpler compare with real world application that require traffic sign recognition and decision making.
* First, I cropped out the sky and the car from the images since we only need to focus on the track.
* I then resized the image to 32X14 and using only saturation channel of the HSV color space which was enough to separate the road with others and reduce the image dimension:

![alt text][image5]

![alt text][image6]

* Finally, save the preprocessed and augmented data as pickle file.

### Model Architecture and Training Strategy

#### 1. Splitting data
* Before training, 85% and 15% of the data were split for training and validation.

#### 2. Model Architecture
* Although the model most commonly used for self-driving application are the Nvidia and the Comma.ai model, it was more than what we need for our lane following application.
* My goal is to create a small network which can deploy on robots with embedded system, so I have created a model as follows:

![alt text][image3]

* Data is first normalized in the model using a Keras lambda layer.
* The data then feed in a convolution layer which consists a filter with size 1X1, valid padding, and RELU activation function to introduce nonlinearity.
* I then added a pooling layer with size 4X4 and stride of 4.
* Fraction of 0.25 dropout layer and early stopping were then introduced to prevent over fitting.
* An Adam optimizer with learning rate of 1e-3 was used for training.
* The model was created through reducing the window and filter size while tested through the simulator and ensuring that the vehicle could stay on the track.
* This network had total 27 parameters which is very efficient for training and deploy on embedded systems.

### Training history visualization

![alt text][image4]

### Final results

#### 1. Track1 from unity
[![IMAGE ALT TEXT HERE](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/unity.gif)](https://youtu.be/suB09shs-Dg)

#### 2. Track1 center view
[![IMAGE ALT TEXT HERE](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/original.gif)](https://youtu.be/1vZ01dx5Xm4)

#### 3. Track1 after cropped
[![IMAGE ALT TEXT HERE](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/crop.gif)](https://youtu.be/bFymz0zy-18)

### Visualize attention
* With the help of [keras-vis](https://github.com/raghakot/keras-vis) library, we can see the important part which the network makes the steering angle decision:

![alt text][image7]
![alt text][image8]
![alt text][image9]

### Additional notes

#### 1. Getting Udacity Self-Driving Car Simulator
```
$ wget https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5831f0f7_simulator-linux/simulator-linux.zip
$ wget https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58983558_beta-simulator-linux/beta-simulator-linux.zip
```

#### 2. Removing annoying Unity logs
```
$ rm /home/ar/.config/unity3d/Udacity/self_driving_car_nanodegree_program/Player.log
```
