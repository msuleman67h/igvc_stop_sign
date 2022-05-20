# IGVC Stop Sign    
 This package allows to implement the stop sign functionality. It determines if we are near stop sign by comparing the stop sign position with the car position. Once we are within the specified radius, it triggers the `/purepursuit/stop` flag which stops the car to a few seconds. 
  
## Requires  
Following are the requirements for the package.  
- Python 2.7  
- ROS Melodic  
  
## Building the package     
```commandline  
catkin build
```  
or 
```commandline  
catkin_make
```  
  
## Running the package  
It is recommended that you run the package with [igvc_estop](https://github.com/msuleman67h/igvc_estop). The launch file in igvc_stop will automatically launch this node. 

### roslaunch 
To launch the package, simple use `roslaunch` command.  
```commandline  
source devel/setup.bash  
roslaunch igvc_stop_sign stop_sign_behavior.launch   
```  

Credit: 
https://github.com/Aixcalibur/pure_pursuit_stop