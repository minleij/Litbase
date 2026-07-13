# Gregorio 2021

*Source file: Gregorio_2021.pdf — 16 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

future internet
Article
Improving Human Ground Control Performance in Unmanned
Aerial Systems
Marianna Di Gregorio 1, Marco Romano 1, Monica Sebillo 1, Giuliana Vitiello 1,* and Angela Vozella 2


Citation: Gregorio, M.D.; Romano,
M.; Sebillo, M.; Vitiello, G.; Vozella, A.
Improving Human Ground Control
Performance in Unmanned Aerial
Systems. Future Internet 2021, 13, 188.
https://doi.org/10.3390/fi13080188
Academic Editor: Nathalie Mitton
Received: 21 June 2021
Accepted: 19 July 2021
Published: 22 July 2021
Publisher’s Note: MDPI stays neutral
with regard to jurisdictional claims in
published maps and institutional affiliations.
Copyright: © 2021 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
1 Department of Computer Science, University of Salerno, 84040 Fisciano, Italy;
madigregorio@unisa.it (M.D.G.); marromano@unisa.it (M.R.); msebillo@unisa.it (M.S.)
2
Italian Aerospace Research Center, 81043 Capua, Italy; a.vozella@cira.it
* Correspondence: gvitiello@unisa.it
Abstract: The use of Unmanned Aerial Systems, commonly called drones, is growing enormously
today. Applications that can benefit from the use of fleets of drones and a related human–machine
interface are emerging to ensure better performance and reliability. In particular, a fleet of drones
can become a valuable tool for monitoring a wide area and transmitting relevant information to
the ground control station. We present a human–machine interface for a Ground Control Station
used to remotely operate a fleet of drones, in a collaborative setting, by a team of multiple operators.
In such a collaborative setting, a major interface design challenge has been to maximize the Team
Situation Awareness, shifting the focus from the individual operator to the entire group decisionmakers. We were especially interested in testing the hypothesis that shared displays may improve
the team situation awareness and hence the overall performance. The experimental study we
present shows that there is no difference in performance between shared and non-shared displays.
However, in trials when unexpected events occurred, teams using shared displays-maintained good
performance whereas in teams using non-shared displays performance reduced. In particular, in case
of unexpected situations, operators are able to safely bring more drones home, maintaining a higher
level of team situational awareness.
Keywords: unmanned aerial systems; user centered design; situation awareness
1. Introduction
Unmanned Aerial Systems (UAS), commonly known as drones, are being employed
in more and more civilian settings, from crowd-monitoring activities, to road traffic control,
to agricultural crop monitoring. The number of civil applications where UAS can be both
effectively and efficiently used has increased in recent years, thanks to a considerable
reduction in costs. UAS can be remotely piloted (RPAS—Remotely Piloted Aircraft System)
or they can automatically fly. As a single powerful UAS equipped with a large array
of different sensors is limited to a single point of view, in recent years, the multi-UAS
paradigm seems to be a more suitable approach for many applications requiring the
observation of wider areas. One of the emerging areas of the civilian use of UAS is public
safety and services [1].
Moreover, the multi-UAS paradigm can guarantee:
• Multiple simultaneous interventions: a UAS fleet can simultaneously collect data from
multiple locations
• Greater efficiency: a UAS fleet can split up to efficiently cover a large area, optimizing
available resources
• Complementarity: a UAS fleet can perform different tasks with growing accuracy
• Reliability: a UAS fleet assures fault-tolerant missions by providing redundancy and
capability of reconfiguration in the case of a failure of a vehicle
• Safety: for a permit to fly, a fleet of mini-UAS is safer than a single big and heavy UAV
Future Internet 2021, 13, 188. https://doi.org/10.3390/fi13080188 https://www.mdpi.com/journal/futureinternet

---
**[Page 2]**

Future Internet 2021, 13, 188 2 of 16
• Cost efficiency: a single vehicle to execute some tasks could be an expensive solution
when comparing to several low-cost vehicles.
Safety is a very important aspect and in recent years the number of accidents in which
drones are involved is high [2]. Studies reveal that a major cause is ground operators’ error,
due to poorly designed user interfaces [3,4].
Therefore, applications have emerged which require the use of a fleet of drones and a
related human-machine interface to ensure better Situation Awareness (SA) by the operator.
In fact, the lack of situation awareness (SA) is also often cited as a major cause of
accidents [5] and therefore understanding SA and improving it with adequate system
design is an important research target [6]. As a result, much work has been published on
the subject.
In a previous paper, we set out a vision on how to design a human machine interface
for a GCS (Ground Control Station) of a fleet of drones performing a mission of persistent
surveillance [7]. The design challenge for the fleet management interface was to capitalize
all the available heterogeneous amount of data coming from drones and to set up a
mechanism to allow efficient and safe interaction between the ground operator and the
fleet, thanks to an enhanced SA. We focused on the design of a user interface which would
allow a single remote ground operator to control a fleet of multiple drones. In the resulting
prototype, scientific data coming from drones’ payload are timely transformed into useful
information on the interface in a way that supports an operator’s SA, reducing the risk of
being overwhelmed by information which may hinder his/her decision-making capability.
The prototype can manage and show relevant data about the status of the drones such as
battery life, altitude, coordinates, id, distance from the next target. All for the sake of safety
and mission success.
In the present paper we consider another realistic situation, which may occur when
a fleet of drones is remotely operated from a ground control room in a collaborative
setting, i.e., by a team of multiple operators. Control rooms for mission critical operations
and monitoring networks have changed considerably over the years, relying today on
smart technology able to better support human–machine allocation tasks and decision
support activities as well as collaborative tasks. In particular, we adopted a MultiTouch
wall display to design a human–machine interface for a GCS (Ground Control Station)
of a fleet of drones, conceived to allow collaboration among multiple operators. The
working conditions of the control room operators are characterized by high cognitive
workload in terms of user’s attention and decision processes both in daily routine and
extraordinary/unexpected circumstances. Therefore, the concept of situation awareness
acquires a collective meaning, shifting the focus from the SA of the individual operator
to that of the entire team of decision makers, resulting in a multidimensional feature that
researchers call Team Situation Awareness (TSA) [8–10]. Maximizing TSA has been our
major interface design challenge. The study we present is meant to test the hypothesis that
shared displays may improve team performance [11,12]. To do this, in the experiment the
displays are manipulated within a simulation of a mission, and the performance assessed
in routine operating conditions and in the event of unexpected events.
The results show that the shared displays do not universally improve team performance, but they help maintain performance in off-nominal situations. Hence, it can be
assumed that in those situations the operators will deliver better performance, relying on a
higher level of situation awareness.
The paper is organized as follows. Section 2 illustrates some related work on the
Ground Control Station interfaces, on the team situation awareness and the shared displays
and team performances. Section 3 illustrates the system requirements that may impact the
interface design choices, the description of the GCS interface prototype, and the system
architecture. Section 4 discusses the study carried out to evaluate the team performance
and situation awareness of the use of the prototype on a shared screen, and the related
results. Section 5 concludes the document.

---
**[Page 3]**

Future Internet 2021, 13, 188 3 of 16
2. State of the Art
2.1. Ground Control Station Interfaces
A survey was carried out on the current state of the GCS user interface for remote
control of drones. There are tools supporting the user to set up the system, procedures to
ensure correct configuration and correct operation of the related software, the procedure
for planning the mission (design of the route that the drone should perform), tools allowing
users to monitor flight in real-time and tools to analyze and debug flight mission data [13].
Some GCS interfaces already communicate to user’s crucial information concerning
the operation of drones: incompatibility alerts, usage instructions or safety checks, that
prevent the user from basic errors. Some apps already provide learning/support material.
Most of them appear in mobile apps targeting basic drone users. However, such apps
were conceived for use in missions only, focusing on video recording or mapping [14].
In addition to displaying graphs, some apps have rerun mission features that are very
interesting for visually representing the data collected during flights [15]. However, they
often result in hard-to-use user interfaces for mission planning activities as well as for
alerting and recovery actions and for drone flight data analysis. Moreover, most of those
interfaces do not support fleet mission management and hence do not properly address
issues related to situation awareness and safety.
Our case study, for detecting an area and transmitting relevant information to the
ground control station, builds upon a more complex system especially conceived to support remote control of multiple drones operating synergistically. In addition, the system
was designed for use on a MultiTouch wall where multiple users can interact with it
simultaneously. Currently, in literature, it is not possible to find this type of system.
For such a system the design of a usable interface raises even more challenges and
becomes paramount for the proper management of a fleet mission.
2.2. Team Situation Awareness
Situation Awareness is an individual’s awareness in a situation—one person’s understanding of “what is going on” in that exact situation. The SA is different from person to
person even if people have the same information available and the same working conditions. This is because cognitive factors such as experience, mental models, schemata, and
qualifications differ between individuals.
A team can be characterized as a group of people with a shared goal. Working in a
team may give several advantages over single operators, such as sharing the workload
between operators, contributing with expertise on subtasks and there may be an advantage
in safety considering that the operators can check each other’s work.
Several papers have been published with good theoretical accounts of situation awareness in teams [8–10,16]. In particular, Endsley defines situation awareness as “the perception of the elements in the environment within a volume of time and space, the comprehension of their meaning and the projection of their status in the near future.” She defines
TSA as “the degree to which every team member possesses the SA required for his or
her responsibility,” distinguishing this from SA which is shared [8]. Salas et al. [9] and
Stout et al. [10] place a greater emphasis on the shared understanding of a situation in TSA
and also consider the issue of how team process influences situation assessment as an
intrinsic component of TSA. The application of the concept of our study combines elements
of the two approaches. It is close to the one by Endsley in that shared understandings are
not emphasized, however, the role of team communication in developing TSA is explicitly
considered, in line with Salas et al. [9]. In short, this experiment draws on both theories
and does not seek to discriminate between them. As a result, the findings are readily
interpretable within either approach.
2.3. Shared Displays and Team Performance
Endsley suggests that SA directly affects performance, particularly poor SA leads
to poor performance [8]. This idea is implicitly and explicitly supported throughout the

---
**[Page 4]**

Future Internet 2021, 13, 188 4 of 16
literature and applies to both teams and people. For example, Cooke et al. found a positive
correlation between TSA and team performance [17]. Endsley also proposes that the
interface design (especially the displays) will influence the SA by determining the amount
and accuracy of the information that can be acquired. Fewer articles focus on the impact
of displays on SA, while the majority comment more on training [9,10]. However, there
have been some. Of these, there are three empirical studies linking display sharing to
team performance through the influence of TSA. Unfortunately, the conclusions of such
experiments are ambiguous both for the pattern of results and for the disorders within
the experimental design. These studies will be briefly reviewed to place this study in the
context of existing work and to demonstrate the need for further experimentation to clarify
the relationship between shared displays and team performance.
Sebok used high-fidelity nuclear power plant simulations to compare teams of nuclear
power plant operators using conventional or advanced interfaces [16]. Advanced interfaces
were designed to improve TSA (along with other factors) and it was found that performance
improved when they were used compared to conventional interfaces. However, it is not
possible to say which feature of the interfaces caused this improvement. The advanced
interfaces provided integrated information and a common overview of the system (shared
display), while conventional interfaces did not. Therefore, they confused the advantages of
an ecological display [18] with the presentation of all the information to all team members.
The latter manipulation was intended to increase TSA, but due to the confusion, it is
unclear whether it was actually influential. Measures of improvements in TSA with the
advanced interface interacted with the size of the crew, further confusing the interpretation
of the results. The study also looked at the effect of various defects that occur in the plant.
They showed that the failures caused a temporary decrease in TSA, but did not investigate
the reverse, i.e., does TSA improve fault response? Still in [16], the author highlights the
relevance for survey drone fleet management applications on shared displays as a means of
improving TSA and demonstrates the importance of comparing routine performance with
that in case of off-nominal situations. Therefore, both these factors have been manipulated
in the experiment we present in this paper, and simulations have been designed accordingly.
Shared displays and TSA were explicitly examined in [11] using a task that required
two-person teams to defend a departure base from arriving planes. One team member was
responsible for classifying the aircraft (e.g., friend or foe) and the other was responsible
for appropriate action (e.g., destroying them). The TSA was manipulated by allowing
both team members to see each other’s displays (good TSA) or by allowing them to see
only their own displays (poor TSA). Unfortunately, the results of this manipulation were
unclear. Performance only deteriorated in the conditions of the non-shared display when it
was completed before the shared condition without any training on the role of the other
team members. In all other counterbalanced presentation performance orders, it was
equivalent. This model of results suggests that the difference in performance arose from
a lack of understanding of the task because so little information was presented about it
(there was no practical evidence) rather than the manipulation of the TSA. Therefore, no
definitive conclusions can be drawn from this study about the effects of TSA on team
performance. Further work should include training to ensure that the results are due to the
displays themselves, not the lack of training. The same group of researchers later conducted
another experiment with an improved design in which all teams were trained on each
other’s roles [12]. They used shared and non-shared displays again and abstract displays
that showed only the most relevant parts of the display for the other team members. In
addition, they manipulated the workload. With low workloads, there was no difference
in performance between conditions, but with higher workloads, teams with non-shared
and abstract displays performed better than those with shared displays. This is surprising,
especially the performance of teams with non-shared displays, as it suggests that TSA
is inversely related to performance, which is contrary to all predictions in the existing
literature. From this model of results, it is not clear how displays affect performance in M
Further work is needed to clarify the outcome of this experiment.

---
**[Page 5]**

Future Internet 2021, 13, 188 5 of 16
Overall, the described experiments demonstrate the relevance of display sharing for
TSA and team performance, but do not offer convincing evidence of the impact of shared
displays and TSA on team performance.
Our study was meant to further investigate this relationship by comparing shared
and non-shared displays and routine and off-nominal situations. An experimental design
will be used that offers greater experimental control and will therefore allow for more solid
conclusions to be drawn.
3. The Ground Control Station Prototype
3.1. Interface Requirement
Designing the interaction between an operator and a multi-UAS system means setting
the communication mechanisms between the human and each drone in the swarm, understanding their specificities and making the human–system relationship effective, efficient
and satisfactory for the operator, in addition to being mission-oriented and safe.
It is, therefore, necessary to consider the mental processes that are activated in the
operator during a remote mission control and to understand which dimensional, configurative, cognitive, and functional features the user interface should guarantee to be consistent
with its user’s expected behavior.
Considering the case when the user must manage multiple events, within a limited
time lapse, it is paramount that the interface keeps the operator’s workload below a given
threshold while maintaining a high level of Situational Awareness. The design of the
interface was already presented in [7], this paper intends to set out a vision on how to
design a human–machine interface for a GCS (Ground Control Station) of a fleet of drones
performing a cooperative mission of persistent surveillance.
The following is a list of requirements which may have a direct impact on the interface
design choices:
• The GCS should allow for the inclusion or removal of a UAS to/from the mission, for
efficient management of the whole swarm. In [19,20], the authors showed that a single
operator could manage a maximum of five drones, the operator’s workload being the
limiting factor as regards the maximum number of UAS to be managed by the GCS.
• The GCS should notify any event which may occur during the mission, such as
a low battery charge or a problem with video transmission from a video camera.
The interface should provide suitable visual clues as a response to those events.
For example, a visual/sound alarm could be activated when the battery reaches a
critical level.
• The GCS should provide timely information on the status of each UAS in the swarm.
The information on the interface must be carefully selected to avoid the operator’s
overload and draw his/her attention on relevant events. The standard GCS can be
used for a maximum number of five drones, and it is recommended to have a list of
drones in a control panel from which the operator can view the parameters associated
with specific drones.
• A certain level of autonomy should be implemented in the system so that the operator can rely on (semi-)automatic procedures meant to take control over an aircraft
featuring an off-nominal behavior and terminate its participation in the mission as
soon as possible. Establishing the right balance between decision-making autonomy
and human intervention in re-planning or homing actions may have serious effects on
mission success.
3.2. The Ground Control Station Interface
In this sub-section, we explain how we took into account the previous requirements
to design the remote-control interface of the persistent surveillance system. Analyzing the
user interface in Figure 1, we immediately distinguish two areas: on the left we have a
sidebar that allows the operator to interact with the application; at the top there are buttons
to create or set the mission, information on the targets, and acquisition of the mission log;

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

Future Internet 2021, 13, 188 6 of 16
while at the bottom we see the possibility of connecting to drones with LEDs indicating the
connection, to start and end the mission; most of the screen is intended for the map.
3.2. The Ground Control Station Interface 
In this sub-section, we explain how we took into account the previous requirements 
to design the remote-control interface of the persistent surveillance system. Analyzing the 
user interface in Figure 1, we immediately distinguish two areas: on the left we have a 
sidebar that allows the operator to interact with the application; at the top there are buttons to create or set the mission, information on the targets, and acquisition of the mission 
log; while at the bottom we see the possibility of connecting to drones with LEDs indicating the connection, to start and end the mission; most of the screen is intended for the 
map. 
Figure 1. The GCS interface before establishing the connection. 
Once the connection is made, the LED highlights the new connection status on the 
map, the targets are added to the mission and the drones at their starting point are indicated. In addition, at the bottom for each drone a card is created with the data related to 
the drone: 
− drone identification, 
− indication of next target, 
− coordinates of the drone, 
− battery status, 
− buttons to send the drone back to the take-off, 
− button to view the artificial horizon related to the drone. 
Once given the start mission command, one will see the drones move towards the 
second target the algorithm set. In the event the drone’s battery status is 30%, a notification 
is displayed in the upper right corner (Figure 2). If it is 10%, the drone returns to the takeoff automatically and a notification is shown in the upper right corner (Figure 3). Finally, 
Figure 1. The GCS interface before establishing the connection.
Once the connection is made, the LED highlights the new connection status on the
map, the targets are added to the mission and the drones at their starting point are indicated.
In addition, at the bottom for each drone a card is created with the data related to the drone:
− drone identification,
− indication of next target,
− coordinates of the drone,
− battery status,
− buttons to send the drone back to the take-off,
− button to view the artificial horizon related to the drone.
Once given the start mission command, one will see the drones move towards the
second target the algorithm set. In the event the drone’s battery status is 30%, a notification
is displayed in the upper right corner (Figure 2). If it is 10%, the drone returns to the
take-off automatically and a notification is shown in the upper right corner (Figure 3).
Finally, when the battery is near 0% the drone lands automatically and the interface shows
the landing position.
In Figure 4 we see how the interface provides the operator with the view of the
artificial horizon associated with any aircraft selected in the swarm, to facilitate the display
of all the information at the same time, if this component is opened in the same position,
all other information regarding the drone is displayed.

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

Future Internet 2021, 13, 188 7 of 16 Future Internet 2021, 13, x FOR PEER REVIEW 7 of 16 
when the battery is near 0% the drone lands automatically and the interface shows the 
landing position. 
Figure 2. The GCS interface during the mission execution in case the drone battery is ≤30%. 
Figure 3. The GCS interface during the mission execution in case the drone battery is ≤10%.
In Figure 4 we see how the interface provides the operator with the view of the artificial horizon associated with any aircraft selected in the swarm, to facilitate the display 
of all the information at the same time, if this component is opened in the same position, 
all other information regarding the drone is displayed. 
Figure 2. The GCS interface during the mission execution in case the drone battery is ≤30%.
Future Internet 2021, 13, x FOR PEER REVIEW 7 of 16 
when the battery is near 0% the drone lands automatically and the interface shows the 
landing position. 
Figure 2. The GCS interface during the mission execution in case the drone battery is ≤30%. 
Figure 3. The GCS interface during the mission execution in case the drone battery is ≤10%.
In Figure 4 we see how the interface provides the operator with the view of the artificial horizon associated with any aircraft selected in the swarm, to facilitate the display 
of all the information at the same time, if this component is opened in the same position, 
all other information regarding the drone is displayed. 
Figure 3. The GCS interface during the mission execution in case the drone battery is ≤10%.

---
**[Page 8]**
*(This page contains a figure/chart/image not captured in text)*

Future Internet 2021, 13, 188 8 of 16 Future Internet 2021, 13, x FOR PEER REVIEW 8 of 16 
Figure 4. The GCS interface during the execution of the mission with the visualization of the artificial horizon. 
3.3. Ground Control Station Architecture 
For the development of the project, we opted for the use of NodeJS technology, this 
allowed us to work in an innovative environment and take advantage of the flexibility 
that this technology exhibits. Indeed, a web app was created with all the pro deriving from 
it: we can in fact use it from any operating system through a browser but what interests 
us even more is the capability to use it on different devices; more specifically it has been 
designed for use on normal desktop or MultiTouch wall systems. 
The application is real-time: it receives updates on drones’ status data in real-time 
and updates the interface to allow the operator to react immediately to changes. We decided to adopt a three-tier architecture: 
• The first level consists of the data source; in the experiments, a JSON-coded scenario 
was used which contains all the initial information on the mission and how the system should behave but in real cases, the data source will be the drones that communicate through MavLink protocol; 
• The second level consists of the controllers; we need a controller that receives events 
from the drones and updates the interface and a controller that instead receives 
events from the operators and communicates them to the level below to send direct 
commands to the drone; 
• The third level takes care of the graphical interface and sends the user inputs in the 
form of events to the associated controller. 
The word “event” has often been used; this is because the NodeJS environment is 
asynchronous and allows event-driven programming. 
For the user interface of the application, we opted for the use of HTML5, Sass (compiled in CSS3), and JavaScript.; this stack of technologies allows us to develop a working 
prototype in a short time (just think the limitations posed by the development of a graphical interface in java). 
Another technology used for the project is Webpack: it is a module bundler that has 
allowed us to implement a workflow such as: speeding up development, ensuring simple 
and intelligent code organization, and optimizing the size of the app in production. 
Figure 4. The GCS interface during the execution of the mission with the visualization of the artificial horizon.
3.3. Ground Control Station Architecture
For the development of the project, we opted for the use of NodeJS technology, this
allowed us to work in an innovative environment and take advantage of the flexibility that
this technology exhibits. Indeed, a web app was created with all the pro deriving from
it: we can in fact use it from any operating system through a browser but what interests
us even more is the capability to use it on different devices; more specifically it has been
designed for use on normal desktop or MultiTouch wall systems.
The application is real-time: it receives updates on drones’ status data in real-time and
updates the interface to allow the operator to react immediately to changes. We decided to
adopt a three-tier architecture:
• The first level consists of the data source; in the experiments, a JSON-coded scenario
was used which contains all the initial information on the mission and how the system
should behave but in real cases, the data source will be the drones that communicate
through MavLink protocol;
• The second level consists of the controllers; we need a controller that receives events
from the drones and updates the interface and a controller that instead receives
events from the operators and communicates them to the level below to send direct
commands to the drone;
• The third level takes care of the graphical interface and sends the user inputs in the
form of events to the associated controller.
The word “event” has often been used; this is because the NodeJS environment is
asynchronous and allows event-driven programming.
For the user interface of the application, we opted for the use of HTML5, Sass (compiled in CSS3), and JavaScript.; this stack of technologies allows us to develop a working
prototype in a short time (just think the limitations posed by the development of a graphical
interface in java).
Another technology used for the project is Webpack: it is a module bundler that has
allowed us to implement a workflow such as: speeding up development, ensuring simple
and intelligent code organization, and optimizing the size of the app in production.

---
**[Page 9]**

Future Internet 2021, 13, 188 9 of 16
4. The Study
The study presents uses of the interface to simulate a scenario in which detection of
an area takes place by five drones and a transmission of relevant information to the ground
control station where a team of operators is present. The aim of this study is to assess the
effects of TSA on team performance.
A team member controls the drones on the map. The second team member checks the
drone’s battery level.
If the drone is discharged below 30%, it is indicated on the display with a notification on the map “Drone almost discharged”. If the drone has a 10% battery status the
drone is immediately homing. This is indicated on the display with a “Drone return to
takeOff” notification.
This task is interdependent as the higher the drone battery rate, the higher the success
rate of the mission.
The drone batteries are limited and require management during the mission.
Two independent variables were considered, referring to display sharing and event
occurrence, respectively. In the “Shared” condition, the teams had the screen shared on the
MultiTouch wall so that both team members could see the interface which represented the
factors that vary in the simulation for their specific task. In the “Non-shared” condition,
the teams had screens that were not shared and had to see all the factors of the simulation,
without distinction of task.
In the “No event” condition, the mission occurred normally. An unexpected event
occurred on the mission in the “Event” condition. In the simulation scenarios that signaled
an unexpected event, this is the drone battery without load.
During this activity, the communication of the team members was also evaluated.
Salas et al. (1995) proposed that group processes are related to TSA. For example, team
members can exchange information to develop TSA. To test this idea, team communication
was analyzed. Specifically, the frequency with which team members asked questions
about the status of the mission was measured. The questions were speculated to provide a
good indication of the extent to which team members tried to improve their SA through
communication with the team.
The following hypotheses were derived. In any case, the performance was measured
by the success of the mission and of the frequency of communication. Endsley (1995)
predicts that poor AS will lead to poor performance, and Cooke et al. (2001) provides an
empirical demonstration of this. A shared view is expected to enhance TSA by providing all
team members with direct access to the complete plant status. Therefore, it is expected that:
Hypothesis 1: Operator’s performance are higher in the “Shared” condition than in the “Nonshared” one:
Hypothesis 1.1: In normal conditions, the performance is higher in the shared setting compared
to the non-shared setting.
Since, Sebok observes that SA is reduced when unexpected events occur (see [16]), we
are interested in exploring which setting can better deal with it.
Hypothesis 1.2: In case of unexpected events, the performance deteriorates more in the non-shared
setting compared to the shared setting.
4.1. Method
4.1.1. Participants
A total of 40 students from the University of Salerno were recruited to participate in
this experiment. There were 25 male and 15 female participants. Their average age was
23.7 years. They were all volunteers and were UAS drivers at amateur level.

---
**[Page 10]**

Future Internet 2021, 13, 188 10 of 16
4.1.2. Design
A between-subject design experiment was performed. We considered two independent variables that are respectively: the display setting, which can be “Shared” or
“Non-Shared”, and the presence of unexpected events, “No Event” and “Event”.
The dependent variables express the operator’s performance. They are the situation
awareness (SA), the communication among the team members (CT) and the number of
drones back home (DBH).
SA is measured through the situation awareness global assessment technique (SAGAT).
SAGAT is a tool that measures situation awareness in terms of three levels: perception,
comprehension, and projection. For each level of situation awareness, SAGAT poses a number
of questions whereby only one of the possible answers is correct.
SAGAT scores provide a detailed collection of information that can directly be compared to reality. Hence, SAGAT is a more objective method that is not dependent on a
subjective evaluation because there is one right answer that is defined from the outset.
The SAGAT questionnaire is filled out while the simulation is at rest. In this way,
participants can only report what they really perceived and remembered from the last seen
situation. The questions refer to objects or events from the just presented situation [19].
The communication among the team members was assessed during the activity as
it is also related to TSA [9]. The team members can exchange information to develop
TSA. To test this idea, the team’s communication was analyzed in [9]. In particular, the
frequency with which team members asked questions (NQ) about the status of the mission
was measured. The authors observed that the questions provided a good indication of the
extent to which team members tried to improve their SA through communication with
the team.
During the mission, the lack of situational awareness can cause the drones to be
lost. Then, the number of drones returning home (DBH) is an additional parameter that
measures the operator’s performance.
4.1.3. Tasks
The task scenario and experiment setting were designed collaborating with the Italian
Aerospace Research Center experts; the operators and the system share responsibility
following the liability allocation [21]. In this case the system informs operators about the
drone status while the operator is in charge to decide when the drone must land or go
back home, except for the minimum battery level in which the system controls the drone
landing automatically. Figure 5 shows two users experimenting with the “Shared” setting.
The goal of the tasks is to correctly monitor the situation during drones’ exploration
mission. Two operators sit in front of the system in the “Shared” or “Non-shared” setting.
A team member controls the drones on the map. The second team member checks the
drone’s battery level.
If the drone is discharged below 30%, a message is displayed on the map. If the drone
has a 10% battery status the drone immediately tries to go back home.
The task is run twice: once in a normal situation and once with the unexpected event
of the battery. The starting task is selected randomly.
During the task an unexpected event is triggered. A drone’s battery suddenly gets
down to 30% causing troubles to the team.
4.1.4. Procedure
Before completing the experimental tests, the operation of the simulated mission
was explained to each participant. Participants completed a practical test during which
they could ask questions about the experiment and the system to make sure they fully
understood it. They were then divided into two groups. The teams were then randomly
assigned to “Shared” or “Non-shared” conditions. Within the shared view group, they
were randomly assigned to the specific control role. The participants were not advised that
this could happen. In a simulation, a drone was discharged, causing a low battery event

---
**[Page 11]**
*(This page contains a figure/chart/image not captured in text)*

Future Internet 2021, 13, 188 11 of 16
(>30%). In the second error test, the battery indicator signaled a low battery event less than
30% but larger than 10%.
Future Internet 2021, 13, x FOR PEER REVIEW 11 of 16 
Figure 5. Two users operating in the “Shared” setting during the experiment. 
4.1.4. Procedure 
Before completing the experimental tests, the operation of the simulated mission was 
explained to each participant. Participants completed a practical test during which they 
could ask questions about the experiment and the system to make sure they fully understood it. They were then divided into two groups. The teams were then randomly assigned 
to “Shared” or “Non-shared” conditions. Within the shared view group, they were randomly assigned to the specific control role. The participants were not advised that this 
could happen. In a simulation, a drone was discharged, causing a low battery event 
(>30%). In the second error test, the battery indicator signaled a low battery event less than 
30% but larger than 10%. 
The order of these simulations was counterbalanced between the teams. Each simulation lasted 4 min. During this period all their communications were recorded for subsequent analysis. After 2 min a facilitator asked the participants the questions coming from 
the SAGAT questionnaire. The questionnaire consists of three items. Each of the three 
items belongs to one of the three levels of SA: perception, understanding and projection. 
Participants were free to respond openly. The right answers were defined from the start 
and were rated as correct or incorrect based on industry expert suggestions. Since each 
participant received two questionnaires made of three questions, respectively, in the two 
settings of the experiment, it was possible to obtain a maximum score of 6 correct answers 
in total. A summary of the questions is provided in the Table 1. 
Table 1. Questions asked during the test to assess operator situational awareness. 
# Question 
Q1. How many UAVs are you controlling? 
Q2. What is the altitude and battery level of each of the UAVs? 
Q3. What is the next UAV target on the screen?
4.2. Results 
Since in our scenario the performance consists of SA, CT and DBH, we formulate the 
following sub-hypotheses: 
Figure 5. Two users operating in the “Shared” setting during the experiment.
The order of these simulations was counterbalanced between the teams. Each simulation lasted 4 min. During this period all their communications were recorded for
subsequent analysis. After 2 min a facilitator asked the participants the questions coming
from the SAGAT questionnaire. The questionnaire consists of three items. Each of the three
items belongs to one of the three levels of SA: perception, understanding and projection.
Participants were free to respond openly. The right answers were defined from the start
and were rated as correct or incorrect based on industry expert suggestions. Since each
participant received two questionnaires made of three questions, respectively, in the two
settings of the experiment, it was possible to obtain a maximum score of 6 correct answers
in total. A summary of the questions is provided in the Table 1.
Table 1. Questions asked during the test to assess operator situational awareness.
# Question
Q1. How many UAVs are you controlling?
Q2. What is the altitude and battery level of each of the UAVs?
Q3. What is the next UAV target on the screen?
4.2. Results
Since in our scenario the performance consists of SA, CT and DBH, we formulate the
following sub-hypotheses:
Sub-Hypothesis 1.1.1: In normal conditions, SA is higher in the shared setting compared to the
non-shared setting.
Sub-Hypothesis 1.2.1: In case of unexpected events, SA deteriorates more in the non-shared
setting compared to the shared setting.
Sub-Hypothesis 1.1.2: In normal conditions, DBH is larger in the shared setting compared to the
non-shared setting.

---
**[Page 12]**

Future Internet 2021, 13, 188 12 of 16
Sub-Hypothesis 1.2.2: In case of unexpected events, DBH deteriorates more in the non-shared
setting compared to the shared setting.
Sub-Hypothesis 1.1.3: In normal conditions, NQ is smaller in the shared setting compared to the
non-shared setting.
Sub-Hypothesis 1.2.3: In case of unexpected events, NQ increases more in the non-shared setting
compared to the shared setting.
As for SA, users answered three questions while performing the two tasks. The
number of correct answers are reported in Table 2 next to the relative p-value calculated
by performing a non-parametric Chi-squared 2-by-2 test. This is to statistically analyze
the frequency of correct and incorrect answers for each group. The test shows that there
are no significant differences between the correct response frequencies among the two
groups, except for Q3 which is related to the operators’ prediction factor. Therefore SH1.1.1
is rejected and we can state that there is no significant difference in situational awareness
between the two settings when there are no unexpected events. On the other hand, SH1.1.2
is supported by data, so we can affirm that when an unexpected event occurs, the predictive
ability of the operators deteriorates, particularly in the “Non-shared” setting.
Table 2. Number of correct answers per question as measured with SAGAT for each setting.
Correct Answers in
Shared Setting Group
Correct Answers in
Non-Shared Setting Group p-Value
No Event task
Q1 20 20 /
Q2 18 16 0.376
Q3 17 13 0.144
Event task
Q1 19 15 0.077
Q2 18 14 0.114
Q3 18 10 0.003
The number of drones that potentially can return home at the end of the mission can vary between 0 and 5. Table 4
shows for each task how many drones each pair of operators managed to bring home.
The Mann–Whitney parametric test analysis was performed. It is adequate to compare
two datasets collected from two different groups. The analysis produced a p-value of 0.271
in the task without an unexpected event and 0.045 in the other case. This indicates that
there are no particular differences in the drones returned to base in the first task, rejecting
SH1.1.2, while there is statistical evidence in the second case, confirming SH1.2.2.
Finally, Table 3 shows the number of questions about the mission status asked between
the pairs of operators during each task. For each task, the means of the two groups were
compared by applying a two tailed independent-samples t-test. For the “No event” task,
the p-value is 0.268, thus rejecting hypothesis SH1.1.3. For the second task the p-value is
0.002 showing that when an unexpected event occurs, the number of questions increases in
the “Non-Shared“ setting.

---
**[Page 13]**

Future Internet 2021, 13, 188 13 of 16
Table 3. The number of questions among the team members (NQ) about the status of the mission.
Number of Questions in
Shared Setting Group
Number of Questions in
Non-Shared Setting Group
No Event task
Team 1 3 2
Team 2 2 3
Team 3 2 2
Team 4 1 1
Team 5 2 4
Team 6 1 2
Team 7 2 2
Team 8 2 1
Team 9 1 2
Team 10 1 2
Event task
Team 1 4 5
Team 2 3 6
Team 3 5 4
Team 4 4 6
Team 5 5 7
Team 6 4 6
Team 7 4 5
Team 8 3 6
Team 9 5 4
Team 10 4 7
4.3. Discussion and Implication
The purpose of this study is to carry out predictions derived from the situation awareness of the team operating the ground control station that sharing displays between team
members would improve team performance. The results show that the shared displays
do not universally improve team performance, but they help to maintain performance in
off-nominal situations. These results are discussed below.
There was no overall visualization effect on team performance. Shared displays
were predicted to cause better TSA than non-shared displays and thus lead to better team
performance by controlling what information team members could easily access. The
analysis of team communication clarifies the picture. Teams with unshared displays asked
many more questions about the simulation. This implies that they integrated the limited
information presented to them with the information aroused by the other team member. It
is entirely possible that this allowed them to develop TSAs comparable to teams in shared
conditions. This explanation of the results is interesting in that it supports the conjecture of
Salas et al. [9] that states that the group process is an intrinsic part of situation assessment
and development of the TSA.
Unexpected events in the simulation reduced performance, showing that they had
a measurable impact on the activity. This leads to the second interesting discovery, that
performance deteriorated significantly when unforeseen events occurred in the “Nonshared” setting, more than in the “Shared” setting. The frequency of mission status
questions demonstrated a similar interaction, implying that the team process offset the
negative impact on TSA caused by the unshared view and an unexpected event.

---
**[Page 14]**

Future Internet 2021, 13, 188 14 of 16
Table 4. The number of drones back home (DBH) at the end of each task.
Number of Drones Back Home in
Shared Setting Group
Number of Drones Back Home in
Non-Shared Setting Group
No Event task
Team 1 5 4
Team 2 5 5
Team 3 5 5
Team 4 5 4
Team 5 5 5
Team 6 5 4
Team 7 4 4
Team 8 5 5
Team 9 5 5
Team 10 5 5
Event task
Team 1 4 3
Team 2 3 3
Team 3 3 2
Team 4 4 3
Team 5 3 3
Team 6 3 2
Team 7 4 1
Team 8 3 4
Team 9 4 3
Team 10 3 2
The implication of these results is that shared displays are particularly useful for
performance in off-nominal situations. This experiment does not reveal how this effect
occurs. It is possible that with shared displays there are more people who can see the status
of the mission and therefore they are more likely to quickly detect an unexpected event.
It may be that with a good TSA they are more able to get around the problem once it has
been detected.
Although the “Shared” setting demonstrated generally more advantages in situations
involving sudden events, and it does not generate difficulties to operators in normal situations, it also reveals the need to have physical spaces enough large to allow collaboration
among operators. Moreover, the experiment studied only the collaboration among two operators while in the wild there is also the possibility to have several operators collaborating
at the same time. Thus, more investigation is needed in this sense.
5. Conclusions
In the paper, we analyzed relevant human factor implications for remote ground
control of multiple unmanned aerial systems.
During the stages of design, the prototype was subject to supervision by the ground
operators involved since the initial contextual inquiry. They actively collaborated with us
in the definition and specification of the interface requirements. The formative evaluation
results obtained so far are considered encouraging. The sensorial isolation of the operator
and the problems related to spatial disorientation of existing multi-UAS systems are
likely to be solved by using a single virtual screen that provides the operator with all the

---
**[Page 15]**

Future Internet 2021, 13, 188 15 of 16
information regarding the mission and all the UAS involved while allowing the horizon
view of any single aircraft.
In conclusion, this study provided qualified support for the prediction that shared
displays would lead to better team performance than non-shared displays.
In particular, the advantages of display sharing arise in off-nominal situations, for
example when an unexpected event occurs but not during routine operation.
The study also suggests the important role of team process (communication) in maintaining TSA. However, the results indicate that the team process cannot overcome the poor
TSA derived from non-shared displays in all situations. In this task, the team process only
seemed to provide sufficient compensation in routine situations. As future work, we plan to
investigate the problem in the context of more complex scenarios. New experiments could
concern wider areas to be monitored, heterogeneous drones characterized by different
performance and payload, and operators located on the territory.
Author Contributions: M.D.G., M.R., M.S., G.V. and A.V. contributed to the design and implementation of the research, to the analysis of the results and to the writing of the manuscript. All authors
have read and agreed to the published version of the manuscript.
Funding: This research was funded by MIUR, PRIN 2017 grant number 2017JMHK4F_004.
Institutional Review Board Statement: All procedures performed in studies involving human
participants were in accordance with the ethical standards of the institutional and/or national
research committee and with the 1964 Helsinki declaration and its later amendments or comparable
ethical standards.
Informed Consent Statement: Informed consent was obtained from all subjects involved in the study.
Data Availability Statement: Not applicable.
Acknowledgments: The authors thank the student Salvatore Fasano for his contribution to the
development of the interface.
Conflicts of Interest: The authors declare no conflict of interest.
References
1. Mohammed, F.; Idries, A.; Mohamed, N.; Al-Jaroodi, J.; Jawhar, I. UAVs for smart cities: Opportunities and challenges. In
Proceedings of the IEEE International Conference on Unmanned Aircraft Systems (ICUAS), Orlando, FL, USA, 27–30 May 2014;
pp. 267–273.
2. Cooke, N.J. Human Factors of Remotely Operated Vehicles. In Proceedings of the Human Factors and Ergonomics Society Annual
Meeting, San Francisco, CA, USA, 16–20 October 2006; Volume 50, pp. 166–169.
3. McCarley, J.S.; Wickens, C.D. Human Factors Concern in UAV Flight; University of Illinois at Urbana-Champaign Institute of
Aviation, Aviation Human Factors Division: Champaign, IL, USA, 2004.
4. Barr, L.C.; Newman, R.; Ancel, E.; Belcastro, C.M.; Foster, J.V.; Evans, J.; Klyde, D.H. Preliminary Risk Assessment for Small
Unmanned Aircraft Systems. In Proceedings of the 17th AIAA Aviation Technology, Integration, and Operations Conference,
Denver, CO, USA, 5–9 June 2017; p. 3272.
5. Cak, S.; Say, B.; Misirlisoy, M. Effects of working memory, attention, and expertise on pilots’ situation awareness. Cogn. Technol.
Work 2020, 22, 85–94. [CrossRef]
6. Endlsey, M.R. Theoretical underpinnings of situation awareness: A critical review. In Situation Awareness Analysis and Measurement;
Endlsey, M.R., Garland, D.J., Eds.; LEA: Mahwah, NJ, USA, 2000; pp. 3–32.
7. Vicente, K.J. Ecological interface design: Progress and challenges. Hum. Factors 2002, 44, 62–78. [CrossRef] [PubMed]
8. Endsley, M.R. Toward a theory of situation awareness in dynamic systems. Hum. Factors 1995, 37, 32–64. [CrossRef]
9. Salas, E.; Prince, C.; Baker, D.P.; Shrestha, L. Situation awareness in team performance: Implications for measurement and training.
Hum. Factors 1995, 37, 123–136. [CrossRef]
10. Stout, R.J.; Cannon-Bowers, J.A.; Salas, E. The role of shared mental models in developing team situational awareness: Implications
for training. Train. Res. J. 1996, 2, 85–116.
11. Bolstad, C.A.; Endsley, M.R. Shared mental models and shared displays: An empirical evaluation of team performance. In Proceedings of the Human Factors and Ergonomics Society 43rd Annual Meeting, Houston, TX, USA, 27 September–1 October 1999.
12. Bolstad, C.A.; Endsley, M.R. The effect of task load and shared displays on team situation awareness. In Proceedings of the
Human Factors and Ergonomics Society 44th Annual Meeting, Los Angeles, CA, USA, 30 July–4 August 2000. pp. 189–192.
13. Sabikan, S.; Nawawi, S.W. Open-source project (OSPs) platform for outdoor quadcopter. J. Adv. Res. Des. 2011, 24, 13–27.

---
**[Page 16]**

Future Internet 2021, 13, 188 16 of 16
14. Zhou, Y.; Hou, J.; Gong, Y. Research and Application of Human-computer Interaction Technology based on Voice Control in
Ground Control Station of UAV. In Proceedings of the 2020 IEEE 6th International Conference on Computer and Communications
(ICCC), Chengdu, China, 11–14 December 2020; pp. 1257–1262.
15. Qian, G.M.; Pebrianti, D.; Chun, Y.W.; Hao, Y.H.; Bayuaji, L. Waypoint navigation of quadrotor MAV. In Proceedings of the 2017
7th IEEE International Conference on System Engineering and Technology (ICSET), Shah Alam, Malaysia, 2–3 October 2017;
pp. 38–42.
16. Cooke, N.J.; Salas, E.; Cannon-Bowers, J.A.; Stout, R.J. Measuring team knowledge. Hum. Factors 2000, 42, 151–173. [CrossRef]
[PubMed]
17. Cooke, N.J.; Kiekel, P.A.; Helm, E.E. Measuring team knowledge during skill acquisition of a complex task. Int. J. Cogn. Ergon.
2001, 5, 297–315. [CrossRef]
18. Sebok, A. Team performance in process control: Influences of interface design and staffing levels. Ergonomics 2020, 43, 1210–1236.
[CrossRef] [PubMed]
19. Dixon, S.R.; Wickens, C.D.; Chang, D. Mission Control of Multiple Unmanned Aerial Vehicles: A Workload Analysis. Hum.
Factors 2005, 47, 479–487. [CrossRef] [PubMed]
20. Luongo, S.; Di Gregorio, M.; Vitiello, G.; Vozella, A. Human Machine Interface Issues for Drone Fleet Management. In Proceedings
of the International Conference on Human Systems Engineering and Design: Future Trends and Applications, Reims, France,
25–27 October 2018; pp. 791–796.
21. Friedrich, M.; Lieb, J. A Novel Human Machine Interface to Support Supervision and Guidance of Multiple Highly Automated Unmanned Aircraft. In Proceedings of the 2019 IEEE/AIAA 38th Digital Avionics Systems Conference (DASC), San Diego, CA, USA,
8–12 September 2019; pp. 1–7.