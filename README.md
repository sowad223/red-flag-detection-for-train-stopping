<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
</p>

**Railway systems play a pivotal role in global transportation
networks, facilitating the efficient movement of passengers
and goods across vast distances. However, alongside their
undeniable utility, railway systems also present inherent risks,
with accidents posing significant threats to human life, infrastructure integrity, and environmental sustainability. Among
the various factors contributing to railway accidents, delayed
train stoppage stands out as a critical concern, often leading
to catastrophic consequences.
In response to this pressing challenge, our team embarked
on a journey to develop an innovative solution aimed at
enhancing railway safety and mitigating the risk of accidents
caused by delayed train stoppage. The result of our endeavors
is a groundbreaking application of machine vision and deep
learning technologies in railway safety.
The rationale behind our project is rooted in the recognition of the fundamental importance of timely detection and
response to critical signals, such as red flags, along railway
tracks. Red flags serve as vital indicators for train stoppage,
signaling hazards, obstacles, or other emergency situations that
necessitate immediate action. However, the reliance on human
operators to detect and respond to red flags introduces inherent
limitations, including the potential for human error, fatigue,
and oversight.
To address these challenges, our project leverages advanced
machine vision techniques to automate the detection of red
flags along railway tracks. By integrating high-resolution cameras and state-of-the-art object detection algorithms, we aim to
empower railway systems with the capability to autonomously
identify and respond to red flags in real time, thereby enhancing safety and minimizing the risk of accidents.
The significance of our project extends beyond its immediate application in railway safety; it embodies the transformative potential of emerging technologies, such as machine vision
and deep learning, in addressing complex challenges and
advancing safety standards across diverse domains. Through
our project, we aim to demonstrate the feasibility and efficacy
of leveraging these technologies to enhance safety, efficiency,
and sustainability in transportation systems worldwide.
In this comprehensive report, we provide a detailed
overview of our project methodology, encompassing dataset
creation, model implementation using YOLOv8, and the thorough evaluation of results. Additionally, we delve into the
implications of our findings, offering insights into the future
directions and potential applications of our system in realworld railway operations.
In essence, our project represents a paradigm shift in railway
safety technology, ushering in a new era of automation and
reliability in train control systems.
II. METHODOLOGY
A. Dataset Creation
At the heart of our project lies the creation of a robust
and diverse dataset comprising images of red flags along
railway tracks. Recognizing the fundamental importance of
high-quality data in driving model performance, our team
embarked on the meticulous curation of a dataset comprising
approximately 5000 annotated images of red flags. Leveraging
the versatile annotation capabilities of the Roboflow platform,
we meticulously annotated each image, delineating the red flag
regions with precision using bounding boxes. This meticulously curated dataset served as the cornerstone for training
and evaluating our object detection model, ensuring its ability
to generalize effectively across diverse scenarios. Furthermore,
to facilitate comprehensive model evaluation and validation,
the dataset was partitioned into distinct training, validation,
and testing subsets, with careful attention given to maintaining
appropriate proportions.
Fig. 1. Processes of Our Dataset Creation
B. Model Implementation
The implementation of our project revolved around the
utilization of Python programming language and the YOLOv8
object detection model. Leveraging the computational resources offered by the Google Colab platform, our team
orchestrated the development process, encompassing data preprocessing, model training, and evaluation. The implementation commenced with the seamless mounting of Google
Drive and the installation of essential packages, including
ultralytics and Roboflow, to facilitate seamless integration with
the dataset. Subsequently, we interfaced with the Roboflow
API to access the annotated dataset and initiated the training
of the YOLOv8 model using the downloaded data. Carefully
chosen configuration parameters such as epochs, input image
size, and model path were optimized to maximize model
performance and ensure robustness. Extensive experimentation
and hyperparameter tuning were conducted to fine-tune the
model and optimize its efficacy in red flag detection across
varied environmental conditions and scenarios.**
