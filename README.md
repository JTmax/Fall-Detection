# Fall-Detection

This is code developed while working at IATSL. This code can be used to detect falls in video, an example is given in the following GIF

<a href="https://imgflip.com/gif/29382v"><img src="https://i.imgflip.com/29382v.gif" title="made at imgflip.com"/></a>

Falls are detected by first training an autoencoder to minimize recontruction error of ADL (activities of dailty living) video frames. The reconstruction error for falls should thus be higher, as is shown in the above GIF.


Code Usage:

Training:

To use this code, first run one of the training modules. A model is then saved to Models/Dataset/....
For example, we can train a deep fully conntected autoendoer (dae) on Thermal data as follows. First, run dae_main_train.py with a choice of dataset. For instance to train on Thermal data, set dset = 'Thermal' in dae_main_train.py.

Testing:

to evaluate the model, run the correpsonding test module. The results of testing will be saved to AEComparisons. Once training has completed, find the saved model under Models/Thermal/{model_name}. To evaluate the model, set the variable pre_load in dae_main_test.py to the path to this model. Run dae_main_test.py and find the results in AEComparisons/AUC/Thermal/{model_name}.

Generating Animation:

To generate an animation, such as shown in the above GIF, run dae_main_test.py, with animate option set to True. An animation (mp4 file) for each testing video will be saved to 


dae: deep autoencoder
cae: convolutional autoencoder

{model}_main_{train}
{model}_main_{test}
