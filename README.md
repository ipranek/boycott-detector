# Overview (Project in Process):

This project is an end-to-end computer vision system prototype that detects brand logos through the embedded camera on the server-side website, and retrieves the boycott status and insights for each detected brand. This system combines YOLO11s for object detection from a custom dataset with a Flask + SQL backend. Currently limited to 5 brands due to the absence of GPU and other computer-related issues.

# Motivation:

This project was undertaken after 19 March 2025, an important turning point in Turkish politics, where the main opposition's presidential candidate was imprisoned. A nationwide boycott began, and it was difficult to keep track of which brands were boycotted. Therefore, this project helps automatically identify brands in visual content and provides reasons for the boycott status with external metadata. 

# Tech Stack:
**Computer Vision**: YOLO11s, OpenCV <br/>
**Backend**: Python Flask <br/>
**Database**: SQL <br/>
**Data Annotation**: Label Studio <br/>
**Deployment**: Flask-based server-side API <br/>
**Model Training**: Custom dataset, data augmentation <br/>

# System Architecture:
1) User consents and shows a brand to the embedded camera on the webpage. <br/>
2) YOLO11s model performs real-time logo detection. <br/>
3) Detected brand names are matched against SQL records. <br/>
4) API returns: boycott status and brand insights. <br/>

# Dataset and Training:

Built a custom logo dataset with approximately 200 images using Label Studio. Applied data augmentation and preprocessing for YOLO11s. Trained with YOLO11s to have good accuracy and not give up on FPS (compared to YOLO11n). Validated on a brand-specific dataset 

# Validation Performance:
**mAP@0.5**: 0.978 <br/>
**Precision**: 0.95 <br/>
**Recall**: 0.95 <br/>

# Project Status
Expanding brand coverage. Currently only has 5 brands: D&R, Mavi, Espressolab, Watsons, and Kırmızı Kedi. Also, improving false positive rate by introducing "background" images. 

# How to Run Locally?
pip install -r requirements.txt <br/>
python app.py


