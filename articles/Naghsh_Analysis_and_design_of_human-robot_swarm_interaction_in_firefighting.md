# Naghsh Analysis and design of human-robot swarm interaction in firefighting

*Source file: Naghsh_Analysis_and_design_of_human-robot_swarm_interaction_in_firefighting.pdf — 6 pages*


---
**[Page 1]**

Analysis and Design of Human-Robot Swarm Interaction in Fireﬁghting
Amir M. Naghsh
Shefﬁeld-Hallam
University,
Shefﬁeld, UK
a.naghsh@shu.ac.uk
Jeremi Gancet
Space Applications Services,
Zaventem, Belgium
jg@spaceapplications.com
Andry Tanoto
Heinz Nixdorf Institute,
University of Paderborn,
Paderborn, Germany
tanoto@hni.upb.de
Chris Roast
Shefﬁeld-Hallam
University,
Shefﬁeld, UK
c.r.roast@shu.ac.uk
Abstract— In a variety of emergency settings robot assistance
has been identiﬁed as highly valuable, providing remote, and
thus safe, access and operation. There are many different forms
of human-robot interactions, allowing a team of humans and
robots to take advantage of skills of each team member. A
relatively new area of research considers interactions between
human and a team of robots performing as a swarm.
This work is concerned with the interactive use of au-
tonomous robots in ﬁre emergency settings. In particular, we
consider a swarm of robots that are capable of supporting
and enhancing ﬁre ﬁghting operations co-operatively and we
investigate how ﬁreﬁghters in the ﬁeld work with such a swarm.
This paper outlines some of the key characteristics of this
emergency setting. It discusses possible forms of interactions
with swarm robotics being examined in the GUARDIANS
project. The paper addresses the use of assistive swarm robotics
to support ﬁreﬁghters with navigation and search operations.
It reports on existing ﬁreﬁghters operations and how human-
swarm interactions are to be used during such operations. The
design approaches for human-swarm interaction are described
and the preliminary work in the area are outlined. The paper
ends by linking current expertise with common features of
emergency related interaction design.
I. INTRODUCTION
GUARDIANS (Group of Unmaned Assistant Robots De-
ployed In Aggressive Navigation by Scent) is an European
project developing and applying the concept of autonomous
robots in urban search and rescue operations. Speciﬁcally the
project is focused upon assisting humans involved in search-
and-rescue emergencies and also employing robot mounted
sensors to provide a heightened level of feedback in such
settings. In addition, by employing a group of robots the
potential to co-operatively compute environmental maps will
be employed to further assist in search and rescue operations.
The speciﬁc search and rescue activity focused upon is that
of ﬁre-ﬁghting in a large warehouse. Project partner SyFire1
was able to provide expert advice regarding the nature of
such emergency situations.
The Swarm robotics is built upon the pioneering work
by Reynolds [12], who simulated a ﬂock of birds in ﬂight.
Sahin [13] describes the swarm robotics as a (i) a large
number, of (ii) homogeneous, (iii) autonomous, (iv) relatively
incapable or inefﬁcient robots with (v) local sensing and
communication capabilities. The GUARDIANS robot swarms
consist of a number of robots with differing communication
and sensing capabilities. The swarm is intended to support
1South Yorkshire Fire and Rescue Service
the real-life tasks of navigation and search operations in a
smoke ﬁlled industrial warehouse.
The interest here is that although the robots in a swarm are
primarily autonomous, they are designed and conﬁgurated to
address an overarching requirement of assisting humans in
search and rescue. Two types of robot operation to support
the human ﬁreﬁghters are distinguished:
• First employing the robot swarm as a means of gaining
essential information about an incident prior to engaging
with it.
• Second employing the swarm as an aid to ﬁreﬁghters
once they engage with the ﬁre incidient.
This paper focuses on the second of these, where human
ﬁreﬁghters are engaged with the incident and the main task
for the robot swarm is to provide support in navigation and
safeguard the humans.
From the point of view of human interaction there are two
types of users to be considered:
• Users
working
in
the
context
of
a
con-
trol/communication
centre,
remotely
overseeing
and managing operations in real-time. These base
station users are able to monitor and control the overall
activities of both the swarm of robots and humans on
the ﬁeld, and to provide decision making support to
the operations commanders.
• Users working directly in the environment, engaged
in speciﬁc exploration and rescue tasks in the ﬁeld.
The ﬁre ﬁghters are fully equipped with ﬁre ﬁghting
apparatus and clothing, and are performing speciﬁc
search and rescue tasks.
Recent research have highlighted some of the challenges
of Human Robot Interaction for search and rescue envi-
ronments. Driewer et al. [4] conducted a user requirement
analysis using questionnaires and personal interviews with
search and rescue professions such as military, plant ﬁre
brigades and ﬁre ﬁghters. Other research also highlighted
requirements by studying interaction among human teams in
bomb squad and ﬁre ﬁghters [1] and SWAT teams in training
[6].
The aim of this paper is to present our grounding in
designing the human-robot swarm interface for supporting
ﬁreﬁghting operation. This is supported by initial domain
research to ensure that the robots and related infrastructures
properly comply with and support existing human practice
Proceedings of the 17th IEEE International Symposium on Robot and Human Interactive Communication, Technische Universität München, Munich,
Germany, August 1-3, 2008
978-1-4244-2213-5/08/$25.00 ©2008 IEEE
255
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:13:43 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 2]**

and rules. The safety of the human ﬁreﬁghters is the highest
priority in such operations.
The work reported here is based upon the assumption that
the swarm robots are capable of extracting required infor-
mation from the environment, and, subsequently, localizing
and navigating themselves in the environment, tracking the
ﬁreﬁghters, as well as safeguarding them. The swarm used in
Guardians’ experimentations is composed of a number (about
20) of Khepera III robots2 equipped with IR, ultrasonic
sensors and chemical sensors, 3 ERRATIC robots3 equipped
as the Kheperas with laser rangeﬁnders and cameras in
addition, and 1 RESCUER robot4 equipped with a number
of sensors including, laser range ﬁnder, DGPS, inclinome-
ter, gyroscope/magnetic, vision and olfactory. Moreover, all
robots will be equipped with a multimodal wireless commu-
nication chip (inc. ZigBee, Bluetooth and WiFi). For more
details about the robotic system, the swarming algorithm,
and the communication network infrastructure see [11] for
example.
Our proposed human-robot swarm interface will be shortly
presented in Section V. In addition to this, the design
approach has to take account of technical constraints. One
signiﬁcant constraint is that the typical operating environ-
ment of a ﬁre incident is one in which robot performance
and reliable communication cannot be guaranteed.
II. FIREFIGHTING CONTEXT, SETTING AND OPERATIONS
A. Emergency Setting
The emergency setting environment for the project is a
large single story industrial warehouse. Such warehouses
usually consist of large open spaces with a variety of differ-
ing goods and materials stored throughout. Such warehouses
can be as large as (400×200)m2, and are often divided into
sections separated by ﬁre resistant walls. However, during
a ﬁre incident, smoke and fumes may cover entire sections
in the warehouse. As a consequence visibility becomes an
issue for ﬁremen. This is a common concern for ﬁre ﬁghters,
their normal training includes working fully blind-folded.
A signiﬁcant risk in such incidents is that ﬁre ﬁghters
can become easily lost. There have been notorious tragic
examples where ﬁreﬁghters died after becoming lost in the
ﬁre smoke. In the warehouse ﬁre of 1991 in Gillender Street
London (UK), two ﬁreﬁghters died this way, and in the 1999
warehouse ﬁre in Worcester (USA), six ﬁreﬁghters lost their
lives in similar conditions.
Thus, the warehouse ﬁre setting is one where poor visi-
bility means the search and rescue is both time consuming
and high risk. Moreover, a warehouse in ﬁre may contain
high quantities of toxic gases or inﬂammable materials.
Adding to the complexity and risk of such an incident is
that key information about the ﬁre may be limited: ambient
conditions, warehouse layout, the potential for ﬂashovers (i.e.
2K-Team: http://www.k-team.com
3Videre Design: http://www.videredesign.com
4Robotnik:
http://www.robotnik.es/automation/productos/agvs/robotnik-
p01-e.html
a simultaneous ignition of all the combustible material in the
area) are often unknown and likely to change.
B. Fireﬁghters Operations
To help the develop user requirements and effectively
understand the conditions that ﬁreﬁghters are subjected to,
the industrial and academic partners of GUARDIANS have
attended one full day training at the SyFire training centre.
Following this, to develop a more speciﬁc understanding of
ﬁreﬁghter activity and priorities there is an on going series
of meetings and trials with SyFire. Successful system design
and development often beneﬁts from direct user involve-
ment from the early stages of design. For the GUARDIANS
project a participatory design [3] approach to support user
involvement is highly important, partly due to the ﬁre ﬁghters
lack of familiarity with robot swarm capabilities. To sup-
port both requirement gathering and end user involvement
GUARDIANS has involved South Yorkshire Fire and Rescue
Service (SyFire) as a project partner.
This section reports on ﬁndings about ﬁreﬁghters opera-
tions and practice to date.
There is usually little information provided when the ﬁre
brigade is alerted to an incident. The ﬁrst task of the arriving
appliances is to assess the incident and the primary risks. The
ﬁreﬁghters safety is considered as a high priority at all times.
Fireﬁghters are initially grouped into teams and briefed
with their speciﬁc tasks and roles. Where possible a map of
the premises is used, however this will only show structures
such as walls and doorways. Other details such as interior
materials will not be known.
The span of control for any ofﬁcer is arranged to be
between three and ﬁve lines of communication, in order to
avoid an overload (and consequently neglect of) information
as shown in Figure 1. In large incident involving industrial
warehouses, the incident commander (IC) deals with the
overall supervision of the incident, where the Operations
Commander (OpsComm) deals with the sector commanders
and crews who are directly involved. In addition, an Entry
Control Ofﬁcer (ECO) for each entry point is appointed with
the following duties: (i) to update the Entry Control Board
with the information of the ﬁreﬁghters who have committed
into the scene of incident or have left it; (ii) to check the
breathing apparatus’s ‘Time of Whistle’ for committed crews
into the incident5; (iii) to liaison with other ECOs; (v) to
liaison with the sector commander.
Fireﬁghters are usually committed into the incident in
teams of two. They are normally protectively clothed and
wearing breathing apparatus. In the United Kingdom pro-
cedures are to deploy a guideline along a wall (see ﬁgure
2). The guideline is a special line which is used to indicate
a route between the Entry Control Point and the scene
of operations. Subsequent teams are able to follow the
guideline. Once within a ﬁre incident ﬁreﬁghters progress
is slow due to unknown obstracles, such as debris, and very
poor visbility.
5The cylinders contain roughly 20 minutes of air supply.
256
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:13:43 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 3]**
*(This page contains a figure/chart/image not captured in text)*

Guardians Base Station
ON Site
ON Sector
HMI
HMI
HMI
data 
links
data 
links
OFF Site
Guardians Appliance
On-the-field
HRI
HMI
CO
IC
OpsComm
Sector Commander
Other Appliances
Other Off-site Actors
Sectors of Operation Support
Safety Officer
ECO(s)
Base Station 
Infrastructure
Robots
Coordinator
Sensor
Specialist
Operators
Human Crew 
Members
Fig. 1.
Guardians appliance w.r.t. SyFyre ﬁre brigade organization. CO
stands for Communication Ofﬁcer, IC stands for Incident Commander,
OpsComm stands for Operations Commander and ECO stands for Exit
Control Ofﬁcer.
Fig. 2.
Guardians partners experiencing “guideline” feeling with a leather
glove (left). Guidelines have pairs of knot points all along the line, one in the
pair having a single knot, and the other one having twice, to disambiguate
direction following (right)
One of the ﬁreﬁghters, usually the squad leader, moves
forward while feeling for obstacles/survivors and testing the
integrity of the ﬂoor. The other ﬁreﬁghter holds on to the
leader and maintain the communication with the squad leader
(verbally) and ECO through the radio channel. On the way
out, the squad team debrief the ECO who reports back to
the sector commander. Further the sector commander feeds
back the collected information to the operations commander.
III. INTERFACES DESIGN CHALLENGES
There are several challenges faced in designing human-
robot swarm interface: noisy and hazardous environment,
high workload, communication issues (between human and
robot swarm, between human at the base station and the
robot swarm, and between human at the incident area and
the base station), situational awareness and eventually testing
and validation.
A. Environment and communications
In intervention-oriented missions, such as those of a rescue
teams and armed SWAT-teams (Special Weapons and Tac-
tics), a considerable amount of communication is devoted
to clarifying positional information termed “re-calibration”
such as conﬁrming the position of speciﬁc agents [6]. The
same can observed of ﬁreﬁghters working in an incident,
reliable common locations and means of orienting are highly
important.
The human ﬁreﬁghters cooperating with a swarm are sub-
ject to conditions such as poor visibility, noisy environment
and a thick clothing gear, which restrict their senses, and
thus their communication abilities. Therefore human robot
swarm interfaces cannot fully rely on the (commonly used)
audio and visual communication means.
Moreover, the wireless communication channels may be
disturbed because of the presence of metalic structures inside
the incident area. It is expected that the radio communication
link will be lost intermittently due to this factor.
B. Stress and workload
Besides the disturbance from the environment, ﬁreﬁghters
are further imposed a high level of stress from the inherent
risks. In the scenario tackled by this project, the operation
time is limited and the environment is hazardous. The need to
work with, and interact with, robots may result in additional
workload if the interactions and interfaces are not carefully
designed. Thus ’alternative’ interaction means are being
investigated.
C. Situational awareness
Another challenge in the design and development process
is to provide situational awareness to ﬁreﬁghters in the
incident area as well as users at the base station. In search and
rescue missions, ﬁreﬁghters face hazardous environments
and are expected to make decision within a short time
window. As a consequence, it is imperative that acquired
information and data allow ﬁreﬁghters and human operators
at the base station to comprehend in real time the on-going
situation, and accordingly to best perform decision making
(Level three of situational awareness, according to Endsley:
[5]).
D. Robots’ and humans’ roles assumptions
In designing interfaces, it is important to take into consid-
eration the roles assigned to humans and robots. For humans,
different roles have different expectations or models of the
robots. If these differ from reality, this will lead to frustration,
additional stress, and possibly serious or critical mistakes.
E. Testing and validation
As far as human-robot swarm interaction is concerned,
testing and validation require the robot swarm to be actually
operational. Although simulation may be helpful, operational
robot swarms will be required to assess the adequacy and
efﬁciency of the interfaces developed. Accordingly test and
validation plans are being prepared, so that the interfaces can
be actually tested and assessed within the upcoming setup of
GUARDIANS’ consortium’s joint experiments.
IV. HUMAN-ROBOT SWARM INTERFACE DESIGN &
DEVELOPMENT PROCESS
Enabling users to envisage or make sense of design
proposals is an essential element of good design practice.
Users can only make informed choices when the proposals
257
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:13:43 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 4]**

being discussed are meaningful to them. Prototyping is one
popular method of helping users (and designers) in this
process, and this beneﬁts from employing tools and methods
which allow designers to rapidly prototype. In the case of
this project it is important that the user interface concepts
are physically prototyped so that they can be realistically
assessed by ﬁreﬁghters.
Several techniques being considered to allow designers to
rapidly prototype novel physical interfaces for human robot
interactions that can be evaluated with the potential human
swarm members. These include the use of Phidgets toolkit6,
Electronic Paper Prototyping [10] and mock-ups. Following
sections report on some of the ﬁndings of our analysis.
A. Fireﬁghters
Scholtz presents ﬁve roles that human may take during
interaction with robots: supervisor, operator, mechanic, peer,
and bystander [14]. Due to high workload during opera-
tion, project partner SyFire preferred maintaining a minimal
approach to interaction. This has result in the interactions
designed to be high level to ensure convenient interaction.
To comply with this, we expect two roles the ﬁreﬁghters will
have during operation: team mates or bystander. As team
mates, ﬁreﬁghters work co-operatively with the robot swarm
in achieving the goal, e.g. explore the incident area, search
for victims, detecting potentially-hazardous materials, etc. As
bystander, ﬁreﬁghters have no direct control over the robot
swarm, hence the base station directly controls the swarm
for some particular task.
B. Base Station Users
The GUARDIANS base station shall provide classical robot
station features such as mission authoring tools, mission
execution monitoring and control means, interface to robots
and human crew members, and mission data recording. The
originality of the approach is the ability to support multiple
parallel client connections to a main base station server,
featuring tailored (and tunable) M&C means according to
user roles:
1) Base station coordinator: responsible for preparing and
validating mission plans, coordinating the activities of
operators, robots, human crew members and sensor
data specialists, taking decisions in the scope of the
GUARDIANS appliance activities and is an interface
from and toward the commanding chain above the
GUARDIANS appliance.
2) Operators: they remotely monitor and control robots
and human crew members activities on the ﬁeld,
support the analysis of the operational situation and
balance the autonomy level of robots (and crew mem-
bers) according to the available information (situational
awareness). They have the means and clearance to
teleoperate robots, groups of robots and humans crew
members.
6http://www.phidgets.com/
3) Sensor data specialists: they observe and analyse sen-
sor data and accordingly provide advices and reports
to the appliance coordinator.
4) Stakeholder
in
the
commanding
chain:
they
re-
motely observe operations, requesting only from the
GUARDIANS appliance the most meaningful informa-
tion for decision making (reports, snapshots, etc.).
They take general purpose decisions regarding the
GUARDIANS appliance activities, that the base station
coordinator shall apply accordingly.
C. Robot Swarm
As described above, ﬁreﬁghters circumstances in an inci-
dent are far from the perfect. Smoke, noise and protective
clothing impair their senses. Through consultation and inter-
views the following activities have been proposed as ways
in a robot swarm may assist ﬁreﬁghters.
1) Notifying the ﬁreﬁghters of possible hazards (e.g.
obstacles, high temperature, chemicals);
2) Indicating unambiguously the direction to the scene of
incident or backwards to the exit point;
3) Grouping - it is important for ﬁreﬁghters that the
swarm stays within a relatively close range to them but
also maintains its distance to the ﬁreﬁghters to allow
them freedom of action.
V. THE PROPOSED INTERFACES FOR HUMAN ROBOT
INTERACTION IN GUARDIANS
This section presents the potential interfaces for human
robot interaction that are under consideration in consultation
with the ﬁreﬁghters.
A. Direct Human-Swarm Interaction
1) Passive: The swarm has to adapt its actions to the
ﬁreﬁghter’s movement in form of a passive human to swarm
interaction. GUARDIANS’ robots are provided with sensors
that are not affected by poor visibility and can be used
to monitor ﬁreﬁghter’s movements. If there is a need to
help robot distinguish the ﬁreﬁghters from surrounding
obstacles, ﬁreﬁghter’s gear could be electronically marked
with technologies such as radio-frequency identiﬁcation
(RFID) tags.
2) Tangible: When the swarm is committed into the ﬁeld
to accompany and safeguard the ﬁreﬁghters, it is assigned
with a high-level task. Swarm algorithms are built based on
the autonomous operations of the robots, however ﬁre ﬁght-
ers may contribute to tactical instructions. Human control in
swarm robotics allows for dynamic authoritative control of
speciﬁc swarm activities based upon local circumstances and
human expertise.
In order to enable ﬁreﬁghters to interact with the swarm,
a tangible interface will be considered. This will have
to take account of the limited ergonomic freedom of the
ﬁreﬁghter when fully equipped with protective clothing.
Work in this area may have to focus identifying the key
tasks that tangible interaction should enable.
258
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:13:43 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 5]**
*(This page contains a figure/chart/image not captured in text)*

3) Movement-Based: Another potentially viable form of
interaction is to enable ﬁreﬁghters movements to serve as in-
structional purposes for the robot swarm. In order to maintain
the control and co-operation between humans and robots, a
movement language could allow for richer communication
supporting a large number of tasks. For instance, a form of
interaction could be recognising simple gestures from the
feedback provided by haptic devices on ﬁreﬁghter’s hands
and/or arms.
B. Direct Swarm-Human Interactions
1) Tactile: The safety of ﬁreﬁghters is a top priority, and
the most noticeable form of interaction that can be used to
notify ﬁreﬁghters of possible hazards is through sense of
touch. A tactile interface consisting of eight tactors will be
attached to the ﬁreﬁghters torso. The interface displays a
“tactile picture” of possible hazards locations surrounding
ﬁreﬁghters. Both parameters of the frequency and amplitude
will be used to communicate the seriousness of hazards.
2) Visual: To lead the ﬁreﬁghters to a point of interest, the
swarm has to forward navigational information to the ﬁre-
ﬁghters. The swarm communicates unambiguous directions
through a novel visual device (Figure 3) to be installed within
the ﬁreﬁghters’ helmet. The visual device display the direc-
tions in a simple form which requires minimum attention
from ﬁreﬁghters in order to understand them. The direction
conveyed to the ﬁreﬁghter is determined from collective
feedback from the robot swarm and the environmental factors
that determine their progress to a speciﬁc goal. Currently the
predominant swarm direction is being examined as the basis
for determining the direction indicated to the ﬁre ﬁghter.
To date, the second of these options has been trialed with
SyFire. This has examining speciﬁc visual conﬁgurations
and identifying the most effect means of communicating
directions. The manner in which such information is acted
upon in the high stress low visibility setting of a ﬁre incident
is of particular interest. Perliminary results seem to indicate
that users of the device value clear ordinal indications of
direction over continuous indicators.
C. Remote Interaction Via Base station
As a GUARDIANS appliance is deployed on the ﬁeld,
robots and human crew members interact to explore the en-
vironment, assess the situation, localize victims, performing
their tasks in extremely harsh conditions. In such conditions
a base station is critical to the safety of the crew members
and the efﬁciency of human crew members and robots tasks
execution. According to potential end users (and especially
ﬁremen), the base station shall primarily feature:
• Timely remote support to human crew members and
robots: providing clear instructions at the right moment
likely to be critical to effective communication. Even the
simplest instructions may result in unexpected outcomes
if the human ﬁre crew is overloaded.
• Realtime overall situational awareness: a signiﬁcant
effort in the design of the base station is devoted to
Fig. 3.
Early stage of visual LED-based interface prototyping for robot to
human communication
enabling simple, efﬁcient situational awareness both
for GUARDIANS system operators and at the different
levels of the command chain (appliance coordinator,
operations commander, etc.). This is of high importance
as failures or accidents in critical systems are often due
to lack of situational awareness7.
The main modules of the base station are illustrated on
Figure 4. The services manager provides users with adequate
remote HRI means (display and other interaction means)
according to their clearance level. It gets telemetry data
(robot attitude, human crew members health monitoring,
etc.), audio-visual data and processed sensor data from the
mission data recorder that, in addition to recording and
replaying mission data on request, is also a data centralizer
and dispatcher for all the system entities.
The mission editor offers authoring tools to design mis-
sion templates that, once applied in the operational context
through the MPSEM, give rise to mission tasks both for
human crew members and robots in the ﬁeld. The MPSEM
allows different schemes of mission monitoring and control
over the human crew and the robots, ranging from teleoper-
ation (step by step action) to policy level control (high level
request such as “explore and report any abnormal event”).
Operators may interfere at any time with plan execution and
can either use or disable the MPSEM autonomous execution
monitoring.
Two types of remote human interaction conﬁgurations are
considered from the base station:
1) Remote human - robot swarm interaction: The prin-
ciple of a robot swarm is to rely on auto-organization and
group behavior emergence to fulﬁll tasks, while beneﬁting
from redundancy. The base station is useful to monitor
the overall swarm activity, to send policy level requests,
and to take the control if necessary over a single or few
robots of the swarm, while others robots continue their
activities. Visualization of the swarm activity in the base
station is an essential issue: efﬁciently encompassing the
overall robots activities in a single view is a major aim
for the GUARDIANS’ base station. Besides, individual (or
small group) control means can be achieved with joysticks
7Historically this has sadly been the case in notorious tragedies such as
the Tchernobyl disaster in 1987, or aerial disasters such as the Tenerife one
in 1977
259
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:13:43 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

Mission 
Templates
Mission Editor
Robots & HCM Interface
Mission Planning, 
Scheduling & 
Execution Monitoring
(MPSEM)
Mission Data 
Recorder and 
Player
Services 
Manager
Sensor Data 
Processing 
Module
Users 
Profiles
TM/TC
AV Data
Sensors
Data
Expl. Data
Expl.
Data
TM/TC
Users 
Profiles Data
User
Data
Mission 
Edition Data
TM/TC
AV Data
Expl. Data
Mission 
Data
Edited Mission 
Templates
Selected 
Mission
Data flow 
TC
Guardians Base Station 
Fig. 4.
GUARDIANS base station architecture and data ﬂows. TM stands
for telemetry, TC stands for telecommand, and AV stands for audio-visual.
and other interacting devices such as touchscreens. Efﬁcient
multi-scale agent control may typically ﬁnd inspiration in
real-time strategy video game (i.e. Warcraft like).
During normal operations, robots operate autonomously.
However there are situations in which autonomy level
adjustment [2], [7]–[9] is deemed necessary. Humans may
take control over one or more robots to enforce a particular
way of performing tasks, if they think it is appropriate
in the current situation: typically if tasks are particularly
complex, delicate, or require knowledge that the robots are
not aware of. With adjustable autonomy, an entity needs not
make all decisions autonomously, rather it can choose to
reduce its own autonomy level and transfer decision making
control to other users or agents. Thus the system is more
ﬂexible, since it can handle tasks that might not have been
anticipated at the design process. Furthermore, the ability to
shift the level of autonomy is an elegant way of balancing
the load among all parties, whether it is human or robot.
2) Remote human - human crew members interaction:
One of the speciﬁcities of the GUARDIANS system is the
ability to take in charge both robots and human beings on
the ﬁelds, both in terms of monitoring and control. The main
beneﬁt is the possibility to coordinate robots and humans
activities on the ﬁelds together, in a comparable way. At ﬁrst
glance teleoperation of human beings is meaningless, but this
should be understood in terms of successive ﬁne grain actions
requests, as operators are likely to have a better overall
situational awareness than the ﬁreﬁghter in some situations:
indeed ﬁreﬁghters sometimes face conditions where visibility
is null and ambient noise makes it impossible to discuss
with other crew members. In such a situation, the base
station can send simple step by step elementary actions
requests through the designed user interface, for instance to
guide the ﬁreﬁghter toward the exit, or toward a victim that
the robot swarm localized. Moreover it shall be mentioned
that adjustable autonomy concepts introduced earlier also
make sense for the remote human - human crew members
interactions.
VI. CONCLUSIONS
The research on the human swarm interface has to tackle
several very new problems. The combination of robot swarm
and the base station in GUARDIANS is to help the human to
navigate where the human senses are failing. Furthermore,
this project aims to develop novel interactions technology to
maintain control and coordination between the swarm and
the humans.
Next steps consist of providing a full conceptual design to
human - robot swarm interactions, and further the physical
and operational prototype will be evaluated in full scale
experiments with end users (i.e. ﬁreﬁghters).
VII. ACKNOWLEDGMENTS
GUARDIANS is a EU funded project (FP6 IST-045269).
We also would like to thank GUARDIANS’ partners for their
comments on earlier drafts of this paper.
REFERENCES
[1] J. Adams. Human-robot interaction design: Understanding user needs
and requirements. In Human Factors and Ergonomics Society 49th
Annual Meeting, volume 4, 2005.
[2] J. A. Adams, P. Rani, and N. Sarkar.
Mixed-initiative interaction
and robotic systems. In AAAI Workshop on Supervisory Control of
Learning and Adaptative Systems, 2004.
[3] CPSR. Participatory design, computer professionals for social respon-
sibility, http://cpsr.org/issues/pd/, 2008.
[4] F. Driewer, H. Baier, and K. Schilling. Robot/human rescue teams: A
user requirement analysis. Advanced Robotics, 19(8), 2005.
[5] M. R. Endsley.
Situation Awareness Analysis and Measurement,
chapter Theoretical Underpinnings of Situation Awareness: A Critical
Review. Lawrence Erlbaum Associates, Mahwah, NJ, 2000.
[6] H. Jones and P. Hinds. Extreme work teams: using swat teams as a
model for coordinating distributed robots. In Proceedings of the 2002
ACM conference on Computer supported cooperative work: CSCW
’02, pages 372–381. New Orleans, Louisiana, USA, 2002, Nov. 2002.
[7] D. Kortenkamp, R. P. Bonasso, D. Ryan, and D. Schreckenghost.
Traded control with autonomous robots as mixed initiative interaction.
In in proceedings of the AAAI Spring Symposium on Mixed Initiative
Interaction, 1997.
[8] D. Kortenkamp and D. Dorais. Tutorial: designing Human Centered
Autonomous Agents, 2000.
[9] R. R. Murphy, J. L. Casper, M. J. Micire, and J. Hyams.
Mixed-
initiative control of multiple heterogeneous robots for urban search
and rescue. In in proceedings of the IEEE Transactions on Robotics
and Automation, 2000.
[10] A. M. Naghsh and M. B. Ozcan.
Gabbeh - a tool for computer
supported collaboration in electronic paper prototyping. In D. A and
W. L., editors, HCI 2004: Design for Life, 2004.
[11] J. Penders, E. Cervera, U. Witkowski, L. Marques, J. Gancet, P. Bu-
reau, V. Gazi, and R. Guzman. Guardians: a swarm of autonomous
robots for emergencies. In Workshop of Robotics in Challenging and
Hazardous Environments in ICRA2007, 2007.
[12] C. W. Reynolds. Flocks, herds and schools: A distributed behavioral
model. In SIGGRAPH ’87: Proceedings of the 14th annual conference
on Computer graphics and interactive techniques, pages 25–34, New
York, NY, USA, 1987. ACM Press.
[13] E. Sahin and W. M. Spears. Swarm robotics, a state of the art survey.
3342, 2005.
[14] J. Scholtz. Theory and evaluation of human-robot interaction. In Proc.
HICSS 36, 2003., 2003.
260
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:13:43 UTC from IEEE Xplore.  Restrictions apply. 
