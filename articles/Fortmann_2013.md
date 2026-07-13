# Fortmann 2013

*Source file: Fortmann_2013.pdf — 10 pages*


---
**[Page 1]**

 
 
SA-Based Guidance to Aid UAV 
Swarm Supervisory Control: What do 
Experts Say? 
Florian Fortmann 
Human Centered Design, OFFIS – Institute for Information Technology 
Abstract 
Recent incident reports reveal that incorrect Situation Awareness (SA) due to deficits in scanning be-
haviour is a frequent cause of human errors in context of supervisory control of Unmanned Aerial 
Vehicles (UAV). In the future, the number of UAVs human operators have to supervise at the same 
time will increase. Thus, methods are needed aiding deficits in their scanning behaviour. Our research 
focuses on the development of a novel attention assistance system – called Supervisory Guide. Supervi-
sory Guide aims at optimizing the scanning behaviour of a human operator based on the determination 
of actual SA-needs. These SA-needs are inferred from eye movements recorded and analysed in real-
time. In this paper we present the results of an early prototype evaluation performed with three Special 
Matter Experts (SME). Each SME evaluated the prototype from a different perspective. Overall, the 
SMEs agreed that Supervisory Guide implements a promising concept to aid deficits in scanning be-
haviour and SA. 
1 Motivation and Background 
Today, a complex, Unmanned Aerial Vehicle (UAV) is typically operated by a team of human 
operators via dedicated Human-Machine Interfaces (HMI). However, the interest of stake-
holders in UAV swarms, which can be operated by a single human operator via a dedicated 
HMI increased significantly (Brian et al. 2005). The expected benefits are, e.g., reduced costs 
for personnel and higher system reliability and resilience. Key enablers are the ever-
increasing levels of machine automation (Parasuraman et al. 2000) and autonomy 
(Cummings 2004), which release limited cognitive resources of  a human operator to rede-
ploy them for managing multiple UAVs at the same time. Consequently, supervisory control 
becomes a much more substantial task a human operator has to perform. A general require-
ment for the successful application of a supervisory control task is the human operator’s 
capability to continuously build and maintain good Situation Awareness (SA). 
S. Boll, S. Maaß & R. Malaka (Hrsg.): Mensch & Computer 2013 
München: Oldenbourg Verlag, 2013, S. 139– 148 

---
**[Page 2]**
*(This page contains a figure/chart/image not captured in text)*

140 
Fortmann 
 
 
Figure 1: Supervisory Guide assists a human operator supervising a highly autonomous UAV swarm  
SA is defined as a state of knowledge including the perception of the elements in the envi-
ronment (SAlevel1), the comprehension of their meaning (SAlevel2) and the projection of their 
status in the near future (SAlevel3) (Endsley 1995). Because these levels build upon each other 
(SAlevel1 → SAlevel2 → SAlevel3) it is important for building and maintaining good SA on all 
levels that a human operator supervising a UAV swarm continuously scans relevant infor-
mation on the HMI. Otherwise, incidents caused by poor SA are likely to occur. However, 
for single UAV supervisory control it was shown that several human factors (e.g., boredom 
and distraction) constrain effective and efficient scanning behaviour (Cummings et al. 2013). 
Further, no prophet is needed to anticipate that supervisory control of future UAV swarms 
will suffer from the same problems and that the effects will be even worse. This assumption 
is supported by studies conducted in synthetic environments (Cummings et al. 2013). Thus, 
there is considerable need for methods, which can be applied to improve the scanning behav-
iour and SA of a human operator managing a UAV swarm. 
In this paper, we present Supervisory Guide – an assistance system that aims at aiding poor 
SA by guiding a human operator’s visual attention during UAV swarm supervisory control to 
information that he/she should know but actually doesn’t know (see Figure 1). Improving SA 
of human operators in charge of supervisory control tasks has received much attention in the 
past. Basically, there are two categories of methods for tackling this problem: the first cate-
gory subsumes methods to design SA-friendly HMIs (Endsley et al. 2003); the second cate-
gory subsumes methods to assist human operators in real-time to build and maintain good 
SA. The focus of our research is on methods of the second category. Examples of the second 
category are, e.g., (1) alarm systems and (2) cognitive assistance systems. 
Alarm systems are event-based, using sensors to measure and analyse given environmental 
and/or vehicle conditions. In the case of an event (encoded using thresholds) an alarm is 
triggered in order to guide the visual attention of the human operator to the relevant infor-
mation source. Using a visual or auditory alarm to raise the awareness of a human operator in 
the case of a critical situation is an effective method to prevent an SA-related error or acci-
dent. However, determining whether and when an alarm is needed is a difficult issue. Reports 
reveal that pilots and air traffic controllers ignored alarms (Breznitz 1984) or even turned 
them off prior to accidents (Wickens et al. 2009). Besides to false alarms, the high number of 

---
**[Page 3]**

SA-Based Guidance to Aid UAV Swarm Supervisory Control: What do Experts Say? 
141 
 
unwarranted nuisance alarms which human operators are exposed to during routine tasks is a 
problem, which could consequently lead to annoyance, frustration and distraction. As stated 
in (Getty et al. 1995) this problem can be approached from two perspectives of the signal 
detection theory, corresponding to the parameters 'sensitivity' and 'response bias'. However, 
this approach is no final solution: (1) more or earlier alarms induce more dispensable alarms 
and (2) less or later alarms induce more critical situations.  
A solution lies in the understanding and consideration of human operator SA within the deci-
sion making process implemented in the alarm system. Such an enhanced decision making 
process is a key feature of cognitive assistance systems like the Cognitive ASsistant SYstem 
(CASSY) (Onken 1999) and the COGnitive cockPIT (COGPIT) (Taylor et al. 2000). A cog-
nitive assistance system takes into consideration the cognitive state and information pro-
cessing limitations of human operators to optimize the information presentation and human-
automation task distribution during task performance in a flexible, context-dependent way. 
The general philosophy of a cognitive assistance system is twofold: (1) to aid SA by guiding 
the attention of human operators to the objectively most urgent task or subtask of that situa-
tion; (2) to take care that human operators are never overburdened, e.g., by too many parallel 
tasks (Flemisch & Onken 1998). In order to accomplish the first aspect of this philosophy the 
cognitive assistance system needs an understanding of the situations in a way that is compa-
rable to the human operator's understanding. In order to accomplish the second aspect the 
cognitive assistance system needs an understanding of the human operator's cognitive state, 
which could be derived from psychological theories and psycho-physiological measures. 
In the remainder of this paper, we briefly present the concept of Supervisory Guide (Section 
2). Then, we present the evaluation of an early prototype conducted with three experts from 
the perspectives usability, human factors and UAV manufacturing in order to get an impres-
sion of the expectable user acceptance, safety impact and market potential (Section 3). Final-
ly, we present our conclusions and future work (Section 4). 
2 Supervisory Guide 
Supervisory Guide aims at optimizing the scanning behaviour of a human operator based on 
the detection of actual SA-gaps. Roughly speaking, an SA-gap is a deviation between what 
the human operator actually knows and what he/she should know about his/her situation. 
According to Endsley, this knowledge includes knowledge on three levels. Basically, SA-
based guidance can be subsumed by the following system’s point of view statement: “Tell me 
what you know about your situation and then I will show you what you should really know.” 
This statement consists of two aspects: 

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

142 
Fortmann 
 
 
Figure 2: Steps performed by Supervisory Guide 
The first aspect (Tell me what you know…) refers to the issues (1) determination and (2) 
assessment of SA, and the subsequent (3) detection of SA-gaps. The second aspect (…and 
then I will show you what you should really know) refers to the issues (4) HMI adaptation, 
(5) guidance of visual attention and the subsequent (6) elimination of SA-gaps. 
Currently, Supervisory Guide focuses on aiding SAlevel1 by eliminating SAlevel1-gaps. The 
generic concept of Supervisory Guide is shown in Figure 2. Green arrows represent steps of 
the first and blue arrows of the second aspect. The foundation of this concept is using eye 
movements as indications of SAlevel1 (Salmon et al. 2006). The theoretic foundation of this 
approach is the eye-mind hypothesis, which states that where humans look at and what they 
think about tends to be the same (Just & Carpenter 1980). Although it can be criticized that 
the hypothesis fails in some situations of daily life we assume that it mainly holds for super-
visory control of a UAV swarm. The validity of this approach is supported by recent studies 
showing that eye movements of human operators in charge of supervisory control tasks are 
valuable indications of SA. This has been shown, e.g., for air traffic control (Moore 2009), 
manned (Van de Merwe et al. 2012) and unmanned aviation (Ratwani et al. 2010). We hy-
pothesize that knowing the relevance of information and the human operator’s mental picture 
in context of a situation allows optimizing the scanning behaviour of the human operator 
with regard to his/her actual SA-needs and therefore reduces the number of unwarranted 
alarms. In the following, we elaborate more on the individual steps applied by Supervisory 
Guide. 
2.1 Steps 1-3: Determination, Assessment and Detection 
Supervisory Guide continuously (1) determines and (2) assesses SAlevel1 based on a formal 
situation model Sit, which is composed on the lowest level of a set of information elements 
Inf (Frische & Lüdtke 2013). In step (1), Supervisory Guide analyses eye movements (rec-
orded by an eye tracker) on the HMI and interprets them in context of the displayed infor-
mation in order to generate a subjective instance Sitsub (including Infsub). In step (2), Supervi-

---
**[Page 5]**
*(This page contains a figure/chart/image not captured in text)*

SA-Based Guidance to Aid UAV Swarm Supervisory Control: What do Experts Say? 
143 
 
sory Guide compares Infsub to the information elements Infobj of the objective situation model 
instance Sitobj. In step (3), Supervisory Guide identifies individual SAlevel1-gaps. For a specific 
information element inf ∈ Inf an SAlevel1-gapinf is a deviation between infsub and infobj. As 
shown 
in 
Figure 
2, 
this 
can, 
e.g., 
be 
a 
sudden 
UAV 
malfunction 
(in-
fobj:UAV2.malfunction=TRUE), which occurs while the human operator is not looking at the 
associated information source (UAV2). Consequently, the human operator might believe that 
there is currently no problem (infsub:UAV2.malfunction=FALSE). 
2.2 Steps 4-6: Adaptation, Guidance and Elimination 
If Supervisory Guide detects an SAlevel1-gap, the assistance system (4) adapts the HMI char-
acteristics accordingly. Comparable to (Ratwani et al. 2010), our HMI consists mainly of a 
single screen with a 2D map display. Furthermore, there is an aircraft (A/C) check list and 
control buttons on the right side (see Figure 3). On the map, information objects (e.g., UAV 
icons or text labels) are presented, which are associated with information elements (e.g., 
UAV identity or location). At each point in time, the HMI is in a certain state determining, 
e.g., the location or salience of information objects and associated information elements. In 
this paper, we initially investigate the suitability of using three colour codes (green, yellow, 
red) as a means for displaying SAlevel1-gaps of three different criticality levels (safe, caution, 
danger) on the HMI. We decided to use three colours because there is international agree-
ment about how they refer to safety words (Salvendy 2012). The criticality level of a certain 
gap SAlevel1-gapinf is calculated based on the relevance of inf in context of pertinent goals and 
the degree of deviation between infsub and infobj. On the HMI, each information object is 
surrounded by a rectangular shape indicating the current criticality level of associated infor-
mation elements. Using these visual cues, Supervisory Guide (5) guides the human operator's 
visual attention (within a volume of time [t1, t2]) to the information object associated with the 
SAlevel1-gap. Consequently, the gap will be (6) eliminated on-the-fly. 
 
Figure 3: HMI for UAV supervisory control with coloured shapes for highlighting the criticality of SAlevel1-gaps 

---
**[Page 6]**

144 
Fortmann 
 
3 Evaluation 
The goal of this evaluation was to get an impression of the expectable user acceptance, safety 
impact and market potential. Thus, the evaluation was performed with Special Matter Ex-
perts (SME) in the field of usability engineering, human factors and UAV manufacturing. 
3.1 Participants 
We invited three SMEs of three different areas to evaluate Supervisory Guide. SME#1 was a 
researcher in the field of human factors in safety critical systems working at the OFFIS – 
Institute for Information Technology in Oldenburg. SME#2 was a researcher in the field of 
usability engineering and interactive human-machine systems working at the University of 
Oldenburg. SME#3 was an aerospace and astronautics engineer working at the UAV manu-
facturer Rheinmetall Airborne Systems GmbH in Bremen. 
3.2 Setup and Equipment 
A notebook was used to run the UAV simulation, the HMI and Supervisory Guide. The eye 
movements of the participants were recorded with the Dikablis head mounted eye tracking 
system from Ergoneers (see Figure 1). A 24-inch monitor was used to display the HMI. Two 
eye tracking markers were attached to the display (bottom left and top right). The partici-
pants were seated approximately 0.6 meters from the display and used a mouse device to 
manage events that occurred during the scenarios. 
3.3 Procedure 
Each participant evaluated Supervisory Guide in a separate session. Each session took about 
an hour. First, each participant was introduced to the concept of SA-based guidance and 
Supervisory Guide. The participants SME#1 and SME#2 were also introduced to UAVs and 
UAV supervisory control tasks. Then, each participant was calibrated for the eye tracker. 
After the successful calibration, each participant participated in an experiment which con-
sisted of two comparable scenarios, where they had to manage a swarm of highly automated 
and autonomous UAVs using our HMI (see Figure 3). In the scenarios, a swarm of three 
UAVs was managed to extinguish fires in an area which was not accessible by human fire 
fighters using ordinary equipment. In order to extinguish the fire sources each UAV had to 
load water at a water source and unload water at one of the fire sources. During mission 
execution each UAV had to frequently recharge energy at a base. The human operator could 
not influence the UAV task selection. However, at random times two distinct types of events 
were induced, which the human operators had to handle manually. First, UAV malfunctions 
were triggered which had to be detected and resolved by the participants by clicking the 
UAV icon and then pressing the „Repair UAV“ button on the HMI. Second, intruders entered 
the mission area, which had to be classified (using the aircraft (a/c) list on the HMI). Intrud-
ers could either be fire fighting aircrafts or civil aircrafts. Fire fighting aircrafts had to be 
allocated to the fire sources by clicking the aircraft icon, a target fire and then pressing the 
“Allocate Target” button. Civil aircrafts had to be detoured by clicking the aircraft icon and 
pressing the “Detour Flight” button. In the first scenario Supervisory Guide was deactivated. 

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

SA-Based Guidance to Aid UAV Swarm Supervisory Control: What do Experts Say? 
145 
 
Thus, the visual attention of the participants was not guided (control condition). In the sec-
ond scenario Supervisory Guide was activated. Thus, the visual attention of the participants 
was guided (experimental condition). Each participant tested each condition for 20 minutes. 
3.4 Measures 
After each condition, the participants rated their SA using SART (Situation Awareness Rating 
Technique). SART is the most widely known SA self-rating technique. We used a shortened 
version of the technique (SART-3), which consisted of three statements. Each of the state-
ments had to be answered on a Likert scale ranging from 1 (strongly agree) to 5 (strongly 
disagree). The statements were: “The task was mentally demanding”, “I could have managed 
more UAVs” and “I was able to keep track of what was going on”. After the experiment, a 
semi-structured interview was performed. 
3.5 Results 
The results of the SART-3 questionnaire are depicted in Figure 4. In average, the participants 
agreed that performing the supervisory control task was more mentally demanding when 
Supervisory Guide was activated (M=2.3) as compared to when the system was not activated 
(M=4). Further, they agreed that they could have managed more UAVs when Supervisory 
Guide was not activated (M=1.7) as compared to when the system was activated (M=2). 
However, they also agreed that they were better able to keep track of what was going on 
when Supervisory Guide was activated (M=1.3) as compared to when the system was not 
activated (M=2.3). Due to the fact that three subjects are not enough to make a strong state-
ment we can only carefully assume that Supervisory Guide increases the mental demand but 
improves SA.  
 
Figure 4: Results of the SART-3 questionnaire 
During the interviews, we received further valuable qualitative feedback from the partici-
pants. Overall, they agreed that SA-based guidance is a very interesting and useful concept 
and that further effort should be invested in the research of Supervisory Guide. Although 
they mentioned that being observed by the eye tracker while performing the supervisory 

---
**[Page 8]**

146 
Fortmann 
 
control task was an unpleasant feeling at first, they agreed that they could adjust after some 
time of using the system. 
SME#1 mentioned that wearing the eye tracker was uncomfortable. The uncomfortable feel-
ing could potentially distract users from the supervisory control task. Thus, he recommended 
replacing the head mounted eye tracker by a screen based eye tracking system to improve the 
comfort. An important remark was that the calibration of the eye tracker is essential for the 
trust that users have in the system. Sloppy calibration would cause the cry-wolf effect 
(Breznitz 1984). It has to be assessed whether it will be possible in the future to guarantee 
good calibrations with acceptable effort. Further, he mentioned that Supervisory Guide seems 
to increase workload because the transitions between the criticality levels were very fast. He 
assumed that better adjustment of threshold parameters would reduce the perceived work-
load. 
SME#2 suggested that using green, yellow and red rectangles is not very useful for the given 
context of use. She argued that green rectangles are not needed at all and that not displaying 
green rectangles would also de-clutter the HMI allowing for better supervisory control per-
formance. For the same reason, she suggested colourizing the icons itself instead of using 
rectangles. A major remark was that using red and green is problematic due to colour blind-
ness. Colour blind users have no chance to distinguish between the criticality levels because 
the shapes are similar. Further on, she suggested using halo effects as a means to increase the 
obtrusiveness of visual alarms. Currently, green, yellow and red rectangles are similar in its 
obtrusiveness. Using the halo effect could also reduce the perceived workload. 
SME#3 agreed that bad scanning performance is actually a problem of human operators in 
charge of UAV supervisory control. He pointed out that using eye tracking and SA-based 
guidance could have impact on safety. However, he stated that the trade-off between cost and 
value has to be kept in mind. Current eye tracking systems are very expensive. But if prices 
fell down the technique would be much more attractive for manufacturers. It would also add 
a new selling point to the company’s portfolio. 
4 Conclusions and Future Work 
In this paper, we presented Supervisory Guide - an assistance system for SA-based guidance 
of visual attention for UAV swarm supervisory control. An evaluation of the Supervisory 
Guide prototype was conducted with three SMEs from the perspectives usability, human 
factors and UAV manufacturing to get an impression of the expectable user acceptance, safe-
ty impact and market potential. Overall, the results showed that Supervisory Guide increased 
mental demand but also improved SA. The interviews revealed that the SMEs think that SA-
based guidance is a very interesting concept and that more research of this concept is desira-
ble. The SMEs also provided valuable feedback to improve guidance of visual attention. The 
evaluation served as first proof-of-concept. In the future, we will investigate how guidance of 
visual attention could be improved. The experts gave a lot of valuable feedback how this 
could be done. Within an iterative design process we will improve our prototype along these 
results and prepare it for a user study with the target group to investigate the effects on SA. 

---
**[Page 9]**

SA-Based Guidance to Aid UAV Swarm Supervisory Control: What do Experts Say? 
147 
 
Acknowledgements 
We would like to thank the SMEs who participated in the evaluation and shared their 
knowledge with us. This research is conducted within the European project D3CoS and 
funded by ARTEMIS-JU and national authorities under grant agreement no. 269336. 
References 
Breznitz, S., 1984. Cry Wolf: The Psychology of False Alarms, Lawrence Erlbaum 
Associates. 
Brian, H.H., Mclaughlan, B. & Baker, M., 2005. Swarm Control in Unmanned Aerial 
Vehicles. In Proceedings of International Conference on Artificial Intelligence (IC-AI), 
CSREA. Press. 
Cummings, M.L. et al., 2013. Boredom and Distraction in Multiple Unmanned Vehicle 
Supervisory Control. Interacting with Computers, 25(1), pp.34–47. 
Cummings, M.L., 2004. Human supervisory control of swarming networks. In 2nd Annual 
Swarming: Autonomous Intelligent Networked Systems Conference. pp. 1–9. 
Endsley, M.R., 1995. Toward a Theory of Situation Awareness. Human Factors, 37(1), 
pp.32–64. 
Endsley, M.R., Bolte, B. & Jones, D.G., 2003. Designing for Situation Awareness: An 
Approach to User-Centered Design, Taylor and Francis. 
Flemisch, F. & Onken, R., 1998. The Cognitive Assistant System and its Contribution to 
effective Man/Machine Interaction. The Application of Information Technology 
(Computer Science) in Mission Systems. 
Frische, F. & Lüdtke, A., 2013. SA-Tracer: A Tool for Assessment of UAV Swarm Operator 
SA during Mission Execution. In Proceedings of the IEEE Conference on Cognitive 
Methods in Situation Awareness and Decision Support (CogSIMA). 
Getty, D.J. et al., 1995. System operator response to warnings of danger: A laboratory 
investigation of the effects of the predictive value of a warning on human response time. 
Journal of Experimental Psychology, 1(1), pp.19–33. 
Just, M.A. & Carpenter, P.A., 1980. A theory of reading: from eye fixations to 
comprehension. Psychological Review, 87(4), pp.329–354. 
Van de Merwe, K., Van Dijk, H. & Zon, R., 2012. Eye Movements as an Indicator of 
Situation Awareness in a Flight Simulator Experiment. The International Journal of 
Aviation Psychology, 22(1), pp.78–95. 
Moore, K.S., 2009. Comparison of Eye Movement Data to Direct Measures of Situation 
Awareness for Development of a Novel Measurement Technique in Dynamic, 
Uncontrolled Test Environments. Clemson University. 
Onken, R., 1999. The Cognitive Cockpit Assistant Systems CASSY/CAMA. In SAE 
International. 
Parasuraman, R., Sheridan, T.B. & Wickens, C.D., 2000. A model for types and levels of 
human interaction with automation. Systems, Man and Cybernetics, Part A: Systems and 
Humans, IEEE Transactions on, 30(3), pp.286–297. 

---
**[Page 10]**

148 
Fortmann 
 
Ratwani, R.M., McCurry, J.M. & Trafton, J.G., 2010. Single operator, multiple robots: An 
eye movement based theoretic model of operator situation awareness. 2010 5th 
ACMIEEE International Conference on HumanRobot Interaction HRI, (55), pp.235–242. 
Available at: http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=5453191. 
Salmon, P.M. et al., 2006. Situation awareness measurement: a review of applicability for 
C4i 
environments. 
Applied 
Ergonomics, 
37(2), 
pp.225–238. 
Available 
at: 
http://eprints.soton.ac.uk/73745/. 
Salvendy, G., 2012. Handbook of human factors and ergonomics, Wiley. 
Taylor, R., Howells, H. & Watson, D., 2000. The Cognitive Cockpit: Operational 
Requirements and Technical Challenge. In P. McCabe, S. Robertson, & M. Hansen, eds. 
Contemporary Ergonomics 2000. CRC Press Inc, pp. 57–66. 
Wickens, C.D. et al., 2009. False Alerts in Air Traffic Control Conflict Alerting System: Is 
There a Cry Wolf Effect? Human Factors: The Journal of the Human Factors and 
Ergonomics Society, 51(4), pp.446–462. 
Contact 
Florian Fortmann (florian.fortmann@offis.de), OFFIS – Institute for Information Technology 
Escherweg 2, 26121 Oldenburg, Germany 
