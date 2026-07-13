# Yang A Human-Factor-Driven Evaluation of Multi-Modal Feedback for Enhancing Teleoperated Microrobotic Swarm Control

*Source file: Yang_A_Human-Factor-Driven_Evaluation_of_Multi-Modal_Feedback_for_Enhancing_Teleoperated_Microrobotic_Swarm_Control.pdf — 5 pages*


---
**[Page 1]**

 
A Human-Factor-Driven Evaluation of Multi-Modal 
Feedback for Enhancing Teleoperated Microrobotic 
Swarm Control 
 
Qijun Yang  
Department of Robotics of 
Southeast University 
Nanjing, China 
220234915@seu.edu.cn 
 
 
 
 
 
 
 Shengming Luo 
Department of Geotechnical of 
Southeast University 
Nanjing, China 
220235053@seu.edu.cn 
 
 
 
 
 
 
Zhiqiang Tang 
Jiangsu Key Laboratory for 
Design and Manufacturing of 
Precision Medicine Equipment, 
School of Mechanical Engineerin 
Department of Robotics, School 
of Mechanica Engineering, 
Southeast University 
Nanjing, China  
zhiqiang.tang@seu.edu.cn 
 
Qianqian Wang* 
Jiangsu Key Laboratory for 
Design and Manufacturing of 
Precision Medicine Equipment, 
School of Mechanical Engineerin 
Department of Robotics, School 
of Mechanica Engineering, 
Southeast University 
Nanjing, China 
qqwang@seu.edu.cn  
Corresponding author*
 
Abstract—Magnetic microrobotic swarms hold immense 
promise for biomedical applications, yet their precise and stable 
manipulation in complex environments remains a significant 
challenge. Teleoperation systems that incorporate human 
operators can enhance adaptability, but often neglect the 
operator's cognitive workload. This paper introduces a 
teleoperated microrobotic swarm control system that integrates 
multi-modal feedback (MMF) designed around human-centric 
principles. We conducted a user study (N=20) to evaluate system 
performance and operator workload across three feedback 
conditions: haptic-only (HF), haptic-visual (HVF), and multi-
modal (haptic, visual, and auditory) feedback. Our results 
demonstrate that MMF significantly improves manipulation 
performance, with the swarm remaining in a stable state for 89% 
of the task duration, compared to 78% for HVF and 44% for HF. 
Furthermore, analysis of eye-tracking data revealed a significant 
reduction in participants' average pupil diameter under the MMF 
condition, indicating lower cognitive load. Subjective assessments 
using the NASA-Task Load Index (NASA-TLX) and Likert scales 
corroborate these findings, showing that MMF is associated with 
the lowest perceived workload and the highest system usability. 
This study validates that an integrated, multi-modal feedback 
approach not only enhances task execution but also optimizes the 
human-robot interaction experience.   
Keywords—Microrobotics, Microrobotic Swarm, Teleoperation, 
Multi-Modal Feedback, Haptics  
I. INTRODUCTION  
Magnetic microrobotic swarms are emerging as a powerful 
tool in modern medicine, offering unprecedented capabilities for 
targeted drug delivery, minimally invasive surgery, and medical 
imaging [1]-[6]. Their ability to navigate non-invasively within 
confined biological spaces makes them ideal candidates for 
complex in-vivo tasks. However, realizing their full potential is 
contingent upon the development of robust and intuitive control 
systems capable of maintaining swarm integrity and precision 
during delivery.  
Initial control strategies evolved from manual adjustments to 
automated algorithms designed to manage swarm formations 
and transitions [7-9]. While automation enhances consistency, it 
often lacks the adaptability and real-time decision-making 
prowess of a human operator, particularly when faced with 
unforeseen environmental changes. Teleoperation systems 
bridge this gap by placing a human in the loop allowing 
operators to leverage their cognitive abilities to guide the robotic 
system [10]. These systems typically rely on feedback 
mechanisms, such as haptic devices or virtual reality interfaces, 
to convey information about the remote environment [11-15]. 
Despite technical advancements in teleoperation focusing on 
system stability, communication latency, and tracking accuracy, 
a critical dimension has been largely overlooked: the human 
factor [16]. The physiological and cognitive load imposed on the 
operator directly impacts performance, efficiency, and safety. 
An overly demanding system can lead to operator fatigue, errors, 
and a negative user experience. Therefore, it is imperative to 
design teleoperation interfaces that are not only powerful but 
also ergonomic and user-friendly.  
In this work, we address this gap by proposing and 
evaluating a teleoperation system for microrobotic swarm 
delivery built upon a human-factor-centric framework(Fig. 1). 
Our primary contribution is the integration and assessment of a 
multi-modal feedback strategy, combining haptic, visual, and 
auditory cues. We hypothesize that this synergistic approach 
will enhance swarm control performance while simultaneously 
reducing the operator's cognitive workload. To validate this, we 
conducted a comprehensive user study and evaluated the system 
through a combination of objective performance metrics, 
physiological data, and subjective user ratings. Our findings 
The work is supported by the National Natural Science Foundation under 
project no. 52575652 and no. 52205590, the Natural Science Foundation of 
Jiangsu Province under project no. BK20220834, the Taihu Lake Innovation 
Fund for the School of Future Technology of Southeast University.  
67
2025 the 9th International Conference on Automation, Control and Robotics
979-8-3315-6286-1/25/$31.00 ©2025 IEEE
2025 9th International Conference on Automation, Control and Robots (ICACR) | 979-8-3315-6286-1/25/$31.00 ©2025 IEEE | DOI: 10.1109/ICACR68388.2025.11360016
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:24:24 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 2]**
*(This page contains a figure/chart/image not captured in text)*

confirm that MMF provides a superior control experience, 
paving the way for more effective and less demanding human-
robot collaboration in medical microrobotics. 
II. SYSTEAM DESIGN AND METHODOLOGY 
A. System Architecture 
Our magnetically assisted delivery system is composed of 
three primary subsystems: a magnetic actuation unit, a multi-
modal feedback interface, and a vision processing module as 
illustrated in Fig. 2. 
The magnetic actuation unit consists of a permanent 
spherical magnet mounted on the end-effector of a 6-DOF 
robotic arm. This configuration allows for precise and flexible 
positioning of the magnetic field source in 3D space, which in 
turn controls the aggregation and movement of the microrobotic 
swarm. The magnetic dipole model is used to represent the 
magnetic fields generated by permanent magnets. This model 
offers an analytical expression that is convenient for both 
theoretical analysis and practical calculations. Specifically, the 
magnetic flux density B
 
produced by the magnetic actuation unit 
at a position in space can be described as follows
 
[17].
 
𝑩𝑩(𝒓𝒓, 𝒎𝒎𝑠𝑠) =
𝜇𝜇0
4𝜋𝜋‖𝒓𝒓‖3 ቆ3𝒓𝒓𝒓𝒓T
‖𝒓𝒓‖2 −𝑰𝑰3ቇ𝒎𝒎𝑠𝑠      (1)
 
where 𝜇𝜇0
 
denotes the permeability of free space, r
 
is the 
vector from the center of the magnet to the point of interest in 
the workspace. I3
 
is the 3 ×
 
3 identity matrix, and 𝒎𝒎𝑠𝑠
 
is the 
magnetic moment of the dipole source.
 
The multi-modal feedback interface provides the operator 
with rich, real-time information. A haptic device (3D Touch) 
serves as the primary master controller, enabling the operator to 
intuitively manipulate the robotic arm's position. The same 
device delivers force feedback to the operator's hand. Visual 
feedback is presented on a monitor, displaying a live video feed 
of the swarm and graphical overlays indicating its current state 
(e.g., stable, spreading). Auditory feedback is delivered via a 
buzzer, which emits a warning signal when the swarm's stability 
degrades beyond a predefined threshold.
 
The vision processing module utilizes a camera mounted 
above the experimental phantom. A fine-tuned YOLO-V5 
model processes the video feed in real-time to detect the swarm's 
bounding box, track its position, and classify its formation state 
based on its area and aspect ratio. An eye-tracking device is 
integrated with the monitor to capture the operator's 
physiological data during the task.
 
B.
 
Control and Feedback Mechanism
 
The system operates within a closed-loop human-robot 
collaboration framework. The operator's hand movements with 
the haptic device are mapped to the target position of the robotic 
arm's end-effector through a coordinate transformation and 
scaling matrix. A
 
discrete PID controller then calculates the 
Fig. 1. The MMF-assisted magnetic microrobotic swarm delivery system
includes a 6-DOF robotic arm, a magnetic actuation unit for precise magnetic
field control, and a force feedback system. The physiological data collection
uses an eye-tracking device. Targeted delivery of the microrobots is controlled 
by the magnetic actuation unit. 
Fig.  2. A schematic of the MMF-based delivery system. Its components include
a haptic device for controlling the robotic arm's movement, an eye tracker for
capturing the participant's physiological data, and a vision feedback module for
real-time recording of the microrobotic swarm's state. 
Fig.  3. The master side consists of the operator, multimode controller, and eye
tracker, with data flow including F : force feedback, A : acceleration, and V :
velocity and feedback loops. The system integrates a 3D Touch interface to 
control the slave side, which includes a robotic arm, magnetic actuation unit, 
and microswarm. Sensory feedback is provided via haptic devices, buzzers, and
cameras to assist the operator in real time. 
68
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:24:24 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 3]**
*(This page contains a figure/chart/image not captured in text)*

necessary joint commands to ensure smooth and accurate 
motion of the robotic arm.
 
The haptic feedback force is a critical component, designed 
to reflect the swarm's state and the error from the target path. It 
is composed of a position feedback force, proportional to the 
deviation from the optimal trajectory, and a velocity feedback 
force, providing damping against overly aggressive movements. 
Crucially, when the vision module detects swarm instability, the 
gain coefficients for both feedback components are amplified. 
This intensified force provides a clear, physical cue to the 
operator that corrective action is needed. The auditory alert 
serves as a complementary, non-visual cue for the same event, 
ensuring the operator is notified even if their visual attention is 
focused elsewhere.  
C.
 
User Study Protocol 
To evaluate the efficacy of our system, we designed a user 
study with 20 participants (10 male, 10 female; mean age 24.2 ± 
1.9 years), all of whom provided informed consent. Each 
participant was tasked with teleoperating the microrobotic 
swarm through a narrow, simulated 3D vascular phantom, which 
included a challenging 90-degree turn. The primary objectives 
were to navigate from a start to a target point while maintaining 
the swarm in a stable, aggregated pattern.
 
Each 
participant 
performed 
the 
task 
under 
three 
counterbalanced experimental conditions:
 
•
 
Haptic Feedback: Operators received only force 
feedback from the haptic device.
 
•
 
Haptic-Visual Feedback: Operators received \item 
haptic feedback plus real-time visual overlays 
indicating the swarm's state.  
•
 
Multi-Modal Feedback: Operators received haptic, 
visual, and auditory feedback.
 
Each condition consisted of three trials, and participants 
were given breaks between sets to complete subjective 
questionnaires.
 
D.
 
Data Collection and Analysis
 
We collected a comprehensive set of metrics to evaluate both 
system performance and the user experience:
 
•
 
Performance Metrics: Task completion time, trajectory 
error, and swarm state.
 
•
 
Physiological Metrics: Eye-tracking data, including 
pupil diameter, fixation duration and count, and 
saccadic velocity, were recorded as objective 
indicators of cognitive load.
 
Fig.  4. Three different modes of feedback for the microrobotic swarm state. (a) The change of shape ratio and area of the microrobotic swarm. (b) Eye
movement metrics with three different feedback modes: Average duration of whole fixation, Average whole fixation pupil diameter, and Average amplitude
of saccades. I: HF, II: HVF, III: MMF. *** p<0.001, **p<0.01, *p<0.05.ww 
69
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:24:24 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

 
• 
Subjective Metrics: After each condition, participants 
completed the NASA-TLX [18] to rate their perceived 
workload and a Likert scale to assess system usability 
and satisfaction. 
The collected data were analyzed using a Repeated-
Measures Analysis of Variance (RM-ANOVA). Post-hoc 
pairwise comparisons were conducted using t-tests or 
Wilcoxon signed-rank tests, with a Bonferroni correction 
applied to control for family-wise error rates as shown in 
algorithm 1. A significance level of 𝛼𝛼 = 0.05 was used for 
all statistical tests. 
III. RESULTS 
A. Swarm Control Performance and Stability 
The integration of multi-modal feedback had a profound 
impact on the operators' ability to maintain swarm integrity. As 
shown in fig4(a), in the MMF condition, the microrobotic swarm 
remained in a stable state for an average of 89% of the task 
duration. This was a significant improvement over the HVF 
condition (78% stable time) and dramatically better than the HF 
condition, where the swarm was stable only 44% of the time. 
Operators in the MMF condition were more adept at navigating 
challenging sections of the phantom, such as the 90-degree turn, 
with minimal swarm dispersion. Trajectory error was also 
lowest in the MMF condition, indicating that operators could 
follow the desired path with higher precision. 
B. Operator Cognitive Load 
As shown in fig4(b), the eye-tracking data provided 
objective evidence that MMF reduces the cognitive burden on 
the operator. The average pupil diameter during fixation, a well-
established correlate of cognitive load, was significantly smaller 
for participants in the MMF condition compared to the HF (p < 
0.01) and HVF conditions. Furthermore, participants under 
MMF exhibited longer average fixation durations (p < 0.01 vs. 
HF) and reduced saccadic velocities (p < 0.01 vs. HF). This 
suggests a more efficient and less strenuous visual search 
strategy, as the auditory and enhanced haptic cues likely 
offloaded some of the cognitive processing required to monitor 
the swarm's state visually. 
TABLE I.  
SUBJECTIVE USER RATINGS FOR THE THREE FEEDBACK CONDITIONS (MEAN ± SD) 
Measure 
 
HF 
HVF 
MMF 
Overall p 
Post-hoc 
Likert usability 
 
18.45±4.98 
22.80±3.47 
26.65±3.1 
< 0.001‡ 
HF<HVF<MMF*** 
NASA-TLX 
Mental demand 
68.55±19.47 
62.75±19.43 
52.25±28.31 
0.0014† 
HF＞MMF***, HVF＞MMF* 
Physical demand 
63.95±23.01 
63.95±21.41 
62.15±26.12 
0.54† 
n.s. 
Temporal demand 
57.30±23.43 
56.00±24.74 
50.00±25.60 
0.10† 
n.s. 
Performance 
40.40±25.14 
29.00±10.21 
21.95±10.67 
0.0068† 
HF＞MMF**, HVF＞MMF* 
Effort 
72.00±18.95 
71.25±17.61 
57.50±24.68 
0.0022† 
HF＞MMF**, HVF＞MMF** 
Frustration 
57.25±27.36 
52.00±21.42 
41.25±25.80 
0.0288† 
HF＞MMF* 
n.s., not significant. SD, standard deviation. †Friedman test p-value. ‡One-way ANOVA p-value. Post-hoc significance after Bonferroni correction (p<0.0167): 
*p<0.0167$, **p<0.01$, ***p<0.001. 
70
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:24:24 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 5]**

C. Subjective User Experience 
Subjective 
ratings 
from 
the 
participants 
strongly 
corroborated the objective findings as shown in Table I. On the 
Likert scale for system usability, MMF received the highest 
scores, with a statistically significant difference compared to 
both HVF and HF (p < 0.001). The NASA-TLX results mirrored 
this trend, with the MMF condition yielding the lowest workload 
scores across all six subscales: mental demand, physical demand, 
temporal demand, performance, effort, and frustration. In 
contrast, the HF condition was consistently rated as the most 
demanding and frustrating, highlighting the difficulty of 
performing the delicate manipulation task without adequate 
sensory information. Task completion times did not differ 
significantly across the three modes, suggesting that the benefits 
of MMF relate to quality and efficiency of control, not speed. 
IV. CONCLUSION 
This study demonstrates that a teleoperation system 
designed with human factors at its core can significantly 
improve the efficacy of microrobotic swarm manipulation. Our 
results consistently show that the multi-modal feedback 
approach is superior to single- or dual-modality feedback, not 
only in terms of objective task performance but also in reducing 
operator cognitive load and enhancing user satisfaction. 
REFERENCES 
[1] B. Wang, J. Du, H. Zhang, Y. Cao, C. Wen, V. Iacovacci, Z. Lyu, T. Li, 
and Q. Wang, ''External-Field-Assisted Additive Manufacturing for 
Micro/Nano Device Fabrication,'' International Journal of Extreme 
Manufacturing, 
2025. 
[Online]. 
Available: 
http://iopscience.iop.org/article/10.1088/2631-7990/ae098e 
[2] X. An, Z. Xu, K. Fang, and Q. Wang, ''Model-Free Control of Magnetic 
Microrobotic Swarm for On-Demand Pattern Spreading,'' IEEE Robotics 
and Automation Letters, vol. 9, no. 4, pp. 3187--3194, 2024. 
[3] Z. Zheng, H. Wang, S. O. Demir, Q. Huang, T. Fukuda, and M. Sitti, '' 
Programmable aniso-electrodeposited modular hydrogel microrobots,'' 
Science Advances, vol. 8, no. 50, pp. eade6135, 2022. 
[4] Y. Ma, X. An, Q. Yang, M. Cai, Z. Tang, J. Chang, V. Iacovacci, T. Xu, 
L. Zhang, and Q. Wang, ''Magnetic Continuum Robot for Intelligent 
Manipulation in Medical Applications,'' SmartBot, vol. 1, no. 2, pp. 
e12011, 2025. 
[5] Q. Wang, Q. Wang, Z. Ning, K. F. Chan, J. Jiang, Y. Wang, L. Su, S. 
Jiang, B. Wang, B. Y. M. Ip, H. Ko, T. W. H. Leung, P. W. Y. Chiu, S. C. 
H. Yu, and L. Zhang, ''Tracking and navigation of a microswarm under 
laser speckle contrast imaging for targeted delivery,'' Science Robotics, 
vol. 9, no. 87, pp. eadh1978, 2024. 
[6] J. Yu, D. Jin, K. F. Chan, et al., ''Active generation and magnetic actuation 
of microrobotic swarms in bio-fluids,'' Nature Communications, vol. 10, 
pp. 5631, 2019. 
[7] H. Xie, M. Sun, X. Fan, Z. Lin, W. Chen, L. Wang, L. Dong, and Q. He, 
''Reconfigurable magnetic microrobot swarm: Multimode transformation, 
locomotion, and manipulation,'' Science Robotics, vol. 4, no. 28, pp. 
eaav8006, 2019. 
[8] L. Yang, J. Yu, and L. Zhang, ''Statistics-Based Automated Control for a 
Swarm of Paramagnetic Nanoparticles in 2-D Space,'' IEEE Transactions 
on Robotics, vol. 36, no. 1, pp. 254--270, 2020. 
[9] F. Arvin, S. Yue, and C. Xiong, "Colias-φ: An autonomous micro robot 
for artificial pheromone communication," International Journal of 
Mechanical Engineering and Robotics Research, vol. 4, no. 4, pp. 349, 
2015. 
[10] K. Feng, Q. Xu, S. F. Wong, and B. Zi, ''Design and Development of a 
Teleoperated Telepresence Robot System With High-Fidelity Haptic 
Feedback Assistance,'' IEEE Transactions on Automation Science and 
Engineering, vol. 22, pp. 1069--1080, 2025. 
[11] E. Abdi, D. Kulić, and E. Croft, ``Haptics in Teleoperated Medical 
Interventions: Force Measurement, Haptic Interfaces and Their Influence 
on User's Performance,'' IEEE Transactions on Biomedical Engineering, 
vol. 67, no. 12, pp. 3438--3451, 2020. 
[12] Z. Lin, A. Gao, X. Ai, H. Gao, Y. Fu, W. Chen, and G.-Z. Yang, ''ARei: 
Augmented-Reality-Assisted 
Touchless 
Teleoperated 
Robot 
for 
Endoluminal Intervention,'' IEEE/ASME Transactions on Mechatronics, 
vol. 27, no. 5, pp. 3144--3154, 2022. 
[13] J. W. Martin, B. Scaglioni, J. C. Norton, V. Subramanian, A. Arezzo, K. 
L. Obstein, and P. Valdastri, ''Enabling the future of colonoscopy with 
intelligent and autonomous magnetic manipulation,'' Nature Machine 
Intelligence, vol. 2, no. 10, pp. 595--606, 2020. 
[14] A. M. M. B. Chowdhury, S. A. Abbasi, N. L. Gharamaleki, J. Kim, and 
H. Choi, ''Virtual Reality-Enabled Intuitive Magnetic Manipulation of 
Microrobots and Nanoparticles,'' Advanced Intelligent Systems, vol. 6, no. 
7, pp. 2300793, 2024. 
[15] J. Lee, X. Zhang, C. H. Park, and M. J. Kim, ''Real-Time Teleoperation 
of Magnetic Force-Driven Microrobots With 3D Haptic Force Feedback 
for Micro-Navigation and Micro-Transportation,'' IEEE Robotics and 
Automation Letters, vol. 6, no. 2, pp. 1769--1776, 2021. 
[16] K. Darvish, L. Penco, J. Ramos, R. Cisneros, J. Pratt, E. Yoshida, S. Ivaldi, 
and D. Pucci, ''Teleoperation of Humanoid Robots: A Survey,'' IEEE 
Transactions on Robotics, vol. 39, no. 3, pp. 1706--1727, 2023. 
[17] J. J. Abbott, E. Diller, and A. J. Petruska, '' Magnetic methods in robotics,'' 
Annual Review of Control, Robotics, and Autonomous Systems, vol. 3, 
no. 1, pp. 57--90, 2020. 
[18] S. G. Hart and L. E. Staveland, ''Development of NASA-TLX (Task Load 
Index): Results of empirical and theoretical research,'' in Advances in 
Psychology, vol. 52, Elsevier, 1988, pp. 139--183. 
 
71
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:24:24 UTC from IEEE Xplore.  Restrictions apply. 
