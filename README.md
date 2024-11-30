# Mask_Ai_Project
This is about Mask Recognition AI. You can see how AI recognize whether people ware a mask or not.

**[If you want to know about Me]**
All you have to do is looking ./original_app/**a_Module.py** and **D_mask_Tracking.py** Thank you.






**[If you want to use, you have to modify somepart]**
1) root where traing and validation dataset is

TRAINING_DIR = "C:/Users/I310/PycharmProjects/pythonProject/mask_dataset/train-set"
VALIDATION_DIR = "C:/Users/I310/PycharmProjects/pythonProject/mask_dataset/test-set"

should change Path "C:/Users/I310/PycharmProjects/pythonProject/mask_dataset/test-set" -> "your own"


*ther are no dataset file in this github because of the capacity of the picture they're over 1GB."
SO you have to do crolling some 'human Face image' from web and put them into folder which is called "train-set" and "test-set"
while keep in mind that "train-set" has more picture then 'test-set'
(I did this for train-set/on-mask 18 photos and for train-set/off-mask 19 photos. 
I did this for test-set/on-mask 9 photos and for test-set/off-mask 9 photos.)
