# Turco Reducing Cognitive Load in Teleoperating Swarms of Robots through a Data-Driven Shared Control Approach

*Source file: Turco_Reducing_Cognitive_Load_in_Teleoperating_Swarms_of_Robots_through_a_Data-Driven_Shared_Control_Approach.pdf — 8 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

Reducing Cognitive Load in Teleoperating Swarms of Robots through a
Data-Driven Shared Control Approach
Enrico Turco1, Chiara Castellani1, Valerio Bo1,
Claudio Pacchierotti2, Domenico Prattichizzo1,3, and Tommaso Lisini Baldi1,3
Abstract— Multi-robot systems have gained increasing in-
terest across various fields such as medicine, environmental
monitoring, and more. Despite the evident advantages, the
coordination of the swarm arises significant challenges for
human operators, particularly concerning the cognitive burden
needed for efficiently controlling the robots. In this study, we
present a novel approach for enabling a human operator to
effectively control the motion of multiple robots. Leveraging a
shared control data-driven approach, we enable a single user to
control the 9 degrees of freedom related to the pose and shape
of a swarm. Our methodology was evaluated through an ex-
perimental campaign conducted in simulated 3D environments
featuring a narrow cylindrical path, which could represent, e.g.,
blood vessels, industrial pipes. Subjective measures of cognitive
load were assessed using a post-experiment questionnaire,
comparing different levels of autonomy of the system. Results
show substantial reductions in operator cognitive load when
compared to conventional teleoperation techniques, accompa-
nied by enhancements in task performance, including reduced
completion times and fewer instances of contact with obstacles.
This research underscores the efficacy of our approach in
enhancing human-robot interaction and improving operational
efficiency in multi-robot systems.
I. INTRODUCTION
Multi-robot systems are emerging as an important area
of research due to their potential to impact various fields,
including search and rescue operations, environmental mon-
itoring, medical robotics, and industrial automation. One
example is the utilization of swarms of drones for tasks such
as surveillance, disaster response, and agricultural monitor-
ing. These systems leverage the collective intelligence and
coordination of multiple robots to achieve tasks that would
be impractical or impossible for a single robot to accomplish
efficiently [1], [2]. Ground mobile robots represent another
significant application of multi-robot systems, particularly
in scenarios requiring exploration, mapping, or transporta-
tion tasks in challenging environments. These robots can
collaborate to cover larger areas, share information, and
effectively adapt to dynamic conditions. In the field of
medical interventions, microrobots designed for endovascular
1Istituto
Italiano
di
Tecnologia,
Genoa,
Italy
{name.surname}@iit.it
2CNRS,
Univ
Rennes,
Inria,
IRISA
–
Rennes,
France.
{name.surname}@irisa.fr
3Universit`a degli Studi di Siena, Dip. di Ingegneria dell’Informazione e
Scienze Matematiche, Siena, Italy. {name.surname}@unisi.it
This work was supported by the European Union’s Horizon Europe
Research and Innovation Programme under Grant Agreement #101070066,
project REGO, by the University of Siena curiosity driven (F-CUR) pro-
gramme project ”BRIOCHE: wearaBle sensoRImOtor interfaCes for Human
augmentation”, and by the European Union’s FSE REACT-EU programme,
PON Ricerca e Innovazione 2014-2020
(a)
(b)
Fig. 1: In a), two operators collaboratively control the 9 DoFs
of the robotic swarm using two interfaces. Conversely, b)
illustrates the effectiveness of the proposed method, in which
a single operator skillfully steers the swarm to complete
a task, exploiting our novel shared control strategy. This
method simplifies the control by assigning a subset of the
degrees of freedom to the user, significantly reducing the
operational complexity and enhancing user capability.
procedures and surgeries [3] offer precise control and mini-
mally invasive capabilities [4], [5]. Their small size enables
access to intricate anatomical structures with reduced risk to
patients. The effective utilization of such robots has already
been demonstrated, with applications including targeted drug
delivery [6], minimally-invasive surgical procedures [7], and
diagnostics [8].
While the advantages of multi-robot systems are evident,
the complexity of coordinating multiple independent agents
poses challenges for human operators. Controlling the mo-
tion of numerous robots simultaneously in an intuitive and
effective manner requires sophisticated interfaces and algo-
rithms. Ensuring seamless interaction between humans and
multi-robot systems is crucial for maximizing their potential
benefits while minimizing operational complexities, safety
risks, human-robot trust, and the cognitive load imposed on
users during control [9]. An emphasis on user-centric design
is essential for unlocking the potential of multi-robot systems
2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
October 14-18, 2024. Abu Dhabi, UAE
979-8-3503-7770-5/24/$31.00 ©2024 IEEE
4731
2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | 979-8-3503-7770-5/24/$31.00 ©2024 IEEE | DOI: 10.1109/IROS58592.2024.10802645
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:27:42 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 2]**
*(This page contains a figure/chart/image not captured in text)*

across a wide range of applications. In this respect, different
approaches have been developed to enable human users to
effectively control multiple robots. Shared control techniques
focus on distributing control responsibilities between humans
and autonomous systems [10]. These methods aim to en-
hance human-robot collaboration by combining the decision-
making capabilities of both entities, leading to improved task
performance and operational efficiency. Similarly, shifting
autonomy approaches emphasize the dynamic adjustment of
robot autonomy levels based on the task requirements and
environmental conditions [11]. By allowing robots to adapt
their autonomy level in real time, these approaches enhance
the flexibility and responsiveness of robotic systems. Further-
more, distributed approaches have been proposed to address
the challenges associated with coordinating robots [12], [13].
Finally, research focusing on neural learning-based control
for multi-robot systems aims to leverage advanced machine
learning techniques to enhance coordination and decision-
making processes among multiple robots [14], [15].
Research has shown that increasing robot autonomy can
reduce the users’ cognitive load [16]. This is due to the fact
that the cognitive load depends on the number of conceptual
elements users need to hold in mind simultaneously to ac-
complish a specific task [17]. However, while the autonomy
level influences the teleoperator’s perceived cognitive load
and trust, there is no clear interaction between these latter
factors [9]. In this context, we can consider each degree
of freedom (DoF) of our robotic system as a conceptual
element; therefore, minimizing the number of DoFs the users
need to control is expected to reduce their cognitive load.
This paper presents a data-driven shared-control approach
designed to dynamically allocate the controlled DoFs of
a multi-robot system between the human operator and an
autonomous controller, seeking the best compromise between
the effectiveness of the control and the demanded cognitive
load. We leverage statistical analysis on data collected from
human demonstrations to design the shared control strategies,
which are then evaluated in a human-subjects experiment
where users control a simulated swarm in a narrow and
tortuous environment. Through such collaborative control
mechanisms, we aim to streamline the teleoperation process,
enabling operators to focus on high-level task objectives
while the system autonomously manages low-level naviga-
tion and coordination tasks.
The rest of the paper is organized as follows. Sec. II
introduces the teleoperation framework, whereas in Sec. III
the devised control strategies are explained. The conducted
experiments are described in Sec. IV, while Sec. V discusses
their outcomes. Lastly, Sec. VI draws the conclusions of the
paper, outlining possible further developments.
II. SYSTEM OVERVIEW
The system reproduces the motion of a robotic swarm,
controlled by a human operator via haptic interfaces through
a narrow and tortuous path emulating a blood vessel or an
industrial pipe.
Fig. 2: Navigation path: the green and red stars indicate the
beginning and end of the route, respectively.
(a)
(b)
Fig. 3: a) Swarm robot with its reference frame; the axes are
represented in red (x), green (y), and blue (z). The angles
ϕ, θ and ψ represent rotations referred to the swarm frame
around its axes. b) Deformations of the swarm along the
three axes of its reference system.
The virtual environment is developed in CoppeliaSim and
graphically rendered using a desktop PC. The swarm is com-
posed of 64 spherical agents initially arranged in a spherical
formation with a depth sensor placed at its center. The target
environment features straight and curved, deformed and
non-deformed segments (turquoise-colored pipe in Fig. 2).
As noticeable from the figure, we intentionally designed a
complex pipe-like pathway to evaluate the operators’ ability
in adjusting the swarm’s shape and trajectory during the
navigation.
The pose and shape of the swarm can be controlled with
9 DoFs, being the pose of the swarm centroid 6 DoFs (i.e.,
position p = [x, y, z] and orientation o = [ϕ, θ, ψ]) and
3 additional DoFs for modifying the shape along its three
perpendicular axes of symmetry (δ = [δx, δy, δz]). Fig. 3
visually reports the controllable degrees of freedom. The
DoFs can be controlled either partially or entirely by one
or two users utilizing a pair of Omega.7 haptic interfaces
(Force Dimension, CH), depending on the specific conditions
being considered. The Omega.7 interfaces enable users to
collaboratively control the 9 DoFs of the robotic swarm.
One haptic interface is for managing the pose of the swarm
centroid (6 DoFs), while the other is dedicated to controlling
the swarm deformation along its 3 axes of symmetry (3
DoFs). A generic deformation δ along one of these axes
results in an expansion or a contraction of the swarm by
4732
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:27:42 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 3]**

moving its elements along that direction (see Fig. 3b).
The deformation control ensures the swarm elements move
along an ellipsoidal surface and prevents overlapping during
expansion or contraction. Besides, deformation values are
limited to avoid excessive contractions and stretching of
the swarm. Deformation DoFs are essential for navigating
complex environments, such as the one proposed in this
work, which includes paths with varying geometries.
The mapping between the 9 DoFs of the swarm and the
two interfaces is realized with an incremental strategy. The
connection between the control interface and the controllable
DoFs of the swarm is established by activating the clutch
on the haptic devices. Consequently, when the clutch is
activated, the poses of both the interface h(t0) and the
swarm s(t0) are stored, allowing the operator to relocate
the interface handle to a new position h(t1). The difference
∆h between h(t0) and h(t1) is calculated as follows:
∆hp = hp(t1) −hp(t0)
∆ho = ho(t1)ho(t0)−1,
where hp ∈R3×1 is the position vector and ho ∈R3×3 is
the orientation matrix of the interface handle. Finally, ∆h
is transformed into the swarm reference system and added
to s(t0) to obtain the desired new pose. A similar approach
can be applied to the deformation control. In addition to
controlling the swarm, the system also provides users with
both haptic and visual feedback crucial for improving per-
formance in accomplishing the tasks. Indeed, in the event of
a collision with the pipe wall, users receive vibrations on the
handles of the haptic interfaces along with visual cues (i.e.,
the pipe-like path changes color from turquoise to red as in
Fig. 1a).
ROS served as the framework between the two haptic
interfaces, and CoppeliaSim was used to control the swarm
robot and acquire data from the simulated environment.
III. DATA-DRIVEN SHARED CONTROL
This Section details the design of a shared-control strat-
egy aiming at minimizing cognitive load while maximizing
performance for a single teleoperator. Initially, we gathered
and processed data from demonstrations involving two users
simultaneously teleoperating the swarm using the two haptic
interfaces. Leveraging data analysis techniques, we propose
a framework for shared control of the swarm.
A. Data collection from dual-user experiments
The data collection procedure involved 10 subjects (5
males and 5 females, aged between 24 and 35 years, average
age 28 ± 3.1). Among these participants, one had prior
experience with teleoperation devices, providing a diverse
sample in terms of familiarity with the technology used.
The 10 participants were randomly paired into 5 groups.
This randomization was aimed at minimizing biases related
to individual skill level or prior experiences. Each pair
formed a collaborative team for the duration of the data
collection phase, jointly controlling the swarm across the
designated pipe-like path (see Fig. 2). The experimental
campaign followed the declaration of Helsinki, and there
was no risk of harmful effects on subjects’ health. Each
participant gave written informed consent and was able to
discontinue participation at any time during experiments. No
payment was provided to the users. None of the participants
reported any deficiencies in their visual or haptic perception
abilities.
Users were introduced to the teleoperation system, asking
them to: i) navigate through the pipe-like path as quickly as
possible, ii) occupy with the robotic swarm the largest pos-
sible cross-sectional area within the path, and iii) minimize
the number of collisions with the environment. Users were
given a short period (2 minutes) to acquaint themselves with
the system, followed by an initial practice session.
Each pair of users repeated the assigned task 6 times. In
the first three trials, one user controlled the swarm pose
while the second one managed its deformation. From the
fourth to the last trial, the roles were reversed allowing each
participant to experience both aspects of the swarm control
(pose or deformation). In this scenario, the human operators
fully controlled all the degrees of freedom of the swarm,
without any autonomy involved.
The following metrics were used to evaluate the per-
formance in accomplishing the requested task: i) the time
necessary to complete the path tp, ii) the percentage Ac ∈
[0, 100] of path area occupied by the swarm along its section,
and iii) the number of collisions nc. Lower values of tp
and nc indicate better performance, whereas Ac closer to
100 corresponds to a higher average occupied cross-sectional
area. For our analysis, we treated the dual system as a
single Dual-Position-Orientation-Deformation (D-POD) sys-
tem, considering these metrics depended on both the users.
Additionally, subjective measures of cognitive load were
collected through the NASA Task Load Index (NASA-
TLX) questionnaire [18] for assessing the perceived work-
load across various dimensions, including Mental Demand,
Physical Demand, Temporal Demand, Performance, Effort,
and Frustration. This method evaluates the load using a 7-
point scale, where each of the six questions is rated on a
21-level scale: 1 indicates “very low”, while 21 indicates
“very high”.
Each participant was asked to complete the questionnaire
twice, once after having controlled the pose (3 trials) and
once after having controlled the deformation (3 trials) of the
swarm. This approach insights into how each aspect of the
control task contributed to the overall workload and how the
allocation of responsibilities between pose and deformation
control influenced the users’ experience.
We collected a total of 30 data sets including both the
users control inputs (i.e., positions p, orientations o and
deformations δ) and the depth data from the sensor.
B. Data analysis for variance estimation
In what follows, we present a systematic approach for ana-
lyzing the demonstration data using point cloud information.
The goal of this analysis is to determine which DoFs were
most controlled during the trials. Initially, we developed a
4733
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:27:42 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 4: A representative path labeled by the Gaussian Mixture
Model clustering algorithm.
method to discretize the obtained data into shorter signals
based on the similarities within the point clouds. This process
started with the computation of Delaunay triangulation to
partition the points into non-overlapping triangles. As second
step, we constructed a dual Voronoi graph to determine the
central path as its medial axis. Two parameters were then
defined to quantify path curvature and deformation, achieved
by comparing fitting errors from linear and quadratic splines
along the central path.
Deformation values were assessed by evaluating the width
of the cloud at various path locations. A Gaussian Mixture
Model (GMM) clustering algorithm was thus applied to
categorize the path into four types: straight non-deformed,
straight deformed, curved non-deformed, and curved de-
formed. This classification process enabled the segmenta-
tion of demonstrations into labeled subsections for further
analysis. Fig. 4 shows the application of this method in a
representative trial. Note that this approach can be applied
to paths of any shape, and consequently can be retrieved in
real environment using standard imaging systems, e.g., 3D,
CT scans.
After having classified the data into the different subsec-
tions, we proceeded to analyze how the users controlled the
swarm DoFs, separately for each path type. Normalization
and alignment of signals were performed to standardize
measurements and compare operator performance, using
Dynamic Time Warping (DTW) algorithm for temporal se-
quence alignment. We then evaluated inter-users variability
among commanded positions, orientations, and deformations
to identify trends in operator performance. To this aim,
Pareto diagrams were utilized to analyze the datasets fea-
tures’ variance. Since we obtained similar results for all the
different subsections, we ended the process with a unified
analysis merging all subsets for a comprehensive evaluation
of the data. As can be seen from Fig. 5, the analysis reveals
that deformation exhibits the highest inter-users variability,
while position demonstrates the least.
Fig. 5: Pareto diagram constructed by plotting the controlled
DoFs along the x-axis, and their corresponding variances
along the y-axis, in descending order. The right y-axis
displays the percentage of the total variance.
C. Shared-control algorithms for multi-robot control
Human operators and autonomous algorithms collaborate
on swarm control, with the sharing of authority depending
on the task, environment, and user experience.
In applications in which the system is controlled by an
expert operator in unstructured and/or dynamic environments
(e.g., industrial maintenance, medical procedures), we expect
users to prefer firsthand managing the DoFs that have been
controlled with less arbitrariness during different demon-
strations, i.e., those who have showed lower variabilities.
Conversely, in applications in which the system is guided
by a na¨ıve operator in more structured environments (e.g.,
industrial or medical training), we expect the autonomous
controller to take over the DoFs users controlled more
similarly among the demonstrations.
As shown in Fig. 5, our analysis identified the greatest
variability in the swarm deformations δ, meaning that these
DoFs were controlled the most by users during the demon-
strations. From this analysis, we proposed four shared control
techniques, that share the available DoFs between one human
user and the autonomous controller in different ways:
Single-Deformation (S-D): one user controls the swarm de-
formation (3 DoF, 65% of the total variance), the
autonomous controller controls the swarm pose (6 DoF).
Single-Deformation-Orientation (S-DO): one user controls
the swarm deformation and orientation (6 DoF, 90% of
the total variance), the autonomous controller controls
the swarm position (3 DoF).
Single-Position (S-P): one user controls the swarm position
(3 DoF, 10% of the total variance), the autonomous con-
troller controls the swarm orientation and deformation
(6 DoF).
Single-Position-Orientation (S-PO): one user controls the
swarm pose (6 DoF, 35% of the total variance), the
autonomous controller controls the swarm deformation
(3 DoF).
Table I summarizes the developed control technique report-
ing controlled DoFs and corresponding explained variance.
The controllers are based on vision data, where the in-
formation extracted from the point cloud as explained in
Sec. III-B is exploited as reference for the controllers. In
this way, our approach can generalize to new environments,
eliminating the need for prior modeling.
4734
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:27:42 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 5]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 6: Shared control scheme. The swarm state s includes position p, orientation o, and deformation δ. In each shared
control strategy, the user is allocated control over a subset of the robot DoFs (sh), while the other DoFs (sc) are imparted by
the autonomous controller. h indicates the pose of the haptic interface handle which is mapped into the desired state value
ˆ
sh. The autonomous controller outputs the desired robot state variables ˆsc, based on the information about the pipe path
extracted from the point cloud (central path and pipe section) and the current robot state. The final vector s is composed of
ˆ
sh and ˆsc
Control
Technique
User
Autonomous Controller
Controlled DoFs
Variance
Controlled DoFs
Variance
S-D
Deformation (δx, δy, δz)
65%
Position (px, py, pz)
35%
Orientation (ϕ, θ, ψ)
S-DO
Deformation (δx, δy, δz)
90%
Position (px, py, pz)
10%
Orientation (ϕ, θ, ψ)
S-P
Position (px, py, pz)
10%
Deformation (δx, δy, δz)
90%
Orientation (ϕ, θ, ψ)
S-PO
Position (px, py, pz)
35%
Deformation (δx, δy, δz)
65%
Orientation (ϕ, θ, ψ)
TABLE I: Developed control techniques. For each modality
the controlled DoFs and the corresponding variance are
reported, both for the user and for the autonomous controller.
The overall shared control scheme is shown in Fig. 6
where sh refers to the DoFs controlled by the user through
the haptic interfaces, while sc refers to the DoFs governed
by the autonomous controller.
When users are in charge of positions (S-P), the au-
tonomous controller adjusts the swarm’s shape to optimize
the occupied area while avoiding collisions with the pipe’s
wall. Here, the autonomous control action sc is represented
by δc, which is computed as δc(t + 1) = δc(t) + uδ, where
the control input uδ is proportional to the deformation error,
defined as the difference between the ideal and the current
deformation. The ideal deformation accounts for the swarm’s
distance from the central path, optimizing the occupied area
while avoiding collisions with the pipe’s wall.
In S-D, the autonomous controller regulates the positions
to minimize the distance between the center of the swarm
and the path while maintaining the elements of the swarm
as close as possible to the borders of the tube. Here, the
autonomous control action sc is represented by pc, which is
defined as pc(t+1) = pc(t)+up, where up, similarly to S-P,
is proportional to the position error, defined as the difference
between the path center and the current swarm center. We
did that to provide users with visual feedback and ensure
consistency in pose and deformation control methodologies.
In both control modes, the swarm is oriented in order to
have its x axis pointing towards the direction of motion.
The working principle of S-PO and S-DO is the same as the
previous controllers, but differently the users are in charge
of orientations.
In addition to these four shared control techniques, for
the sake of comparison, we consider two standard human-in-
the-loop teleoperation conditions, where the human operator
retains complete control (no autonomy), i.e.,
Single-Position-Orientation-Deformation (S-POD): one
user controls both the swarm pose (6 DoF) and
deformation (3 DoF).
Dual-Position-Orientation-Deformation (D-POD): one user
controls the swarm pose (6 DoF), another user controls
the swarm deformation (3 DoF). This modality was used
in Sec. III-A for the data collection).
The allocation of the control DoFs between the two
Omega.7 interfaces is the same as in Sec. III-A.
IV. EXPERIMENTAL EVALUATION
In this Section, we describe the experiments conducted to
evaluate the shared-control strategies described in Sec. III-
C. The same 10 subjects who participated in the initial
data collection phase of Sec. III-A were involved in this
experimental evaluation.
The experimental protocol was designed to conclude
within a maximum duration of sixty minutes per participant,
aiming to minimize fatigue and ensure a high engagement
throughout the session. Participants received a briefing on
the objectives and a 2-minute training session to familiarize
themselves with the control techniques.
Each participant was asked to navigate the swarm through
the pipe-like path described in Sec. II three times per control
4735
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:27:42 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 7: Comparison of the quantitative metrics. Median and
interquartile range of the six conditions are plotted. p-values
are reported above the bar charts. The symbols ∗, ∗∗, and
∗∗∗denote the levels of statistical significance.
condition, for a total of 15 trials (3 repetitions × 5 controls:
S-D, S-DO, S-P, S-PO, S-POD). We did not carry out new
repetitions in the D-POD control condition, as it had already
been tested during the data collection phase (see Sec. III-
A). As described in Sec. III-A, participants were asked to
steer the swarm across the pipe-like path as fast as possible
and occupy the largest possible cross-sectional area while
minimizing the number of collisions with the environment.
To mitigate potential learning biases, the presentation order
of the control conditions to the users was randomized.
After each task, participants were asked to complete a
NASA-TLX questionnaire to assess their subjective cognitive
load. We also recorded quantitative performance metrics, i.e.,
the task completion time tp, the average normalized cross-
sectional area of the path occupied by the swarm Ac, and
the number of collisions nc, as in Sec. III-A.
V. RESULTS AND DISCUSSION
This Section presents and discusses the outcomes of the
experimental evaluation.
Data across the three repetitions from the same subject and
control condition were averaged. Values that lay beyond 1.5
times the interquartile range (IQR) from the first (Q1) and
third (Q3) quartiles were considered outliers, We identified
and removed from the analysis three outliers within our
dataset associated with the temporal metric tc. Specifically,
their values surpassed the aforementioned threshold, indi-
cating significant deviation from the typical trial durations.
Data were normally distributed as assessed by the Shapiro-
Wilk test (p > 0.05). A one-way repeated-measures ANOVA
was employed to analyze metrics tc (time) and Ac (occupied
area), whereas we carried out a Friedman test to analyze
nc (collisions), as this variable is measured on an ordinal
scale. A post-hoc analysis employing a Bonferroni correction
was conducted to identify differences between the conditions.
This adjustment is crucial in multi-comparison scenarios to
mitigate the risk of type I errors, i.e. to reduce possible false
positive results.
The NASA-TLX questionnaire results were weighted to
reflect the relative importance of each workload dimension.
Subsequently, a Friedman non-parametric test was applied to
these weighted scores to assess significant differences among
the controllers we developed. This analysis was instrumental
in confirming the distinctions in perceived workload and
cognitive demands associated with each control strategy1.
A. Quantitative metrics
Fig. 7 shows the results for the objective metrics. Overall,
all the four shared control techniques (S-D, S-DO, S-P, S-
PO) present statistically significant improvements compared
to single- (S-POD) and dual-user (D-POD) standard teleop-
eration controls.
Results also suggests that each of the four shared control
techniques offers distinct advantages. The control strategies
in which the user directly controls the swarm deformation
(S-D, S-DO) demonstrate high performance in maximizing
the swarm’s occupied area during navigation, indicative of
an effective space utilization. S-D displays a median score
of 65.63 with a Q1-Q3 range of 46.54-72.88, while S-DO
records a median of 64.02 within a more compact range of
49.31-67.9. Furthermore, both modalities contribute to a no-
table reduction in terms of task completion time, signifying
their operational efficiency. The consistency of these results
is reflected in the interquartile ranges, indicating reliable
performance across trials.
Control strategies with direct user control over swarm
position (S-P, S-PO) yielded different results. The S-P control
strategy not only presents good performance indicators in
terms of occupied areas, but it also enhance users precision,
resulting in significantly fewer collisions and lower task com-
pletion time with respect to the standard S-POD and D-POD
control strategies. Conversely, S-PO is the control condition
that led to the worst results. It showed the lowest median for
the occupancy area Ac (Mdn: 13.15, Q1-Q3:12.72-17.52);
1For NASA-TLX analysis, the D-POD analysis was split in D-PO and
D-D as users filled questionnaires for both pose and deformation.
4736
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:27:42 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 8: Comparison of the NASA-TLX for all the tasks. Mean and standard deviation are reported for all the conditions.
p-values are reported above the bar charts.
however, it still outperforms in terms of completion time the
two standard teleoperation modalities S-POD and D-POD.
We can also appreciate how the shared control techniques
show significantly lower variability with respect to S-POD
and D-POD, reflecting inconsistent performance when par-
ticipants had to control all the available DoFs. This inconsis-
tency is likely due to the higher manual dexterity required,
which led to both high variability in the results as well as
generally worse performance. However, S-POD did not lead
to significantly better performance than D-POD. Indeed, we
expected that collaborating with another user would have
led to worse performance, also considering that all subjects
carried out the task in the D-POD condition first.
B. Qualitative metrics
Fig. 8 shows the results for the subjective metrics. The
subjective findings align with the objective analysis discussed
above. This quantitative evidence is mirrored in the subjec-
tive experiences of participants, as captured in the data from
the NASA-TLX scores.
The weighted NASA-TLX results presented in the boxplot
reflect differences in perceived workload among the various
control strategies. It’s notable that strategies involving de-
formation control (S-D and S-DO) show significantly lower
scores in mental demand with respect to S-POD and D-
PO. This reduction points to an improved user experience,
suggesting that the deformation control strategies may align
better with the operator’s capabilities, leading to a more
intuitive and less mentally taxing interaction. The congru-
ence between these subjective assessments and the objective
performance metrics underscores the effectiveness of these
control strategies in both perceived and actual ease of use,
enhancing overall satisfaction with the system’s performance.
Additionally, participants positively evaluate the S-P con-
troller in terms of mental demanding (Mdn:31, Q1-Q3: 18.5-
44). Overall, all the developed shared controllers are less
cognitively demanding than full manual control modalities.
Regarding physical load, participant feedback generally
indicates a low physical demand among the controllers.
Notably, the S-POD modality exhibits considerable variabil-
ity (Mdn: 18.75, Q1-Q3: 12-25.5), likely due to the com-
plexity of manipulating dual interfaces simultaneously, thus
increasing the physical engagement required. Furthermore,
compared to the deformation controllers (S-D, S-DO, and D-
D), bimanual control physical demand is significantly higher.
Temporal demand was perceived similarly across all con-
trol modalities, indicating no perceivable difference in the
pressure to perform tasks quickly. Lower temporal demand
values were noted for autonomous trajectory control of the
swarm (S-D and S-DO). However, there are no significant
differences, as the perception of individual users is very
variable, as can be seen in the wide interquartile range of
S-D, Q1-Q3:18-39. Conversely, position controls (S-P and
S-PO) and manual controls (S-POD and D-PO) exhibited
narrower interquartile ranges, indicating a more uniform user
experience in terms of temporal pressure.
While the NASA-TLX scores for performance do not
show statistically significant differences among the various
4737
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:27:42 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 8]**

S-P
S-PO
S-D
S-DO
S-POD
D-PO
D-D
Overall Weighted
Workload Score
41.58
52.83
38.2
35.6
72.07
70.25
58.8
TABLE II: NASA-TLX workload.
control modes, the participants generally gave lower perfor-
mance ratings to the shared control strategies over direct
teleoperation. Note that, for this metric, the lower the score
the better the perception of success. This suggests that the
shared control interfaces may enhance the user’s perceived
effectiveness in operating the swarm.
In assessing perceived effort, our shared control archi-
tectures evidently ease the workload on users. Specifically,
the position control (S-P) and the deformation controls (S-
D and S-DO) are associated with significantly less effort as
per user feedback, in stark contrast to the direct controls,
such as S-POD and D-PO. This distinction underscores the
ergonomic advantage of shared control systems in user-
system interaction.
Eventually, S-P, S-D, and S-DO control modes show
marked reduced user frustration compared to the bimanual
control (S-POD) and dual-user teleoperation (D-PO). This is
likely due to the complexity of managing the swarm’s posi-
tion and orientation, which is inherently more demanding and
can lead to increased frustration, as reflected by the higher
median score (Mdn: 31.25, Q1-Q3: 2.5-52.5) observed in the
S-PO pose control mode.
Overall, the subjective analysis reveals that our shared-
control strategies statistically significantly reduce cognitive
load, indicating reduced mental demand, effort, and frustra-
tion for the users.
For the sake of completeness and clarity, we report the
total workload in Table II. It is evident that the deformation
control strategies (S-D and S-DO) exhibited the lowest
overall workloads, indicating an optimized user experience.
These outcomes suggest a correlation between the measured
performance improvements and the operators’ perceived ease
of use and satisfaction with the system.
VI. CONCLUSION AND FUTURE WORKS
In this work, we designed, implemented, and tested data-
driven shared control strategies aimed at reducing the human
cognitive burden on operators during the teleoperation of
robot swarms while enhancing task performance. The pro-
posed approach leveraged an initial data collection phase
involving a dual-user teleoperation task in a 3D simulated
complex environment. Analyzing the variability of the de-
grees of freedom controlled by the users, we designed four
shared control policies which differ in the level of autonomy.
The resulting controllers demonstrated the capacity to assist a
single operator in managing a complex system with multiple
degrees of freedom.
An extensive and careful evaluation, supported by a user
study, confirmed that the developed controllers significantly
reduce the cognitive load and improve the task performance.
In particular, the best control modality turned out to be to
automate the DoFs with less variability while leaving the
user in control of the others; in this way, it is possible to
create shared control strategies where the user can focus on
the more subjective aspects of the task, i.e. the ones with
more variability.
Future work will employ machine learning algorithms
(e.g., Reinforcement Learning) to improve the presented
controllers starting from the data gathered in this study.
We will also explore the application of these strategies in
more varied and dynamic environments to further validate
their robustness and applicability in real-world scenarios
(e.g., microrobot swarm navigation in blood vessels or drone
navigation in constrained scenarios at the macroscale).
REFERENCES
[1] J. Cort´es and M. Egerstedt, “Coordinated control of multi-robot
systems: A survey,” SICE Journal of Control, Measurement, and
System Integration, vol. 10, no. 6, pp. 495–503, 2017.
[2] R. N. Darmanin and M. K. Bugeja, “A review on multi-robot systems
categorised by application domain,” in Proc. Mediterranean confer-
ence on control and automation (MED), 2017, pp. 701–706.
[3] Z. Lin, T. Jiang, and J. Shang, “The emerging technology of biohybrid
micro-robots: a review,” Bio-Design and Manufacturing, pp. 1–26,
2022.
[4] B. J. Nelson, S. Gervasoni, P. W. Chiu, L. Zhang, and A. Zemmar,
“Magnetically actuated medical robots: An in vivo perspective,” Pro-
ceedings of the IEEE, vol. 110, no. 7, pp. 1028–1037, 2022.
[5] B. Wang, K. Kostarelos, B. J. Nelson, and L. Zhang, “Trends in
micro-/nanorobotics: materials development, actuation, localization,
and system integration for biomedical applications,” Advanced Ma-
terials, vol. 33, no. 4, p. 2002047, 2021.
[6] M. Luo, Y. Feng, T. Wang, and J. Guan, “Micro-/nanorobots at work in
active drug delivery,” Advanced Functional Materials, vol. 28, no. 25,
p. 1706100, 2018.
[7] P. A. York, R. Pe˜na, D. Kent, and R. J. Wood, “Microrobotic laser
steering for minimally invasive surgery,” Science Robotics, vol. 6,
no. 50, p. eabd5476, 2021.
[8] X. Yan, Q. Zhou, M. Vincent, Y. Deng, J. Yu, J. Xu, T. Xu, T. Tang,
L. Bian, Y.-X. J. Wang et al., “Multifunctional biohybrid magnetite
microrobots for imaging-guided therapy,” Science robotics, vol. 2,
no. 12, p. eaaq1155, 2017.
[9] J. Pan, J. Eden, D. Oetomo, and W. Johal, “Exploring the effects
of shared autonomy on cognitive load and trust in human-robot
interaction,” arXiv preprint arXiv:2402.02758, 2024.
[10] D. A. Abbink, M. Mulder, and E. R. Boer, “Haptic shared control:
smoothly shifting control authority?” Cognition, Technology & Work,
vol. 14, pp. 19–28, 2012.
[11] M. Chiou, N. Hawes, and R. Stolkin, “Mixed-initiative variable
autonomy for remotely operated mobile robots,” ACM Transactions
on Human-Robot Interaction (THRI), vol. 10, no. 4, pp. 1–34, 2021.
[12] L. Iocchi, D. Nardi, M. Piaggio, and A. Sgorbissa, “Distributed coor-
dination in heterogeneous multi-robot systems,” Autonomous robots,
vol. 15, pp. 155–168, 2003.
[13] M. Aggravi, G. Sirignano, P. R. Giordano, and C. Pacchierotti,
“Decentralized control of a heterogeneous human–robot team for
exploration and patrolling,” IEEE Transactions on Automation Science
and Engineering, vol. 19, no. 4, pp. 3109–3125, 2021.
[14] C. Jiang, Z. Chen, and Y. Guo, “Multi-robot formation control:
a comparison between model-based and learning-based methods,”
Journal of Control and Decision, vol. 7, no. 1, pp. 90–108, 2020.
[15] A. Marino, C. Pacchierotti, and P. R. Giordano, “On the stability of
gated graph neural networks,” arXiv preprint arXiv:2305.19235, 2023.
[16] S. Baltrusch, F. Krause, A. de Vries, W. van Dijk, and M. de Looze,
“What about the human in human robot collaboration? a literature
review on hrc’s effects on aspects of job quality,” Ergonomics, vol. 65,
no. 5, pp. 719–740, 2022.
[17] J. L. Plass, R. Moreno, and R. Br¨unken, “Cognitive load theory,” 2010.
[18] S. G. Hart, “Nasa-task load index (nasa-tlx); 20 years later,” in
Proceedings of the human factors and ergonomics society annual
meeting, vol. 50, no. 9.
Sage publications Sage CA: Los Angeles,
CA, 2006, pp. 904–908.
4738
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:27:42 UTC from IEEE Xplore.  Restrictions apply. 
