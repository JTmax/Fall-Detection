# DeepFall: 3D Spatio-Temporal Autoencoders for Fall-Detection from Privacy Protecting Cameras

This code is developed by Jacob Nogas while working at IATSL (http://iatsl.org/) as a UofT PEY intern under the supervision of Dr. Shehroz Khan, Scientist, KITE-Toronto Rehab, University Health Network, Canada. 

Under the supervision of Dr. Jaime Valls Miro, the code is modified and tested for validation by Taryar Myint Mo, University of Technology, Sydney, as final year capstone project.

Please refer to the original code from the repository: https://github.com/JJN123/Fall-Detection for more details.

## Code Usage & Modifications

The original code is structured in such a way that different neural networks and different datasets can be tested rapidly. The two major datasets of interest are UR_Kinect dataset and SDU dataset.

UR_Kinect dataset that is used in the orignal research, as well as custom dataset made for validation is available in the following link. UTS account is needed to get access to the link.

onedrive link: https://studentutsedu-my.sharepoint.com/:f:/g/personal/12675005_student_uts_edu_au/EqVNte_6AYtAnc9H-mZZXqkBJ7Wk6P_EC8PtYh2wkyaxug?e=7fHK4Z

The files of interest in my research are as follows.

1. dstcae_c3d_main_test.py
2. dstcae_c3d_main_train.py
3. seq_exp.py
4. util.py
5. h5py_init.py
6. opencvinpaint.py
7. camera.py

**1. ---**
dstcae_c3d_main_test.py file is the main script that runs the test, and output animation videos. The model to use, dataset to use as well as input shapes of the tensors can be modified in this script.

**2. ---**
dstcae_c3d_main_train.py file requires a dataset, trains and outputs a model.

**3. ---**
seq_exp.py consists of train and test functions that are called in the above two scripts. "test" function is the main function of interset and it includes code for animation and manipulation of results.

**4. ---**
util.py includes functions on how the results are manipulated for calculation of ROC scores. It also includes code that limits the number of videos that will be tested at one time. At line 162, custom folder is added to the code. Video numbers has to be edited to match the number of videos that are required to be tested.

**5. ---**
h5py_init.py includes preprocessing code for the images (videos). Custom folder is added to the list of datasets. New videos taken manually can be placed in the custom dataset or new dataset name can be added to the list.

**6. ---**
opencvinpaint.py is the script used to modify depth images that has black spots (holes) and fill them for better consistency.

**7. ---**
camera.py is the script used to take depth images using the depth camera Intel Realsense D435.
