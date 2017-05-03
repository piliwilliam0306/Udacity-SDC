# Behavioral-Cloning

## Getting Udacity Self-Driving Car Simulator
```
$ wget https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5831f0f7_simulator-linux/simulator-linux.zip
$ wget https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58983558_beta-simulator-linux/beta-simulator-linux.zip
```

## Removing annoying Unity logs
```
$ rm /home/ar/.config/unity3d/Udacity/self_driving_car_nanodegree_program/Player.log
```
## Collecting Data

getting training data from Udacity
```
$ wget -nc "https://d17h27t6h515a5.cloudfront.net/topher/2016/December/584f6edd_data/data.zip"
```
### splitting data to training and validation set command line way
using 'head' command to read the first few lines
```
$ head driving_log.csv
center,left,right,steering,throttle,brake,speed
IMG/center_2016_12_01_13_30_48_287.jpg, IMG/left_2016_12_01_13_30_48_287.jpg, IMG/right_2016_12_01_13_30_48_287.jpg, 0, 0, 0, 22.14829
IMG/center_2016_12_01_13_30_48_404.jpg, IMG/left_2016_12_01_13_30_48_404.jpg, IMG/right_2016_12_01_13_30_48_404.jpg, 0, 0, 0, 21.87963
IMG/center_2016_12_01_13_31_12_937.jpg, IMG/left_2016_12_01_13_31_12_937.jpg, IMG/right_2016_12_01_13_31_12_937.jpg, 0, 0, 0, 1.453011
IMG/center_2016_12_01_13_31_13_037.jpg, IMG/left_2016_12_01_13_31_13_037.jpg, IMG/right_2016_12_01_13_31_13_037.jpg, 0, 0, 0, 1.438419
IMG/center_2016_12_01_13_31_13_177.jpg, IMG/left_2016_12_01_13_31_13_177.jpg, IMG/right_2016_12_01_13_31_13_177.jpg, 0, 0, 0, 1.418236
IMG/center_2016_12_01_13_31_13_279.jpg, IMG/left_2016_12_01_13_31_13_279.jpg, IMG/right_2016_12_01_13_31_13_279.jpg, 0, 0, 0, 1.403993
IMG/center_2016_12_01_13_31_13_381.jpg, IMG/left_2016_12_01_13_31_13_381.jpg, IMG/right_2016_12_01_13_31_13_381.jpg, 0, 0, 0, 1.389892
IMG/center_2016_12_01_13_31_13_482.jpg, IMG/left_2016_12_01_13_31_13_482.jpg, IMG/right_2016_12_01_13_31_13_482.jpg, 0, 0, 0, 1.375934
IMG/center_2016_12_01_13_31_13_584.jpg, IMG/left_2016_12_01_13_31_13_584.jpg, IMG/right_2016_12_01_13_31_13_584.jpg, 0, 0, 0, 1.362115
```
use 'wc -l' command to print out length of the file
```
$ wc -l driving_log.csv
8037 driving_log.csv
```
randomize and separate data to training and validation data
```
$ cat data/driving_log.csv | tail -n+2 | shuf > data/driving_log_all.csv
$ cat data/driving_log_all.csv | head -n7000 > data/driving_log_train.csv
$ cat data/driving_log_all.csv | tail -n+7001 > data/driving_log_validation.csv
```
checking length of file
```
$ wc -l data/driving_log_train.csv
$ wc -l data/driving_log_validation.csv
7000 data/driving_log_train.csv
1036 data/driving_log_validation.csv
```
### splitting data to training and validation set sklearn way
```
images_train, images_validation, angles_train, angles_validation = train_test_split(
    images, angles, test_size=0.15, random_state=42)
```
