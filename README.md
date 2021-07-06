# FaceFeatures

## Datasets

### FDDB: Face Detection Data Set and Benchmark 

Research Paper: [FDDB: A Benchmark for Face Detection in Unconstrained Settings](http://vis-www.cs.umass.edu/fddb/fddb.pdf) V.Jain, E. Learned-Miller. University of Massachusetts Amherst. 

[FDDB](http://vis-www.cs.umass.edu/fddb/)

**Reasons for choosing this dataset**

- Ground Truth for the bounding box and the ellipses of the faces are available
- Includes images with occlusions

### Other Datasets Considered

**Public-IvS database**

[Database](http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/LBL/main.htm)

Advantages
- Mostly Asian faces
- Has images with occlusions

Disadvantages
- Not annotated
- Dataset not created with similar goals as our project 

**Caltech Occluded Faces in the Wild**

[Database](http://www.vision.caltech.edu/xpburgos/ICCV13/)

Advantage
- Dataset was created to test the method Robust Cascaded Pose Regression (RCPR)

Disadvantages
- Not annotated
- Virtually no Asian faces 


## Related Research and Algorithms

### Mask RCNN

Research Paper: [Mask RCNN](https://arxiv.org/pdf/1703.06870.pdf) K.He, G.Gkioxari, P.Dollar, R.Girshick. Facebook AI Research. 

[Code](https://github.com/matterport/Mask_RCNN)

**Utilization of Mask RCNN**

- Placing "person mask" to a white background

This is done to reduce the noise produced from diverse backgrounds as use-case is likely to have a clean white background.

![Image of Removed Background](/RemoveBackground/works1.jpg)

- Train with FDDB 

This would allow us to predict the parameters of facial ellipses. This is important as most biometric photos require the head (bottom of the jaw to top of the head) to cover a certain range of the photo - ensuring that the face is not too far or too close to the camera 

**In progress**

### Ellipse RCNN

Research Paper: [Ellipse R-CNN](https://arxiv.org/pdf/2001.11584.pdf) W.Dong, P.Roy, C.Peng, V.Isler. IEEE.

Code not made public


**Utilization of Ellipse RCNN**

- Develope algorithm with the ideas presented in the paper 

This paper suggests a better way of predicting Ellipses and is built on Mask RCNN. 

**In progress**


### Robust Face Landmark Estimation Under Occlusion

Research Paper: [Robust Face Landmark Estimation Under Occlusion](http://www.vision.caltech.edu/xpburgos/papers/ICCV13%20Burgos-Artizzu.pdf) X.P. Burgos-Artizzu, P.Perona, P.Dollar. California Institute of Technology. Microsoft Research. 

[Code](http://www.vision.caltech.edu/xpburgos/ICCV13/#code)

The original code is in MATLAB.

The code relies on [Piotr's Computer Vision Matlab Toolbox](http://pdollar.github.io/toolbox/)

**Utilization of RCPR**

A requirement for a photo to pass is that features such as the eyes and eyebrows cannot be occluded. This paper proposes a way to not only return the facial landmarks but also their occlusion state. 

**In progress**
