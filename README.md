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
## quantization 

| Publisher | Year | Name | Tags | Team | Read | Logic |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| <strong><code>ICLR</code></strong>  | 2023 | PowerQuant: Automorphism Search For Non-Uniform Quantization<br/> | <strong><code>non-uniform</code></strong>  |  | <strong><code>abs</code></strong>  | This paper hope to propose a non-uniform quantization in data-free way and it should be hardware-friendly without dedicated design, which is a simple change to activation in PowerQuant.   It proves that the power function makes sure the matrix multiplication in quantized space and does quantization in this way. But the de-quantization requires Newton's method to get the power a back. The optimal power exponent is searched by Nelder-Mead method.<br/>def compute_newton_sqrt(x: tf.Variable) -&gt; tf.Variable:<br/>  """<br/>  the algorithm assumes that x is positive non-zero.<br/>  """<br/>  max_iter = 5<br/>  x_0 = tf.math.pow(2.0, tf.math.round((tf.math.log(x) / tf.math.log(2.0)) / 2.0))<br/>  for cpt in range(max_iter):<br/>      x_next = tf.math.round((x_0 + tf.math.round(x / x_0)) / 2.0)<br/>  return x_next<br/> |
| <strong><code>Arxiv</code></strong>  | 2023 | ACQ: Improving Generative Data-free Quantization Via Attention Correction<br/> | <strong><code>ptq</code></strong> <strong><code>data-free</code></strong>  |  | <strong><code>rough</code></strong>  | For generated images in DFQ, they has higher BN gap in eval/train mode than normal images, which causes a gap for quantization. Also, generated images for the same class usually share too much info, so the quality of them could be improved. This paper provides a way to generate images with less train/eval gap and to improve uniqueness of generated images.<br/> |
| <strong><code>Arxiv</code></strong>  | 2023 | Efficient Adaptive Activation Rounding for Post-Training Quantization<br/> | <strong><code>ptq</code></strong>  |  | <strong><code>rough</code></strong>  | This paper hopes to optimize the default 0.5 boarder in AdaRound based method to obtain better performance, which also applies for the activation quantization. Learn the quantization boarder of activation in a element-wise quadratic manner. <br/> |
| <strong><code>Arxiv</code></strong>  | 2023 | Q-Diffusion: Quantizing Diffusion Models<br/> | <strong><code>ptq</code></strong>  |  | <strong><code>rough</code></strong>  | The diffusion models are iterative and computation-intensive. The first could result in accumulated quantization error, and the second could be alleviated by compression methods. It just does PTQ over data sampled from different time and adjusts the activation at the end rather that with PTQ.<br/> |
## metric 

| Publisher | Year | Name | Tags | Team | Read | Logic |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| <strong><code>ICLR</code></strong>  | 2023 | Data Valuation Without Training of a Model | <strong><code>data</code></strong>  |  | <strong><code>rough</code></strong>  | This paper proposes the complexity gap score of data, which could inflect the complexity of data, i.e., the difficulty to learn from it. The score is from Gram matrix, and is easy to compute. However, no WHY TO DO IT LIKE THAT is provided.<br/> |
## understand 

| Publisher | Year | Name | Tags | Team | Read | Logic |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| <strong><code>ICLR</code></strong>  | 2023 | Towards Understanding Ensemble, Knowledge Distillation and Self-Distillation in Deep Learning | <strong><code>ensemble</code></strong>  |  | <strong><code>rough</code></strong>  | 1. The learning of deep networks could be treated as learning a function with some random noise (related to the seed). Thus, after ensemble, the noise could be reduced. But this paper DOUBTS it! If the number of ensemble increase continuously, the performance would saturate. If the bias of the noise is non-zero, why would it works.  2. The paper proposes a theorem that networks learn some certain features, but they could be not complete. With those part-feature, the network could know that some cases could provide gradients as they do not have these features. In Ensemble, the models' outputs are averaged to use all features in the models.  In Distillation, the model are learning from each others with the left features. In Self-Distillation, the model learns features in different angle of seed, which could fix the previous caught features.<br/> |
## distributed system 

| Publisher | Year | Name | Tags | Team | Read | Logic |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| <strong><code>Communications ACM</code></strong>  | 1978 | Time, Clocks, and the Ordering of Events in a Distributed System | <strong><code>basic</code></strong>  |  | <strong><code>detailed</code></strong>  | This paper proposes an algorithm to synchronize the physical clocks and gives the bound of out-synchrony, which is the fundamental problem of the distributed system. <br/>The concept of time, like before and after, is normal in daily life but not in distributed systems. A distributed system is a system with a non-negligible transmission delay. In a distributed system, the order of events is hard to determine. This paper provides partial ordering and total ordering with an algorithm. To deal with anomalous behavior, real physical clocks could be leveraged.           <br/>We can define a partial order by whether one event could affect another, no matter whether they belong to the same process. Based on this, Logical Clocks are proposed, under which the events in the same and different processes are coupled with a process-wise clock. In one process, the events happen sequentially and get an increasing timestamp. In different processes, the receiver should update its timestamp to no less than the received one. With the manner of a process-wise clock, a total ordering method is proposed with an example of concurrent resource lock. The algorithm's rules could be too hard to obey in the real world, as the output of users and input of the algorithm are not at exactly  the same time. By defining the clock rate and time error between different processes, and constraining the system, the algorithm could handle timestamped input correctly under an error bound.<br/> |
| <strong><code>ACM Transactions on Computer Systems</code></strong>  | 1985 | Distributed snapshots: determining global states of distributed systems<br/> | <strong><code>basic</code></strong>  |  | <strong><code>detailed</code></strong>  | This paper proposed an algorithm for taking snapshots under distributed systems. Usually, we have to analyze a distributed system by checking its states. But states of the distributed system's nodes could be fetched simultaneously due to the inherent inconsistency of clocks. So this paper explains what is a meaningful state or snapshot of distributed systems and then how to get it. <br/>To illustrate the algorithm, a system model is first built. A system is abstracted to processes and channels, where (atomic) events occur in processes and messages transfer between channels. Atomic events could send/receive one message, and the state could change or keep it. Once a message is transferred, the related channel also changes its state. With the above assumptions, the next state of the system could be a function that takes the now state and the immediate event. <br/>To make a record meaningful, the states of a snapshot should be consistent, i.e., no wrong ordering of events happens. In order to make the state of the channel valid, some process should send a marker as some incident occurs, while the receivers should record its state on the first recipient of the marker, and record the state of the channel. <br/>Given such a system state, we should prove it is meaningful. Note that a state could have many concurrent parts, which means the snapshot could be different from the exact state at the time of the incident. But in fact, by exchanging the concurrent parts(preRec, postRec)' order, we could construct a computation state identical to the needed one. In conclusion, it is meaningful. If a snapshot happens to be stable, all its reachable states should be stable.<br/> |
| <strong><code>Journal of the ACM</code></strong>  | 1985 | Impossibility of distributed consensus with one faulty process<br/> | <strong><code>basic</code></strong>  |  |  | This paper shows that even one process fails in a system, there will be possibility of non-termination in the consensus problem of an asynchronous system. Concensusity is a important part of a distributed system, as the data in distributed nodes should be consistent, so any operation on the data should be applied to all nodes. And the FLP applies to even weak forms of consensus.     Some assumptions are made, such as the total asynchronous, message channel stability, in order to simplify the proof.     A consensus protocol is a multi-process asynchronous system. Each process gets a 1-bit input (0/1) and tri-level output (0/1/b), while the storage could be infinite. The 0/1 output states are called the decision of the process, while the b is undetermined. Once the decision is made, any transition from other processes could not change the output.    The transition in the system is abstracted to message (p, m), where p is the target process and m is a pre-defined value. Messages are sent via a global buffer, which could be read or written by processes. Note that, a reading could get null as the buffer could have a time delay.     The internal state of a process is called configuration. So configuration could be toggled by messages as described before.     The following lemmas and theorems are shown in the class. And at the end of the paper, it proposed the initially dead process, which means if more than half processes work fine, the system could get consensus from the alive processes at least. This is similar to the Paxos but without proof.<br/> |

