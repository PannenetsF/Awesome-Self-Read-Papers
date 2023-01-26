# Awesome-Self-Read-Papers


Pannenets' Read Papers and Note.


## lane-detection 

| Publisher | Year | Name | Tags | Team | Read | Logic |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| <strong><code>Pattern Recognition</code></strong>  | 2021 | A Review of Lane Detection Methods based on Deep Learning | <strong><code>review</code></strong>  |  | <strong><code>rough</code></strong>  | How to extract features: 1) CNN; 2) RNN to merge temporal info (STLNet). 3) Kalman filter for lane tracking prediction. 4) Dilated convolution to prevent loss in downsampling, and could be used many times to gather more. 5) Non-local operations to focus on certain region. 6)<br/>How to cluster: RANSAC. <br/>What to predict: 1) start/end points of lane and their depth. 2) vanishing point (VP) to give geometry info of the scene. 3) a 3-point quadratic curve of lane. <br/>What to post-process: 1) each lane is a class. 2) each lane is a instance. <br/>How to design loss: 1) the imbalance of background and lane. 2) large-margin softmax.<br/>How to pre-process: 1) ROI. 2) inverse perspective transformation.<br/>How to post-process: 1) Density-Based Spatial Clustering of Applications with Noise. 2) <br/>Need to Read: 1) LaneNet, what is parameters regression? 2)<br/> |
| <strong><code>CVPR</code></strong>  | 2022 | Rethinking Efficient Lane Detection via Curve Modeling | <strong><code>curve</code></strong>  |  | <strong><code>detailed</code></strong>  | Curves are more naturally representation of lanes. This paper models lanes as cubic Bezier curves, as they have intrinsic geometry on image. Also, cars usually stay in the middle of two lanes, thus they are symmetric. This paper proposes a module to merge info from flipped features named Feature Flip Fusion. The loss contains curve regression loss, lane existence loss and segmentation loss to provide a more spatial feature map.<br/> |
| <strong><code>CVPR</code></strong>  | 2022 | A Keypoint-Based Global Association Network for Lane Detection | <strong><code>keypoints</code></strong>  |  | <strong><code>detailed</code></strong>  | This paper directly regress keypoints to start point directly, where offsets are predicted.<br/> |
| <strong><code>CVPR</code></strong>  | 2022 | Eigenlanes: Data-Driven Lane Descriptors for Structurally Diverse Lanes<br/> | <strong><code>curve</code></strong> <strong><code>new dataset</code></strong>  |  | <strong><code>detailed</code></strong>  | It is a paper mainly about how to model a curved/straight lane.  This paper contains (1) lane candidates generation: take lanes from training set, and find their SVD. (2) a network, predicting probability of lane cad, scores of lanes combination, and regressing the offset of combination. NMS and MWCS are used in post processing. The work performs well on curved lanes than others. <br/> |
| <strong><code>CVPR</code></strong>  | 2022 | Towards Driving-Oriented Metric for Lane Detection Models | <strong><code>metric</code></strong> <strong><code>new dataset</code></strong>  |  | <strong><code>rough</code></strong>  | This paper proposed two autonomous driving oriented metrics: 1) end to end lateral deviation metrics, 2) per-frame simulated lateral deviation metric. Traditional metric could have strongly negative correlations with them, thus some methods could have been overfitting to the dataset. The two metrics are mainly about the deviation between lane center.<br/> |
| <strong><code>CVPR</code></strong>  | 2022 | CLRNet: Cross Layer Refinement Network for Lane Detection<br/> | <strong><code>keypoints</code></strong>  |  | <strong><code>rough</code></strong>  | Note that, the points it used should be treated as a set. The cross layer refinement is to take use of each level of features to get a better lane points (prior). The ROI gather gets info from ROI to lane and adds output to lane prior. The line IOU loss treats line as one part, hoping the lane and gt could be the same in length, angle, start point. In the ablation, we could see the most valuable part is the CLR part, and then the loss. <br/> |
| <strong><code>Intelligent Vehicles Symposium (IV)</code></strong>  | 2018 | Towards End-to-End Lane Detection: an Instance Segmentation Approach<br/> | <strong><code>segment</code></strong>  |  | <strong><code>rough</code></strong>  | LaneNet uses two segment branches for detection, one for the binary lane mask, one for the distance embedding which targets at minimizing the distance between points in one lane. Note that, the curve is fitted in H-Net space and then turns back to image.<br/> |
| <strong><code>AAAI</code></strong>  | 2018 | Spatial As Deep: Spatial CNN for Traffic Scene Understanding<br/> | <strong><code>segment</code></strong>  |  | <strong><code>detailed</code></strong>  | Lanes on roads could be invisible while an AD system should estimate it as well as human. In the process, spatial information should be leveraged while keep it easy to be trained. The spatial CNN send its previous output to next slice just like RNN while keeps higher efficiency.  In the ablation, we can see the effectiveness of multi-direction SCNN, window width of message passing, the better position to place the module, the way to add it as residual rather than get a weighted sum. <br/> |
| <strong><code>CVPR</code></strong>  | 2021 | Keep your Eyes on the Lane: Real-time Attention-guided Lane Detection<br/> | <strong><code>detection</code></strong>  |  | <strong><code>detailed</code></strong>  | This paper proposed Lane-ATT with anchor based proposal pooling and attention mechanism. The anchor is defined with a start point and a angle. The attention is to aggregate the global info the tensors. Note that, the proposal is the most important part, which provides a structure prior. Also, it leverages parallelism and equidistance of lanes to predict the boundaries. <br/> |
| <strong><code>CVPR</code></strong>  | 2019 | FastDraw: Addressing the Long Tail of Lane Detection by Adapting a Sequential Prediction Network<br/> |  |  |  | This paper predicts the distribution of a point and a possible lane, then finds the lane with greedy algorithms.<br/> |
| <strong><code>WACV</code></strong>  | 2020 | Lane detection using lane boundary marker network with road geometry constraints<br/> | <strong><code>keypoints</code></strong>  |  |  | This paper applied inverse perspective mapping to turn the input image of car's camera into a bird-view one. On the view, it predicts key-points by lane boundaries and the weighted average them into a lane. The lane boundaries are left, right, center, which could be used together with the lane self. If the lane is without lane marker, the methods could find the evidence from the surroundings.<br/> |

