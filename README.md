# Robofest-rover-opencv

Computer vision part of the rover.

<p>The cameras on the rover will capture the surroundings which will help with slope estimation of the terrain, object detection and segmentation. The object detection is done using the YOLOv8 model. For calculating the slope of the terrain, we can use a stereo vision camera setup which will find the depth of each pixel in the image of the terrain. From the depth map, we can easily find the slope between any two points of the terrain.</p>

