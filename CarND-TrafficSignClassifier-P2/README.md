**Traffic Sign Recognition** 

---

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report

[//]: # (Image References)

[image1]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/data1.png "Visualization"
[image2]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/data2.png "Visualization"
[image3]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/original.png
[image4]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/grayscale.png
[image5]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/shuffled.png
[image6]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/new_imgs.png "Traffic Sign 2"
[image7]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/priority-road.png
[image8]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/stop.png
[image9]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/no-vehicles.png
[image10]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/bumpy-road.png
[image11]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/road-narrows-on-the-right.png
[image12]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/traffic-signs.png
[image13]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/wild-animals-crossing.png
[image14]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/go-straight-or-left.png
[image15]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/end-of-no-passing.png
[image16]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/normalize.png
[image17]: https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/writeup_images/sermanet.jpg

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/481/view) individually and describe how I addressed each point in my implementation.  

---
### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one. You can submit your writeup as markdown or pdf. You can use this template as a guide for writing the report. The submission includes the project code.

Here is a link to my [project code](https://github.com/piliwilliam0306/Udacity-SDC/blob/master/CarND-TrafficSignClassifier-P2/P2.ipynb)

### Data Set Summary & Exploration

#### 1. Provide a basic summary of the data set. In the code, the analysis should be done using python, numpy and/or pandas methods rather than hardcoding results manually.

I used the pandas library to calculate summary statistics of the traffic
signs data set:

* The size of training set: 34799 samples.
* The size of the validation set: 4410 samples.
* The size of test set: 12630 samples.
* The shape of a traffic sign image: (32, 32, 3).
* The number of unique classes/labels in the data set: 43 classes.

#### 2. Include an exploratory visualization of the dataset.

Here is an exploratory visualization of the data set:

![alt text][image1]

![alt text][image2]

### Design and Test a Model Architecture

#### 1. Describe how you preprocessed the image data. What techniques were chosen and why did you choose these techniques? Consider including images showing the output of each preprocessing technique. Pre-processing refers to techniques such as converting to grayscale, normalization, etc. (OPTIONAL: As described in the "Stand Out Suggestions" part of the rubric, if you generated additional data for training, describe why you decided to generate additional data, how you generated the data, and provide example images of the additional data. Then describe the characteristics of the augmented training set like number of images in the set, number of images for each class, etc.)

##### Pre-processing:
* Since recognizing traffic signs does not require color information, I first converted RGB images to grayscale, which then normalized to scale 0 to 1. 
* By doing so, we should get zero mean and equal variance which helps when performing gradient descent optimization. 

![alt text][image16]

* Furthermore, I applied localized histogram equalization (CLAHE) which improves feature extraction.

Here is an example of a traffic sign image before and after grayscaling and normalization:

![alt text][image3]

![alt text][image4]

##### Image Augmentation:

* In order to prevent overfitting, I have decided to generate addtional data such as rotating, shifting, shearing and zooming of the original images with the help of Keras ImageDataGenerator class.
* Image blur technique was also used to generate more data.
* Save all preprocessed and agumentated images as pickle file for training.

Here is an example of an original image and an augmented image:

![alt text][image3]

![alt text][image5]


#### 2. Describe what your final model architecture looks like including model type, layers, layer sizes, connectivity, etc.) Consider including a diagram and/or table describing the final model.

My final model consisted of the following layers:

| Layer         		|     Description	        					| 
|:---------------------:|:---------------------------------------------:| 
| Input         		| 32x32x1 grayscale image   							| 
| Convolution 3x3     	| 1x1 stride, valid padding, outputs 28x28x12 	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 14x14x12 				|
| Dropout	(1)      	| 0.8 				|
| Convolution 3x3	    | 1x1 stride, valid padding, outputs 10x10x24   |
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 5x5x24 				|
| Dropout	(2)      	| 0.6 				|
| Fully connected		| input = flatten(max_pooling(1)) + flatten((2)) = 1188. Output = 320 |      
| Dropout	      	| 0.5 				|
| Fully connected		| Input = 320, output = 43 |
| Softmax				|         									|


#### 3. Describe how you trained your model. The discussion can include the type of optimizer, the batch size, number of epochs and any hyperparameters such as learning rate.

* To train the model, rather than tuning mu and sigma for truncated_normal initializer , I used Xavier initializer which determines the scale of initialization based on the layers’ dimensions automatically.
* I then used 30 epochs with a batch size of 128 and AdamOptimizer with a learning rate of 0.001 for training. 

#### 4. Describe the approach taken for finding a solution and getting the validation set accuracy to be at least 0.93. Include in the discussion the results on the training, validation and test sets and where in the code these were calculated. Your approach may have been an iterative process, in which case, outline the steps you took to get to the final solution and why you chose those steps. Perhaps your solution involved an already well known implementation or architecture. In this case, discuss why you think the architecture is suitable for the current problem.

My final model results were:
* training set accuracy of 0.998
* validation set accuracy of 0.971
* test set accuracy of 0.967

The network architecture I used was the [Traffic Sign Recognition with Multi-Scale Convolutional Networks](http://yann.lecun.com/exdb/publis/pdf/sermanet-ijcnn-11.pdf) which mentioned in the ipynb Udacity provided.

![alt text][image17]

The performance of such architecture was convining since the author achieved result of 99.17% which is better than human.

The difference of of the architecture between mine and [Sermanet](http://yann.lecun.com/exdb/publis/pdf/sermanet-ijcnn-11.pdf) are:
1. One less convolution layer which reduces amount of parameters for training.
2. Using ReLU activation function which is commonly used recently instead of tanh.
3. Adding Dropping and L2 regularization to prevent overfitting.

### Test a Model on New Images

#### 1. Choose five German traffic signs found on the web and provide them in the report. For each image, discuss what quality or qualities might be difficult to classify.

Here are nine German traffic signs that I found on the web:

![alt text][image6] 


#### 2. Discuss the model's predictions on these new traffic signs and compare the results to predicting on the test set. At a minimum, discuss what the predictions were, the accuracy on these new predictions, and compare the accuracy to the accuracy on the test set (OPTIONAL: Discuss the results in more detail as described in the "Stand Out Suggestions" part of the rubric).

Here are the results of the prediction:

| Image			        |     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| Priority road      		| Priority road   									| 
| Stop     			| Stop 										|
| No vehicles					| No vehicles											|
| Bumpy road	      		| Bumpy Road					 				|
| Road	narrows on the right		| Road	narrows on the right      							|
| Traffic signals		| Traffic signals      							|
| Wild animals crossing		| Wild animals crossing      							|
| Go straight or left		| Go straight or left      							|
| End of no passing		| End of no passing      							|

* The model was able to correctly guess 9 of the 9 traffic signs, which gives an accuracy of 100%. 
* Compare with test set result, the new images from web performs better since the images were pretty clear.

#### 3. Describe how certain the model is when predicting on each of the five new images by looking at the softmax probabilities for each prediction. Provide the top 5 softmax probabilities for each image along with the sign type of each probability. (OPTIONAL: as described in the "Stand Out Suggestions" part of the rubric, visualizations can also be provided such as bar charts)

The top five soft max probabilities for the new images are as follows:
<!--
| Probability         	|     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| .60         			| Stop sign   									| 
| .20     				| U-turn 										|
| .05					| Yield											|
| .04	      			| Bumpy Road					 				|
| .01				    | Slippery Road      							|
-->
![alt text][image7]

![alt text][image8] 

![alt text][image9] 

![alt text][image10] 

![alt text][image11] 

![alt text][image12]

![alt text][image13] 

![alt text][image14] 

![alt text][image15]


### (Optional) Visualizing the Neural Network (See Step 4 of the Ipython notebook for more details)
#### 1. Discuss the visual output of your trained network's feature maps. What characteristics did the neural network use to make classifications?
