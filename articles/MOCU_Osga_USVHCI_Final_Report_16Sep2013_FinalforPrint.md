# MOCU Osga USVHCI Final Report 16Sep2013 FinalforPrint

*Source file: MOCU_Osga_USVHCI_Final_Report_16Sep2013_FinalforPrint.pdf — 80 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

Technical Report 2022
August 2013
Unmanned Surface Vehicle 
Human-Computer Interface 
for Amphibious Operations
Glenn Osga
Mike McWilliams
Darren Powell
David Kellmeyer
Jerry Kaiwi
Al Ahumada
SSC Pacific
Approved for public release.
Approved for public release.
Space and Naval Warfare Systems Center Pacific
San Diego, CA 92152-5001

---
**[Page 2]**
*(This page contains a figure/chart/image not captured in text)*

SSC Pacific
San Diego, California 92152-5001
J. J. Beel, CAPT, USN
Commanding Officer
C. A. Keeney 
Executive Director
ADMINISTRATIVE INFORMATION 
The work described in this document was sponsored and funded by the Office of Naval Research 
(ONR) under the Capable Manpower Future Naval Capability (FNC) 08-03 Program. The Project 
Unmanned Surface Vehicles Human-Computer Interface for Amphibious Operations (USV-HCI) 
was performed under the direction of ONR Code 34 – Warfighter Performance Division. The work 
was performed by Codes 5300, 53621 in the Command, Control Technologies & Experimentation 
Division, Command and Control Department, and Code 71710 in the Autonomous Systems Division, 
Research and Applied Sciences Department. 
The citation of trade names and names of manufacturers in this report is not to be construed as 
official government endorsement or approval of commercial products or services referenced herein. 
ACKNOWLEDGMENTS 
The science and technology work described in this report was conducted over a 5-year period 
from 2007 through 2012. The initial work was conducted under the direction of ONR Code 34 
Warfighter Performance, Dr. Kip Krebs and Dr. Amy Bolton from 2007 through 2011, with a followon effort conducted during 2012 sponsored by LCS Mission Modules Program Office (PMS 420) 
under the direction of Eng Kwok. The Multi-Operator Control Unit (MOCU) HCI design team 
included David Kellmeyer, Michael McWilliams, and Dr. Glenn Osga of SSC Pacific. The Visual 
Performance model team included Dr. Jerry Kaiwi of SSC Pacific and Dr. Al Ahumada of NASA 
Ames. The software implementation team included Darren Powell, Scott Przybylski, Gary Gilbreath 
of SSC Pacific, with usability test support for software trials by LT Maxwell Long, SPAWAR HSI. 
Fleet support for usability testing was obtained from the Littoral Combat Ship Anti-Subsurface 
Warfare Mission Package (LCS ASW MP) Command and the Mine Countermeasures Mission 
Package (LCS MCM MP) Command in San Diego, California. 
Released by
G. Osga, Senior Technologist
Decision Support Systems
Under authority of
B. Bonwit, Acting Head
Command and Control 
Department

---
**[Page 3]**

i 
EXECUTIVE SUMMARY 
This report describes a multiyear research effort conducted by SPAWAR Systems Center Pacific 
(SSC Pacific) investigating Human-Computer Interface (HCI) issues associated with operating 
unmanned surface vehicles (USVs). An iterative user-design process was used that resulted in the 
development of an enhanced HCI design. The primary focus of this effort was to investigate 
improvements to the baseline HCI design of the SPAWAR Multi-Operator Control Unit (MOCU) 
software to support simultaneous operation of multiple USVs by a single operator. This effort was 
sponsored by the Office of Naval Research (ONR), Code 34, under the Capable Manpower Future 
Naval Capability (FNC) 08-03 Program. A number of significant design enhancements were made to 
the baseline HCI as it was adapted to support multiple USVs. The enhancements included integrated 
visualization of video and graphics combined with multi-modal input and output using synthetic 
speech output and game-controller input. Significant gains in performance times and error reduction 
were found with the enhanced design. Following the ONR effort, Naval Sea Systems Command 
(NAVSEA) LCS Mission Modules Program Office (PMS 420) supported the development of a 
prototype HCI design for operation of a single USV. While overall results of simulator-based 
usability evaluations indicate improved operator performance, the researchers conclude that 
improvements in on-board sensor capabilities and obstacle avoidance systems may still be necessary 
to safely support simultaneous operation of multiple USVs in cluttered, complex transit 
environments.

---
**[Page 4]**

ii
CONTENTS 
EXECUTIVE SUMMARY ......................................................................................................i
GLOSSARY ....................................................................................................................... vi
1. INTRODUCTION AND BACKGROUND .......................................................................... 1
2. HUMAN PERFORMANCE ISSUES ................................................................................. 3
2.1 SUPERVISORY CONTROL ...................................................................................... 3
2.2 WORKLOAD MANAGEMENT ................................................................................... 5
2.3 SITUATION AWARENESS........................................................................................ 5
3. MOCU ARCHITECTURE AND SIMULATION DEVELOPMENT ...................................... 7
3.1 BASELINE MOCU ..................................................................................................... 7
3.2 BASELINE MOCU HCI .............................................................................................. 8
3.3 MOCU BASELINE RE-ARCHITECTURE 2008 ......................................................... 8
3.4 MOCU MISSION SIMULATION ...............................................................................10
4. MOCU HCI ITERATIVE DESIGN PROCESS ................................................................. 12
4.1 MOCU BASELINE USABILITY EVALUATION AND HEURISTIC REVIEW .............12
4.2 MOCU INTERMEDIATE DESIGNS .........................................................................13
4.2.1 MOCU Preliminary Design Wrap-Around Format ........................................... 13
4.2.2 Preliminary Designs for Graphics and Audio .................................................. 14
4.2.3 User Feedback Preliminary Design ................................................................ 18
4.2.4 Preliminary Design Conclusions and Results ................................................. 18
4.3 MOCU V3.0 AND 3.1 DESIGN ................................................................................19
4.3.1 Video and Map Display Re-Design ................................................................. 20
4.3.2 Alarms and Alerts ........................................................................................... 22
4.3.3 Route Status Information ............................................................................... 24
4.3.4 Contact Location and Video Integration ......................................................... 27
4.3.5 USV Pan-Tilt-Zoom Display ........................................................................... 27
4.3.6 Controller Interface ........................................................................................ 28
4.3.7 Procedure Re-Design ..................................................................................... 31
4.3.8 Vehicle and Mission Status ............................................................................ 32
5. HCI USABILITY TESTING .............................................................................................34
5.1 PURPOSE AND SCOPE .........................................................................................34
5.2 PARTICIPANTS ......................................................................................................34
5.3 METHODOLOGY AND TEST PROCEDURES ........................................................36
5.3.1 Mission Scenario ............................................................................................ 36
5.3.2 Performance Measures and Data Collection .................................................. 36
5.3.3 Participant Welcome and Background Questionnaire ..................................... 36
5.3.4 MOCU Orientation and Practice ..................................................................... 36
5.3.5 Usability Testing ............................................................................................. 37
5.3.6 Exit Survey and Debrief ................................................................................. 37

---
**[Page 5]**

iii 
5.4 RESULTS ................................................................................................................38
5.4.1 Data Analysis ................................................................................................. 38
5.4.2 Phase I – One USV vs. Two USVs with Baseline HCI .................................... 39
5.4.3 Phase II – Baseline MOCU vs. MOCU v3 (Two USVs) .................................. 40
5.4.4 Phase III - MOCU v3 vs. MOCU v3.1 (Two USVs) ......................................... 40
5.4.5 Phase IV - Baseline MOCU vs. MOCU v3.1 (One USV) ................................. 41
5.4.6 Summary Comparison across All MOCU Versions ......................................... 42
5.4.7 Results of Exit Survey .................................................................................... 43
5.4.8 Technology Transition Exit Criteria ................................................................. 44
6. VISUAL PERFORMANCE MODEL ...............................................................................46
6.1 RATIONALE FOR EMBEDDED VISUAL MODELS .................................................46
6.2 VISUAL PERFORMANCE MODEL DEVELOPMENT ..............................................46
6.2.1 Simple Search Model ..................................................................................... 46
6.2.2 Underlying Assumptions ................................................................................ 47
6.2.3 Stimuli ............................................................................................................ 47
6.2.4 Methods ......................................................................................................... 47
6.2.5 Preliminary Findings....................................................................................... 48
6.2.6 Discussion ..................................................................................................... 48
7. CONCLUSIONS AND RECOMMENDATIONS ..............................................................49
7.1 ASSESSMENT OF BASELINE MOCU ....................................................................49
7.2 ASSESSMENT OF ENHANCED MOCU ................................................................. 49
7.3 ASSESSMENT OF GAME CONTROLLER INPUT DEVICE ....................................49
7.4 IMPLICATIONS FOR SINGLE USV OPERATION ...................................................50
7.5 EASE OF USE AND TRAINING IMPLICATIONS ....................................................50
7.6 RECOMMENDATION FOR FURTHER TESTING ...................................................50
8. REFERENCES ..............................................................................................................51
APPENDIX A. SCENARIO SCRIPT ................................................................................ A-1
APPENDIX B. VOLUNTARY CONSENT FORM ............................................................. B-1
APPENDIX C. BACKGROUND QUESTIONNAIRE ......................................................... C-1
APPENDIX D. TRAINING PROTOCOL ........................................................................... D-1
APPENDIX E. MISSION BRIEFING ................................................................................ E-1
APPENDIX F. EXIT SURVEY.......................................................................................... F-1

---
**[Page 6]**

iv
FIGURES 
Figure 1. MOCU Baseline HCI using Both Aerial Photo and Digital Nautical Chart (DNC) 
Maps to Control and Monitor Land, Sea, and Air Vehicles. .............................................. 8
Figure 2. MOCU v2 Architecture (Before Re-Design). .......................................................... 9
Figure 3. MOCU v3 Architecture (After Re-Design). ........................................................... 10
Figure 4. Virtual Sailor and MOCU Configuration for Mission Simulation............................ 11
Figure 5. V1.0 HCI Configuration of Baseline MOCU with Simulated Ocean Video Feed. .. 11
Figure 6. Usability Test Display for MOCU Baseline Study. ................................................ 12
Figure 7. Screen Capture from 2009 Live USV Demonstration with Initial Map-Video 
Integration. ..................................................................................................................... 13
Figure 8. Integrated Display Visualization Design Concept for Advanced MOCU. .............. 14
Figure 9. Summary of Route Graphics Designs. ................................................................. 15
Figure 10. Summary of Control Mode Design Graphics Designed to Map to Current 
Surface Craft Robot Control Mode States. ..................................................................... 16
Figure 11. Integration of Robot Control Mode Graphics with Composite View - Route 
Following Mode Example Shown. .................................................................................. 16
Figure 12. Sample Page from Video Worksheet of the Advanced MOCU Specifications. ... 17
Figure 13. Sample Page for Developing USV Audio Alert Messages. ................................ 18
Figure 14. HCI Design Changes Made from MOCU v2 to MOCU v3. ................................. 19
Figure 15. Replacement of Video and Map Information MOCU v2 to MOCU v3. ................ 20
Figure 16. Rearrangement of Video Forward and Aft Video Feeds in MOCU v3. ............... 21
Figure 17. Relocation of PTZ Camera View in MOCU v3. .................................................. 21
Figure 18. Removal of Persistent Aft View Video and Enlarged Secondary USV Forward 
View in MOCU v3.1. ....................................................................................................... 22
Figure 19. MOCU v2 Alarm Presentation (top) and MOCU v3 Alarm Graphics (bottom). ... 23
Figure 20. MOCU v3.1 Alert Presentation with Visual and Auditory Cues. ......................... 24
Figure 21. Route Waypoint Information in MOCU v3 shown on upper dashboard and 
along compass heading. ................................................................................................ 25
Figure 22. Route Insets (top) and Waypoint Countdown Insets (bottom) for v3.1. .............. 26
Figure 23. Contact Graphics Integrated with Video Information in MOCU v3...................... 27
Figure 24. PTZ On-Screen Controls and Indicators. ........................................................... 28
Figure 25. Functional Mapping with Game Controller User Interface. ................................. 28
Figure 26. Typical Task Sequence with PopUp (Pie) Menu. ............................................... 30
Figure 27. Shifting Primary Control between USV 1 and USV 2. ........................................ 30
Figure 28. Baseline MOCU Task Procedure Sequence. ..................................................... 31

---
**[Page 7]**

v 
Figure 29. MOCU v3 Procedure Sequence Example. ......................................................... 32
Figure 30. Upper Display Showing Vehicle and Mission Status. ......................................... 33
Figure 31. Subject Demographics. ...................................................................................... 35
Figure 32. Subject at MOCU Simulation Workstation. ........................................................ 37
Figure 33. Percent Correct Responses Controlling One USV vs.Two USVs Using 
Baseline MOCU. ............................................................................................................ 39
Figure 34. Percent Correct Responses Controlling Two USVs Using Baseline MOCU vs. 
MOCU v3. ...................................................................................................................... 40
Figure 36. Percent Correct Responses Controlling One USV Using Baseline MOCU vs. 
MOCU v3.1. ................................................................................................................... 42
Figure 37. Comparison of Accuracy Rates across All MOCU Versions. ............................. 43
Figure 38. Participant Responses Controlling Two USVs Using MOCU v2 vs. 
MOCU v3.1. ................................................................................................................... 44
Figure 39. Approximate Appearance of a Test Stimulus for Target on Horizon. ................. 47

---
**[Page 8]**

vi
GLOSSARY 
Acronym 
or Term
Meaning
ACTD Advanced Concept Technology Demonstration
AID Advanced Interface Display
API Application Programming Interfaces
ASW Anti-Submarine Warfare
CM Capable Manpower Program
CO Commanding Officer
COA Course of Action
DNC Digital Nautical Chart
FNC Future Naval Capability
HCI Human-Computer Interface
HRI Human-Robot Interface
HSI Human-Systems Integration
LCS Littoral Combat Ship
MCM Mine Countermeasures Mission
MMWS Multi-Modal Watchstation
MOCU Multi-Robot Operator Control Unit
NAVSEA Naval Sea Systems Command
NUWC Naval Undersea Warfare Center
ONR Office of Naval Research
OOVO Offboard Organic Vehicle Operator
PTZ Pan-Tilt-Zoom
SA Situation Awareness
SME Subject Matter Expert
SOA Service Oriented Architecture
SSC 
Pacific
Space and Naval Warfare Systems Center Pacific
TAO Tactical Action Officer
TM Task Manager
UAV Unmanned Aerial Vehicles
UCD User Centered Design
UGV Unmanned Ground Vehicle
USV Unmanned Surface Vehicle
WOO Window of Opportunity

---
**[Page 9]**

1 
1. INTRODUCTION AND BACKGROUND
Unmanned Surface Vehicles (USVs) are envisioned as an integral part of the mission module 
packages for the Littoral Combat Ship (LCS) of the future. To date, preoperational exercises and 
training have focused on the USV shipboard operator controlling a single USV. However, given the 
small crew size on an LCS ship, mission demands may call for a single operator to control and 
monitor multiple USVs simultaneously. Therefore, it is vital to evaluate the effectiveness of the 
current user interface to gain insights into design improvements that could help support multiple 
USV operations. 
This report describes a multiyear research effort conducted by SPAWAR Systems Center Pacific 
(SSC Pacific) investigating Human-Computer Interface (HCI) issues associated with operating 
USVs. An iterative user-centered design process resulted in development of an enhanced HCI design. 
The primary focus of this effort was to investigate improvements to the baseline HCI design that 
would support simultaneous operation of multiple USVs by a single operator. This effort was 
sponsored by the Office of Naval Research (ONR), Code 34, under the Capable Manpower Future 
Naval Capability (FNC) 08-03 Program. 
This project was initiated in 2007 to address the ONR defined Capability Gap 1, “Next Generation 
Autonomous Systems” by the application of human factors research and engineering to the next 
generation control interface for the LCS HCI. The project goal was to study design factors with 
respect to operator Situation Awareness (SA) and interaction with the Mission Supervisor. Key 
technical objectives of this FNC included: 
 Development of effective attention management mechanisms, including visual and auditory 
displays to guide user attention and maintain situation awareness based on mission 
conditions. 
 Development of low-risk, easy-to-use interactive methods supporting both supervisory 
control and migration to or from manual control. 
 Development of simple, efficient, and effective HCI control and displays. 
 Development of multi-layer visual integration techniques to reduce user visual scanning and 
reduce visual and cognitive integration across separate display windows. 
 Collection of human performance data to measure the impact of design factors through the 
iterations. 
 Development of flexible, expandable multi-robot controller software architecture to enable 
future growth and HCI additions. 
A secondary objective was: 
 Development of a risk model of mission conditions based on operational environmental 
conditions, operating speed, and user visual performance with respect to obstacle detection 
and avoidance. Use the model to guide the user during varying operational conditions. 
This project was conducted through a series of iterative design evolutions that involved the testing 
of new HCI concepts and evaluating the effects of the concepts on human performance. At the start 
of the project, the SSC Pacific Multi-robot Operator Control Unit (MOCU) was the “baseline”
design. Initial project tasks were conducted during the 2007 to 2009 time frame as follows: 
 The User-Centered Design (UCD) team conducted heuristic reviews and usability testing of 
the Baseline MOCU to define design qualities that could negatively impact operator

---
**[Page 10]**

2 
performance and estimate initial design changes required (Kellmeyer and Bernhard, 2009), 
(Kellmeyer, McWilliams, and Bernhard, 2009). 
 Human factors guidelines and principles were applied to develop early HCI concepts which 
then directed the requirements for re-architecture of MOCU software into a service oriented 
architecture (SOA) with the capability to support the visual integration features (e.g., video 
and graphics) requested by the UCD team (McWilliams, 2009). 
The project need for human performance testing required a simulation capability to be acquired 
and integrated into MOCU to allow human-in-the-loop hands-on testing within the context of 
operational scenarios. With the creation of a dynamic simulation and MOCU re-architecture, it 
became possible to study human performance interacting with simulated USVs. The following tasks 
were conducted during the 2010–2011 time frame: 
 Task analysis for anti-submarine warfare (ASW) and mine countermeasures mission (MCM) 
mission domains. The ASW mission domain was cancelled during later phases of the project, 
but the tasks selected were also representative of work activities in the MCM mission. 
 Creation of dynamic operational task scenario with at-sea mission simulation. The scenario 
was designed to contain varying levels of difficulty in decision tasks. 
 Identification of task outcome-based metrics for collection in usability studies. 
 Creation of integrated visualization design for an Advanced MOCU HCI. 
Usability testing was conducted with initial versions of the Advanced HCI (McWilliams, Osga, 
Kellmeyer, and Viraldo, 2010): 
 Definition of lessons learned and design issues to be corrected in upgrades to the Advanced 
MOCU HCI design. 
Usability testing was conducted with the enhanced MOCU HCI (McWilliams, Osga, and 
Kellmeyer, 2010, McWilliams, 2011): 
 Definition of a final design for transition to LCS Mission Modules with recommendations for 
implementation. 
 Creation of transition plans and documentation to aid in the integration of the ONR FNC 
product with the Naval Sea Systems Command (NAVSEA) Program of Record (Powell, 
2011). 
On completion of the initial project, a follow-on effort, sponsored by NAVSEA LCS Mission 
Modules Program Office (PMS 420), was performed to design and evaluate a version of the 
improved HCI for control of a single USV. This work was performed during Fiscal Year 2012 (FY
12). Because this follow-on effort significantly leveraged research, experimental techniques, and 
resultant design concepts from the preceding ONR work, the PMS 420-sponsored work is presented 
within the context of the overall USV HCI ONR research effort in this comprehensive report.

---
**[Page 11]**

3 
2. HUMAN PERFORMANCE ISSUES 
Tasks related to the monitoring and control of multiple USVs involve user skills and abilities 
related to situation awareness and supervisory control. The design of the MOCU HCI and functions 
must account for limitations in human performance and offer enhancements to guide attention during 
multi-tasking dynamic operations. This section of the report discusses key human performance issues 
related to USV control. 
2.1 SUPERVISORY CONTROL 
Supervisory control typically involves less operator direct manual control of systems, and 
increased higher levels of planning and decision-making (Sheridan, 1992). This type of control 
involves operators at a higher cognitive level for a knowledge-based set of behaviors where the user 
intermittently interacts with a computer, receiving feedback from and providing commands to a 
controlled process or task environment. According to Mitchell, Cummings, and Sheridan (2005), 
there are perhaps 10 key issues related to human performance in network-centric operations in 
supervisory control of systems. These include: 
 Information Overload 
 Appropriate Levels of Automation 
 Adaptive Automation 
 Distributed Decision-Making and Team Coordination 
 Mitigating Complexity 
 Decision Biases 
 Attention Allocation 
 Supervisory Monitoring of Operators 
 Trust and Reliability 
 Accountability 
For the purposes of this project, supervisory control is assisted through the use of visual and 
auditory displays, alerts, and integration of critical information. Design goals are: 
1. Mitigate information overload, 
2. Support user situation awareness, and 
3. Provide effective attention allocation. 
Operator Knowledge, Skills, and Abilities with respect to Visual, Auditory, and Cognitive, dictates 
human performance for USV control and psychomotor performance as related to mission tasks and 
work pacing demands. Thus, the simulated USVs used in Human-Robotic Interface (HRI) studies 
were created to match the operational characteristics of the real USV platforms, and are multifunctional and re-programmable machines not requiring a constant operator inputs or corrective 
actions. Studies indicate that more automation is not always better with respect to operator reaction. 
For example, Parasurman, Mouloua, Molloy and Hilburn (1996) report that in general, studies 
indicate that when operators do not actively control a process they are poorer at detecting 
malfunctions than when they are engaged both in control and monitoring. Results are unclear though 
given length of tasks studied and whether operators had other manual tasks as well. Further studies 
appear to indicate that monitoring performance for failures is often poorer if there are other manual 
tasks being performed. We consider the operator to be performing USV tasks without the need for

---
**[Page 12]**

4 
other concurrent manual tasks. If automation monitoring is the only task, performance is not 
impaired (Parasurman, Molloy, and Singh, 1993). Hancock et al. (2007) state that given a control 
regimen such as making intermittent commands under supervisory control, the number of 
controllable UAVs is directly contingent on the temporal capacity of each machine for independent, 
autonomous action (Mouloua, Gilson, and Hancock, 2003). Thus a key factor is how much time the 
robot demands from the operator and what the operators’ surround task environment is. Competitive 
tasking at the same time reduces performance for monitoring. Our work assumes the 
operator/monitor is not in any immediate combat danger and the USV operations are managed from a 
controlled shipboard command center environment. Thus, the operators on the LCS ship are 
dedicated to the mission functions (mine-warfare or other missions) and may be time-sharing HRI 
tasking with verbal communication tasks to other operators (e.g., sensor) or mission supervisors. 
Multiple vehicle control and monitoring creates possible error conditions due to: 
1. Sensory input conflict, 
2. Central decision-making processing overload, and 
3. Response confusion and interference (Hancock et al., 2007). 
Each of these performance-shaping factors must be considered in designing controls and displays 
that support user shift of control and monitoring between multiple vehicles. Considering these 
performance issues it is likely that planning and analysis of incoming information streams from 
sensors (e.g., sonar) is best done by an analyst (given the full attention of visual and cognitive 
resources given to analyses) with vehicle control and monitoring best done by a dedicated controller. 
Similarly, Barnes et al. (2006) indicate from study of task distribution among a two-person team that 
performance was better when split by roles vs. by vehicles. For example, team workload for two 
USVs would be distributed by Operator A doing observation and analysis for both vehicles while 
Operator B does navigation/control for both vehicles. Still, the issue of workload bottlenecks for that 
controller/monitor must be addressed given multiple vehicles and external mission pacing. 
One way to aid users is through the use of “predictive” displays, (Baldwin, Basu, and Zhang, 1998, 
1999; Bejczy, Kim, and Venema, 1990; Mathan et al., 1996). Researchers studying intelligent aids 
for predicting of high workload periods in the control of multiple unmanned aerial vehicles (UAVs) 
found that users would fixate on optimizing a future schedule to the detriment of solving certain near 
term problems (Mitchell, Cummings and Sheridan 2005). Cummings further investigated the 
depiction of projected task opportunity time periods in the flight profiles of multiple Tactical 
Tomahawks. As determined for control of multiple tactical tomahawks in flight, the user can be aided 
by showing task “windows of opportunity” (WOO) where time slots are graphically shown for best 
operator attention to multiple missile control decisions, (Cummings and Guerlain, 2004) With regard 
to route planning and waypoint adjustments with USVs, it should be possible to aid users with 
decision support tools similar to the WOO based on projected workload (timing and concurrence) 
with multiple routes. The user could then adjust their task schedules in advance to balance workload 
before a high load condition is created. Displays developed at SSC Pacific were used together with a 
tactical route plot display to monitor multiple Tactical Tomahawks (UAVs) in flight (Osga et al., 
2005). The graphics and color coding shown was used to draw operator attention to critical mission 
task path items requiring attention and management. 
These principles were applied to the waypoint announcement and inset information HCI to provide 
advance notices to users of upcoming mission route events. Another important design goal was to 
integrate and overlay information such that visual scanning and search workload is limited.

---
**[Page 13]**

5 
2.2 WORKLOAD MANAGEMENT 
Workload can be defined according to the WINDEX (Workload Index) model which describes 
components of workload along six dimensions: Visual Perception, Auditory Perception, Verbal 
Cognition, Spatial Cognition, Manual Response, and Speech Response. A recent study created a Task 
Network model predicting workload for ASW search operations using multiple USV sorties with 
multiple vehicle control (Miller, 2006). With the software and USVs used in this study it may be 
possible to use same or similar scenarios to measure workload with actual systems, which serves to 
validate the model results as well as defining system success. Workload management is a key design 
issue that must account for the entire gamut of operator tasks, including control, monitoring, and 
team communication/collaboration. The Miller study predicts high workload for communication 
tasks. The controller/monitor must be able to not only safely control the vehicle but also receive input 
and coordinate actions with the mission analyst/tasking part of the team. Osga et al. (2002) found that 
use of decision support visual aids in small tactical teams reduced the amount of required verbal 
communications as team members were able to see tasks in progress requiring less discussion of 
“who, when, what, how” of imminent task needs. With multiple USV operations, there are options 
available to management mission workload, including. 
1. Reducing mission pace by slowing or delaying operations. Speed can be reduced or one 
vehicle delayed or placed in loiter mode while another is given full attention. These tactics 
may become more desirable if both USVs are in manual control mode or if surface clutter is 
high. 
2. Using leader and follower USV path tactics. Thus one USV “clears the path” for the second, 
and the speed and course of the second following USV is based on the lead USV. 
3. Under high-clutter conditions, completing task sequences for one USV, then placing that 
vehicle in loiter mode while completing a sequence for the second USV. 
Tactics must be considered to adjust workload levels dependent on the operational risks and 
environment (e.g., visibility, clutter, waves). The scenario developed for this project contained 
varying workload levels simulating multiple simultaneous environmental and equipment critical 
events. This approach allows the analysis impact of workload demands at varying levels across HCI 
designs. 
2.3 SITUATION AWARENESS 
Situation awareness (SA) must be distributed and shared between controller and planner. SA has 
been described as having three major levels of awareness. Situation awareness is a conscious human 
process of information collection, filtering and storage, interpretation and reaction. 
Jones and Endsley (2000) refer to three levels of SA as: 
 Level 1: perception of the elements in the environment within a volume of time and space, 
 Level 2: comprehension/understanding of their meaning, and 
 Level 3: Projection of their status in the near future. 
Level 1 SA tasks include visual search, filtering of important task information from peripheral 
visual “noise,” and auditory sampling from multiple sources. All are part of the sampling process to 
continually update human short-term memory regarding the current status of the environment. 
System aiding can be provided for various types of SA sampling, storage, and retrieval activities. 
Level 2 activity implies that incoming information presented is compared to the current and nearterm goal-states of mission tasks and activities to determine the significance of events relative to 
goals. The resulting actions include decisions to start, delay, or cancel task activities. Level 3 implies

---
**[Page 14]**

6 
that there is temporal nature to decision making and that activities may be launched or altered based 
on projections into the near-term future. In USV control/monitoring tasks, this includes decisions for 
altering courses or waypoints to over-ride the current route plan in favor of manual control. This 
decision may be based on individual SA or shared SA, including the goals and intent of the mission 
commander or other crewmembers. There is evidence that users build a story (or mental model) 
based on the operating environment, expected events, and observed events, and compare this to past 
experiences in their decision-making training or operational experiences (Klein, 1993). Problems in 
mission performance may appear when errors occur in SA, producing a mismatch between the user’s 
mental model of the situation and the actual situation. Endsley and Garland (2000) refer to 
“representational errors” when information has been correctly perceived but the significance of 
various pieces of information is not properly understood, meaning problems with Level 2 SA. In 
USV control, visual cues that a craft is potentially moving into a collision path may be overlooked in 
favor of evidence that something more important to the mission context is nearby. For example. the 
user may be inspecting something with the Pan-Tilt-Zoom camera and temporarily lose SA for the 
forward path of the USV. The system requirement, therefore, is to provide information in a manner 
that prompts the user to be attentive and to support ongoing SA of USV activity regarding mission 
needs and priorities.

---
**[Page 15]**

7 
3. MOCU ARCHITECTURE AND SIMULATION DEVELOPMENT
3.1 BASELINE MOCU 
During the 2000-2007 time period, SSC Pacific developed an unmanned vehicle and sensor 
operator control interface capable of simultaneously controlling and monitoring multiple sets of 
heterogeneous unmanned systems. The term heterogeneous is used to describe vehicles that are 
dissimilar in both modality (land, air, sea, or undersea) and communications protocol. The goal was 
to not just minimally control, but to have full access to the vehicle/sensor and its payloads. To 
achieve this goal, a modular, scalable approach was developed. The modularity, scalability, and 
flexible user interface of the Multi-Robot Operator Control Unit (MOCU) accommodates a wide 
range of vehicles and sensors in varying mission scenarios. Figure 1 shows the Baseline HCI view of 
MOCU with air, sea, and ground vehicle monitoring and control. 
To avoid time-consuming and expensive changes to a monolithic OCU to support new devices or 
technologies, the MOCU was designed to improve flexibility by using a modular, scalable, and 
flexible architecture. Modularity allows for a breadth of functionality, such as communicating in 
unrelated protocols or displaying video with a proprietary video codec. Modularity also allows for 
third-party expansion of MOCU. Scalability allows MOCU to be installed on a wide range of 
hardware. MOCU also allows the user to define what information is displayed and determine what 
control is needed for each system. The same core software is currently used on a wide variety of 
projects, each utilizing these attributes in its own way. 
As of 2008, MOCU version 2 provided the common USV operator interface for the LCS ASW and 
MCM mission modules. The LCS USV operator interface was built from the prior command and 
control interface, MOCU version 1, that had been developed for the Spartan Advanced Concept 
Technology Demonstration (ACTD) USV. MOCU was also being used by the Army’s PM Force 
Protection Systems office as the unmanned vehicle and sensor interface for a joint experiment with 
the Air Force Research Laboratory and to control many of the SSC Pacific developmental vehicles 
(land, air, sea, and undersea). For the ground robot domain, it provided a common OCU for the 
Urban/Cave assault ACTD for the iRobot Packbot and SSC Pacific URBOT Unmanned Ground 
Vehicles (UGVs). SSC Pacific had also received funding from the Defense Threat Reduction Agency 
(DTRA) to adapt MOCU as the user interface for a mid-size UAV for force protection of fixed site 
Army bases. 
MOCU was designed with a modular architecture to allow for orderly expansion and addition of 
new capabilities. Much of the functionality of MOCU resides in plug-in modules that are 
dynamically linked at runtime. Additional functionality can be added to an existing MOCU 
installation by simply copying new modules to the folder without changing any of the core MOCU 
code. An Application Programming Interfaces (API) document has been written that fully describes 
the MOCU module interface. This allows third-party developers to add their own functionality to 
MOCU with very little support from SSC Pacific. The API was used by the Naval Undersea Warfare 
Center (NUWC) Newport to develop the MOCU interface module that communicates to ASW 
mission planning tools. The user interface is similarly flexible. The layout and functionality of 
MOCU is determined via XML text configuration files. The user interface can be changed very 
quickly and as many times as needed, again without modifying and re-coding. This approach made 
MOCU an ideal platform on which to study user interface and HSI issues.

---
**[Page 16]**
*(This page contains a figure/chart/image not captured in text)*

8 
Figure 1. MOCU Baseline HCI using Both Aerial Photo and Digital Nautical Chart (DNC) 
Maps to Control and Monitor Land, Sea, and Air Vehicles. 
3.2 BASELINE MOCU HCI 
The Baseline MOCU interface is a tiled window interface with multiple window tiles that included 
2D maps with USV symbol location superimposed on chart and separate satellite image 
backgrounds. Control Button options and Inset Chart views are included at closer range-scales than 
shown in the wide-area map. Video input is shown in windows of varying size. As parameters are 
selected by clicking on objects, drop down windows appear allowing data parameter changes through 
keyboard or mouse entry. The application ran on a Windows-based computer with a single monitor.. 
For the FNC, the application was reconfigured to run on a dual-monitor console similar to that 
aboard the Littoral Combat Ship (LCS). 
3.3 MOCU BASELINE RE-ARCHITECTURE 2008 
The MOCU v2 architecture is shown in Figure 2 before re-design. The core software of MOCU 
loads other modules to perform various functions, such as communicating with robots, displaying 
map data, decoding video, etc. The core also reads configuration files that govern what the user 
interface looks like as well as providing customization data that may be needed for a particular 
project. MOCU v2 communicates with the modules using several different APIs depending on the 
module type. This functionality is inherited from MOCU v1 and is supported primarily for backward 
compatibility. A newer more flexible interface was introduced in MOCU v2 using a publish and 
subscribe (“pubsub”) paradigm to share data between the MOCU core and the other modules, making 
it unnecessary to have specific interfaces for particular module types.

---
**[Page 17]**
*(This page contains a figure/chart/image not captured in text)*

9 
Figure 2. MOCU v2 Architecture (Before Re-Design).
While MOCU v2 offered a great deal of flexibility regarding the user interface organization, it also 
contained a number of deficiencies. 
MOCU v2 used the Windows graphics device interface that is not very fast and cannot handle 3D 
graphics, making it impossible to implement a modern user interface. The core of MOCU defined the 
look-and-feel of the user interface, so changes to user interactions (mouse clicks, wheel movements, 
and keyboard accelerators) required changes to the core, which can be difficult to do and affects 
other projects using MOCU. Because most of the MOCU v2 modules used module-specific APIs 
instead of the pubsub API, their functionality was quite limited. Also, the Configuration Files were 
not stored in the data server — much information useful to various modules was not available. 
The MOCU v3 architecture developed in FY 08 (see Figure 3) addressed these issues. There was 
no longer a MOCU “core” application that provided the majority of the functionality of MOCU. The 
core was replaced by a set of modules (referred to as the “core modules”) supplying the same basic 
functionality previously provided by the core application. Each of these is a module and only 
performs one function to facilitate isolated modifications.

---
**[Page 18]**
*(This page contains a figure/chart/image not captured in text)*

10
Figure 3. MOCU v3 Architecture (After Re-Design). 
MOCU v3 only supports the pubsub module interface (denoted by Ips in the figure) so modules 
have access to all the data in the system as well as the ability to communicate with other modules. 
The modules communicate via the DataServer module, which provides access to raw data 
(properties) as well as providing an inter-module communication mechanism (method calls). 
Some modules interact exclusively with the DataServer (such as modules that receive information 
from robots or other exterior devices). Others provide display data to the user or process user input. 
Because the configuration information is read from external files but stored in the DataServer, all 
modules have access to configuration information that now gives MOCU more flexibility than in 
previous versions. 
3.4 MOCU MISSION SIMULATION 
A dynamic mission simulation is the pre-cursor to conducting human performance experiments 
with multiple USVs. Although the MOCU software supports operations with live USVs, cost 
cutbacks during the FNC time frame prohibited expensive operations with live USVs. In addition, 
there was only one USV available, making multiple USV operations impossible. 
A list of possible simulation toolsets was compiled, organized, and rated according to essential 
project criteria. Presagis Corp tools and several other top candidates were investigated and demos 
observed. Tools were compared on cost criteria vs. requirements for supporting user-performance 
and usability testing. A low-cost and functionally adequate game simulator product, “Virtual Sailor,”
was selected as the method of creating a simulated ocean environment to mimic the return of a video 
feed from the simulated USV. 
Figure 4 shows the architecture employed to construct the simulation capability to support human 
performance studies. First, a screen capture is done on each Virtual Sailor screen at 10 Hz. Initially, 
the vehicle status is retrieved from the screen using optical character recognition techniques to 
populate simulated sensor returns and throttle/rudder commands are sent as virtual key presses to a 
specific Virtual Sailor module. This version used Microsoft's DirectX "Direct Play" SDK (a 
Microsoft utility) to ensure a common visualization across multiple virtual sailors. The Virtual Sailor 
software company was eventually funded to modify the base software, SNS-s70, to provide a sharedmemory API to enable higher resolution vehicle status, better control of the vehicle and environment 
setup, and to sync the multiple instances of Virtual Sailor. Screen captures are sent as an MJPEG 
formatted stream when requested.

---
**[Page 19]**
*(This page contains a figure/chart/image not captured in text)*

11
Figure 4. Virtual Sailor and MOCU Configuration for Mission Simulation. 
Figure 5 shows a Baseline MOCU user-interface configuration for the simulated ocean 
environment along with the baseline HCI (map, USV control functions, status indicators). As the user 
monitors the USV path and mission progress, the simulated USV camera view can be manipulated to 
correspond with the simulated USV mission path and progress on MOCU. 
Figure 5. V1.0 HCI Configuration of Baseline MOCU with Simulated Ocean 
Video Feed.

---
**[Page 20]**
*(This page contains a figure/chart/image not captured in text)*

12
4. MOCU HCI ITERATIVE DESIGN PROCESS
4.1 MOCU BASELINE USABILITY EVALUATION AND HEURISTIC REVIEW 
In July 2008, a usability evaluation was conducted using the Baseline MOCU software. The 
evaluation focused on the usability of the current computer interface (see Figure 6) in supporting 
users who performed general functions associated with controlling a USV. The goal of the test was to 
identify key functions where the current interface may be inefficient, complicated, or perhaps 
increase workload or fail to provide adequate decision support. 
Participants consisted of six sailors from the Littoral Combat Ship Anti-Subsurface Warfare 
Mission Package (LCS ASW MP) command in San Diego, California. These sailors were among 
those who would have been tasked to control the first operational USV prior to the cancellation of the 
USV component. An introductory training session was provided to expose each participant to the 
basic functionality of the MOCU controls and displays. Because the vehicle controller job rating was 
so new, participant experience with MOCU was minimal and varied from a few days to a few weeks. 
The training consisted of a 1-hour group instructional training session, followed by a 1-hour handson training session. A think-aloud protocol was used to capture the users thought and decisionmaking processes while attempting to perform basic mission tasks. 
Initial findings suggested that the design was at high risk for modal errors, given multiple modes 
and lack of adequate visual or auditory feedback as to what mode the USV is currently in. Numerous 
errors of both omission and commission were observed. Additionally, HCI navigation to access the 
required functionality was often difficult. These concerns were given top priority in subsequent 
modification and redesign. A full review of the findings and recommendations of this evaluation are 
provided in Kellmeyer and Bernhard (2009). 
Figure 6. Usability Test Display for MOCU Baseline Study.

---
**[Page 21]**
*(This page contains a figure/chart/image not captured in text)*

13
4.2 MOCU INTERMEDIATE DESIGNS 
Based on the initial results from the heuristic review, several design concepts were explored, 
aimed at resolving many of the HCI issues identified. Examples are discussed below.
4.2.1 MOCU Preliminary Design Wrap-Around Format 
Following the MOCU re-architecture in FY 08, FY 09 was devoted to building an advanced 
human-computer interaction format using the new architecture. In April 2009, the first live 
demonstration was conducted in San Diego Bay illustrating USV monitoring and control. Figure 7 
shows a screen capture from MOCU during the operational demonstration. Personnel were located 
on the USV for safety purposes. The USV was launched and landed at the Shelter Island Marina and 
the demonstration site was located near Ballast Point at the Naval Submarine Base Point Loma. The 
demonstration showed that it was possible in real-time to dynamically orient a map, radar returns, 
and wrap around 360-degree camera views in an integrated visualization. A movie of the 
demonstration was delivered to ONR. 
The 3D perspective map shown in Figure 8 correlated visually with a wrap-around video 
perspective view. A concise user interface specification was prepared that incorporated task-centered 
design principles with visual integration and attention management principles. The April 
demonstration with initial integration was a first step toward a concise design integration 
incorporating these principles. Figure 8 shows a concept visualization of the integrated display, 
representing the next phase in design leading toward MOCU v3. 
Figure 7. Screen Capture from 2009 Live USV Demonstration with Initial Map-Video Integration.

---
**[Page 22]**
*(This page contains a figure/chart/image not captured in text)*

14
Figure 8. Integrated Display Visualization Design Concept for Advanced MOCU. 
This design concept contained several important design features not found in today’s state-of-art 
robotic user interface systems. First, radar-detected surface contacts were visually integrated with 
information on the video wrap-around display. Next, the task-centered approach shows current and 
planned tasks correlating these with voice reports prepared for delivery to the warfare commander. 
Thus, the interface supports the USV use in the context of the mission process and mission plan. This 
is distinctly different than designing an interface to “just operate a piece of equipment.” In this 
concept, the pan-tilt-zoom (PTZ) camera is also shown as an overlay on the wide view cameras. The 
interface is interactive and the user can drag and relocate icons to change the view. Also, a visual 
model is superimposed on the map, indicating to the user the estimated visual range such that objects 
in view or beyond detection can be more easily estimated. Critical mission events are also shown, 
such as the “unknown contact” indicated. Software implementation for the next versions of MOCU 
captured many of the design concepts shown in this initial concept. 
4.2.2 Preliminary Designs for Graphics and Audio 
Initial guidelines were developed for several critical user situation awareness and robot control 
visualization tools. This included route monitoring and reporting graphics as shown in Figure 9. The 
graphics were implemented in MOCU v3 and not only depict critical events in the mission, but also 
indicate to the user a connection between the mission plan, current status, and upcoming tasks such 
as reports and decision points during the mission. A next step in design was the integration of the 
route and task graphics with the robot control modes. Figure 10 shows the specifications developed 
for each of the robot control modes. This includes route following mode, vector mode, and manual 
mode. This design feature addressed gaps in modal situation awareness that were found to be a 
critical problem in the first usability test conducted with Baseline MOCU in FY 08 (Kellmeyer,

---
**[Page 23]**
*(This page contains a figure/chart/image not captured in text)*

15
McWilliams, and Bernhard, 2009). Next, the modal control information was integrated in the 
composite MOCU view as shown in Figure 11. The complete set of specifications was captured in a 
spreadsheet for use by MOCU programmers. Figure 12 shows one page from the video specs 
worksheet. 
Figure 9. Summary of Route Graphics Designs.

---
**[Page 24]**
*(This page contains a figure/chart/image not captured in text)*

16
Figure 10. Summary of Control Mode Design Graphics Designed to Map to Current 
 Surface Craft Robot Control Mode States. 
Figure 11. Integration of Robot Control Mode Graphics with Composite View - Route 
Following Mode Example Shown.

---
**[Page 25]**
*(This page contains a figure/chart/image not captured in text)*

17
Figure 12. Sample Page from Video Worksheet of the Advanced MOCU Specifications. 
The attention management schema developed for MOCU under this project prescribes integrated 
auditory cues with gender-specific voices used to represent each robot (one male voice and one 
female voice). A demonstration held in concert with our April demo for a visiting NATO robotics 
group illustrated the use of Cepstral voice patterns for the Army robots at Fort Ord test facility near 
Monterey, CA. These voice models were subsequently purchased and incorporated into MOCU. A 
voice feedback library was then developed and mapped to the Cepstral synthetic speech output1
.
Figure 13 shows a sample page from the USV alert taxonomy that was used as a template for 
deriving the specific alert messages that were subsequently incorporated using synthetic auditory 
speech methods. Audio cues were not included in MOCU v3.0 version but were added to Version 3.1 
for the final usability test. 
 
1
 See http://cepstral.com/ for further information on Cepstral products.

---
**[Page 26]**
*(This page contains a figure/chart/image not captured in text)*

18
Figure 13. Sample Page for Developing USV Audio Alert Messages. 
4.2.3 User Feedback Preliminary Design 
Users gathered to review paper wireframe designs of the preliminary “wrap around” design 
concepts in August 2009. Four ASW Sonar Technicians, all of whom had received training and had 
some experience in operating USVs for ASW, made up the review team. Operators expressed several 
concerns regarding the overall concept of the integrated display, including: 
 Loss of video data (only about 75%) of 360-degree field they currently have. 
 Want 90-degree direct starboard/port views “to see anything coming at them from the side.”
 Concerned about video distortion from video wrap. 
 Want a larger rear view mirror – maybe stretched across bottom of screen. 
 Loss of SA when digital nautical chart (DNC) moves relative to USV heading. 
 Of paramount importance is location of LCS home ship to quickly orient to its location. 
4.2.4 Preliminary Design Conclusions and Results 
Results from initial user interviews with the “wrap around” design resulted in decisions to consider 
re-design and orientation of the map (chart) components of the HCI. The initial design considered the 
map view and orientation as aligning and integrated with the video. The user’s perspective for the 
map was noted as not being from the USVs point-of-view, but from ownship orientation and the 
USV being a separate off-board vehicle/sensor. This perspective aligns with an overall command and 
control larger area point of view, and less focused on the immediate robot locale. The comments 
noted on video prompted the design for MOCU v3 to include integrated PTZ and rear-view cameras,

---
**[Page 27]**
*(This page contains a figure/chart/image not captured in text)*

19
combined with the front and side views. User feedback with respect to alarms and warnings 
prompted the use of summary warnings for equipment alerts, and avoidance of audio alarms for v3.0. 
4.3 MOCU V3.0 AND 3.1 DESIGN 
FY 10 and 11 work focused on continued software development of MOCU based on human factors 
guidelines developed in FY 08 and FY 09 and usability tests conducted in FY 09. The MOCU 
components included video (360-degree view, rear view, PTZ), mission plan graphics, 
map/geographics, task and event indicators, and post mission analysis. Significant changes in design 
included: 
 Relocation and re-design of map and video windows 
 Re-design of alerts and alarms 
 Enhanced display of route status 
 Integration of contact location and video 
 Re-design of the PTZ camera display and controls 
 Adoption of a game hand-held controller device 
 Procedure re-design 
 Vehicle and mission status information 
Figure 14 shows the overall HCI design changes that were made from Baseline MOCU v2 to 
MOCU v3. The left side of the figure shows the upper and lower displays for MOCU Baseline V2 
and the right side shows the same displays for MOCU v3. 
Figure 14. HCI Design Changes Made from MOCU v2 to MOCU v3.

---
**[Page 28]**
*(This page contains a figure/chart/image not captured in text)*

20
4.3.1 Video and Map Display Re-Design 
The relative visual focus time shared between video and map displays favored the most frequently 
used display being in the primary lower display position. Thus, the video camera images were moved 
to the lower display in MOCU v3 as shown in Figure 15. The map information was moved to the 
upper display. The video information was also rearranged due to confusion about camera image 
content. Figure 16 shows the baseline configuration of the video feeds for MOCU v3 design. The 
port, forward, and starboard camera images are “stitched” together, configured left to right to provide 
a 180 degree windshield type view. The aft view was placed top center of the lower display, similar 
to the placement of a rear view mirror in an automobile. This redesign follows basic human factors 
principles of orientation and compatibility of displays with the information spatial orientation. 
Figure 15. Replacement of Video and Map Information MOCU v2 to MOCU v3.

---
**[Page 29]**
*(This page contains a figure/chart/image not captured in text)*

21
Figure 16. Rearrangement of Video Forward and Aft Video Feeds in MOCU v3. 
The PTZ camera view was placed in the upper left portion of the lower display in MOCU v3 as 
shown in Figure 17. The PTZ, aft view, and forward view are all shown for the USV in primary 
control/view. The “secondary” USV shows the forward view in upper right (colored with orange 
border). 
Figure 17. Relocation of PTZ Camera View in MOCU v3. 
Further changes were made to the arrangement of the video windows following usability testing of 
v3. In v3.1, the secondary USV forward view was enlarged and the aft view was changed to toggle 
with the PTZ view. The ability to selectively hide the aft view was added based on feedback from

---
**[Page 30]**
*(This page contains a figure/chart/image not captured in text)*

22
users that the constant movement and stream of the wake image in the aft view was distracting from 
other ongoing visual tasks. Figure 18 shows the v3.1 configuration. 
Figure 18. Removal of Persistent Aft View Video and Enlarged Secondary USV Forward 
View in MOCU v3.1. 
4.3.2 Alarms and Alerts 
Alarms and alerts are used in the design to communicate equipment and mission status event 
changes to the operator. Figure 19 shows the location of the alarms in MOCU v2 and an example of a 
red flashing equipment alarm in the right side of the screen. Note, however, the inconsistent use of 
color coding with five buttons along the bottom of the screen also colored red during normal 
operations. In MOCU v3, the alarm indicators were distributed with an icon shown on PTZ view and 
also on the central control dashboard.

---
**[Page 31]**
*(This page contains a figure/chart/image not captured in text)*

23
Figure 19. MOCU v2 Alarm Presentation (top) and MOCU v3 Alarm 
Graphics (bottom). 
Results from usability testing for MOCU v3 indicated that a higher alerting cue saliency was 
required for the alarm information. A combination of increased visual cues and auditory information 
was added to the alarm indicators in v3.1. Figure 20 shows the visual changes to the alert indicators 
for v3.1. The visual alerting cue was increased in size to cover the entire section of the window and 
flashed on and off. Auditory messaging was also added to MOCU v3.1, alerting the operator to 
system alarms, changes in driving mode, waypoint approach, and potential collisions. A female voice 
was used for one USV and a male voice used for the other USV. An example auditory report is 
“USV One, high engine temperature” as shown in the figure, paired with the large flashing icon.

---
**[Page 32]**
*(This page contains a figure/chart/image not captured in text)*

24
Figure 20. MOCU v3.1 Alert Presentation with Visual and Auditory Cues. 
4.3.3 Route Status Information 
MOCU v3 also included indicators for route status, including upcoming waypoints. Figure 21
shows the locations for USV1 and USV2 notices in video and dashboard locations. The map inserts 
are shown in the figure for each of the USVs. Route and waypoint information is shown on the lower 
part of the dashboard, with the next mission plan item shown on the bearing it occurs. The purpose of 
co-location of route information with video is to reduce the number of visual scan shifts typically 
done between the video and map displays. In MOCU v3.1, the route information was enlarged and 
displayed more prominently within the video area as shown in Figure 22. Auditory alerts were also 
added to inform the operator of the USV approaching each waypoint.

---
**[Page 33]**
*(This page contains a figure/chart/image not captured in text)*

25
Figure 21. Route Waypoint Information in MOCU v3 shown on upper dashboard and along compass 
heading. 
Waypoint to port off camera Route plan leg on bearing 106.4

---
**[Page 34]**
*(This page contains a figure/chart/image not captured in text)*

26
Route Insets Shown for USV 1 (purple) and USV 2 (orange). 
 
 Waypoint Countdown Indicator at 200 yds. Waypoint Countdown Indicator at 100 yds. 
Figure 22. Route Insets (top) and Waypoint Countdown Insets (bottom) for v3.1.

---
**[Page 35]**
*(This page contains a figure/chart/image not captured in text)*

27
4.3.4 Contact Location and Video Integration 
Information integration is a design attribute used to decrease visual workload and increase 
information transfer efficiency. Contact and collision avoidance is a critical mission task and 
situation awareness for surrounding contacts a critical decision-support need. Sensor-derived contacts 
shown on map in MOCU v2 were integrated with video displays in MOCU v3 as shown in Figure 23. 
The bearing and range of the contact is known from radar information and the corresponding contact 
information is shown on the contact bearing within the wrap-around video feeds display. Also, 
indicators are shown in the lower right and left of display for the number of tracks out of sight to port 
or starboard directions. 
Figure 23. Contact Graphics Integrated with Video Information in MOCU v3. 
4.3.5 USV Pan-Tilt-Zoom Display 
MOCU v3 integrated on-screen camera controls with the camera being controlled. First, the PTZ 
camera could be controlled with on-screen arrows, as shown in Figure 24. The user could click and 
hold on the arrow controls to move the camera up, down, left, or right. A PTZ heading indicator was 
included in the design after observing users would leave the camera slewed to a port or starboard 
direction and later during camera re-use would think it was pointed straight ahead. The user could 
also use the camera joystick as described below. On the larger video displays looking port, starboard, 
and ahead, clicking and dragging the 360-degree camera tiled view rotates that view to port or 
starboard.

---
**[Page 36]**
*(This page contains a figure/chart/image not captured in text)*

28
Figure 24. PTZ On-Screen Controls and Indicators. 
4.3.6 Controller Interface 
MOCU v2 required numerous and repeated point and click actions to conduct task sequences with 
the USV. For MOCU v3 and 3.1, an Xbox game controller was adopted and programmed to conduct 
many of the frequently repeated tasks conducted during a mission. Figure 25 shows the mapping of 
functions to the game controller interface. 
Figure 25. Functional Mapping with Game Controller User Interface.

---
**[Page 37]**

29
Manual “driving” of the USV is performed in either Teleoperation Mode or Vector Mode. In 
MOCU v2, steering was performed by clicking on or dragging directional arrows. In MOCU v3 and 
3.1, the left joystick and D Pad are used to control the direction of the vehicle in each of those modes. 
Movement of the left joystick immediately switches to Teleoperation Mode from either Vector or 
Waypoint Navigation. USV heading is then controlled by pushing the joystick in the direction of 
intended travel (forward, right, left, reverse). Speed is controlled by the distance the joystick is 
pushed from center position. As the joystick is pushed further in any direction, the speed increases. 
When the joystick is fully released, the USV stays in Teleoperation Mode but coasts to a stop. Vector 
Mode is activated via any movement of the D-Pad control, which switches the mode to Vector Mode 
from Teleoperation or Waypoint Navigation. The north and south nodes on the D-Pad control speed 
(north = increase, south = decrease). Each momentary button press increases or decreases speed by 1 
knot. Speed will continue to increase or decrease if the button is held in the depressed position. 
Direction is controlled by the east-west nodes on the D-Pad. The west node changes USV direction to 
the left (port). The east node changes USV direction to the right (starboard). Each button press 
changes the direction by 1 degree. Direction will continue to change if the button is held in the 
depressed position. 
For MOCU v3.1, several refinements were made to the driving controls and functionality based on 
observations from the usability testing. Movement of the left joystick now overrides the current drive 
mode and temporarily puts the USV in Teleoperation mode. This was done to provide the operator 
immediate, manual control in the event of an emergency situation. As the joystick is pushed further 
in the selected direction, speed increases. When the joystick is fully released, the USV will revert to 
the mode it was previously in (Vector or Navigation) unless Teleoperation mode has been 
deliberately selected by depressing the joystick (push down). Heading is still controlled by moving 
the joystick in the direction of intended travel (forward, right, and left), but the ability to put the USV 
into reverse via the joystick was eliminated. In MOCU v3.1, the operator must deliberately select 
reverse from the transmission options accessed through the Pie Menu. This was done to eliminate the 
possibility of inadvertently putting the USV into reverse as was observed during MOCU3 usability 
testing. The sensitivity of the joystick for teleoperation was also reduced in MOCU 3.1 based on 
feedback received after simulator testing. Controls for Vector Mode driving remained the same for 
MOCU v3.1 as in v3.0. 
The right joystick is used to control the onboard PTZ camera and will direct the camera left, right, 
up, and down. Pushing down on the joystick automatically returns the camera to the home position. 
This feature was added to MOCU v3.1, along with a camera position icon, after observing several 
instances of subjects failing to return the camera to the home position after use and losing situational 
awareness with regard to the camera image they were observing. The trigger buttons are used to 
control the zoom feature of the PTZ camera. 
Many secondary controls are accessed via the Pie Menu that is opened and closed using the arrow 
buttons on the controller as shown in Figure 26. This approach allows the user to remember 
sequences by “feel and location” vs. conducting a visually focused cursor movement to a button or 
menu location during point and click. The user presses the Menu button and then A, B, X, or Y 
(green, red, blue, or yellow) depending on the desired menu selection. As shown in the figure, the 
user has selected “B” for Radar and “X” for Active, with the result shown on the radar graphic 
indicator.

---
**[Page 38]**
*(This page contains a figure/chart/image not captured in text)*

30
Figure 26. Typical Task Sequence with PopUp (Pie) Menu. 
The Toggle USV controls shift the display focus as shown in Figure 27, with the primary focus 
USV being the subject of control manipulations from the controller. The secondary USV maintains a 
forward view camera while the primary USV has forward, PTZ, and rear views. 
Figure 27. Shifting Primary Control between USV 1 and USV 2. 
1. Press Pie Menu Button 2. Menu appears, press “B” for Radar
3. Press “X” for Active 4. Menu disappears and radar status is active
USV 1 in Primary Control (purple border) USV 2 in primary control (orange border)

---
**[Page 39]**
*(This page contains a figure/chart/image not captured in text)*

31
4.3.7 Procedure Re-Design 
Procedure design affects usability and training. Complex and multi-step procedures inhibit 
efficiency of use and require a higher cognitive loading for memory. HCI procedures are also less 
efficient if they require constant hand-eye coordination such as point and click on display objects. If 
the objects are in a sequence that require movements from window to window or across screens, 
workload is further increased. Figure 28 shows a typical sequence for Baseline MOCU. Figure 29
contrasts this sequence with the MOCU v3 workflow. 
Figure 28. Baseline MOCU Task Procedure Sequence.

---
**[Page 40]**
*(This page contains a figure/chart/image not captured in text)*

32
First, viewing the video screens the user sees something on video that requires an action 
controlling the USV. The procedure design requires that attention is then shifted to the lower screen 
where several point and click actions are needed (as shown in steps 3 through 8 in the sequence). 
Next, attention shifts to the upper screen to verify visually that the change is taking place. The 
sequence is cumbersome and requires significant reaction time to complete once a visual cue prompts 
the sequence. 
In comparison, as shown in Figure 29 for MOCU v3, the user first views the visual item as in 
MOCU baseline; however, the forward views (e.g., for detecting possible collisions) are located on 
the primary lower display. The need to shift between displays is eliminated. Next, the user does not 
need to point and click on menus or controls on the screen to make an evasive maneuver. The 
controller provides hands-on control options while the visual focus can remain on the primary video 
windows. This allows for a continuous focus on critical visual information. Thus, “React” requires 
only a single control action on the hand-held controller. Observe and Verify become seamless and 
“React” requires no visual workload. 
Figure 29. MOCU v3 Procedure Sequence Example. 
4.3.8 Vehicle and Mission Status 
For MOCU v3 and 3.1, windows were also added to the map (upper) display showing summary 
vehicle status information displayed on either side of the map, and mission status and analysis 
information, displayed above the map. Figure 30 shows the additional windows added to the map 
display. For purposes of the simulator usability testing described later, the Event Viewer and Mission 
Analysis windows were not active.

---
**[Page 41]**
*(This page contains a figure/chart/image not captured in text)*

33
Figure 30. Upper Display Showing Vehicle and Mission Status.

---
**[Page 42]**

34
5. HCI USABILITY TESTING
Following completion of the USV simulator that included the integration of simulated video into 
MOCU, a series of usability tests were conducted in which Navy operators performed USV 
operations during a simulated mission scenario. Performance was measured for operation of one 
USV as well as operation of two USVs. The results were used to derive conclusions about the design 
and recommendations for changes to be included in subsequent design iterations. Details of the 
simulator usability testing procedures and results are provided in the following section. 
5.1 PURPOSE AND SCOPE 
The purpose of the usability testing described here was to guide development of HCI 
enhancements to the MOCU design and to empirically evaluate operator performance using the new 
HCI designs against baseline versions. HCI evaluation was accomplished through collecting 
performance measures indicative of workload and situational awareness while conducting simulated 
missions in which USVs were deployed on a simulated mission. The study consisted of four phases 
of usability evaluation, corresponding to delivery of successive versions of the MOCU interface. 
Performance data and user feedback collected during each phase were used to guide HCI 
enhancements that were integrated into each subsequent MOCU version as previously described. 
The focus of the initial testing (Phase l) was to establish a baseline level of performance for 
operating both a single USV and two USVs using the current interface and to determine whether the 
addition of a second USV would adversely affect operator performance. For operation of two USVs, 
only minimal revisions were made to the existing interface to allow for dual vehicle control. In 
essence, this constituted a side-by-side replication of the system status displays and video camera 
windows currently displayed for a single USV on one monitor and incorporation of the second USV 
on the overall Digital Navigation Chart (DNC) displayed on the second monitor. Based on 
conversations with USV subject matter experts (SMEs), this interface design was representative of 
the configuration that could be anticipated if operators were required to control two USVs 
“tomorrow.” Phase II of the study measured operator performance using the initial prototype 
interface design concepts incorporated into MOCU v3 compared to the Baseline MOCU interface. 
Phase III evaluated additional refinements incorporated in the MOCU v3.1 HCI design. Phase IV 
then evaluated the impact of HCI improvements made over the course of the project in controlling a 
single USV, comparing the Baseline HCI to a single USV version of the MOCU v3.1 interface. 
5.2 PARTICIPANTS 
Over the course of the project, 32 Navy enlisted personnel participated in simulator usability 
testing sessions. Distribution of subjects to experimental conditions was as follows: 
 2 USVs, Baseline HCI – 6 Participants 
 2 USVs, MOCU v3 HCI – 8 Participants 
 2 USVs, MOCU v3.1 – 10 Participants 
 1 USV, Baseline HCI – 4 Participants 
 1 USV, MOCU v3.1 HCI – 4 Participants 
Most participants were assigned to one of the two mission package detachments that had been 
designated to operate USVs when they are deployed aboard USS Freedom (LCS 1). Ten were Sonar 
Technicians from the ASW detachment and 17 were Minemen from the MCM detachments. All 
participants were stationed in San Diego. Twenty participants had actual USV driving experience, 
but due to the newness of the position, less than half the participants had more than 10 hours, and

---
**[Page 43]**

35
only four had operated a USV within the past 6 months. All participants had at least some small boat 
driving experience. Additional participants were involved in pilot testing that preceded formal 
usability testing phase to validate the mission scenario and refine the test protocol, including two 
Sonar Technicians with significant USV experience who assisted in validating the realism of the 
scenario. Participant demographics are shown in Figure 31. 
Subject
Number
Years 
Service
Job
Specialty
Years in 
Rate
USV 
Hours
Simulator
Hours
Recent USV 
Experience
1 13 STG > 5 > 20 1-5 Yes
2 8 MN 1-2 > 20 > 20 No
3 8 STG 0 0 0 No
4 8 MN 2-5 5-10 10-20 No
5 10 STG > 5 0 0 No
6 14 MN > 5 5-10 5-10 No
7 7 STG 1-2 < 5 10-20 No
8 14 MN >5 0 0 No
9 14 MN >5 >20 >20 No
10 11 STG >5 >20 0 No
11 11 STG > 5 >20 <5 No
12 12 STG > 5 >20 >20 No
13 16 MN >5 5-10 <5 No
14 13 STG >5 10-20 >20 No
15 13 MN >5 <5 <5 No
16 11 MN >5 <5 <5 No
17 12 MN >5 0 <5 No
18 8 BM 0 0 0 No
19 12 MN >5 <5 <5 Yes
20 4 MN >5 <5 <5 No
21 16 SK/DV >5 >20 <5 No
22 15 Cox 0 0 0 No
23 9 FC 0 0 <5 No
24 10 EngO <1 0 0 No
25 8 STG >5 0 0 No
26 7 STG >5 0 0 No
27 8 MN 1-2 10-20 5-10 No
28 7 MN >5 0 0 No
29 8 MN 1-2 10-20 5-10 Yes
30 15 MN 1-2 5-10 5-10 Yes
31 10 MN 3-5 10-20 10-20 No
32 12 MN 3-5 0 2-5 No
Figure 31. Subject Demographics.

---
**[Page 44]**

36
5.3 METHODOLOGY AND TEST PROCEDURES 
5.3.1 Mission Scenario 
The usability testing consisted of each participant performing the role of USV operator in a 
simulated ASW mission scenario. The scenario required them to respond to a series of predetermined conditions and events as they transited the USVs from the LCS host ship to the mission 
operations area. The scenario was designed to elicit performance of critical tasks derived from 
previous SME interviews, ranging from making routine reports to taking emergency actions to avoid 
collision with other vessels in the immediate area. The test scenario ran on a PC-based simulation 
program developed by SSC Pacific’s Unmanned Systems Group that incorporated video graphics 
from a customized nautical gaming simulator with the MOCU-based user interface displays and 
controls. Although not all MOCU functionality was available in the simulation, feedback from the 
participants regarding the level of fidelity was quite positive. The scenario script is provided in 
Appendix A. 
5.3.2 Performance Measures and Data Collection 
For each critical event (CE) in the scenario requiring an operator response, an expected course of 
action (COA) was defined along with criteria for successful completion. These COAs constituted the 
decision support focus for performance metrics on speed and accuracy, and were listed next to each 
initiating event on the facilitator’s scenario script that also served as the data collection form. As the 
scenario progressed, the facilitator noted whether the participant executed the correct course of action 
for the CE. In some cases, the response was time dependent and had to be performed within a 
specified window to be considered a correct response. The facilitator also recorded any comments 
made by the participant or observations made that provided additional context to the COA selected 
by the user for each event. 
5.3.3 Participant Welcome and Background Questionnaire 
Upon arriving at the site, participants were greeted by the researchers and thanked for their 
participation. The researchers presented an overview of the project explaining the purpose of the 
study and the participant’s role. Participants were told that the objective of the study was to evaluate 
the user interface and was not a test of his or her skills. Each participant was assured of the 
confidentiality of the results and that their participation was strictly voluntary. After agreeing to 
continue their involvement in study and signing the Voluntary Consent form (Appendix B), each 
participant completed a brief Background Questionnaire designed to obtain information regarding the 
participants’ overall military service experience as well as experience specific to USV operations. 
The Background Questionnaire is provided in Appendix C.
5.3.4 MOCU Orientation and Practice 
Although most participants in the formal usability study were assigned to mission package 
detachments that were expected to deploy USVs, a significant number of individuals had only been 
recently assigned and had not yet operated a USV. Also, there are some minor differences between 
the MOCU interface for the ASW and MCM mission packages. To ensure that all participants had a 
basic understanding of the specific MOCU interface used in the study, a brief (approximately 30-
minute) training session with hands-on guided practice was conducted prior to the actual test. The 
training also addressed differences between the simulator and the actual system. An outline of the 
training protocol is provided in Appendix D.

---
**[Page 45]**
*(This page contains a figure/chart/image not captured in text)*

37
5.3.5 Usability Testing 
Upon completion of the training and practice session, the facilitator read the mission briefing to 
each participant that described the nature of the mission as well as the communications protocol 
between the facilitator, who played the role of the Mission Supervisor, and the participant, who 
performed the role of the USV operator (See Appendix E). The briefing also included instructions 
calling for the USV operator to make periodic reports to the Mission Supervisor throughout the 
course of the mission, including waypoint achievement and sighting of any contacts along the route.. 
After answering any questions the participants had, the mission was initiated by the facilitator 
directing the USV operator to “Take control of USV 1,” followed by instructions to “activate radar 
and proceed to the first waypoint in vector mode.” A second researcher located out of sight from the 
participants acted as the simulator operator, controlling the timing of initiating events such as alarm 
activation and directing other boat traffic. Figure 32 shows a subject seated at the workstation during 
usability testing. 
Figure 32. Subject at MOCU Simulation Workstation. 
5.3.6 Exit Survey and Debrief 
On completion of the testing, participants were asked to complete an Exit Survey that asked 
questions designed to elicit subjective feedback as to how well the interface supported the operator in 
performing the mission. The participants were asked to agree or disagree with a series of statements 
about MOCU’s effectiveness and intuitiveness for navigation and control tasks. A 5-point Likert-

---
**[Page 46]**
*(This page contains a figure/chart/image not captured in text)*

38
style rating scale was used to measure participants’ responses, with the scale ranging from 1, 
“Strongly Disagree,” to 5, “Strongly Agree.” Open-ended questions were also included asking for 
participants suggestions on improving various aspects of the interface. This was followed by a 
debrief session in which the facilitator was able to gain further understanding of certain actions taken 
(or not taken) by the participant USV operators. The Exit Survey is provided in Appendix F. 
5.4 RESULTS 
5.4.1 Data Analysis 
For each experimental condition, pass/fail performance on critical tasks was determined based on 
the subject’s course of action during the mission scenario. For data analysis and description purposes, 
related critical tasks were grouped into the following five task domains: USV System Control, 
Waypoint Reporting, Contact Reporting, Collision Avoidance, and System Alarm Response. Each 
task domain was made up of six to eight related or recurring tasks constituting N trial opportunities 
for pass/fail data points for each subject. Pair-wise comparisons were made within each task domain 
and for the total tasks between: MOCU v1 and MOCU v2 (Phase I), MOCU v2 and MOCU3 (Phase 
II), MOCU v3 and MOCU v3.1 (Phase III), and MOCU v1 and MOCU v3.1 for a single USV only 
(Phase IV). For each condition, the number of passes and fails for N trials were computed and used 
to generate a probability of success and a probability of failure. Given the total number of trials for 
each task domain, p and q were used to generate an expected number of passes and failures for the 
comparative condition. The expected number of pass/fails were then compared to the obtained 
number of pass/fails for that condition. 
In order to test whether the obtained number of pass/fails were significantly different than the 
expected number of pass/fails, three statistical tests were carried out. A χ2 test was first computed. In 
cases where there are only two outcomes, it can be shown that χ2 = z2 and that: 
Taking the square root then generated a z-score for each trial. The z-score in this two alternative 
outcome is an approximation of the binomial distribution. A Yates correction was then applied, 
giving the following equation: 
Lastly, given the p and q for each task domain within each version of MOCU, the probability of 
obtaining the observed number of passes and failures in each comparative MOCU condition of 
MOCU was computed with the binomial distribution.

---
**[Page 47]**
*(This page contains a figure/chart/image not captured in text)*

39
5.4.2 Phase I – One USV vs. Two USVs with Baseline HCI 
In Phase 1, subjects controlled either one USV or two USVs using the Baseline MOCU HCI in 
both conditions. The results of the Phase 1 Baseline testing are shown in Figure 33. Data analysis 
showed a significantly lower percentage of correct responses across each task domain for participants 
operating two USVs rather than a single USV. Of notable concern was the dramatic decrease in 
performance for Alarm Response tasks when operating two USVs (38% correct response rate with 
two USVs) and for Collision Avoidance tasks (only 50% correct response rate). The overall 
(combined) performance score for two USVs was also significantly lower than the overall score for 
single USV operations. 
Figure 33. Percent Correct Responses Controlling One USV vs.Two USVs Using 
Baseline MOCU.

---
**[Page 48]**
*(This page contains a figure/chart/image not captured in text)*

40
5.4.3 Phase II – Baseline MOCU vs. MOCU v3 (Two USVs) 
Phase II evaluated subject performance while controlling two USVs, comparing the baseline HCI 
to the first version of the advanced prototype HCI (MOCU v3). The results of Phase II testing are 
shown in Figure 34. For three of five task domains, subjects demonstrated a significant performance 
improvement using the MOCU v3 interface over the Baseline HCI. The overall performance score 
was also significantly higher for the MOCU v3 users. The most notable improvements were noted for 
Alarm Response tasks (66% correct vs. 33%) and Collision Avoidance tasks (84% correct vs. 50%). 
Slight but insignificant improvements were noted for Waypoint and Contact Reporting Tasks. In 
follow-up interviews, several participants indicated that “in the real world” they do not routinely 
provide waypoint reports or report contacts that have been identified and do not pose a potential 
threat. Therefore there may have been some selective under-reporting during the scenario due to 
carryover from previous experience. 
Figure 34. Percent Correct Responses Controlling Two USVs Using Baseline MOCU vs. MOCU v3. 
5.4.4 Phase III - MOCU v3 vs. MOCU v3.1 (Two USVs) 
Phase III testing was conducted to evaluate the effects of the enhancements introduced in MOCU 
3.1 vs the initial prototype HCI (MOCU v3). The results of Phase III testing are shown in Figure 35. 
Data analysis confirmed a significant increase in the percentage of correct responses for participants 
using the MOCU v3.1 interface vs. participants using the MOCU v3 interface across three of five 
task domains and for all tasks combined. The most significant increase in correct responses was 
0
1 0
2 0
3 0
4 0
5 0
6 0
7 0
8 0
9 0
100
System
Controls
Waypoint
Reports
Contact
Reports
Alarm
Response
Collision
Avoidance
All Tasks
MOCU 2 MOCU 3
**
** **
**
* P < .05 **p < .01
Percentage Correct Responses

---
**[Page 49]**
*(This page contains a figure/chart/image not captured in text)*

41
observed for Alarm Response tasks, (95% correct vs. 63%) likely due to the addition of audio alerts 
announcing changes in alarm status. A slight but not statistically significant decrease in Collision 
Avoidance accuracy was noted. 
0
1 0
2 0
3 0
4 0
5 0
6 0
7 0
8 0
9 0
100
System
Controls
Waypoint
Reports
Contact
Reports
Alarm
Response
Collision
Avoidance
All Tasks
MOCU 3 MOCU 3.1
*
**
**
*
* P < .05 **p < .01
Percentage Correct Responses
Figure 35. Percent Correct Responses Controlling Two USVs Using MOCU v3 vs. MOCU v3.1. 
5.4.5 Phase IV - Baseline MOCU vs. MOCU v3.1 (One USV) 
The Phase IV study was conducted to evaluate the impact of HCI improvements made over the 
course of the project in controlling a single USV. Although the overall purpose of the ONR FNC was 
to investigate HCI improvements to support multiple USV operations, implementing design 
improvements for single USV operations would be a logical “first step” in the transition process. 
Therefore, the research team (with support from NAVSEA) felt it important to validate the prototype 
design in a single USV environment as well. The results of Phase IV testing are shown in Figure 36. 
Although performance improvement was observed across all task domains for participants using the 
MOCU v3.1 interface (except for Waypoint Reporting which was already maxed at 100%), the 
results were statistically significant only for Alarm Response tasks and combined tasks due to the 
relatively small number of participants in this phase (8 total). As noted in the analysis of the Phase III 
results, the significant improvement in performance observed for Alarm Response tasks is attributed 
to the addition of audio messaging used to alert the operator to changes in alarm status.

---
**[Page 50]**
*(This page contains a figure/chart/image not captured in text)*

42
Figure 36. Percent Correct Responses Controlling One USV Using Baseline MOCU vs. MOCU v3.1. 
5.4.6 Summary Comparison across All MOCU Versions 
Results are shown in Figure 37 for each of the major scenario critical tasks and events, across all 
the MOCU versions. For all operational tasks, MOCU v3.1 was significantly improved from v3.0 
(p = .01) and from Baseline MOCU. USV System Control tasks showed significant improvement (p 
= .05) from v3.0 and from Baseline (p = .01). Contact reporting, a secondary workload measure 
verbal report task, improved significantly (p = .05) in v3.1 from v3.0. v3.1 was significantly better 
than Baseline MOCU. Collision avoidance was unchanged from v3.0 to v3.1, with both versions 
significantly improved from MOCU baseline (p = .01). Alarm response improved significantly from 
v3.0 to v3.1 (p = .01) and improved from Baseline MOCU (p = .01). Analysis of collisions separated 
them into easy and hard problem groups. Results indicated that difficult collision problems, which 
contained no radar or sensor detection cues, still caused problems for operators with a 50% miss rate 
in v3.1. In comparison, easier problems where visual and sensor information was available in parallel 
with video information, produced a 100% accuracy rate in v3.1.

---
**[Page 51]**
*(This page contains a figure/chart/image not captured in text)*

43
Figure 37. Comparison of Accuracy Rates across All MOCU Versions. 
5.4.7 Results of Exit Survey 
The results of the exit survey administered at the conclusion of each testing session indicated a 
strong user preference for the advanced interface when controlling two USVs. Figure 38 shows 
percentage of positive and negative participant responses between the Baseline MOCU and MOCU 
v3.1, the final prototype HCI for two USVs.

---
**[Page 52]**
*(This page contains a figure/chart/image not captured in text)*

44
Figure 38. Participant Responses Controlling Two USVs Using MOCU v2 vs. MOCU v3.1. 
5.4.8 Technology Transition Exit Criteria 
The following exit criteria were listed in the TTA2and reported to NAVSEA at the conclusion of 
the FNC program, (t) = Minimum Threshold, (o) = Objective. 
1. Objective: Continuous operation of two vehicles: one mission suspension under highest 
workload (t); all workload conditions (o). 
Result: Users were able to operate two vehicles simultaneously with no mission suspension 
required and under all imposed test workload conditions. Objective met. 
2. Objective: Correct object interpretation : >90% (t) with suspension of multiple streams due to 
reduced image quality; >99% with multiple video streams with time-sharing of tasks. 
Result: Budget limited the ability to test with live USVs and broadcast video; however, 
simulated results indicated that the improved video arrangement and tiling significantly 
reduced errors in object detection and interpretation. 100% accuracy achieved with full 
sensors. 89% overall with simulated degraded radar sensors. Objective met with fully 
operational sensors. With degraded sensors threshold nearly met. 
3. Objective: Training hours required for operator success: <5 (t); <2 (o) hrs. 
 
2
 Technology Transition Agreement, Office of Naval Research, Maritime Warfare Branch N863 and LCS 
Mission Modules Office (PMS-420) PEO Littoral and Mine Warfare, June 30th, 2008.

---
**[Page 53]**

45
Result: Training was successful in far less than 2 hours; usually, approx. 15 min. of training 
was sufficient for acceptable performance. Objective met. 
4. Objective: Operator SA for Key Mission components: 80% (t); 95% (o). 
Result: Situation Awareness as measured by mission progress through waypoints, 
surrounding contacts, USV status and response to status alarms and changes was significantly 
improved. All exceeded minimum threshold of 80% accuracy with 89% overall accuracy for 
all tasks. Objective met. 
5. Objective: Operator awareness: react to verbal instructions (t); adaptive proactive reaction 
(o).
Result: Users were 100% able to react to verbal instructions during experiments from a roleplay of the officer in charge of USV operations. Users responded to command requests and 
provided verbal reports as required during testing. Users also were able to enact proactive 
responses to emergency situations as they developed. Objective met.

---
**[Page 54]**

46
6. VISUAL PERFORMANCE MODEL
In addition to the work described in previous sections, a model of human visual detection 
performance against small objects on the horizon was developed to support automated human visual 
attention management for command and control of multiple autonomous or semi-autonomous robots 
by a single operator. An eye-tracker system was used to collect data in a human visual detection task 
utilizing a single-pixel high-contrast target on a simulated horizon (1280 pixels). Initial results 
indicate near perfect detection performance was achieved using on average 18 fixations (eyemovements), each with an average duration of 296 seconds. This corresponds to an average of 5.3 
seconds per trial (24 trials). This result was used to calculate an observed fovea diameter of 1.66 
degrees (67.3 pixel field of view). These results are consistent with a simple detection model that 
assumes a target is detected if it is foveated. This initial experiment and results were presented at the 
May 2010 Visual Sciences Society Symposium. The abstract was published in the Journal of Vision.
(Ahumada, 2010, 2011).
6.1 RATIONALE FOR EMBEDDED VISUAL MODELS 
The operation of multiple semi-autonomous vehicles will require operator attention shifts between 
robots. Attention can be guided by visual and auditory cues; however, these cues must be 
appropriately used within the context of the robot state and mission status. The robots will not 
contain obstacle avoidance hardware or software requiring visual supervision and operator attention. 
The conditions that are worrisome include the floating oil drum or wood palette not detectable by 
radar, that can damage or sink the robot, and that is only detectable by visual methods through video 
cameras. Another dangerous condition involves local small craft that might be difficult for radar 
detection. A simple method to guide attention would be to consider the kinematics of the robot 
(course and speed), known obstacles (digital charts), and local ship radar contact picture, and to 
provide simple timing cues to drive attention allocation. Tying alerts to this simple model would 
likely become annoying and result in operator intervention to circumvent embedded cues. An 
alternate method would be to also add consideration of visual conditions embedded in a human 
performance model that would adjust the attention cues according to robot operating conditions. This 
method would allow alternate cue intervals, depending on visual conditions. The result would be 
embedded cues for attention that are tied to robot conditions and human visual performance within 
the operational environment. 
6.2 VISUAL PERFORMANCE MODEL DEVELOPMENT 
Computational models predicting the distribution of the time to detection of small targets on a 
display are being developed to improve workstation designs. Search models usually contain bottomup processes, like a saliency map, and top-down processes, like a priori distributions over the 
possible locations to be searched. A case that needs neither of these features is the detection of target 
near an empty horizon. Initial models have incorporated a saccade-distance penalty and inhibition-ofreturn with a temporal decay. For very small, but high-contrast targets, using the simple detection 
model that the target is detected if it is foveated is sufficient. For low-contrast signals, a standard 
observer detection model with masking by the horizon edge is required. Testing to determine 
parameter values for this model was conducted in FY 10. 
6.2.1 Simple Search Model 
 Select fixation position at random. 
 Is target in fovea? If yes, end search. If no, go to 1.

---
**[Page 55]**
*(This page contains a figure/chart/image not captured in text)*

47
 Search task: Detect a small target on a simulated horizon in a uniform sky above a uniform 
ocean. 
6.2.2 Underlying Assumptions 
 The luminance difference of the target pixel is such that it will be detected with p = 1.0 if it is 
fixated. 
 The visual search is memoryless, i.e., a previously visited fixation point may be returned to. 
6.2.3 Stimuli 
 Screen distance: 69 cm Image width: 38 cm 
 Image size in pixels: 1280 x 1024 (W x H)
 Sky y pixel range: 0–509 
 Sky RGB color: 0 128 255 => 45.4 cd/m^2 
 Target, ocean: 0 0 128 => 6.62 cd/m^2 
 Target pixel size: 1 x 1
 Target y position: 509 
 Target x positions: i*100, i=1,12 
 Blank screen fixation cross, x y: 512 384 
 (Samsung Syncmaster 910T LCD monitor) 
An approximation of an actual test stimulus is provided in Figure 39. Note that the size of the 
target relative to the ocean and sky is much greater than the proportional size of the one-pixel target 
in the actual simulated scene. 
Figure 39. Approximate Appearance of a Test Stimulus 
for Target on Horizon. 
6.2.4 Methods 
Eye positions were recorded at 250 Hz by an SR Research Eyelink II head-mounted tracker. The 
experiment was controlled by an SR Research Experiment Builder program. There were three test 
runs of 12 trials. Before each three-trial group a recalibration was performed. Each test included all 
12 positions in a random order. The sequence of fixations was extracted by an SR Research Data 
Viewer program. The data from the first test run was discarded.

---
**[Page 56]**

48
6.2.5 Preliminary Findings 
Detection of a single pixel on a simulated horizon (1280 pixels) requires on average 18 fixations 
(eye-movements), each with an average duration of 296 seconds. This corresponds to an average of 
5.3 seconds per trial (24 trials). This result was used to calculate an observed fovea diameter of 1.66 
degrees (0.024652 deg/pix, fovea = 67.3 pixel field of view). 
6.2.6 Discussion 
The above assumptions are clearly violated by the data, but relaxing the assumptions in meaningful 
ways, e.g., assuming P = .75 and the search is not memoryless, changes the estimate of the fovea 
diameter by a factor close to 1.0 so the estimate from the data is very reasonable. If the fovea 
diameter is relatively constant, then detection time is simply the ratio of the estimated fovea diameter 
to the size of the area being searched times the duration of a fixation. 
In terms of automated visual attention management, an unobtrusively eye-tracked operator can be 
alerted when the expected time to detect is passed so that he or she can safely shift visual attention to 
another task. A higher-level decision support system could also calculate risk levels for 
shifting/resuming visual search based on the simple detection model and situational variables such as 
speed, visibility, and target contrast models. 
Next steps include obtaining more detection data in order to validate the fovea diameter estimate 
and evaluate effects due to non-random search and the assumption of a target luminance detection 
threshold. Note that the initial data did not include any false alarms. However, data just recently 
collected and not reported here indicate false alarms are possible even with high-contrast targets. In 
this case and especially when low contrast targets are present, the assumption of a target luminance 
detection threshold must be dropped and the detection model modified to include a false-alarm 
parameter. This more complicated model can be investigated using the test paradigm reported here 
by utilizing low-contrast targets, i.e., a target pixel having a luminance value closer to that of the 
simulated sky.

---
**[Page 57]**

49
7. CONCLUSIONS AND RECOMMENDATIONS
7.1 ASSESSMENT OF BASELINE MOCU 
The results of the study clearly indicate that the Baseline MOCU does not support safe operation 
of multiple vehicles by a single operator. When participants were tasked with controlling two USVs 
simultaneously in a simulated mission, overall performance on operational tasks dropped from 86% 
correct course of action (COA) responses to 65% correct COA responses. Significant drops in 
performance were seen across all task domains. Of particular concern though was the performance 
drop-off observed in participants’ responses to potential collision situations where correct COA 
response rates dropped from 83% to only 50%. Also of notable concern was the diminished rate of 
correct responses to system alarms. Using the baseline HCI, correct response rate was only 58% for a 
single USV and dropped to a disturbing 33% correct COA when operating two USVs. 
7.2 ASSESSMENT OF ENHANCED MOCU 
The significant improvements in operator performance that were observed after implementing the 
enhanced MOCU v3.1 interface indicates the potential for successful operation of multi-USV 
operations with HCI visual, auditory, and control enhancements. Performance improved across all 
major task COA categories; however, collision avoidance still contained a level of operational risk. 
The most difficult tasks involved avoidance of contacts with no detection or radar information, 
relying only on human vision and manual reaction to a pending collision. Even though all 
participants were warned during the mock mission briefing that radar was unreliable on one USV, 
requiring diligent monitoring of video cameras, many participants failed to adequately monitor the 
forward view video window for extended periods of time when other distracting activities (such as 
system alarms) were taking place. Using the baseline interface (MOCU v2) when controlling two 
USVs, participants were five times more likely to collide with a vessel that did not appear on radar. 
With the MOCU v3.1 interface, collisions with vessels not displayed on radar were twice as likely as 
those with sensor information available. Two participants actually reported seeing the obstacle vessel 
in the video window prior to collision but because they did not have a radar image to confirm, they 
were not sure of the impending threat and took no action to avoid collision. These findings indicate a 
very narrow window of opportunity that the operator attention can stray from direct USV video 
monitoring without the added assistance of reliable radar or other collision avoidance obstacle 
detection alarms. 
Thus, USV system functions for obstacle avoidance – missing in this simulation – may be critical 
in supporting multi-USV operations, including improved sensor capability to detect and warn of 
potential collisions. Although the HCI enhancements implemented assistance to operators’ ability to 
monitor video displays, the lack of an active warning system leaves the USV vulnerable to collisions 
with undetected objects, particularly during periods of heavy workload (alarms or other visual 
distractions across multiple USVs). 
7.3 ASSESSMENT OF GAME CONTROLLER INPUT DEVICE 
User performance while using the game controller indicates that game-type controllers represent a 
trainable and effective option to control a USV across manual-vector-waypoint operational modes. 
The addition of the game type controller was seen as an integral component of the overall MOCU 
v3.1 interface package. As indicated during post-test discussions, a high percentage of the 
participants engage in video games on a regular basis and were already familiar with the basic 
operation of the X-box type controller. We suspect that this is not atypical of the enlisted Navy 
population in general. Because the USV functions were mapped to the controller following “standard

---
**[Page 58]**

50
gaming conventions” where possible, the button and joystick assignments made intuitive sense to the 
participants who were able to learn to drive the USV in relatively short order. Although a controller 
mapping diagram was provided during training and available to participants throughout the scenario, 
researchers rarely observed participants needing to consult the diagram. In most cases, participants 
operated the controller by feel and rarely had to visually site the buttons or joystick in order to 
execute a command. This ability to “drive by feel” then afforded significantly more visual attention 
resources to monitoring the map, video windows, and status indicators. While the MOCU v3.1 
interface still relies on menus for execution of some lower order tasks, menus are called up and 
options prosecuted through an easy-to-use button configuration on the controller that is similar to 
menu strategies found in many video games. This is in contrast to the multilayered pull-down menus 
in the baseline HCI that required participants to control and visually monitor the location of an 
onscreen cursor to make selections. 
7.4 IMPLICATIONS FOR SINGLE USV OPERATION 
The Phase IV study conducted as a follow-on effort to the multiple USV work indicates that the 
HCI enhancements made to support multiple USV operation had a significant (positive) effect in 
controlling a single USV. While some improvements were noted across all task domains, the highly 
significant improvement in response to alarm indications was noteworthy. Since current plans call for 
developing a redesigned USV to support MCM operations onboard the LCS, in a single USV 
configuration, these results have an immediate impact on near-term LCS HCI design. 
7.5 EASE OF USE AND TRAINING IMPLICATIONS 
The USV mission simulator proved to be a valuable tool for evaluating the potential of the HCI 
products from this project related to positive training impact. The simulation used for these studies 
has potential for being an easy-to-use training method allowing users to gain experience in USV 
operations in a cost-effective manner. The short time period to train and familiarize users with the 
operations of MOCU indicates an easy transition from Baseline MOCU or an efficient introduction 
for a novice operator. These interface design properties should also be considered for other humanrobotic interfaces on LCS. 
7.6 RECOMMENDATION FOR FURTHER TESTING 
The current set of studies had limitations with respect to validity of results. First, the laboratory 
simulation estimated the results of live video, radar, and other sensors. The degree of difference 
between the real operational sensors and the simulation could affect results in a positive or negative 
manner. For example, the HCI “windshield” view was created by “stitching” together video images 
from four discrete cameras into one continuous panoramic view. While this feature was well received 
by the subjects using simulated video, trials with real video feeds from the actual USV cameras 
should be performed to determine the effects of distortion or blind spots created at the seams where 
the images meet. Second, the simulation of a USV with no active radar stressed the range of system 
performance from all systems working toward a degraded state. In reality, tactics and operations 
could reduce the effects of degraded radar, e.g., the degraded USV could follow the fully operational 
one, or a mandated reduced speed or other cautionary methods could be employed. In reality, the 
mission could be postponed for sensor repairs depending on urgency or another robot inserted. 
Obstacle detection systems could be incorporated, but increase the cost of the USV platform. This 
cost must be weighed against the risk of collision and need to collect mission data under all 
circumstances of environmental clutter. Thus, further tests of operational results with operational 
USVs on the water would increase the validity of HCI design decisions made during this ONR 
project.

---
**[Page 59]**

51
8. REFERENCES
Ahumada, A. (2010) A Model for Search and Detection of Small Targets. Journal of Vision, vol 10 
(7), p 11.
Ahumada, A. (2011) Searching the Horizon for Small Targets. Journal of Vision, September 23, vol 
11, no. 11 article 500. http://www.journalofvision.org/content/11/11/500.short 
Baldwin, J., Basu, A., and Zhang, H. (1998) Predictive Windows for Delay Compensation in 
Telepresence Applications. Proc. IEEE Int. Conf. on Robotics and Automation (ICRA), 2884-2889. 
Baldwin, J., Basu, A., and Zhang, H. (1999) Panoramic Video with Predictive Windows for 
Telepresence Applications. Proc. IEEE Int. Conf. on Robotics and Automation (ICRA), 1922-1927. 
Barnes, M., Chen, J., Jentsch, F., and Haas, E. (2006) Soldier Interactions with Aerial and Ground 
Robots in Future Military Environments. NATO Report HFM-135. (Unclassified) 
Bejczy, A. K., Kim, W. S., and Venema, S. C. (1990) The Phantom Robot: Predictive displays for 
Teleoperation with Time Delay. Proc. IEEE Int. Conf. on Robotics and Automation (ICRA'90), 546-
551. 
Cummings, M. L. and Guerlain, S. (2004) An Interactive Decision Support Tool for Real-time Inflight Replanning of Autonomous Vehicles. American Institute of Aeronautics and Astronautics 
Unmanned Unlimited Systems, Technologies, and Operations, September 2004. 
Endsley, M. R., and Garland, D. I. (2000) Pilot Situation Awareness Training in General Aviation. In 
Proceedings of the International Ergonomics Society/Human Factors and Ergonomics Society 2000 
Congress, San Diego Ca. July 31-Aug 4th, 2000. pp 2-359. 
Fowler, M. (2005) The New Methodology. Web on-line published article. 
http://www.martinfowler.com/articles/newMethodology.html#FlavorsOfAgileDevelopment 
Hancock, P.A., Mouloua, M., Gilson, R., Szalma, J. and Oron-Gilad, T. (2007) Provocation: Is the 
UAV control Ratio the Right Question? Ergonomics In Design, Winter 2007, Human Factors and 
Ergonomics Society, Santa Monica CA. 
Jones, D., and Endsley, M. (2000) Overcoming Representational Errors in Complex Environments. 
Human Factors, vol 42(3), pp 367-378. 
Kellmeyer, D. and Bernhard, R. (2009) Multi-Robot Operational Control Unit (MOCU) version 1.0 
Usability and Heuristic Evaluation Report, SPAWAR Systems Center Pacific San Diego (unreleased 
tech report) January 2009. 
Kellmeyer, D., McWilliams, M., and Bernhard, R. (2009) Multi-Robot Operational Control Unit 
(MOCU) V1.0 Usability and Heuristic Evaluation Report, SPAWAR Systems Center Pacific 27 
January 2009. 
Klein, G. (1993) A Recognition-Primed Decision (RPD) Model of Rapid Decision Making. In G.A. 
Klein, J. Orasanu, R. Calderwood, and C.E. Zsambok (Eds.), Decision making in action: Models and 
methods, Norwood NJ: Ablex. 
Mathan, S., Hyndman, A., Fischer, K., Blatz, J., and Brams, D. (1996) Efficacy of a Predictive 
Display, Steering Device, and Vehicle Body Representation in the Operation of a Lunar Vehicle. 
Proceedings of the ACM SIG-CHI 96. 
http://acm.org/sigchi/chi96/proceedings/intpost/Mathan/ms_txt.HTM

---
**[Page 60]**

52
McWilliams, M. (2009) User Review for USV MOCU v3 (v. 8) Wireframe Displays and Design 
Strategies Aug 8, 2009, unpublished Technical Document, SPAWAR Systems Center Pacific, San 
Diego CA. 
McWilliams, M., Osga, G. Kellmeyer, D. and Viraldo, J. (2010) Usability Test for Baseline Multirobot Control Unit (MOCU). Unpublished Test Report, SPAWAR Systems Center Pacific, San 
Diego CA. August. 
McWilliams, M., Osga, G., and Kellmeyer, D. (2010) Usability Test Plan for Multi-robot Control 
Unit (MOCU) December, unpublished report SPAWAR Systems Center Pacific, San Diego CA. 
McWilliams, M. (2011) Recommendations from USV MOCU v3 User Testing, unpublished 
technical report, SPAWAR Systems Center Pacific San Diego CA. 
Miller, J. (2006) LCS ASW WCM Phase I Manning Analysis Report. Alion Science and Techology 
MAandD Operation. Orlando FL. 
Mitchell, P. M., Cummings, M. L., and Sheridan, T. B. (2005). Mitigation of Human Supervisory 
Control Wait Times through Automation Strategies. Cambridge, MA: MIT Humans and Automation 
Laboratory. 
Mouloua, M., Gilson, R., & Hancock, P.A. (2003). Designing controls for future unmanned aerial 
vehicles. Ergonomics in Design, 11 (4), 6-11 
Osga, G. Van Orden K. Campbell, N. Kellmeyer, D. and Lulue D. (2002) Design and Evaluation of 
Warfighter Task Support Methods in a Multi-Modal Watchstation. Space and Naval Warfare 
Systems Center San Diego Tech Report 1874. 
Osga, G., Linville, M., Kellmeyer, D., Griffith, C., Williams, E., Feher, B., Adams, R., Lulue, D., 
and Edwards, B. (2005) Advanced Interface Display (AID) Guidelines and Lessons Learned. 
Technical Report (in press), Space and Naval Warfare Systems Center San Diego CA. 
Parasurman, R., Mouloua, M., Molloy, R., & Hilburn, B. (1996). Monitoring of Automated Systems. 
In Automation and Human Performance, R. Parasurman & M. Mouloua, Eds. Lawrence Erlbaum 
Associates, pp. 91-116. 
Parasurman, Molloy and Singh (1993) Performance Consequences of Automation Induced 
Complacency. International Journal of Aviation Psychology, 3(1), pp 1-23. 
Powell, D. (2011) Unmanned Surface Vehicle Monitoring and Control Human Computer Interface 
(USV HCI) Software Transition Plan. Unpublished Report Space and Naval Warfare Systems Center 
San Diego CA. June. 
Sheridan, T. B. (1992). Telerobotics, Automation and Human Supervisory Control. Cambridge, MA: 
The MIT Press. 
Vicente, K. J. 1990. A Few Implications of an Ecological Approach to Human Factors, Edited by K. 
Harwood, Human Factors Society Bulletin, vol.33, no. 11. 
Vicente, K. J. 1999. Cognitive Work Analysis. Lawrence Erlbaum Associates, Mahwah NJ.

---
**[Page 61]**

A-1 
APPENDIX A. SCENARIO SCRIPT 
Participant # Date
USV One USV Two Observations / 
S Comments imulation Event Expected COA Yes No Simulation Event Expected COA Yes No
MS "Take control of USV1" Selects correct USV.
MS "Activate radar and display 
contacts for USV1"
Selects: Activate, Display. 
Contacts up by WP1.
MS "In vector mode, set course to 
WP1, 20 knts."
Sets correct heading, 
speed.
MS "At WP1 check with MS to 
execute route."
USV 1 reaches WP1. Reports WP1 to MS.
MS " Select and execute Southern 
Route for USV 1 in waypoint mode." Correct Rte executed.
USV 1 heads to WP2. MS - "Take control of 
USV 2 ". Selects correct USV.
USV 1 continues to WP2.
MS - In vector mode, 
set course to WP1, 20 
knts
Sets correct heading, 
speed.
USV passes oil rig on SB. Oil rig reported to MS.
MS "At WP1 check
with MS to execute 
route."
MS "Use PTZ to inspect oil rig for 
adversaries". Able to use PTZ. USV 2 reaches WP1, heads to WP2. Reports WP1 to MS.
USV 1 continues to WP2.
MS Select and execute 
Northern route for 
USV2.
Executes correct route.
USV 1 continues to WP2. USV 2 heads to WP2.
USV 1 continues to WP2. Sailboat traffic in 
display / radar. Traffic reported to MS.
Temp alarm light flashes red. Reports alarm within 10 
secs.
MS "Change to vector 
mode, reduce speed to 
10 kts."
Vector mode selected. 
Speed set at 10 kts.
MS "USV1 has high temp alarm. 
Shut down both engines." Selects: Stop Engines. Operator continues in vector mode. Avoids hitting sailboats.

---
**[Page 62]**

A-2 
Alarm light clears, MS "Restart 
engines & resume route."
Reports alarm clear within 
10 secs. Resumes route.
MS "When USV 2 is 
clear of traffic, resume 
route."
Resumes waypoint mode 
AFTER clear of sailboat 
traffic.
USV1 continues to WP2. USV2 continues to 
WP2.
 Temp. alarm flashes again. Reports alarm to MS 
within 10 secs.
USV2 continues to 
WP2.
MS "Pause route and put engines in 
neutral to allow alarm to clear." Selects pause, neutral.
USV2 reaches WP2, 
heads to
WP3.
Reports WP2 to MS.
Alarm light goes off. Reports alarm clear within 
10 secs.
USV2 continues to 
WP3.
MS "Resume Waypoint Route on 
USV1".
Places in forward. 
Resumes route.
USV 1 reaches WP2, heads to WP3. Reports WP2 to MS. 2 boats in collision 
path.
Executes Emergency 
Maneuver in time.
USV1 continues to WP3. USV2 reaches WP3, 
heads to WP4. Reports WP3 to MS
USV1 continues to WP3. USV2 continues to 
WP4.
USV1 continues to WP3. Boat approaches head 
on collision.
Executes Emergency 
Maneuver in time.
USV1 reaches WP3, heads to WP4. Reports WP3 to MS. USV2 continues to 
WP4.
Container ship in direct path of new 
heading. Reports contact to MS. USV2 continues to WP4.
MS: Monitor movement of contact. 
Switch to vector mode and adjust 
course as necessary.
Avoids exclusion zone. USV2 continues to 
WP4.
USV continues to WP4.
Pursuit boat 
approaches from aft 
port.
Reports correct location 
of pursuit boat before 
passing.
USV reaches WP4 (Mission Area). Reports WP4 to MS. USV reaches WP4 
(Mission Area). Reports WP4.

---
**[Page 63]**
*(This page contains a figure/chart/image not captured in text)*

B-1 
APPENDIX B. VOLUNTARY CONSENT FORM

---
**[Page 64]**
*(This page contains a figure/chart/image not captured in text)*

B-2

---
**[Page 65]**
*(This page contains a figure/chart/image not captured in text)*

B-3

---
**[Page 66]**
*(This page contains a figure/chart/image not captured in text)*

B-4

---
**[Page 67]**

C-1 
APPENDIX C. BACKGROUND QUESTIONNAIRE 
Demographic and Experience Questionnaire 
Branch of Service ___________________________ 
Occupational Specialty ________________________ 
Years of Service _____________________________ 
Rank/Rate __________________________________ 
1. How many years of experience do you have in the area of ASW or MCM? 
None
Less than 1 year
1-2 years
2-5 years
More than 5 years
2. How many hours of USV operational experience do you have? 
None 
Less than 2 hours
2-5 hours
5-10 hours
More than 10 hours
3. How many hours of USV simulator experience do you have? 
None
1-2 times
3-4 times
5-6 times
7 times or more
4. Have you operated a USV during the past 6 months? 
Yes
No

---
**[Page 68]**

C-2

---
**[Page 69]**

D-1 
APPENDIX D. TRAINING PROTOCOL 
Welcome Participants
 Discuss purpose of the study – to capture data for improving the user interface. 
 Discuss the nature of participation – conduct a simulated ASW mission. 
 Assure it is not a test of his / her skills. 
 Ensure confidentiality and have participants read the Informed Consent Document (including 
Privacy Act Statement) and sign the ICD if they agree to participate. 
 Have Participants Complete Background Survey. 
 
Review Upper Monitor Screen (Map and Status) 
 DNC (Use mouse to zoom in / out) 
o Boat icons, inc compass rose and speed header 
o North / South routes / WP markers 
o Operations area and Exclusion Zone 
 Vehicle Status Information (color coding) 
 Mission Analysis / Event Viewer not active 
Review Lower Monitor Screen (Video and Dashboard) 
o Video Window Layout 
 Main Windshield (Stiched video) 
 PTZ, Aft View, Forward view of Other USV 
o Speed / Rudder Position / Throttle & Gear 
o Waypoint previews 
o Control Mode and Radar Status 
o Alarm Icons and Alerts 
Walkthrough Controller Mapping 
 Taking / Switching Control of USVs (note screen changes) 
 Using the Camera Controls 
o Toggle PTZ to Camara Can (note camera arrows) 
o Pan / Tilt , Zoom / Home 
 Driving in Vector Mode 
o Steering 
o Speed Set 
 Manual Mode Override (Teleop) 
o Steering /Speed 
o Pull back for idle speed 
 Driving in Waypoint Mode 
o Executing Routes 
o Pause / Resume 
 Other Pie Menu Functions 
o Enabling Radar - Active / Contacts 
o Starting / Stopping Engines 
o Transmission gear select / idle 
Download and Run Practice Scenario

---
**[Page 70]**

*(no extractable text on this page)*

---
**[Page 71]**

E-1 
APPENDIX E. MISSION BRIEFING 
2 Boats: 
This mission involves deployment of 2 USVs from the Littoral Combat Ship, USS Freedom in 
the Aegean Sea off the coast of Greece. We will be conducting ASW operations using bi-static sonar 
surveillance techniques. For this scenario we will be transiting the USVs to the mission area but will 
not be running search tracks. You will act as the operator, controlling and monitoring both USVs as 
they transit to the mission area and I will act as the mission supervisor. The USV routes have been 
reviewed and entered into MOCU and are ready to be executed. Both USVs have already been 
launched, systems have been checked out and are ready to have you take control. At the direction of 
the mission supervisor, you will take control of USV 1 and drive the USV away from the LCS in 
vector mode toward Waypoint 1. When USV 1 reaches Waypoint 1 (WP1), request permission from 
the Mission Supervisor to execute the route in auto mode. After USV 1 has reached WP1, directions 
will be given to take control of USV 2. You will then drive USV 2 to Waypoint 1 for its route and 
again request permission to execute the USV 2 route. For this mission, the radar on USV 2 is 
inoperable. Radar from the host ship provides coverage up to WP 2 but from there on there is no 
reliable radar for USV2 so be extra vigilant in monitoring your video cameras. 
1 Boat: 
This mission involves deployment of 2 USVs from the Littoral Combat Ship, USS Freedom in 
the Aegean Sea off the coast of Greece. We will be conducting ASW operations using bi-static sonar 
surveillance techniques. For this scenario you will be transiting one of the USVs to the mission area 
but will not be running search tracks. You will act as the operator, controlling and monitoring the 
USV as it transits to the mission area and I will act as the mission supervisor. The USV route has 
been reviewed and entered into MOCU and is ready to be executed. The USV has already been 
launched, systems have been checked out and is ready to have you take control. At the direction of 
the mission supervisor, you will take control of the USV and drive away from the LCS in vector 
mode toward Waypoint 1. When the USV reaches Waypoint 1 (WP1), request permission from the 
Mission Supervisor to execute the route in auto mode. For this mission, the radar on the USV may 
not be operating properly. Radar from the host ship provides coverage up to WP 2 but from there on 
there is no reliable radar for so be extra vigilant in monitoring your video cameras. 
You will need to make several reports to the MS during the mission: 
o As each waypoint is reached, report the WP reached and the new heading and speed 
for the next track. 
o Report all contacts observed along the route and whether they present a potential 
collision hazard that may require change of course. 
o If there are any immediate collision hazards, use the emergency maneuver control to 
avert contact. Report these as conditions allow. 
o Report any system problems to MS, including alarms and cautions.

---
**[Page 72]**

*(no extractable text on this page)*

---
**[Page 73]**

F-1 
APPENDIX F. EXIT SURVEY
Exit Survey 
1. I found it easy to use for monitor the status of each USV separately.
Strongly Disagree
Disagree
Neutral
Agree
Strongly Agree
Comments_____________________________________________________________________
_________________________________________________________________________________
_________________________________________________________
2. I had difficulty monitoring the status of both USVs at the same time.
Strongly Disagree
Disagree
Neutral
Agree
Strongly Agree
Comments_____________________________________________________________________
_________________________________________________________________________________
_________________________________________________________
3. I found it easy to assess the immediate environment using the USV cameras.
Strongly Disagree
Disagree
Neutral
Agree
Strongly Agree
Comments_____________________________________________________________________
_________________________________________________________________________________
_________________________________________________________

---
**[Page 74]**

F-2 
4. I had difficulty keeping track of the USV camera orientation (direction of view).
Strongly Disagree
Disagree
Neutral
Agree
Strongly Agree
Comments_____________________________________________________________________
_________________________________________________________________________________
_________________________________________________________ 
5. I found it was easy to MANUALLY set and maintain the desired speed of the USVs.
Strongly Disagree
Disagree
Neutral
Agree
Strongly Agree
Comments_____________________________________________________________________
_________________________________________________________________________________
_________________________________________________________
6. I found it was easy to MANUALLY set and maintain the desired course heading of the USVs. 
Strongly Disagree
Disagree
Neutral
Agree
Strongly Agree
Comments_____________________________________________________________________
_________________________________________________________________________________
_________________________________________________________

---
**[Page 75]**

F-3 
7. I found the interface provided the necessary visual information for orientation while navigating 
and performing mission tasks.
Strongly Disagree
Disagree
Neutral
Agree
Strongly Agree
Comments_____________________________________________________________________
_________________________________________________________________________________
_________________________________________________________
8. I had difficulty locating necessary information on the display to perform mission tasks. 
Strongly Disagree
Disagree
Neutral
Agree
Strongly Agree
Comments_____________________________________________________________________
_________________________________________________________________________________
_________________________________________________________
8. The most difficult part of controlling two USVs is: 
______________________________________________________________________________
_________________________________________________________________________________
_________________________________________________________
9. If I could change one thing about the system status displays it would be: 
______________________________________________________________________________
_________________________________________________________________________________
_________________________________________________________

---
**[Page 76]**

F-4 
10. If I could change one thing about the camera displays it would be: 
______________________________________________________________________________
_________________________________________________________________________________
_________________________________________________________ 
11. If I could change one thing about the digital chart displays it would be: 
______________________________________________________________________________
_________________________________________________________________________________
_________________________________________________________

---
**[Page 77]**

5f. WORK UNIT NUMBER
REPORT DOCUMENTATION PAGE Form Approved
OMB No. 0704-01-0188
The public reporting burden for this collection of information is estimated to average 1 hour per response, including the time for reviewing instructions, searching existing data sources, gathering 
and maintaining the data needed, and completing and reviewing the collection of information. Send comments regarding this burden estimate or any other aspect of this collection of information, 
including suggestions for reducing the burden to Department of Defense, Washington Headquarters Services Directorate for Information Operations and Reports (0704-0188), 1215 Jefferson 
Davis Highway, Suite 1204, Arlington VA 22202-4302. Respondents should be aware that notwithstanding any other provision of law, no person shall be subject to any penalty for failing to 
comply with a collection of information if it does not display a currently valid OMB control number.
PLEASE DO NOT RETURN YOUR FORM TO THE ABOVE ADDRESS.
1. REPORT DATE (DD-MM-YYYY) 2. REPORT TYPE 3. DATES COVERED (From - To)
4. TITLE AND SUBTITLE 5a. CONTRACT NUMBER
5b. GRANT NUMBER
5c. PROGRAM ELEMENT NUMBER
5d. PROJECT NUMBER
5e. TASK NUMBER
6. AUTHORS
7. PERFORMING ORGANIZATION NAME(S) AND ADDRESS(ES) 8. PERFORMING ORGANIZATION 
 REPORT NUMBER
10. SPONSOR/MONITOR’S ACRONYM(S)
11. SPONSOR/MONITOR’S REPORT
 NUMBER(S)
9. SPONSORING/MONITORING AGENCY NAME(S) AND ADDRESS(ES)
12. DISTRIBUTION/AVAILABILITY STATEMENT
13. SUPPLEMENTARY NOTES
14. ABSTRACT
15. SUBJECT TERMS
16. SECURITY CLASSIFICATION OF:
a. REPORT b. ABSTRACT c. THIS PAGE
17. LIMITATION OF
 ABSTRACT
18. NUMBER
 OF
 PAGES
19a. NAME OF RESPONSIBLE PERSON
19B. TELEPHONE NUMBER (Include area code)
Standard Form 298(Rev. 8/98)
Prescribed by ANSI Std. Z39.18
06–2013 Final
Unmanned Surface Vehicle Human-Computer Interface 
for Amphibious Operations
Glenn Osga, Mike McWilliams, Darren Powell, David Kellmeyer, 
Jerry Kaiwi, Al Ahumada
Space and Naval Warfare Systems Center Pacific (SSC Pacific)
San Diego, CA 92152–5001 TR 2022
Office of Naval Research
Warfighter Performance Division, Code 34
Arlington, VA 22203-1995 
ONR
Approved for public release.
This report describes a multiyear research effort conducted by SPAWAR Systems Center Pacific (SSC Pacific) investigating 
Human-Computer Interface (HCI) issues associated with operating unmanned surface vehicles (USVs). An iterative user-design 
process was used that resulted in the development of an enhanced HCI design. The primary focus of this effort was to investigate 
improvements to the baseline HCI design of the SPAWAR Multi-Operator Control Unit (MOCU) software to support 
simultaneous operation of multiple USVs by a single operator. 
A number of significant design enhancements were made to the baseline HCI as it was adapted to support multiple USVs. The 
enhancements included integrated visualization of video and graphics combined with multi-modal input and output using synthetic 
speech output and game-controller input. Significant gains in performance times and error reduction were found with the enhanced 
design. Following the ONR effort, Naval Sea Systems Command (NAVSEA) LCS Mission Modules Program Office (PMS 420) 
supported the development of a prototype HCI design for operation of a single USV. While overall results of simulator-based 
usability evaluations indicate improved operator performance, the researchers conclude that improvements in on-board sensor 
capabilities and obstacle avoidance systems may still be necessary to safely support simultaneous operation multiple USVs in 
cluttered, complex transit environments.
Mission Area: Command and Control,
Unmanned Surface Vehicles; Human-Computer Interface; Amphibious Operations
M. McWilliams
U U U U 78 (619) 553–6654

---
**[Page 78]**

*(no extractable text on this page)*

---
**[Page 79]**

INITIAL DISTRIBUTION 
853 Archive/Stock (1) 
843 Library (2) 
853 L. Hood (1) 
56240 M. McWilliams (6) 
Defense Technical Information Center 
Fort Belvoir, VA 22060–6218 (1)

---
**[Page 80]**
*(This page contains a figure/chart/image not captured in text)*

Approved for public release.
Space and Naval Warfare Systems Center Pacific
San Diego, CA 92152-5001