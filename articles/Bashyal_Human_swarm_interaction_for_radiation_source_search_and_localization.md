# Bashyal Human swarm interaction for radiation source search and localization

*Source file: Bashyal_Human_swarm_interaction_for_radiation_source_search_and_localization.pdf — 8 pages*


---
**[Page 1]**

2008 IEEE Swarm Intelligence Symposium 
St. Louis MO USA, September 21-23, 2008 
978-1-4244-2705-5/08/$25.00 ©2008 IEEE 
  
Abstract - This study1shows that appropriate human 
interaction can benefit a swarm of robots to achieve goals 
more efficiently. A set of desirable features for human 
swarm interaction is identified based on the principles of 
swarm robotics.  Human swarm interaction architecture 
is then proposed that has all of the desirable features. A 
swarm simulation environment is created that allows 
simulating a swarm behavior in an indoor environment. 
The swarm behavior and the results of user interaction 
are studied by considering radiation source search and 
localization application of the swarm. Particle swarm 
optimization algorithm is slightly modified to enable the 
swarm to autonomously explore the indoor environment 
for radiation source search and localization. The 
emergence of intelligence is observed that enables the 
swarm to locate the radiation source completely on its 
own. Proposed human swarm interaction is then 
integrated in a simulation environment and user 
evaluation experiments are conducted. Participants are 
introduced to the interaction tool and asked to deploy the 
swarm to complete the missions. The performance 
comparison of the user guided swarm to that of the 
autonomous swarm shows that the interaction interface 
is fairly easy to learn and that user guided swarm is more 
efficient in achieving the goals. The results clearly 
indicate that the proposed interaction helped the swarm 
achieve emergence. 
I. INTRODUCTION 
obots are no now finding applications beyond the three 
D (Dirty, Danger or Dull) environments they were 
traditionally confined to; they are now used for 
entertainment, education and elder-care among several other 
new applications. The wide acceptance of robots in society 
has accelerated robotics research and new ideas are 
emerging in robot deployment. Swarm robotics is one such 
 
Manuscript received May 16, 200. This research has been funded by two 
different NSF grants: i) SENSORS: Approximate Dynamic Programming 
for Dynamic Scheduling and Control in Sensor Networks, ECCS #0625737 
and ii) NSF CAREER: Scalable Learning and Adaptation with Intelligent 
Techniques and Neural Networks for Reconfiguration and Survivability of 
Complex Systems, ECCS # 0348221. 
Shishir Bashyal is a Research Assistant at the Real-Time Power and 
Intelligent Systems Laboratory, Missouri University of Science and 
Technology, Rolla, MO 65409 USA. (E-mail: sbashyal@ieee.org).  
Ganesh Kumar Venayagamoorthy is an Associate Professor of Electrical 
and Computer Engineering and Director of Real-Time Power and Intelligent 
Systems Laboratory at Missouri University of Science and Technology, 
Rolla, MO 65409 USA. (E-mail: gkumar@ieee.org, Ph: 573-341-6641, fax : 
573-341-4532). 
 
area that has started to gain momentum in the last decade 
[1]. 
While a number of research studies are reported each 
year, swarm robotics has not yet been able to go beyond 
laboratory research. One of the factors limiting the use of 
swarm robots in real-life environment is the lack of 
appropriate method for humans to interact with the swarm. 
Almost all studies in swarm robotics rely on autonomous 
operation of the robots. One reason for such reliance is the 
insect swarm metaphor that researchers often use in swarm 
robotics. It is uncommon for humans to collaborate, 
command or interact with insect swarms and hence the 
benefits of such an arrangement in swarm robotics have 
never been explored. Penders in [2] presents the idea of a 
human interacting with the swarm and raises some relevant 
questions about such interaction which the author calls 
assistive swarming. The author opines that the user input can 
prove to be useful in deploying the swarm and that the 
traditional swarm interaction techniques that use audio 
(chirping, beeping), visual (blinking, flashing) cues cease to 
be useful in adverse situations the swarm might to deployed 
in.   
In swarm robotics, the individual robots are simple and 
have very limited planning capabilities compared to that of 
human beings. As with several other autonomous systems, 
swarm robotics can benefit by making provisions for 
humans to observe the performance of the system and inject 
knowledge in to the system where necessary. While some of 
the research studies (e.g. [3], [4]) have developed effective 
methods for observing the swarm behavior, the provision for 
humans to guide the swarm behavior has been least 
explored. Such provision for humans to affect the swarm 
behavior enables swarm robotics to overcome the barriers 
often posed by the environment. This study proposes a 
method for human swarm interaction (HSI) that allows users 
to interact with the swarm without affecting their group-
intelligence. The benefit of the proposed interaction is 
evaluated by comparing the performance of the autonomous 
swarm with that of the user-guided swarm.  
II. HUMAN SWARM INTERACTION LITERATURE 
The study of existing literature reveals that not much work 
has been done in HSI. Some of the research in human robot 
interaction provides inspiration and ideas for human swarm 
interaction. 
Most 
of 
the 
works 
that 
discuss 
the 
implementation of human interaction in a swarm of robots 
still call the approach human robot interaction (HRI) [3], [5] 
and in fact, in many cases the approach is equally applicable 
Human Swarm Interaction for Radiation Source                    
Search and Localization 
Shishir Bashyal, Ganesh Kumar Venayagamoorthy 
R
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:18:09 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 2]**

 
 
 
to other multi-robot systems. Some of the research in multi-
robot HRI [6], [7] and HCI [8] provide useful insight for 
HSI. 
In [5], McLurkin et al. discuss how interaction with a 
large number of robots differs from single robot HRI and 
explore strategies to maintain, program and interact with 
swarm without having to handle them individually. While 
the project emphasizes on the simplicity aspect of swarm 
robotics by using LEDs and MIDI sounds for status 
revealing of individual robots, it fails to maintain the 
autonomy required in swarm robotics. The study uses 
methods to allow user to control individual robot or the 
entire swarm; both of which is against the notion of 
emergent intelligence. In [6] and [7], Bruemmer et al. 
discuss multi robot HRI and propose that rather than making 
the user exert global, centralized control from above, the 
interaction should allow emergence of swarm intelligence. 
They identify the difference between the perception of 
environment by a single sophisticated robot and the 
perception of an element in the swarm and argue that HRI 
for multi-robot system should be inspired from nature and 
should promote swarm intelligence. The research later 
deviates slightly from the notion of swarm intelligence: 
“Unlike in the insect world, the robotic system must interact 
with human operators. At a minimum, this interaction 
includes responding to operator directed tasking and status 
reports on task progress”. This contradicts their own 
statement that once a system stops exploring the 
environment on its own and starts to follow commands from 
above; it ceases to promote swarm intelligence. The tasking 
of the robots by the human user introduced later deviates 
away from the notion of swarm robotics. In [9], 
Dudenhoeffer et al. conduct modeling and simulation for 
exploring HRI requirements and suggest that with high level 
of automation where the operator serves mainly a 
monitoring role; situation awareness may be negatively 
impacted. Their study suggests that emphasis on monitoring 
alone ignoring collaboration roles in multi-robot interaction 
poses a significant problem to the overall swarm due to 
degradation of situational awareness. 
In [3] and [4], an augmented reality based interaction 
mechanism is developed for swarm robotics. The proposed 
approach makes monitoring of the swarm effective but the 
use of head-mount device makes the approach complicated 
and costly. The study also lacks the human-robot 
collaboration component that can improve the swarm 
performance. Casper et al. in [10] opine that the present day 
robotics technology is not able to operate autonomously and 
hence the HRI is a key component in success of the human-
robot team. In [11], though the issues raised are for HRI, 
valuable insight for HSI is provided. The authors argue that 
automation is a likely way to succeed in some critical areas 
of technology. They find that the present day robot tele-
operation is not suitable for team-centric HRI. They also 
point out the possibility that use of intelligent software may 
provide higher degree of autonomy in the robots and argue 
that peer-peer interaction is possibly beneficial for HRI. 
Murphy in [12] emphasizes the importance of HRI in 
rescue-robotics. Billings [8] provides valuable insights to 
man-machine interface with real-life examples that prove the 
importance of effective interface. The author states that 
automation that is strong, silent and hard to direct is not a 
team player. The author argues that computers (robots in this 
context) should act as intelligent assistants; it should monitor 
our actions, to shield against human errors. Palmer et al. in 
[13] present a novel approach to swarm intelligence 
research. They begin with the quote “Smart things Form 
Teams, Stupid things Swarm” and modify the question to 
“What can we learn about swarms by having smart things 
act dumb?” They make a swarm of people act dumb and ask 
them to perform set of tasks so as to come up with effective 
algorithms for swarm intelligence. The work provides an 
inspiration to think out-of-the-box for solving problems in 
swarm robotics. Holly et al. in [14] present a detailed study 
of HRI taxonomy that helps to understand different modes 
and levels of HRI and to extend the concepts to HSI. 
Kartoun et al. in [15] present an intelligent approach in 
which a robot collaborates with a human in learning a task. 
Though the study is not in the context of HSI, it gives some 
idea on possible approach for HSI. Finally in [16], Breazeal 
explores HRI from the perspective of designing sociable 
autonomous robots. The author presents the classification of 
systems on the basis of HRI: robot as tool, robot as cyborg 
extension, robot as avatar and robot as sociable partner. Each 
is distinguished from the others based on the mental model a 
human has of the robot when interacting with it. 
Literatures in human swarm interaction suggest that the 
systems that only offer monitoring roles to the user tend to 
be least useful as monitoring alone makes users less 
participative adversely affecting situational awareness. On 
the other hand, an interaction that gives a complete control 
to the user suffers from human errors and the user workload 
is very high. The ideal man-machine interaction is said to be 
the one that functions autonomously while providing users 
with a method to inject knowledge and guidance so as to 
improve the performance of the system. 
III. FEATURES OF HUMAN SWARM INTERACTION  
In HSI, complete control of the swarm affects the 
emergent behavior of the swarm and thus swarm interaction 
methods need to limit users control over the swarm. The 
users should be able to inject domain knowledge without 
needing to manipulate the entire swarm. The degree of 
autonomy desired in swarm robotics is 100% and thus the 
swarm should be capable to work even without user input. 
The user input should help the swarm get better results and 
within a short interval. 
Another aspect in which HSI differs from HRI is the 
scalability of the interaction. Swarm interaction mechanism 
needs to be capable of supporting thousands of robots. The 
large number of robots necessitates that the interaction be 
robust; the swarm should be able to perform even with out 
user input. With a large number of robots, it is not possible 
for human users to monitor the entire swarm and provide 
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:18:09 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 3]**
*(This page contains a figure/chart/image not captured in text)*

 
 
 
appropriate input. It is therefore necessary for HSI methods 
to adopt some kind of divide-and-rule strategy allowing 
users to focus on a sub-group of robots at a time while the 
rest of the swarm operates without user interaction. Multi-
robot systems often adopt a centralized command and 
control strategy whereas swarm robotics emphasizes on local 
sensing and communication. This difference suggests that 
the HSI methods be able to influence the swarm locally as 
opposed to global control in multi-robot interaction. 
Furthermore, individual robots in swarm robotics are far less 
sophisticated than those in multi-robotics. HSI architecture 
must therefore adhere to simplicity in design and the existing 
swarm robot resources should be utilized rather than 
requiring sophisticated equipments. The goal of multi-robot 
interaction is to provide methods to task and control the 
robots whereas in HSI the goal is to help the robots attain 
emergence in shorter period of time or to help them do so in 
cases previously not possible. 
Based on the characteristics of swarm robotics, the 
following set of desirable features has been identified for 
HSI: 
i. 
Should promote positive emergence of intelligence 
ii. Should facilitate local rather than global interaction 
iii. Should be scalable, supporting large swarm size 
iv. The swarm should be able to perform well even without 
human input; the external input shall be used to speed up 
the mission or to achieve emergence in cases otherwise 
not possible 
v. Should support multiple users to interact simultaneously  
vi. Should be able to present useful information to the user(s) 
for situational awareness 
vii. Should use methods that utilize existing simple swarm 
resources rather than requiring sophisticated equipments 
viii. Should allow user(s) to adopt divide-and-conquer strategy 
enabling them to interact with a sub-group of robots at a 
time 
ix. The interaction should provide easy interface for user(s) 
to provide tactical input and domain knowledge to the 
swarm 
x. The architecture should be generic such that it could be 
used in a variety of applications rather than being limited 
to specific applications   
The insect swarm metaphor is used to come up with 
architecture for the human swarm interaction: if user(s) were 
to provide strategic input to a group of ants searching for 
food, what could be the method to drive the ants to the food 
source without affecting their group intelligence. Ants are of 
course capable of finding food on their own; user input can 
help them find it sooner. 
 
IV. PROPOSED ARCHITECTURE 
This study proposes architecture for swarm interaction 
that has features suitable for swarm robotics. The 
architecture lets human users to represent themselves in the 
swarm using their avatars2 which means human user(s) can 
select a robot and take control of it. The rest of the robots 
perceive the avatar as just another element in the swarm and 
thus the avatar (and therefore the user) does not have 
authority over the swarm. Their control over the swarm is 
only as much as that of any other member in the swarm. This 
provision of peer-to-peer interaction ensures that the user 
cannot exert external global control over the swarm. Since 
the swarm algorithms use a set of protocols for robot-to-
robot interaction, the user input eventually is subjected to the 
protocol and thus the user input in helping the swarm to 
attain the goal is appreciated by the swarm to the extent 
allowed by the protocol. Usually it means that the users 
ability to guide the swarm is only as much as her/his ability 
to help the swarm obtain better results. 
The user(s) use a computer (preferably a handheld device) 
to observe the swarm distribution and their behavior. Each 
user establishes a communication link to the swarm via 
her/his avatar. The robots in the swarm route their messages 
to the user via the avatars that act as base stations. The user 
can select any one of the robot in the swarm as her/his avatar 
at a time. The avatar can then be fully controlled by using 
the remote computational device; it can be moved by the 
user as desired and its status can be changed as required. 
Figure 1 illustrates the proposed swarm interaction 
architecture. 
 
Figure 1: Proposed human swarm interaction architecture 
It is evident that the users control over the swarm is very 
limited. However, as each user has access to one robot in the 
swarm, they can control it so as to lead the swarm towards 
the goal. For example in a swarm deployed to localize odor 
source, if the user drives the avatar towards the area with 
higher likelihood using tactical skills, other robots would 
start following the avatar once the odor signal detected by 
 
2 The Sanskrit word avatāra- literally means "descent" and implies a 
deliberate descent (of god) into lower realms of existence (humans or 
animals) for special purposes. 
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:18:09 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

 
 
 
the avatar is stronger than that of others in the swarm. The 
swarm is able to follow the odor gradient in the environment 
to localize the odor source but before the robots reach the 
area with odor gradient, the swarm needs to randomly 
explore the environment. The human navigational skills are 
far more superior in this regard and hence the user input not 
only increases the chances of detecting the odor source but 
also reduces the mission execution time. 
The proposed architecture has all of the features identified 
in section III. The user does not have authority over the 
entire swarm and can influence only a part of the swarm at a 
time. The user observes a sub-group of the swarm at a time 
and controls the avatar so as to influence the swarm in a 
strategic manner. This approach makes user workload 
independent of the swarm size and thus scalability is 
achieved. When the swarm size is large, the user can still 
focus on a part of the swarm and act to help the swarm. 
Multiple users can select multiple avatars in such cases to 
increase the efficiency of the swarm. Furthermore, the 
architecture is standard in the sense that the architecture 
remains the same from one application to the other. The only 
difference would be in the protocol that the swarm uses to 
interact with each other and the environment. 
V. SIMULATION ENVIRONMENT AND HSI 
INTERFACE 
This study uses MATLAB based simulation 
environment for simulating the swarm behavior. A 
two-dimensional indoor environment is created and the 
swarm is placed in the environment. The experiments 
conducted in this study use 20 robots in the swarm for 
experimentation. Each robot in the swarm is capable of 
sensing the walls and turning around to avoid collision. 
Inter-robot collision is not taken care of in the 
simulation as it does not impact the observations in this 
study. The robots in the swarm are programmed with 
different modes that they can operate in. Initially the 
robots are in the normal mode in which they wander 
around in straight lines deflected only by walls and 
obstructions. The robots can operate in a repel mode in 
which the robot becomes stationary and signals the 
robots in the neighborhood to move away from the 
robot. There are also four different director modes, one 
each for four directions up, down, left and right, in 
which case the robot remains stationary and signals the 
neighboring robots to move towards one direction.  
When the simulation is launched, the robots are 
initialized in the normal mode. The user can use the 
mouse pointer to click on a robot to select it and then 
click on one of the buttons to switch it to a certain 
mode. The robot icon in the simulation environment 
changes its color and shape based on its present mode 
aiding the users understanding of the swarm behavior. 
Table I shows the different buttons and the associated 
modes the buttons switch the robot to. The table also 
presents the influence of the robot mode to its 
neighbors. Robots could be assigned several other 
modes based on the requirement for the particular 
application. In this study, repel, director, avatar and 
normal are the only modes used. 
TABLE I  
GUI BUTTONS AND THEIR FUNCTION 
Button 
Mode 
Assigned 
Effect on the Neighbor Icon 
 
Repel 
Vx = - Vx or Vy  =  - Vy
 
 
Up Director 
Vy =  -1 * abs(Vy) 
 
 
Down 
Director 
Vy = abs(Vy) 
 
 
Left Director 
Vx =  -1 * abs(Vx) 
 
 
Right Director Vx =  abs(Vx) 
  
 
Select Avatar / 
Release Mode
None 
 
 
A graphical user interface (GUI) is provided using which 
a user can select robots in the swarm as the avatar and use it 
in different roles. Figure 2 displays GUI and simulation 
environment with different robots assigned to different 
modes. White lines are the trails of different robots. 
 
Figure 2: Effect of Director and Repel robots on neighbors 
 
When the user selects a robot and clicks either the repel 
button or one of the director buttons, the user has selected 
the robot as the avatar and changed its mode to that 
corresponding to the button. Therefore the robot remains 
stationary and signals the neighbors as per the mode. Once 
user changes the mode of a robot, it remains to be so even 
after the user releases it as the avatar. This allows the user to 
select multiple robots one by one and change their mode 
over time and the robots once assigned remain in the mode 
until the user does not select it again and release it by using 
the Select Avatar / Release Mode button. Selecting a robot in 
the normal mode and clicking on the Select Avatar / Release 
Mode button makes the robot the user’s avatar without any 
impact on the neighbors. In any of the modes, the robot last 
selected by the user can be moved by using the number pad 
Repelled Robot 
Repel mode 
Left Director 
Up Director 
Right Director 
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:18:09 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 5]**

 
 
 
in the keyboard. The director robots direct neighbors in their 
respective direction whereas repel mode repels robots 
approaching from all directions.    
VI. RADIATION SOURCE LOCALIZATION 
In order to evaluate the effectiveness of the proposed 
interaction, the swarm of robots is used for radiation source 
search and localization. The goal for the swarm is to search 
an indoor environment to detect presence of radiation 
sources in the environment and if radiation is detected, the 
radiation source needs to be localized. The robots are 
programmed to move randomly through the environment 
until the radiation source is detected. Particle swarm 
optimization (PSO) algorithm is used in the robots that 
enable them to locate the source of radiation once at least 
one robot detects the radiation. 
PSO has been used in a number of studies in swarm 
robotics. Doctor et al. in [17] propose a PSO based 
collective robotic search application where a number of 
robots distributed over a search space collaborate to locate 
the target. The work uses a PSO to do the target search and 
another PSO to tune the parameters of the search PSO for 
better convergence. The tuned PSO leads to better 
convergence in single as well as multiple target searches. 
Marques et al. in [18] present a particle swarm based 
olfactory guided search where robots with odor sensors 
collaborate to localize the source of the odor. In absence of 
the odor signal, robots in the swarm repel each other 
achieving explorative behavior. Pugh et al. recently reported 
their work [19] in PSO based multi-robot search in which 
they modified standard PSO algorithm to better suit their 
problem. 
Particle swarm optimization proposed in [20] is an 
optimization tool inspired by the foraging behavior of a 
flock of birds. Particle swarm optimization algorithm, since 
its proposition in 1995, has been used in solving a wide 
variety of problems and has recently been used in multi-
robot search applications. 
In particle swarm optimization, a particle is an n-
dimensional vector that encodes the n-dimensional solution 
to the optimization problem. A swarm of such particles are 
randomly initialized in the problem space. Each particle has 
some memory that stores (i) the best position (called pbest) 
the particle has achieved so far, (ii) the present position of 
the particle in the problem space and (iii) the velocity with 
which the particle ‘flies’ in the problem space. In addition to 
that, the particles communicate with each other to share the 
best solution discovered by the entire swarm (called gbest). 
Based on this two information, pbest and gbest, the position 
and velocity of each particle is updated which eventually 
leads to the convergence of the swarm to the best solution in 
the search space. The standard particle swarm optimization 
algorithm is presented below: 
i. 
Initialize a population of particles with random 
positions and velocities in n dimensions of the problem 
space and fly them. 
ii. Evaluate the fitness of each particle in the swarm. In 
each iteration, compare each particle's present fitness 
with its pbest. If the current value is better than pbest, 
then set pbest equal to the current value and the pbest 
location equal to the current location in the n-
dimensional space. 
iii. Compare pbest of particles with each other and update 
the gbest 
iv. Change the velocity and position of the particle 
according to equations (1) and (2) respectively. 
)
(
)
(
2
2
1
1
1
P
gbest
rand
c
P
pbest
rand
c
V
w
V
k
k
k
k
k
−
+
−
+
=
+
 
V
P
P
k
k
k
+
=
+1
 
 
V and P represent the velocity and position of the 
particles with n dimensions respectively. rand1 and 
rand2 are two uniform random numbers between 0 and 
1, and w is the inertia weight (0 < w < 1). c1 and c2 are 
cognition and social constant respectively. 
v. Repeat steps (ii) to (v) until desired convergence is 
reached. 
 
When a number of robots with sensing, positioning and 
communication capability are put together and treated as the 
particles in the particle swarm optimization algorithm, the 
swarm is capable of locating the source of signal (radiation, 
odor, heat or light source that the sensors in the robot are 
capable of sensing) given that the robots are evenly 
distributed in the search space such that at least some of the 
robots sense the signal from the source. Studies [18], [19] 
and [20] use PSO based approach to localize the source that 
creates a gradient in the environment (e.g. light, odor, vapor 
etc) using a swarm of robots. The studies assume that the 
swarm is already dispersed in the environment. Usually, a 
swarm of robots are brought to the search space in a 
container and need to be deployed from there. The random 
initial distribution is in itself a problem in swarm robotics. 
PSO implementation in this study is slightly different 
from the standard PSO. Initially, when the robots are 
brought to the environment, none of the robots can detect the 
radiation as they are away from the region. The robots 
therefore start moving with randomly initialized velocity 
changing directions only when they come across walls and 
obstructions. This process of exploration continues unless 
the radiation strength detected by a robot is higher than that 
of others. The robot detecting the highest radiation shares its 
position to others in the neighborhood (as opposed to sharing 
it to the entire swarm in the standard PSO) and thus the 
algorithm is a localized version of PSO. The best position of 
the robot then becomes the local best (lbest) for its neighbors 
and the neighbors use equation (1) (replacing gbest with 
lbest) for velocity update. Position update equation remains 
the same as in equation (2). The local sharing of the 
behavior allows other elements in the swarm to continue 
exploring other areas in the environment therefore enabling 
the swarm to search and localize multiple radiation sources 
in the environment. Figure 3 shows flow-chart of the PSO 
implementation. 
(1) 
(2) 
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:18:09 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

 
 
 
In order to evaluate the proposed interaction architecture 
and 
the 
interaction 
interface, 
two 
user-evaluation 
experiments are conducted for radiation source search and 
localization. The first experiment is designed to familiarize 
the participants with the interaction tool and to observe their 
learning behavior during the process. The second experiment 
is meant to compare the performance of the user-guided 
swarm to that of the autonomous swarm. 
Mission 
Completed
Lbest(Robot Id) > 
fitness(Robot Id) ?
)
(
)
(
2
2
1
1
1
P
gbest
rand
c
P
pbest
rand
c
V
w
V
k
k
k
k
k
−
×
×
+
−
×
×
+
×
=
+
Robot Id = 1
= 0.9, c = 2.0, c = 2.0
0
=
V k
V
V
P
P
rand
k
k
k
+
+
=
+1
Sense the radiation level at new location
Update pbest and lbest
Robot Id = Robot Id + 1
No
All key-points 
covered?
Yes
Start
Yes
No
Robot Id < Population Size?
Yes
No
0
=
V rand
()
rand
V rand =
 Figure 3: PSO implementation flowchart 
A. A. User Familiarization Experiment 
The swarm application used in the experiment is to deploy 
the swarm to detect and localize the radiation source in the 
environment. To make things easy for the participants, the 
radiation is displayed in the map and therefore searching for 
the radiation is not necessary. The robots have the ability to 
navigate through the environment sensing the radiation 
signal. If at least one robot reaches the region where the 
radiation can be detected, it collaborates with other robots 
using PSO algorithm to navigate to the source. Participant’s 
goal is therefore to help robots reach the region with 
detectable radiation within a minimum time. Figure 3 shows 
the scenario with the higher radiation area appearing white. 
The radiation field is created using graphics editing tool and 
placed in the simulation environment. The goal of the swarm 
is to reach the centre of the white gradient. 
A brief introduction of the HSI research was provided to 
each participant at the beginning of the experiment. Some 
participants requested for a demonstration in addition to the 
instructions provided in the documentation which was 
provided to them. The participants are allowed to repeat the 
sample application up to 5 times and their mission 
completion time for each run is noted. 
The trend of the mission completion time reflects the 
learning curve of the interface. If the mission time decreases 
with repetitions, it reflects that the interface is easy to learn. 
If the users do not find it necessary to repeat up to the 
maximum allowed number of times, it reflects that the 
interface is very easy to learn and that users are confident of 
the interaction within a short period of time. Of the five 
participants that participated in the experiment, four 
participants repeated the sample application 5 times, the 
maximum allowed number of repetitions. One participant 
repeated it 4 times before moving on to the next experiment. 
This indicates that the interaction is fairly easy to get 
familiar with; had it been too easy, all participants would 
have repeated it less number of times. If it had been too 
difficult, the participant who did it only for four times would 
have continued it for the fifth time as well. 
 
Figure 3: Sample radiation source localization application 
scenario 
 
Almost all participants’ sample mission completion time 
decreased with the number of repetitions except for some 
fluctuations due to the random initialization of the swarm. 
Figure 4 presents the learning curve for all five participants. 
When the swarm operated without user input, the average 
and standard deviation of the mission completion time is 
found to be 69.64± 8.91 seconds. In the first try, the mission 
completion time of the participants was higher than the 
swarm performing on its own. The reason is that the users 
experimented with the different modes of the robots rather 
than focusing on the goal of the mission. In later runs, their 
performance improved and three users achieved mission 
completion time shorter than the average completion time of 
the autonomous swarm. Participants 2 and 5 demonstrated 
ideal 
learning 
behavior 
whereas 
other 
participant’s 
performance fluctuated. All but participant 3 performed 
better in repetitions than in the first attempt. Only participant 
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:18:09 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

 
 
 
4 did not achieve mission completion time as good as the 
average completion time for the autonomous swarm 
displayed in blue line in the figure. 
 
Figure 4: Comparison of completion time of participant 
guided swarm (bars) with that of the autonomous swarm 
(horizontal line) for sample mission 
B. B. User Evaluation Experiment 
After the users are familiar with the simulation 
environment and the interaction interface, the users are 
asked to deploy the swarm for searching an indoor 
environment to decide whether any sources of radiation are 
present in the environment. If there are any radiation 
sources, the swarm also needs to localize them. Radiation 
source, if present, would radiate over an entire region and 
thus it is not necessary that the entire space be scanned 
thoroughly. Furthermore, there is a gradient of the radiation 
signal around the source which the swarm can use to 
converge to the source using computational intelligence 
techniques. PSO is used in this study to enable the swarm to 
converge to the radiation source. The details of the algorithm 
are presented in the next section. 
In a practical radiation source search scenario, human user 
can plan the mission by identifying a set of key-points in the 
map that can be searched to decide whether a radiation 
source is present in the environment or not. By taking into 
account the area covered by radiation sources; the presence 
or absence of radiation sources can be determined just by 
searching a number of key-points. The user planning, absent 
in the autonomous swarm,  can therefore help in completing 
the mission earlier as searching only the key-points can be 
completed in a short time as compared to the through search 
of the entire search space. The mission completion time 
achieved by the participants is compared with that of the 
autonomous swarm to evaluate the benefit of proposed HSI. 
To evaluate the usefulness of the HSI for this application, 
participants are provided with a map of the environment. 
Seven key-points are previously marked in the map so as to 
standardize the experiment among different participants. The 
goal of each participant therefore reduces to sending at least 
one robot each to all seven of the key-points. If there is a 
radiation source in the environment, it would be detected by 
the time all seven key-points are explored. The robot that 
first detects the radiation source then collaborates with 
others in the neighborhood to localize the source of 
radiation. Figure 5 shows the map of the environment with 
the key-points marked with blue ‘x’ signs. 
 
Figure 5: Map of the environment with key-points marked 
with blue ‘x’ markers 
 
The simulation is run for 5 times (equal to the number of 
participants) without user input to obtain the mean and 
standard deviation of the mission completion time for the 
autonomous swarm which is found to be 637.02± 343.75 
whereas 
that 
for 
the 
human 
guided 
swarm 
is 
314.19± 155.40. This is a reduction in mission completion 
time by 50.68%. All participants completed the mission 
before the average time for the autonomous swarm. Four of 
the participants completed the mission in less than half of 
the mean time required by the autonomous swarm. This 
result shows that the human’s ability to develop strategies 
can be used to guide the swarm to the desired areas much 
faster therefore improving the efficiency of the swarm. In 
this experiment no radiation sources were placed in the 
environment and the mission is complete when the user 
drives at least one robot each to the seven areas identified by 
the markers. If there was a radiation source, at least one 
robot would detect the radiation signal and the PSO 
algorithm would come into effect and localize the swarm, 
just like in the previous mission. Figure 6 shows the 
completion time for the users and the average mission 
completion time for the autonomous swarm. 
As evident from the result, the user guided swarm is able 
to complete the mission much earlier by visiting all seven 
key-points within a short period of time. Users were able to 
convert their tactical knowledge to appropriate input for the 
swarm enabling the swarm to achieve the goal in a shorter 
period of time.  
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:18:09 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 8]**
*(This page contains a figure/chart/image not captured in text)*

 
 
 
 
Figure 6: Comparison of completion time of the participant 
guided swarm (bars) to that of the autonomous swarm 
VII. VI. CONCLUSION 
Methods and benefit of user guided swarm has been least 
explored in literatures. This study proposes swarm 
interaction architecture that has scalability, robustness and 
emergent features suitable for swarm robotics. User-
interaction interface is developed based on the proposed 
architecture and user evaluation experiments are conducted 
to evaluate the interaction interface. The results of the 
experiments show that the interface is fairly easy to use and 
that user guided swarms achieve goals much faster. Faster 
completion of the mission is critical in applications like 
radiation source search and localization and hence the 
proposed user interaction makes the swarm much more 
preferable. 
Energy consumption of robots is another major constraint 
that severely limits the mission lengths. Elements of the 
swarm are miniature in size and thus the battery life is very 
short due to small size of the batteries. As the result obtained 
in this experiment shows that the use of proposed user 
interaction helps the swarm search the area more efficiently, 
it is possible to search a larger area by deploying user-
guided swarm. The proposed interaction can therefore 
improve the performance of swarm deployment for search 
and localization tasks. 
REFERENCES 
[1]  Erol Sahin, William M. Spears. Preface in Swarm robotics:
SAB 2004 international workshop, Santa Monica, CA, USA,
July 17, 2004: revised selected papers 
[2] Jacques 
Penders, 
“Robot 
Swarming 
Applications.”
http://www.cs.unimaas.nl/jaap60/papers/B31_penders.pdf, 
visited 03/15/2008. 
[3] Daily, M.; Youngkwan Cho; Martin, K.; Payton, D.; World
embedded 
interfaces 
for 
human-robot 
interaction;
Proceedings of the 36th Annual Hawaii International
Conference on System Sciences, 2003. 
[4] David Payton, Regina Estkowski, Mike Howard, Pheromone
Robotics and the Logic of Virtual Pheromones. SAB 2004
International Workshop, Santa Monica, CA, USA, July 17,
2004, Revised Selected Papers 
[5] James McLurkin, Jennifer Smith, James Frankel, David
Sotkowitz, David Blau, Brian Schmidt. Speaking Swarmish:
Human-Robot Interface Design for Large Swarms of
Autonomous Mobile Robots, AAAI Spring Symposium,
March 28, 2006 
[6] D. J. Bruemmer, D. D. Dudenhoeffer, J. Marble. Mixed-
Initiative Remote Characterization Using a Distributed Team
of Small Robots, 2001 AAAI Mobile Robot Workshop,
Seattle, WA, July 2001 
[7] D. J. Bruemmer, D. D. Dudenhoeffer, M. O. Anderson, M.
D. McKay. A Robotic Swarm for Spill Finding and
Perimeter Formation, Spectrum 2002, Reno, NV, Aug. 2002.
[8] Charles E. Billings, Issues Concerning Human-Centered
Intelligent Systems: What's "human-centered" and what's the
problem? 
URL:
http://www.ifp.uiuc.edu/nsfhcs/talks/billings.html 
[9] D. D. Dudenhoeffer, and D. J. Bruemmer, and M. L. Davis.
Modeling And Simulation For Exploring Human-Robot
Team Interaction Requirements. 2001 Winter Simulation
Conference, Washington DC, Dec 2001 
[10] J. Casper and R. R. Murphy. Human-robot interaction during
the robot assisted urban search and rescue response at the
World Trade Center. IEEE Trans. Syst., Man, Cybern. B,
vol. 33, pp. 367--385, June 2003. 
[11] Burke, J., Murphy, R.R., Rogers, E., Scholtz, J., and
Lumelsky, V., “Final Report for the DARPA/NSF
Interdisciplinary Study on Human-Robot Interaction,” IEEE
Systems, Man and Cybernetics Part A, vol.34, No.2, May
2004, pp. 103-112. 
[12] R. Murphy, "Human-Robot Interaction in Rescue Robotics",
IEEE Trans. Systems, Man, and Cybernetics , vol. 34, no. 2,
2004, 138–153. 
[13] Daniel W. Palmer, Marc Kirschenbaum, Jon P. Murton,
Michael A. Kovacina, Daniel H. Steinberg, Sam N.
Calabrese, Kelly M. Zajac, Chad M. Hantak, and Jason E.
Schatz; Using a Collection of Humans as an Execution Test
bed for warm Algorithms; IEEE Swarm Intelligence
Symposium, April 24-26, 2003 
[14] Holly A. Yanco and Jill L. Drury. Taxonomy for Human-
Robot Interaction, In Proceedings of the AAAI Fall
Symposium on Human-Robot Interaction, AAAI Technical
Report FS-02-03, Falmouth, Massachusetts, November
2002, pp. 111-119. 
[15] Kartoun U., Stern H., Edan Y.; Human-Robot Collaborative
Learning System for Inspection. IEEE International
Conference on Systems, Man, and Cybernetics. Oct. 2006. 
[16] C. Breazeal . "Social Interactions in HRI: The Robot View,"
R. Murphy and E.  Rogers (eds.), in IEEE SMC
Transactions, Part C.2004 
[17] Doctor, S., Venayagamoorthy, G. K., Gudise, V. G., 2004.
“Optimal PSO for Collective Robotic Search Applications”,
IEEE Congress on Evolutionary Computation, June 19-23,
Portland, OR, pp. 1390-1395. 
[18] Marques, L., Nunes, U., & de Almeida, A. T., 2006.
“Particle 
swarm 
based 
olfactory 
guided 
search”,
Autonomous Robotics, Vol. 20, pp. 277- 287 
[19] J Pugh, A Martinoli. Inspiring and Modeling Multi-Robot
Search with Particle Swarm Optimization in Swarm
Intelligence Symposium, 2007. SIS 2007. IEEE, 2007 
[20] Kennedy, J.; Eberhart, R., "Particle swarm optimization,"
Neural Networks, 1995. Proceedings., IEEE International
Conference on, vol.4, no., pp.1942-1948 vol.4, Nov/Dec
1995. 
 
Mean for user- 
guided swarm
Mean for autonomous swarm 
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:18:09 UTC from IEEE Xplore.  Restrictions apply. 
