## Fire Detection Using Surveillance Camera

## **Project Overview**
This project is a computer vision-based fire detection system that uses surveillance cameras to identify fire and smoke in real time. It analyzes video frames using color detection, motion analysis, and contour detection techniques. When fire is detected, the system triggers an alert to enable quick response and reduce damage.

## **Key Features**
- Real-time fire and smoke detection  
- HSV color-based flame detection  
- Motion detection to reduce false positives  
- Contour analysis for identifying fire regions  
- Alert system (sound/notification)  

## **Technical Stack**
- Python  
- OpenCV  
- NumPy  

## **How It Works**
1. Capture live video from the surveillance camera  
2. Convert video into frames for processing  
3. Detect fire-like colors using HSV color space  
4. Apply motion detection to confirm dynamic behavior  
5. Use contour detection to identify fire regions  
6. Trigger alert if fire is detected continuously  

## **Challenges Faced**
- False positives due to red-colored objects and lighting  
- Difficulty in distinguishing real fire from static bright regions  
- Maintaining performance for real-time detection  

## **Solutions**
- Combined color detection with motion detection  
- Used contour filtering to remove small irrelevant regions  
- Added frame persistence check before triggering alerts  

## **Output**
<img width="1920" height="1020" alt="Screenshot 2026-04-02 075059" src="https://github.com/user-attachments/assets/fd4b6433-8dc5-4807-8e21-5d49cf0547aa" />


## **Future Improvements**
- Integrate deep learning models (e.g., YOLO) for better accuracy  
- Improve smoke detection capabilities  
- Send alerts via mobile app or email  
- Deploy system for real-world surveillance environments
  
## **Conclusion**
This project demonstrates how computer vision techniques can be used for early fire detection using surveillance cameras. It provides a cost-effective and real-time solution compared to traditional sensor-based systems.
