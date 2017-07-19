# **Behavioral Cloning** 

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


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
[image10]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/model.png "Model"
[image11]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/sterring_angle.png "steering"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup_report.md or writeup_report.pdf summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable
* Here is the link to my [project notebook](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/P3.ipynb), which shows the pipeline for data preprocess, augmentation, and network training.
* The model.py file contains the code for loading pickle file, training, and saving the convolution neural network.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

* My model consists of a convolution neural network with 3x3 filter sizes and depths between 32 and 128 (model.py lines 18-24) 

The model includes RELU layers to introduce nonlinearity (code line 20), and the data is normalized in the model using a Keras lambda layer (code line 18). 

#### 2. Attempts to reduce overfitting in the model

The model contains dropout layers in order to reduce overfitting (model.py lines 21). 
early stopping

The model was trained and validated on different data sets to ensure that the model was not overfitting. The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 25).

#### 4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used a combination of center lane driving, recovering from the left and right sides of the road ... 

For details about how I created the training data, see the next section. 



### Model Architecture and Training Strategy

#### 1. Solution Design Approach


#### 2. Final Model Architecture

The final model architecture (model.py lines 18-24) consisted of a convolution neural network with the following layers and layer sizes ...

Here is a visualization of the architecture (note: visualizing the architecture is optional according to the project rubric)

![alt text][image1]

#### 3. Creation of the Training Set & Training Process

![alt text][image2]

![alt text][image3]
![alt text][image4]


![alt text][image5]
![alt text][image6]

![alt text][image10]
![alt text][image11]

### Final results

#### Track1 from unity
[![IMAGE ALT TEXT HERE](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/unity1.png)](https://youtu.be/suB09shs-Dg)

#### Track1 center view
[![IMAGE ALT TEXT HERE](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/original.gif)](https://youtu.be/1vZ01dx5Xm4)

#### Track1 after cropped
[![IMAGE ALT TEXT HERE](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-BehavioralCloning-P3/images/crop.gif)](https://youtu.be/bFymz0zy-18)

### Visualize attention

![alt text][image7]
![alt text][image8]
![alt text][image9]
