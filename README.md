# FaceFeatures

## Datasets

### FDDB: Face Detection Data Set and Benchmark 

Research Paper: [FDDB: A Benchmark for Face Detection in Unconstrained Settings](http://vis-www.cs.umass.edu/fddb/fddb.pdf) V.Jain, E. Learned-Miller. University of Massachusetts Amherst. 

[FDDB](http://vis-www.cs.umass.edu/fddb/)

**Reasons for choosing this dataset**

- Ground Truth for the bounding box and the ellipses of the faces are available
- Includes images with occlusions

### Other Datasets Considered



## Related Research and Algorithms

### Mask RCNN

Research Paper: [Mask RCNN](https://arxiv.org/pdf/1703.06870.pdf) K.He, G.Gkioxari, P.Dollar, R.Girshick. Facebook AI Research. 

[Code](https://github.com/matterport/Mask_RCNN)

**Utilization of Mask RCNN**

- Placing "person mask" to a white background

![Image of Removed Background](/RemoveBackground/works1.jpg)

- Train with FDDB 

### Ellipse RCNN

Research Paper: [Ellipse R-CNN](https://arxiv.org/pdf/2001.11584.pdf) W.Dong, P.Roy, C.Peng, V.Isler. IEEE.

Code not made public




