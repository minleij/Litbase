# MUSIM Fern

*Source file: MUSIM_Fern.pdf — 29 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

NASA/TP—2018–219875
Multi-Operator Multi-UAV (MOMU) Control: 
Exploring the Influence of Sensor Tools and 
Playbook Task Delegation
Lisa Fern
NASA Ames Research Center
Mark Draper
Air Force Research Laboratory
Tal Oron-Gilad
Ben-Gurion University of the Negev
Robert J. Shively
NASA Ames Research Center
Talya Porat
Ben-Gurion University of the Negev & King’s College London
Michal Rottem-Hovev
Israeli Ministry of Defense
Jacob Silbiger
Synergy Integration
March 2018

---
**[Page 2]**

ii
NASA STI Program…in Profile
Since its founding, NASA has been dedicated 
to the advancement of aeronautics and space 
science. The NASA scientific and technical 
information (STI) program plays a key part in 
helping NASA maintain this important role.
The NASA STI program operates under the 
auspices of the Agency Chief Information 
Officer. It collects, organizes, provides for 
archiving, and disseminates NASA’s STI. The 
NASA STI program provides access to the 
NTRS Registered and its public interface, the 
NASA Technical Reports Server, thus 
providing one of the largest collections of 
aeronautical and space science STI in the 
world. Results are published in both non-NASA 
channels and by NASA in the NASA STI 
Report Series, which includes the following 
report types:
• TECHNICAL PUBLICATION. Reports 
of completed research or a major 
significant phase of research that present 
the results of NASA programs and 
include extensive data or theoretical 
analysis. Includes compilations of 
significant scientific and technical data 
and information deemed to be of 
continuing reference value. NASA 
counterpart of peer-reviewed formal 
professional papers but has less stringent 
limitations on manuscript length and 
extent of graphic presentations.
• TECHNICAL MEMORANDUM. 
Scientific and technical findings that are 
preliminary or of specialized interest, e.g., 
quick release reports, working papers, and 
bibliographies that contain minimal 
annotation. Does not contain extensive 
analysis.
• CONTRACTOR REPORT. Scientific and 
technical findings by NASA-sponsored 
contractors and grantees.
• CONFERENCE PUBLICATION. 
Collected papers from scientific and 
technical conferences, symposia, 
seminars, or other meetings 
sponsored or co-sponsored by NASA.
• SPECIAL PUBLICATION. 
Scientific, technical, or historical 
information from NASA programs, 
projects, and missions, often 
concerned with subjects having 
substantial public interest.
• TECHNICAL TRANSLATION. 
English-language translations of 
foreign scientific and technical 
material pertinent to NASA’s 
mission.
Specialized services also include creating 
custom thesauri, building customized 
databases, and organizing and publishing 
research results.
For more information about the NASA STI 
program, see the following:
• Access the NASA STI program home
page at http://www.sti.nasa.gov
• E-mail your question via to 
help@sti.nasa.gov
• Phone the NASA STI Help Desk at 
(757) 864-9658
• Write to:
NASA STI Information Desk
Mail Stop 148
NASA Langley Research Center
Hampton, VA 23681-2199

---
**[Page 3]**
*(This page contains a figure/chart/image not captured in text)*

iii
NASA/TP—2018–219875
Multi-Operator Multi-UAV (MOMU) Control: 
Exploring the Influence of Sensor Tools and 
Playbook Task Delegation
Lisa Fern
NASA Ames Research Center
Mark Draper
Air Force Research Laboratory
Tal Oron-Gilad
Ben-Gurion University of the Negev
Robert J. Shively
NASA Ames Research Center
Talya Porat
Ben-Gurion University of the Negev & King’s College London
Michal Rottem-Hovev
Israeli Ministry of Defense
Jacob Silbiger
Synergy Integration
National Aeronautics and
Space Administration
Ames Research Center
Moffett Field, California
March 2018

---
**[Page 4]**

iv
Trade name and trademareks are used in this report for 
identification only. Their usage does not constitute an 
official endoresement, either expressed or implied, by the 
National Aeronautics and Space Administration.
Available from:
NASA STI Program
STI Support Services
Mail Stop 148
NASA Langley Research Center
Hampton, VA 23681-2199
This report is also available in electronic form at http://www.sti.nasa.gov 
or http://ntrs.nasa.gov/

---
**[Page 5]**

v
Table of Contents
Acronyms and Definitions...................................................................................................... vi
List of Figures and Tables ...................................................................................................... vii
1.0 Introduction ....................................................................................................................... 2
2.0 Method............................................................................................................................... 4
2.1 Participants.................................................................................................................. 4
2.2 Multiple UAV Simulator (MUSIM).......................................................................... 4
2.3 Mission Scenarios....................................................................................................... 6
2.4 Mission Tasks.............................................................................................................. 7
2.5 Experimental Design .................................................................................................. 8
2.6 Procedure..................................................................................................................... 12
3.0 Measures............................................................................................................................ 13
3.1 Objective Performance ............................................................................................... 13
3.2 Subjective Performance.............................................................................................. 13
4.0 Results................................................................................................................................ 13
4.1 Objective Performance ............................................................................................... 13
4.2 Subjective Performance.............................................................................................. 16
5.0 Discussion.......................................................................................................................... 16
5.1 Control......................................................................................................................... 16
5.2 UAV Level .................................................................................................................. 17
5.3 Area of Operations...................................................................................................... 17
6.0 Conclusion......................................................................................................................... 18
References................................................................................................................................ 20

---
**[Page 6]**

vi
Figures and Tables
Figure 1. The MUSIM display interface in the 1:5 oerator to UAV configuration ............ 5
Figure 2. The Connexion SpaceExplorer input device ......................................................... 6
Figure 3. The two AOs consisting of a high-density urban area with POI Echo and 
a low-resolution suburban area with Route Zulu ................................................. 7
Figure 4. Examples of civilian, humvee, and HVT vehicles................................................ 7
Figure 5. The tools interface in the active sensor window with buttons for LOS, 
Maintain, and Coupling ......................................................................................... 9
Figure 6. The LOS tool with current line of sight symbology and predictive castling....... 10
Figure 7. Two UAVs coupled together sharing the same stare point and loiter waypoint. 11
Figure 8. The Playbook interface located under the Plays tab in the MFD......................... 12
Figure 9. Prosecution time by Control and AO..................................................................... 14
Figure 10. Civilian marking accuracy by UAV Level and AO............................................ 15
Table 1. Composite Score Matrix........................................................................................... 13

---
**[Page 7]**

vii
Acronyms and Definitions
2D......................................2 dimensional
AO.....................................Area of Operation
CPU...................................central processing unit
deg.....................................degree
DOF...................................degree of freedom
FLTK.................................Flash Light Toolkit
GCS...................................Ground Control Stations
GLMM..............................General Linear Mixed Model
GUI....................................graphical user interface
HVT ..................................High Value Target
LSD...................................least significant difference
LOS...................................Line of Sight
M .......................................mean
MFD..................................multi-function display
mIRC.................................Internet Relay Chat
MOMU..............................multi-operator multi-UAV
MOUT...............................Military Operations In Urban Terrain
MUSIM.............................Multiple UAV Simulator
NASA................................National Aeronautics and Space Administration
NASA-TLX......................NASA-Task Load Index
POI ....................................Points of Interest
RSTA ................................reconnaissance, surveillance, and target acquisition
s.........................................seconds
SD......................................standard deviation
SME ..................................Subject Matter Expert
UAV..................................unmanned aerial vehicle

---
**[Page 8]**

1
Multi-Operator Multi-UAV (MOMU) Control:
Exploring the Influence of the Sensor Tools and
Playbook Task Delegation
Lisa Fern1, Mark Draper2, Tal Oron-Gilad3, Robert J. Shively1, Talya Porat4, Michal 
Rottem-Hovev5, Jacob Silbiger6
New concepts of operations for Unmanned Aerial Vehicles (UAVs) will require a change from the 
current 2:1 operator to vehicle crew configuration. One particular control paradigm, largely driven 
by logistics, manpower, and training burdens, as well as the desire to force multiply, involves a 
single operator simultaneously managing multiple UAVs. This mode of operations has shown to 
significantly increase cognitive workload and decrease situation awareness, as operators are 
required to simultaneously attend to multiple sources of information. One potential way to mitigate 
potential drawbacks of multi-vehicle control by a single operator is to migrate to a multi-operator 
multi-UAV (MOMU) crew configuration, whereby M operators control N (> M) vehicles. This type 
of crew configuration can be organized in several ways to dynamically manage cognitive workload, 
match operator qualifications and skills to mission requirements, increase utilization of available 
assets, and thereby achieve maximum force multiplication.
The present experiment examined task performance in a simulated MOMU environment and 
evaluated the potential benefits of sensor management aids (“Tools”) as well as integrated sensor 
and flight automation (“Plays”) compared to a fully manual condition (“Manual”). Tools support 
the operator by facilitating rapid understanding and management of sensor information, while the 
Plays support the operator by offloading/ automating subtasks. Six pairs of participants were 
recruited for this study and tasked with sharing a pool of UAVs in order to conduct reconnaissance, 
surveillance, and target acquisition missions in adjacent Areas of Operation. Participants were 
given four tasks to accomplish, in order of priority: 1) prosecute High Value Targets; 2) 
identify/track targets (military vehicles); 3) identify/mark civilian vehicles; and 4) respond to chat 
messages. Performance on the mission tasks was measured in terms of accuracy and reaction time. 
A composite mission score was also calculated using a payoff matrix that weighted each task 
according to priority. The results indicate that Playbook demonstrated better performance overall 
with higher accuracy rates and the highest composite score compared to Tools and Manual. The 
implications of these results to supporting future MOMU concepts of operations is discussed.
 1 NASA Ames Research Center.
2 United States Air Force Research Laboratory.
3 Ben-Gurion University of the Negev. 4 Ben-Gurion University of the Negev, and King’s College London. 5 Israeli Ministry of Defense.
6 Synergy Integration.

---
**[Page 9]**

2
1.0 Introduction
New concepts of operations for Unmanned Aerial Vehicles (UAVs) will require a change from the 
current 2:1 operator to vehicle crew configuration. One particular control paradigm, largely driven 
by logistics, manpower, and training burdens, as well as the desire to force multiply, involves a 
single operator, or team of operators, simultaneously managing multiple UAVs. An increasing body 
of evidence has examined the effectiveness of a single operator controlling multiple UAVs across 
several different applications (e.g., Miller & Parasuraman, 2007; Nehme, Scott, Cummings, & 
Furusho, 2006; Cummings, Nehme, & Crandall, 2006; Cummings, Bruni, Mercier, and Mitchell; 
Cummings, Andrew, & Hart, 2010; Draper, Calhoun, Ruff, Mullings, Lefebre, Ayala, & Wright, 
2008; and Fern, Shively, Draper, Cooke, Oron-Gilad, & Miller, 2001). However, this mode of 
operations often significantly increases cognitive workload and decreases situation awareness 
because operators are required to simultaneously attend to multiple sources of information. Previous 
research has shown that switching between information sources can disrupt operator performance 
(Draper et al., 2008) and it has been claimed that as the autonomy of the video feed source increases 
and interfaces improve, switch costs gradually become the bottleneck which limits the number of 
source feeds that a single operator can manage or be aware of (Hancock et al., 2007). Furthermore, 
previous studies where the operator is responsible for controlling two to four UAVs at once have 
demonstrated that such setups (mainly the tri-UAV or more) are not efficient because the operators 
demonstrate difficulties in processing information from three or more separate sources and therefore 
do not utilize all assets to their full capacity (Porat et al., 2016). 
One possible way to mitigate the potential drawbacks of multi-vehicle control by a single operator is 
to migrate to a multi-operator multi-UAV (MOMU) crew configuration, whereby M operators control 
N (> M) vehicles. This type of crew configuration can be organized in several ways to dynamically 
manage cognitive workload, match operator qualifications and skills to mission requirements, 
increase utilization of available assets, and thereby achieve maximum force multiplication. One 
configuration might consist of operators with similar skill sets where all tasks are shared between 
them equally, offloading to other teammates when changes in the mission environment create 
workload spikes. Other configurations might include operators with different specialized skill sets 
where each teammate is responsible for a particular aspect of the UAV team they are controlling (e.g. 
one operator may be responsible for monitoring health and status, while another manages a 
specialized payload, etc.). Whatever the crew configuration, MOMU potentially allows for dynamic 
task and expertise sharing across team members, resulting in enhanced collaboration.
However, several challenges exist before the MOMU control paradigm can be effectively achieved. 
Hardware-related challenges include increased automation, the establishment of robust distributed 
network control architecture with required communication links and bandwidth, as well as the 
development of interoperability standards for messages and interfaces. There are also many human 
factors challenges involved, including a need to better equip each single operator to 
control/supervise multiple vehicles, a standardized method for vehicle handovers, and the 
development of new collaboration aids to facilitate MOMU operations. Previous multi-vehicle 
control research has explored a variety of interface solutions with varying degrees of success (e.g. 
Brzezinski, Seybold, & Cummings, 2007; Ruff, Narayanan, & Draper, 2002; Saqer, de Visser, 
Emfield, Shaw, & Parasuraman, 2011; and Schulte, Meitinger, & Onken, 2009). Team collaboration 
enhancement has also been studied in UAV applications, mainly in the context of multiple operators

---
**[Page 10]**

3
operating a single vehicle (e.g., Cooke et al. 2006) but not, to the best of our knowledge, in the 
context of sharing as in MOMU.
Of particular concern is the increased requirement of attentional shifts. Operators controlling 
multiple vehicles need to selectively attend across many sources of information, requiring frequent 
shifting of attention. This is a time-critical, cognitively demanding task. The collaborative nature of 
the MOMU paradigm adds additional sources of information to attend to, including who is 
responsible for which aircraft, target, or even mission. The quality of these attentional shifts has a 
vital effect on mission accomplishment, situation awareness, workload, and team communication 
(Oron-Gilad, et al, 2011). 
One can envision many potential interface aids, or tools, to improve human performance in MOMU 
operations. Two such categories of tools include: 1) sensor management aids designed to support 
task switching and assist the operator in rapidly building situation awareness to become 
operationally effective; and 2) integrated sensor/flight control automation that significantly reduces 
operator control input requirements by delegating a series of tasks via the concept of calling a 
concise ‘play.’
Sensor management aids facilitate task switching and coordination. These tools focus primarily on 
helping the operator simultaneously manage multiple sensors and provide decision support for 
selecting appropriate sensors for mission tasks. Previous studies have yielded mixed results on 
performance. Structured interviews with experienced Subject Matter Experts (SMEs) have provided 
evidence for the value of sensor management aids in reducing operator workload and improving 
mission performance, particularly when they provide clear decision aiding for facilitating specific 
task switching (Porat, Oron-Gilad, Silbiger, & Rottem-Hovev, 2010). However, these tools have had 
more uncertain effectiveness in improving overall mission performance (Oron-Gilad, Porat, Silbiger, 
& Rottem-Hovev, 2011). The three sensor management tools examined in this study (Line of Sight 
with Castling, Coupling, and Maintain Video Coverage) were developed specifically to facilitate ongoing missions where acquiring UAVs, delegating UAVs to specific tasks, and switching is necessary 
(Porat et al., 2010; Porat, Oron-Gilad, Silbiger, & Rotem-Hovev, 2011; Oron-Gilad et al., 2011). 
Integrated sensor and flight control automation can be provided through “Playbook,” a 
delegation control human-automation interface that allows users to assign pre-determined goals 
or tasks to individual or multiple UAVs through the calling of concise “plays” (Miller, 
Goldman, Funk, Wu & Pete, 2005). Playbook implementation allows operators to quickly 
delegate high-level tasks, such as monitoring Points of Interest (POIs) or roads, so that they can 
then attend to other important tasks (e.g. identifying targets in sensor imagery). Recent studies 
examining the use of Playbook to control multiple UAVs has yielded performance benefits on 
mission tasks and operator workload when compared with manual or single-UAV automation 
(Fern and Shively, 2009; Shaw, et al., 2010; Miller, Shaw, Hamell, Emfield, Musliner, De 
Visser, & Parasurman, 2011).
The present experiment examined task performance in a simulated MOMU environment and 
evaluated the potential benefits of sensor management aids (“Tools”) as well as integrated sensor 
and flight automation (“Plays”). Tools support the operator by facilitating rapid understanding and 
management of sensor information, while the Plays support the operator by offloading/automating 
subtasks. Although this experiment was mainly conceived as an initial exploration of the novel 
MOMU operational concept, three main hypotheses were evaluated. First, it was hypothesized that

---
**[Page 11]**

4
both Plays and Tools would improve operator task performance over the baseline condition where 
no aids were provided. In particular, the value of Plays would be more task-specific according to 
the suitability of the available Plays, whereas Tools would aid task performance more generally 
across a trial. 
2.0 Method
2.1 Participants
Six pairs of participants were recruited for this study; each pair was assigned as a MOMU team. All 
twelve participants were male with an age range of 19 to 25 years (M = 21; SD = 3.8). Due to the 
strong teaming and communication component of the study, participants were recruited in pairs of 
pre-existing relationships, i.e., friends or co-workers7. Given the demonstrated association between 
video game playing and performance on these sorts of tasks (Bavelier, Achtman, Mani & Focker, 
2012; Strobach, Frensch, & Schubert, 2012), participants were also required to currently play video 
games a minimum of ten hours per week (mean 14.2 hours). Participants were required to be righthanded and have normal or corrected-to-normal vision. None of the participants had prior military 
experience, piloting experience, or UAV operation experience.
2.2 Multiple UAV Simulator (MUSIM)
The simulation testbed used for this study was MUSIM, an Army-developed multi-UAV control 
station simulation testbed used for a wide variety of UAV-related research (Fern & Shively, 2011; 
Fern & Shively, 2009; Shively, Neiswander, & Fern, 2011). The simulation was generated with a 
quad-core central processing unit (CPU) using an NVidia GeForce® 8800 GTX video card and 2GB 
RAM. A 30" Apple Cinema Display provided a display resolution of 2560x1600 and 24-bit color. 
MUSIM software includes the Suse Linux 10.3 operating system, OpenSceneGraph for graphics,
and Flash Light Toolkit (FLTK) for the graphical user interface (GUI). Mission scenarios were 
generated by MAK Technologies’ VR Forces. A visual database was created using Creator Terrain 
Studio 2.0.2 and Creator 2.5.1. Terrain imagery was obtained from U.S. Geological Survey satellite 
photography. The simulation utilized 30-meter elevation data with 45-meter texture data in the lower 
resolution areas and 0.7-meter texture data in the high-resolution areas. A generic flight control 
model emulated up to five notional, tactical fixed-wing UAVs for this simulation. Airspeed and 
altitude were fixed for all UAVs in all conditions.
The MUSIM operator interface supported both mission/flight management as well as sensor 
management functions associated with the UAVs under control. The mission/flight management 
interface populated roughly the left half of the display and consisted of a 2D top-down map view 
with task-relevant overlay symbology and waypoint editing GUI, a Multi-Function Display (MFD) 
window, and an Internet Relay Chat (mIRC) room display (see Figure 1). An optical mouse was 
used for navigation of operator control panels in the operator interface and a keyboard was used for 
chat responses.
 7 There are costs and benefits to using people who already know each other, prior interpersonal experience 
lets teams concentrate more effectively on task performance by fostering coordination and integration 
improved team mental models and sense of stability, but it may also affect the pattern of delegation among 
members (see for example, Harrison, Mohammed, McGrath, Florey & Vanderstoep, 2003).

---
**[Page 12]**
*(This page contains a figure/chart/image not captured in text)*

5
Figure 1. The MUSIM display interface in the 1:5 operator to UAV configuration. This figure shows 
the MUSIM tactical map display (top left), active sensor window (top right), secondary sensor 
windows (bottom right), MFD (bottom center), and mIRC window (bottom left).
The right half of the MUSIM operator interface was devoted to sensor management and consisted of 
three or five sensor views (depending on the number of UAVs being controlled) along with sensorrelated functionality. The simulated sensor payload on each UAV was gimbaled electro-optical 
video with 360 deg pan capability, +45/-110 pitch limits, and zoom capabilities from 16 to 2 deg 
field of view. Sensor slew rate was set at 60 deg/second. The gimbaled sensor was operatorcontrolled via a 6-DOF Connexion SpaceExplorer® input device (Figure 2), which has been shown to 
be an effective means for controlling sensor viewpoint (Flaherty, Fern, Turpin, & Scheff, 2012). The 
SpaceExplorer was also configured with dedicated buttons for sensor-related functions such as: 
stare, mark, autotrack, fire, and lase.

---
**[Page 13]**
*(This page contains a figure/chart/image not captured in text)*

6
Figure 2. The Connexion SpaceExplorer input device used to control the UAV payloads/sensors.
In this experiment, two MUSIM Ground Control Stations (GCSs) were networked together to share 
control of the available UAVs. While both GCSs received payload and flight data for all UAVs in 
the simulation environment, only one GCS at a time could have control of any particular UAV and 
manipulate its sensor or flight path. Control of a UAV could be requested and transferred through 
the operator interface. 
2.3 Mission Scenarios 
The overall mission context involved a team of two networked participants sharing a pool of UAVs 
in order to conduct reconnaissance, surveillance, and target acquisition (RSTA) missions in adjacent 
Areas of Operation (AOs). 
A total of six, eight-minute experimental scenarios were developed for this experiment. Each 
scenario encompassed the two adjacent AOs. These two AOs were: 1) a downtown, urban area 
consisting of high-resolution 3D cultural features; and 2) a larger suburban area consisting of 
lower-resolution 2D imagery. The two AOs are shown in Figure 3. Events in the downtown area
occurred at POI Echo, a building entrance marked on the map and in the sensor window with a 
single green dot. Events in the suburban area occurred along Route Zulu, a stretch of roadway 
marked on the map display and in the sensor window with a series of white dots. Scenarios 
included two main types of vehicle events: civilian (friendlies) and military (targets). Civilian 
vehicles were cars, trucks, and vans of various colors. Military vehicles were camouflage-colored 
humvees. Vehicle events occurred when a civilian or military vehicle drove out of POI Echo or 
onto Route Zulu. In addition, military vehicles could suddenly ‘acquire’ a weapon and become a 
High Value Target (HVT) (i.e. a gun would instantly appear in the truck bed of the humvee). 
Examples of a civilian, humvee, and HVT are shown in Figure 4. The numbers of events were 
balanced across each AO for each scenario. Humvee and HVT event frequencies were varied 
between scenarios to reduce predictability. Scenario events consisted of 30 civilian, 6 to 8 military, 
and 2 to 4 HVTs per scenario.

---
**[Page 14]**
*(This page contains a figure/chart/image not captured in text)*

7
Figure 3. The two AOs consisting of a high-density urban area with POI Echo (left) and a lowresolution suburban area with Route Zulu (right) identified by POI (green) and route (white) 
markers.
Figure 4. Examples of civilian (left), humvee (center), and HVT (right) vehicles.
2.4 Mission Tasks
At the beginning of each scenario, participant teams were assigned to their respective AOs and a 
fixed number of UAVs to share. The assigned AOs were alternated between the team members 
across trials. When assigned the downtown area, the participant was required to monitor POI Echo 
for exiting vehicles. The participant assigned to the suburban area was required to monitor Route 
Zulu for vehicles driving on it. Participants were given four tasks to accomplish, in order of priority: 
1) prosecute HVTs; 2) identify/track targets (military vehicles); 3) identify/mark civilian vehicles;
and 4) respond to chat messages. 
To mark a civilian vehicle as friendly, the participant centered a UAV sensor on the vehicle and 
pressed the “mark” button on the SpaceExplorer controller. A virtual yellow dot then appeared on 
top of the successfully “marked” vehicle. To track a military target, the participant centered a UAV 
sensor on the humvee and pressed the “autotrack” button on the SpaceExplorer. Once autotrack was 
engaged, the camera would stay locked and centered on the vehicle until the vehicle stopped, at 
which point the autotrack would automatically disengage. Participants were required to track the 
military humvee until it stopped or acquired a gun (visible in the truck bed). If the humvee stopped, 
Echo	POI	Marker Zulu	Route	Markers

---
**[Page 15]**

8
the participant could disregard it since it no longer represented a threat. If the target acquired a gun, 
it became a HVT and the participant could then prosecute it (i.e., fire upon it). Prior to prosecuting 
the HVT, participants were required to confirm the identification of it using a second UAV’s 
camera. Once the participant located and tracked the HVT with a second UAV, it could be 
prosecuted. Prosecuting a HVT involved the following steps: 1) place the laser in stand-by mode in 
the weapons menu of the MFD; 2) engage the laser on the target by pressing the “lase” button on the 
SpaceExplorer; 3) put the laser guided missiles in stand-by mode in the weapons menu of the MFD;
and 4) fire the weapon by pressing the “fire” button on the SpaceExplorer controller. The lase would 
not engage and the weapon would not fire if the participant was no longer autotracking the target.
To accomplish these tasks, the team of participants was provided a fixed number of UAVs that they 
could share between them. Both participants could see all of the available UAV sensor windows and 
flight paths in their ground control stations, however only one participant could actively control a 
particular UAV at any time. Each available UAV was assigned to an AO operator at the beginning 
of each scenario, however UAVs could be subsequently transferred between participants using the 
“request” button in the MUSIM sensor windows. Once control of a UAV was requested, the ‘owner’ 
of the UAV had to approve the request. Participants were instructed that UAVs should be handed off 
if the requestor needed it to carry out a task that was of higher priority. Once the request was 
approved, control of the UAV would be instantly handed off to the receiver. UAVs that were not 
currently under control of an AO operator were indicated by red icons in the lower right corner of 
the sensor window as well as on the tail of the aircraft icon on the map display. 
In addition to monitoring for civilian vehicles and military targets, participants had to occasionally 
respond to chat messages directed to their team. This chat task required participants to monitor the 
mIRC chat room window located in the lower left hand corner of the MUSIM interface. The chat 
queries that they responded to were directly related to their missions; for example, how many targets 
they had tracked, how many UAVs they were currently controlling, etc. 
2.5 Experimental Design
The present study utilized a within-subjects, repeated measures design in order to examine the 
effects of different operator interface configurations while conducting RSTA missions in a MOUT 
(Military Operations in Urban Terrain) environment. Three control modes (Control: Manual, Tools, 
Plays) were compared across two levels of available UAVs (UAV Level: 3, 5) and two different 
areas of operation (AO: urban, suburban). Control and UAV Level were counterbalanced. AO and 
UAV Level were blocked by control mode. 
Control Mode. Three modes of control were examined in this experiment: Manual, Tools, and 
Playbook. The Manual, or baseline, condition required participants to manually control both payload 
and flight control aspects of the UAVs under their control. Using the point, click, and drag interface 
in the tactical map display, participants manipulated the flight of each UAV independently through 
use of single waypoint loiters, multiple fly-thru waypoints creating a flight path, or a combination of 
both. The sensor of each UAV was manipulated independently with the SpaceExplorer input device, 
allowing pan, tilt, and zoom capabilities. 
The Tools mode provided additional tools that the participants could use to assist in their mission 
tasks. In particular, these tools were created to facilitate a rapid understanding and management of 
sensor information associated with MOMU operations. Three tools were provided: 1) Line of Sight

---
**[Page 16]**
*(This page contains a figure/chart/image not captured in text)*

9
with Castling (LOS); 2) maintain video coverage (Maintain); and 3) Coupling. Based on previous 
experimentation (Porat et al., 2010; Oron-Gilad et al., 2011) these tools were found to be beneficial 
to operators and also were perceived as the most fundamental tools of the pool-set of tools 
developed and tested. All three tools were manipulated through the use of buttons in the active 
sensor window. The Tools interface is shown in Figure 5. The LOS and Maintain tools also had
redundant buttons on the SpaceExplorer device.
Figure 5. The tools interface in the active sensor window with buttons for LOS (far left), Maintain 
(second from right), and Coupling (far right).
The LOS tool provided the participants with symbology in the sensor windows that allowed them to 
view the line-of-sight vectors (i.e., a line connecting the UAV camera to the point it is viewing on 
the ground) of all UAVs in the simulation environment, which could aid in identifying the most 
proximal sensor to a task. The castling functionality of the LOS tool allowed the participants to 
temporarily view a predicted line-of-sight from all UAV sensors to the center point of each sensor 
window, which could assist in determining which UAVs would have acceptable views of that area if 
its sensor was moved. The LOS tool is shown in Figure 6.

---
**[Page 17]**
*(This page contains a figure/chart/image not captured in text)*

10
Figure 6. The LOS tool with current line-of-sight symbology (left) and predictive castling (right).
The Maintain tool allowed the participants to lock the footprint of any sensor window. By locking 
the footprint, the imagery in the sensor window would appear to maintain the same size even if the 
UAV moved closer toward or farther away from the stare point. This was done by automatically 
adjusting the camera zoom level so that the sensor continuously covered the same area on the 
ground. The expected advantage of this tool was in maintaining consistency in both target area and 
target size, regardless of the current location of the aircraft.
Finally, Coupling allowed the participants to link two or more UAVs together so that they would 
share the same camera stare point so that if the operator moved the camera of one UAV the other 
coupled sensor(s) would follow. This tool simplified coordination of multiple cameras on a single 
POI as well as facilitated manipulation of multiple cameras at one time. Figure 7 shows two UAVs 
coupled together sharing the same stare point and loiter waypoint.

---
**[Page 18]**
*(This page contains a figure/chart/image not captured in text)*

11
Figure 7. Two UAVs (outlined in the lime [upper payload window] and orange [middle right 
payload window]) coupled together sharing the same stare point and loiter waypoint.
The third control mode (Playbook) provided the participants with three “plays” to assist them in 
completing their mission tasks. Plays are a form of UAV automation that allows a user to delegate 
high-level tasks to one or more UAVs. Plays can control both the flight control and sensor behavior 
for multiple UAVs at once. The Playbook interface was located under the “Plays” menu of the MFD 
(Figure 8). Participants were able to assign which UAVs to use or they could allow Playbook to 
choose which UAVs to use from those under the participants’ control. The three plays available to 
the participants were: 1) Surveillance; 2) Route Recon; and 3) Prosecute Target. The Surveillance 
play allowed the participants to assign one or more UAV to monitor one or more POIs. Once a 
Surveillance play was called, the play automation would assign the UAV(s) to loiter and pre-point 
their sensors at the POIs. The Route Recon play allowed participants to assign UAVs to monitor a 
defined route. The assigned UAVs would fly a flight path around the route and slew their sensors 
along it. Route recon fight paths were generated dynamically by the Playbook automation based on 
the location of the assigned UAVs and the route at the time the play was called. Finally, the 
Prosecute Target play assisted the participants in weapons setup for target prosecution. Upon calling 
the play, the assigned UAVs would lock their sensors on the selected target and place both a laser 
and a weapon in standby, which the participants then were required to engage and fire in order to 
complete the prosecution task.

---
**[Page 19]**
*(This page contains a figure/chart/image not captured in text)*

12
Figure 8. The Playbook interface located under the Plays tab in the MFD.
2.6 Procedure
After completing a demographic survey to elicit information, including participants’ gaming and 
media experience, participants were given a training briefing introducing the basic MUSIM 
simulation environment. Participants then completed a guided 12-minute practice scenario at their 
own, non-networked, MUSIM Ground Control Stations (GCSs) to learn how to manipulate the flight 
paths and sensors. These practice scenarios involved four UAVs.
After this initial MUSIM training, participants were given a 30-minute briefing describing the 
specific MOMU mission environment and tasks. Participants then completed four 12-minute training 
scenarios at their networked GCSs to learn how to accomplish each of the four mission tasks as well 
as how to transfer control of UAVs. The participants alternated AOs between practice trials, 
completing two trials in each area. Participants were required to achieve a minimum score of 50% 
on the composite performance score (see below) or the practice trial was repeated.
The experimental trials were blocked by control mode. At the beginning of each experimental block 
participants were given a briefing on the control mode, followed by two practice trials (one in each 
AO). The participants then completed four experimental trials (2 AOs x 2 UAV levels) with that 
control mode. Participants provided a workload rating following each trial, a post-block 
questionnaire following each block, and a post simulation questionnaire at the end of the 
experimental session. Presentation of control mode and number of UAVs was counterbalanced 
across participant teams.

---
**[Page 20]**

13
3.0 Measures
3.1 Objective Performance
Accuracy and reaction time were recorded for the four main mission tasks: prosecute HVTs, track 
military targets, mark civilians, and respond to chat messages. Accuracy was defined as the number 
of correct identifications (of HVT, target, or civilian) or correct answers (to chat queries) out of the 
total possible. Response rate (% answered out of total possible) was also collected for the chat task. 
A composite mission score was also calculated using a payoff matrix that weighted each task 
according to priority. The payoff matrix scoring is shown in Table 1. For all events except HVTs, 
incorrect responses were defined as a missed event. For the HVT event, an incorrect response was 
defined as prosecuting any vehicle that wasn’t a HVT. Participants were shown the matrix during the 
MOMU training briefing and it was kept visible at their testing station. Participants’ composite 
scores were calculated as a percentage of the highest possible score for each mission.
Table 1. Composite Score Matrix
Event Total 
Possible
Points for Correct 
Response
Points 
Subtracted for 
Incorrect 
Response
Prosecute HVT 2–4 +50 -100
Track targets 6–8 +20 -10
Mark civilians 30 +5 -2
Chat response 6 +10 -5
3.2 Subjective Performance
Workload ratings were collected using the NASA Task Load Index (TLX; Hart & Staveland, 1988). 
Self-ratings of performance by task were collected after each control mode block, utilizing a 7-point 
Likert scale. Ratings of “Ease of Use” and “Usefulness for Mission” were collected for each Tool 
and Play. For “Ease of Use” a 7-point Likert scale ranging from “Very Difficult” (1) to “Very Easy” 
(7) was used. “Usefulness for Mission” utilized a 7-point Likert scale ranging from “Not at all 
Useful” (1) to “Very Useful” (7).
4.0 Results
The objective performance and NASA-TLX results were analyzed utilizing a General Linear Mixed 
Model (GLMM) with Control Mode (Manual, Tools, and Playbook), UAV Level (3, 5), and AO 
(Urban, Road) as fixed effects and participants as a random effect. The full factorial model was 
included in the analyses. Results are organized by task priority, followed by the composite score 
analysis. Descriptive statistics for subjective performance and tool use ratings are also provided.
4.1 Objective Performance
Prosecute Target. For prosecution task accuracy, there were significant main effects for Control 
(F(2,140) = 6.38, p < .01 and AO (F(1,140) = 7.30, p < .01). Prosecution accuracy was significantly

---
**[Page 21]**
*(This page contains a figure/chart/image not captured in text)*

14
higher for Manual (M = .562; SE = .06) and Playbook (M = .604; SE = .06) than for Tools (M = 
.323; SE = .06). Prosecution accuracy in the Urban AO (M = .40; SE = .05) was lower than on the 
Road (M = .59; SE = .05). There was also a significant main effect of prosecution time for Control
(F(2,66) = 13.48, p < .001) as well as a significant interaction of Control by AO (F(2,66) = 6.87, p < 
.01). While there were no significant differences in prosecution time among modes in the Road AO,
there was a significant increase in prosecution time in the Urban area (Figure 9), with Manual (M = 
64.50; SE = 4.13) prosecution time nearly twice as long as Tools (M = 32.21; SE = 4.13) and 
Playbook (M = 33.12; SE = 4.13). 
Figure 9. Prosecution time by Control and AO. The Area legend refers to the Urban and Road AOs.
Track Target. There were no significant main effects or interactions of Control, UAV Level, or AO 
on target tracking accuracy. Tracking accuracy was 59%, on average. However, there was a 
significant main effect of AO (F(1,142) = 138.7, p < .0001) on reaction time. Identifying and 
tracking a target was faster in the Urban area (M = 11.44; SE = 1.61) than on the Road (M = 38.25; 
SE = 1.61).
Mark Civilians. There were significant main effects of Control (F(2,132) = 4.00, p < .02), UAV 
(F(1,132) = 14.94, p < .0001), and AO (F(1,132) = 30.16, p < .0001) on accuracy of marking 
civilian vehicles. There was also a significant UAV by AO interaction (F(1,132) = 4.70, p < .032), 
as shown in Figure 10. Participants using Playbook (M = .662, SE = .02) were significantly more 
accurate than in Manual (M = .583; SE = .02) or Tools (M = .596; SE = .02). Participants allocated 
five UAVs were more accurate altogether (68% versus 55% for five and three UAVs, respectively). 
The interaction of UAV by AO implies that participants allocated to five UAVs had an advantage 
over participants allocated to three UAVs mainly in the Urban AO but not the Road AO; participants 
using three UAVs in the Urban area were the least accurate (47%) compared to all other UAV by 
AO combinations. Hence the interaction stemmed mainly from the statistically significant decrease 
in accuracy in the three UAV Urban area condition relative to the three other conditions (three
UAVs and Road 62%, five UAVs and Urban 60%, and five UAVs and Road 70%). For reaction 
time, there was a significant main effect for AO (F(1,131) = 1335.1, p < .0001) and no interactions. 
Marking a civilian target was faster in the Urban area (M = 9.05; SE =1.36) compared to the Road 
(M = 73.70; SE = 1.36).

---
**[Page 22]**
*(This page contains a figure/chart/image not captured in text)*

15
Figure 10. Civilian marking accuracy by UAV Level and AO.
Chat. For chat response rate, there were significant main effects of Control (F(2,129) = 4.76, p < 
.010) and AO (F(1,129) = 4.62, p < .033), with no interactions. Participants using Manual responded 
to significantly more chat messages (M = 64.4%) than using Tools and Playbook (54.4 and 54.8%, 
respectively). Participants in the Urban AO responded to significantly more chat messages (61.1%) 
than those operating on the Road (54.6%). For the chat response accuracy, there was a near 
significant main effect of UAV (F(1,142)=3.73, p < .055). Responses in the five-UAV condition (M
= .61; SE = .03) appeared to be more correct than in the three -UAV condition (M = .52; SE = .03). 
Finally, there was a significant main effect for Control (F(2,130)=3.502, p < .033) on reaction time, 
with no interactions. Responding to a chat query was faster with Playbook (M = 23.6; SE = 2.7) 
compared to Manual (M = 28.4; SE = 2.7) and Tools (M = 32.1; SE = 2.7).
Composite Score. There were significant main effects of Control (F(2,127) = 14.12, p < .0001) and 
UAV Level (F(1,127) = 4.74, p < .031) with no interactions. LSD post hoc tests revealed that 
Manual (M = .616; SE = .036) and Playbook (M = .662; SE = .036) conditions generated 
significantly higher scores than Tools (M = .475; SE = .036) but were not statistically different from 
one another. The availability of three UAVs (M = .552; SE = .033) significantly degraded the score 
compared to five UAVs (M = .617; SE = .033).

---
**[Page 23]**

16
4.2 Subjective Performance
Workload. Analysis of the overall workload ratings revealed no statistically significant effects for 
Control, AO, or UAV. Overall ratings were moderate for all conditions and mean workload
estimates for all conditions were estimated at about 50% of the scale (SE of 2%).
Ease of Use. Ease of Use ratings revealed that both Tools (M = 5.92; SE =1.27) and Plays (M = 
5.83; SE =1.24) were perceived favorably by the participants.
Usefulness for Mission. Usefulness for Mission ratings revealed that both Tools (M = 6.75; 
SE =1.01) and Plays (M = 6.75; SE =1.09) were perceived as useful for mission performance 
by the participants. As also noted in some of the comments given by operators: 
“The tools and plays helped me achieve my missions by making the obstacles easy. I 
developed many strategies; one for each tool. The ‘Maintain Video’ helped me guard 
my building while I was following a target.”
“I found using Playbook should be used when setting up the UAVs for surveillance. 
Coupling was more useful when prosecuting.” 
Thus, participants were able to identify specific mission components where a specific play or tool 
was more beneficial. 
5.0 Discussion
The results associated with each independent variable will be reviewed in turn, starting with Control 
mode and followed by UAV Level and AO.
5.1 Control
For the three sensor tasks (marking, tracking, and prosecuting), Playbook generally appeared to 
demonstrate better performance overall. It was more accurate than Tools (56% vs. 32%) and nearly 
twice as fast than Manual for prosecuting HVTs in the urban AO (33 s vs. 65 s). In addition, it was 
more accurate than both Manual and Tools for marking civilians (66% vs. 58% and 59%, 
respectively). For the chat task, Playbook also had faster reaction times than the other two control 
modes, although Manual had a higher response rate (discussed further below).
When looking at overall mission performance, Playbook scored highest in the composite score 
(66%) along with Manual (61%), compared to Tools (48%). The higher scores for Playbook and 
Manual is likely a result of the high weighting of the prosecute target task in the composite score 
(where they performed comparably) and the low accuracy performance seen with Tools. One 
drawback of the composite score is that reaction time was not taken into account. If considered, the 
advantage of Playbook would be further underscored due to the significantly faster reaction time on 
this task.
The improved mission performance for Playbook was likely due to two main factors: the 
applicability of the plays to mission tasks and the integrated nature of the plays. Each instantiated 
play had a direct relevance to the operators’ tasks. Thus, the utility of each play was almost 
immediately obvious to the operators, encouraging their usage. In fact, all three plays were rated 
highly by the operators for their perceived usefulness to the mission. In addition, the integrated flight 
and sensor control automation allowed for quick configuration of UAVs to relevant tasks, potentially

---
**[Page 24]**

17
offloading workload and enabling attention switching to other tasks. Although the post-trial 
subjective workload ratings failed to reveal a significant difference, the task of marking targets can 
be considered as a secondary task for workload assessment. Thus Playbook’s higher accuracy in that 
task may be indicative of increased spare capacity. Along the same line of reasoning, the faster 
reaction times to chat messages for Playbook provides further evidence to this possibility.
Conversely, the relevance of Tools to each mission task was less specific and therefore it was likely 
less clear than Playbook in terms of how to best implement the available capabilities. This is 
somewhat confirmed by low perceived usefulness for the mission for both the Castling component 
of the LOS tool and the Maintain tool, despite comparable ease of use ratings to the plays. The 
poorer accuracy performance of Tools on both the prosecute and marking tasks confirms previous 
findings that Tools are less effective when their immediate implication to the task is not clear and 
where there is a significant learning curve for developing strategic knowledge for how to best
employ the Tool (Oron-Gilad et al., 2011). Furthermore, despite being rated as easy to use overall, 
post simulation ratings indicate that the participants found the Tools less useful than the plays for the 
mission tasks and many felt they actually degraded prosecution performance. 
The Manual mode resulted in mixed performance. Accuracy was near that of Playbook—which 
indicates that the task could be successfully completed without the use of plays or tools. However, 
the increased reaction times indicate that significantly more effort was required in the Manual mode 
compared to Playbook. Considering chat as a secondary task, slightly more chat messages were 
responded to in Manual mode (less than one more on average than Tools and Playbook). However, 
Manual failed to produce more correct responses compared to the other control modes. The finding 
that more chat messages were responded to in Manual compared to Tools and Plays is contradictory 
to the increased reaction times needed in this control mode (which indicate reduced excess capacity). 
One explanation is that the Manual mode required more operator interaction and a wider scan 
pattern with the MUSIM interface, whereas the Playbook and Tools modes resulted in more operator 
attention being directed at the sensor tasks. However, given the lower overall performance of Tools, 
this attention may have been directed toward further exploring the applicability of the tools versus 
effective utilization.
5.2 UAV Level
For the two most critical tasks, tracking and prosecuting HVTs, there were no significant differences 
between number of UAVs available. However, five UAVs showed significant accuracy 
improvements over three UAVs on both of the other two tasks (marking civilians and responding to 
chat messages). These findings suggest effective prioritization of available resources to highest 
priority tasks; operators tasked available UAVs first toward accomplishing tracking and prosecuting 
of HVTs while marking and responding to chat messages were not fully attended to unless 
additional resources were available. Given that workload was rated to be very manageable even in 
the five-UAV condition, it appears there is enough spare capacity to support adding more UAVs to 
these operations.
5.3 Area of Operations 
The observed findings for the AOs were to be expected given the characteristics of each area. The 
urban area consisted of a single point of observation whereby all vehicles appeared in the same 
location before eventually dispersing into the larger urban area with other distractor vehicles, 
facilitating quick detection and identification of civilians and targets in the urban AO. This resulted

---
**[Page 25]**

18
in faster reaction times for all three sensor tasks. Conversely, while the road took longer to search 
due to the larger area, vehicles persisted in that AO longer. This resulted in higher accuracy for both 
prosecuting targets and marking civilians since they were easy to identify and available for a longer 
period of time. 
AO appears to have some influence on the impact of UAV Level and Control Mode. While five
UAVs improved accuracy on the marking civilian task, that improvement was most pronounced on 
the road. This finding is not surprising given the difference in persistence of civilian vehicles on the 
road compared to the urban AO described above. The different characteristics of the two AOs also 
interacted with the effectiveness of the Control Modes on the prosecute task. While there was no 
significant difference in reaction time between Control Modes on the road, Tools and Playbook had 
significantly shorter reaction times compared to Manual in the urban AO. This is likely due to the 
difficulty of acquiring the HVT with the second UAV in an area densely populated with distractor 
targets and obscured by tall buildings. Tools and Playbook added the functionality of sharing sensor 
location information to quickly acquire the HVT with the second required UAV. 
6.0 Conclusion
Overall, potential benefits associated with the MOMU concept of operations appear to be supported 
by this study. Operators were able to work together, sharing a pool of assets to accomplish their 
respective missions. As the highest priority task shifted from one operator to the other, they were 
able to dynamically shift resources to address the most pressing need.
The hypothesized value of task-specific plays was confirmed with this study. The ability to delegate 
combined flight and sensor automation to rapidly configure assets to support the mission enables 
operator attention to be redirected to additional perception and identification tasks. This is ideally 
suited for supervisory control and especially MOMU operations where frequent task switching 
occurs and assets need to be configured quickly to respond to dynamic situations. However, caution 
must be used in the application of a Playbook-like capability—the benefit of Playbook in this 
experience was directly linked to the suitability of the available plays to the operational 
environment. Playbook is more likely to be useful when similar operational tasks are regularly 
executed such that play automation can be developed to match those tasks. In more dynamic 
environments where tasks change frequently, a small set of plays are unlikely to be a good match to 
the situation and thus their benefit may be less certain and the ability to easily modify or adapt play 
automation becomes critical to their effectiveness.
Although not demonstrated in this study, Tools also have the potential to significantly aid 
supervisory control tasks. From the subjective data it is evident (Table 1) that participants thought 
that the Tools were useful and effective, however, they identified less opportunities in the 
scenarios to utilize them. This may be attributed at least in part to their inexperience in the task, 
thus failing to see the situations where they could have benefited from use of tools. However, 
additional efforts should be made to increase the intuitiveness and task-specific benefits of 
candidate tools as well as appropriate training on how to effectively utilize the more generic 
sensor management support Tools.
One potential drawback of the two MOMU aids presented in this study is the tendency for 
participants to exhibit tunneling effects (in the form of lower response rates to chat messages) when 
using these tools compared to the manual control mode. However, it is unclear if this was a result of

---
**[Page 26]**

19
participants’ aforementioned lack of proficiency at using the tools, a tendency that might diminish as 
participants became more expert at tool utilization. Again, the need for appropriate and sufficient 
training on new operator aids is critical.
Overall, the results clearly indicate that operators were able to achieve better performance when 
more assets were available. However, performance was still low while workload remained 
manageable, suggesting that additional resources could be successfully applied to support mission 
operations. Future research should explore the tradeoff between increased mission performance and 
higher workload when more assets are introduced.

---
**[Page 27]**

20
References
Bavelier, D., Achtman, R. L., Mani, M., & Föcker, J. (2012). Neural bases of selective attention in 
action video game players. Vision research, 61, 132–143.
Brzezinski, A. S., Seybold, A.L., & Cummings, M. L. (2007). Decision support visualizations for 
schedule management of multiple unmanned aerial vehicles. Presented at the AIAA 
InfoTech@Aerospace, Rohnert Park, CA.
Cummings, M.L., Clare, A. & Hart, C. (2010). The role of human-automation consensus in multiple 
unmanned vehicle scheduling. Human Factors, 52(1), 17–27.
Cummings, M. L., Bruni, S., Mercier, S., & Mitchell, P. J. Automation Architecture for Single 
Operator, Multiple UAV Command and Control. International C2 Journal, 1(2).
Cummings, M. L., Nehme, C. E., Crandall, J., & Mitchell, P. (2007). Predicting operator capacity 
for supervisory control of multiple UAVs. In Innovations in Intelligent Machines-1 (pp. 11–
37). Springer Berlin Heidelberg.
Draper, M., Calhoun, G., Ruff, H., Mullins, B., Lefebvre, A., Ayala, A., & Wright, N. (2008). 
Transition display aid for changing camera views in UAV operations. In Proceedings of the 
first conference on Humans Operating Unmanned Systems (HUMOUS’08), Brest, France.
Fern, L., & Shively, R. J. (2009). A comparison of varying levels of automation on the supervisory
control of multiple UASs. Proceedings of AUVSI’s Unmanned Systems North America 2009, 
Washington, D.C..
Fern, L., & Shively, J. (2011). Designing airspace displays to support rapid immersion for UAS 
handoffs. In Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 
55(1), 81–85. 
Fern, L., Shively, R. J., Draper, M. H., Cooke, N. J., & Miller, C. A. (2011). Human-automation 
challenges for the control of unmanned aerial systems. In Proceedings of the Human Factors 
and Ergonomics Society Annual Meeting, 55(1), 424-428.
Flaherty, S. R., Fern, L., Turpin, T., & Scheff, S. (2012). Universal Ground Control Station (UGCS) 
joystick evaluation. In Aerospace Conference, 2012 IEEE, 1–15. 
Hancock P.A., Mouloua, M., Gilson, R., Szalma, J., & Oron-Gilad, T.(2007). Is the UAV Control 
Ratio the Right Question? Ergonomics in Design, 15(1), 30–31.
Harrison, D. A., Mohammed, S., McGrath, J. E., Florey, A. T., & Vanderstoep, S. W. (2003). Time 
matters in team performance: Effects of member familiarity, entrainment, and task 
discontinuity on speed and quality. Personnel Psychology, 56(3), 633–669.
Hart, S. G., & Staveland, L. E. (1988). Development of NASA-TLX (Task Load Index): Results of 
empirical and theoretical research. Advances in psychology, 52, 139–183.

---
**[Page 28]**

21
Miller, C., Funk, H., Wu, P., Goldman, R., Meisner, J., & Chapman, M. (2005). The Playbook™ 
Approach to Adaptive Automation. In Proceedings of the Human Factors and Ergonomics 
Society Annual Meeting 49(1), 15-19. 
Miller, C. A., & Parasuraman, R. (2007). Designing for flexible interaction between humans and 
automation: Delegation interfaces for supervisory control. Human Factors: The Journal of the 
Human Factors and Ergonomics Society, 49(1), 57–75.
Miller, C. A., Shaw, T. H., Hamell, J. D., Emfield, A., Musliner, D. J., De Visser, E., & Parasurman, 
R. (2011). Delegation to automation: performance and implications in non-optimal situations. 
In Engineering Psychology and Cognitive Ergonomics, 322–331. 
Nehme, C. E., Scott, S. D., Cummings, M. L., & Furusho, C. Y. (2006). Generating Requirements 
for Futuristic Hetrogenous Unmanned Systems. In Proceedings of the Human Factors and 
Ergonomics Society Annual Meeting, 50(3), 235–239.
Oron-Gilad, T., Porat, T., Fern, L., Draper, M., Shively, R. J., Silbiger, J., & Rottem-Hovev, M. 
(2011). Tools and Techniques for MOMU (Multiple Operator Multiple UAV) Environments; 
an Operational Perspective. In Proceedings of the Human Factors and Ergonomics Society 
Annual Meeting. 55(1), 86–90. 
Oron-Gilad, T., Porat, T., Silbiger, J., & Rottem-Hovev, M. (2011). Decision support tools and 
layouts for MOMU (multiple operator multiple UAV) environments. In Proceedings of the 
International Syposium on Aviation Psychology, Dayton OH.
Porat T., Oron-Gilad, T.Rottem-Hovev, M. & Silbiger, J. (2016). Supervising and Controlling 
Unmanned Systems: A Multi-Phase Study with Subject Matter Experts. Frontiers in 
Psychology.
Porat, T., Oron-Gilad, T., Silbiger, J., & Rotem-Hovev, M. (2011). Switch and Deliver: Display 
layouts for MOMV (Multiple Operator Multiple Video feed) environments. In Cognitive 
Methods in Situation Awareness and Decision Support (CogSIMA), 2011 IEEE First 
International Multi-Disciplinary Conference on, 264–267. 
Porat, T., Oron-Gilad, T., Silbiger, J., & Rottem-Hovev, M. (2010). 'Castling rays'a decision support 
tool for UAV-switching tasks. In CHI'10 Extended Abstracts on Human Factors in Computing 
Systems, 3589–3594.
Ruff, H. A., Narayanan, S., & Draper, M. H. (2002). Human interaction with levels of automation 
and decision-aid fidelity in the supervisory control of multiple simulated unmanned air 
vehicles. Presence: Teleoperators and virtual environments, 11(4), 335–351.
Saqer, H., de Visser, E., Emfield, A., Shaw, T., & Parasuraman, R. (2011). Adaptive Automation to 
Improve Human Performance in Supervision of Multiple Uninhabited Aerial Vehicles 
Individual Markers of Performance. In Proceedings of the Human Factors and Ergonomics 
Society Annual Meeting, 55(1), 890–893.

---
**[Page 29]**

22
Schulte, A., Meitinger, C., & Onken, R. (2009). Human factors in the guidance of uninhabited 
vehicles: oxymoron or tautology?. Cognition, Technology & Work, 11(1), 71–86.
Shaw, T., Emfield, A., Garcia, A., de Visser, E., Miller, C., Parasuraman, R., & Fern, L. (2010). 
Evaluating the Benefits and Potential Costs of Automation Delegation for Supervisory Control 
of Multiple UAVs. In Proceedings of the Human Factors and Ergonomics Society Annual 
Meeting, 54(19), 1498–1502. 
Shively, R. J., Neiswander, G.M., & Fern, L. (2011). Manned-unmanned teaming: delegation control 
of UAS. Proccedings of the AHS 66th Annual Forum & Technology Display, Pheonix, AZ.
Strobach, T., Frensch, P. A., & Schubert, T. (2012). Video game practice optimizes executive 
control skills in dual-task and task switching situations. Acta psychologica, 140(1), 13–24.