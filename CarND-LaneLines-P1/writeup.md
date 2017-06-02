# **Finding Lane Lines on the Road** 

## Reflection

## 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.
### My pipeline has the following steps:
* Convert image into grayscale: grayscale()
* Apply Gaussian smoothing: gaussian_blur()
* Run Canny Edge Detector: canny()
* Create a trapezoidal region-of-interest: region_of_interest()
* Run Hough Line Detector: hough_lines()
* Draw the lines: draw_lines_improved()
* Overlay lines on the original image: weighted_img()
### Improving the draw_lines() function:
* Separate lines by slope and endpoint location, if the lines have positive slope and on the left side of the image, then we group them into left lines, if the lines have negative slope and on the right side of the image, then we group them into right lines.
* Then I applied the numpy.polyfit() linear regression function on candidate right and left line segment endpoints to find right and left line slope and intercept.
* Applying the slope and intercept in the y = slope * x + intercept euqation to find the upper and lower x coordinate.
* Draw the lines on the image.
## 2. Identify potential shortcomings with your current pipeline
* if the camera was located differently, the ROI would be different.
* if there were cars or pedestrians that block the lanes.
* if the weather condition was different.

## 3. Suggest possible improvements to your pipeline
* Tuning the parameters based on different weather conditions or location of shadows.
* Can probably use some machine learning algorithms to tune the parameters.
