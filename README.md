# Awesome-Self-Read-Papers


Pannenets' Read Papers and Note.


## lane-detection 

| Publisher | Year | Name | Tags | Team | Read | Logic |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| <strong><code>Pattern Recognition</code></strong>  | 2021 | A Review of Lane Detection Methods based on Deep Learning | <strong><code>review</code></strong>  |  | <strong><code>rough</code></strong>  | How to extract features: 1) CNN; 2) RNN to merge temporal info (STLNet). 3) Kalman filter for lane tracking prediction. 4) Dilated convolution to prevent loss in downsampling, and could be used many times to gather more. 5) Non-local operations to focus on certain region. 6)<br/>How to cluster: RANSAC. <br/>What to predict: 1) start/end points of lane and their depth. 2) vanishing point (VP) to give geometry info of the scene. 3) a 3-point quadratic curve of lane. <br/>What to post-process: 1) each lane is a class. 2) each lane is a instance. <br/>How to design loss: 1) the imbalance of background and lane. 2) large-margin softmax.<br/>How to pre-process: 1) ROI. 2) inverse perspective transformation.<br/>How to post-process: 1) Density-Based Spatial Clustering of Applications with Noise. 2) <br/>Need to Read: 1) LaneNet, what is parameters regression? 2)<br/> |
| <strong><code>CVPR</code></strong>  | 2022 | Rethinking Efficient Lane Detection via Curve Modeling | <strong><code>curve</code></strong>  |  | <strong><code>detailed</code></strong>  | Curves are more naturally representation of lanes. This paper models lanes as cubic Bezier curves, as they have intrinsic geometry on image. Also, cars usually stay in the middle of two lanes, thus they are symmetric. This paper proposes a module to merge info from flipped features named Feature Flip Fusion. The loss contains curve regression loss, lane existence loss and segmentation loss to provide a more spatial feature map.<br/> |

