# Gale 2018 Playbook for CASAS

*Source file: Gale_2018_Playbook_for_CASAS.pdf — 13 pages*


---
**[Page 1]**

Playbook for UAS: UX of Goal-Oriented
Planning & Execution
Jack Gale1, John Karasinski2, Steve Hillenius2
1 San Jose State University Research Foundation, San Jose, CA 95112 2 NASA Ames Research Center, Mountain View, CA 94035
jack.w.gale@nasa.gov
Abstract. We are evaluating Playbook for CASAS (Connected Autonomous 
Smart Aerospace Systems), a tool designed to aid first responders in disaster relief efforts. We are adapting an existing tool, Playbook, to support a future unmanned aircraft system (UAS) swarm demonstration. Playbook for CASAS will 
be used to plan, edit, and monitor simulated UAS swarms, and we are interested 
in evaluating the user experience of this prototype as well as developing recommendations for future UAS interfaces. Allocation of roles and responsibilities 
between human-automation systems is key to promoting productive cooperation 
between users and automation. Future interfaces, however, must allow for adaptive management of the swarm not a constant split in human-automation control. Our early research indicates that when a single pilot is controlling swarms 
of robotic agents, such as UAS or ground rovers, operators require a higher 
level, goal-based interface with usability at its core. Along with that high-level 
control, users can leverage sensors within the swarm to be notified when lower 
level actions must be taken by the pilot. First responders working in disaster relief efforts require a high level of situational awareness (SA) and precise control 
at key moments within a mission. This balance in operator workload paired 
with SA can lead to improved safety and mission outcomes. Our research below 
outlines leverage points as well as the balance between human involvement and 
autonomy in UAS interfaces.
Keywords: Swarms, UAV, UAS, Autonomy, Engineering Psychology, 
Cognitive Ergonomics, User Experience, Human Centered Design, HCI.
1 Introduction
1.1 Future UAS
The field of unmanned aircraft systems (UAS) have seen tremendous growth over the 
past few decades. Recent advances in hardware have reduced the size and cost of 
UAS, spurring greater research interest in both government and private industry. The 
resulting increased availability in this technology has led to a need to provide untrained operators (i.e., operators without explicit pilot training) the ability to monitor 
and command both individual and swarms of UAS. As the number of UAS in a 
swarm increases, however, it is important to provide an operator with a user interface 
that maximizes gains in situational awareness (SA) while simultaneously minimizing

---
**[Page 2]**

the increases in workload associated with managing the additional vehicles. We have 
designed and evaluated a novel interface for UAS swarm management which requires 
minimal-to-no training for use by first responders for disaster relief. Using a humancentered design usability study, we have evaluated this interface with first responders, 
analyzed their feedback, and synthesized recommendations for similar swarm interfaces.
1.2 Situational Awareness
UAS have been embraced by emergency and disaster relief communities for their use 
in situations where it is either impractical, impossible, or extremely dangerous to deploy first responders. These vehicles can monitor emergency areas, deliver supplies, 
and search for missing persons, often faster than would be possible with humans and 
with no risk to their operator. Perhaps more importantly, these vehicles can be used in 
tandem with first responders already on the ground, providing greater situational 
awareness and safety in emergency situations. This increase in situational awareness 
allows first responders to more effectively complete their jobs.
Endsley defines situational awareness as "the perception of elements in the environment within a volume of time and space, the comprehension of their meaning, and the 
projection of their status in the near future" [1]. While UAS can provide important SA 
to first responders on the ground, this should not be a purely unidirectional information flow. The information first responders glean on the ground can be used to redefine the goals of the assisting aircraft. Some tasks, such as modifying the flight 
plans of UAS, however, requires that first responders also take on the role of air traffic controllers (ATCs). Endsley specifically calls out the "taxing" role of air traffic 
controllers when she notes that controllers "must maintain up-to-date assessments of 
the rapidly changing locations of aircraft...and their projected locations relative to 
each other" [1]. This requirement cannot come without some increase in workload, 
but a well-designed interface should minimize this impact. The ability to increase situational awareness through the use of live video and other sensor feeds can provide 
ground workers the knowledge they need to remain safe in highly dynamic scenarios.
1.3 Goal-Oriented Planning 
In an ideal scenario, first responders, using the contextual information they’ve gained 
on the ground, should be able to control the UAS by pointing them to regions of interest and commanding them to accomplish goals. First responders can use goal-oriented
planning in order to minimize the impact of this additional role as ATC. Goal oriented 
planning can be defined as “the process of breaking down complicated goals into simpler, more manageable sub-goals” [2]. As an example, a first responder may have the 
goal to search a large fire zone for survivors. This goal can be divided into sub-goals 
by creating a trajectory of several waypoints which cover the entire fire zone. The 
goal is then completed when the swarm has searched each of the waypoints. In this 
scenario, the immediate benefit to the first responder is that they need only assign the 
system to “search the fire zone” instead of determining and then assigning a complete 
set of waypoints for the swarm to search.

---
**[Page 3]**

Goal oriented planning also simplifies the planning process when a first responder has 
many different goals that need to be completed. As an example, a first responder 
needs to plan out three goals: “search the fire zone”, “deliver a package”, and “monitor the waypoint”. While each of these goals may contain many sub-goals, the first responder only needs to consider the functional aspects of the goals, such as:
• How long will the goal take to complete?
• How many UAS are required to complete the goal? and
• Which goal has the highest priority?
The first responder can use the answers to these questions to create their plan, without 
needing to worry about which aircraft will fly to which waypoint at any given time. 
This allows the first responder to more effectively manage the swarm to respond to 
current priorities, without needing to concern themselves with the finer details of 
ATC. This goal level planning has been used by several researchers, with varying 
numbers of UAS, to result in reduced simulated mission time [3] [4].
2 Interface
2.1 Playbook
Our prototype interface is adapted from the Playbook tool. Playbook is a mobile webbased schedule planning tool currently used in operation by NASA spaceflight analog
missions as well as a platform to research crew autonomy. Originally developed as a 
plan viewer, it was extended significantly in 2014 to become a tool used to enable 
crew autonomy. These features and capabilities are necessary as we prepare in the 
spaceflight domain for future deep space missions, where traditional mission control 
tasks will need to shift to the crew. Shifting these tasks is challenging, as the current 
roles of mission control are handled by teams of people (100+ in total), where the 
number of crew onboard may be on the order of 4-6 [5][6].
The use of the horizontal timeline differs significantly from most consumer products 
where a vertical timeline is used, primarily because of user familiarity with historical 
mission plans. Apollo mission plans were produced using a vertical timeline layout, 
but Shuttle and International Space Station mission plans used a horizontal layout
[7][8]. As our main target users for the Playbook interface and earlier tools were flight 
controllers and astronauts who were already accustomed to horizontal mission plan 
timeline layouts, this was used as a basis for retaining their familiarity. Over the 
years, however, Playbook team has looked at how the same information would be displayed in a vertical layout. Although we have not done a formal study on the differences, our initial impressions, as we tried to represent the high-density space station 
or Mars rover plans, is that the readability and flexibility break down in such a scenario [9]. The vertical time layouts tended to rely on vertical text which is difficult to 
read. When data plots such as power usage or altitude, are displayed on a vertical 
timeline they become difficult to read and to compare with the timeline. The other 
main consideration in favor of a horizontal timeline is the heavy use of hierarchy in a 
mission plan. Each element on the timeline may contain several additional elements

---
**[Page 4]**

(similar to Gantt style charts) that may represent individual activities inside a larger 
group, or smaller activities that are contained in a larger activity such as on a rover or 
orbiter mission plan. Three or four levels of hierarchy are not uncommon in these 
dense mission plans. Since the timeline itself is horizontal, the hierarchy can be displayed vertically, allowing for a natural mapping: higher abstraction are higher vertically compared to lower-level activities. These relationships also map to users familiar with Gantt charts.
2.2 Adapting to UAS
The advantages of providing astronauts with mobile web-based planning tools have 
benefits and applications that translate over to the UAS space. To support crew autonomy, Playbook was designed with an emphasis to provide lightweight plan editing 
that allows astronauts to quickly and easily manipulate their mission plan while not 
taking up time from execution of their spaceflight tasks for the day. Key design goals 
to enable this were the emphasis on mobile interfaces that allow astronauts to perform 
mission plan changes without being at a designated computer or console. Emphasis on 
"walk up and use" usability, and the ability for multiple astronauts to collaboratively 
work on their mission plan simultaneously was key [5]. These design goals map well 
to the UAS domain for our use case of first responders arriving at a disaster area. Mobility is key in this UAS context, as our target users are in the field and are not situated at a dedicated console. The target users are not expert pilots and are under similar 
operational pressures of astronauts, so walk up and use plays a large role in the design 
and ability to quickly make plan changes. Collaboration allows multiple users to aid 
in planning, rather than relying on a single user to be designated or otherwise able to 
accomplish the task at a given time. In addition to the mission planning design elements, the application to the UAS domain required us to integrate time domain planning (used in the Playbook spaceflight mission planning tool) with geospatial planning, which is traditionally seen in many UAS style interfaces. This is represented in 
the UI by the timeline portion of the interface side by side with the geospatial interface. Depending on what task the user is working on, the timeline or geospatial portion of the interface will grow to maximize the screen real estate, while the non-active 
portion of the interface will shrink, but not disappear, to allow the user to see the relationship of their planning actions in both the time and geospatial planning domains.
2.3 Interface Elements
Our prototype interface included three main interactive areas which allow users to execute tasks (see Fig. 1). The top of our interface includes a timeline which is very 
similar to Playbook, but, replaces each crew member row with a single UAS. Each 
UAS has its own row, followed by a timeline of that UAS future goals and waypoints.
Each hour is labeled with a vertical line so users have a sense of when a waypoint or 
goal will be met or completed.

---
**[Page 5]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 1. Playbook for CASAS prototype interface showing the timeline (Top), geospatial view 
(Center), and stream view (Right). This is showing alternate flight trajectory options, waypoints, and temporary flight restriction (TFR) volumes.
The second area is an overhead or geospatial view, which presents the most radical 
change to the existing Playbook interface, and much of the focus of our usability studies. This area allows a user to zoom in and out of an area to keep an eye on all UAS, 
as well as to view trajectories, waypoints, and flight restriction volumes. Users can 
tap, pinch to zoom, and pan using traditional gestures, although this functionality was 
not included in our initial prototypes. By leveraging interactions from other widely 
used products, we can reduce onboarding and training time, especially with the user 
group of untrained operators.
The last area is the “stream view”. In Playbook, the stream view allows users to glean 
more detailed information, such as temporal information, constraints, and descriptions 
of each activity. In this prototype, the stream view is used similarly for waypoints.
Some additional functionality was also implemented to this area, which makes it, 
along with the overhead view, the two primary areas of interaction. The stream view 
appears on the right side of the screen, and slides in and out as needed. It was designed to be visually distinct from the rest of the interface in order to prompt the user 
to make decisions at key moments within the mission. 
2.4 Early Iterations
Early paper prototypes were employed to better understand key elements, button sizing, placement, and to provide a starting point for discussion with our target users.

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

There are often difficulties early in the design process when it's unclear what functionality should be included or removed after initial exploratory research. A paper 
prototype, which in this case was simply a cardboard cutout of an iPad with paper 
taped on top, is useful in the early stages of design (see Fig. 2). Paper prototypes allow quick understanding of the hierarchy of elements and the need for certain actions 
to be added or removed from the interface. One example of this occurred early in this 
research with the first version of this prototype. We were interested in displaying 
UAS prognostics to the user and had the idea to show these metrics for each UAS in a 
card format. This technique is commonly used in interfaces for single UAS pilots. 
Once we built this into a paper prototype, however, we quickly realized that allocating 
prognostics space for each drone was unnecessary and consumed too much space on 
the iPad. The paper prototype allowed us to recognize those areas that needed to be 
autonomous, and what information might be unnecessary when guiding multiple 
UAS. This prognostics card idea works well for individual aircraft management; however, that information is much less relevant to a first responder in the field when guiding a swarm. 
Fig. 2. Early paper prototype of a swarm interface. This version has more controls which we 
later removed like velocity and drone allocation sliders.

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

3 Methodology
3.1 Research Strategy 
For this study, our team built an interactive prototype that was presented to subjects 
with and without training in UAS management. We then describe a "search and recover" mission using a swarm of aircraft that they must control. We asked each participant to complete tasks which include starting the mission, selecting waypoints, and 
selecting alternate flight trajectories developed by an auto resolver (AR) algorithm. 
An auto-resolver is defined as a "trajectory-based conflict resolution algorithm that 
provides efficient flight path changes to solve medium term conflicts." [10] The autoresolver used for our upcoming flight demonstration will produce multiple flight trajectories autonomously and use our interface to present these trajectory options to a 
user. Along with evaluating trajectory selections, we also sought to better understand 
the role of first responders in the field. To accomplish this, we completed several 
rounds of early flight tests with three UAS at the NUARC (NASA UAS Autonomy 
Research Complex), (see Fig. 3).
Fig. 3. Initial testing at NASA Ames Research Center in Mountain View, CA. Three drones 
completing routes planned through the Playbook interface. 
To assist us in our research, we recruited seven subjects made up from members of 
the Ames Disaster Assistance Rescue Team (DART) and UAS researchers from the 
Human Systems Integration Division at Ames. Our strategy was to evaluate our prototype interface and better understand our users through the analysis of qualitative data 
from our usability studies. After testing with subjects, we separated data into three

---
**[Page 8]**

categories: our observations, subjective thoughts from the users, and direct quotes. At 
the end of this first round of testing, we developed key insights and recommendations 
that both inform and evaluate the design of our prototype as well as future unmanned 
aircraft systems. Our team's primary method of research is a standard human-centered 
design iterative evaluation loop that allows for rapid prototyping of interfaces, thereby 
allowing for multiple rounds of usability testing.
3.2 Testing Protocol 
Future UAS studies tailored for users with little-to-no experience in UAS management require building a usability protocol with onboard training. Clear usability protocols are essential to familiarize users with UAS controls and complex disaster relief 
scenarios. Our usability protocol consisted of defined roles for the subjects, an outline 
of timing and schedule for testing, an introduction, scenario, tasks for the user, completion criteria, and follow up questions. This structured protocol was created to ensure that the data resulting from these studies was as reliable as possible once we began synthesis of our data. We asked subjects to complete a series of tasks that were 
framed as messages from a ground control station. During their execution of the task, 
the subject was asked to think-aloud and try to complete the task on our iPad prototype. A think-aloud study asks the user to verbalize each action they take as well as 
their thinking while completing tasks [11]. This method allows testers to more easily 
identify and record pain points or moments of confusion, as well as spot differences in 
their actions versus their intent. The rationale behind conducting a think-aloud usability study is not only to assist testers in highlighting moments of confusion but also 
times at which the interface felt most clear to the user. Given the increase in use and 
availability of autonomous systems, NASA has stated an interest in building requirements for testing human-autonomy interfaces and creating verifiable testing protocols
[12]. 
3.3 User Group and Goals
As noted above, this research was conducted with seven volunteer subjects which 
consisted of Ames Disaster Assistance Rescue Team (DART) members and UAS researchers from the Human Systems Integration Division at Ames. DART is a federal 
emergency response and recovery team that can be deployed in support of disaster relief efforts. Previous deployments include the Loma Prieta Earthquake, Oakland Firestorm, Oklahoma City Bombing, and the World Trade Center terrorist attack [13]. 
Many of our subjects are also members of the CA Task Force 3, a FEMA Urban 
Search and Rescue Task Force which has separate deployments and training exercises 
also related to disaster relief. The goal of this research was to gain insight into the human's role in an autonomous UAS traffic management (UTM) systems. We are investigating a network of ground control systems which together produce flight path trajectories that ultimately display to users on an iPad. Future interfaces must allow for 
sufficient human agency, but a balance between human involvement and automation 
is at the core of future UAS operations. The innovation in our human-autonomy research was to determine those tasks that can be offloaded to the air traffic management systems and those that must be pushed to the user on the ground. To do this, we

---
**[Page 9]**

must better understand the role of first responders and the needs of this group on the 
ground.
4 Results
4.1 Introduction 
After the first round of testing, we developed a list of insights, recommendations, and 
behaviors that will inform both our prototype and other unmanned aircraft interfaces. 
These recommendations and insights highlight user behavior when guiding swarms 
and underline key leverage points as UAS becomes more ubiquitous. This is by no 
means an exhaustive study, but is a first step in understanding this complex system 
within unique mission constraints. It should be noted that these recommendations are 
pointed towards first responders and firefighters working in disaster areas using unmanned aircraft technology and specifically leveraging swarms.
4.2 Recommendations
Any interface that is designed for walk up and use should provide clear language, and 
removing air traffic control jargon like NOTAMs is required when designing usable 
interfaces. NOTAMs are notices to airmen concerning conditions or airspace or hazards usually resulting in a temporary flight restriction and reroute. Our target group 
has minimal ATC and flight knowledge, so removing this terminology and replacing 
it with clear language is key to reduce confusion. Another point of confusion with our 
prototype was that guiding many UAS at once increased the amount of information
the user must hold in their head. Clear labels on zones, trajectories, and flight plan options reduce cognitive loads and are essential to assist the user when guiding multiple 
UAS. Tasks within the geospatial view were also found to be difficult for users because of a lack of clear labels associated with goals and trajectory options. When a 
user has to hold multiple items in their working memory, like goal completion percentage, waypoints met, and ending battery life for three trajectories, an interface 
needs to be clear and easily digestible at a glance.
The ultimate goal of the UAS swarm is to increase a user's situational awareness with 
information gathered by sensors on the UAS. With this in mind, we asked the subjects 
which sensors would be the most useful during a disaster relief scenario. While subjects responded with a variety of different sensors, they all felt that a live video feed 
was the most important. Subjects also suggested many other sensors such as heat and 
radar. Subjects thought heat would be most useful for locating survivors in damaged 
buildings, and that radar would be useful in gaging heights of those buildings and terrain. While small UAS payloads are extremely limited, we feel that this unique mission environment requires the use of multiple sensors to assist first responders. 
Providing this sensor data gives first responders more information and tools, enabling 
greater agency. Users desire agency, and allowing them to control sensors and make 
real-time decisions on the ground provides freedom to an otherwise fully autonomous 
system. During our usability study, one participant said, "Pilots don't like being told

---
**[Page 10]**

what to do," and this thought is an important debate between mission planners and operators. Any human-autonomy partnership suggests minimal human involvement 
from mission planners, however, operators in the field will commonly request more 
freedom. Current technology is unable to handle every edge case and critical moment, 
and it's at these times where the human can take over. Real-time sensor data is also 
key in enabling situational awareness (SA), especially when evaluating a disaster 
area. Users first need an overall, 360-degree view, then a more detailed view of objectives and points of interest. One subject said, "Scene assessment is the first step, start 
out high, then focus in", this global SA is critical in high-intensity disaster relief environments.
4.3 Behavior
During testing, we noticed behavior from subjects that informed our thinking surrounding UAS interfaces as well as the choice architecture presented in this interface. 
We found that subjects hesitated before sending instructions to the swarm and ground 
control stations (GCS). Go/No-Go indicators were recommended by multiple subjects, and could reduce hesitation when sending alternate trajectories or waypoints to 
GCS. One subject who had experience operating UAS said, when asked about his hesitation when sending trajectories, "It's a military thing, double check everything". 
Both his behavior and his thinking at that moment led us to believe that greater affordances were needed to assist users in making these decisions. 
During our simulated test, subjects were presented with a temporary flight restriction 
that required them to change the route of a UAS. After selecting their priority waypoints, the prototype suggested three alternate flight plans for the subjects to choose 
from. Subjects were presented with a geospatial view of the flight plans, as well as 
data presenting how long each flight plan would take, what percentage of their goal 
would be met, and the resulting battery life available after the flight plan was completed. Some users placed importance on hitting waypoints or high percentage current 
goal completion. Others placed importance on saving battery life for future or upcoming goals. This led us to believe that a clear pre-mission briefing was essential for first 
responders to prioritize mission objectives. In a real disaster scenario, first responders 
would have clear objectives, and while we did not instruct them to prioritize time over 
battery life or mission completion, this prototype allowed them to choose flight paths 
based off their own experience. It also indicated that the interface was successful in 
allowing for immediate usability, despite the brief pre-flight introduction.
4.4 Patterns
Several patterns within our data emerged after our usability testing was complete. In 
particular, when subjects were presented with a temporary flight restriction that required them to select high priority waypoints, users felt they didn't have enough information to make an informed decision. Many subjects requested the time to the next 
waypoint as well as the time from waypoint to waypoint. We also found that users 
preferred using both the geospatial and stream view to make these waypoints and trajectory selections. While the timeline view of Playbook presented users with this

---
**[Page 11]**

temporal waypoint information, this was not sufficiently clear, and future prototypes 
need to address this deficiency.
Along with temporal waypoint information, subjects also asked for weather and wind 
data to assist them in making future trajectory decisions, as rotorcraft operated by batteries are especially susceptible to weather and wind. If a UAS is flying into a headwind, that information is crucial to a first responder in the field. Lastly, feedback from 
our usability studies showed an aversion to standard barometric altitude based on sea 
level. Users felt that absolute altitude (Above Ground Level, or "AGL") was preferred. One of pilots' biggest concerns when dealing with low flying aircraft is running straight into objects without knowing it. AGL has a stronger relationship to topography and ground, which is preferred, especially in the case of mountainous areas 
where wildfires commonly take place.
4.5 Future Steps & Discussion 
We also identified some recommendations that are important, but beyond the technical scope of our upcoming flight demonstrations. Through both feedback from our 
subjects and observations from testing, we identified that first responders in some 
cases need to create their own trajectories and requested the ability to drag waypoints. 
This is preferred when negotiating temporary flight restriction (TFR) volumes as the 
areas can change from moment to moment - especially when these are caused due to 
the wildfire itself. Auto-resolver algorithms may not be able to send alternate trajectories fast enough and will not have the same information as a first responder on the 
ground. For this reason, at critical points such as this, we can offload some waypoint 
and trajectory planning to the first responder when necessary. Users also need more 
pre-flight information regarding objectives to make these decisions. This could be a 
preflight briefing as outlined previously, however, future UAS interfaces should be 
able relay this briefing back to the user when requested during a mission. After our 
first round of testing, we realized an additional application for swarm technology was 
to use UAS to create communication network arrays. One subject during our usability 
testing described the difficult terrain common in wildfire or earthquake scenarios, 
which can disrupt standard communication. UAS swarms can provide reliable networks for communication when outfitted with appropriate sensors and antenna arrays 
[14]. However, due to the cost and weight of this equipment, we have not yet been 
able to incorporate this technology in future flight tests.
5 Conclusion
5.1 Summary of Results 
This research is by no means exhaustive, and is only our first round of testing in preparation for our upcoming flight test. We feel that the insights gathered in this initial 
research provide cues for future interfaces for both first responders and usable swarm 
interfaces. Allocation of roles and responsibilities between human-automation systems is key to promoting productive cooperation between these two agents. When

---
**[Page 12]**

guiding a swarm, low-level control should be automated, but, UAS should alert pilots 
and hand over control at key points within a mission. First responders and firefighters 
working in disaster areas using unmanned aircraft technology and swarm interfaces 
need to have a balance between autonomy and workload.
Real-time sensor data is also useful in building situational awareness and notifying 
users when they should take over control of a single aircraft. Users first need an overall, 360-degree view, then a more detailed view of objectives and points of interest. 
First responders need to be able to form a mental model of disaster areas to make informed decisions. These sensors can indicate moments within the mission to notify 
the user when they should take control of single aircraft. Transferring control over a 
single aircraft to the operator is useful at certain key moments in a mission, however, 
this manual process can only be performed on a limited number of aircraft at one time 
[15]. Once decisions need to be made, Go/No-Go indicators could reduce hesitation 
and confusion in these high-intensity environments. One other method for reducing 
confusion and cognitive load is to ensure that these interfaces are removing systemoriented terminology, as first responders often do not have ATC or flight knowledge.
Removing technical terminology is key to reduce confusion and promote risk reduction. Finally, breaking complex missions into clear goals frame UAS tasks and mission objectives. As the number of UAS and tasks increase within a mission, clear 
goals provide clarity for first responders.
One of NASA's human research goals is to develop design guidelines for effective human-automation-robotic systems, specifically distributed swarm systems [16]. The 
use cases for this type of technology include transportation, construction, relief efforts, military, and space applications. Reducing operator workload in these disaster 
relief environments can lead to improved safety and mission outcomes. The interface 
presented here is focused on a future flight demonstration at NASA Ames, however, 
these insights and recommendations can be translated to other swarm applications 
outside of the use in disaster relief.
When one user is controlling multiple actors in a system, they are no longer concerned with the low-level actions of each aircraft. Goal-oriented planning and higherlevel interactions are more useful [17]. This style of goal-oriented planning can reduce cognitive load for the user as they will no longer have to focus on many concurrent tasks being executed by the swarm. Controlling swarms of robotic agents, such as 
UAS or ground rovers for space applications, requires a higher level, goal-based interface with usability at its core.
5.2 Acknowledgments 
The authors would like to thank Jimin Zheng, Matthew Chan, and Richard Joyce for 
support and development work during the various stages of this project. The authors 
would also like to thank the subject testing participants, Ames DART, as well as Eric 
Mueller for his leadership on the Connected Smart Aerospace Systems project 
(CASAS). This work was performed under a US Govt. Contract in the Human-Systems Integration Division at NASA Ames Research Center.

---
**[Page 13]**

References
1. Endsley, Mica R.: Toward a Theory of Situation Awareness in Dynamic Systems. Human 
factors 37.1. (1995).
2. Barber, K. Suzanne. Han, David C.: Multi-Agent Planning Under Dynamic Adaptive Autonomy. International Conference on Systems Man and Cybernetics. Institute of Electrical 
Engineers INC (IEEE). (1998).
3. Jung, Dongwon. Ratti, Jayant. Tsiotras Panagiotis.: Real-Time Implementation and Validation of a New Hierarchical Path Planning Scheme of UAVs via Hardware-in-the-Loop 
Simulation. Journal of Intelligent and Robotic Systems. (2009).
4. Rasche, Christoph, et al.: Combining Autonomous Exploration, Goal-Oriented Coordination and Task Allocation in Multi-UAV Scenarios. Autonomic and Autonomous Systems 
(ICAS), 2010 Sixth International Conference on. IEEE. (2010).
5. Hillenius, S.: Designing Interfaces for Astronaut Autonomy in Space. CanUX 2015. Ottawa, Canada. (2015). Invited Speech.
6. Hillenius, S. Marquez, J. Deliz, I. Kanefsky, B. Korth, D. Healy, M. Gibson, S. Zheng, J.: 
Designing and Building a Crew-Centric Mobile Scheduling and Planning Tool for Exploring Crew Autonomy Concepts Onboard the International Space Station. ISS R&D Conference 2016. Conference. San Diego, CA. (2016). Speech.
7. Space Shuttle Program Flight Data File, https://www.nasa.gov/centers/johnson/pdf/567071main_FLT_PLN_135_F.pdf, last accessed 2018/2/9.
8. Apollo 11 Flight Plan, https://www.hq.nasa.gov/alsj/a11/a11fltpln_final_reformat.pdf, last 
accessed 2018/2/9.
9. Hashemi, S. Hillenius, S.: @NASA: The User Experience of a Space Station. SXSW Interactive 2013. Interactive. Austin, TX. (2013).
10. Erzberger, H.: Automated Conflict Resolution for Air Traffic Control. Proc 25th International Congress of the Aeronautical Sciences (ICAS). Germany (2006).
11. Ericsson, K. Anders. Simon, A. Herbert.: Protocol Analysis: Verbal Reports as Data. Cambridge, MA. MIT Press (1993).
12. NASA: HCI-05.: We need verifiable requirements that specify standard measurement techniques and metrics for evaluating the quality of user interfaces. (2017). https://humanresearchroadmap.nasa.gov/gaps/gap.aspx?i=329, last accessed 2018/2/7.
13. DART Homepage, http://dart.arc.nasa.gov, last accessed 2018/2/9.
14. Palat, R.C. Annamalau, A. Reed, J.R.: Cooperative Relaying for Ad-hoc Ground Networks Using Swarm UAVs. Military Communications Conference. MILCOM 2005. IEEE, 
Atlantic City, NJ, USA (2005).
15. Prevot, Thomas. Homola, Jeffrey. Mercer, Joey.: Human-in-the-Loop Evaluation of 
Ground-Based Automated Separation Assurance for NextGen. The 26th Congress of International Council of the Aeronautical Sciences (ICAS). Anchorage, Alaska, USA (2008).
16. NASA: HARI-02 We need to develop design guidelines for effective human-automationrobotic systems. (2017). https://humanresearchroadmap.nasa.gov/Gaps/gap.aspx?i=334, 
last accessed 2018/2/9.
17. Lieberman, Henry. Espinosa, Jose.: A Goal-Oriented Interface to Consumer Electronics 
Using Planning and Commonsense Reasoning. Proceedings of the 11th International Conference on Intelligent User Interfaces - IUI (2007).