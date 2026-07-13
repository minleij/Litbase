# lewis-2013-human-interaction-with-multiple-remote-robots

*Source file: lewis-2013-human-interaction-with-multiple-remote-robots.pdf — 44 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

CHAPTER 4
131
XXX10.1177/1557234X13506688Reviews of Human Factors and Ergonomics, Volume 9Human Interaction
2013
Human Interaction With Multiple Remote Robots
Michael Lewis
In this chapter, I review research involving remote human supervision of multiple unmanned 
vehicles (UVs) using command complexity as an organizing construct. Multi-UV tasks 
range from foraging, requiring little coordination among UVs, to formation following, in 
which UVs must function as a cohesive unit. Command complexity, the degree to which 
operator effort increases with the number of supervised UVs, is used to categorize human 
interaction with multiple UVs. For systems in which each UV requires the same form of 
attention (O(n)), effort increases linearly with the number of UVs. For systems in which the 
control of one UV is dependent upon another (O(>n)), additional UVs impose greater than 
linear increases due to the expense of coordination. For other systems, an operator interacts 
with an autonomously coordinating group, and effort is unaffected by group size (O(1)). 
Studies of human/multi-UV interaction can be roughly grouped into O(n) supervision, 
involving one-to-one control of individual UVs, or O(1) commanding, in which higher-
level commands are directed to a group. Research in O(n) command has centered on round-
robin control, neglect tolerance, and attention switching. Approaches to O(1) command are 
divided into systems using autonomous path planning only, plan libraries, human-steered 
planners, and swarms. Each type of system has its advantages. Less complete work in scalable 
displays for multiple UVs is reviewed. Mixing levels of command is probably necessary to 
supervise multiple UVs performing realistic tasks. Research in O(n) control is mature and 
can provide quantitative and qualitative guidance for design. Interaction with planners and 
swarms is less mature but more critical to developing effective multi-UV systems capable of 
performing complex tasks.
Introduction
In recent decades, the number of mobile unmanned vehicles (UVs) deployed in field 
applications has risen dramatically. Their usage offers obvious advantages of reduced 
costs, removing humans from harm’s way, or enabling entirely new applications that were 
previously impossible, especially when combining many such UVs into a comprehensive 
system. The domains of potential application are equally diverse and range from low-cost 
warehouse security to interplanetary exploration. New developments in commodity hard-
ware, which serve as low-cost replacements for otherwise expensive sensing or motion 
capabilities, promise to further accelerate the trend toward deploying large teams of 
mobile UVs. This trend, however, poses a challenge for the control of such systems. 
Keywords: multirobot control, neglect tolerance, attention switching, planners, task coordination
Reviews of Human Factors and Ergonomics, Vol. 9, 2013, pp. 131–174. DOI 10.1177/1557234X13506688. Copyright 2013 by Human Factors 
and Ergonomics Society. All rights reserved.

---
**[Page 2]**

132 	
Reviews of Human Factors and Ergonomics, Volume 9
Currently, multiple operators are often required to control a single UV, as in the case of 
the Predator drone. For larger systems with multiple UVs (and low-cost hardware), such 
a control approach may not be practical. Although autonomy is already playing a vital role, 
even for powerful systems, in the form of mapping tools, path planners, and monitoring 
and detection systems, it will become increasingly important for the control of robotic 
systems with larger numbers of UVs.
Multi-UV systems have their greatest potential for performing tasks that could not be 
performed by individual UVs. Loosely coupled tasks, such as deploying UVs to form a sen-
sor network, require relatively little coordination. However, many of the potentially most 
beneficial applications, such as construction, flexible manufacturing, or distributed mass 
transportation, will require UVs to exchange and respond to combinatorially massive 
amounts of information. This increase in application complexity with tightness of cou-
pling is the dominant characteristic of multi-UV systems and constrains the roles available 
to humans for controlling them. This chapter is organized to address the complexity of 
multi-UV applications and the human’s control task, and the manner of human–system 
coupling. An underlying theme is that human control remains necessary for loosely coor-
dinated activities, but automation may be applied for most other structured and highly 
coordinated activities.
A brief outline of current work in multi-UV systems is presented in the first section. 
This outline is followed by examples of the types of multi-UV simulations on which most 
of the chapter’s findings are based. In the subsequent section, models and taxonomies of 
multi-UV systems are reviewed, and a complexity-based taxonomy is discussed. The fol-
lowing section introduces levels of autonomy (LOAs) for loosely coupled multi-UV sys-
tems and presents results related to the complexity of the various forms of control. Findings 
on human interaction with multi-UVs through planners and control of swarms are then 
discussed. The subsequent section reviews studies and techniques for displaying data from 
multiple UVs. A fielded system is used to illustrate many of the issues raised in the chapter, 
which concludes with guidelines.
Survey of Research on Multi-UV Human–Robot 
Interaction (HRI)
Although research in human control of multi-UV teams is less than two decades old, the 
scope and proliferation of work prohibit a comprehensive survey within the limits of a 
single chapter. Instead, this review is focused on efforts around HRI problems and asso-
ciated techniques for multiple UVs. Systems in which single UVs are controlled by single 
operators are excluded, although the difficulties and benefits of multi-UV coordination, 
such as use of robots to observe one another (Casper, Murphy, Micire, & Hyams, 2000), 
are much the same. The first major works pairing a single operator with multiple UVs 
came in a dissertation by Julie Adams (1995), later reported in Adams (2009) and Ali 
(1999). Both studies were performed within robotics labs in computer science depart-
ments, and both studies involved remote human control over real robots. A majority of 
HRI researchers now come from departments with traditional human factors special-
ties, including psychology, industrial engineering, and aeronautical engineering. 
Human-in-the-loop simulation has come to dominate the field, although there remain 

---
**[Page 3]**

Human Interaction	
133
notable exceptions, such as Arkin’s Mission Lab, discussed in the section on interaction 
through plan libraries.
A survey of papers presented in 2012 at major conferences, including human control of 
UVs as a topic, illustrates these trends. Papers on single-human control of multiple UVs 
were found at each of the traditional robotics conferences: IEEE Conference on Robots 
and Automation, IEEE/RSJ Conference on Intelligent Robots and Systems, and IEEE 
Symposium on Robots and Human Interactive Communication. Fifteen papers were pre-
sented at meetings attracting researchers from both computer science and human factors 
research communities, including 5 at the IEEE Conference on Systems, Man, and 
Cybernetics and 10 at the ACM/IEEE Conference on Human–Robot Interaction. At the 
annual meeting of the Human Factors and Ergonomics Society, by contrast, 12 papers 
(including a special session) were devoted to the topic of multi-UV control. Twenty-two of 
all surveyed studies were conducted using human-in-the-loop simulations, whereas only 4 
employed physical platforms. Simulations were distributed between unmanned ground 
vehicles (UGVs) with 9 studies, unmanned aerial vehicles (UAVs) with 12 studies, and 
unmanned underwater vehicles (UUVs) with 1 study. Four of the identified papers were 
nonexperimental or design studies.
The most widely used simulations were ALOA (Adaptive Levels of Autonomy; Johnson, 
Leen, Goldberg, & Chiu, 2005), a multi-UAV simulation developed for the Air Force 
Research Laboratory, and Multirobot Control System (MrCS)/Unified System for 
Automation and Robot Simulation (USARSim), a UGV simulation available on 
SourceForge. (A list of acronyms occurring in the text is provided at the end of the chapter 
for reference.) Each of these simulations was used in multiple studies, yielding 3 papers per 
simulation (i.e., a total of nine publications). Onboard Planning System for UVs Supporting 
Expeditionary Reconnaissance and Surveillance (OPS-USERS) is a recent multi-UAV sim-
ulation from the Human Automation Laboratory (HAL) at MIT, and ROS/Stage is a stan-
dard simulation tool often used in robotics research. Each of these tools was used in 
multiple studies, yielding 2 papers per simulation. The 10 remaining studies each used a 
different simulator, with 7 employing publically available simulations along with four cus-
tom simulations. Both UGV and UAV simulations typically provide map-based interfaces, 
and robot trajectories are usually controlled through manual waypoints or automated 
path planning rather than direct teleoperation. However, many systems will allow teleop-
eration when needed. Operator tasks with the simulations are frequently some variant of 
foraging, in which UVs are deployed to search for targets and operators must plan or 
supervise motion paths as well as view video and other data. The basic problems of con-
trolling and monitoring multiple UVs while making sense of spatially distributed data are 
common to many of the studies reviewed.
Detail on Multi-UV Simulation Platforms
The questions that can be asked, and the generalizability of results, of simulation studies 
depend to some extent on the fidelity and capacities of the simulation used to generate 
those results. High-fidelity simulations reproduce many of the problems encountered in 
actual operations, but this very specificity may limit the range of research issues that can 
be addressed. Low-fidelity simulations, by contrast, may fail to capture the complexity and 

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

134 	
Reviews of Human Factors and Ergonomics, Volume 9
nuances of real multi-UV systems but provide a controlled tool for investigating a wide 
range of research issues. A wide variety of simulation platforms have been used in multi-
UV HRI research, ranging from first-person shooter video games (Chadwick, Gillan, 
Simon, & Pazuchanics, 2004; Chen, 2010) to standalone multi-UAV simulations, such as 
UMAST (Narayanan et al., 2000), to sophisticated networked simulations, such as the 
Mixed Initiative Experimental Testbed, a distributed multi-UV simulation developed by 
the Army Research Laboratory (Barber, Davis, Nicholson, Finkelstein, & Chen, 2008). This 
section describes three widely used multi-UV simulations, including RoboFlag (see Figure 
4.1), Research Environment for Supervisory Control of Heterogeneous Unmanned 
Vehicles (RESCHU), and USARSim, in order to provide a context for evaluating results 
and findings presented later in the chapter.
RoboFlag (D’Andrea & Babish, 2003) is a game loosely based on Capture the Flag. Two 
teams play the game, the Red Team and the Blue Team. The Red Team’s objective is to 
infiltrate Blue’s territory, grab the Blue Flag, and bring it back to the Red Home Zone while 
defending against the Blue Team’s efforts to do the same. The RoboFlag simulator provides 
a communications and control infrastructure for representing multiple UVs. The Arbiter 
acts as referee and scorekeeper and stores the rules and dynamics of the game. Low-level 
sensing and control for UVs are mediated by the Arbiter. For example, a UV can sense 
Figure 4.1. The RoboFlag simulator provides a simple map view of two unmanned vehicle 
teams (from D ’Andrea & Babish, 2003). Copyright 2003 by IEEE. Used with permission.

---
**[Page 5]**

Human Interaction	
135
other UVs only within a fixed range and, regardless of commanded values, accelerations, 
and velocities, is limited to a prescribed operational range. RoboFlag has been a popular 
platform for human/multi-UV studies because the Arbiter provides convenient access to 
UV control and simulated sensing. The game also makes supervisory control of teams and 
artificial opponents convenient to program.
Most research with RoboFlag has involved comparisons between manual control and 
automated coordination; however, Shankar, Jin, Adams and Bodenheimer (2004) report 
interface experiments. RoboFlag has also been used in contemporary human/multi-UV 
research as a result of being selected for use by researchers in a 2001 Defense Advanced 
Research Projects Agency (DARPA) program, Mixed-Initiative Control of Automata-
teams (MICA). Studies using the RoboFlag simulation are reviewed in sections on LOAs 
(e.g., Squire, Trafton, & Parasuraman, 2006), task switching (e.g., Squire et al., 2006; Squire 
& Parasuraman, 2010), and planning libraries (e.g., Parasuraman, Galster, Squire, 
Furukawa, & Miller, 2005; Parasuraman, Miller, & Galster, 2003; Squire et al., 2006).
Over the past decade, Cummings and colleagues at MIT’s HAL have developed a series 
of multi-UAV simulations for human-in-the-loop experiments, including (a) the Multi 
UAV Environment (MUAVE) in 2005, (b) a map-plus-maze search-and-rescue simulation 
in 2007, (c) RESCHU in 2008, and (d) OPS-USERS in 2010. Some unique features of these 
simulations have included (a) a focus on mission planning with timeline displays and 
schedule-oriented tasks introduced in MUAVE (and continued in RESCHU and OPS-
USERS); (b) tasks and scenarios involving human interaction with planners with tools, 
such as the configural display of plan quality, introduced in Bruni and Cummings (2005) 
and incorporated in OPS-USERS; and (c) simplified user task design to facilitate human 
performance measurement and modeling using discrete event simulation, as found in the 
map-plus-maze and RESCHU simulations (see Figure 4.2).
As the oldest of these simulations, MUAVE has accumulated the most research (seven 
journal articles and five conference papers to date), and OPS-USERS is currently the most 
actively used (producing four journal articles and five conference papers within the past 2 
years). RESCHU, which has been made available to the public through the HAL website, is, 
however, more representative of the general population of UAV simulations in that it is not 
closely linked to interaction with a planner nor is it necessarily dependent on scheduling 
decisions. Instead, it flexibly provides a map for navigation and payload window for target 
search, capacities common to most UAV simulations used by the studies reported in this 
chapter.
RESCHU (Nehme, 2009) simulates multiple heterogeneous UAVs and/or UUVs con-
ducting surveillance tasks. UVs travel along planned paths toward their target. Upon 
arrival, a payload task is spawned, requiring the operator to search for target(s) in a simu-
lated streaming video. After completing the payload task, the UV is assigned a new target 
and the process repeats. This sequence of navigation followed by visual search upon arrival 
is used in many of the simulations reported in this chapter, including Dixon, Wickens, and 
Chang (2003, 2005). The operator’s navigation task involves rerouting UVs to avoid threat 
areas and reassigning UVs to targets when poor assignments are returned by a planner. 
The task timeline with estimated arrival times provided by the software can support sched-
uling sensitive automation, as does MAUVE or OPS-USERS. The control panel in RESCHU 
provides a basis for monitoring and incorporating constraints, such as fuel usage or battle 

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

136 	
Reviews of Human Factors and Ergonomics, Volume 9
damage, into scenarios. The provision of multiple UV types and capabilities allows an 
experimenter to develop tasks of considerable complexity and difficulty, if desired. Studies 
that used the RESCHU simulation are reviewed under LOAs (Gartenberg, Breslow, 
McCurry, & Trafton, 2012), characteristics of O(n) systems (Donmez, Nehme, & 
Cummings, 2010; Gartenberg, Breslow, Park, McCurry, & Trafton, 2013), task switching 
(Gartenberg, McCurry, & Trafton, 2011), and multi-UV display (Bertucelli & Cummings, 
2012).
USARSim is a simulation of urban search-and-rescue (USAR) robots and environ-
ments (Lewis, Wang, & Hughes, 2007). USAR is a popular research domain for mobile 
robotics and has been simulated in the National Institute of Standards and Technology 
(NIST) reference environments as well as RoboCup competitions (Jacoff, Messina, Weiss, 
Tadokoro, & Nakagawa, 2003). Validation studies for simulated camera video, laser range 
finders, and robot kinematics are reported in Carpin, Stoyanov, Nevatia, Lewis, and Wang 
(2006). Wang, Lewis, Hughes, Koes, and Carpin (2005) report comparisons between oper-
ators controlling a simulated P2-AT pioneer robot and a real P3-AT at a remote location, 
finding only minor differences.
Figure 4.2. Research Environment for Supervisory Control of Heterogeneous Unmanned 
Vehicles display. Map on right shows numbered unmanned vehicles with paths to diamond-
shaped targets. Threat areas are marked by circles. Timeline and vehicle status displays 
appear at the bottom left of the display, and the chat and payload windows appear in the 
upper left.

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

Human Interaction	
137
MrCS, a multirobot communications and control infrastructure with accompanying 
user interface, was developed for experiments in multirobot control and RoboCup compe-
titions (Balakirsky et al., 2007). MrCS provides facilities for starting and controlling robots 
in the simulation, displaying camera and laser output, and supporting inter-robot com-
munication. Figure 4.3 shows the elements of the MrCS configured for 24 robots. The 
operator selects the robot to be controlled from colored thumbnails at the top of the 
screen. Thumbnails of robot camera feeds are shown on the left side of the screen, and the 
video feed of interest is presented at the top middle. The bottom right shows the current 
map displaying robot positions.
Fielded multirobot control interfaces, such as SAGE (Olson et al., 2012), differ in detail 
but feature similar map and vehicle-centric displays with selection of individual robots for 
detailed examination of sensor data or control. Studies using USARSim are reviewed under 
LOAs (Chien, Mehrotra, Brooks, Sycara, & Lewis, 2011; Valero-Gomez, Puente, & Hernando, 
2011), characteristics of O(n) systems (Lewis et al., 2010; Humphrey, Henk, Sewell, Williams, 
& Adams, 2007), aiding through scheduling (Gao, Cummings, & Bertuccelli, 2012), 3.2.2 
(Wang & Lewis, 2007b), and multi-UV display (Brooks et al., 2011; Wang et al., 2011).
Models and Taxonomies for HRI  
and Multi-UV Systems
Because of the great variety of possible ways multiple UVs can be organized and con-
trolled, researchers have been concerned with classifying multi-UV systems since the 
Figure 4.3. MrCS/USARSim multi-UV interface with map, camera views, and interaction 
through selection.

---
**[Page 8]**

138 	
Reviews of Human Factors and Ergonomics, Volume 9
beginning of the field. Dudek, Jenkin, Milios, and Wilkes (1993, 1996) and Dudek, Jenkin, 
and Milios (2002) have proposed, and repeatedly refined, a seven-dimensional classifica-
tion of UV teams based on size, three communication-related dimensions, reconfigurabil-
ity, processing ability, and heterogeneity. This taxonomy helps researchers compare “apples 
to apples” but is predominantly focused on physical and communication capabilities. 
Balch (2002) proposes a similar capability-based taxonomy but focuses on the tasks a UV 
team performs and amenability to reinforcement learning. Farinelli, Iocchi, and Nardi 
(2004) propose a different classification approach by crossing the capability dimensions of 
Dudek et al. (2002) with coordination dimensions characterizing mutual awareness and 
coordination characteristics of UVs. Although the behavioral characteristics captured by 
these taxonomies would certainly affect the ways in which a human might command 
UV teams, the taxonomies do not specify or make distinctions based on what the effects 
might be.
Scholtz, Theofanos, and Antonishek (2002) proposed a widely used taxonomy of HRI 
based on Norman’s (1988/2002) seven stages of action. Their model distinguished between 
human roles of supervisor, operator, mechanic, peer, or bystander with interpretations 
very much as the names suggest. The first two roles of supervisor and operator are con-
ceived to be predominately remote. The supervisor role is described as “monitoring and 
controlling the overall situation.” The operator is expected to “determine if actions are 
being carried out correctly and if the actions are in accordance with the longer term goal.” 
The other human roles are more likely to involve face-to-face interactions.
Yanco and Drury (2004) proposed a structural model of HRI that explicitly includes the 
possibility of interactions with teams. In their model, one considers both the numbers of 
humans and UVs and their possible links for communication/coordination. This design 
results in eight possible configurations, five involving one or more humans interacting 
with multiple UVs.
In a recent survey of HRI research, Goodrich and Schultz (2007) began by making a 
distinction between remote interaction and proximate interaction. They went on to associ-
ate remote interaction with mobile UVs with teleoperation or supervisory control while 
classifying work involving proximate interaction as primarily in the area of human–robot 
social interaction. This distinction is also made in this chapter, which focuses on remote 
interaction with multiple UVs.
A Complexity-Based Taxonomy of Multi-UV HRI
The earlier taxonomies of multi-UV systems have focused on physical characteristics, 
whereas later HRI taxonomies have dealt with roles and structure. None, however, have 
directly addressed the complexity of the operator’s tasks. In computer science, the notion 
of computational complexity, the time that must be used to solve a problem as a function 
of the size of its input, has proved fruitful for identifying poor algorithms. Algorithms with 
high complexity may work for small problems but fail or grow inefficient for even slightly 
larger ones. The task of controlling multiple UVs is similar to an algorithm in that the 
operator must perform sequences of decisions and actions to control multiple UVs. If the 
UVs perform independent but identical activities, an operator can devote the same level 
of attention to each in turn, resulting in a complexity of Order n, written O(n). That is, 

---
**[Page 9]**

Human Interaction	
139
each UV requires the same set of actions, and the total operator effort, therefore, will be 
proportional to the number of UVs. Another benefit of independence is that more UVs 
can be controlled simply by adding more operators because the UVs and their operators 
will not interfere with one another.
A different form of control, such as designating a region to be searched by drawing it on 
a map, can command an arbitrary number of UVs with a single act. Because the number 
of actions the operator must take are independent of the number of UVs, control of this 
sort is O(1) and has a constant effort. Dependent tasks, such as multiple UVs being used to 
push a box, by contrast, can be arbitrarily difficult in terms of command complexity, 
O(>n). That is, dependencies among the UVs can create cascading demands. When one 
robot pushes one corner of a box, for example, the operator must control the other robot 
to push the other corner to straighten the path of the box, after which the first robot needs 
attention again, ad infinitum.
Wang and Lewis (2007a) demonstrate that operators controlling heterogeneous box-
pushing UGVs by waypoints become rapidly saturated with no time left for additional 
tasks. Kaminka and Elmaliach (2006a, 2006b) investigated similarly tight coordination of 
Aibo robots in box pushing and formation following. In their experiments, the operator 
controlled a single UV with the others following according to their control laws. The 
experiments compared displays, one of which portrayed the relationship between robots 
as well as their camera views. Even in this case, the control task was difficult, with many 
observed failures due to the need for careful balancing of velocities and accelerations in 
order to maintain coordination among the slaved robots. It is this cascade of actions and 
reactions that makes interdependent control of even a single UV extremely difficult. 
Swarms, as discussed later in the section on “holistic” control, pose similar problems of 
indirect control but are generally more robust. The fact that only a few experiments have 
been conducted on direct human control over tightly coordinating UVs bolsters the con-
tention that augmented forms of teleoperation or semiautonomous control should be 
used by operators of such systems.
O(1) tasks require fully autonomous coordination on the part of the UVs but impose a 
constant demand only on the human operator. In general, O(1) control is appropriate 
when a large number of UVs must be tightly coordinated with a relatively simple goal, such 
as formation following or area search, or a precomputed plan can be executed. O(n) tasks, 
such as approving targets or identifying victims, are UV-centric tasks that can be per-
formed independently by one or more operators and impose a predictable additive 
demand. O(>n) tasks, by contrast, cannot be specified simply and, depending on the task, 
could require arbitrarily large control effort on the part of the operator. Figure 4.4 illus-
trates these hypothesized relations. Figure 4.5 provides examples of control at each of these 
levels of complexity.
Given the complexity of tasks envisioned for future multi-UV teams, it is unlikely that 
they can be effectively controlled at any single level of complexity. Instead we envision a 
future in which control over UVs will at various times, and sometimes simultaneously, be 
performed by different people at different levels of complexity. Although levels of com-
plexity are not identical to levels of LOAs, they characterize the degree to which coordina-
tion among UVs can be automated and whether or not a human-in-the-loop system can 
be scaled to a larger number of UVs.

---
**[Page 10]**
*(This page contains a figure/chart/image not captured in text)*

140 	
Reviews of Human Factors and Ergonomics, Volume 9
The remainder of this chapter reviews research using level of control complexity to 
develop a coherent picture of how these characteristics shape and constrain the architec-
ture of future multi-human/multi-UV systems and the human performance issues they 
raise.
Control of Independent UVs: O(n) Complexity
LOAs in Loosely Coupled Multi-UV Systems
This section covers some general findings involving LOA within independent or loosely 
coupled multi-UV systems. Research on LOA (Parasuraman, Sheridan, & Wickens, 2000; 
Sheridan & Verplank, 1978) for multi-UV control (Goodrich, Olsen, Crandall, & Palmer, 
Number of UVs
O(1)
O(n)
O(>n)
Cognitive limit
Operator
Resources
Figure 4.4. Command complexity: The figure illustrates the hypothesized relationship between 
task types and command complexity.
Figure 4.5. Examples of multi–unmanned aerial vehicle control using FalconView: O(1), 
designating search areas; O(n), setting waypoints; and O(>n), timed rendezvous requiring 
multi–unmanned vehicle synchronization.

---
**[Page 11]**

Human Interaction	
141
2001) has focused on two intermediate levels: management by consent (MBC) and man-
agement by exception (MBE). Manual control has typically involved serial control of UVs 
through teleoperation, assigning waypoints, or monitoring and prosecuting targets using 
a single UV. Full autonomy has had many meanings ranging from autonomy for indi-
vidual UVs to automated coordination through which the human interacts with UVs as a 
team. (This type of automation is discussed in later sections.) MBC and MBE LOAs cor-
respond to function allocations in which automation aids in the “implementation aspects 
of the task,” the most favorable allocation found by Kaber and Endsley (1997). A common 
finding is that the effects of automation of one task are frequently observed in perfor-
mance on another (Chen et al., 2013; Chien et al., 2011). Automating navigation, for 
example, can improve processing of targets, so measures of performance need to balance 
relative losses and gains in order to judge effectiveness. Shifts in strategy associated with 
workload reported by Gartenberg et al. (2012), who found that operators relied more on 
knowledge (inspecting retasked UAVs for conflicts, first) and memory (inspecting UAVs 
previously in conflict) under high workload illustrate the need to look beyond univariate 
measures of performance. Multiple effects were also reported by Nielsen, Goodrich, and 
Crandall (2003), who found that increases in UV autonomy reduced operator workload 
but at the same time decreased performance.
How many UVs an operator can control has been a recurring theme, and many of the 
studies covered in this chapter manipulate the number of UVs. Early studies by Trouvain 
and Wolf (2002) and Trouvain, Schlick, and Mevert (2003), for example, first set the num-
ber to four to five UVs and then back again to one, upon observing that human interven-
tion led to worse performance than automation alone. Hancock, Mouloua, Gilson, Szalma, 
and Oron-Gilad (2007) asked whether the UAV control ratio was the right question to 
study and came up with the same answer of one UV per operator. Valero, Saracini, de la 
Puente, Rodriguez-Losada, and Matia (2010) found a drop-off in performance between 
two to three UVs. Other researchers, including Humphrey et al. (2007), found a break in 
performance between six and nine UVs. Where this number may actually fall is not intrin-
sic and ultimately depends on what aspects of the task have been automated and to what 
degree. Later sections examine this issue more closely, relating it to automation of tasks, 
such as path planning.
In a study comparing control of one, two, and four UAVs in a suppression of enemy air 
defenses (SEAD) task, Ruff, Narayanan, and Draper (2002) found MBC led to better per-
formance in destroying targets, fewer hits, and higher situation awareness (SA) than did 
MBE. Their experiment used a relatively novel form of aiding in which assistance was 
provided for 10 distinct situations the UAVs might encounter. A follow-on study (Ruff, 
Calhoun, Draper, Fontejon & Guilfoos, 2004) using the more complex Multi-Modal 
Immersive Intelligent Interface for Remote Operation (MIIIRO) UAV simulation (Tso 
et al., 2003) with four interleaved tasks, and assistance limited to route replans and target 
identification, failed to demonstrate differences between MBC and MBE. The authors 
noted, however, that participants completed most tasks manually, making the compari-
sons between LOAs equivocal.
Cummings and Mitchell (2005, 2006) studied control of one, two, four, and six UAVs 
applied to a SEAD task using the MAUVE simulation (Brzezinski & Cummings, 2006). In 
this study, the initial path planning was fully automated, with operators intervening during 

---
**[Page 12]**

142 	
Reviews of Human Factors and Ergonomics, Volume 9
execution to replan aspects of the mission in response to unexpected events. In the two 
highest LOAs tested in this experiment, the automation suggested a course of action to 
alleviate periods of high anticipated workload (MBC) or executed arming and firing 
actions when a UAV reached its target (MBE). In this case, MBE produced the best perfor-
mance and highest SA whereas MBC was the poorest. As in the Ruff et al. (2004) study, 
however, this analysis could be considered a comparison of apples to oranges. The schedul-
ing task automated through MBC allowed operators to delay UAV arrival on targets in 
order to distribute workload in arming and firing missiles, whereas the MBE automated 
this task. Poor performance of MBC operators was attributed to overuse of UAV delays. 
Calhoun, Draper, and Ruff (2009) compared three LOAs, the highest of which corre-
sponded to MBE, in a three-UAV rerouting task. They found that MBE led to the longest 
rerouting times.
As this brief review suggests, there may be no best LOA for all multi-UV tasks, and 
as Hancock et al. (2007) questioned, the number of UVs that can be effectively con-
trolled may not be the right research question. Adjustable autonomy (Crandall & 
Goodrich, 2001b), in which an operator chooses the level at which to interact with a 
system, by contrast, has been found to improve operational effectiveness typically by 
allowing an operator to interleave manual commands with control at higher LOAs 
(Squire et al., 2006; Valero-Gomez et al., 2011). However, Calhoun, Ruff, Draper, 
Wright, and Mullins (2009) and Calhoun, Ruff, Draper, and Wright (2011) found that 
consistent LOAs across tasks may lead to better performance than do varying LOAs. 
The authors compared sequential tasks in which operators used same or varying LOAs 
in control of three UAVs. They found that matching LOAs led to better performance 
than did mixed LOAs.
Another line of research has involved investigating the joint effects of LOA and automa-
tion reliability on multi-UV performance. Ruff et al. (2002) also varied the fidelity of auto-
mation decisions, finding that MBC led to better rejection of bad advice than did MBE. 
Levinthal and Wickens (2006), Chen and Terrence (2009), and Chen and Barnes (2012) 
investigated trust and the effects of automation unreliability by varying the proportion of 
false alarms (Fas) and misses in UAV control. Levinthal and Wickens compared control of 
two and four UAVs supported by an automatic target recognition system with high (90%) 
reliability, that is, producing an equal number of misses and FAs, or low (60%) reliability, 
that is, biased toward either misses or FAs. They found that both the high reliability and 
miss-prone aid improved performance, whereas the FA-prone aid did not. Chen and 
Terrence did not find a main effect for miss-prone and FA-prone alerts but did find a sig-
nificant interaction with attentional control, in which participants low in attentional con-
trol benefited from the FA-prone aid but others did not. In a later study of interaction with 
a path planner, Chen and Barnes found that low-attentional-control participants per-
formed less well at path editing than did their counterparts under miss-prone conditions 
but not under FA-prone ones. Operators as a whole did less well at the unaided task of 
monitoring and marking targets in the miss-prone condition. Fincannon, Ososky, Jentsch, 
Keebler, and Phillips (2010) and Sellers, Fincannon, and Jentsch (2011) also found rela-
tions between perceptual ability and performance. High perceptual ability improved per-
formance, and team performance was largely dependent on the member with the highest 
spatial ability.

---
**[Page 13]**
*(This page contains a figure/chart/image not captured in text)*

Human Interaction	
143
Again, the findings of these studies are too equivocal for blanket recommendations. 
Chen, Barnes, and Harper-Sciarini (2011) provide a more complete review with some 
recommendations.
Control Characteristics of O(n) Systems
O(n) tasks are plentiful and likely to account for a substantial portion of a UV operator’s 
necessary interactions. Foraging tasks, such as search and rescue or reconnaissance (in 
which UVs are relatively sparse and unlikely to interfere with one another or employ auto-
mated path planning), form a broad class of applications that can be treated as O(n). Tasks 
involving individual UV status, such as monitoring for problems or failures or making 
adjustments, are also O(n) because they can be performed without reference to other UVs. 
A third class of O(n) tasks among the most crucial performed by a UV operator are those 
requiring human judgment or decision, such as target identification or weapons release. 
Taken together, foraging, status, and judgment tasks are likely to make significant contri-
butions to control of multi-UV teams.
To formalize the problems involved in O(n) control, I begin by considering the neglect 
tolerance model proposed by Crandall and Goodrich (2001a; see Figure 4.6).
According to this model, an operator’s interaction with a UV can be described as a 
sequence of control episodes. The operator interacts with the UV for period (IT), raising 
its performance above some upper threshold, after which the UV is neglected for a period 
(NT) until its performance deteriorates below a lower threshold, when the operator must 
again interact with it. The duration of the IT/NT intervals depends on the task require-
ments that determine appropriate performance thresholds. Lowering performance thresh-
olds shortens IT and lengthens NT, whereas increasing automation increases NT. This 
model is very general and can describe a range of human-UV system performance from 
very poor to the best obtainable.
Olsen’s fan-out model (Crandall, Goodrich, Olsen, & Nielson, 2005; Goodrich & Olsen, 
2003; Olsen & Wood, 2004) fixes these parameters to give an upper bound on the number 
of independent homogeneous UVs that a single human can manage. This upper bound is 
computed by identifying how long an individual UV can be neglected and then determin-
ing how many other UVs could receive interactions during this neglect interval. Thus, span 
of control is given by FO = +1. This fan-out model of span of control has been validated 
Figure 4.6. Neglect tolerance cycle from Crandall, Goodrich, Olsen, and Nielsen (2005). 
Copyright 2005 by IEEE.

---
**[Page 14]**

144 	
Reviews of Human Factors and Ergonomics, Volume 9
for teleoperated UGVs (Olsen & Wood, 2004) and waypoint-following UAVs (Cooper & 
Goodrich, 2008). The fan-out model is illustrated in Figure 4.6.
In the first interval, the operator interacts with the UV to bring it above its performance 
threshold. In the following interval, he or she neglects the UV, giving himself or herself the 
opportunity to interact with other UVs. In the third interval, the first UV’s performance 
has declined to the threshold and the operator must again interact with it. The system 
described by this fan-out model is a closed queuing system in which the operator acts as a 
server and UVs (upon reaching the lower threshold) represent jobs. Because closed queu-
ing systems are extremely difficult to model, most models discussed in this chapter treat 
the system as open, that is, with independent arrival times. If this model were accurate, 
O(n) HRI should be amenable to analysis, and aiding operators through task scheduling 
would be a possibility. One evident oversimplification of the model is the assumption of 
fixed IT and NT. Goodrich, Morse, Cooper, and Adams (2009) demonstrate that for even 
relatively small variations in IT/NT duration, operators may need to be idle up to 90% of 
the time if unserviced UVs are to be avoided.
Fixed thresholds are another simplification with testable consequences. If operators are 
expected to execute UV control to a fixed threshold, one would expect uniform increases 
in system performance up to the fan-out number with no improvement thereafter. Instead, 
a common finding (Crandall & Cummings, 2007; Humphrey et al., 2007; Lewis et al., 
2010) is that operators will attempt to control as many UVs as available, with declining 
performance per UV leading to a gradual curve without an abrupt plateau. Allowing extra-
threshold improvements and declines opens the door to more sophisticated scheduling 
techniques. Whetten, Goodrich, and Guo (2010) demonstrate that reducing fan-out 
by increasing IT duration can improve system performance whereby the derivative of 
improvement in efficiency during IT is greater than its decline during the corresponding 
interval of NT. Xu, Dai, Sycara, and Lewis (2010), assuming the same monotonicity 
of performance improvements with IT duration, developed a scheduling model 
taking advantage of individual differences among operators to optimize performance by 
varying ITs.
A more substantive mismatch between the basic fan-out model and the tasks actually 
performed by operators in the supervisory control of multi-UV systems lies in the other 
competing tasks that operators may perform during what is ostensibly UV neglect time. 
Cummings, Nehme, Crandall, and Mitchell (2007) proposed an augmented model taking 
into account wait time, FO = +1, where wait time is summed across UVs. They attribute 
wait time to three causes:
1.	 WTI: Operator time spent in planning before taking action.
2.	 WTQ: Time spent by UVs in degraded states, waiting in a queue for operator attention, 
due to near-simultaneous arrival of problems.
3.	 WTSA: Time spent before an operator notices a degraded UV state due to operator loss 
of SA or switching attention among UVs.
  The model was tested by categorizing operating intervals containing user interactions 
(IT and WTI), intervals during which a UV was in a degraded condition and another was 

---
**[Page 15]**

Human Interaction	
145
being serviced (WTQ), and intervals during which one or more UVs persisted in a 
degraded state without operator intervention (WTSA). The augmented model resulted in 
more conservative estimates of fan-out and provided a basis for simulating operator per-
formance. A series of studies by Crandall and Cummings (2007); Cummings et al. (2007); 
Nehme, Mekdeci, Crandall, and Cummings (2008); Mekdeci and Cummings (2009); 
Donmez et al. (2010); and Nehme, Kilgore, and Cummings (2008) demonstrated good fits 
between human data and discrete event simulation models treating the operator as a 
server in a queuing system incorporating the observed wait time parameters.
When systems are likely to generate WTQ and degraded states may be particularly det-
rimental to system performance, it may be desirable to specify default behaviors that take 
effect when an operator is unavailable. Tambe, Scerri, and Pynadath (2002) have proposed 
utility-based mechanisms for implementing transfer-of-control policies. One example is 
to delay the need for human attention as described earlier in Cummings and Mitchell 
(2005, 2006), whereby operators could avoid simultaneous demands by delaying a UAV’s 
arrival at a target. Glas, Kanda, Ishiguro, and Hagita (2012) and Zheng, Glas, Ishiguro, and 
Hagita (2013) confront this problem in an unusual application of control of four social 
robots in a shopping mall. In their application, mobile robots approach shoppers and initi-
ate conversational interactions. A concealed human operator supervises the four social 
robots, switching between robots as needed. By dividing interactions into phases in which 
human input is critical and not critical, they were able to maintain effective supervisory 
control, with the robots performing such “rote” tasks as greetings, introductions, and 
“small talk” autonomously. Operators took over control only when needed to interpret a 
shopper’s questions and provide guidance. By prolonging the chatting phase, the robots 
helped to modulate demand and reduced social faux pas, such as extended silences in 
communication.
Another augmented model of fan-out proposed by Chien et al. (2011) treats multi-UV 
foraging as a superposition of the task of monitoring for targets and processing through 
interaction in order to preserve UV effectiveness. In this case, both queues (monitoring, 
interaction) must be considered. As with the wait time models, both endogenous (decay in 
UV efficiency) and exogenous (arrival of targets) events must be modeled. The differences 
in models arise partially from differences in how tasks are handled. Wait time models 
describe simulations, such as MAUVE, in which the monitoring/navigation task is inter-
rupted by payload tasks, whereas in the MrCS or USARSim, the tasks are performed in 
parallel. Both augmented models point out the discrepancies between a pure queuing sys-
tem, portrayed by the basic fan-out model, and interfering tasks operators must perform 
in realistic systems. If the basic premise of the neglect tolerance model is that human inter-
action will always be needed at some interval in order to maintain the effectiveness of a UV, 
then the avenue to improving performance at the level of a multi-UV system should be to 
minimize or eliminate competing tasks. This tactic would also reduce task-switching costs.
The impact of tasks that require monitoring might be reduced by use of alarm or alert-
ing functions for UV status and automated target recognition for prosecuting targets. 
Non-UV-specific audible alarms have been found effective in reducing response times and 
errors for multi-UAV control by Dixon et al. (2003, 2005) and Donmez, Cummings, and 
Graham (2009). Gartenberg et al. (2013) compared UV-specific alarms indicating correct 
hazard region with non-UV-specific alarms displayed at unrelated regions. Accurate 

---
**[Page 16]**

146 	
Reviews of Human Factors and Ergonomics, Volume 9
alarms led to less damage while producing similar distributions of error types. Chien et al. 
(2011) found that UV-specific alarms for declines in UV effectiveness produced improve-
ments in system performance; however, queued alarms that allowed the operator to see 
only one alarm at a time produced smaller gains.
Aiding through scheduling. The possibility of improving performance through sched-
uling techniques is an immediate consequence of treating the operator as a server in a 
queuing system. The ability to schedule operator attention, however, is the fundamental 
prerequisite for using scheduling techniques to aid HRI. Chien et al.’s (2011) negative find-
ing for queued alarms suggested that it may be difficult to direct attention as precisely as 
needed in order to benefit from sophisticated scheduling algorithms. Crandall, Cummings, 
Della Penna, and de Jong (2011) addressed this question for a search-and-rescue task using 
the RESCU simulation (Crandall & Cummings, 2007). In this study, operators controlled 
two, four, six, or eight UGVs to gather tokens within a building over an 8-min period. Any 
UGVs remaining in the building when time expired were lost. Performance was deter-
mined as the number of tokens collected less the UGVs lost. The demands of the task 
varied over time, with deploying UGVs being most important at the beginning, token col-
lection taking priority in the middle of the task, and evacuation of the building dominat-
ing the close.
Using a discrete event simulation, the authors identified a utility-maximizing operator 
attention allocation scheme (OAAS) that identified a preference ordering over UGV states 
for 8-min segments of operation. So, for example, in the final minute, moving idle UGVs 
out of the building and picking up tokens were preferred to sending UGVs into the build-
ing. Their experiment compared three conditions paralleling those in Chien et al. (2011): 
a manual mode in which operators were not aided, a guided mode in which displays indi-
cated UGVs in need of attention, and an auto mode in which UGVs in need of service were 
presented one by one. Although the differences among conditions were not significant, 
operators in the manual and guided modes had higher scores, and auto participants fell 
substantially below their predicted performance. The authors note that interaction times 
in the auto mode were 1.6 s longer than in the manual mode. They attribute this effect to 
time needed to reacquire SA after switching attention to an “unexpected” UGV, an effect 
predicted by Parasuraman et al. (2000).
Chien, Mehrotra, Brooks, Lewis, and Sycara (2012) extended their study of directed 
attention to a situation in which, as in Crandall et al. (2011), a preferred ordering of actions 
(shortest job first [SJF]) existed. Under these conditions, if operator attention could be 
directed to servicing a recommended sequence of UVs, and unaided operators would not 
spontaneously choose the same optimal sequence, HRI performance should be improved 
by schedule-based aiding. This experiment compared an alarm condition in which all UVs 
in need of service were indicated, a FIFO (first in, first out) condition in which UGVs to be 
serviced were presented one at a time in the order in which they arrived, and an SJF condi-
tion in which UGVs were presented according to a throughput optimizing discipline. 
Performance of the SJF group did not statistically differ from the best-performing condi-
tion on any of the measures. However, the FIFO and alarm conditions were each signifi-
cantly worse in terms of primary failure resolution or secondary target monitoring. As in 
Crandall et al. (2011), performance in the directed attention condition fell below 

---
**[Page 17]**

Human Interaction	
147
predictions, suggesting that potential gains must be substantial in order to overcome the 
deficits in SA imposed by directing attention to an unselected UGV.
This weakly demonstrated ability to schedule operator attention between UVs is a fun-
damental prerequisite for the scheduling-based approaches to aiding HRI. Proposed 
scheduling-based approaches to multi-UV HRI have included the SJF discipline (Mau & 
Dolan, 2007; Chien et al., 2012), load balancing between operators (Powell & Morgansen, 
2012), service-level differentiation to adapt to individual differences (Xu et al., 2010), 
mechanism design to match operator levels of effort with their abilities (Dai, Sycara, & 
Lewis, 2011), and dynamic queue management to modulate operator utilization (Salva & 
Frazzoli, 2011).
Three out of these five approaches explicitly involve multiple operators, taking credit 
for load balancing to improve performance. Although multioperator/multi-UV control 
comprises five of the eight architectures identified by Yanco and Drury (2004), there has 
been relatively little empirical study in the area. Two questions involving the relation 
between multiple operators and UVs for O(1) tasks that have been addressed experimen-
tally are whether operators are more effective sharing a single queue or controlling separate 
queues and whether operators are better at sharing whole tasks or performing separate 
subtasks. Mekdeci and Cummings (2009) and Whetten et al. (2010) both found improved 
performance when operators controlling multiple UVs separated responsibility by func-
tion rather than by UV. However, Lewis et al. (2011) found better performance for opera-
tors controlling single sectors of 12 UGVs rather than sharing control of 24, although 
workload was also elevated. Fincannon, Evans, Jentsch, Phillips, and Keebler (2009) also 
report a decline in response to requests under shared control conditions. Gao et al. (2012) 
found a similar advantage for sector control but were able to eliminate it by providing 
search guidance, leading operators to shift attention between UVs more frequently.
Although these preliminary studies have yet to demonstrate the major efficiencies 
promised by scheduling models, multioperator control of multiple UVs remains a theo-
retically promising avenue of research. In particular, the call center conjecture (Nickerson 
& Skiena, 2005) holds that for the control of multiple UVs by human organizations, O(n) 
interactions can be most efficiently handled by referring UV requests for interaction to 
human operators through a scheduler. Because O(n) tasks are independent, such a system 
could scale simply by adding more operators. Because requests would originate with UVs 
rather than rely on human monitoring, the humans could behave more like the simple 
servers portrayed in the basic fan-out model, allowing load balancing in the distribution of 
requests.
Task switching. Human performance demands posed by O(1) multi-UV control 
revolve primarily around difficulties associated with switching attention among UVs and 
between tasks. These switches contribute to wait times associated with loss of SA, mea-
sured by Cummings et al. (2007) as WTSA. A basic finding of a mature literature on task 
switching (Kiesel et al., 2010) is that it costs more, typically measured in reaction time, to 
switch between task sets than to repeat a task of the same type. A task set includes a task 
goal, a set of task-relevant stimuli, a set of possible responses, and a mapping of stimuli to 
responses (Koch, Gade, Schuch, & Philipp, 2010). Switching costs are asymmetric and 
higher going from more difficult or dominant tasks to easier ones. For example, a 

---
**[Page 18]**

148 	
Reviews of Human Factors and Ergonomics, Volume 9
respondent would experience greater costs switching from a second language to a native 
tongue than vice versa (Kiesel et al., 2010). Switching between task sets with common ele-
ments, such as shared stimuli or responses, also imposes greater costs (Kiesel et al., 2010). 
From the task set perspective, there are a variety of different types of task switches involved 
in controlling multiple UVs. Shifting attention between UVs will involve shifts between 
relevant stimuli and may involve shifts in goals, if UVs are in different situations. Shifts 
between primary and payload tasks, to pursue a target, for example, involves a shift in goals 
and likely relevant stimuli. Changes in context make these types of switches relatively 
benign as they do not involve direct competition among stimuli and responses.
RoboFlag studies by Squire et al. (2006) and Squire and Parasuraman (2010) have 
addressed the more pernicious effects of switching between strategies at differing LOAs 
and workload. Strategies were defined by categorizing participant actions as offensive or 
defensive in nature. For example, a participant could alternate between waypoint control 
and play calling without entailing a switch, whereas a switch would be defined for consecu-
tive waypoints placed on different sides of the field. These studies showed that participants 
were faster in performing the same task (offense/defense), were slower at higher LOAs, and 
performed better with flexible delegation. However, Arrington and Logan (2005) also 
demonstrated that switch costs remain, even when participants choose when to switch.
A related difficulty in switching attention between UVs could involve change blindness 
(Simons & Rensink, 2005), the inability of observers to notice even large changes that 
occur when their attention is diverted. In the absence of motion signals that accompany 
change, people have substantial difficulty identifying changes in visual scenes from mem-
ory. When attention is switched between UVs, an operator is regularly confronted with this 
problem because the scene being viewed through a UV camera or instrument readings will 
have changed since last viewed but give no clue as to what that change might have been. 
Parasuraman, Cosenzo, and de Visser (2009) and de Visser and Parasuraman (2011) con-
ducted two experiments in which operators identified targets spotted from UAVs, planned 
routes for stalled UGVs, responded to SA queries, and responded to changes in the display 
in which icons were displaced by 4° visual angle. Change detection was uniformly low, 
ranging from 9.4% to 43.8%, leading Parasuraman et al. (2009) to comment, “This result 
indicates that the change blindness effect, which has typically been demonstrated in simple 
laboratory tasks or contrived social interactions . . . also occurs with more realistic displays 
relevant to real-world environments.”
Insensitivity to changes also proved to be a crucial cue for adaptive aiding at the target 
detection task that led to performance that was superior to static automation. Although 
change blindness is usually associated with aspects of a scene that are not within the focus 
of the operator’s attention, the prolonged interruptions associated with switching atten-
tion between UGVs might weaken that focus, making task-relevant aspects of the scene 
subject to change blindness. Gartenberg et al. (2011), using the RESCHU simulation alter-
nating between navigation and payload tasks, offered an alternate explanation attributing 
the loss of SA in shifting tasks to a matter of reinstating goals rather than identifying situ-
ational changes. As evidence, they cited an increase in refixations on objects viewed prior 
to interruptions.
Estimates of the cost of switching attention between UVs are of consistent magnitude, 
ranging from 2 to 4 s (Crandall & Cummings, 2007) to 4 to 5 s (Gartenberg et al., 2011). 

---
**[Page 19]**

Human Interaction	
149
Cummings et al. (2007) report that wait time, the time not accounted for by other parts of 
the NT model, is strongly dominated by WTSA, the wait time component most closely 
associated with shifts in attention between UVs. Other aspects of multi-UV control, such 
as switching between navigation and payload tasks or from monitoring to prosecuting 
targets, involve switches among task sets that are known to be particularly costly (Kiesel 
et al., 2010). Problems of both types are aggravated in multi-UV systems in which multiple 
tasks need to be performed for multiple UVs.
Goodrich, Quigley, and Cosenzo (2005) provide an estimate of the cost of task switch-
ing for change detection in the context of multi-UV control, finding switching times 
between a UAV-based secondary tasks and UGV primary tasks to be about 12 s. This dura-
tion was significantly longer than for dissimilar secondary tasks, such as Tetris (9 s), that 
did not rely on visual search or involve competing stimuli/response sets. All of Goodrich 
et al.’s delays, even those for a blank task (6 s), exceed times reported for task switching not 
involving change detection. These results suggest that change detection may dominate 
when changes are present and that changes may be missed by operators switching at 
shorter times. These results suggest that switching between navigation and target monitor-
ing, two common tasks relying on similar spatial processing, may be particularly debilitat-
ing when they must be performed using the same display.
Both Chadwick et al. (2004) and Wang and Lewis (2007b) found operators switch 
between UGVs approximately once per minute to maintain control. At these high rates of 
switching that appear necessary to maintain SA across multiple UGVs, the designer’s goal 
should be to reduce the range of tasks the operator must confront and aid in recovery of 
SA following a switch. Possibilities include use of alarms for UV status or automatic target 
recognition in order to eliminate monitoring tasks or automated path planning (discussed 
in the next section) to alleviate navigation demands. Other remedies include techniques to 
assist in reacquiring SA following a switch. Scott, Mercier, Cummings, and Wang (2006); 
Sellner, Heger, Hiatt, Simmons, and Singh (2006); and Chadwick (2006) found advantages 
to varying degrees for use of video replay to help acquaint operators with a UV’s new situ-
ation. St. John, Smallman, and Manes (2005) claimed better performance for their CHEX 
automated change detection tool; however, this claim presupposed the ability to automati-
cally detect salient changes, an unlikely capability for many tasks requiring human moni-
toring. A third approach with promising results, the GITZ (Get in the Zone) tool, uses 
principles of visual momentum (Woods, 1984) and synthetic video to move an operator’s 
viewpoint from a current UAV to a new unit (Calhoun, Warfield, Wright, Spriggs, & Ruff, 
2010; Draper et al., 2008).
Interacting With Planners: O(1)
One consequence of the conjecture that coordination of UVs is generally too complex for 
a human operator to handle is that operators will need to manage coordination of UVs 
some other way. Using planners, or programs that generate plans to satisfy user-specified 
criteria, as an intermediary is the most widely adopted solution. Planners vary greatly in 
sophistication and scope. In this section, independent path planners providing simple 
standalone path planning capability are distinguished from plan library planners that can 

---
**[Page 20]**

150 	
Reviews of Human Factors and Ergonomics, Volume 9
generate complex, multiphase plans from stored templates as well as cooperative planners 
that construct plans to satisfy an objective function under operator guidance. Independent 
planners are most useful when UVs are relatively independent, performing tasks, such as 
foraging, based on simple criteria or moving to a frontier while avoiding other UVs. Plan 
libraries are useful when complex, variable, interdependent behavior is needed, such as 
missions in which multiple UVs assume different roles at different times. Cooperative 
planners are useful when intent can be expressed relatively succinctly in an objective func-
tion and a near-optimal solution is desired.
Independent Path Planners
Independent path planners are usually designed so that the human operator cannot 
directly alter constraint or objective function parameters, so the planner must be run as a 
black box. Because the operator lacks the ability to influence the plan that is produced, 
such systems are usually fully automated or practice some form of MBC or MBE. A com-
mon strategy for interacting with independent planners is to allow the operator to adapt 
the generated plan (Chen & Barnes, 2012; Velagapudi, Wang, Scerri, Lewis, & Sycara, 
2009), often by moving planner-generated waypoints.
Path planning is the most commonly automated function in multi-UV control. For a 
variety of tasks, such as moving between locations, searching an area, deploying evenly, 
converging to a rendezvous, assigning weapons to targets, or patrolling a boundary, opti-
mal or near-optimal trajectories can be defined and computed for multiple UVs. Because 
the number and complexity of these computations for even small numbers of UVs readily 
exceed human capacities, path planning is a logical target for automation. For foraging 
(search) tasks that involve both directing UV movement and monitoring for targets, auto-
mating path planning has been shown to produce greater improvements in performance 
than aiding or automating the monitoring task (Chen et al., 2011; Goodrich, McLain, 
Anderson, Sun, & Crandall, 2007; Humphrey et al., 2007; Lewis et al., 2010). In a review of 
multi-UAV studies, Cummings et al. (2007) conclude that automated path planning 
appears necessary for applications in which operators supervise more than four UAVs.
In some systems, such as RoboLeader (Chen, Barnes, & Qu, 2010; Chen, Barnes, Quinn, 
& Plew, 2011), initial path planning is fully automated but subsequent replanning is man-
aged by consent. When confronted by a change in conditions, the operator can either select 
new waypoints or request replanning of a UGV’s path, which can then be accepted or 
disregarded. In these studies, performance also improved with automation of path plan-
ning without loss of SA. Prinet, Terhune, and Sarter (2012) employed a similar scheme, 
comparing manual waypoints, choice among alternate plans, or a single best plan. Increased 
automation improved performance across all measures except UAV loss, for which opera-
tors received chat messages unavailable to the automation. Although multi-UV path plan-
ners typically operate in a centralized fashion to dictate sets of noninterfering trajectories, 
partially distributed planners have been used as well (Chien, Wang, & Lewis, 2010; 
Cummings, How, Whitten, & Toupet, 2012). Experiments comparing foraging perfor-
mance between UGVs following prerecorded human-originated paths (Chien et al., 2010) 
with long smooth trajectories and a path-planning algorithm that produced paths with 
many loops and reversals, as confirmed by higher fractal dimension (e.g., tortuosity), 

---
**[Page 21]**

Human Interaction	
151
showed no differences in performance. The ability of human operators to gain full advan-
tage from automated path planning, even for highly complex “unnatural” paths, is further 
evidence of the robustness of the advantage and the appropriateness of automating this 
function.
Automation of path planning in multi-UV systems shifts an operator’s frame of refer-
ence from navigation of platforms to the environment through which they move. This 
shift from a platform-centric to network-centric orientation (Alberts, Garstka, & Stein, 
1999) can improve SA for the environment by allowing operators to maintain a common 
frame of reference rather than continuously shifting between different platform-centric 
viewpoints. SA regarding platform locations, orientations, movements, and fields of view 
(FOVs), however, may be lost or weakened. To help maintain a common frame of refer-
ence, UV data should be spatially organized with respect to a common frame. For UAV 
data, this organization may be accomplished by rotating camera views and other sensor 
footprints to matching orientations and laying them out in their relative spatial positions 
in a mosaic (see section on multi-UV displays). For UGV data wherein sensor FOVs are 
parallel rather than normal to the Earth’s surface, the same spatial region can be viewed 
from very different perspectives, making it difficult to show sensor data from multiple 
platforms on a single graphic.
Planners With Plan Libraries
Planning multi-UV paths to meet geometric objectives, such as coverage or rendezvous, is 
a complex problem but simple to define mathematically. Other tasks that involve phased 
actions, such as ingress, search, and egress or triggered patterns with role-based coordina-
tion (target detection, role recruitment, and battle damage assessment), are less easy to 
define in terms of an objective function to be minimized. Of all the possible actions that 
might be taken, however, such “plans” can be specified through a small number of coor-
dinated actions in a stereotyped sequence. If the appropriate coordination plan can be 
instantiated and executed, then coordination can be automated. The success of this 
approach relies on the match between the situations for which plans have been prepared 
and those that are actually encountered. Reliance on plan libraries allows a human to 
formulate plans with role assignments, decision points, termination conditions, and so on, 
which can be executed at a pace and involve cascading interdependencies. Such planning 
could not be managed by a human operator in real time.
The most well-developed of these approaches is Playbook (Miller & Parasuraman, 
2007), a family of systems that integrates a hierarchical task network (HTN) planner (Erol, 
Hendler, & Nau, 1994) with a human interface. HTN planners break down tasks, like going 
to the store, into a recursive series of subtasks, such as driving or taking a bus, culminating 
in a sequence of atomic actions, such as entering the car and inserting the key. Constraints 
among these tasks and subtasks are represented through task networks. Although allowing 
some leeway at each level of the hierarchy, plans are constrained to follow this precon-
ceived decomposition and stored in plan libraries. The skeletal plan provides a common 
task model supporting interaction between the operator and the planner. The operator 
interacts with the system by “calling plays” (skeletal plans) and providing needed parame-
ters, such as designating targets. Because the task models are presumed shared between 

---
**[Page 22]**

152 	
Reviews of Human Factors and Ergonomics, Volume 9
operator and system, human input is possible at any level of decomposition. This design 
results in an adaptable delegation interface in which the operator specifies a “play” to a 
desired level of specificity, delegating the remaining details to the planner.
The concept was initially introduced (Miller, Pelican, & Goldman, 1998) through a pro-
totype tasking interface and usage scenario for controlling multiple unmanned combat 
aerial vehicles. This research was later described in Miller and Parasuraman (2003) and 
Miller and Parasuraman (2007). Prototype applications of the planner for control of UGVs 
and heterogeneous UAVs are reported in Parasuraman and Miller (2006). These applica-
tions call for relatively sophisticated plans. The “overwatch” play described in Miller, 
Goldman, Funk, Wu, and Pate (2004), for example, requires nine parameters, ranging from 
earliest time on target to identification of the sensors required for the mission. Human 
experiments testing the effectiveness of Playbook as a tasking interface have been con-
ducted in simple domains, such as RoboFlag. Parasuraman et al. (2003) reported that play-
ers adjusted to an opponent’s strategy and that the simulation demonstrated participants’ 
willingness and ability to use plays to control multiple UVs.
Parasuraman et al. (2005) reported two additional experiments. The first compared 
flexible delegation (in which operators could both call plays and assign waypoints) with 
conditions in which they were limited to either manual or automated control. Missions 
took longer in the automated condition, and participants reported a higher level of SA in 
the manual condition. The second experiment crossed abstraction (offense/defense as 
opposed to more specific plays) with aggregation (all assigned vs. pick UVs to assign). 
Participants who had to assign all UVs the same command did better when using abstract 
plays than when using waypoints. Participants reported higher workload when only way-
point control was available. Squire et al. (2006) examined strategy switches in which a 
participant shifted between offense and defense (defined as choosing a waypoint on the 
other side of the center line in the manual condition or choosing a play from the opposite 
category in the automated condition). Switches were less common than repetitions of a 
chosen stance, and switching times were highest in the automated condition, lowest in the 
manual condition, and intermediate in the mixed condition. Goodrich et al. (2007) found 
similar results for Playbook-like autonomy conditions in which groups of UVs could be 
jointly tasked. Operators chose joint tasking as workload increased. This choice improved 
performance in one experiment but produced poor trajectories in another involving man-
ual control in which timing coordination, O(>n) control, was required.
Recent experiments using a more realistic three-UAV simulation (Fern & Shively, 2009; 
Shaw et al., 2010) compared three levels of delegation (waypoint, UAV-specific delegation, 
team delegation), finding the highest level (team delegation) and flexibility in choice of 
level to produce superior performance. Shaw et al. (2010) also examined effects of failures 
requiring manual control and found that operators responded more rapidly in the plays 
condition. This finding suggested that the technique did not foster complacency or auto-
mation bias. Versions of this system are currently undergoing usability testing (Calhoun 
et al., 2012; Miller et al., 2012) to improve design and incorporate new features.
Machinetta, also employing an HTN-like planning mechanism, began as a multiagent 
coordination infrastructure implementing Milind Tambe’s (1997) STEAM theory of joint 
intentions and teamwork. Operating in a distributed fashion, Machinetta provides mecha-
nisms for instantiating plans, allocating roles, executing plans, and detecting termination 

---
**[Page 23]**

Human Interaction	
153
conditions. Unlike Playbook, in which UVs are coordinated by sending synchronized 
instructions, coordination in Machinetta is achieved by the UVs themselves through the 
asynchronous exchange of messages and instantiation of shared plans. To Machinetta, a 
human is just another agent connected to a proxy that provides the necessary mechanisms 
for coordination. Machinetta has been used for human control of multiple UVs in much 
the same way as Playbook, with the operator instantiating plans that are then carried out 
by coordinating UVs. Schurr et al. (2005) report on experiments controlling the RoboCup 
Rescue simulation through Machinetta in which human assistance did not improve overall 
system performance. Machinetta was later used in field studies (Lewis, Polvichai, Sycara, & 
Scerri, 2006) and a subsequent flight test (Air Force Magazine, 2005) of the LOCASS (Low-
Cost Autonomous Attack System), a UAV-like munition that flew in coordination with 
simulated munitions under human supervisory control.
In a later study (Scerri, Owens, Sycara, & Lewis, 2010), Machinetta was used to provide 
control over heterogeneous air/ground UVs coordinating in persistent surveillance tasks. 
It is also part of the MrCS and used when UGVs must be coordinated for anything other 
than simple path planning, for example, coordinating scouts and rescuer UGVs in crisis/
emergency response (Lewis & Wang, 2009). Additionally, Machinetta emphasizes scalabil-
ity and has been demonstrated to scale to 1,000 agents (Xu et al., 2005).
Machinetta differs architecturally from Playbook in that it is a fully distributed system 
without centralized planning or control and puts primary emphasis on coordinating 
autonomous UVs. The centralized Playbook architecture by contrast retains control over 
UVs through a single planner that provides more opportunities for human interaction at 
different levels of plan composition. Although in principle Machinetta might support 
similar richness of interaction, the complexity would run counter to its assumptions of 
limited connectivity and interchangeability of agents.
Mission Lab (Endo, MacKenzie, & Arkin, 2004), a system developed for coordinating 
mobile robots, takes an approach even more reliant on individual UV autonomy and pro-
gramming. Although Mission Lab is descended from a long line of multirobot control 
architectures, such as Alliance (Parker, 1998), it is the first to put a primary emphasis on 
conveying human intent and HRI. In Mission Lab, UVs are programmed through assem-
blages that are temporally sequenced. An assemblage consists of groups of basic behaviors 
and coordination mechanisms. So, for example, a leader-following robot might have go-
forward and stop behaviors and a sensor that allows it to estimate its distance to an “obsta-
cle.” In the leader-follow assemblage, the robot would go forward as long as the distance to 
the obstacle was greater than X and stop otherwise. The temporal sequencing of assem-
blages can be represented as finite-state automata in which the transition between assem-
blages is triggered by changes in perception. By associating mission phases with expected 
perceptual changes, an operator can construct an executable mission plan using the sys-
tem’s graphical user interface (GUI). The human operator’s role in this system is that of the 
planner, with the UVs executing the plan autonomously.
Early usability tests (MacKenzie & Arkin, 1998) showed that users could program mis-
sions faster using this system and GUI than using the C programming language. A subse-
quent test of a new wizard feature (case-based reasoning), which retrieved and allowed 
editing of prior missions (Endo et al., 2004), worked well but fell just short of significance 
when compared to the unaided system. A contract net protocol was subsequently added to 

---
**[Page 24]**

154 	
Reviews of Human Factors and Ergonomics, Volume 9
the editor (Ulam, Endo, Wagner, & Arkin, 2007) to adjust task allocation for heteroge-
neous robots. The system was evaluated by Wagner, Endo, Ulam, and Arkin (2006) through 
comparison of NGOMSL models (Kieras, 1997) as well as estimates of gains in accuracy in 
mission generation expected through use of the cbr-cnt tools.
All three of these systems allow construction of plans for multi-UV coordination 
offline. Therefore, operators are not confronted with the complexity of that interaction 
during plan execution. Whereas Mission Lab limits human input to planning, current 
work with Playbook (Calhoun et al., 2012; Miller et al., 2012) incorporates plan monitor-
ing and retasking to extend control into execution. As a multiagent coordination infra-
structure, Machinetta was designed for dynamic plan instantiation and monitoring but 
lacks Playbook’s features for supporting human interaction.
MacKenzie and Arkin’s (1998) finding that operators did better using their graphical 
plan editor than programming missions with the C language is emblematic of the human 
factors problems facing such systems. As team numbers grow, behaviors become more 
complex, and constraints become more abundant, the operator must choose, understand, 
and adapt complex programs on the fly to supervise a multi-UV system. The studies 
reviewed show that advantages of a plan library over manual control appear to grow rap-
idly as the complexity of the situation increases; however, cognitive demands on the opera-
tor grow as well. The literature on work flow authoring (Kim, Spraragen, & Gil, 2004) and 
work flow editors might provide a guide to some of the pitfalls and solutions that arise in 
similar tasks.
Cooperative Planners
Planners typically produce a plan by finding some sequence of actions that satisfies a set 
of constraints while minimizing an objective function. Operators and planners each have 
limited visibility. The planner has access to large amounts of sensor and other data inac-
cessible to the human, and the human has knowledge of factors unrepresented within the 
planner. There are three basic reasons for humans to interact with planners:
1.	 to set objectives, such as targets to be visited by a UV;
2.	 to inject information unavailable to planners, such as marking closed roads in a data-
base; and
3.	 to mitigate shortcomings of the planner, such as directing it away from local minima and 
to help the system achieve more globally optimal solutions.
  Although planners relying on preplanned solutions can accommodate complex hetero-
geneous activities, they usually offer no guarantees of the absolute quality or appropriate-
ness of their plans. When goals and search space can be precisely defined, however, it may 
be possible to find what is truly the best plan. Planners behind the fully automated path 
planning discussed earlier may find solutions of this sort, but they do so largely without 
user influence and, therefore, are unable to benefit from an operator’s greater visibility or 
more precise knowledge of intent. At the next level of involvement, an operator can influ-
ence the plan content and not merely the choice of plan by altering either the constraints 

---
**[Page 25]**

Human Interaction	
155
or the objective function. After a plan is produced, an operator may be allowed to alter 
some aspect of the plan, such as moving a waypoint (Chen et al., 2010; Chien et al., 2010), 
or an alteration can be passed back to the planner for incorporation in a new plan 
(Cummings et al., 2012). All of these methods, sometimes in combination, have been used 
to control multi-UV teams.
Because planning involves sequences rather than single actions, it is often not apparent 
what the results of a change will be. Interactions with planners, therefore, may involve a 
test loop in which the operator proposes changes and then views test results before imple-
mentation (“what-if” testing). Roth, Hanson, Hopkins, Mancuso, and Zacharias (2004) 
and Hanson, Roth, Hopkins, and Mancuso (2004), for example, report participants’ diffi-
culties in commanding multiple-UAV teams using changes to “intent matrices” that altered 
relative target values in their planner’s objective function. Their operators expressed con-
fusion over the ordering and choices of targets in the resulting plans and had difficulties in 
adjusting entries to achieve their desired result. In the weapon-to-target assignment prob-
lem, for example, including a particular target in a plan might require multiple iterations 
and changes in preferences in order to find a plan that included a desired target without 
eliminating other desired targets. These results can be contrasted with the ease with which 
Parasuraman et al.’s (2003) participants adapted to using plays in the previous section 
while working on the same types of problems for the DARPA MICA program. Although 
the Boeing Experiment Platform (Yang et al., 2004) used in Hanson et al.’s (2004) experi-
ments was a more complex, engineering-oriented simulation, the difficulties described 
appear to arise more from the opacity of the planner than from the complexity of the task.
Constraints may be expressed to a planner through either constraining the planning 
space or delimiting an admissible space within which to plan. Constraining the planning 
space allows the operator to influence the planner’s search by disallowing some alternatives. 
In Lewis et al. (2006), for example, wide-area search munitions were directed to search some 
areas, avoid others, and jettison into a third simply by drawing associated regions onto a 
map, as presented through FalconView (Figure 4.2), a personal flight planning system. 
Delimiting an admissible space is more restrictive in that the operator must provide an 
initial rough outline of the desired plan. This approach is widely used within the animation 
community (Karamouzas, Geraerts, & Overmars, 2009) to specify wide paths within which 
crowds may travel, allowing entities to choose their own trajectories within these paths. This 
design permits the operator to roughly specify the plan while the automation optimizes 
within the operator-defined space. Cummings, Marquez, and Roy (2011) applied a variant 
of this approach to human path planning for extraterrestrial exploration by providing a 
map showing “equal cost contours” defining a wide but restricted range of paths an astro-
naut might choose. By fusing measures of “quality,” these methods are not limited to spatial 
constraints but could include limits such as fuel consumption or length of travel as well.
Cummings and colleagues have conducted a series of studies manipulating many of the 
available mechanisms for influencing planners. The base version of their operator interface 
to the OPS-USERS multi-UV simulation (How et al., 2009) incorporates several novel 
enhancements to the human–planner interface. Consequently, it is not possible to assess 
the individual contributions of each of the enhancements to simulation performance. 
However, experimental results (Cummings et al., 2012) showing performance improve-
ments, acceptable levels of workload, and user acceptance of human-directed planning 

---
**[Page 26]**

156 	
Reviews of Human Factors and Ergonomics, Volume 9
suggest that the overall interface design approach has overcome many of the difficulties 
encountered by Roth et al.’s (2004) participants.
The OPS-USERS interface (Cummings et al., 2012) consists of two screens. The first is 
a standard map display showing assets, routes, and a mission timeline. The Schedule 
Comparison Tool (SCT) (Figure 4.7) is engaged when the operator initiates replanning. 
New search tasks created by clicking on regions of the map display can be incorporated as 
constraints into the planning process. The configural displays at the top of the interface 
show the area that could be searched using the current or planner-proposed plans (upper 
left and upper right, respectively). Dragging newly created search tasks into the triangle at 
the center of the display causes the planner to create a “working schedule” incorporating 
the new task(s). This schedule is displayed in the center of the top row. The operator 
chooses one of these plans and then returns to the map display. These interactions incor-
porate two features missing in the Roth et al. (2004) system. The designation of new search 
tasks is made directly on the domain of interest, the map, rather than indirectly through 
manipulating the objective function. As a consequence, the operator gets to see the effects 
of a concrete request. The second improved feature is the incorporation of configural dis-
plays of area and priorities that allow the operator to make global as well as local judg-
ments about the quality of plans. This design helps eliminate confusions over why a 
particular plan has been adopted by the planner.
In a subsequent experiment (Clare, Cummings, How, Whitten, & Toupet, 2012), 
weightings of the objective function were added to elements under the operator’s control. 
Operators were allowed to select plan characteristics, such as target tracking or fuel effi-
ciency, through either a radio button interface (allowing a single selection) or a check box 
(when multiple alternatives were available). Under a dynamic planning condition in which 
a single objective held sway over a limited period, the radio button selection weights 
worked best; however, over the remainder of the experiment, the check box selection of 
multiple criteria led to enhanced SA and performance. A possible conjecture arising from 
these and similar studies would be that control through constraints may be most effective 
for achieving adjustments to plans, whereas modifying an objective function can provide 
secondary assistance.
Another aspect of the OPS-USERS planner is rapid replanning that allows it to suggest 
(often slightly) superior plans within a matter of seconds. Although it would be advanta-
geous for the system to always run its “best” plan, a replanning rate that imposes too high 
a workload on the human operator and prevents value-added contributions to the plan 
would be a disadvantage. Cummings, Clare, and Hart (2010) and Clare, Maere, and 
Cummings (2012) report on replanning strategies and rates, finding that moderate rates 
and compliance with planner recommendations generally led to better performance and 
lower workloads.
Rapid random tree (RRT) path planning (LaValle, 1998) provides another case in which 
human input relative to the domain of interest (map or diagram) can improve planning 
performance. The RRT method for finding collision-free paths through complex environ-
ments has difficulties finding paths through constricted areas, which are relatively easily 
seen and marked by an operator. Studies reporting improvements from human assistance 
include UAV path planning (Caves, 2010), haptic control of a virtual UGV (Taïx, Flavigné, 
& Ferré, 2012), and path planning through cluttered virtual environments (Ladevèze & 
Fourquet, 2010).

---
**[Page 27]**
*(This page contains a figure/chart/image not captured in text)*

Human Interaction	
157
The crucial feature for successful interaction with cooperative planners appears to lie in 
the relation between the human’s inputs and intentions and their effect on the plan. A less 
formal 5-participant study (Malasky, Forest, Kahn, & Key, 2005) of the system for which 
Hanson et al. (2004) reported difficulties in control through an intent matrix showed that 
allowing operators to choose the initial clusters of targets used by the algorithm for 
resource allocation and path planning substantially improved the “values” of plans. When 
the relation between the expression of intent, such as searching or avoiding a region of a 
map, realizes intelligible expression in a returned plan, cooperative planning can be fruitful 
and improve performance. When there is no such direct correspondence, as in, for exam-
ple, saving more fuel and avoiding solo flight, it may be difficult for an operator to judge 
the merits of one plan over the other. In this case, some, potentially multidimensional, 
display of plan quality, such as the SCT, may be needed for effective interaction.
Control of Team as a Whole: O(1) Swarms  
and Amorphous Computing
A new area of research in human interaction with large multi-UV teams is in the control 
of robotic swarms. Swarms are distinct from conventional multi-UV systems in that they 
Figure 4.7. Schedule Comparison Tool from Clare (2010). Reprinted with permission.

---
**[Page 28]**

158 	
Reviews of Human Factors and Ergonomics, Volume 9
use a high level of autonomy inspired from natural systems or control theory to control 
the local interactions of their members, thus reducing the need for a human to act as a 
centralized controller or to coordinate all interactions. The presumed advantages of this 
form of coordination are its robustness to loss of members or other disruptions and its 
ability to scale to very large numbers of UVs. McLurkin et al. (2006) were some of the first 
to present a serious approach to facilitating human interaction with a robotic swarm. 
Monitoring of the swarm was accomplished by viewing LEDs on the tops of robots that 
changed color with the robot’s internal state, allowing a user to get an overall picture of 
the swarm or to focus on a particular robot to diagnose a problem.
Swarming as used in robotics is a coordination mechanism that might be implemented 
in very different ways from the metaphor on which it is based. Physico-memetic mecha-
nisms, for example, use imaginary forces of attraction and repulsion to achieve coordina-
tion and direct behavior, but the actual interaction between the UVs might consist of 
message passing or proximity sensing. Swarm behavior can be influenced either by chang-
ing the perceived environment of the swarm via virtual particles or forces (Fields, Haas, 
Hill, Stachowiak, & Barnes, 2009; Kira & Potter, 2010) or by changing the variables in the 
control algorithms themselves either as a hybrid system switching between control laws 
(Kolling, Sycara, Nunnally, & Lewis, 2013) or through influence over selected leaders 
(Goodrich, Sujit, Pendleton, & Pinto, 2011; Sirouspour, 2005). Current research issues 
include methods for propagating human influence across a swarm (Amraii Amirpour, 
Lewis, & Chakraborty, 2012) and switching the behavior of swarms balanced between 
torus/flock attractors (Goodrich & Mercer, 2012).
Amorphous computing (Abelson, Beal, & Sussman, 2007) refers to the programming 
of many imaginary computers distributed irregularly throughout some surface or volume, 
each controlled through identical programs that dictate its behavior through interactions 
with nearby nodes. These computers form a discrete approximation of the continuous 
space they inhabit and, thus, can be controlled programmatically through gradients or 
vector fields. Bachrach, McLurkin, and Grue (2008) developed a language, Proto, and a 
compiler for simulating such a computer. The authors built a set of reusable swarm primi-
tives in the form of Proto programs that can be invoked during UV operations and suc-
cessfully tested their system in simulation with 10,000 individual robots and on a real-world 
system of 40 robots. There is no current research investigating how an operator could 
modify a Proto, or other amorphous computing language program, on the fly in order to 
significantly alter a swarm’s behavior after deployment; however, if such a capability were 
achieved, amorphous computing might offer a way to control swarms through 
programming.
Multi-UV Display and Visualization
While efforts to increase span of control over multiple UVs appear to be making progress, 
the asymmetry between what we can command and what we can comprehend has been 
growing. Automation can reduce excessive demands for human input, but exploiting the 
information being collected and returned poses a greater problem. Humans are frequently 
included in the loop of a multi-UV system to monitor and interpret electro-optical (such 

---
**[Page 29]**

Human Interaction	
159
as video) and other data being gathered by UVs. This task can be difficult with even a 
single camera. Gugerty and Brooks (2001) investigated the ability of Air Force recruits to 
make cardinal direction judgments from aerial imagery. Participants were presented with 
a north-up map with an icon of an aircraft and a line indicating camera heading. The 
aerial image contained a building with parking lots on four sides, only one of which had 
cars. The participants’ task was to indicate whether this parking lot was on the north, 
south, east, or west side of the building. For some camera headings, accuracy was well 
below 50%. With multiple UVs, this problem is multiplied because each view must be 
reconciled with the multiple frames of reference. With increasing autonomy of UV teams 
and plans for swarms of much greater size, the problem of absorbing and benefiting from 
the data they supply has become a bottleneck in such systems.
There are three basic problems for exploiting data returned from multiple sensors or 
UVs: (a) information fusion to integrate data from multiple viewpoints, (b) providing 
context to maintain SA, and (d) filtering to prevent operator overload. Synchronous dis-
plays from multiple UVs can easily overwhelm an operator, who must search multiple 
video streams for targets. If targets are plentiful, the operator will likely miss targets that 
enter and leave unattended views while occupied with targets in attended views. The 
related fusion and context problems arise because multiple FOVs from UVs are not aligned 
and may overlap, forcing an operator to reconcile views by mentally “piecing them 
together.” Taken together, the problems of multisensor monitoring and fusion of view-
points can pose tremendous challenges for operators, who must develop and maintain SA 
through remote sensing (Woods, Tittle, Feil, & Roesler, 2004). For more, these tasks must 
also be accomplished while operators monitor for UV errors and perform recovery, when 
necessary. Work on remote sensing and data fusion problems is most advanced for UAV 
imagery because such imagery is largely normal to the surface being viewed and can be 
organized and indexed by map coordinates.
In two studies, Calhoun, Draper, Nelson, and Ruff (2006) and Draper, Calhoun, Nelson, 
Lefebvre, and Ruff (2006) investigated the use of synthetic video overlays to supply context 
to UAV video (see Figure 4.8). Both studies showed advantages for marking landmarks in 
overlays, but in the initial experiment, Calhoun et al. (2006) found no advantage for pic-
ture-in-picture (PiP) technique, in which the UAV video was displayed in context bordered 
by synthetic imagery showing the adjacent regions of an aviation map. In the follow-on 
studies (Calhoun, Ruff, Lefebvre, Draper, & Ayala, 2007; Draper, Calhoun, Nelson, Lefebvre, 
& Ruff, 2006), a terrain elevation overlay was substituted and the PiP condition led to sub-
stantial improvements in performance. In a separate experiment, Drury, Richer, Racklie, 
and Goodrich (2006) found differences in target-marking accuracy favoring PiP and 
strong participant preference for the contextual display. Although these experimental 
results were for single UVs, the technique of presenting video in context appears to offer at 
least a partial solution to Gugerty and Brooks’ (2001) problem of translating between 
frames of reference.
A variety of display techniques have been investigated for visualizing and controlling 
multiple UVs. Porat, Oron-Gilad, Silbiger, and Rottem-Hovev (2010) propose a multi-
UAV viewing technique called “ray castling” to aid operators in choosing which UAV feed 
to view in order to continue tracking a target that has been obstructed in a currently 
attended view. Additional techniques for matching size and resolution of video when 

---
**[Page 30]**
*(This page contains a figure/chart/image not captured in text)*

160 	
Reviews of Human Factors and Ergonomics, Volume 9
switching between UAV views are reported in Oron-Gilad et al. (2011). Humphrey, 
Gordon, and Adams (2006) investigated techniques for aiding operators to visualize and 
control UGVs moving in formation, finding that an idealized semitransparent outline of 
the formation made it easier for operators to control than either a solid figure obscuring 
the UGVs or UGV icons without a formation referent. See also Kaminka and Elmaliach 
(2006a, 2006b), as earlier discussed, for use of relational visualization to assist in control-
ling formations. McCann, McSheehy, and Yanco (2012) developed a multiuser/multitouch 
interface using a Microsoft Surface that allowed users to select, group, and command 
UGVs through direct manipulation and gestures, simplifying what might be otherwise 
complex interactions. Bertuccelli and Cummings (2012) proposed a requeuing solution to 
missed targets in multi-UV viewing. By their method, an operator may shift to a new task 
if he or she is unable to rapidly locate a target in an area of interest. The UAV requeues (to 
revisit) the area so that at a later time the operator will have another opportunity to search 
the scene. This system represents a type of well-studied retrial queuing system, making it 
amenable to modeling through a discrete event simulation.
Hunn (2005, 2006) reports on a system extending PiP to fusing video from multiple 
UAVs. The display provides a movable third-person view of the UAVs showing their view-
ing cones with video projected onto a map. The SUAVE system (Abedin et al., 2011; Owens, 
Sycara, & Scerri, 2009) attacks this problem by creating textures from video imagery and 
pasting them onto a height map of the terrain. As wider areas are covered, the map is con-
tinually updated, reflecting the areas of the environment that have been viewed. To gain 
information from the UV feeds, the user inspects the map. Although the user’s interaction 
with this display is asynchronous, the map contains all information that would be cur-
rently available from synchronous video, albeit at a lower frame rate. This display is 
Figure 4.8. Synthetic video overlay with picture in picture (PiP; center) and labeled landmarks 
(right) from Calhoun, Draper, Abernath, Delgado, and Patzek (2005). Reprinted with permission.

---
**[Page 31]**
*(This page contains a figure/chart/image not captured in text)*

Human Interaction	
161
demonstrably O(1) because adding more UAVs without altering the area being covered 
will either increase the spatial resolution of the map or increase the temporal resolution of 
the map due to more frequent updates without affecting the operator’s task.
Reducing the difficulty of monitoring UGV video is a more challenging problem 
because there is no convenient correlate of an aerially viewed map to provide a common 
representation. Because UGV cameras collect many drastically different views of the same 
scene, there is no simple algorithmic way to fuse all these views simultaneously into a sin-
gle, fully informative display. Instead, an asynchronous display for UGVs needs some other 
basis for filtering imagery. One candidate would be to select as small a set of images as 
possible covering as wide an area as possible.
The ImageQueue (Brooks et al., 2011; Wang et al., 2011) accomplishes this by storing 
UGV pose and laser scans along with video frames allowing the area viewed to be com-
puted. A greedy algorithm then selected the smallest set of images that covered the greatest 
area, removing areas with viewed imagery from the queue, as shown in Figure 4.9.
This display is also O(1) because adding more UGVs without expanding the area 
searched will (with high probability) yield some views covering wider areas. Therefore, the 
display will capture either a larger percentage of the area covered within a given number of 
frames or the same area with fewer frames.
From Simulation to the Field
Although research into human control of multiple remote UVs began with robots in the 
field, most recent work has been conducted in simulation. The reasons are various, includ-
ing expense, difficulties in maintenance of large UV teams, and the increasing multidisci-
plinarity of researchers. The primary reason, however, is that with accurate/validated 
simulations, the experience of operators controlling simulations or real systems can be 
made substantially the same. In fact, in experiments, such as Wang et al. (2005), when 
operators have controlled both remotely located and simulated robots, they could not tell 
the difference and produced similar results on navigation trials across a variety of surfaces. 
As research accumulates, however, it is important that the results transfer back to the field 
and benefit the design and operation of real systems.
Figure 4.9. An illustration of the utility of individual frames from a video stream. The frame 
taken at 1) has the largest visual coverage and highest utility, whereas the frame at 2) has no 
utility since it is entirely overlapped by 1). Frame 3) has some utility since it provides coverage 
in an area not covered by 1).

---
**[Page 32]**

162 	
Reviews of Human Factors and Ergonomics, Volume 9
A primary objective of this chapter was to illustrate the degree to which no one approach 
to control or coordination is likely to be sufficient to allow operators to direct UVs in the 
numbers or complexity of behaviors they desire. The recent winner of the MAGIC (Multi-
Autonomous Ground Robot International Challenge) urban reconnaissance competition 
(Olson et al., 2012) provides a snapshot of what such systems may look like in the wild. The 
winning University of Michigan team fielded 14 robots controlled through four distinct 
user interfaces. A read-only status dashboard with visual alarms to “highlight any anoma-
lous state” and “text-to-speech announcements to indicate important error states” of indi-
vidual robots helped automate monitoring in support of the O(n) status task of directing 
operator attention to individual failures. The task operator console on which they responded 
provided a map-based interface showing UV location resembling the primary interfaces of 
most systems reviewed in this chapter. As with these systems, UVs were selected for interac-
tion from the map with their video displayed prominently only after selection.
The situations, actions, goals, and environment (SAGE) display provided a global view 
of the mission, including a map, but also showed relational events, such as a robot’s prox-
imity to dangerous objects or changes in goal state from “explore” to “neutralize.” The 
change in goal occurred autonomously, but the operator was required to perform an O(n) 
decision task to approve neutralizing the target before the robot could proceed. In keeping 
with the discussion of aiding independent control through scheduling, SAGE events were 
prioritized with only the top four displayed to better direct operator attention.
While SAGE supplied higher-level information to support SA, multirobot O(1) com-
mands, such as plays, were not available. Operators were instead required to go to the task 
console to issue individual commands, such as “Go to x,y.” In the absence of operator 
intervention, the system tasked robots autonomously using an unmodifiable frontier-
based algorithm, similar to other independent path planners discussed in this chapter. As 
this example shows, working with multi-UV systems may require a variety of control 
approaches with human intervention at a variety of levels to function successfully.
Guidelines
This section concludes the chapter with a concise set of guidelines for multi-UV system 
design based on the proposed taxonomy of operator task complexity.
O(n) Tasks
Loss of SA in switching between UVs and between tasks is the greatest difficulty posed by 
O(n) control. To help remedy this designers should
••
aid or automate monitoring tasks to as great an extent as feasible through use of auto-
matic target recognition or status alarms (Dixon et al., 2005; Donmez et al., 2009),
••
minimize the need for operators to switch between types of tasks (Goodrich et al., 2005; 
Kiesel et al., 2010), and
••
provide aiding for reacquiring SA on UVs upon task switching (Calhoun et al., 2012; 
Scott et al., 2006).

---
**[Page 33]**

Human Interaction	
163
Scheduling schemes for directing attention to individual UVs should not be used unless 
there is a strong preference for an order of servicing that may not be apparent to a human 
operator (Chien et al., 2012; Crandall et al., 2011).
O(>n) and O(1) Tasks
••
If UVs must coordinate, the coordination function should be automated before any other 
aspect of the system. This approach is based on the expectation that coordination exacts the 
highest workload cost for system operators (Chen & Barnes, 2012; Velagapudi et al., 2009).
••
Waypoint navigation imposes substantial load on operators even for relatively inde-
pendent UVs; therefore, it is a good candidate for automation (Cummings et al., 2007; 
Humphrey et al., 2007).
••
Planning methods for controlling multi-UV teams should be selected based on mission 
requirements (Goodrich et al., 2007; Squire et al., 2006).
••
Independent planners are appropriate when UVs are relatively independent and envi-
ronmental uncertainty is high (Chen et al., 2010; Goodrich et al., 2007).
••
Cooperative planners are appropriate when UV behaviors are relatively independent 
and a relatively simple objective functions can characterize operator intent. Interaction 
methods that allow an operator to express intent in the domain of interest are preferred 
(Cummings et al., 2012; Roth et al., 2004).
••
Plan libraries are appropriate when UV behaviors are highly interdependent (Endo  
et al., 2004; Miller & Parasuraman, 2007).
Abbreviations and Acronyms
AFRL: Air Force Research Laboratory
ARL: Army Research Laboratory
BDA: battle damage assessment—confirming the result of an attack often by a separate 
platform 
FIFO: first in, first out—a simple queuing discipline
GUI: graphical user interface
HRI: human–robot interaction
HTN: hierarchical task network planner—a planner that relies on a library of plans that 
can be reused with only minor changes
IT: interaction time—interval during which human interacts with UV to bring its perfor-
mance above a threshold
LOA: level of autonomy
LOCASS: Low Cost Autonomous Attack System—a UAV-like missile
MAGIC: Multi-Autonomous Ground Robot International Challenge—a DARPA-
sponsored international competition for multi-UV exploration and mapping of wide 
indoor/outdoor areas
MAUVE: Multi-Aerial Unmanned Vehicle Experiment—a multi-UAV simulation with 
timeline MBC: management by consent—an LOA in which human approves automation 
decisions
MBE: management by exception—an LOA in which automation acts unless human 
intervenes

---
**[Page 34]**

164 	
Reviews of Human Factors and Ergonomics, Volume 9
MIIIRO: Multi-Modal Immersive Intelligent Interface for Remote Operation—a multi-
UAV simulation developed for AFRL
MIX: Mixed Initiative Experimental Testbed—a distributed multi-UV simulation devel-
oped for ARL 
MrCS: multirobot control system—experimental interface and control architecture
Multi-UV: system with multiple unmanned vehicles
NT: neglect time—interval during which a robot can be neglected before requiring human 
interaction O(1), O(n), O(>n): interaction complexity in number of UVs
OPS-USERS: Onboard Planning System for UVs Supporting Expeditionary Reconnaissance 
and Surveillance
PiP: picture in picture—a display enhancement in which UAV video is displayed in the 
context of synthetic surroundings
RoboFlag: a simple multi-UV simulation environment implementing Capture the Flag 
task
RRT: rapid random tree—a widely used path planning algorithm
SA: situation awareness
SAGE: situations, goals, and environment display—multi-UV control interface used by 
winning MAGIC team
SEAD: suppression of enemy air defense
SCT: Schedule Comparison Tool—part of the MAUVE simulation
SJF: shortest job first—a queuing discipline known to maximize throughput
STEAM: Shell for Teamwork—multiagent coordination architecture developed by Milind 
Tambe
UAV, UCAV, UGV, USV, UUV, UxV: Unmanned AV—aerial vehicle; CAV—combat air 
vehicle; GV–ground vehicle; SV—surface vehicle; UV—underwater vehicle; xV—anytype 
vehicle
USAR: urban search and rescue
USARSim: Unified System for Automation and Robot Simulation—a high-fidelity UGV 
simulation WASM: wide area search munition—broadened mission for LOCASS
WT: wait time—time interval not accounted for by IT or NT
WTI: operator planning time
WTQ: wait time in queue
WTSA: wait time due to loss of situation awareness
References
Abedin, S., Wang, H., Lee, P., Lewis, M., Brooks, N., Owens, S.,  . . . Sycara, K. (2011). SUAVE: Integrating UAV 
video using a 3d model. In 2011 IEEE International Conference on Systems, Man, and Cybernetics (pp. 
2865–2869). Piscataway, NJ: IEEE.
Abelson, H., Beal, J., & Sussman, G. J. (2007). Amorphous computing. MIT CSAIT technical report, Cambridge, 
MA.
Adams, J. (1995). Human management of a hierarchical system for the control of multiple mobile robots (Disserta-
tion). University of Pennsylvania, Philadelphia.
Adams, J. A. (2009). Multiple robot-single human interaction: Effects on perceived workload and perfor-
mance. Behaviour & Information Technology, 28, 183–198.

---
**[Page 35]**

Human Interaction	
165
Air Force Magazine. (2005). LOCAAS testing at Eglin. Retrieved from http://www.airforcemag.com
Alberts, D., Garstka, J., & Stein, F. (1999). Network centric warfare: Developing and leveraging information supe-
riority. Washington, DC: Command and Control Research Program.
Ali, K. (1999). Multiagent telerobotics: Matching systems to tasks (Dissertation). Georgia Institute of Technol-
ogy, Atlanta.
Amraii Amirpour, S., Lewis, M., & Chakraborty, N. (2012, November). Input efficiency for influencing swarm. 
Paper presented at the AAAI Fall Symposium on Human Control of Bio-Inspired Swarms, Arlington, VA.
Arrington, C. M., & Logan, G. D. (2005). Voluntary task switching: Chasing the elusive homunculus. Journal of 
Experimental Psychology: Learning, Memory, and Cognition, 31, 683.
Bachrach, J., McLurkin, J., & Grue, A. (2008). Protoswarm: A language for programming multi-robot sys-
tems using the amorphous medium abstraction. Proceedings of the 7th International Joint Conference on 
Autonomous Agents and Multiagent Systems, 3, 1175–1178.
Balakirsky, S., Carpin, S., Kleiner, A., Lewis, M., Visser, A., Wang, J., & Zipara, V. (2007). Toward hetereogeneous 
robot teams for disaster mitigation: Results and performance metrics from RoboCup Rescue. Journal of 
Field Robotics, 24, 943–967.
Balch, T. (2002). Taxonomies of multirobot task and reward. In T. Balch & L. E. Parker (Eds.), Robot teams: 
From diversity to polymorphism (pp. 23–36). Natick, MA: A. K. Peters.
Barber, D., Davis, L., Nicholson, D., Finkelstein, N., & Chen, J. (2008). The Mixed Initiative Experimental 
(MIX) Testbed for human robot interactions with varied levels of automation. In International Sympo-
sium on Collaborative Technologies and Systems (pp. 483–489). New York, NY: IEEE.
Bertuccelli, L. F., & Cummings, M. L. (2012). Operator choice modeling for collaborative UAV visual search 
tasks. IEEE Transactions on Systems, Man and Cybernetics, Part A: Systems and Humans, 42, 1088–1099.
Brooks, N., Wang, H., Chien, S., Lewis, M., Scerri, P., & Sycara, K. (2011). Asynchronous control with ATR 
for large robot teams. In Proceedings of the Human Factors and Ergonomics Society 55th Annual Meeting 
(pp. 444–448). Santa Monica, CA: Human Factors and Ergonomics Society.
Bruni, S., & Cummings, M. L. (2005, June). Human interaction with mission planning search algorithms. Paper 
presented at the ASNE Human Systems Integration Conference, Arlington, VA.
Brzezinski, A., & Cummings, M. (2006). Decision support design for workload mitigation in human supervisory 
control of multiple unmanned aerial vehicles (Tech. Rep. HAL2006-05). Cambridge, MA: MIT.
Calhoun, G., Draper, M., Abernath, M., Delgadoc, F., & Patzek, M. (2005). Synthetic vision system for improv-
ing unmanned aerial vehicle operator situation awareness. Proceedings of SPIE, 5802, 219–230.
Calhoun, G., Draper, M., Nelson, J. T., & Ruff, H. A. (2006). Advanced display concepts for UAV sensor opera-
tions: Landmark cues and picture-in-picture.  In Proceedings of the Human Factors and Ergonomics Soci-
ety 50th Annual Meeting (pp. 121–125). Santa Monica, CA: Human Factors and Ergonomics Society.
Calhoun, G., Draper, M., & Ruff, H. (2009). Effect of level of automation on unmanned aerial vehicle routing 
task. In Proceedings of the Human Factors and Ergonomics Society 53rd Annual Meeting (pp. 197–201). 
Santa Monica, CA: Human Factors and Ergonomics Society.
Calhoun, G., Draper, M., Ruff, H., Barry, T., Miller, C., & Hamell, J. (2012, June). Future unmanned aerial 
systems control: Feedback on a highly flexible operator-automation delegation interface concept. Paper pre-
sented at Infotech@Aerospace 2012, Garden Grove, CA.
Calhoun, G., Ruff, H., Draper, M., & Wright, E. J. (2011). Automation-level transference effects in simulated 
multiple unmanned aerial vehicle control. Journal of Cognitive Engineering and Decision Making, 5, 55–
82.
Calhoun, G., Ruff, H., Draper, M., Wright, N., & Mullins, B. (2009, April). Levels of automation in multi-UAV 
control allocation and router tasks. Paper presented at AIAA Infotech@Aerospace, Seattle, WA.
Calhoun, G., Ruff, H., Lefebvre, A., Draper, M., & Ayala, A. (2007). Picture-in-picture augmentation of UAV 
workstation video display. In Proceedings of the Human Factors and Ergonomics Society 51st Annual Meet-
ing (pp. 70–74). Santa Monica, CA: Human Factors and Ergonomics Society.
Calhoun, G., Warfield, L., Wright, N., Spriggs, S., & Ruff, H. (2010). Automated aid evaluation for transitioning 
UAS camera views. In Proceedings of the Human Factors and Ergonomics Society 54th Annual Meeting (pp. 
413–417). Santa Monica, CA: Human Factors and Ergonomics Society.
Carpin, S., Stoyanov, T., Nevatia, Y., Lewis, M., & Wang, J. (2006). Quantitative assessments of USARSim accu-
racy. In Proceedings of PerMIS 2006 [CD-ROM]. Gaithersburg, MD: NIST.

---
**[Page 36]**

166 	
Reviews of Human Factors and Ergonomics, Volume 9
Casper, J., Murphy, R., Micire, M., & Hyams, J. (2000). Mixed-initiative control of multiple heterogeneous robots 
for urban search and rescue. Technical report, University of South Florida, Tampa.
Caves, A. D. J. (2010). Human–automation collaborative RRT for UAV mission path planning (Doctoral disserta-
tion). Massachusetts Institute of Technology, Cambridge.
Chadwick, R. (2006). Operating multiple semi-autonomous robots: Monitoring, responding, detecting. In 
Proceedings of the Human Factors and Ergonomics Society 50th Annual Meeting (pp. 329–333). Santa 
Monica, CA: Human Factors and Ergonomics Society.
Chadwick, R., Gillan, D., Simon, D., & Pazuchanics (2004). Cognitive analysis methods for control of multiple 
robots: Robotics on $5 a day. In Proceedings of the Human Factors and Ergonomics Society 48th Annual 
Meeting (pp. 688–692). Santa Monica, CA: Human Factors and Ergonomics Society.
Chen, J. Y. (2010). UAV-guided navigation for ground robot tele-operation in a military reconnaissance envi-
ronment. Ergonomics, 53, 940–950.
Chen, J. Y., & Barnes, M. J. (2012). Supervisory control of multiple robots effects of imperfect automation and 
individual differences. Human Factors, 54, 157–174.
Chen, J. Y., Barnes, M. J., & Harper-Sciarini, M. (2011). Supervisory control of multiple robots: Human- 
performance issues and user-interface design. IEEE Transactions on Systems, Man, and Cybernetics, Part 
C: Applications and Reviews, 41, 435–454.
Chen, J. Y., Barnes, M. J., & Qu, Z. (2010). RoboLeader: An agent for supervisory control of multiple robots. In 
Proceedings of ACM/IEEE International Conference on Human–Robot Interaction (HRI’ 10) (pp. 81–82). 
New York, NY: ACM.
Chen, J. Y., Barnes, M. J., Quinn, S., & Plew, W. (2011). Effectiveness of RoboLeader for dynamic re-tasking in 
an urban environment. In Proceedings of the Human Factors and Ergonomics Society 55th Annual Meeting 
(pp. 1501–1505). Santa Monica, CA: Human Factors and Ergonomics Society.
Chen, J. Y., Quinn, S., Wright, J., Barber, D., Adams, D., & Barnes, M. (2013). Human–agent teaming for robot 
management in multitasking environments. In Proceedings of the 8th ACM/IEEE International Conference 
on Human–Robot Interaction (pp. 103–104). New York, NY: ACM.
Chen, J. Y., & Terrence, P. I. (2009). Effects of imperfect automation and individual differences on concurrent 
performance of military and robotics tasks in a simulated multitasking environment. Ergonomics, 52, 
907–920.
Chien, S., Mehrotra, S., Brooks, N., Lewis, M., & Sycara, K. (2012). Scheduling operator attention for multi-
robot control. In Proceedings of the 2012 IEEE/RSJ International Conference on Intelligent Robots and 
Systems (IROS 2012) (pp. 473–479). New York, NY: IEEE.
Chien, S., Mehrotra, S., Brooks, N., Sycara, K., & Lewis, M. (2011). Effects of alarms on control of robot teams. 
In Proceedings of the Human Factors and Ergonomics Society 55th Annual Meeting (pp. 434–438). Santa 
Monica, CA: Human Factors and Ergonomics Society.
Chien, S., Wang, H., & Lewis, M. (2010). Human vs. algorithmic path planning for search and rescue by robot 
teams. In Proceedings of the Human Factors and Ergonomics Society 54th Annual Meeting (pp. 379–383). 
Santa Monica, CA: Human Factors and Ergonomics Society.
Clare, A. S. (2010). Dynamic human–computer collaboration in real-time unmanned vehicle scheduling (Thesis). 
Massachusetts Institute of Technology, Cambridge.
Clare, A. S., Cummings, M. L., How, J. P., Whitten, A. K., & Toupet, O. (2012). Operator object function guid-
ance for a real-time unmanned vehicle scheduling algorithm. Journal of Aerospace Computing, Informa-
tion, and Communication, 9, 161–173.
Clare, A. S., Maere, P., & Cummings, M. (2012), Assessing operator strategies for real-time replanning of mul-
tiple unmanned vehicles. Intelligent Decision Technologies, 6, 221–231.
Cooper, J., & Goodrich, M. (2008). Towards combining UAV and sensor operator roles in UAV-enabled visual 
search. In Proceedings of ACM/IEEE International Conference on Human–Robot Interaction (pp. 351–358). 
New York, NY: ACM.
Crandall, J., & Cummings, M. (2007). Developing performance metrics for the supervisory control of multiple 
robots. In Proceedings of the ACM/IEEEE International Conference on Human–Robot Interaction (HRI’ 07) 
(pp. 33–40). New York, NY: ACM.
Crandall, J., Cummings, M. L., Della Penna, M., & de Jong, P. M. (2011). Computing the effects of operator 
attention allocation in human control of multiple robots. IEEE Transactions on Systems, Man and Cyber-
netics, Part A: Systems and Humans, 41, 385–397.

---
**[Page 37]**

Human Interaction	
167
Crandall, J., & Goodrich, M. (2001a). Characterizing efficiency of human robot interaction: A case study of 
shared-control teleoperation. In Proceedings of the 2002 IEEE/RSJ International Conference on Intelligent 
Robots and Systems (ICRA’02) (pp. 1290–1295). New York, NY: IEEE.
Crandall, J., & Goodrich, M. (2001b). Experiments in adjustable autonomy. Proceedings of the IEEE Interna-
tional Conference on Systems, Man, and Cybernetics, 3, 1624–1629.
Crandall, J., Goodrich, M., Olsen, D., & Nielsen, C. (2005). Validating human–robot interaction schemes in 
multi-tasking environments. IEEE Transactions on Systems, Man, and Cybernetics, Part A: Systems and 
Humans, 35, 438–449.
Cummings, M., Clare, A., & Hart, C. (2010), The role of human–automation consensus in multiple unmanned 
vehicle scheduling. Human Factors, 52, 17–27.
Cummings, M., How, J., Whitten, A., & Toupet, O. (2012). The impact of human–automation collaboration in 
decentralized multiple unmanned vehicle control. Proceedings of the IEEE, 100, 660–671.
Cummings, M., Marquez, J., & Roy, N. (2011). Human–automation path planning optimization and decision 
support. International Journal of Human Computer Studies, 70, 116–128.
Cummings, M. L., & Mitchell, P. J. (2005). Managing multiple UAVs through a timeline display. In Proceedings 
of AIAA InfoTech@Aerospace [CD-ROM]. Reston, VA: American Institute of Aeronautics and Astronau-
tics.
Cummings, M. L., & Mitchell, P. J. (2006). Automated scheduling decision support for supervisory control of 
multiple UAVs. Journal of Aerospace Computing, Information, and Communication, 3, 294–308.
Cummings, M. L., Nehme, C., Crandall, J., & Mitchell, P. (2007). Predicting operator capacity for supervisory 
control of multiple UAVs. Studies in Computational Intelligence, 70, 11–37.
Dai, T., Sycara, K., & Lewis, M. (2011). A game theoretic queuing approach to self-assessment in human robot 
interaction systems. In IEEE International Conference on Robotics and Automation (ICRA 2011) (pp. 
58–63). New York, NY: IEEE.
D’Andrea, R., & Babish, M. (2003). The RoboFlag testbed. Proceedings of the 2003 American Control Conference, 
2003, 656–660.
de Visser, E., & Parasuraman, R. (2011). Adaptive aiding of human–robot teaming effects of imperfect auto-
mation on performance, trust, and workload. Journal of Cognitive Engineering and Decision Making, 5, 
209–231.
Dixon, S. R., Wickens, C. D., & Chang, D. (2003). Comparing quantitative model predictions to experimental 
data in multiple-UAV flight control. In Proceedings of the Human Factors and Ergonomics Society 47th 
Annual Meeting (pp. 104–108). Santa Monica, CA: Human Factors and Ergonomics Society.
Dixon, S. R., Wickens, C. D., & Chang, D. (2005). Mission control of multiple unmanned aerial vehicles: A 
workload analysis. Human Factors, 47, 479–487.
Donmez, B., Cummings, M. L., & Graham, H. D. (2009). Auditory decision aiding in supervisory control of 
multiple unmanned aerial vehicles. Human Factors, 51, 718–729.
Donmez, B., Nehme, C., & Cummings, M. L. (2010). Modeling workload impact in multiple unmanned vehi-
cle supervisory control. IEEE Transactions on Systems, Man and Cybernetics, Part A: Systems and Humans, 
40, 1180–1190.
Draper, M., Calhoun, G., Nelson, J., Lefebvre, A., & Ruff, H. (2006, October). Synthetic vision overlay concepts 
for uninhabited aerial vehicle operations: Evaluation of update rate on four operator tasks. Paper presented 
at the NATO-HTM-135 Symposium on Human Factors of Uninhabited Military Vehicles as Force Mul-
tiplier, Biarritz, France.
Draper, M., Calhoun, G., Ruff, H., Mullins, B., Lefebvre, A., Ayala, A., & Wright, N. (2008). Transition display 
aid for changing camera views in UAV operations. In Proceedings of Humans Operating Unmanned Sys-
tems. Brest, France: Telecom Bretangne.
Drury, J., Richer, J., Racklie, N., & Goodrich, M. (2006). Comparing situation awareness for two unmanned 
aerial vehicle human interface approaches. In Proceedings of the IEEE International Workshop on Safety, 
Security and Rescue Robotics.
Dudek, G., Jenkin, M., & Milios, E. (2002). A taxonomy of multirobot systems. In T. Balch & L. E. Parker (Eds.), 
Robot teams: From diversity to polymorphism (pp. 3–22). Natick, MA: A. K. Peters.
Dudek, G., Jenkin, M., Milios, E., & Wilkes, D. (1993). A taxonomy for swarm robots. In Proceedings of the 
1993 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS ’93) (pp. 441–447). New 
York, NY: IEEE.

---
**[Page 38]**

168 	
Reviews of Human Factors and Ergonomics, Volume 9
Dudek, G., Jenkin, M., Milios, E., & Wilkes, D. (1996). A taxonomy for multi-agent robotics. Autonomous 
Robots, 3, 375–397.
Endo, Y., MacKenzie, D., & Arkin, R. (2004). Usability evaluation of high-level user assistance for robot mis-
sion specification. IEEE Transactions on Systems, Man, and Cybernetics, Part C: Applications and Reviews, 
34, 168–180.
Erol, K. J., Hendler, J., & Nau, D. (1994). HTN planning: Complexity and expressivity. Proceedings of the Annual 
Meeting of the Association for Advancement of Artificial Intelligence (AAAI-94) (pp. 1123–1128). Palo Alto, 
CA: AAAI Press.
Farinelli, A., Iocchi, L., & Nardi, D. (2004). Multirobot systems: A classification focused on coordination. IEEE 
Transactions on Systems, Man, and Cybernetics, Part B, 34, 2015–2028.
Fern, L., & Shively, R. J. (2009, August). A comparison of varying levels of automation on the supervisory control 
of multiple UASs. Paper presented at AUVSI’s Unmanned Systems, Washington, DC.
Fields, M., Haas, E., Hill, S., Stachowiak, C., & Barnes, L. (2009). Effective robot team control methodologies 
for battlefield applications. In Proceedings of IEEE/RSJ International Conference on Intelligent Robots and 
Systems (IROS’ 09) (pp. 5862–5867). New York, NY: IEEE.
Fincannon, T. D., Evans, A. W., Jentsch, F., Phillips, E., & Keebler, J. (2009). Effects of sharing control of 
unmanned vehicles on backup behavior and workload in distributed operator teams. In Proceedings of 
the Human Factors and Ergonomics Society 53rd Annual Meeting (pp. 1300–1303). Santa Monica, CA: 
Human Factors and Ergonomics Society.
Fincannon, T. D., Ososky, S., Jentsch, F., Keebler, J., & Phillips, E. (2010). Some good and bad with spatial abil-
ity in three person teams that operate multiple unmanned vehicles. In Proceedings of the Human Factors 
and Ergonomics Society 54th Annual Meeting (pp. 1615–1619). Santa Monica, CA: Human Factors and 
Ergonomics Society.
Gao, F., Cummings, M. L., & Bertuccelli, L. F. (2012). Teamwork in controlling multiple robots. In Proceedings 
of the Seventh Annual ACM/IEEE International Conference on Human–Robot Interaction (pp. 81–88). New 
York, NY: ACM.
Gartenberg, D., Breslow, L. A., McCurry, J. M., & Trafton, J. G. (2012). Time pressure, memory, and task knowl-
edge facilitate the opportunism heuristic in dynamic tasks. In Proceedings of the Human Factors and 
Ergonomics Society 56th Annual Meeting (pp. 1025–1029). Santa Monica, CA: Human Factors and Ergo-
nomics Society.
Gartenberg, D., Breslow, L. A., Park, J., McCurry, J. M., & Trafton, J. G. (2013). Adaptive automation and cue 
invocation: The effect of cue timing on operator error. In Proceedings of the 2013 ACM Annual Conference 
on Human Factors in Computing Systems (pp. 3121–3130). New York, NY: ACM.
Gartenberg, D., McCurry, M., & Trafton, G. (2011). Situation awareness reacquisition in a supervisory control 
task. In Proceedings of the Human Factors and Ergonomics Society 55th Annual Meeting (pp. 355–359). 
Santa Monica, CA: Human Factors and Ergonomics Society.
Glas, D. F., Kanda, T., Ishiguro, H., & Hagita, N. (2012). Teleoperation of multiple social robots. IEEE Transac-
tions on Systems, Man, and Cybernetics, Part A: Systems and Humans, 42, 530–544.
Goodrich, M. A., McLain, T. W., Anderson, J. D., Sun, J., & Crandall, J. W. (2007). Managing autonomy in robot 
teams: Observations from four experiments. In Proceedings of the ACM/IEEE International Conference on 
Human–Robot Interaction (pp. 25–32). New York, NY: ACM.
Goodrich, M. A., & Mercer, E. G. (2012). Abstraction and persistence: Macro-level guarantees of collective bio-
inspired teams under human supervision. In Proceedings of Infotech@Aerospace [CD-ROM]. Reston, VA: 
American Institute of Aeronautics and Astronautics.
Goodrich, M. A., Morse, B., Engh, C., Cooper, J., & Adams, J. (2009). Towards using UAVs in wilderness search 
and rescue: Lessons from field trials. Interaction Studies Journal, 10, 453–478.
Goodrich, M. A., & Olsen, D. R., Jr. (2003). Seven principles of efficient human robot interaction. IEEE Inter-
national Conference on Systems, Man and Cybernetics, 4, 3942–3948.
Goodrich, M. A., Olsen, D. R., Crandall, J. W., & Palmer, T. J. (2001). Experiments in adjustable autonomy. In 
Proceedings of IJCAI Workshop on Autonomy, Delegation and Control: Interacting With Intelligent Agents 
(pp. 1624–1629). International Joint Conference on Artificial Intelligence.
Goodrich, M. A., Quigley, M., & Cosenzo, K. (2005). Task switching and multi-robot teams. In A. Schultz, 
L. Parker, & F. Schneider (Eds.), Multi-robot systems: From swarms to intelligent automata (Vol. 3, pp. 
185–195). New York, NY: Springer.

---
**[Page 39]**

Human Interaction	
169
Goodrich, M. A., & Schultz, A. (2007). Human–robot interaction: A survey. Foundations and Trends in Human–
Computer Interaction, 1, 203–275.
Goodrich, M. A., Sujit, P., Pendleton, B., & Pinto, J. (2011). Toward human interaction with bio-inspired robot 
teams. In Proceedings of the IEEE International Conference on Systems, Man, and Cybernetics (pp. 2859–
2864). New York, NY: IEEE.
Gugerty, L., & Brooks, J. (2001). Seeing where you are heading: Integrating environmental and egocen-
tric reference frames in cardinal direction judgments. Journal of Experimental Psychology: Applied, 7, 
251–266.
Hancock, P. A., Mouloua, M., Gilson, R., Szalma, J., & Oron-Gilad, T. (2007). Provocation: Is the UAV control 
ratio the right question? Ergonomics in Design, 15(1), 7.
Hanson, M. L., Roth, E., Hopkins, C. M., & Mancuso, V. (2004). Designing human system interfaces for super-
vising multiple UAV teams. In AIAA Aerospace Sciences Conference (pp. 5–8). Reston, VA: American Insti-
tute of Aeronautics and Astronautics.
How, J., Fraser, C., Kulling, K., Bertuccelli, L., Toupet, O., Brunet, L.,  . . . Roy, N. (2009). Increasing autonomy 
of UAVs decentralized CSAT mission management algorithm. IEEE Transactions on Robotics and Auto-
mation, 16(2), 43–51.
Humphrey, C. M., Gordon, S. M., & Adams, J. A. (2006). Visualization of multiple robots during team activi-
ties. In Proceedings of the Human Factors and Ergonomics Society 50th Annual Meeting (pp. 651–655). 
Santa Monica, CA: Human Factors and Ergonomics Society.
Humphrey, C. M., Henk, C., Sewell, G., Williams, B., & Adams, J. (2007). Assessing the scalability of a multiple 
robot interface. In Proceedings of ACM/IEEE 2007 International Conference on Human–Robot Interaction 
(HRI’ 07) (pp. 239–246). New York, NY: ACM.
Hunn, B. (2005). The human challenges of command and control with multiple unmanned aerial vehicles. 
In Proceedings of the Human Factors and Ergonomics Society 49th Annual Meeting (pp. 20–24). Santa 
Monica, CA: Human Factors and Ergonomics Society.
Hunn, B. (2006). Video imagery’s role in network centric, multiple unmanned aerial vehicle (UAV) operations. 
In N. Cooke, H. Pringle, H. Pedersen, & O. Connor (Eds.), Human factors of remotely operated vehicles 
(pp. 179–192). Oxford, UK: Elsevier.
Jacoff, A., Messina, E., Weiss, B., Tadokoro S., & Nakagawa, Y. (2003). Test arenas and performance metrics 
for urban search and rescue robots. In 2003 IEEE/RSJ International Conference on Intelligent Robots and 
Systems (pp. 3396–3403). New York, NY: IEEE.
Johnson, R., Leen, M., Goldberg, D., & Chiu, M. (2005). Adaptive levels of autonomy (ALOA) for UAV super-
visory control. Whittier, CA: OR Concepts Applied. Retrieved from http://www.dtic.mil/dtic/tr/fulltext/
u2/a437269.pdf
Kaber, D. B., & Endsley, M. R. (1997). Out-of-the-loop performance problems and the use of intermediate 
levels of automation for improved control system functioning and safety. Process Safety Progress, 16, 
126–131.
Kaminka, G. A., & Elmaliach, Y. (2006a, May). Experiments with an ecological interface for monitoring tightly-
coordinated robot teams. In Proceedings 2006 IEEE International Conference on Robotics and Automation 
(ICRA) (pp. 200–205). New York, NY: IEEE.
Kaminka, G. A., & Elmaliach, Y. (2006b). Single operator, multiple robots: Call-request handling in tight-
coordination tasks. Distributed Autonomous Robotic Systems, 7, 103–113.
Karamouzas, I., Geraerts, R., & Overmars, M. (2009). Indicative routes for path planning and crowd simula-
tion. In Proceedings of the 4th International Conference on Foundations of Digital Games (pp. 113–120). 
Santa Cruz, CA: Society for the Advancement of the Science of Digital Games.
Kieras, D. (1997). A guide to GOMS model usability evaluation using NGOMSL. In M. Helander & 
T. Landauer (Eds.), The handbook of human–computer interaction (2nd ed., pp. 733–766). Amsterdam, 
Netherlands: North-Holland.
Kiesel, A., Steinhauser, M., Wendt, M., Falkenstein, M., Jost, K., Philipp, A., & Koch, I. (2010). Control and 
interference in task switching: A review. Psychological Bulletin, 36, 840–874.
Kim, J., Spraragen, M., & Gil, Y. (2004). An intelligent assistant for interactive workflow composition. In Pro-
ceedings of the International Conference on Intelligent User Interfaces (pp. 125–131). New York, NY: ACM.
Kira, Z., & Potter, M. (2010). Exerting human control over decentralized robot swarms. In IEEE/RSJ Interna-
tional Conference on Intelligent Robots and Systems (IROS) (pp. 566–571). New York, NY: IEEE.

---
**[Page 40]**

170 	
Reviews of Human Factors and Ergonomics, Volume 9
Koch, I., Gade, M., Schuch, S., & Philipp, A. M. (2010). The role of inhibition in task switching: A review. Psy-
chonomic Bulletin & Review, 17, 1–14.
Kolling, A., Sycara, K., Nunnally, S., & Lewis, M. (2013). Human swarm interaction: An experimental study of 
two types of interaction with foraging swarms. Journal of Human–Robot Interaction, 2, 103–128.
Ladevèze, N., & Fourquet, J. Y. (2010, December). On the collaboration of an automatic path-planner and a 
human user for path-finding in virtual industrial scenes. In 2010 11th International Conference on Con-
trol Automation Robotics & Vision (ICARCV) (pp. 467–472). New York, NY: IEEE.
LaValle, S. (1998). Rapidly-exploring random trees: A new tool for path planning (TR 98-11). Iowa State Uni-
versity, Ames.
Levinthal, B. R., & Wickens, C. D. (2006). Management of multiple UAVs with imperfect automation. In Pro-
ceedings of the Human Factors and Ergonomics Society 50th Annual Meeting (pp. 1941–1944). Santa Mon-
ica, CA: Human Factors and Ergonomics Society.
Lewis, M., Polvichai, J., Sycara, K., & Scerri, P. (2006). Scaling-up human control for large UAV teams. In N. 
Cooke, H. Pringle, H. Pedersen, & O. Connor (Eds.), The human factors of remotely piloted vehicles (pp. 
237–250). New York, NY: Elsevier.
Lewis, M., & Wang, J. (2009). Measuring coordination demand in multirobot teams. In Proceedings of the 
Human Factors and Ergonomics Society 53rd Annual Meeting (pp. 779–783). Santa Monica, CA: Human 
Factors and Ergonomics Society.
Lewis, M., Wang, H., Chien, S., Ma, Z., Velagapudi, P., Scerri, P., & Sycara, K. (2011). Process and performance 
in human–robot teams. Journal of Cognitive Engineering and Decision Making, 5, 186–208.
Lewis, M., Wang, H., Chien, S., Velagapudi, P., Scerri, P., & Sycara, K. (2010). Choosing autonomy modes for 
multirobot search. Human Factors, 52, 225–233.
Lewis, M., Wang, J., & Hughes, S. (2007). USARsim: Simulation for the study of human–robot interaction. 
Journal of Cognitive Engineering and Decision Making, 1, 98–120.
MacKenzie, D., & Arkin, R. (1998). Evaluating the usability of robot programming toolsets. International Jour-
nal of Robotics Research, 4, 381–401.
Malasky, J., Forest, L. M., Kahn, A. C., & Key, J. R. (2005). Experimental evaluation of human-machine collab-
orative algorithms in planning for multiple UAVs. 2005 IEEE International Conference on Systems, Man 
and Cybernetics, 3, 2469–2475.
Mau, S., & Dolan, J. (2007). Scheduling for humans in multirobot supervisory control. In IEEE/RSJ Interna-
tional Conference on Intelligent Robots and Systems (pp. 1637–1643). New York, NY: IEEE.
McCann, E., McSheehy, S., & Yanco, H. (2012). Multi-user multi-touch multi-robot command and control of 
multiple simulated robots. In Proceedings of the Seventh Annual ACM/IEEE International Conference on 
Human–Robot Interaction (pp. 413–414). New York, NY: ACM.
McLurkin, J., Smith, J., Frankel, J., Sotkowitz, D., Blau, D., & Schmidt, B. (2006). Speaking swarmish: Human–
robot interface design for large swarms of autonomous mobile robots. In Proceedings of AAAI Spring 
Symposium to Boldly Go Where No Human–Robot Team Has Gone Before (pp. 72–75). Palo Alto, CA: 
AAAI Press.
Mekdeci, B., & Cummings, M. (2009, September). Modeling multiple human operators in the supervisory control 
of heterogeneous unmanned vehicles. Paper presented at the 9th Conference on Performance Metrics for 
Intelligent Systems (PerMIS’ 09), Gaithersburg, MD: NIST.
Miller, C., Goldman, R., Funk, H., Wu, P., & Pate, B. (2004). A playbook approach to variable autonomy 
control: Application for control of multiple, heterogeneous unmanned air vehicles. In Proceedings of 
FORUM 60, the Annual Meeting of the American Helicopter Society (pp. 7–10). American Helicopter Soci-
ety International.
Miller, C., Hamell, J., Barry, T., Ruff, H., Draper, M., & Calhoun, G. (2012). Adaptable operator–automation 
interface for future unmanned aerial systems control: Development of a highly flexible delegation con-
cept demonstration. In Proceedings of AIAA Infotech@Aerospace (pp. 1507–1527). Reston, VA: American 
Institute of Aeronautics and Astronautics.
Miller, C., & Parasuraman, R. (2003). Beyond levels of automation: An architecture for more flexible human–
automation collaboration. In Proceedings of the Human Factors and Ergonomics Society 47th Annual 
Meeting (pp. 182–186). Santa Monica, CA: Human Factors and Ergonomics Society.
Miller, C., & Parasuraman, R. (2007). Designing for flexible interaction between humans and automation: 
Delegation interfaces for supervisory control. Human Factors, 49, 57–75.

---
**[Page 41]**

Human Interaction	
171
Miller, C., Pellican, M., & Goldman, R. (1998). A high-level “tasking” interface for uninhabited combat air 
vehicles. In IUI ’99 Proceedings of the 4th International Conference on Intelligent user interfaces (p. 197). 
New York, NY: ACM.
Narayanan, S., Ruff, H. A., Edala, N. R., Geist, J. A., Patchigolla, K. K., Draper, M., & Haass, M. (2000). Human-
integrated supervisory control of uninhabited combat aerial vehicles. Journal of Robotics and Mechatron-
ics, 12, 628–639.
Nehme, C. E. (2009). Modeling human supervisory control in heterogeneous unmanned vehicle systems. Cam-
bridge: Massachusetts Institute of Technology.
Nehme, C. E., Kilgore, R. M., & Cummings, M. L. (2008). Predicting the impact of heterogeneity on unmanned-
vehicle team performance. In Proceedings of the Human Factors and Ergonomics Society 52nd Annual 
Meeting (pp. 917–921). Santa Monica, CA: Human Factors and Ergonomics Society.
Nehme, C. E., Mekdeci, B., Crandall, J. W., & Cummings, M. L. (2008). The impact of heterogeneity on opera-
tor performance in futuristic unmanned vehicle systems. International C2 Journal, 2(2), 1–30.
Nickerson, J., & Skiena, S. (2005). Attention and communication: Decision scenarios for teleoperating robots. 
In Proceedings of the 38th Annual Hawaii International Conference on Systems Science (HICSS’ 05)  
(pp. 1–10). New York, NY: IEEE.
Nielsen, C., Goodrich, M., & Crandall, J. (2003, October). Experiments in human-robot teams, Proceedings of 
the 2002 NRL Workshop on Multi-Robot Systems.
Norman, D. (2002). The design of everyday things. New York, NY: Basic Books. (Original work published 1988)
Olsen, D., & Wood, S. (2004). Fan-out: Measuring human control of multiple robots. In Human Factors in 
Computing Systems (CHI’ 04) (pp. 231–238). New York, NY: ACM.
Olson, E., Strom, J., Morton, R., Richardson, A., Ranganathan, P., Goeddel, R.,  . . . Marinier, B. (2012). Progress 
towards multi-robot reconnaissance and the MAGIC 2010 competition. Journal of Field Robotics, 29, 
762–792.
Oron-Gilad, T., Porat, T., Fern, L., Draper, M., Shively, R. J., Silbiger, J., & Rottem-Hovev, M. (2011). Tools and 
techniques for MOMU (multiple operator multiple UAV) environments: An operational perspective. 
In Proceedings of the Human Factors and Ergonomics Society 55th Annual Meeting (pp. 86–90). Santa 
Monica, CA: Human Factors and Ergonomics Society.
Owens, S., Sycara, K., & Scerri, P. (2009). Using immersive 3D terrain models for fusion of UAV surveillance 
imagery. In Proceedings of AIAA InfoTech [CD-ROM]. Reston, VA: American Institute of Aeronautics and 
Astronautics.
Parasuraman, R., Cosenzo, K. A., & de Visser, E. (2009). Adaptive automation for human supervision of mul-
tiple uninhabited vehicles: Effects on change detection, situation awareness, and mental workload. Mili-
tary Psychology, 21, 270.
Parasuraman, R., Galster, S., Squire, P., Furukawa, H., & Miller, C. (2005). A flexible delegation-type interface 
enhances system performance in human supervision of multiple robots: Empirical studies with Robo-
Flag. IEEE Systems, Man, and Cybernetics, Part A: Systems and Humans, 35, 481–493.
Parasuraman, R., & Miller, C. (2006). Delegation interfaces for human supervision of multiple unmanned 
vehicles: Theory, experiments, and practical applications. In N. Cooke, H. Pringle, H. Pedersen, 
& O. Connor (Eds.), Human factors of remotely operated vehicles (pp. 251–266). San Diego, CA: 
Elsevier.
Parasuraman, R., Miller, C., & Galster, S. (2003). Human control of multiple robots in the RoboFlag simula-
tion environment. In IEEE International Conference on Systems, Man, and Cybernetics (pp. 3232–3237). 
New York, NY: IEEE.
Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction 
with automation. IEEE Transactions on Systems, Man and Cybernetics, Part A: Systems and Humans, 30, 
286–297.
Parker, L. (1998). ALLIANCE: An architecture for fault tolerant multi-robot cooperation. IEEE Transactions on 
Robotics and Automation, 14, 220–240.
Porat, T., Oron-Gilad, T., Silbiger, J., & Rottem-Hovev, M. (2010). “Castling rays”: A decision support tool 
for UAV-switching tasks. In CHI’ 10 Extended Abstracts on Human Factors in Computing Systems (pp. 
3589–3594). New York, NY: ACM.
Powell, N., & Morgansen, K. (2012). Multiserver queueing for supervisory control of autonomous vehicles. In 
Proceedings of the 2012 American Controls Conference (pp. 3179–3185). New York, NY: IEEE.

---
**[Page 42]**

172 	
Reviews of Human Factors and Ergonomics, Volume 9
Prinet, J. C., Terhune, A., & Sarter, N. B. (2012). Supporting dynamic re-planning in multiple UAV control: A 
comparison of 3 levels of automation. In Proceedings of the Human Factors and Ergonomics Society 56th 
Annual Meeting (pp. 423–427). Santa Monica, CA: Human Factors and Ergonomics Society.
Roth, E., Hanson, M., Hopkins, C., Mancuso, V., & Zacharias, G. (2004). Human in the loop evaluation of a 
mixed-initiative system for planning and control of multiple UAV teams. In Proceedings of the Human 
Factors and Ergonomics Society 48th Annual Meeting (pp. 280–284). Santa Monica, CA: Human Factors 
and Ergonomics Society.
Ruff, H. A., Calhoun, G. L., Draper, M. H., Fontejon, J. V., & Guilfoos, B. J. (2004). Exploring automation issues 
in supervisory control of multiple UAVs. In Proceedings of the Human Performance, Situation Awareness, 
and Automation Technology Conference (pp. 218–222). Hillsdale, NJ: Lawrence Erlbaum.
Ruff, H. A., Narayanan, S., & Draper, M. H. (2002). Human interaction with levels of automation and decision-
aid fidelity in the supervisory control of multiple simulated unmanned air vehicles. Presence: Teleopera-
tors & Virtual Environments, 11, 335–351.
Salva, K., & Frazzoli, E. (2011). A dynamical queue approach to intelligent task management for human opera-
tors. Proceedings of the IEEE, 100, 672–686.
Scerri, P., Owens, S., Sycara, K., & Lewis, M. (2010). User evaluation of a GUI for controlling an autonomous 
persistent surveillance team. Proceedings of SPIE, 7694.
Scholtz, J., Theofanos, M., & Antonishek, B. (2002). Theory and evaluation of human robot interactions. In 
36th Hawaii International Conference on Systems Sciences (HICSS’ 02). New York, NY: IEEE.
Schurr, N., Marecki, J., Tambe, M., Scerri, P., Kasinadhuni, N., & Lewis, J. P. (2005). The future of disaster 
response: Humans working with multiagent teams using DEFACTO. In AAAI Spring Symposium: AI 
Technologies for Homeland Security (pp. 9–16). Palo Alto, CA: AAAI Press.
Scott, S. D., Mercier, S., Cummings, M. L., & Wang, E. (2006). Assisting interruption recovery in supervisory 
control of multiple UAVs. In Proceedings of the Human Factors and Ergonomics Society 50th Annual Meet-
ing (pp. 699–703). Santa Monica, CA: Human Factors and Ergonomics Society.
Sellers, B., Fincannon, T., & Jentsch, F. (2011). Indexing spatial ability across team size the influence of the 
weakest link, strongest link, and aggregate ability on performance with multiple unmanned systems. 
In Proceedings of the Human Factors and Ergonomics Society 55th Annual Meeting (pp. 899–903). Santa 
Monica, CA: Human Factors and Ergonomics Society.
Sellner, B., Heger, F. W., Hiatt, L. M., Simmons, R., & Singh, S. (2006). Coordinated multiagent teams and slid-
ing autonomy for large-scale assembly. Proceedings of the IEEE, 94, 1425–1444.
Shankar, S., Jin, Y., Adams, J. A., & Bodenheimer, B. (2004). Enhancing RoboFlag users’ situational awareness. 
In Proceedings of the Human Factors and Ergonomics Society 48th Annual Meeting (pp. 856–860). Santa 
Monica, CA: Human Factors and Ergonomics Society.
Shaw, T., Emfield, A., Garcia, A., de Visser, E., Miller, C., Parasuraman, R., & Fern, L. (2010). In Proceedings 
of the Human Factors and Ergonomics Society 54th Annual Meeting (pp. 1498–1502). Santa Monica, CA: 
Human Factors and Ergonomics Society.
Sheridan, T. B., & Verplank, W. L. (1978). Human and computer control of undersea teleoperators. Cambridge: 
Massachusetts Institute of Technology, Man-Machine Systems Lab.
Simons, D. J., & Rensink, R. A. (2005). Change blindness: Past, present, and future. Trends in Cognitive Sciences, 
9, 16–20.
Sirouspour, S. (2005). Modeling and control of cooperative teleoperation systems. IEEE Transactions on Robot-
ics, 21, 1220–1225.
Squire, P., Trafton, G., & Parasuraman, R. (2006). Human control of multiple unmanned vehicles: Effects of 
interface type on execution and task switching times. In ACM Conference on Human–Robot Interaction 
(pp. 26–32). New York, NY: ACM.
Squire, P. N., & Parasuraman, R. (2010). Effects of automation and task load on task switching during human 
supervision of multiple semi-autonomous robots in a dynamic environment. Ergonomics, 53, 951–961.
St. John, M., Smallman, H. S., & Manes, D. I. (2005). Recovery from interruptions to a dynamic monitoring 
task: The beguiling utility of instant replay. In Proceedings of the Human Factors and Ergonomics Society 
49th Annual Meeting (pp. 473–477). Santa Monica, CA: Human Factors and Ergonomics Society.
Taïx, M., Flavigné, D., & Ferré, E. (2012). Human interaction with motion planning algorithm. Journal of Intel-
ligent & Robotic Systems, 67, 285–306.
Tambe, M. (1997) Towards flexible teamwork. Journal of Autonomous Agents and Multiagent Systems, 7, 83–124.

---
**[Page 43]**

Human Interaction	
173
Tambe, M., Scerri, P., & Pynadath, D. V. (2002). Adjustable autonomy for the real world. Journal of Artificial 
Intelligence Research, 17, 171–228.
Trouvain, B., Schlick, C., & Mevert, M. (2003). Comparison of a map- vs. camera-based user interface in a 
multi-robot navigation task. IEEE International Conference on Systems, Man and Cybernetics, 4, 3224–
3231.
Trouvain, B., & Wolf, H. L. (2002). Evaluation of multi-robot control and monitoring performance. In Pro-
ceedings of the 11th IEEE International Workshop on Robot and Human Interactive Communication (pp. 
111–116). New York, NY: IEEE.
Tso, K., Tharp, G., Tai, A., Draper, M., Calhoun, G., & Ruff, H. (2003). A human factors testbed for command 
and control of unmanned air vehicles. In Proceedings of the 23rd Digital Avionics Systems Conference (pp. 
1–12). New York, NY: IEEE.
Ulam, P., Endo, Y., Wagner, A., & Arkin, R. (2007, April). Integrated mission specification and task alloca-
tion for robot teams-design and implementation. In 2007 IEEE International Conference on Robotics and 
Automation (pp. 4428–4435). New York, NY: IEEE.
Valero, A., Saracini, C., de la Puente, P., Rodriguez-Losada, D., & Matia, F. (2010, March/April). Exploratory 
analysis of operator: Robot ratio in search and rescue missions. Paper presented at the 2nd Symposium New 
Frontiers in Human–Robot Interaction, Leicester, UK.
Valero-Gomez, A., de la Puente, P., & Hernando, M. (2011). Impact of two adjustable-autonomy models 
on the scalability of single-human/multiple-robot teams for exploration missions. Human Factors, 53, 
703–716.
Velagapudi, P., Wang, H., Scerri, P., Lewis, M., & Sycara, K. (2009). Scaling effects for streaming video vs. 
static panorama in multirobot search. In International Conference on Intelligent Robots and Systems (pp. 
5874–5879). New York, NY: IEEE.
Wagner, A. R., Endo, Y., Ulam, P., & Arkin, R. C. (2006). Multi-robot user interface modeling. Distributed 
Autonomous Robotic Systems, 7, 237–248.
Wang, H., Kolling, A., Abedin, S., Lee, P., Chien, S., Lewis, M.,  . . . Sycara, K. (2011). Scalable target detection 
for large robot teams. In Proceedings of the 6th ACM/IEEE International Conference on Human–Robot 
Interaction (pp. 363–370). New York, NY: IEEE.
Wang, J., & Lewis, M. (2007a). Assessing coordination overhead in control of robot teams. In Proceedings of 
2007 IEEE International Conference on Systems, Man, and Cybernetics (pp. 2645–2649). New York, NY: 
IEEE.
Wang, J., & Lewis, M. (2007b, March). Human control for cooperating robot teams. In 2nd ACM/IEEE Inter-
national Conference on Human–Robot Interaction (pp. 9–16). New York, NY: ACM.
Wang, J., Lewis, M., Hughes, S., Koes, M., & Carpin, S. (2005). Validating USARsim for use in HRI research. 
In Proceedings of the Human Factors and Ergonomics Society 49th Annual Meeting (pp. 457–461). Santa 
Monica, CA: Human Factors and Ergonomics Society.
Whetten, J., Goodrich, M., & Guo, Y. (2010). Beyond fan-out: Towards multi-operator supervisory control. In 
Proceedings of the IEEE International Conference on Systems, Man, and Cybernetics (pp. 2008–2015). New 
York, NY: IEEE.
Woods, D. (1984) . Visual momentum: A concept to improve the cognitive coupling of person and computer. 
International Journal of Man–Machine Studies, 21, 229–244.
Woods, D., Tittle, J., Feil, M., & Roesler, A. (2004). Envisioning human–robot coordination in future opera-
tions. IEEE Transactions on Systems, Man, and Cybernetics, Part C, 34, 210–218.
Yanco, H., & Drury, J. (2004). Classifying human–robot interaction: An updated taxonomy. Proceedings of the 
IEEE Conference on Systems, Man and Cybernetics, 3, 2841–2846.
Yang, L., Kreamer, W., Adams, M., Carr, F., Guerra, C., Page, L.,  . . . Falcone, C. (2004, September). Hierarchi-
cal planning for large numbers of unmanned vehicles. Paper presented at the AIAA 1st Intelligent Systems 
Technical Conference, Chicago, IL.
Xu, Y., Dai, T., Sycara, K., & Lewis, M. (2010). Service level differentiation in multi-robots control. In 2010 
IEEE/RSJ International Conference on Intelligent Robots and Systems (pp. 2224–2230). New York, NY: 
IEEE.
Xu, Y., Scerri, P., Yu, B., Okamoto, S., Lewis, M., & Sycara, K. (2005). An integrated token-based algorithm for 
scalable coordination. In Fourth International Joint Conference on Autonomous Agents and Multiagent 
Systems (pp. 407–414).

---
**[Page 44]**

174 	
Reviews of Human Factors and Ergonomics, Volume 9
Zheng, K., Glas, D. F., Kanda, T., Ishiguro, H., & Hagita, N. (2013). Designing and implementing a human–
robot team for social interactions. IEEE Transactions on Systems, Man, and Cybernetics: Systems, 43, 
843–859.
ABOUT THE AUTHOR
Michael Lewis is a professor of information sciences and intelligent systems at the Uni-
versity of Pittsburgh. He received his PhD from the Georgia Institute of Technology in 
1986. His current research focuses on human–robot interaction. His group at the Uni-
versity of Pittsburgh has developed a number of widely used research tools, including 
USARSim, a robotic simulation developed under National Science Foundation funding, 
adopted for RoboCup competition and available from SourceForge; and CaveUT, widely 
used software for inexpensive immersive displays.
