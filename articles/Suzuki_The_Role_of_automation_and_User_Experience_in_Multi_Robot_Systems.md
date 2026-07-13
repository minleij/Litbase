# Suzuki The Role of automation and User Experience in Multi Robot Systems

*Source file: Suzuki_The_Role_of_automation_and_User_Experience_in_Multi_Robot_Systems.pdf — 8 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

The Role of automation and User Experience in Multi Robot Systems
Kouta Suzuki1 and Miaohui Shi1 and Vimolmongkolporn Vitvasin1 and Yukiko Iwasaki2 and Hiroyasu Iwata1
Abstract— This research delves into the realm of multi-robot
systems, with a focus on integrating remote operation tech-
nologies. It aims to examine how different levels of automation
impact user experience and efficiency in controlling multiple
robots simultaneously. Through a unique approach that blends
automation with human interaction, the study aims to advance
capabilities in multi-presence environments, laying groundwork
for future advancements. At its core is the development of
a state-of-the-art multi-presence system, integrating advanced
robotic arms for remote manipulation tasks. Special attention
is given to automation features to enhance user control. The
research outlines a comprehensive experimental setup to rig-
orously test system performance, assessing aspects like user
efficiency and cognitive load. By comparing scenarios with
varying automation levels, the research seeks to identify an
optimal balance for efficiency and user comfort, providing
insights crucial for future multi-robot system design and im-
plementation in multi-presence environments.
I. INTRODUCTION
In our daily lives, we frequently encounter situations
that require us to multitask, often leading us to wish for
additional ”selves” to ease the burden. Consider the scenario
of preparing a family dinner in the kitchen: while frying food
in a pan and using the oven, it can become overwhelming
to manage both tasks simultaneously. Similarly, when man-
aging a store with insufficient staff, one might wish for an
extra arm capable of performing tasks autonomously. The
ability to be present in multiple locations and accomplish
various tasks concurrently would be immensely beneficial.
Detachable body technology offers a partial realization of
this fantasy, enabling us to manage such situations more
effectively. Yukiko Iwasaki first introduced the concept of
detachable body in 2020, a novel idea for a robotic arm
that could be worn as an extension of the body called
Detachable Body. It can be removed from the user’s natural
body and attached to objects outside of other people and to
other objects[1][2].(Fig1) Jeffrey I. Lipton et. al co-authored
a study titled ”Baxter’s Homunculus,” focusing on the de-
velopment of an innovative remote operation system that
integrates com mercial Virtual Reality (VR) technology with
existing robotic control infrastructures in manufacturing[3].
Researchers at the University of Tokyo have developed a
Telexistence system, a teleoperation mechanism equipped
with an array of sensors[4]. However, there are still many
problems of researchers face. For example, how to operate
the device in a multi-device scenario, how to operate the
device independently when it is not being worn, and how
to reduce the attentional load required when operating the
device.
Ahmed’s experimental studies were conducted in a multi-
presence environment[5]. ”Multi-presence” is a system that
Fig. 1.
(a)Third Arm and (b)Detachable Body
enables simultaneous execution of different tasks at multiple
locations by placing remotely operable extended bodies in
different places and controlling them simultaneously, which
was previously impossible. In these experiments, variables
such as number of robots, task difficulty, and task concur-
rency were manipulated. In the multi-presence setting, the
dimensions of the integrated automatic assistance mode were
also investigated, with the goal of reducing the cognitive load
on the user. According to a 2014 study, robotics automation
levels can be categorized into three classifications based
on human involvement: Human-In-Loop (HIL), Human-
On-Loop (HOL), and Human-Leave-Loop (HLL)[6]. HIL
involves high human participation, HOL involves human
decision-making or monitoring, and HLL involves no direct
human involvement. The study focuses on grasping tasks and
classifies automation levels of a Multi-presence System into
three categories: Level 1 as HIL, Level 2 as a lower HOL,
and Level 3 as a higher HOL. The study excludes HLL
levels to maintain user engagement(TABLE I). The findings
of this study are particularly important in understanding
the cognitive limitations of managing multiple robots. The
study showed that operating three or more robots simulta-
neously places considerable cognitive stress on the user and
reduces performance. However, in active task scenarios that
require continuous attention and decision making, automatic
assistance systems were found to play an important role
in reducing the cognitive load, suggesting that automation
technology could raise the limit on the number of robots that
can be operated simultaneously. The purpose of this study
is to investigate the effect of the degree of autonomy of the
robots on the operator when there are multiple robots that
can be freely operated.
II. METHOD
A. Hardware
The multi-occurrence system proposed in this study pri-
marily consists of three parts: the execution unit, the com-
2024 IEEE 20th International Conference on Automation
Science and Engineering (CASE)
August 28 - September 1, 2024. Bari, Italy
979-8-3503-5851-3/24/$31.00 ©2024 IEEE
3818
2024 IEEE 20th International Conference on Automation Science and Engineering (CASE) | 979-8-3503-5851-3/24/$31.00 ©2024 IEEE | DOI: 10.1109/CASE59546.2024.10711808
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:29:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 2]**
*(This page contains a figure/chart/image not captured in text)*

TABLE I
AUTOMATION LEVELS IN ROBOT CONTROL
Level
Human Task
Robot Task
1
Move robot to the object
Pick up the object
Move robot to the goal
Drop the object
2
Move robot to the object
Pick up the object
Move robot to the goal
Drop the object
3
Decide object
Move robot to the object
Pick up the object
Move robot to the goal
Drop the object
Fig. 2.
(a)Gripper (b)Graping Scene (c)Robot Head
putation unit, and the human input unit.
1) Execution Unit: In this study, we adopted Mycobot,
one of the lightest robot arms in the world. Furthermore,
by attaching a gripper like the one shown in Fig2(a) to
the end of this Mycobot, we enabled it to grasp objects of
various shapes (Fig2(b)). This gripper mimics the movement
of fins in underwater organisms, allowing for flexible object
manipulation. Moreover, its small size and lightweight design
make it suitable for integration with the Mycobot robot
arm. The robot head, shown in Fig.2(c), synchronizes with
the wearer’s movements when attached to a robot’s end
equipped with an HMD-mounted camera, facilitating real-
time viewing of the surroundings and enhancing immersion
in the task or environment. Two main cameras are used in the
robot head for this study: the Intel Realsense L515 and the
Logitech camera. The Intel Realsense L515 is a compact and
lightweight depth camera known for providing high-quality
RGB images. In contrast, the Logitech camera is a standard
RGB camera valued for its high-quality color images, also
compact and lightweight.
2) Computing Unit: The computation part mainly in-
cludes the computation unit on the robot side and the
computation unit on the user side. The computing unit on
the robot side is mainly responsible for the motion control
of the robot and the operation of AI algorithms, while the
computing unit on the user side is mainly responsible for the
human input and the display of information flow. These two
parts are described in detail below. The two communicate
with each other through a network, and the data exchange is
done locally through a router.
3) Human Input Unit: The human input unit mainly
consists of a gamepad and a VR HMD. the gamepad is
mainly used to control the movement of the robotic arm, and
the VR HMD is mainly used for human visual input. The
VR system was chosen to be HTC Vive Pro. a VR headset,
two fixed tracckers were mainly utilised. n this study.
B. Software
1) Middleware: In the Unity environment, ROS# is uti-
lized as the communication method between the robot side
and the user side, primarily accomplishing two tasks[7][8].
Firstly, the robot side sends the images captured by the
camera to the Unity side. Secondly, it sends the head-
mounted display pose and position information to the robot
side to drive the motion of the mechanical head.
In the robot side, ROS serial is utilized as the communi-
cation method between the robot and the mechanical head.
A ROS subscriber has been deployed on the OpenCR to
receive the user’s head pose information sent from the Unity
application. Upon receiving the pose information, it under-
goes decoupling, enabling the control of three servomotors
to move to their respective positions. The servomotors are
connected to the OpenCR via a digital serial bus.
2) Robot Arm Control: In this study, we focus on op-
timizing the control program for a robotic arm, a crucial
component that significantly impacts its performance and ef-
ficiency. We utilized the Python SDK provided by MyCobot
as a robust foundation for creating our own robotic arm
control class, which incorporates both basic functions and
advanced features for complex operations. Special attention
was given to two primary control modes: continuous control
and executing specific actions, managed effectively through
a multi-threaded approach. We implemented a position servo
mechanism for precise movement control, complemented by
a task servo mechanism that allows sequential execution of
predefined tasks. To prevent resource conflicts between these
mechanisms, we employed a semaphore approach, ensuring
efficient task execution while maintaining stability. These
mechanisms have enabled the streamlining of operations
for multiple robotic arms through automation technology,
resulting in improved overall operational efficiency and
precision(Fig3).
3) Image Processing: In this research, the primary tasks
of image processing include integrating images from dif-
ferent cameras and annotating object information identified
Fig. 3.
Robotic Arm Control Diagram
3819
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:29:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 3]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 4.
F1-Confidence Curve
by artificial intelligence in the graphics. Face Vector is
also implemented based on image processing techniques for
interaction. The image processing techniques in this study
are primarily implemented using OpenCV[9][10].
4) Object Detection: Target detection technology was
crucial in this study, particularly in automation Level Three,
aimed at identifying interactive objects within the environ-
ment. The study utilized the YOLOv8 algorithm for target
detection, constructing a dataset with common household
items like kitchen sponges, seasoning boxes, and a toy
truck. Objects were placed within reach of a robotic arm
and rotated to capture information from various angles
realistically. After video generation and editing for clarity,
frames were converted into images to form a dataset. Data
augmentation, including brightness adjustment, blurring, and
rotation, enhanced the dataset. The yolov8m model was
chosen for its size and prediction speed, showing excellent
performance after 20 epochs of training as shown in Fig4.
In the system, RGB images will be input into the YOLOv8
model to obtain position information and bounding box of
the item, with recognition performed in a separate thread for
each captured image[11-17].
5) Camera: In a multi-threaded environment, a double
buffering mechanism is employed to prevent contention
between the camera and other operations. This ensures stable
system performance by allowing continuous image capture
and transmission while avoiding conflicts with memory ac-
cess by other programs.
6) Pose Estimation: To achieve automation level 3, AI-
based 6D pose estimation algorithms were explored, with
PVNet being utilized due to its strong performance on pure
RGB images. However, because different objects require
different models, estimating the poses of multiple objects
in a single image using PVNet would increase processing
time. To mitigate this, following approach was adopted.
Initially, the YOLOv8 model detects objects in the im-
age, then the user selects the target object. Finally, the
appropriate PVNet model is chosen based on the selected
object’s category. This optimization successfully achieved
pose estimation for interactable objects while significantly
Fig. 5.
Pose Estimation Work Flow
Fig. 6.
6D Pose Bound Box
reducing processing time. In this system, an RGB image is
first acquired from the camera, fed into the YOLOv8 model
to obtain object positional information, and then transmitted
to the corresponding PVNet model for pose estimation if a
selected object exists(Fig5). Pose information is subsequently
visualized on the image as shown in Fig6.
C. Single Telepresence System
In this study, the Logitech F710 gamepad is used as the
interface for the user to operate the robotic arm. Based on the
automation levels defined earlier, in both automation Level
1 and automation Level 2, human control is still necessary
for the movement of the robotic arm. Therefore, in these
two automation levels, a game controller’s joystick is used to
control the motion of the robotic arm in Cartesian space. The
left thumb stick and the left D-pad serve the same function,
with the x-axis controlling the robot’s wrist axis motion and
the y-axis controlling the robot’s end effector’s z-axis motion.
The right thumb stick is used to control the robot’s forward,
backward, left, and right movements. The green button is
Fig. 7.
Gamepad Function Layout
3820
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:29:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 8.
Single automation Level 3 workflow
used to activate the robotic arm to open the gripper and return
to the initial position. The red button is used to activate the
robotic arm to perform the function corresponding to the
current automation level, as shown in Fig7.
In automation level 1 and automation level 2, functionally,
the user needs to control the movement of the robotic arm’s
end effector in Cartesian space. The only difference lies in
the function button, namely the red button. In level 1 of
automation, this button is used to drive the gripper to open or
close (reversing the gripper’s state). In level 2 of automation,
the function of the red button is to drive the robotic arm to
close the gripper, then move the gripper above the endpoint
position, and release the gripper.
At automation level 3, the user’s only task is to make a
decision. At this level of automation, the role of the red
button is to confirm the current selection. In this study,
we used face vectors, which were employed for detachable
bodies in previous studies, as a method of selecting objects
for the user to grasp[18]. In this system, the object selected
by the user is the object on the extension parallel to the
orientation of the user’s face that emerges from the center
of the user’s face. In this study, since the user is wearing
a VR-HMD, a direct point is drawn in the center of the
screen to show the orientation of the user’s face. This allows
the user to select objects using head posture. After the user
selects an item, the pose estimation program obtains the
item’s pose information in the camera coordinate system.
Next, the camera coordinates are calculated using MoveIt!
and finally the world coordinates of the item are solved based
on the camera coordinates and sent to the robotic arm. [19]
The robot arm grasps the item based on this information.
The workflow of the system is shown in Fig8.
D. Control System of Multi-Presence
To realize a object control system, the user’s primary
issue is the existence of multiple control targets for a single
user. Therefore, this study has designed a system to ensure
accurate transmission of control signals to the designated
control objects. In this system, an event-driven task response
model is employed. Each control object is equipped with
an event queue. When a user selects a specific control
object, the corresponding event queue is activated. Any user
action triggers a predefined event, which is then added to
the event queue of the selected object and executed. This
design enables simultaneous control of multiple objects while
preventing conflicts. Once an object is activated, all relevant
Fig. 9.
Event Manage System
events are queued without impacting other objects. When
controlling multiple objects, some functions, such as return-
ing to the initial position, differ from single-object control.
This necessitates an independent signal that binds specific
actions to the event of the mechanical arm returning to the
initial position, bypassing the selector. Consequently, the user
can manage both single and multiple objects simultaneously,
as illustrated in Fig9.
This study in automation level 3 of a multi-presence
system adopts a simpler approach. This approach only re-
tains YOLOv8 for item recognition and assigns predefined
positions to the items. When a user selects an item, the preset
position is directly sent to the robotic arm, which moves
to the specified location and performs the grasping task.
This design avoids the need for pose estimation and camera
coordinate calculations, significantly reducing the system’s
computational requirements and greatly enhancing system
stability.
III. EXPERIMENT
A. Experiment Design
This experiment consist of two following tasks.
• Grasp Task:The grasping task refers to the act of
controlling a robotic arm to grasp various interactive
objects. In this experiment, the interactive objects, as
illustrated in the Fig10, included a dish-washing sponge,
Fig10(a), a container for powdered seasoning, Fig10(c),
and a toy truck model, Fig10(b).
• The Paced Auditory Serial Addition Task (PASAT): is
a neuropsychological test often used to assess cognitive
function, particularly in relation to working memory
and attention. It was originally developed to evaluate
cognitive impairment in individuals with multiple scle-
rosis (MS), but it has since been used in a broader
context, including other neurological conditions and
brain injuries. [20]
In the experiment, the participants will be required to operate
three robotic arms at different levels of automation to grasp
various objects. Simultaneously, they will also be asked
to perform the PASAT. During the experiment, the partic-
ipants’ PASAT scores and the number of objects grasped
3821
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:29:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 5]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 10.
Interactive Objects
Fig. 11.
Multi-Presence Questionnaire
by the robotic arms will be recorded. Upon completion of
the experiment, participants will be subjected to a two-
part questionnaire survey: one part focusing on the user
experience of the Multi Presence System, as shown in Fig11,
and the other part being the NASA-TLX questionnaire [21].
In the Multi-Presence questionnaire, as shown in Fig11,
different questions. Questions marked with a ”+” are scored
normally, while those marked with a ”-” are scored in reverse.
Ultimately, the score for each dimension is the average of
the scores from its respective questions.
In the experimental setup, as illustrated in the Fig12,
the experimental subjects were seated in front of a table
within the Unity environment, wearing a HMD and holding
a game controller. Robots being operated were located on
the opposite side of the room, at a certain distance from the
experimental subjects. The digits of the PASAT were played
through two speakers placed in front of the experimental
subjects.
In the course of system operation, the robotic arm may
Fig. 12.
Experiment Setup
encounter random failures. Specifically, under automation
levels 1 and 2, the robotic arm may become stuck during
operation, i.e., it does not respond to user commands. Con-
versely, under automation level 3, the primary failure mode
manifests as unsuccessful item grasping. This investigation
aims to assess how failures in an automated robotic system,
under different automation levels, influence the level of trust
users have in the system.
In the beginning of the experiment, participants were
provided with a detailed introduction to the experimental ob-
jectives and procedures. After ensuring that the participants
understood the rules, the experiment with the administration
of the PASAT task. Subsequently, participants engaged in
practice exercises at automation Level 1. These practice
exercises were divided into two phases: on-site operation
practice and simulated practice with VR. The criterion for
successful practice was that participants could control the
robotic arm to grasp and place objects at specified locations.
Following each practice session, participants were provided
with a 5-10 minute break to prepare for the next stage of the
experiment, which involved the formal testing of automation
Level 1. After each formal experiment, participants were also
given a 5-10 minute break. The experiment followed a pattern
of ”one practice session followed immediately by one formal
experiment,” continuing until the entire experimental process
was completed.
IV. EXPERIMENT RESULT
A. PASAT Score
For the PASAT scores, as shown in Fig13, this study
conducted a detailed analysis. Firstly, each individual exhib-
ited different attention allocation strategies for multitasking,
which is evident from the differences in scores when per-
forming PASAT individually. Secondly, when facing mul-
titasking, individuals also had varying attention allocation
strategies. Some individuals were better at handling parallel
tasks, hence their performance in PASAT was less affected,
while others performed poorly in multitasking, resulting in
3822
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:29:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 13.
PASAT Score
Fig. 14.
Grasp Score
lower PASAT scores. To this end, this study calculated the
average PASAT score for each participant across three trials
as a baseline and computed the deviation of their scores
from this baseline. The results indicated that performance
was optimal at automation level 3 since the robot took on
the majority of tasks, allowing users to concentrate their
attention on PASAT. In contrast, performance was poorest
at automation level 2. Possible reasons for this could be
that, although automation was increased, users still needed
to allocate attention to stargazing and monitoring the robot’s
movements, increasing the complexity of the task and result-
ing in lower PASAT scores.
B. Grasp Score
In grasping tasks, we observed that as the level of automa-
tion increases, as shown in Fig14, users’ grasping scores also
show a significant improvement. This indicates that the level
of automation has a noteworthy impact on the enhancement
of task efficiency.
C. NASA-TLX
The results of NASA-TLX are shown in the Fig15 and are
next analysed according to the different dimensions. In terms
of mental demand, research indicates that there is no signifi-
cant difference between automation Level 1 and automation
Level 2 in their impact. However, automation Level 3 shows
a significant improvement compared to automation Level
1. This suggests that only a slight increase in automation
levels is not sufficient to significantly improve the mental
demand of the system, but higher levels of automation can
achieve this goal. Regarding temporal demand, as the level of
automation increases, users’ temporal demands on the system
seem to increase, indicating that the increase in automation
levels has not been effective in reducing temporal demands.
Fig. 15.
NASA-TLX result
Fig. 16.
Answers Average Results for Multi-Presence Questionaire
In particular, there is a significant difference between au-
tomation Level 1 and automation Level 3 in this regard. In
terms of Effort, as the level of automation increases, the
effort required from users gradually decreases, demonstrating
a significant effect of automation levels in reducing effort.
This aligns with the previously mentioned grip score results.
Finally, from the analysis of average scores, as the level
of automation increases, users’ overall evaluation of the
system improves, indicating a significant positive impact of
automation levels on system evaluation.
D. Questionnaire for Multi-presence
In the Fig16, it can be observed that the presence and
engagement of users are almost unaffected by changes in
automation levels. However, the sense of achievement is
influenced by the level of automation, with users experi-
encing a higher sense of achievement as automation levels
increase. Nevertheless, as automation levels further increase,
the improvement in the sense of achievement becomes less
pronounced. automation levels have a significant enhancing
effect on the performance of multi-instance systems. As
automation levels gradually rise, users become increasingly
satisfied with the overall system performance. Finally, higher
levels of automation can enhance users’ trust in the system,
as well as their tolerance for system failures. As automa-
tion levels increase, users become more tolerant of system
failures.
V. DISCUSSION
A. Complex Task with automation System
This research proposes three levels of automation tailored
to specific scenarios and tasks, with the potential for further
automation enhancements in complex settings. At automa-
tion Level Three, users can select items using simple head
movements, requiring them to maintain focus on the task.
3823
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:29:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

However, higher levels of automation, such as introduction
of embodied intelligence technology, enable users to con-
trol robotic arms with basic voice commands like ”fetch
me something.” The robotic arm can then autonomously
complete tasks and provide feedback, freeing users to con-
centrate on more critical tasks. This advanced automation
also facilitates simultaneous control of multiple robotic arms,
significantly improving efficiency and convenience.
But, real-world applications face challenges such as en-
vironmental complexity and task diversity. While current
research primarily addresses simple grasping tasks, robots
in reality must perform a broader range of tasks. There-
fore, there is a need to establish finer and more compre-
hensive standards for levels of automation, akin to those
in autonomous driving, to accommodate diverse tasks and
complex environments.
Additionally, leveraging recent advancements in multi-
modal large models like ChatGPT and Gemini shows
promise for enhancing robot control[22]. ChatGPT, for in-
stance, can interpret vague user commands, break down
complex tasks into simpler sub-tasks, and proactively seek
clarification to improve task success rates, thereby enhancing
robot system intelligence and user interaction experiences.
B. Additional Learning Costs Due to Different Input Modes
For different levels of automation, the input methods are
also an interesting issue. In this study, for automation levels 1
and 2, the input method involves controlling the robotic arm
using a game controller. Compared to other methods that
directly map user arm movements, this approach is more
user-friendly in terms of physical effort, as users do not
need to constantly lift their arms. In automation level 3,
since the only thing the user needs to do is make decisions
and communicate them to the robotic arm system, Head
Vector is used as one of the interaction methods. However,
while this method may seem intuitive, users still require
some time to learn this interaction mode. When users switch
from automation level 1 to level 2, almost no learning curve
is needed. In the experiments, most participants quickly
mastered the use of automation level 2 immediately after
ending their experience with automation level 1. However,
when transitioning to automation level 3, participants require
a significantly longer learning period. For automation level
3, there are various methods to achieve user input, such as
using voice commands.
C. Attention measurement error from continuous experi-
ments
In experimental design, the PASAT was selected as the test
tool to assess the attentional state of the subjects. Although
a minimum rest period of 5 minutes was provided between
each PASAT test in the experiment, the attentional state
of the subjects is a continuous process, and even with
sufficient rest, changes in their attentional state occurred
between two consecutive PASAT tests. These variations in
attentional state were more pronounced in some individuals
than others, with some showing a decrease or even no
Fig. 17.
PASAT Score with Exception
change in attentional state over time. Evidently, through the
course of the experiment, the mental state of the subjects
deteriorated. Nevertheless, most participants still managed to
achieve better scores, thereby demonstrating the effectiveness
of the automated technology proposed in this study. However,
a small group of participants did not see an improvement in
their scores with the increase in automation levels, as shown
in Fig17, the two red line show that there is subject do not
fit for the proposed experiment. Instead, their scores showed
a gradual decline. This suggests that the decreased difficulty
in attention allocation due to the automation was insufficient
to compensate for the decline in their mental state.
D. The Dilemma of Robotic Arms and Control Precision
In this study, the detachable body and detachable head
used in previous studies are retained and improved upon.
To ensure comfort when wearing it, Mycobot, which weighs
only 1.2 kg, was used for the arm part. The digital servo
motors used in the Mycobot and the connecting parts of the
arm are injection-molded plastic structures, and the inherent
strength limitations of plastic may limit the accuracy of the
MyCobot. The fact that the total weight remains within the
maximum load range of the robot arm, even with the heaviest
additions, suggests that the weight of the gripper may have
caused deformation of the internal structural components,
affecting accuracy. In fact, our experiments showed that de-
spite the manufacturer claim of 0.5 mm repetitive positioning
accuracy, the actual tested repetitive positioning accuracy
reached 1 cm. This low accuracy is detrimental to the design
of the experiment. The balance between weight and accuracy
is an important issue for detachable body-type robot arms.
In the wearable condition, due to the mobility of the user’s
body and visual aids, the accuracy requirement is not high
and weight is the most important factor. However, when
the robotic arm is detached and operates independently, it
becomes difficult to construct a closed-loop system, and at
this point, accuracy becomes more important than weight.
Thus, when designing a versatile robotic arm, balancing its
weight with its accuracy in different scenarios is a complex
challenge. The ideal solution would be to design dedicated
robotic arms that are lightweight and highly accurate for
these scenarios.
3824
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:29:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 8]**

VI. CONCLUSIONS AND RECOMMENDATION
A. Conclusion
This study introduces a novel Multi Presence System
featuring various levels of automation. Users can either fully
operate the system or merely provide decision-making input,
with robots handling the remaining tasks. At automation level
3, we integrated artificial intelligence for the first time to
estimate the pose of objects and detect targets. Additionally,
the concept of the Face Vector is applied to the Multi Pres-
ence System for the first time. Experiments were conducted
to investigate how different levels of automation affect user
experience and efficiency. The experimental results lead to
the following conclusions.
• automation technology significantly enhances the oper-
ational efficiency of the Multi Presence System. How-
ever, it does not always reduce the mental demands of
operating the system.
• Different levels of automation should be considered
in various scenarios. For situations requiring high ef-
ficiency and freedom, such as work environments, a
moderate level of automation is preferable for im-
proved operational efficiency. In contexts demanding
high mental engagement, like educational settings, a
high level of automation is desirable to reduce cognitive
load. Conversely, in complex scenarios, a low level of
automation aids in detailed user interactions.
• As the level of automation increases, there is a corre-
sponding rise in user tolerance for system errors.
Future research could delve into integrating more sophisti-
cated automation techniques like speech recognition, speech
synthesis, and semantic understanding. This would involve
developing algorithms that enable robots to interpret and
respond to human speech, making the system more intuitive
and user-friendly. Such advancements could significantly
enhance the automation level of the system, allowing for
more natural and efficient human-robot interactions.
REFERENCES
[1] Y. Iwasaki, K. Ando, S. Iizuka, M. Kitazaki, and H. Iwata, “Detachable
body: The impact of binocular disparity and vibrotactile feedback in
co-presence tasks,” IEEE Robotics and automation Letters, vol. 5, no.
2, pp. 3477–3484, 2020.
[2] Yukiko Iwasaki, Kozo Ando, Shuhei Iizuka, Michiteru Kitazaki,
Hiroyasu Iwata, “Detachable Body: The Impact of Binocular Disparity
and Vibrotactile Feedback in Co-Presence Tasks”, IEEE Robotics and
automation Letters, vol.5, no. 2, April 2020.
[3] J. I. Lipton, A. J. Fay, and D. Rus, “Baxter’s homunculus: Virtual
reality spaces for teleoperation in manufacturing,” IEEE robotics and
automation letters, vol. 3, no. 1, pp. 179–186, 2018.
[4] S. Tachi, Telexistence [electronic resource] / Susumu Tachi. Hacken-
sack, N.J: World Scientific, 2010.
[5] A. Alsereidi, “Multi-presence system with local augmented body-
investigation of human cognitive limitation in multi-robot operation
and spatial awareness-,” mastersthesis, Waseda University, Tokyo,
Japan, 2022.
[6] J. M. Beer, A. D. Fisk, and W. A. Rogers, “Toward a framework for
levels of robot autonomy in human-robot interaction,” J. Hum.-Robot
Interact., vol. 3, p. 74–99, jul 2014.
[7] M. Quigley, K. Conley, B. Gerkey, J. Faust, T. Foote, J. Leibs, R.
Wheeler, and A. Ng, “Ros: an open-source robot operating system,”
vol. 3, 01 2009.
[8] M. Bischoff, “ROS#,” June 2019.
[9] Itseez,
“Open
source
computer
vision
library.”
https://github.com/itseez/opencv, 2015.
[10] Itseez, The OpenCV Reference Manual, 2.4.9.0 ed., April 2014.
[11] Y. Sasaki, T. Kamegawa, and A. Gofuku, “Effect of display of yolo’s
object recognition results to hmd for an operator controlling a mobile
robot,” Artificial Life and Robotics, 2023.
[12] Y. Ge, Z. Li, X. Wang, X. Yue, and L. Meng, “Yolo-or: a lightweight
cross-stage object detection model for dish recycling robot,” in 2023
IEEE 3rd International Conference on Advanced Mechanical Systems
(ICAMechS), IEEE, 2023.
[13] N. Mukai, M. Suzuki, T. Takahashi, Y. Mae, Y. Arai, and S. Aoyagi,
“Application of object grasping using dual-arm autonomous mobile
robot path planning by spline curve and object recognition by yolo,”
Journal of Robotics and Mechatronics, 2023.
[14] B. Zhang, K. Xu, H. Cong, and M. Sun, “Channel and spatial
attention mechanism-based yolo network for target detection of the
lung ultrasound scanning robot,” in 2023 IEEE 13th International
Conference on Control Science and Systems Engineering (ICCSSE),
IEEE, 2023.
[15] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, “You only look
once: Unified, real-time object detection,” in 2016 IEEE Conference
on Computer Vision and Pattern Recognition (CVPR), pp. 779-788,
2016.
[16] G. Jocher, A. Chaurasia, and J. Qiu, “Ultralytics yolov8,” 2023
[17] J. Redmon and A. Farhadi, “Yolo9000: Better, faster, stronger,” in
2017 IEEE Conference on Computer Vision and Pattern Recognition
(CVPR), pp. 6517–6525, 2017.
[18] Y. Iwasaki and H. Iwata, “A face vector - the point instruction-type
interface for manipulation of an extended body in dual-task situations,”
in 2018 IEEE International Conference on Cyborg and Bionic Systems,
CBS 2018, Jan. 2019, pp. 662–666, doi: 10.110.
[19] D. Coleman, I. Sucan, S. Chitta, and N. Correll, “Reducing the barrier
to entry of complex robotic software: a moveit! case study,” 04 2014.
[20] T. Tanosoto, K. H. Bendixen, T. Arima, J. Hansen, A. J. Terkelsen,
and P. Svensson, “Effects of the paced auditory serial addition task
(pasat) with different rates on autonomic nervous system responses
and self-reported levels of stress,” Journal of oral rehabilitation, vol.
42, no. 5, pp. 378–385, 2015.
[21] E. A. Bustamante and R. D. Spain, “Measurement invariance of the
nasa tlx,” Proceedings of the Human Factors and Ergonomics Society
Annual Meeting, vol. 52, no. 19, pp. 1522–1526, 2008.
[22] D. Hassabis, “Gemini: The most capable and general model we’ve
ever built,” 2024.
3825
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:29:03 UTC from IEEE Xplore.  Restrictions apply. 
