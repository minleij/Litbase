# MUSCIT Hughes 2012

*Source file: MUSCIT_Hughes_2012.pdf — 58 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

AFRL-RH-WP-TR-2012-0129
Multi-UAV Supervisory Control Interface Technology (MUSCIT) 
Thomas C. Hughes
John K. Flach
Mark P. Squire
James Whalen
Infoscitex Corp.
Douglas J. Zimmer
Michael J. Patzek, Ph.D
Lt Britany A. Miller
Warfighter Interface Division
Supervisory Control Interfaces Branch
September 2012
Distribution A: Approved for public release; distribution unlimited.
AIR FORCE RESEARCH LABORATORY
711 HUMAN PERFORMANCE WING,
HUMAN EFFECTIVENESS DIRECTORATE,
WRIGHT-PATTERSON AIR FORCE BASE, OH 45433
AIR FORCE MATERIEL COMMAND
UNITED STATES AIR FORCE

---
**[Page 2]**

NOTICE AND SIGNATURE PAGE
Using Government drawings, specifications, or other data included in this document for any purpose 
other than Government procurement does not in any way obligate the U.S. Government. The fact that 
the Government formulated or supplied the drawings, specifications, or other data does not license the 
holder or any other person or corporation; or convey any rights or permission to manufacture, use, or 
sell any patented invention that may relate to them. 
This report was cleared for public release by the 88th ABW Public Affairs Office and is available to 
the general public, including foreign nationals. Copies may be obtained from the Defense Technical 
Information Center (DTIC) (http://www.dtic.mil). 
 
AFRL-RH-WP-TR-2012-0129 HAS BEEN REVIEWED AND IS APPROVED FOR PUBLICATION 
IN ACCORDANCE WITH ASSIGNED DISTRIBUTION STATEMENT.
//signed// //signed//
Douglas J. Zimmer. Gregory Barbato
Program Manager Chief, Systems Control Interfaces Branch
Systems Control Interfaces Branch Warfighter Interface Division
//signed//
Michael A. Vidulich
Technical Advisor
Warfighter Interface Division
Human Effectiveness Directorate
711 Human Performance Wing
This report is published in the interest of scientific and technical information exchange, and its 
publication does not constitute the Government’s approval or disapproval of its ideas or findings.

---
**[Page 3]**

i
REPORT DOCUMENTATION PAGE Form Approved
OMB No. 0704-0188
Public reporting burden for this collection of information is estimated to average 1 hour per response, including the time for reviewing instructions, searching existing data sources, gathering and maintaining the 
data needed, and completing and reviewing this collection of information. Send comments regarding this burden estimate or any other aspect of this collection of information, including suggestions for reducing 
this burden to Department of Defense, Washington Headquarters Services, Directorate for Information Operations and Reports (0704-0188), 1215 Jefferson Davis Highway, Suite 1204, Arlington, VA 22202-
4302. Respondents should be aware that notwithstanding any other provision of law, no person shall be subject to any penalty for failing to comply with a collection of information if it does not display a currently 
valid OMB control number. PLEASE DO NOT RETURN YOUR FORM TO THE ABOVE ADDRESS.
1. REPORT DATE (DD-MM-YYYY)
01-09-2012
2. REPORT TYPE
Other
3. DATES COVERED (From - To)
1 Jun 2012 – 31 Aug 2012
4. TITLE AND SUBTITLE
Multi-UAV Supervisory Control Interface Technology (MUSCIT)
5a. CONTRACT NUMBER
IN-HOUSE
5b. GRANT NUMBER
5c. PROGRAM ELEMENT NUMBER
63231F
6. AUTHOR(S)
Thomas C. Hughes, John K. Flach, Mark P. Squire, James Whalen
Douglas J. Zimmer, Michael J. Patzek Ph.D., Lt Britany A. Miller
5d. PROJECT NUMBER
2830
5e. TASK NUMBER
 02
5f. WORK UNIT NUMBER
 28302923
7. PERFORMING ORGANIZATION NAME(S) AND ADDRESS(ES) 8. PERFORMING ORGANIZATION REPORT 
 NUMBER
Infoscitex Corporation
4027 Colonel Glenn Highway
Dayton, Ohio 45431
9. SPONSORING / MONITORING AGENCY NAME(S) AND ADDRESS(ES) 10. SPONSOR/MONITOR’S ACRONYM(S)
Air Force Materiel Command
Air Force Research Laboratory
711 Human Performance Wing
Human Effectiveness Directorate
Warfighter Interface Division
Supervisory Control Interfaces Branch
Wright-Patterson AFB OH 45433-7511
711 HPW/RHCI
11. SPONSOR/MONITOR’S REPORT 
 NUMBER(S)
AFRL-RH-WP-TR-2012-0129
12. DISTRIBUTION / AVAILABILITY STATEMENT
Distribution A: Approved for public release; distribution unlimited.
 13. SUPPLEMENTARY NOTES 
88 ABW/PA Cleared 01/25/2013; 88ABW-2013-0334. 14. 
The tremendous success of UAVs has seen the role of unmanned systems expand well beyond the mission for which they were originally 
intended. One can hardly imagine a role which unmanned systems will not eventually be applied. The future use of UAVs secure, the 
challenge for unmanned air systems (UAS) developers has shifted from one of demonstrating their value on the battlefield to one of 
increasing the efficiency of their use. The Multi-UAV Supervisory Control Interface Technology (MUSCIT) program, a research initiative 
sponsored by the Air Force’s Supervisory Control Interface Branch of the Human Effectiveness Directorate (711HPW/RHCI), was tasked 
to investigate operator interface control issues associated with multi-UAV control. The focus of this effort was to investigate automation 
and interface technologies that will reverse the status quo to move from multiple operators per vehicle to multiple vehicles per single 
operator.
15. SUBJECT TERMS
 
16. SECURITY CLASSIFICATION OF: 17. LIMITATION 
OF ABSTRACT
18. NUMBER 
OF PAGES
19a. NAME OF RESPONSIBLE PERSON
Douglas J. Zimmer
a. REPORT
 Unclassified b. ABSTRACTUnclassified 
c. THIS PAGE
 Unclassified 
SAR 58 19b. TELEPHONE NUMBER (include area 
code)
 Standard Form 298 (Rev. 8-98) Prescribed by ANSI Std. 239.18

---
**[Page 4]**

ii
THIS PAGE INTENTIONALLY LEFT BLANK.

---
**[Page 5]**

iii
Table of Contents
1.0 INTRODUCTION 1
2.0 METHOD 8
2.1 APPARATUS 8
2.1.1 MUSCIT Spiral 3 Simulation Architecture 8
2.1.2 Communications 12
2.2 DATA COLLECTION LAYOUT 12
2.3 EXPERIMENTAL DESIGN 13
2.3.2 Design 13
2.3.3 Experimental Trials 15
2.3.4 Dependent Variables 22
2.4 PROCEDURE 23
3.0 DATA ANALYSIS & RESULTS 24
3.1 INFERENTIAL ANALYSES 24
4.0 SPIRAL 3 FLIGHT TEST 26
4.1 FLIGHT TEST OBJECTIVES 27
4.2 METHOD 27
4.2.1 Apparatus 27
4.2.2 Communications 30
4.2.3 Data Collection Layout 31
4.2.4 Flight Test Design 31
4.2.5 Dependent Variables 35
4.2.6 Flight Test Operations 36
4.3 FLIGHT TEST RESULTS 37
5.0 DISCUSSION 39
6.0 CONCLUSIONS 46
7.0 REFERENCES 48
8.0 LIST OF ACRONYMS AND ABBRIVIATIONS 50

---
**[Page 6]**

iv
LIST OF FIGURES
FIGURE 1. ILLUSTRATED ARCHITECTURE FOR THE MUSCIT SPIRAL 3 SIMULATION .................................................8
FIGURE 2. SAMPLE LAYOUT OF THE CONTROL STATION.............................................................................................9
FIGURE 3. FLAMES® SCENARIO DEVELOPMENT ENVIRONMENT............................................................................11
FIGURE 4. MUSCIT SPIRAL 3 DATA COLLECTION CONFIGURATION.......................................................................13
FIGURE 5. OPERATION LOOKOUT AREA OF OPERATIONS .....................................................................................17
FIGURE 6. ANNOTATED PHOTO IMAGERY ................................................................................................................18
FIGURE 7. RTVS AUTOMATIC TARGET TRACKER.....................................................................................................19
FIGURE 8. MACROGRID OVERLAY OF AREA OF OPERATIONS FOR OPERATION OVERLOOK.................................21
FIGURE 9 SUMMARY SIMULATION DATA PLOTS .....................................................................................................25
FIGURE 10. PARTICIPANT SUBJECTIVE RATINGS ........................................................................................................26
FIGURE 11. MLB CC BAT 3 UAV............................................................................................................................28
FIGURE 12. RELIEF MAP AND SATELLITE VIEW OF CAMP ATTERBURY......................................................................29
FIGURE 13. ILLUSTRATED ARCHITECTURE FOR THE FLIGHT TEST GROUND STATIONS................................................30
FIGURE 14. MUSCIT SPIRAL 3 FLIGHT TEST DATA COLLECTION CONFIGURATION .................................................31
FIGURE 15. OPERATION OVERLOOK AREA OF OPERATIONS (FLIGHT TEST)..............................................................33
FIGURE 16. ANNOTATED PHOTO IMAGERY FOR FLIGHT TEST.....................................................................................34
FIGURE 17. SUMMARY FLIGHT TEST DATA PLOTS ......................................................................................................38
FIGURE 18. PARTICIPANT SUBJECTIVE RATINGS ........................................................................................................39

---
**[Page 7]**

v
LIST OF TABLES
TABLE 1. MUSCIT SPIRAL 3 EXPERIMENT TRIALS .....................................................................................................14
TABLE 2. OPERATION LOOKOUT BLUE FORCES........................................................................................................16
TABLE 3. PERFORMANCE MEASURES COLLECTED DURING MUSCIT SPIRAL 3 SIMULATION ........................................22
TABLE 4. DESCRIPTIVE STATISTICS FOR DEPENDENT MEASURE COLLECTED DURING MUSCIT SPIRAL 3 SIM..............24
TABLE 5. DESCRIPTIVE STATISTICS FOR SUBJECTIVE DATA COLLECTED DURING MUSCIT SPIRAL 3 SIM ...................26
TABLE 6. MUSCIT SPIRAL 3 EXPERIMENT TRIALS .....................................................................................................32
TABLE 7. PERFORMANCE MEASURES COLLECTED DURING MUSCIT SPIRAL 3 FLIGHT TEST .......................................35
TABLE 8. DESCRIPTIVE STATISTICS FOR FLIGHT TEST DEPENDENT MEASURE................................................................37
TABLE 9. DESCRIPTIVE STATISTICS FOR FLIGHT TEST SUBJECTIVE DATA.....................................................................38

---
**[Page 8]**

1
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
1.0 INTRODUCTION
The military utility of unmanned air vehicles (UAV) is no longer in doubt (Hq USAF, 2009, 
OSD, 2007). The ability to provide persistent surveillance over the battlespace has been cited on 
several occasions as the critical capability that led to the capture and/or termination of numerous 
high value targets (HVTs) in ongoing conflicts in Iraq and Afghanistan (Cullen, 2011). The 
tremendous success of UAVs has seen the role of unmanned systems expand well beyond the 
mission for which they were originally intended. One can hardly imagine a role which 
unmanned systems will not eventually be applied. The future use of UAVs secure, the challenge 
for unmanned air systems (UAS) developers has shifted from one of demonstrating their value 
on the battlefield to one of increasing the efficiency of their use. Given the increased demand for 
such assets, the using community must find ways to reverse the manning ratio for their use. 
Current concepts of operations require multiple operators for every unmanned system, a ratio 
that cannot be sustained if the projected increase in use is to be believed. If the anticipated 
expanded use of UAVs is to be realized, a more desirable manning concept must be identified.
The Multi-UAV Supervisory Control Interface Technology (MUSCIT) program, a research 
initiative sponsored by the Air Force’s Supervisory Control Interface Branch of the Human 
Effectiveness Directorate (711HPW/RHCI), was tasked to investigate operator interface control 
issues associated with multi-UAV control. The focus of this effort was to investigate automation 
and interface technologies that will reverse the status quo to move from multiple operators per 
vehicle to multiple vehicles per single operator.
Given this charge, the dominant question became, ‘How many UAVs can a single operator 
effectively control?’ We quickly discovered that, like all such questions, it depends on the 
context and the demands associated with particular situations. In responding to this question, the 
MUSCIT program executed a series of developmental spirals, each spiral consisting of a 
simulation and flight test phase; and each phase expanding on the complexity of situations 
associated with multi-UAV operations. Early spirals focused exclusively on static tasking,
emphasizing point surveillance and the demands associated with providing persistent 
surveillance across multiple locations (Hughes et.al, 2009, Hughes, et.al, 2011). The second 
spiral extended the emphasis from merely point surveillance to route surveillance and area 
search. The idea being that in addition to the sensor control and monitoring activities associated 
with route surveillance and area search, these tasks would also require operators to attend to
vehicle control and mission management functions as well (Hughes et.al., In Press). In each of 
these spirals the primary research question centered on the impact on operator performance as 
the number of vehicles increased. In each case, the addition of a vehicle coincided with an 
increase in tasking as each vehicle was assigned a point surveillance location, a route segment or 
an area to be searched. Ultimately, the measure of success was the ability to demonstrate that 
one operator (equipped with an advanced control station and associated automated systems) 
could perform as well as two operators performing comparable tasks. 
Findings from both Spirals 1 and 2 were relatively predictable. Under certain conditions, a 
single operator controlling multiple vehicles executing multiple tasks could perform as well as a 
single operator performing a single task (or multiple operators performing multiple tasks).

---
**[Page 9]**

2
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
However, like all finite systems, there exists a limit to their capacity. We learned a great deal 
about many of the issues that limit capacity and operator interface concepts that can expand that 
capacity. We also, to some extent, demonstrated the feasibility of multi-UAV control, at least 
within the context of the mission tasks and scenarios we investigated. What we didn’t learn was 
how operators truly responded to the dynamics of operational situations and how they adapted
their strategies to compensate for limits in the capacities of their systems. The full-mission 
scenario conducted as a demonstration during the Spiral 2 simulation provided some insight into 
how operators really think about their task. We were able to observe how they adaptively 
reacted to situations that posed significant problems to task execution and challenged their ability 
to successfully perform a mission. Such situations force the competent operator to move beyond 
standard protocols and engage in true problem solving behavior. Given their inability to 
effectively perform all tasks, they were forced to prioritize their activities and focus on what they 
believed to be most important given their ongoing assessment of the situation. These 
demonstrations were enlightening in that they provided a means to gain a view into how 
operators “think” about their work, how they assess situations, which aspects of a given situation 
are important, and what actions are appropriate. In many cases, these priorities differed 
significantly from our own. Our surprise in their responses to the situations we placed them in 
was, to say the least, very educational. This demonstration also illustrated to us that if we are to 
gain any real insight into how UAVs are to be used, and how operators are going to interact with 
them, we must create a simulation environment that presents representative problems and 
situations and allows our operators the freedom to respond to these situations naturally. Rather 
than the controlled experiments that dominated the first two spirals, our third and final spiral 
would sacrifice experimental control for operational authenticity. Our belief was that we would 
uncover a much richer understanding of the demands and constraints of UAV operations if we 
observed operators as they engaged in the process of adapting to situations as they arose and to 
escalation in activity as the situation evolved. It was important, therefore, that the tasking and 
the flow of activity be as representative as possible.
It has become our contention that simulations should be designed to capture or “stage” what is 
believed to be the critical, deeper aspects of the situations of interest from actual field operations. 
The stronger the control one uses to shape the simulation task, the more confident one must be 
that the variables being manipulated are indeed the most critical for understanding adaptive 
control.
During Spirals 1 and 2 we discovered that there lies a natural tension between experimental 
control and situational authenticity. We find that the closer we move to actual operations, the 
less control of the sequence of activities and the associated tasks we are able to exercise. In fact, 
the data we collect and the methods for collection become fundamentally different. The 
comparisons we make to differentiate and explain variability in the data are often fundamentally 
different. We look across conditions and situations to develop an understanding of the decisions 
to be made, the nature of the challenges encountered, the trade-offs to be considered, and the 
goals to be balanced. From a control station perspective, we make observations targeted at 
understanding how the available capabilities and features of the control station support those 
strategies and help to facilitate the development and adoption of alternative strategies as 
situations dictate. We also note any problems encountered during operations and identify any 
workarounds developed by operators in response to those problems.

---
**[Page 10]**

3
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
As such, naturalistic studies do not necessarily fall under the category of a traditional experiment 
where independent variables are controlled and dependent variables are collected, but such 
naturalistic observation is essential to understanding the dynamics of complex operational 
domains (Klein, 1998). In fact, it is arguably the form of research that should precede more 
controlled experimentation. Granted, we are unable to directly observe operators in the field. 
However, we are able to create a synthetic task environment through simulation that can, to some 
extent, replicate those task conditions. The challenge is to identify those aspects of operational 
conditions that are critical to shaping the strategies adopted by operators. In essence, a 
simulation is a model of the system being simulated (Woods & Hollnagel, 2006). Our 
understanding of these essential aspects of the field of practice should be reflected in the 
development of our simulations. If our model is a reasonable representation of these critical 
aspects, our observations will be valid; if not, we run the risk of inaccuracies. In short, our task 
environment would be weak in terms of authenticity as it does not capture the demands and 
constraints of actual operations. Highly controlled experiments can have the same impact as the 
desire to carefully constrain activity to ensure experimental integrity changes the nature and flow 
of activity in ways and weaken the authenticity of the task environment. We dictate how tasks 
should be conducted which guarantees we capture the dependent variables under the specific 
conditions prescribed by the experimental matrix. 
During Spiral 3, we believe we have established a reasonable balance between these two ends of 
the spectrum (i.e., controlled experimentation through highly constrained simulation and 
authenticity through natural field observations). It is possible, through simulation, to create 
interesting situations that drive the demands and constraints in ways that force operators to 
engage in goal conflict resolution, resource allocation, and value-tradeoffs. Within such a study 
the comparisons of interest is the design of the situation itself. The data is detailed observations 
of operators’ behaviors in response to these situations, how they assessed the situation, 
information considered, strategies for dealing with uncertainty, sources of uncertainty, tradeoffs 
considered, etc. In the current spiral, our focus has not been on attempting to quantify how many 
vehicles can a single operator control, but rather how might an operator’s approach to a task 
change given the availability of multiple vehicles. Will the overhead associated with 
vehicle/sensor control outweigh the benefits of additional sensor resources? Or conversely, will 
the addition of resources increase the capacity of operators to dynamically respond to a series of 
escalating situations?
In working directly with our counterparts within the operational community, we developed a 
series of scenarios that we believe accurately reflect the demands and constraints, conflicts and 
challenges, and uncertainty and ambiguity that are typical of many of the missions currently 
being performed by operational forces engaged in ongoing combat operations.
Observations during simulation and flight test trials during the past two spirals revealed many of 
the challenges associated with attention management across multiple platforms and design issues 
relative to means by which operators selectively control and interact with individual vehicles. In 
this third spiral, enhancements to the control station baseline have been incorporated that we 
believe address many of these issues. This third spiral has been initiated with the purpose of 
assessing the appropriateness of these enhancements, as well as the value-added of specific 
automation technologies targeted at further supporting operators during multi-UAV operations.

---
**[Page 11]**

4
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
The following sections provide an overview of these enhancements and the rationale for their 
incorporation. 
Mission/Sensor Management. One of the initial focuses of the MUSCIT program was an 
emphasis on mission and sensor management. The separation of these two functions was 
precipitated largely due to the configuration prevalent in many of the current UAV ground 
control stations (i.e., Predator, Reaper, Hunter, Shadow) that include both a pilot and sensor 
operator. As one would expect, the pilot is primarily responsible for vehicle control and 
maintaining the viability of the platform to perform the mission. Likewise, the sensor operator is 
primarily responsible for control of the sensor and ensuring that the system’s sensors are 
providing the necessary imagery and sensor data required for the mission. Typically, when 
speaking of mission management one often is actually referring to vehicle or flight management;
the process of placing and maintaining the vehicle in position where its sensors can provide the 
imagery necessary to perform its assigned mission. Therefore, we often think of mission 
management as mission planning; identifying a sequence of appropriate waypoints that one 
believes will place the vehicle (and sensor) in a position that provides the necessary field of 
regard at the appropriate time. The response to the inevitable uncertainty and dynamics 
associated with military operations is to engage in the process of ongoing dynamic replanning.
Conversations with operational SMEs following our Spiral 2 simulation indicated that the 
attention required to engage in deliberate planning would be prohibitive given the demands on 
attention during active RSTA operations. Such constraints on attention forced us to reconsider 
how mission management (i.e., vehicle control) should be attended. It became clear to us that 
the sensor operators we spoke to cared to pay little attention to the vehicle or vehicle control. As 
far as they were concerned, the vehicle was a distraction; merely a means of positioning the 
sensor. All other vehicle considerations were secondary. For them it was all about the sensor. 
This attitude would seem to lend justification for the separation between vehicle and sensor 
control. In the Predator/Reaper community the pilot is responsible for vehicle control while the 
sensor operator is responsible for sensor control. To the extent that these two functions interact, 
the two operators coordinate their actions to achieve the desired effect, sensor on target.
In our experience however, vehicle and sensor control are so tightly coupled that it would seem 
reasonable to integrate these control functions into a single operation. In other sensor platforms 
a sensor guidance mode is often used to help maintain the vehicle in position to maintain sensor 
coverage. The mode couples the sensor’s view angle to the vehicles autopilot or flight director. 
By coupling the sensor steering to the autopilot/flight director, the system is able to maintain the 
vehicle in an optimal position both for sensor viewing. As part of the Spiral 3 enhancements we 
have integrated a similar capability into the Vigilant Spirit Control Station (VSCS). During 
operations each vehicle is placed in its loiter mode. While in loiter mode, the vehicle will 
maintain a loiter over its designated loiter position. During pervious spirals, VSCS included a 
Loiter Slave mode where the sensor would center itself on the center of the current vehicle loiter 
position. An alternative mode was created (Sensor Slaved) where the center of the vehicle’s 
loiter was constantly updated to correspond to the center of the sensor’s field of view. As the 
sensor operator moved the sensor to various positions on the ground, the vehicle loiter point 
would update to keep the vehicle in a position to maintain quality sensor coverage. This mode 
was particularly useful while tracking moving targets.

---
**[Page 12]**

5
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
The risk with such an approach is that the intense focus on the sensor image will result in a 
failure to maintain awareness of the vehicle and vehicle status. The primary concern from a 
pilotage perspective is to ensure the airworthiness of the vehicle and its flight path. For the 
purposes of the current study, we made assumptions regarding the reliability of the air vehicle 
and its auto-pilot control. In other words, we assumed that the vehicle would remain airborne 
and it would fly where the control station commanded it to fly. That being said, there remains 
several issues that need to be addressed to ensure airworthiness. First and foremost is terrain 
clearance. If one is to give free reign to an air vehicle within an area of operations it is critical 
that the vehicle flies at an altitude to ensure clearance over terrain in the area. Although it would 
be possible to integrate some form of terrain following algorithm, this issue was resolved by 
placing the altitude hold for each vehicle well clear of any terrain in or around the area of 
operations. 
Second, one must also be concerned with deconfliction of ownship aircraft. Given that vehicles
will likely fly in close proximity to one another, the risk of potential midair collision with other 
aircraft is always present. Ownship deconfliction was achieved through altitude separation. 
Placing each of the vehicles at different altitudes eliminated the possibility of a mid-air collision, 
even if both aircraft were flying in the identical loiter pattern. For the purposes of the current 
study a separation of 100 ft was deemed sufficient to assure altitude separation. While intruder 
aircraft were not included in the current study, an effective sense and avoid capability would be 
required to prove the viability of this concept. And while sense and avoid capability is an 
ongoing subject of research (Tadema, 2011), it was not included as part of the current effort.
Finally, one must ensure that each vehicle under one’s control must remain within the confines 
of assigned airspace. In the current simulation it was assumed that the vehicles were assigned a 
block of airspace in which they were free to maneuver. However, given focus on the sensor 
image, it is not unreasonable to assume that it would be easy for an operator to lose awareness of 
these boundaries and allow a vehicle to stray outside the assigned airspace. To ensure that 
vehicles did not violate airspace constraints while in the Sensor Slave mode it was necessary that 
operators create a “Keep In Box” that corresponded to the assigned airspace for the mission. The 
creation and activation of a “Keep In Box” was a prerequisite to the activation of the Sensor 
Slave mode. If an operator would attempt to place a vehicle in Sensor Slave mode without an 
active Keep In Box a warning would be presented indicating that Sensor Slave mode is not 
available. Once in Sensor Slave mode, the vehicle’s loiter point would update to correspond to 
the center of the sensor’s field of view. In the event that the sensor FOV went outside the Keep 
In Box boundaries, the positioning of the vehicle loiter would be limited such that a minimum of 
a two radii distance was maintained between the center of the loiter and the edge of the Keep In 
Box boundary. This ensured that the vehicle remained well within established safe airspace 
constraints. Once the loiter position became limited due to movement of the sensor FOV toward 
the airspace boundary, the operator was given an advisory indicating that the loiter position was 
being limited by the Keep In Box. While we recognize that refinements to such an approach 
may be required, we felt the current implementation was sufficient for the current simulation and 
flight test effort.
Automatic Target Tracking. As part of previous spirals the impact of automation on operator 
performance has been a central theme. One of the primary assumptions behind multi-UAV

---
**[Page 13]**

6
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
control has been the assumed dependence on automation for the viability of the multi-UAV 
concept. While automation was a central focus of our investigation, the limited availability of 
viable automation capability required that we simulate these automated features. In Spiral 2 we 
implemented an auto-detect feature to support the point surveillance, route surveillance and area 
search tasks. In each case we relied on ground truth of targets and distracter objects to simulate 
the auto-detect capability. While such an approach can provide useful insights into the potential 
impact of such automation, given the inability to accurately represent the specific behavior of 
these systems, we often gain very little insight into the human-automation coordination issues 
associated with operating at the competency boundaries of the automated system. Since such 
coordination issues are a primary concern of multi-UAV control station design, we believed it 
was important that during our final spiral we consider incorporating a viable auto tracking 
capability as part of the available control station features. Prior to Spiral 3 simulation, VSCS 
developers had been working with Real Time Video Systems (RTVS) and had integrated a realtime image processing system that provided both a mosaicing and an auto-tracking capability. 
The implementation of each of these features will be described in more detail later in the report. 
While the incorporation of this system potentially introduces an additional source of variability 
in the performance data, its inclusion provided an opportunity to observe how operators deploy 
such capabilities, the conditions under which they tend to rely on its performance or conversely 
their tolerance for sub-optimal automation performance. The extent to which operators used the 
features of this system was totally dependent upon their confidence that the capability would 
help rather than hinder their ability to perform their assigned mission. It was the variability in 
the performance of the auto-tracking that ultimately provides the desired insight into operator 
attitudes and behaviors relative to its use.
VSCS Familiarization System. One of the most insightful discoveries during Spiral 2 was that 
the quality of our data and the insights gained from the data runs was critically dependent upon 
the specific backgrounds, qualifications and familiarization of the participants with the control 
station itself. The ability of operators to effectively use the full complement of features available 
via the control station was critically dependent upon their level of competence with the 
implementation of those features. During the previous two spirals, participants were given an
instructional presentation on the capabilities of the control station to include the specific 
mechanisms and mechanics of those features that would likely be required to execute the tasks 
planned for the data collection trials for those simulation trials. Following the instructional 
briefing, participants were given a full demonstration of the control station and then offered the 
opportunity to “experiment” with the control station. 
Once participants indicated they felt reasonably comfortable with the workings of the interface,
they were exposed to a series of training trials. These training trials were similar in tasking to 
the data collection trials they were to perform during the course of the simulation study. 
Training trials were performed for each configuration to be encountered during data collection 
trials. Participants were required to demonstrate a minimum level of competence on the training 
trials and indicate their confidence in the ability to adequately perform each of the tasks. In each 
case the total training time, to include the instructional presentation, was approximately 3-4 
hours. While this level of training appeared sufficient for the part task elements of the previous 
spirals, it was evident that during the full mission trials performed during the Spiral 2 simulation 
the lack of intimate familiarity with many of the nuances of the control station limited the

---
**[Page 14]**

7
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
participants’ ability to adequately exploit its capabilities during the trials. They often reported 
that while they wanted to adopt a certain strategy, they weren’t sure how that might be 
accomplished within the current control station implementation.
Based on these observations, it was evident that if we expected participants to effectively 
perform a representative full-mission scenario and use the control station in a manner that would 
be expected under operational conditions, the level of competence with the mechanics of control 
station was essential. In short, we need to create qualified VSCS operators. With the assistance 
of our sponsor, the MUSCIT team prepared and delivered a full VSCS system to support a more 
robust control station training program. Our sponsor developed a control station training 
program fashioned after the training program currently being used to qualify other small UAV 
operators (e.g., Raven). Each participant was given several hours of instruction on the operation 
of the VSCS, its features, and implementation. 
OBJECTIVE
The objective of this study was to investigate the demands associated with the use of multiple 
unmanned aerial vehicles (UAV) within the context of representative RSTA and counterproliferation set of scenarios and establish a performance benchmark for the control of multiple 
UAVs using advanced control station designs. Supplemental study objectives included: 
• Investigating the value of control station interface enhancements to operator performance 
during representative operational tasks.
• Assessing the ability of operators to use the control station in response to unanticipated 
and unexpected events. 
• Evaluating the ability of the control station to support the development of adaptive 
strategies in response to increasing levels of mission complexity and uncertainty.
• Investigating the performance effects and behavioral adaptations operators adopt as the 
number of UAVs available and video image streams being monitored increases. 
• Investigating the means and mechanisms of coordination and collaboration as the number 
of operators transition from a single operator to two operator crew. Assess the ability of 
the control station to support cooperative strategies in response to dynamic events within 
the mission scenario.
• Increasing our understanding of operational missions, operational task demands and 
constraints, and coordination requirements both inside and outside of immediate UAV 
support teams.
• Identifying opportunities via automation, visualizations, control mechanization, concepts 
of operations, etc. that would enhance the feasibility usefulness of multiple UAVs.
• Assessing the quality and fidelity capabilities of our simulation environment and identify 
specific feature and capability candidates for future incorporation in subsequent 
simulation spirals.

---
**[Page 15]**
*(This page contains a figure/chart/image not captured in text)*

8
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
2.0 METHOD
2.1 Apparatus
The following section describes how the software and hardware components functioned in 
support of the Spiral 3 program.
2.1.1 MUSCIT Spiral 3 Simulation Architecture
The simulation architecture implemented for the Spiral 3 simulation study is presented in Figure 
1. The simulation included two and four digital simulations of small UAVs, each equipped with 
a gimbaled electro-optical (EO)/infrared (IR) sensor. Vehicle simulations were modeled after the 
MLB Company’s Bat 3 UAV platform, while sensor simulation was based on Cloud Cap 
Technology’s TASE Duo gimbaled EO/IR sensor system. Simulation of ground entities was 
created using the FLexible Analysis Modeling and Exercise System (FLAMES®), while the 
sensor simulation visualization was created using the Virtual Reality Scene Generator™
(VRSG™) by MetaVR, Inc. The Vigilant Spirit Control Station (VSCS) served as the framework 
for creating the control station configuration used in the current study. Details regarding the 
features and capabilities of each of these components are provided in the sections that follow.
Figure 1. Illustrated architecture for the MUSCIT Spiral 3 Simulation
2.1.1.1 VSCS (One and Two Operator Configurations)
The control station interface (see Figure 2) has four main parts; vehicle status, tactical situation 
display (TSD), vehicle and payload management, and sensor exploitation. The vehicle status 
area allows the operator to maintain situation awareness of the UAV(s) the operator is 
controlling. The TSD allows the operator to maintain battlespace awareness. The vehicle 
payload and sensor management area allow the operator to control the aircraft and the payloads 
they are carrying. Finally, the sensor exploitation area allows the operator to view and interpret 
the sensor information coming from the UAVs. The control station interface was displayed on 
two side by side 24” widescreen Dell LCD monitors with a combined resolution of 3840 x 1200

---
**[Page 16]**
*(This page contains a figure/chart/image not captured in text)*

9
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
or 1920 x 1200 per monitor. Under the default set up, the vehicle status area, TSD, and vehicle 
and payload management area are shown on the left monitor and the sensor exploitation area is 
shown on the right monitor. 
Figure 2. Sample layout of the control station
The VSCS interface runs on a single Dell Precision PWS690 with dual 2.66 GHz Intel Xeon 
X5355 processors and 2.75 GB of RAM, with Windows 7 as the operating system for the PC. 
The PC also uses Nvidia Quadro FX 4600 Video Card.
For the Spiral 3 simulation, VSCS also incorporated a commercial off the shelf product from 
Real Time Video Systems (RTVS) that included a pixel tracking system as well as an image 
mosaic capability. The pixel tracking system would allow an operator to “designate” an object 
within an image and the system would control sensor steering in an attempt to maintain that 
object within the center of the sensor field of view. In order to use the pixel tracking system, the 
user would have to switch into the mosaic image mode in the video tool. The user would select 
the object they would like to track (CTRL-Left Mouse), a red tracking box would be drawn, and 
the automation would try and center the object in the middle of the screen. A problem occurred 
while trying to center the object; when the sensor moved too fast the object would “break lock” 
from the tracking system. In order to correct this, a dampening algorithm was added to slow the
movement of the camera. One of the side effects to using the RTVS system was the inability to 
draw an overlay during the mosaic mode. The user would lose their sensor overlay when the 
mode was switched on.
The Spiral 3 configuration of VSCS also included the Dynaspeak Voice Recognition in 
conjunction with a Push-To-Talk switch as its voice recognition system. The vocabulary was 
expanded from Spiral 2. In this spiral, the mission became much more complex, so the 
vocabulary was tailored with that in mind. The vocabulary contained more commands that 
enabled the operator to switch automation modes and command the movement of the aircraft. 
The goal continued to allow the user to complete tasks without the operator having to draw 
his/her attention away from the sensor imagery.
Finally, to assist operators in positioning the vehicle to maintain the sensor within an acceptable 
viewing range, a sensor guidance feature was incorporated into the vehicle guidance control 
mechanisms of the VSCS. While in the Loiter Slave mode, the operator was given the option to

---
**[Page 17]**

10
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
place the vehicle within a Sensor Slave mode. The Sensor Slave mode synchronized sensor 
steering to vehicle loiter position. As the operator, or auto tracking system, updated the position 
of the sensor’s field of view, the center of the loiter position for the vehicle was simultaneously 
adjusted to correspond to the center of the sensor’s field of view. In this manner the sensor 
would continuously maintain a constant slant range to the object(s) of interest. 
One caveat to the use of the Sensor Slave mode was that prior to entering this mode it was 
necessary that the operator create a “Keep-In” box. The box created an area in which the vehicle 
was free to move in response to sensor position updates. In the event that the sensor position 
moved outside the confines of the Keep-In box, an alert was presented to the operator indicating 
that the system was commanding a loiter update outside established constraints. As a result, the 
vehicle’s loiter position could not be placed any closer than a distance equal to 2 radii of the 
current orbit. This constraint was included to reduce the potential for vehicles to stray outside 
established safe flying zones and protect against the possibility that operators become fixated on 
sensor imagery to the extent that they lost situational awareness on current airspace constraints. 
The alert upon sensor movements outside the defined boundaries is intended to cue the operator 
that further excursion in the current direction will require an expansion of the Keep-In box and 
associated coordination with appropriate airspace control authorities.
2.1.1.2 Vigilant Spirit Simulation
The Vigilant Spirit Simulation (VSSim) is responsible for simulating both the vehicles as well 
any other system that the control station may receive information from. For the vehicles, 
configuration files are read in with the vehicle real world specifications (weight, max speeds, 
etc.) and the VSSim publishes CMF 4586 messages to the control station with telemetry and 
other status information (gas, power, etc.) just as real UAVs would. One of the other major 
systems modeled is the Cursor On Target XML routing system. It streams information to the 
control station about all of the blue forces that exist in the current theater. One of the main goals 
of VSSim is to represent, as closely as possible, the capability of a real world system as it would 
work with the control station.
2.1.1.3 FLAMES®
FLAMES® is a family of computer software products that provide a framework for computer 
programs simulating physical and cognitive behaviors of complex entities that act and interact in 
time and space. This study used FLAMES® version 8.0.1 to develop individual entities and 
script their movements, saving the resulting scenarios for the experimental trials. The 
FLAMES® interface was run on a single Dell Precision PWS690 with a 3.2 GHz processor and 2 
GB of RAM. During scenario generation, entities and their movements were displayed using a 
VRSG™ image generation tool, as discussed in the next section. Information passes from 
FLAMES® to VRSG™ via a distributed interactive simulation (DIS) interface. 
2.1.1.4 VRSG™ by MetaVR, Inc.
VRSG™ is a real-time computer image generator designed to visualize geographically expansive 
and detailed worlds on PCs. VRSG™-generated images display in the sensor management area 
of the VSCS. Directing of mobile elements (e.g., personnel, vehicles) in the scene occurred 
using FLAMES® scripts. Each VSCS video window required an instance of VRSG™ to be

---
**[Page 18]**
*(This page contains a figure/chart/image not captured in text)*

11
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
running. For the current simulation, VRSG™ software ran on a Dell XPS 720 with 3.0 GHz Intel 
Core Duo 2 with 3 GB of RAM.
A major challenge in creating the simulation was the correlation of FLAMES® and VRSG™. 
Entities built and scripted in FLAMES® display in VRSG™, but FLAMES® is not cognizant of 
terrain and cultural items placed in VRSG™. Examples of these items are the buildings and 
roads placed in VRSG™ to create the compounds used for this study. FLAMES® has no idea as 
to the location of buildings and roads. To keep people from walking into buildings and to keep 
cars on the roads, these cultural features had to be represented in FLAMES®. Accordingly, 
experimenters very carefully mapped the latitude/longitude locations of cultural features residing 
in VRSG™ into FLAMES®. Experimenters accomplished this intricate mapping using airspaces, 
depicted in Figure 3. Roads were represented by black lines and buildings by green polygons. 
In addition to mapping building corners, the experimenters mapped the doors of certain buildings 
in order to enable the appearance of entities entering and exiting those buildings.
Figure 3. FLAMES® scenario development environment
A second challenge of scripting scenarios in FLAMES® is that scenario events must occur at 
specifically prescribed times. The movement of entities in FLAMES® is based on routes, start 
times, and speeds, rather than on a given entity’s appointment to a specific location at a specific 
time. Therefore, to ensure that entities arrived at desired locations at desired times, 
experimenters timed how long specific routes took to complete and then varied entity start times 
to accommodate proper event times. To expedite this process, experimenters created only a 
handful of routes for the entities at each area of interest (AOI). After recording route travel times 
for the entities, experimenters were able to prescribe appropriate entity start times.

---
**[Page 19]**

12
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
2.1.1.5 Scenario Generation/Scenario Control (Zippo Tool)
Per discussions with sponsor representatives, the scenario for Spiral 3 simulation was designed to 
be flexible and dynamic. In order to keep participants from gaming the scenario, we wanted the 
ability to inject various events into the scenario. These events included sensor noise, GPS 
failures, communication failures, additional unanticipated enemy forces, IEDs hitting convoys, 
and many others. This desire to inject unexpected events into a scenario during runtime forced 
us to design a new method to create simulation scenarios. In the past, these scenario events were 
rigidly scripted. Once the scenario started, the test operator had no way to control or alter any of 
the events. 
In creating scenarios for the Spiral 3 simulation, rather than following a scripted list of events, 
we created a flexible and dynamic timeline of events. The test operator could indicate what 
events would happen when at the start of the mission. At any time, the test operator could inject 
system failures, weather conditions, detonations, or entity behavior events by adding them to a 
running timeline. A log of these events was then recorded so that our approach to simulation 
design could be both flexible and repeatable for the purposes of data collection.
The events that were sent out from the Scenario Generation tool were sent directly to MetaVR or 
used by the Zippo tool. The Zippo tool was the “bridge” between our scenario generation tool 
and FLAMES. Zippo would connect into the FLAMES constructive simulation and command 
which entities to load based off the messages received from the Scenario Generation tool. The 
test operator no longer had to adhere to a rigid timeline and the order of the events no longer 
needed to be carefully constructed because Zippo allowed for the “on-the-fly” scenario 
construction.
2.1.2 Communications
Voice Net. The UAV crew communicated to other entities via Voice Net. These 
communications took the form of either mission coordination, mission tasking, or surveillance 
reports based on UAV imagery. The study employed a commercial Voice-over Internet Protocol 
(VoIP) communication system, TeamSpeak, to provide the communication capability.
2.2 Data Collection Layout
To provide a more representative environment for multi-UAV operations, participants were 
isolated from the test administrators, much like they would be in many existing ground control 
stations (i.e., Predator/Reaper, Hunter, Shadow, etc.). The configuration of participant control 
stations and test operator/test administrator stations is presented in Figure 4. The separation of 
the participants from the test administration team afforded the opportunity for the administration 
team to “role play” many of the entities incorporated into each of the scenarios. Given the 
dynamic nature of the scenarios and the uncertainty associated with how participants would 
respond to mission events, it was both impractical and unwise to script all communications 
between these entities and the MUSCIT participants. For the most part, communications 
initiated by directing elements (i.e., EAGLE15) or communications that did not include 
MUSCIT, were scripted and implemented via a scripted playback of recording radio messages. 
When an active dialog between MUSCIT participants and another party was necessary, members

---
**[Page 20]**
*(This page contains a figure/chart/image not captured in text)*

13
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
of the test administration team assumed those roles, engaging in real-time radio communications 
via the Teamspeak VoIP communication system. 
To ensure test administration personnel were able to monitor MUSCIT participant activities, 
dual-monitor workstations were included in each of the test administrator stations that were 
running the MORAE screen capture software. MORAE provided a real-time video capture of 
each of the MUSCIT control station screens, highlighting cursor position and mouse selections. 
The MORAE application also afforded the opportunity for the test administrator(s) to 
“bookmark” any event or activity during the course of the scenario that could be subsequently 
used to collate specific operator performance metrics (e.g., target detections, track initiations, 
vehicle movements, etc.). One issue associated with the MORAE screen recordings was the 
constraint of a 1Hz update rate for the recording. The selection of a 1 Hz update rate was 
established as a tradeoff between data collection requirements and control station performance 
constraints. Since the recording is accomplished on the VSCS machine it was important to 
ensure that the processing required to support the rate of recording did not adversely impact the 
performance of the control station. Pre-data collection trials indicated that a 1Hz update rate 
would not put at risk the operation of VSCS. 
Figure 4. MUSCIT Spiral 3 Data Collection Configuration
2.3 Experimental Design
3.3.1 Participants
For MUSCIT Spiral 3 simulation, eight individuals were recruited to participate in the data 
collection. 
2.3.2 Design
The MUSCIT Spiral 3 simulation investigated operator performance during a typical mission 
involving a range of RSTA tasks to include point surveillance, route surveillance, area search,

---
**[Page 21]**

14
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
and target tracking. This simulation was conducted using a 2 x 2 within-subjects design. 
Participants performed trials using a 1 or 2 operator VSCS configuration and with two or four 
UAVs. For the four trials within this experiment, data collection across control station 
configuration levels was blocked. Operators performed the mission with two and four UAVs at 
one level of control station configuration before moving on to the other level. The order of 
presentation of control station configuration blocks was counter balanced. The order of number 
of UAVs available within each block was also counter balanced. Each trial lasted approximately 
45 minutes. Conditions for each of the Spiral 3 simulation trials are presented in Table 1.
Total session time per participant was approximately 8 hours (including 2 hours for 
familiarization training on the use of controls and displays, completion of post-trial ratings, postsession debriefs and breaks). 
Table 1. MUSCIT Spiral 3 Experiment Trials
Trial Task Number of UAVs # of Operators
1 Mission 2 1
2 Mission 4 1
3 Mission 2 2
4 Mission 4 2
Control Station Configuration:
1-Operator Control Station. The study participants performed both pilot and sensor operator 
activities. For 1-operator control station configuration, the participant marked and reported all 
surveillance events, responded to and executed any re-tasking requests, and responded to any 
information request via voice. This condition provided the operator with full functionality of the 
control station. 
2-Operator Control Station. The Dual Operator control station configuration assumed a 
distribution of work across two operators. As such, the features and capabilities available in both 
control station were identical. Participants were given the flexibility to assign responsibilities as 
they deemed appropriate. Participants coordinated during the mission as necessary to effectively 
perform the assigned tasks in support of mission objectives. Participants needed to coordinate 
their response to unanticipated events, and manage the allocation of resources to meet evolving 
demands. 
Note: While operators could monitor vehicle state information and sensor imagery from vehicles 
they did not control, any attempt to direct the vehicle or steer the sensor would result in a 
message indicating that the vehicle/sensor the operator was attempting to control was not under 
his control. To attain control, the operator must first request and then be granted control of the 
vehicle, the sensor, or both.

---
**[Page 22]**

15
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
2.3.3 Experimental Trials
Each participant completed a total of 4 trials, and while each scenario was different, the primary 
tasks included in each trial were fundamentally the same. The primary difference across 
scenarios was the sequencing and locations at which various events within the scenario occurred. 
This variability in the scenario design was included to ensure that participants were not able to 
completely anticipate the onset of an event prior to its presentation. The following sections 
provide a detailed description of the various scenario events that were included in each scenario, 
the relevant cuing mechanisms, radio communications and red and blue ground force behaviors 
which constituted each of the scenario trials. We felt it was also important to set a context to the 
execution of the present scenario as a basis for operator decision making. During trial debriefs 
following previous spiral sessions it became evident that operator decision making behavior was 
fundamentally dependent on their interpretation of the operational context, goals, and objectives. 
In lieu of such a context, a participant might feel free to assume or create a context upon which 
to base high order decisions such as resource allocation and task prioritization. Therefore, we 
felt it essential that we, as experimenters, set the context to the extent possible, at least it terms of 
outlining the order of battle and the overall commander’s intent for this mission.
The intelligence briefing for Operation LOOKOUT presented to each participant provided the 
following background information:
Recent intelligence indicates that a meeting between two High Value Targets is to be 
conducted within the next several hours. Willie Britches, a suspected IED manufacturer 
and know member of the Dunbar Underboss Mob Brigade (DUMB), and Ali Rod, also a 
reputed member of DUMB, are reportedly scheduled to meet at a Chemical Plant located 
on the east side of their local village. Both parties are considered by coalition leadership 
as highly dangerous. Britches’ DUMB recently claimed responsibility for the May 25th
bombing of a government building that resulted in the deaths of 14 multi-national tourists. 
Rod is responsible for IED proliferation throughout the town of Gridironstan. The meeting 
at the Chemical Plant to take possession of a suspected WMD represents an escalation in 
the level of violence they are planning within the region against local and foreign forces. 
Both Britches and Rod have been under constant surveillance at their respective 
compounds by Surveillance-Reconnaissance Teams (SRT) for the past several days. 
Britches (HVT1) is currently located at Objective Steelers and Rod (HVT2) is currently 
located at Objective Cowboys. It is believed that both HVTs will be leaving their 
respective compounds within the next hour, enroute to their meeting at the Chemical Plant 
(Objective Giants). MUSCIT vehicles are to be assigned to provide support. Of primary 
importance is that upon confirmation of departure from their respective compounds by the 
SRTs on the ground, MUSCIT assets must maintain positive contact on HVT and confirm 
arrival at Objective Giants. Upon HVT arrivals MUSCIT assets will continue to support 
overwatch of Objective Giant providing situation updates as appropriate and provide 
convoy escort support to the assault team as they move from FOB Freedom to the 
preplanned blocking positions around Objective Giants. MUSCIT would also provide 
tracking support throughout the assault, tracking any personnel attempting escape from the 
compound until the WMD and the HVTs had been positively secured.

---
**[Page 23]**

16
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
A Small Unmanned Aerial System (SUAS) will be assigned to provide available overwatch
of the area of operations, providing the JTAC assigned to the assault team real-time visual 
imagery of HVTs, their compounds, and the assault location (Objective Giants)
The Request for support as presented to the participants during the mission brief is as follows: 
REQUEST MQ-1 (SUAS CAPABLE) CONDUCT OVERWATCH ON CAOC APPROVED 
TGTS. SONIC21 WILL TRANSFER CHAIN OF CUSTODY OF HVT1 TO MUSCIT21. 
SONIC22 WILL TRANSFER CHAIN OF CUSTODY TO MUSCIT 22 WITH APPROVAL 
THROUGH LOAF 44. ONCE EYES ON LOAF44 WILL LOITER OBJ GIANTS TO 
ANTICIPATE HVT1/2 ARRIVAL AT GIANTS. SONIC21 REMAINS ON OBJ STEELERS. 
SONIC 22 REMAINS ON OBJ COWBOYS. SONIC23 IVO OBJ GIANTS. HVTS ARE 
EXPECTED TO RENDEZVOUS AT GIANTS TO COLLECT SUSPECTED WMD FOR 
FURTHER PROLIFERATION. CHAOS43 WILL PROVIDE ON CALL CAS/OVERWATCH 
AS EAGLE ELEMENTS DEPART FOB FREEDOM ENROUTE TO OBJ GIANTS. 
EXPECT VDO/CORDON OF OBJ GIANT. ONCE HVT1/2 DETAINED/WMD SECURED 
CHAOS43 WILL PROVIDE ARMED RECCE/CONVOY ESCORT TO FOB FREEDOM.
A listing of all the BLUE players included in the scenario is presented in Table 2 and a map of 
the Area of Operations, including the ingress and egress routes of the assault team from FOB 
Freedom is presented in Figure 5. 
Table 2. Operation LOOKOUT Blue Forces
NAME LOCATION REMARKS
/SONIC 21/ /OBJ STEELERS/ /SR TM 1//
/SONIC 22/ /OBJ COWBOYS/ /SR TM 2//
/SONIC 23/ /OBJ GIANTS/ /SR TM 3//
/EAGLE 15/ /FOB FREEDOM/ /JTAC/ASSAULT FORCE//
/FALCON25/ /FOB FREEDOM/ /QRF// 
AIRCRAFT INFORMATION
TYPE// //CALLSIGN// //ARMAMENT// //REQUEST//
Direct fire sup //CHAOS 43// //105,40, 25, //ON CALL CAS/ ISO GAF//
1XMQ-1// //LOAF 44// //SPECTER FINDER/MUSCIT 21/22// // ISO GAF//
2XF-16CJ// //VIPER 41/42// //HARM/AAMRAM/AIM-9// //SEAD REQUESTS//
1XAWACS// //SHOGUN// //NA// //COMMAND AND CONTROL//

---
**[Page 24]**
*(This page contains a figure/chart/image not captured in text)*

17
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
Figure 5. Operation LOOKOUT Area of Operations
In creating the individual scenarios, the MUSCIT team designed a series of mission events. 
Each event was designed to exercise a specific feature or capability within the control station and 
create specific demands on operators to exercise these capabilities. The blending and sequencing 
of these tasks into an integrated scenario provided an opportunity to observe the changes in 
adaptive strategies adopted by operators as 1) the number of vehicles available to support this 
tasking was varied and 2) how crews would coordinate the distribution and negotiation of tasking 
as the demands on available resources were increased.
Objective Overwatch. As per the mission brief, each trial began with two of the MUSCIT 
vehicles positioned in a loiter over Objective Steelers (current location of HVT1) and Objective 
Cowboys (current location of HVT2). The primary purpose of positioning these vehicles at these 
locations was to ensure the sensors were in a position to assume custody (i.e., visual contract) of 
the HVTs as they departed their respective compounds enroute to the chemical plant (Objective 
Giants). While providing overwatch, a secondary objective of operators during point 
surveillance was to identify and describe “pattern of life” behaviors. While the term pattern of 
life is broadly defined from an operational perspective, its meaning in the current mission context 
required operators to report the presence of any armed individuals in and around the compound 
and indicate which buildings these individuals were entering and exiting. As mentioned earlier, 
MUSCIT vehicles have been assigned to these locations in anticipation of the need to establish 
and maintain chain of custody of the HVTs as they move from their respective compounds to the 
chemical plant (Objective Giants) for their meeting. The desire to collect pattern of life data for 
each objective is motivated by the possibility that at some point, it may become necessary as part 
of the current mission to execute an assault on one or both of these compounds. In that case,

---
**[Page 25]**
*(This page contains a figure/chart/image not captured in text)*

18
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
information regarding the level of potential resistance and the likely concentration of that 
resistance would be useful during assault planning and execution.
As part of the mission brief, operators were provided as series of photo intelligence images of the 
objective areas (Figure 6) 
(a) (b) (c)
Figure 6. Annotated photo imagery of (a) Objective Steelers, (b) Objective Cowboys and (c) Objective
Giants
As mentioned in the mission brief, SRTs are collocated at each of the objective points (SONIC21 
at Steelers, SONIC22 at Cowboys and SONIC23 at Giants) observing these compounds for 
several hours. Within the context of the current mission, the SRTs are responsible for providing 
positive identification of the HVTs as they depart the compound area. Upon confirmation of the 
HVT’s eminent departure, the SRT will provide a contact report to the JTAC attached to the 
assault team (EAGLE15). EAGLE15 will then radio MUSCIT to confirm visual contact of HVT 
by the MUSCIT vehicle, thus establishing chain of custody. 
HVT Dynamic Tracking. At predetermined times within each scenario the SRT would contact 
EAGLE15 and report the departure of the HVT from a specific building within the compound. 
EAGLE15 would then report the departure and building to MUSCIT, cuing MUSCIT to establish 
visual contact of the HVT. An example of the exchange follows:
SONIC21: EAGLE15 – SONIC21 reports HVT1 is departing building 9
EAGLE15: 15 copies … Break Break … MUSCIT – EAGLE15, report 
contract HVT departing building 9
MUSCIT: MUSCIT is contact on HVT1 departing building 9
EAGLE15: 15 copies, maintain contact
MUSCIT: MUSCIT Wilco
The pervious exchange reflects SONIC’s initial positive identification of the HVT and provides a 
location (exiting building 9) to cue MUSCIT to the appropriate individual. EAGLE instructs 
MUSCIT to confirm contact on HVT. Upon MUSCIT’s report of contact, EAGLE

---
**[Page 26]**
*(This page contains a figure/chart/image not captured in text)*

19
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
acknowledges and instructs MUSCIT to maintain visual contact on HVT. MUSCIT 
acknowledges request and indicates that he will comply.
Upon departure of the building the HVT would proceed to a structure outside the compound 
perimeter, mount a motorcycle and begin the route toward Objective GIANTS. Again, SONIC 
would report the departure of the HVT from the compound area on a motorcycle, indicate the 
direction of departure, and the road on which the HVT was traveling. MUSCIT would confirm 
contact and indicate his intention to maintain visual contact on target.
The participant was given the option of deploying an automatic target tracking capability. The 
tracker was a feature included in a third-party application, Real Time Visual System (RTVS) that 
had been integrated in the VSCS. To initiate the tracker, it was necessary that the operator 
activate the RTVS, which placed the video image into its mosaicing mode. Once in mosaic 
mode, the operator could initiate the auto tracker by placing the cursor over the object to be 
tracked (i.e. HVT) and simultaneously pressed the Shift Key and the left mouse button. A red 
box was presented within the sensor image indicating the object the auto-tracker was currently 
tracking (Figure 7). The RTVS would attempt to steer the sensor such that the tracked object 
remained within the center of the sensor’s field of view. An indication that the quality of the 
tracking solution was degrading was noted when the red box drifted from the object being 
tracked. To re-establish track the operator would re-engage the tracker by placing the cursor 
over the object to be tracked and again simultaneously press Shift-left mouse button. If the 
vehicle was placed in Sensor Slaved mode and the RTVS auto-tracker was engaged, it was 
possible for the operator to remain “hands off” while the system continued to track the HVT and 
continue to update the vehicle position to maintain the HVT within the sensor’s field of view.
(a) (b)
Figure 7. RTVS automatic target tracker (a) indication that target tracker is actively tracking HVT, HVT 
is centered within red box and red box centered within sensor field of view, (b) target tracker 
may be losing positive track on HVT as HVT is outside red box. Operator may need to 
reacquire target by selecting the HVT object to realign tracking algorithm.
At a predetermined time following the departure of the first HVT from his compound, the second 
HVT would depart the other compound. Cueing of the HVT departure was the same for both 
HVTs (i.e., SONIC reports). The timing of the departures was scheduled such that operators

---
**[Page 27]**

20
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
were required to track a single HVT for at least 3 min prior to the second HVT’s departure. This 
allowed analysts to collect performance data during periods of single and dual target tracking.
Improvised Explosive Device (IED) Event. During the course of each trial operators were 
presented with an IED event. Operators were initially cued to the event via a radio call from 
CHAOS43 to EAGLE15 reporting that a friendly convoy was taking fire in the center of town. 
EAGLE15 immediately requested and received location coordinates for the besieged convoy. 
Upon receipt of these coordinates, EAGLE15 instructed MUSCIT to immediately move one 
vehicle to the IED location and provided the coordinates. MUSCIT was also instructed to 
contact the Quick Reaction Force (QRF) that was preparing their departure from FOB Freedom 
enroute to support friendly forces at the point of the IED attack. 
When contacted by MUSCIT, the QRF unit commander instructed MUSCIT to provide situation 
report of the IED location and move a second vehicle overhead their location to provide convoy 
escort as they moved from FOB Freedom to the location of the IED attack. As the QRF moved 
from FOB Freedom to the IED location, multiple areas of interest that posed potential threats to 
the QRF were present. (e.g., armed pickup trucks (technicals), armed roadblocks, mobs of 
civilian personnel, etc.). It was the responsibility of the MUSCIT operator to establish contact 
with these areas, assess the level of potential threat, and inform the QRF unit commander of the 
potential threat. At that time the unit commander would determine whether a change in course 
was appropriate. While the QRF was enroute, red forces in armed technicals arrived at the IED 
location creating a more immediate threat to friendly ground forces. As part of their ongoing 
situation report the MUSCIT crew would provide updates on the evolving IED event, reporting 
the arrival of the hostile forces. As the QRF approached, they engaged hostile forces and 
destroyed the red technicals. The IED event ended when the QRF radioed that the location was 
secure and that MUSCIT vehicles were released to contact EAGLE15 for further tasking.
Search for Hostile Activity. During each trial MUSCIT was also instructed to move one of the 
vehicles to a specified location and provide a situation report on what was believed to be 
potentially hostile activity in and around the area. The instruction came in the form of a radio 
transmission from EAGLE15 requesting MUSCIT move a vehicle to a predefined MacroGrid 
location. The MacroGrid is a grid overlay of the area of operations used to help coordinate the 
location of sectors within the operational area. Specific grid location, designated by two letters 
and two numbers, specified a particular grid location corresponding to a location on the ground. 
The MacroGrid used by participants in the current simulation is presented in Figure 8. The 
request from EAGLE15 to MUSCIT was as follows:
EAGLE15: MUSCIT – EAGLE15 we have reports of potential hostile 
activity in the area of MacroGrid GOLF GOLF One One. 
Move MUSCIT vehicle to that location and provide sit rep
MUSCIT: Wilco Suspicious activity in vicinity of GOLF GOLF One 
One. Moving MUSCIT21 to that location, will report when 
overhead.

---
**[Page 28]**
*(This page contains a figure/chart/image not captured in text)*

21
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
EAGLE15: 15 copies
Figure 8. MacroGrid Overlay of Area of Operations for Operation OVERLOOK. (Note: The shaded 
area would indicate the approximate location of the reported suspicious activity referred to in 
the previous radio message)
Upon receipt of the request the operator would reference the MacroGrid and identify the 
appropriate grid location (in this case Golf Golf One One) and correlate the MacroGrid location 
to a specific area within the TSD. Moving a vehicle and sensor footprint to that location the 
operator would begin a wide area search of the area, looking for any objects meeting the 
description of the reported activity. Upon location of the activity the operator provided an initial 
situation report. At that time the operator may request additional information regarding the 
suspicious activity. In response to such requests, EAGLE15 would indicate that ground forces 
had reported that they had seen what they believed to be a large collection of technicals in a 
compound as well as what appeared to be potential IED activity. The operator would then 
indicate whether he could confirm either the presence of armed technicals or any potential IED 
activity. Upon completing this report EAGLE15 would either retask MUSCIT or have the 
vehicle resume previous tasking. If the suspicious activity was not located prior to a new tasking 
being received from EAGLE15, it was assumed that the new tasking was given precedence and 
the search was discontinued. 
Assault on GIANTS. In preparation for the assault on the GIANTS compound, it was necessary 
for the assault force to travel from FOB Freedom to their respective blocking position located at 
tactical positions surrounding the chemical plant. Prior to the assault team’s departure, 
EAGLE15 would contact MUSCIT requesting that one of the MUSCIT vehicles be moved to a 
position overhead FOB Freedom to be available for convoy escort. Upon the assault team’s 
departure from FOB Freedom EAGLE15 would again contact MUSCIT to confirm visual 
contact with the convoy and to establish convoy look ahead. Specifically, MUSCIT was 
responsible for identifying any potential threats to the safe passage of the convoy as they moved 
from Freedom to the blocking positions.

---
**[Page 29]**

22
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
Once blocking positions were established, EAGLE15 would direct CHAOS43 (Direct fire 
support) to move into position to initiate the assault on GIANTS. On EAGLE’s command, 
CHAOS would release rounds to take out the two guard towers located within the GIANTS 
compound. MUSCIT’s primary responsibility during the assault was to provide visual oversight 
as the assault team approached and entered the compound and track any ground personnel 
attempting to escape (squirters). Of particular interest was tracking of the HVTs; it was assumed 
that HVTs attempting escape would travel via the motorcycles they used enroute to GIANTS. 
As personnel departed the compound MUSCIT operators were to maintain track, giving priority 
to fast moving personnel, and report their approach to any of the established blocking positions. 
If squirters moved away from blocking positions, MUSCIT operators were to maintain contact 
until they stopped movement, at which time the operators were to maintain visual contact and 
provide EAGLE15 with the coordinates of the stationary squirter to direct ground forces to 
intercept and take into custody. MUSCIT was to maintain contact until ground forces arrived 
and confirmed personnel were secured or the trial was terminated. The various scenario events, 
dependent measures, descriptions are displayed in Table 3.
A total of four separate scenarios were generated combining the variations of the above mission 
events in various sequences. Four scenarios ensured that no participant would experience the 
identical mission events or the same sequence of events more than once during data collection 
trials. Detailed descriptions of each of the scenarios are presented in Appendix D. of this report.
2.3.4 Dependent Variables
2.3.4.1 Objective Data Collection
Table 3. Performance measures collected during MUSCIT Spiral 3 simulation
Scenario Event Dependent Measure Operational Definition
Objective Overwatch − Detection Rate Measured as the percentage of armed personnel entering and 
exiting buildings within the Steelers and Cowboys compounds 
that were positively reported by MUSCIT operators
HVT Dynamic Tracking − Percentage of time HVT 
positively tracked
Measured in terms of the percentage of time from when the 
HVT departed the compound to entry into the chemical plant 
that the HVT was within the FOV of the MUSCIT sensor 
tracking the target
− Single track performance Measured the percentage of time HVT was within the sensor 
field of view when a single HVT was being tracked
− Dual track performance Measured the percentage of time both HVTs were within the 
sensor fields of view when a two HVTs were being tracked 
simultaneously
IED Event − Time to IED event within FOV 
of MUSCIT sensor
Measured in terms of the time elapsed between when the IED 
event occurred and when the convoy entities engaged by the 
IED were within the FOV of the MUSCIT sensor
− Time to provide initial 
situation report of IED event
Measure as the time elapsed between when the IED event 
occurred and when the test administrator noted the first 
verbal report of visual contact with IED event
Forced Distracter − Time to locate activity Measured as time from when the radio call requesting 
MUSCIT investigate activity to the time the specific area is 
within the MUSCIT sensor field of view
− Time to report activity Measured as the time from when the radio call requesting 
MUSCIT support to investigate suspicious activity to the time 
MUSCIT operator provides a situation report

---
**[Page 30]**

23
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
Compound Assault − Percentage of time squirters 
are positively tracked
Measured as the percentage of time personnel squirting from 
the compound were in the sensor field of view.
2.3.4.2 Subjective Data Collection
During the course of the experimental session a series of subjective assessment techniques were 
administered. After each trial, participants were asked to provide a workload assessment based 
on the NASA TLX rating scale (Hart & Staveland, 1988), a situational awareness rating based on 
a modified China Lake Rating Scale, and a series of ratings related to the unique characteristics 
of the trial and control configuration. Following the completion of all experimental trials, the 
participant was asked to complete a short end of exercise (ENDEX) satisfaction survey to 
provide comments and opinions regarding the operator interface. Following the completion of 
all the experimental trials, a final debriefing was conducted which allowed the participant to 
comment on various aspects of the experimental trials, the features and capabilities of the control 
station, and opportunities for enhancing the control station design, the simulation environment, 
and employment concepts and mission scenarios. 
2.4 Procedure
Up to 8 hours per participant was required to process through the entire training and test 
sequence, including scheduled breaks. Procedures were standardized such that each participant 
received the same information and opportunity for familiarization with the simulation throughout 
the briefing and training phases of the experiment. The sequence of events was the same for all 
participants, except that the order of the treatment conditions was determined by the 
experimental design. 
Participant Screening/Consent. Participants reviewed material summarizing the nature of their 
involvement. Also administered was a brief background questionnaire, which included questions 
on operational background and sensor operator/image analyst experience. 
Mission Briefing. In addition to a mission brief that was made available to participants prior to 
arrival, participants received an intelligence and mission brief outlining the specific operational 
situation and mission objectives. The mission scenario was described in detail, including a 
review of relevant concepts of operation and rules of engagement. Call signs of those with 
whom the UAV crew would be communicating were identified, and the communication plan 
reviewed.
Upon arrival to the lab, each participant received refresher training in all procedures to be 
employed during the entire experiment. First, participants were given an introductory briefing 
on the VSCS, to include a description of its features, displays, and control mechanism. The 
voice commands were also emphasized, as it was determined that participants did not receive 
sufficient instruction or opportunity with the voice system. Training continued until the test 
director judged the participant competent on all aspects of task performance (e.g., mission 
management, sensor management, and communications).

---
**[Page 31]**

24
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
Experimental Trials. Each run lasted approximately 45 minutes. Participants wore headsets for 
all experimental trials. Task order and time into the trial was randomized within the constraints 
listed in Table 1. 
Debriefing Questionnaires. Subjective data was collected by having participants complete a 
series of short rating scales after each trial (NASA TLX, modified China Lake Rating Scale). 
Following the completion of all experimental trials, a final debrief was conducted that included 
questions asking participants to comment on various aspects of the experimental trials; the 
features, capabilities, and potential enhancements of VSCS; the simulation environment; and 
alternative mission scenarios. If time permitted, discussion extended to solicit feedback on 
current systems and envisioned challenges associated with multi-UAV control.
3.0 DATA ANALYSIS & RESULTS
3.1 Inferential Analyses
As part of the MUSCIT Spiral 3 simulation, various measures of statistical inference investigated 
the effect of two treatment variables: Number of UAVs (2 and 4) and Number of Operators (1 
and 2). Many dependent measures discussed in a previous section and abbreviated here as HVT 
1, HVT 2, Forced Dis, IED (Sec To in FOV, and Sec to Report), and Squirter, were included in 
the analyses. Information on other dependent variables was collected, but not included in this 
analysis. Data for these variables can be found in Appendix C. For these measures,
experimenters used a 2 x 2 repeated-measures Multivariate Analysis of Variance (MANOVA). 
Results of this analysis yielded no significant main effects for the treatment conditions nor a 
significant interaction between conditions. Summary statistics for the dependent variables 
included in the analysis are presented in Table 4 and Figure 9. 
Table 4. Descriptive statistics for dependent measure collected during MUSCIT Spiral 3 Sim
HVT 1
% Coverage
HVT 2
% Coverage
Forced Dis
Sec to Report
IED
Sec To in FOV
IED
Sec To Report
Squirters
% Coverage
1-Op 2-Air 87% 91% 162.00 46.57 117.29 62%
1-Op 4-Air 93% 96% 226.63 62.88 158.38 75%
2-Op 2-Air 99% 99% 113.50 10.75 104.50 60%
2-Op 4-Air 82% 84% 204.25 -6.25 24.25 74%
Plots of the data included in the analysis are presented in Figure 9 (a) – (e). As Figure 9(a) 
shows, there is little difference in the HVT coverage across conditions, with the 2-Op 2-Air 
condition showing the best performance, and the 2-Op 4-Air condition showing the worst 
performance. For the Forced Distracter task, the number of aircraft seems to affect performance. 
It appears that the more aircraft the operators had to deal with, the longer it took them to 
complete this task. The operators were also able to complete this task slightly faster in the 2 
operator condition. These trends can be seen in Figure 9(b). There are two scores reported for 
the IED task, Time from the IED explosion to when the operators put the IED location into the 
field of view (FOV) and time from the explosion to when the operators reported on the scene. 
This data is displayed in Figures 9 (c) and (d). In each case, the operators were able to perform 
faster in the 2 operator, 4 Aircraft condition. In the case of the IED Call to in FOV (Figure 9 (c)), 
operators were actually able to put the sensor on the convoy before the attack. This explains the 
negative time. And finally for the task of tracking squirters it seems that the number of aircraft

---
**[Page 32]**
*(This page contains a figure/chart/image not captured in text)*

25
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
accounted for the difference in coverage. The two 4 aircraft conditions performed similarly, and 
better than the two 2 aircraft conditions. This trend is displayed in Figure 9 (e).
(a) (b)
(c) (d)
(e)
Figure 9 Summary plots for (a) Coverage of HVTs 1 and 2, (b) Time to Report on Forced Distractor
Task, (c) Time from IED Explosion to when it was in FOV, (d) Time from IED Explosion to 
when it was reported on, and (e) Coverage of Squirters
Operators also provided subjective feedback at the end of each trial. This feedback summarized 
in Table 5 and Figure 10. As mentioned previously, operators were asked to provide a number 
on the China Lake scale to correspond with his or her perceived situation awareness (SA). It is 
important to note that for the China Lake scale, a lower number indicates better SA. Figure 10(a) 
shows mean China Lake scores for the different conditions. The NASA TLX was collected as a 
measure of reported workload. Figure 10 (b) shows the 2-Op 2-Air condition having the highest

---
**[Page 33]**
*(This page contains a figure/chart/image not captured in text)*

26
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
reported workload. Experimenters also administered a post trial survey that focused on the 
feasibility, reasonability, and timeliness of the mission considering this control station, as well as 
scoring the usefulness of a number of features of the control station. As Figure 10 (c) shows, 
operators rated the mission to be at least moderately feasibly, reasonable, and timely, with this 
control station. The figure also shows that all 4 features in question were rated to be useful, with 
the Sensor guidance, and POI tracking rated to be the most useful.
Table 5. Descriptive statistics for Subjective Data collected during MUSCIT Spiral 3 Sim
(a) (b)
(c)
Figure 10. Participant subjective ratings for (a) China Lake Situational Awareness, (b) NASA TLX 
Workload Rating, and Summary of Participant response to post trial
4.0 SPIRAL 3 FLIGHT TEST
Although the fundamental testing occurred within a rigid lab environment, it was decided to 
compliment the lab simulation with a subset of capabilities as a flight test. The flight test was 
Feasible Reason Timely Voice Guidance AutoTrk POI RTVS TLX CLSA
1-Op 2-Air 2.500 2.250 1.625 2.875 2.625 1.875 2.714 -0.857 47.259 1.917
1-Op 4-Air 2.222 2.333 2.056 2.667 2.889 1.167 2.375 -0.143 45.926 2.167
2-Op 2-Air 2.875 2.875 3.000 2.375 2.875 1.875 2.625 0.167 64.852 1.167
2-Op 4-Air 2.556 2.222 2.444 1.222 2.667 1.778 2.667 -0.714 53.481 2.438

---
**[Page 34]**

27
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
conducted with surrogate UAVs to exercise the mission functionality and tasks. Activities 
consisted of data collection while one or two operators managed 2 small UAVs during 
representative RSTA scenarios.
Our team of 18 personnel, military, civilian, and contractors, travelled to Camp Atterbury, 
Indiana for two weeks in August 2011 to conduct the flight test. 
The Flight Test Plan and testing scenarios were vetted and submitted for all required safety and 
technical review boards through AFRL, 711th HPW. In addition, Test Cards were submitted for 
approval to the appropriate Test Approval Authority. Test Hazard Analysis forms were also 
completed and approved before testing began. 
4.1 Flight Test Objectives
The objective of this study was to investigate the demands associated with the use of multiple 
unmanned aerial vehicles (UAV) within the context of representative RSTA and counterproliferation set of scenarios and to establish a performance benchmark for the control of 
multiple UAVs using advanced control station designs within a flight test environment. 
Supplemental study objectives included: 
• Investigate the value of control station interface enhancements to operator performance 
during RSTA tasks.
• Assess the ability of operators to use the control station in response to unanticipated and 
unexpected events. 
• Evaluate the ability of the control station to support the development of adaptive 
strategies in response to increasing levels of mission complexity and uncertainty.
• Investigate the means and mechanisms of coordination and collaboration as the number 
of operators increase from a single operator to dual operators. 
• Assess the ability of the control station to support cooperative strategies in response to 
dynamic events within the mission scenario.
• Increase our understanding of operational missions, operational task demands and 
constraints, and coordination requirements both inside and outside of immediate UAV 
support teams.
• Identify opportunities via automation, visualizations, control mechanization, concepts of 
operations, etc. that would enhance the feasibility of multi-UAV control.
• Assess the quality and fidelity capabilities of our flight test environment and identify 
specific feature and capability candidates for future incorporation in subsequent iterations 
of the control station design.
4.2 Method
4.2.1 Apparatus
The following section describes the flight test facilities as well as how the software and hardware 
components functioned in support of the Spiral 3 flight test.

---
**[Page 35]**
*(This page contains a figure/chart/image not captured in text)*

28
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
4.2.1.1 Flight Test Tools, Equipment, Location
The test was conducted using 2 MLB CC Bat 3 UAVs, as seen in Figure 11. The MLB Bat 3 is a 
commercial off the shelf small, unmanned aerial vehicle that operates 5 hours autonomously 
while delivering high quality video imagery. The BAT 3 was launched autonomously using a 
car-top, bungee-powered catapult and landed autonomously on its wheels. 
Figure 11. MLB CC BAT 3 UAV
The UAV weighs 31 lbs fueled with payload with a range of 6-10 mile radius. Other 
specifications of the BAT 3 include:
• Maximum ceiling range of 10,000 ft
• Data Link of 900 MHz C2, 2.4 GHz video
• Launch Platform is a bungee, catapult system
• Operations include PCC Autonomous flight, left and right manual control
• Flight wind limits of 35 knots
The BAT 3 used a TASE gimbaled camera system from Cloud Cap Technology which allowed 
the operator to manipulate the camera for specific location viewing. The operators were able to 
deploy, steer, and zoom the gimbaled camera from the ground station. 
The flight test was conducted at Camp Atterbury, Indiana in which we utilized a 7km X 12km
restricted airspace flight box. The flight test relief map with kill and caution boundaries is show 
in Figure 12. Our Team was located in two mobile trailers at the south end of the Camp 
Atterbury runway (as indicated in the satellite view of Camp Atterbury, Figure 12).

---
**[Page 36]**
*(This page contains a figure/chart/image not captured in text)*

29
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
Figure 12. Relief Map and Satellite view of Camp Atterbury
4.2.1.2 MUSCIT Spiral 3 Flight Test Architecture
The Flight Test portion, similar to the laboratory testing, utilized the VSCS as the control station. 
The VSCS station simultaneously presented planned and real-time routing flight information for 
the BAT 3s while they were performing their RSTA tasks. The VSCS displayed planned routes, 
real-time positional information on a map, and simultaneous video from the UAVs. 
For the MUSCIT Spiral 3 flight test, the workstation configuration consisted of two side by side 
1920x1200 pixel LCD monitors, with four main parts; vehicle status, tactical situation display 
(TSD), vehicle and payload management, and sensor exploitation. The vehicle status area 
allowed the operator to maintain situation awareness of the UAV(s). The TSD allowed the 
operator to maintain battlespace awareness. The vehicle payload and sensor management area 
allowed the operator to control the aircraft and payloads. Finally, the sensor exploitation area 
allowed the operator to view and interpret the sensor feeds coming from the UAVs. Figure 13
shows the flight test ground station architecture. 
A key enabler for allowing VSCS to be easily connected to the BAT 3 vehicles is the Vigilant 
Spirit 4586 Common Message Framework (CMF) Toolkit. The VS 4586 CMF Toolkit is an 
implementation of the NATO STANAG 4586 data link interface standard. It provided a 
standard set of messages for communicating between the control stations and the BAT 3. This 
concept was successfully demonstrated during several flight tests (e.g, MUSCIT Spiral 1, ICET). 
The flight test setup allowed for redundant data recording. Each Piccolo Command Center 
(PCC) ground station recorded the telemetry data in the Piccolo format. Additionally, all of the 
CMF data sent to and from the Vigilant Spirit Control Station was recorded.

---
**[Page 37]**
*(This page contains a figure/chart/image not captured in text)*

30
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
Figure 13. Illustrated architecture for the flight test ground stations
4.2.1.2.1 Vigilant Spirit Control Station
4.2.1.2.2 Vigilant Spirit Simulation
During MUSCIT Spiral 3 flight test the Vigilant Spirit Simulation (VSSim) component provided 
the means by which the test administrator was able to manage and control flight test data 
collection trials. 
4.2.1.2.3 Small UAV Control Station
Cloud Cap’s Piccolo Command Center (PCC) and Portable Ground Station (PGS) served as the 
small UAV Control System for this flight test. The PCC provided the interface for safety pilots 
to send command and control inputs to and receive telemetry data from the aircraft through the 
PGS, via a 900 MHz antenna. The aircraft was also sending back video that was collected by a 
separate 2.4 GHz patch antenna, piped into an AXIS video encoder and distributed over the 
network. This video was available to anyone on the network.
4.2.2 Communications
Voice Net. The UAV crew communicated to other entities via Voice Net. These 
communications took the form of either mission coordination, mission tasking, or surveillance 
reports based on UAV imagery. The study employed a commercial Voice-over Internet Protocol 
(VoIP) communication system, TeamSpeak, to provide the communication capability. In 
addition to the TeamSpeak VoIP communication net the flight test team also used hand held 2-
way radios. These radios were used primarily to coordinate between the PCC operators, the test 
administrator, the MUSCIT operators, the Safety Officer, the Safety Pilot, and the scenario 
actors to coordinate the initiation and termination of each trial.

---
**[Page 38]**
*(This page contains a figure/chart/image not captured in text)*

31
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
4.2.3 Data Collection Layout
To provide a more representative environment for multi-UAV operations, participants were 
isolated from the test administrators, much like they were during the Spiral 3 simulation. Data 
collection for the participants was conducted in a trailer provided by Camp Atterbury for UAV 
flight test, flight demonstration and training purposes. The configuration of participant control 
stations and test operator/test administrator stations is presented in Figure 14. The separation of 
the participants from the test administration team afforded the opportunity for the administrator
to “role play” many of the entities incorporated into each of the scenarios. 
Again, to ensure that the test administrator was able to monitor MUSCIT participant activities, 
dual monitor workstations were included at the test administrator workstation running the 
MORAE screen capture software. As during simulation, the MORAE application provided a 
real-time video capture of the MUSCIT control stations, highlighting cursor position and mouse 
selections. Due to space constraints in the shelter being used only one MORAE system was used 
and was attached to the number 1 control station. As a result, only screen captures were 
available from one of the operator control stations. Trials were conducted such that the number 
1 control station was used for both single and dual operator trials. Repeater displays of the 
MUSCIT control were presented in a common area in the center of the shelter to allow visitors 
and other interested parties to observe operations without disrupting the flow of activity of the 
MUSCIT participants.
Figure 14. MUSCIT Spiral 3 Flight Test Data Collection Configuration
4.2.4 Flight Test Design
4.2.4.1 Participants
To the extent possible the MUSCIT team wanted to include those operators that had participated 
in the MUSCIT Spiral 3 simulation. Due to operational constraints, only 2 sensor operators 
were able to participate in the flight test effort. To supplement these participants, we also 
recruited individuals from within the AFRL community who either had piloting experience 
and/or were actively engaged in UAV and/or UAV control station development research. These 
individual were given the same opportunities for familiarization training afforded their 
counterparts prior to their participation in the flight test data trials. In all, a total of six 
individuals were included as participants in the MUSCIT Spiral 3 flight test effort.

---
**[Page 39]**

32
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
4.2.4.2 Design
The flight test investigated operator performance during a representative mission involving a 
range of RSTA tasks to include aspects of point surveillance, route surveillance, area search, and 
target tracking. During flight test trials participants conducted the flight test scenario within the 
context of a single operator and as a member of a two operator crew. As in the MUSCIT Spiral 
3 simulation crews were free to distribute tasking across the crew as they saw fit. Participants 
were brought to the flight test as two member crews. The order in which conditions (i.e., single 
operator versus dual operators) were presented to the participants was such that the first 
participant completed a single operator trial after which the second participant joined the first to 
complete the two operator trial. Following the two operator trial, the first participant was 
excused for a post trial debrief and the second participant completed a single operator trial. The 
experimental matrix for the flight test is in Table 6.Total session time, per participant, was 
approximately 6 hours (including 2 hours for training on the use of controls and display, 
completion of post-trial ratings, post-session debriefs, repositioning of air vehicles, and breaks).
Table 6. MUSCIT Spiral 3 Experiment Trials
Trial Task # of Operators # of UAVs
1 Mission 1 2
2 Mission 2 2
4.2.4.2.1 Independent Variables
Control Station Configuration
1-Operator Control Station. Utilizing the 1-Operator control station configuration the 
participant was responsible for the management and control of all UAVs assigned. The 
participant was given the flexibility to allocate resources as they deemed appropriate. The 
participant was responsible for all vehicle and sensor management functions as well as 
coordination with any and all external entities to include simulated C2 elements, ground forces, 
etc. 
2-Operator Control Station. The 2-Operator control station configuration assumed a distribution 
of work across two operators. Participants were given the flexibility to assign responsibilities as 
they deemed appropriate. Participants coordinated during the mission as necessary to effectively 
perform the assigned tasks in support of mission objectives. Participants needed to coordinate 
their response to unanticipated events, and managed the allocation of resources to meet evolving 
demands. 
4.2.4.3 Flight Test Trials
For the flight test, each participant completed a total of 2 trials, one as a single operator and the 
other as a member of a two operator crew. The mission brief presented to participants was 
essentially the same as the brief presented during the MUSCIT Spiral 3 simulation (3.5.1.1 of 
this report). The fundamental differences between the flight test scenario and the simulation

---
**[Page 40]**
*(This page contains a figure/chart/image not captured in text)*

33
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
scenario was the layout of Objectives Steelers, Cowboys, Giants and FOB Freedom. The area of 
operations for the MUSCIT Spiral 3 flight test is presented in Figure 15. More detailed images 
of each of the objective locations is presented in Figure 16. The flight test scenarios included all 
the same players the simulation scenarios did and all the same tasks were incorporated with the 
exception of the IED Event. While the tasks were designed to be as similar as possible, there 
were some notable differences between the flight test versions of these tasks relative to their
simulation counterparts. These variations are noted in the following sections. 
Figure 15. Operation Overlook Area of Operations (Flight Test)
Objective Overwatch. As during the Spiral 3 simulation, each trial began with the two MUSCIT 
vehicles positioned in a loiter over Objective Steelers (current location of HVT1) and Objective 
Cowboys (current location of HVT2). MUSCIT operators were to monitor activity at each 
location while waiting for confirmation from the SR teams that the HVT had departed that 
position. Rather than report the entry and exit of armed personnel in and out of buildings at each 
objective, participants were instructed to report the presence of any target objects in the area of 
each objective. Each objective area was populated with several “objects of interest”. For the 
flight test, objects of interest were 4’x3’ blue and yellow cloth sheets, each presenting a black 
symbol (e.g.,○ ∆ × □). Prior to each trial the test administrator would indicate to participants the 
color (blue or yellow) and symbol (○, ∆, ×, or □) that represented a target object for that trial. 
Upon detection of a target object anywhere around any of the objective areas, participants were 
to report the presence of the target and create a track designating the position of the target.

---
**[Page 41]**
*(This page contains a figure/chart/image not captured in text)*

34
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
(a) (b) (c)
Figure 16. Annotated photo imagery of (a) Objective Steelers, (b) Objective Cowboys and (c) Objective 
Giants
HVT Dynamic Tracking. The HVT tracking task was functionally equivalent to that performed 
during simulation trials. At scripted times that depend upon the specific scenario being run, the 
HVTs would depart from their respective objective areas. Upon receipt of positive identification 
of the HVT departing the objective area, participants were to maintain positive contact of the 
HVT as he travelled to Objective GIANTS. For the flight test, actors portraying the HVTs rode 
bicycles from their original positions at Steelers and Cowboys to the destination at Giants. At 
some point during their trip to Giants each HVT would stop along their route, dismount their 
bicycle, and place an object of interest along the road. The participants were to note this event 
and report whether the object of interest was indeed a target object. Once the HVT arrived at 
Giants the participants were to continue monitoring HVT activity at Giants and report the 
presence of any target objects in that area. In addition they were to respond to any additional 
tasking directed at them by EAGLE15. 
Search for Hostile Activity. During simulation trials participants were directed by EAGLE15 to 
a specific MacroGrid location to investigate what was believed to be suspicious activity within 
the area. Likewise during flight test, participants were again directed to a specific MacroGrid 
location. However, in these cases, participants were to report the presence of a target object (i.e., 
color sheet with specific symbol). At each of the two MacroGrid locations used during the flight 
test, two objects of interest were placed within the area of interest, one of each color. As the 
participant approached the designated location he would have to first detect the location of the 
objects of interest. Upon detection, the operator could attempt to identify both the color of the 
object and the specific symbol present on the object to determine whether it was indeed a target. 
Upon confirmation of a target object, the participant was to report the presence of the target and 
create a track to designate its specific location. Upon confirming that no target object was 
present at the location (i.e., the objects of interest) were not of the proper color and symbol the 
operator would report such to EAGLE15 who would then direct MUSCIT to resume pervious 
tasking.
Assault on Giants. Similar to simulation trials, the assault event was initiated with a call from 
EAGLE15 to come overhead FOB Freedom to provide convoy escort for the assault team 
enroute to Objective Giants. MUSCIT would establish positive contact on the lead assault 
vehicle (Note: during flight test trials the assault convoy included a single red pickup truck, the 
truck was easily identifiable to participants and would depart FOB Freedom at a predefined time

---
**[Page 42]**

35
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
following the call for MUSCIT to come overhead FOB Freedom). The assault convoy would 
travel from FOB Freedom to Objective Giants at which time the HVT located at Giants would 
mount their vehicles (i.e., bicycles) and attempt escape from capture by the assault team. While 
the assault team did not actively pursue the HVTs, MUSCIT was instructed to maintain visual 
contact on HVTs so assault ground forces could subsequently intercept. MUSCIT would 
maintain contact on HVTs until such time that either the trial was terminated or the HVT became 
stationary. At that time, MUSCIT would create a track on the TSD and report the exact 
coordinates for the location of the HVT for assault force intercept. 
4.2.5 Dependent Variables
4.2.5.1 Objective Data Collection
Several performance metrics were captured during each of the simulation trials. Table 7 
provides an operational definition of each dependent measure for each of the scenario events 
included in each trial.
Table 7. Performance measures collected during MUSCIT Spiral 3 Flight Test
Scenario Event Dependent Measure Operational Definition
Objective Overwatch − Detection Rate Measured as the percentage of Target Objects within the 
Steelers and Cowboys compounds that were positively reported 
by MUSCIT operators
HVT Dynamic Tracking − Percentage of time HVT 
positively tracked
Measured in terms of the percentage of time from when the 
HVT departed the compound to entry into the meeting location 
that the HVT was within the FOV of the MUSCIT sensor tracking 
the target
− Single track performance Measured the percentage of time HVT was within the sensor 
field of view when a single HVT was being tracked
− Dual track performance Measured the percentage of time both HVTs were within the 
sensor fields of view when a two HVTs were being tracked 
simultaneously
Forced Distracter − Time to report activity Measured as the time from when the radio call requesting 
MUSCIT support to investigate suspicious activity to the time 
MUSCIT operator provides a situation report
Compound Assault − Percentage of time 
squirters are positively 
tracked
Measured as the percentage of time personnel squirting from 
the compound following the initiation of the assault to the End 
of the scenario
4.2.5.2 Subjective Data Collection
During the course of the flight test trials, a series of subjective assessment techniques were 
administered. After each trial, participants were asked to provide a workload assessment based 
on the NASA TLX rating scale (Hart & Staveland, 1988), a situational awareness rating based on 
a modified China Lake Rating Scale, and a series of ratings related to the unique characteristics 
of the trial and control configuration. Following the completion of all the flight test trials, a final 
debriefing was conducted which allowed the participants to comment on various aspects of the 
flight test trials, the features and capabilities of the control station, and opportunities for 
enhancing the control station design, the flight environment, and employment concepts and 
mission scenarios.

---
**[Page 43]**

36
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
4.2.6 Flight Test Operations
4.2.6.1 Flight Coordination/Approach
The Safety Officer and Flight Test Director coordinated the flight tests at Camp Atterbury with 
Atterbury Airfield Operations. Camp Atterbury UNICOM deconflicted and coordinated all air 
traffic and ground vehicles on and around the airfield and drop zones. The test Safety Officer 
notified Camp Atterbury Range Control of the flight test plans and pertinent safety issues. The 
minimum vehicle altitude was no lower than 500' AGL, except during the takeoff and landing 
phases of operations. 
4.2.6.2 Flight Conditions
The following environmental conditions set the limits for conducting the test. These ensured 
acceptable equipment performance and appropriate visual contact with the platform. Weather 
conditions were always confirmed with Camp Atterbury tower and from available ground 
instrumentation. Weather conditions were evaluated at the beginning of each test day for a 
go/no-go test decision. With the possibility of rapidly changing weather, the Test Director and 
Safety Officer monitored conditions throughout the test day. The following wind limits are well 
within the Bat 3’s operational envelope as established by the manufacturer, but there was no 
need to operate the MUSCIT Bat 3s in more severe conditions.
• Daylight Operations
• Temperature: Greater than 40o
F
• Maximum Wind: 30 knots (35 knot maximum gust)
• Precipitation: No more than light rain (only if outdoor equipment is covered/protected)
• Visibility: at least 3 nm
• Ceiling: 500 ft above operating altitude, no lower than 1000 ft AGL
4.2.6.3 Flight Test Procedure
The Spiral 3 flight test occurred over a 7 day period beginning on 7 August, 2011. The first four 
days of flights served as a “dry-run” of the experimental trials as well as training for the flight 
test team. While several members of the test team had participated in UAV flight tests, these 
four days were an opportunity to reorient to the procedures and protocol of the flight test 
environment and the coordination demands associated with live-fly operations. The first part of 
the week was also used to train and certify/recertify four members of the MUSCIT team as 
Piccolo Ground Control Station (PGCS) operators in accordance with AFRL guidelines. Each 
test team member that was to serve as a PGCS operator was required to complete ground and 
simulation training as well as perform at least two successful flight sorties. These flights 
afforded the opportunity to verify communication between the PGCS and the VSCS as well as 
demonstrate the capabilities of the sensor relative to the planned flight test tasks.
Following the required flight to upgrade and certify/recertify the cadre of PGCS operators, the 
test team began rehearsals of the scenarios that were to be utilized during data collection trials. 
This included the determination of target locations and travel routes to be used by “actors” 
within the mission scenarios. Force distractor areas were also located for inclusion in testing.

---
**[Page 44]**

37
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
When participants arrived to the flight test area they were given a brief tour of the facilities and 
were able to watch and ask questions during the ground preparation of the UAVs. Experimenters 
then brought the participants into the data collection trailer. Experimenters briefed the 
participants on the VSCS flight test interface and highlighted any new features. All of the flight 
test participants had had some prior experience with VSCS, so more in-depth training was not 
needed. After the differences training was completed, participants were given the opportunity to 
interact with the control station during actual flight operations. Participants were encouraged to 
interact with the interface as if they were conduct actual data trials, engaging the sensor and auto 
tracker capability. This was a chance for the participants to experience and adapt to the real 
world aspects of UAV and sensor control. Prior to data collection trials it was important that 
participants became familiar with the unique aspects of vehicle and sensor control in actual flight 
operations in comparison to the simulation environment in which they had previously trained. 
This practice session continued until the test administrator judged the participant to be ready to 
continue with the experimental trials. 
The experimental trials began as shown in Table 6. Since participants were run in pairs, one of 
the participants would begin with a one operator trial, while the other observed from another 
room. After completion of the first one operator trial, the second participant would join the first 
in a two operator trial. Finally, the second participant would complete the final, one operator 
trial while the first participant observed from another room. Individual and team debriefs 
occurred after each trial as well as at the end of all three trials. This process was repeated for all 
pairs of participants. 
4.3 Flight Test Results
Given the limited number of data runs available as part of the flight test effort and the degree of 
uncontrolled variability across data collection trials, the MUSCIT team felt it would be 
inappropriate to conduct formal statistical analysis on the available flight test data. Summary 
statistics for some of the key dependent variables captured across the treatment condition (i.e., 
crew composition) is presented in Table 8 and Figure 17. Information on other dependent 
variables was collected can be found in Appendix C.
Table 8. Descriptive statistics for dependent measure collected during MUSCIT Spiral 3 flight test 
HVT Cowboys HVT Steelers Forced Dis Squirter Coverage
1-Op 47% 42% 305 64%
2-Op 93% 64% 125 83%
Plots of the data included in the analysis are presented in Figure 17 (a) – (c). As figure 17 (a) 
shows, HVT coverage was better in the 2 operator case. It is interesting to note though that even 
in the 2 operator case, coverage was much lower for the HVT leaving Steelers. Figure 17 (b) 
shows that it took 80 seconds longer to respond to the forced distracter task with 1 operator than 
it did to respond to the task with 2 operators. Participants also performed better in the squirter 
task with 2 operators. This is evident in Figure 17 (c).

---
**[Page 45]**
*(This page contains a figure/chart/image not captured in text)*

38
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
(a) (b)
(c)
Figure 17. Summary plots for (a) Coverage of HVTs Cowboys and Steelers, (b) Time to Report on Forced 
Distractor Task, (c) Coverage of Squirters 
Operators also provided subjective feedback at the end of each trial. This feedback is 
summarized in Table 9 and Figure 18. As mentioned previously, operators were asked to 
provide a number on the modified China Lake scale to correspond with his or her perceived 
situation awareness (SA). It is important to note that for the China Lake scale, a lower number 
indicates better SA. Figure 18 (a) shows the mean China Lake scores for the different conditions. 
The NASA TLX was collected as a measure of reported workload. Figure 18 (b) shows the 1-Op 
condition having the highest reported workload. Experimenters also administered a post trial 
survey that focused on the feasibility, reasonability, and timeliness of the mission considering 
this control station configuration, as well as scoring the usefulness of a number of features of the 
control station. As Figure 18 (c) shows, operators rated the mission to be at least moderately 
feasibly, reasonable, and timely, with this control station. The figure also shows that all four 
features in question were rated to be useful, with the Sensor Guidance, and Voice Control rated 
to be the most useful.
Table 9. Descriptive statistics for Subjective Data collected during MUSCIT Spiral 3 Flight test
Feasible Reason Timely Voice Guidance AutoTrk KeepIn TLX CLSA
1-Op 1.80 2.40 1.60 2.80 2.80 1.80 2.20 80.00 1.90
2-Op 2.67 2.83 2.17 2.67 2.50 2.00 2.33 48.05555 1.17

---
**[Page 46]**
*(This page contains a figure/chart/image not captured in text)*

39
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
(a) (b)
(c)
Figure 18. Participant subjective ratings for (a) China Lake Situational Awareness, (b) NASA TLX 
Workload Rating, and (c) Summary of post trial survey
5.0 Discussion
In the context of MUSCIT’s spiraled approach to multi-UAV control station development and 
empirical demonstration, the current spiral represented a significant departure from previous 
spiral efforts. During the current spiral, the focus was not directed solely on assessing the 
capacity of a single operator in controlling and managing multiple UAVs, but rather to more 
fully understand how multiple UAVs could be used to support envisioned operations during a 
representative RSTA/counter-proliferation type mission. The question we were asking focused 
less on “how much” to merely “how” and “why”. The hallmark of an experienced operator is 
that they “make it work”. A recurring comment from participants across spirals was that they 
felt it was their responsibility to make it work. To our participants we insisted that as a 
technology development program, we were interested in understanding the vulnerabilities in the 
design, weaknesses in the concept, and flaws in the implementation of the control station. In 
other words, our hope was that their exposure to the control station in a simulated and flight test

---
**[Page 47]**

40
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
environment would expose many of the design flaws in the system and help point us toward 
enhancements that would improve the system and increase the likelihood that the feasibility of 
multi-UAV control was indeed achievable. Without fail, however, operators were consistently 
quick to blame themselves for suboptimum performance. While they might provide some 
indication of problems they encountered with the system, guiding us toward potential 
opportunities for design enhancements, they were unrelenting in their insistence to take 
responsibility for performance. 
In making the system work, they remain adamant that they are responsible for identifying and 
deploying strategies and possible workarounds that will ultimately result in success. While it 
may seem a bit cliché, for them, failure is not an option. During Spiral 3, the MUSCIT team 
hoped to capitalize on this drive to “make it work”. Our focus was on understanding “how” 
operators make things work in the face of time stress, uncertainty, and conflicting goals. To do 
this, we created an environment through a series of operational scenarios that challenged their 
ability to cope; that created time stress, which provided limited and sometimes ambiguous 
information that forced operators to prioritize objectives in the face of conflicting goals. In 
doing so, we might catch a glimpse into their thought processes and the adaptive strategies they 
adopt in managing multiple assets to accomplish a complex task. Looking beyond the “how” of 
making it work, we were also interested in the “why”. What guided the decisions, what tradeoffs 
were considered, what values were to be considered in selecting between alternative courses of 
action. We weren’t so much interested in quantifying a limit on capacity of a single operator as 
we were in understanding how and why operators act as they do in the face of difficult and 
challenging situations and how the capabilities and features of the control system either 
supported or inhibited their ability to make it work.
The following section provides a detailed description of many of the situations encountered 
during the simulation and flight test trials, some of the specific control station features and 
capabilities that significantly contributed to the ease with which operators were able to 
accomplish tasks, as well as those instances that significantly challenged operators and thereby 
suggest opportunities for either refinement to existing capabilities or the integration of new 
capabilities. Where possible, specific examples of operator interactions with the control station 
will be used to illustrate the point. 
Sensor Slaved Mode (Sensor Guidance). Probably the most desirable feature of the control 
station within the context of the current mission was the incorporation of the Sensor Slaved 
mode. Activation of the Sensor Slaved mode significantly reduced the demands for vehicle 
control on the operator. As described earlier in the report, once the vehicle was placed in sensor 
slaved mode the vehicle’s loiter point would be continuously updated to correspond with the 
current look point of the active sensor. As a result, operators were not required to continuously 
update the loiter point of the vehicle in order to maintain an appropriate slant range to the target, 
particularly during dynamic target tracking. The Sensor Slaved mode, probably more than any 
other feature, greatly reduced the attentional demands on operators. Evidence of the value of the 
sensor slave mode was illustrated when one operator commented that “Operating 4 was tough, 
operating 4 when you didn’t have sensor slaved was nearly impossible”. Given we were
working with experienced operators, their primary focus was on controlling and monitoring the

---
**[Page 48]**

41
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
sensor imagery. The ability to automatically position the sensor to provide the desired image 
was a monumentally advancement in terms of being able to make use of multiple UAVs.
There were, however, a couple of instances where problems with the sensor slave mode were 
encountered. During one dual operator trial one of the operators was in the process of actively 
tracking one of the HVTs from Objective Cowboys to Objective Giants. The second operator 
had just received confirmation of the departure of the HVT from Objective Steelers and had 
established contact and was actively tracking the HVT using the auto-tracking capability. As the 
HVT was being tracked the operator noticed that the slant range of the sensor image was 
increasing. This cued him that maybe the loiter point of the vehicle was not being properly 
updated. A glimpse at the TSD to check on the position of the sensor footprint and the current 
loiter position confirmed that the loiter point was not being updated. Thinking that maybe he 
had forgotten to place the vehicle in sensor slave he again pressed the sensor slave mode button. 
Again, the loiter did not update. Coincidentally, the vehicle, in its static loiter, flew directly 
overtop the moving HVT causing the sensor to enter a Nadir condition. One reason UAV sensor 
operators try to avoid nadir conditions is that at sensor elevation angles approaching 90o
, the 
sensor steering mechanism has difficulty stabilizing its azimuth control. As a result, the sensor 
swung wildly away from the HVT location and the operator lost contact on the HVT. Because 
the sensor slave mode did not seem to be operating as expected the operator was required to 
manually update the loiter point during the subsequent search to reacquire the HVT. Due to the 
added demands of vehicle control and the confusion associated with the sensor slave mode 
operations, the operator was unable to reacquire the HVT prior to its subsequent arrival at 
Objective Giants, which the first operator reported given that he was on station at Giants 
providing point surveillance on the compound.
A review of this incident revealed that the unexpected behavior of the sensor slave mode was due 
to a failure to create a Keep In Box prior to activating the sensor slave mode. The Keep In Box 
is a safety feature implemented by VSCS developers to ensure that vehicles being controlled
under sensor slave mode would not violate their current airspace constraints. Again, while the 
operator, upon realizing that the Keep In Box was not active was quick to focus blame on
himself, this episode also points to an issue of control station feedback and mode awareness. 
While the control station did provide an annunciator that indicated that the sensor slave mode 
was not active when the operator attempted to re-engage the mode, it failed to provide any 
indication as to the source of the fault. While hindsight is perfect, it is not unreasonable to 
assume that a message reporting that a Keep In Box needs to be established before a vehicle can 
be placed in sensor slave mode. The operator also indicated that in all likelihood, a formal 
checklist detailing each of the steps required to place the control station, vehicle and sensor in 
operational mode for that mission would have been performed. During simulation, 
experimenters relied on participants remembering the procedural steps required to engage each 
of the modes. While such checklist might be considered a work around, and should not replace 
sound interface design concepts, they are part of the operational culture and should not be 
ignored when evaluating systems for military use.
One other problem noted when interacting with the sensor slaved mode was the name itself. The 
term “slaved” has been used for other modes such as loiter slaved and lat/lon slaved. In loiter 
slaved mode, rather than the vehicle being slaved to the sensor starepoint (sensor slaved) the

---
**[Page 49]**

42
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
sensor is slaved to the vehicles loiter point. The confusion was most evident when operators 
were trying to engage either of these modes using voice commands. On several occasions 
operators either inadvertently engaged the wrong mode or the utterance used to engage the voice 
command was in appropriately spoken (e.g., improper grammar or syntax). Given the frequency 
with which such errors occurred, it appeared evident to the MUSCIT team that an alternative 
label for the sensor slaved mode would be appropriate, minimizing the potential for mode 
engagement errors. A couple participants commented that the term “slaved” typically refers to 
the sensor given that sensors are slaved to particular points or locations. Conversely, vehicles 
are steered or guided, not slaved; further suggesting that a change in the mode label is warranted. 
Automatic Target Tracking. Probably the second most desirable feature incorporated into the 
control station was the automatic target tracking capability. However, the desirability of this 
feature is fundamentally dependent upon its reliability. When functioning as intended, the 
system can be a tremendous aid in supporting operators during multi-UAV operations. Using the 
“red box” as an indicator of the track quality, operators could quickly cross-check tracking 
performance and realign the tracker as necessary if it appeared that track quality might be 
degrading. This afforded the opportunity for operators to attend to other activities within the 
mission, reasonably confident that the autotracker would maintain contact. The interval of time 
between cross check might provide a viable indicator of the level of confidence the operator 
placed on the tracker during the course of the trial. The longer the interval between crosschecks, 
the more confident the operator might be in the ability of the tracker to maintain target contact. 
Shorter crosscheck intervals might indicate less confidence in tracker performance. 
Across trials there was a great deal of variability in terms of how well and how reliably the auto 
tracker could maintain a positive track on a moving target. Given that the auto tracker available 
via the RTVS system was a third party application integrated into the control station, the 
development team had little insight into the internal algorithms that enable the feature. 
Therefore, it is difficult to identify with any certainty the specific conditions that might have 
contributed to the frequent loss of tracking. However, having observed several trials, one can 
begin to identify certain patterns that emerge as operators have difficulty getting the system to 
maintain contact. 
One of the conditions that appeared to have a significant impact on the ability of the auto tracker 
to maintain sufficient track quality was the FOV setting selected by the operator. Image FOV 
influences two factors that weigh heavily in track quality; resolution and rate of target movement 
across the image. At wider fields of view a target moving at a constant rate will tend to move 
across the image at a slower rate than the same target viewed within a smaller FOV. As the rate 
at which the target moves across the image increases there will come a point where the tracker 
will no longer be able to effectively track the pixels that define the target. In short, the slower 
the target moves, which coincides with a wider image FOV, the better the track will be able to 
maintain track quality. The tradeoff then is target size, that is, the number of pixels that 
constitute the target within the image (i.e., resolution). At wider fields of view, the ground 
sample distance (the distance on the ground subtended by a single pixel) becomes larger. At the 
widest FOV settings the current target (i.e., HVT on motorcycle) may subtend only a couple of 
pixels making tracking of transitions in the leading and trailing edge of target pixels extremely

---
**[Page 50]**

43
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
difficult. Therefore, target tracking via pixel analysis, like target detection and identification, is 
made easier as the ground sample distance decreases, or as image resolution increases. 
Operators tended to converge on a FOV setting that established a balance between these two 
factors. The tracker seemed to work at its best during the HVT tracking when the FOV was set 
at a mid-range setting (~28o
). Many of the operators also would switch to the IR sensor mode to 
provide better target contrast against the background. The limitation associated with the IR 
mode was that, as opposed to a continuous FOV setting available in the EO mode, IR imagery 
was available at only two FOV settings.
Another consequence of using the RTVS tracking system was the limitation associated with fully 
integrating the interface into the control station. One example of this limitation was the inability 
to integrate symbology into the imagery while the RTVS system (and by definition the auto 
tracker feature) was active. Based on participant feedback, the most significant impact of this 
limitation was the loss of the orienting North pointer presented as part of the symbology overlay. 
Modeled after the north pointer incorporated into the sensor imagery overlay on the Sensor 
Operator station, the north pointer is a floating “N” symbol that indicates the north direction 
within the sensor image. Operators often rely on this symbol to provide necessary orienting 
cues. In the absence of such a cue operators report that one can easily become disoriented, 
particularly in the absence of any significant cultural or natural features within the terrain being 
surveyed. Participants compensated for this limitation by creating a repeater image window such 
that one image window could have the RTVS system active and the other window could have the 
symbology overlay. Given the current configuration of the control station, such an approach 
worked during the 2 UAV conditions or during the 2 operator 4 UAV condition; although in this 
case operators would be unable to monitor the imagery feeds from the vehicles that were not 
under their control. While the limitation does not represent a significant technical challenge, its 
presence in the current study did serve to highlight the importance of the symbology overlay 
feature and the extent to which operators come to rely on the information it makes available.
Crew Coordination. One of the objectives of the Spiral 3 evaluation, both in simulation and in 
flight test, was to assess how operators coordinated their activity under conditions of 2-operators, 
and how the approach toward allocation of available assets and operator attention changed when 
performing the scenario under the 1 operator condition. One of the first issues that was typically 
resolved prior to trial initiation was who would be the primary “voice” for MUSCIT to 
EAGLE15. In nearly all cases, one of the MUSCIT operators was designated as the primary 
point of contact to external entities from all MUSCIT vehicles. In several cases however strict 
adherence to this division of roles applied only to those communications that were initiated by 
EAGLE15 (i.e., those instances where EAGLE15 was providing information and directing
MUSCIT to perform some task). Those instances where communications were initiated by 
MUSCIT; such as contact reports, vehicle status, situation reports, the crew often found it more 
convenient to have the operator assigned they vehicle/sensor from which the information was 
generated make the report directly to EAGLE15. In some cases crews initially limited 
communications to EAGLE to a single operator however given the frequency and details of 
reports they eventually agreed that each operator would report separately, identifying themselves 
as using the vehicle callsign (e.g., MUSCIT22) rather than MUSCIT Lead (or MUSCIT).

---
**[Page 51]**

44
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
During the 2-operator conditions the crew also needed to determine the appropriate distribution 
of tasking and assets to support this tasking. Prior to initiation of each trial, crews would 
typically decide which operator would have responsibility for each of the HVT compounds, 
Cowboys and Steelers. When four vehicles were available the allocation of the remaining two 
vehicles was at the discretion of the crew as to how to distribute these assets. In every instance 
each operator took control of one of the remaining vehicles, how they were tasked varied 
significantly across tasks. I several cases one of the vehicles was positioned over the Giants 
objective to provide ongoing situation reports. The final vehicle was either left in its original 
orbit, positioned over FOB Freedom, or in a couple of instances the final vehicle was placed in 
an orbit at a center of the area of operations, providing a general overlook of the area. One crew 
member mentioned that the positioning at the center of the area of operations would allow him to 
move quickly to any position where the vehicle may be tasked or an additional sensor asset may 
be needed. 
While the majority of tasking could be accomplished with minimal coordination, crews often 
reported to one another their current status and any significant events occurring within their area 
of responsibility. Those instances when new tasking was assigned to MUSCIT from EAGLE 15 
(e.g., forced distracter, IED event, approaching mob) without exception crews would coordinate 
on the course of action and the appropriate assignment of vehicles to the required tasking. In 
most cases, the vehicle that was in closest proximity to the assigned tasking was repositioned to 
provide the desired sensor coverage. 
Because of the dynamic nature of the assault and the required tracking of multiple squirters from 
Objective Giants, this task tended to require a higher degree of crew coordination, particularly in 
preparation for the assault itself. As the assault force moved into their respective blocking 
positions, crew would typically discuss how they would distribute the available assets, often 
dividing the compound to sections (north-south or east-west). The east-west distribution seemed 
to be the most common as the northern escape routes were well covered by the assault forces 
blocking positions. Therefore, the most vulnerable escape routes were to the south, east and 
west. Once the assault was initiated and squirters began exiting the compound, operators would 
report the location and direction of squirters and their approach toward established blocking 
positions. Those moving away from blocking positions were tracked until they stopped moving, 
at which time the operators were to provide position coordinates and help direct ground forces to 
intercept and take personnel into custody. The extent to which operators coordinated the search 
and tracking of squirters during this phase of the mission was to alert potential movement of 
individuals from one area of responsibility to another (e.g., squirter moving from the east to the 
west).
Simulation vs Flight Test. As in previous spirals, the flight test was conducted primarily to 
determine whether results from simulation trials would transfer to the flight test environment. 
The flight test environment also moves us closer to actual operations. This is because operators 
must deal with many of the same issues one finds under such conditions. Many of these issues 
we reported during previous flight test efforts. Given the sample size for the flight test it is very 
difficult to draw any definitive conclusions regarding the performance differences between the 
simulation and flight test trials. That being said, we do see that comparisons of the situational 
awareness and workload ratings between simulation and flight test appeared to track relatively

---
**[Page 52]**

45
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
well. In addition, participant responses to the post trial surveys regarding the degree to which 
various control station features supported operators during both simulation and flight test trials 
also correlate well. However, from a performance perspective there are many reasons why we 
might expect differences between the simulation and flight test environments. Probably the most 
notable difference between the simulation and flight test environment is the stability of the 
imagery that is captured by each of the sensors. While the environmental conditions present 
during the Spiral 3 flight test were much more benign than those of the Spiral 2 flight test, image 
stability remained an issue; particularly while operators narrowed the sensor FOV in their 
attempt to identify specific targets. 
Another environmental condition that appeared to have a significant impact on operator 
performance was the bright sunlight. While our previous flight tests revealed problems 
associated with image washout and glare associated with bright sunlight, the impact of sunlight 
in the current flight test was focused more on how shade influenced the ability of operators to 
maintain contact on moving targets. In mapping out locations for Objectives Steelers, Cowboys 
and Giants (See Figures 15 and 16) the MUSCIT team was conscious of the visibility of the 
route to be travelled by the HVT actors as they moved from their initial locations at Steelers and 
Cowboys to Giants. There was concern that obscuration of the route due to tree canopies would 
significantly inhibit the ability to effectively track the targets. While we were confident that the 
Cowboys location presented little problem, the route segment from Steelers to Route Michigan 
and along the initial portion of Route Michigan did have trees on either side. However, the tree 
coverage did not directly obscure visibility of the route itself. 
During data collection trials, however, participants discovered that given the sun angle and the 
position of the trees relative to the route, the route fell in shadow most of the time. Participants 
found it very difficult to discern the HVT actors once they had gone into the shadows. Several 
reported that in EO mode the shadows obscured the targets just as if they had been covered by 
trees. The impact of this effect is evident by the difference in 2 operator HVT tracking 
performance between the HVT originating from Steelers (64%) and Cowboys (93%) (See Table 
8). While the difference was not as apparent during the 1 operator trials, participants reported 
that the amount of attention directed toward maintaining track on the HVT from Steelers had a 
negative impact on their ability to establish and maintain track on the HVT from Cowboys. The 
same effect was reported during the assault phase of the mission when operators attempted to 
track HVTs departing Giants. While the HVT actors were instructed not to hide under trees, 
once they entered the shade, operators frequently reported that they had lost track due to targets 
entering the tree line.
Another difference between simulation and flight test that operators commented on was the 
impact of the Keep In Box. During the simulation trials participants were unrestricted in creating 
their Keep In Box. In most cases participants made the box big enough that it never restricted 
movement of the vehicle. During the flight test however, the Keep In Box was restricted due to 
the airspace limits imposed for safety of flight issues. On several occasions participants were 
required to steer their sensors outside the constraints of the established Keep In Box, restricting 
the movement of the loiter point (Figure 19). The effect of this restriction was the increase in the 
slant range and decrease in the slant angle of the sensor imagery. While participants commented 
on this condition, they did not report than it had any significant impact on their performance

---
**[Page 53]**
*(This page contains a figure/chart/image not captured in text)*

46
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
from an imagery perspective. Those that did report a negative consequence associated with this 
situation indicated that because the loiter point did not coincide with the sensor stare point, there 
were times during the orbit when the vehicles landing gear would obscure the imagery. This 
seemed to be more of an annoyance than a significant problem.
Figure 19. Impact of Keep In Box on vehicle mobility and MacroGrid incorporated into the TSD
The only modification to the control station interface between simulation and flight test was the 
incorporation of the MacroGrid into the TSD (Figure 19). As previously mentioned, during 
simulation, operators were required to reference a hardcopy of the MarcoGrid to locate the 
position of the suspicious activity. Several participants reported that the incorporation of the 
MarcoGrid on the TSD could reduce the time required to locate the proper grid coordinate as 
well as the opportunity for error. One of the concerns regarding the incorporation of the 
MacroGrid on the TSD was the added clutter it would create. To mitigate this concern the 
MacroGrid could be turned on and off as required using either voice command or an on-screen 
selection. Flight test participants unanimously favored the incorporation of the MarcoGrid.
6.0 Conclusions
During Spiral 1 MUSCIT investigated multi-UAV control in the context of a static task (i.e., 
point surveillance). Based on observations during data trials and participant comments it was 
evident that demands on attention management increased beyond the ability of operators to 
cope. The additional demands associated with increases in the number of vehicles (and by 
definition surveillance tasks) challenged their ability to sustain their level of performance. We 
also discovered that vulnerabilities in the means by which operators could transition across 
vehicles/sensors not only increased the difficulty of the task but significantly increased the 
opportunity for errors. Our focus, therefore, during Spiral 2 was to address these issues and 
provide better support for attention management, as well as the means to seamlessly transition 
control in correspondence with shifts in attention.

---
**[Page 54]**

47
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
In Spiral 2 we approached the attention management issue by looking at how the application of 
specialized automated features (simulated auto-detection) could help direct operator focus to 
relevant aspects of the scenario. During Spiral 2 we also expanded the set of tasks to include not 
only point surveillance, but also route surveillance and area search. By expanding the task set 
we were interested in incorporating elements of vehicle/mission management functions as well 
as the sensor management activities that were the focus of Spiral 1. As anticipated, we found 
that reliable automation can significantly enhance operator performance and serve to direct 
attention and help maintain sensor focus on relevant aspects of the mission area. Unsurprisingly, 
the key to the viability of the approach is reliable automation, a capability that accurately 
responds to the dynamics of the task under the operational conditions to be anticipated. 
During Spiral 2 we also exposed participants to a full-mission context that integrated each of the 
tasks into a composite mission scenario. The intent was to set the stage for operators and allow 
them to develop their own strategies in responding to the dynamics of evolving situations. 
Unlike the part-task trials where tasks were accomplished in isolation, operators were required to 
simultaneously perform all tasks in coordination to support a broader mission objective. 
Relaxing the constraints revealed many interesting notions in terms of how operators approached 
each phase of the scenario. What became immediately apparent was that those participants that 
had direct operational experience in these types of missions had a very unique mindset relative to 
the priorities and emphasis placed on individual task performance. Further, as the mission 
scenario increased in complexity, the ability of operators to actively respond was often inhibited 
by their lack of familiarity with the mechanics of the control station. Operators were clear in 
their intent, their strategy was sound; they were just unable to execute due to an incomplete 
understanding of the control station features. 
As we turned toward Spiral 3, the MUSCIT team concluded that the validity of our findings 
would be dependent upon two critical components. First, Spiral 3 participants should have direct 
operational experience in the type of mission to be executed. Second, participants must become 
fully competent in the mechanics and features of VSCS to fully exercise the capabilities of the 
control station. In response to this need a fully-functional VSCS control station simulation was 
delivered to our sponsor, affording the opportunity to both recruit and train competent operators 
that would participate in Spiral 3 data collection trials. This single action significantly improved 
the quality of simulation trials and provided MUSCIT analysts the opportunity to observe and 
capture the actions of experienced operators as they actively engaged in a representative 
scenario. The insights gained were invaluable in understanding the operational demands, as well 
as the opportunities afforded, while employing multiple UAVs within an operational setting.
While developing enhancements to the control station in preparation for the Spiral 3 simulation, 
discussions with operators challenged our myopic view that sensor and vehicle control were two 
separate functions. They made us realize that the ultimate reason for vehicle movement was to 
place the sensor in the position to acquire desired imagery. In other words, where one wants to 
look directly impacts where we want to place the vehicle. This led us to consider coupling 
sensor control directly to vehicle control. This feature, which we called Sensor Slaved, was 
rated by our participants as the most highly desirable feature. The coupling of sensor and vehicle 
control suddenly relieved operators of the demands of vehicle management. It should be noted 
that consideration must be given to issues related to vehicle control such as airspace

---
**[Page 55]**

48
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
deconfliction and vehicle separation. We accomplished this through altitude separation of 
MUSCIT vehicles and constrained movement of vehicles to a limited restricted operating zone. 
As part of the Spiral 3 control station we also incorporated an auto-tracking capability that was 
capable of maintaining positive contact on dynamic ground targets. Unlike Spiral 2 where 
automation was simulated, the auto-tracker used during Spiral 3 was a viable capability. 
Operators could designate a target and using pixel processing, the tracker would steer the sensor 
to maintain the target within the sensor FOV. The variable reliability of the auto-tracker 
provided some unique insights into how operators used the feature and the tolerance to failure 
they exhibit before they would revert to manual tracking. That said, the incorporation of the 
auto-tracker coupled with the Sensor Slaved mode proved to be an extremely powerful tool and 
was considered highly desirable by participants.
In the final analysis, the question remains, “Is multi-UAV operations a viable concept?” Based 
on observations and findings resulting from the three MUSCIT spirals we believe the answer is 
yes. MUSCIT’s initial spirals focused on the issue of capacity; how many can a single operator 
manage. Like all such questions, it depends. However, we were certainly able to identify 
specific capabilities and features that could certainly reduce demands on operators and improve 
the quality of experience during multi-UAV operations. During our final spiral we found that 
increasing the number of UAVs can actually improve performance and the ability of operators to 
adaptively respond to dynamic situations. Given the additional resources available through 
access to more vehicles, operators were able to position their sensor in anticipation of events, 
allowing them to respond in a more timely manner to time critical events. The challenge for 
developers of UAV systems is to ensure that the overhead associated with providing additional 
vehicles does not outweigh the value gained from additional sensor resources.
7.0 References
Cullen, T.M. (2011). The MQ-9 Reaper Remotely Piloted Aircraft: Humans and Machines in 
Action. Dissertation Thesis, Massachusetts Institute of Technology, Cambridge, MA
Hart, S.G. and Staveland, L.E. (1988). Development of NASA TLX (Task Load Index): Result
of Empirical and Theoretical Research. In P. A. Hancock & N. Meshkati (Eds.), Human Mental
Workload (pp. 239-250). Amsterdam: North Holland Press.
Headquarters United States Air Force (2009). United States Air Force Unmanned Aircraft 
Systems Flight Plan 2009-2047. Washington D.C.
Hughes, T.C., Flach, J.K., Patzek, M.J., Zimmer, D.J. and Delaunois, S.A (2009). Multi-UAV 
Supervisory Control Interface Technology (MUSCIT) Spiral 1 Simulation Study Test Report. 
AFRL-RH-WP-TR-2010-0112, Wright-Patterson AFB, OH

---
**[Page 56]**

49
Distribution A: Approved for public release; distribution unlimited.
88ABW/PA Cleared 01/25/2013; 88ABW-2013-0334.
Hughes, T.C., Flach, J.K., Squire, M., Zimmer, D.J., Delaunois, S.A. and Patzek, M.J. (2011). 
Multi-UAV Supervisory Control Interface Technology (MUSCIT): Spiral 1 Flight Test Report. 
AFRL-RH-WP-TP-2011-0024, Wright-Patterson AFB, OH
Hughes, T.C., Flach, J.K., Squire, M., Zimmer, D.J., Patzek, M.J. and Feitshans, G.L. (In Press). 
Multi-UAV Supervisory Control Interface Technology (MUSCIT): Spiral 2 Technical Report. 
AFRL-RH-WP-TP-2012-XXXX, Wright-Patterson AFB, OH
Klein, G. (1998). Sources of Power: How People Make Decisions. The MIT Press, Cambridge, 
Massachusetts, pp. 4-6.
Office of the Secretary of Defense (2007). Unmanned Systems Roadmap 2007-2032. 
Washington D.C. 
Tadema, J. (2011). Unmanned Aircraft Systems HMI & Automation: Tackling Control, Integrity 
and Integration Issues. Shaker Publishing, Maastricht, Netherlands. 
Woods, D.D. and Hollnagel E. (2006). Joint Cognitive Systems: Patterns in Cognitive Systems 
Engineering. CRC Press, Boca Raton, FL

---
**[Page 57]**

50
8.0 List of Acronyms and Abbriviations
ACA Airspace Control Authority
AFRL Air Force Research Lab
AOI Area of Interest
ATC Air Traffic Control
CAS Close Air Support
CIB Controlled Image Database
CMF Common Message Format
DMP Dynamic Mission Planning
DoD Department of Defense
DV Dependent Variable
DVR Digital Video Recorder
EO Electro-Optical
ETA Estimated Time of Arrival
ETE Estimated Time Enroute
FOV Field of View
FLAMES FLexible Analysis Modeling and Exercise System
GNC Global Navigation and Planning Charts
HCI Human Computer Interaction
IR Infrared 
JNC Jet Navigation Charts
JOG Joint Operation Graphics

---
**[Page 58]**

51
LCD Liquid Crystal Display
MAC Multi-Aircraft Control
MUSCIT Multi-UAV Supervisory Control Interface Technology
NASA National Aeronautics and Space Administration
ONC Operation Navigation Charts
POI Point of Interest
RSTA Reconnaissance, Surveillance, and Target Acquisition
SO Sensor Operator
SOF C2 Special Operations Forces Command and Control
SUV Sport Utility Vehicle
TLX Task Load Index 
TPC Tactical Pilotage charts
TSD Tactical Situation Display
UAS Unmanned Aircraft System
UAV Unmanned Aerial Vehicle
VoIP Voice-over Internet Protocol
VRSG Virtual Reality Scene Generator
VSCS Vigilant Spirit Control Station