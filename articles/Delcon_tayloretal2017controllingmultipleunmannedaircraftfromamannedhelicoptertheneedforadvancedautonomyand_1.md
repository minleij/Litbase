# Delcon tayloretal2017controllingmultipleunmannedaircraftfromamannedhelicoptertheneedforadvancedautonomyand 1

*Source file: Delcon_tayloretal2017controllingmultipleunmannedaircraftfromamannedhelicoptertheneedforadvancedautonomyand_1.pdf — 5 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

Controlling Multiple Unmanned Aircraft from a Manned Helicopter:
The Need for Advanced Autonomy and Refined Pilot-Vehicle Interface
Dr. Grant S. Taylor1, Dr. Thomas J. Alicia1, Terry Turpin1, & Dr. Amit Surana2
1U.S. Army Aviation Development Directorate (ADD)
2United Technologies Research Center (UTRC)
Manned-Unmanned Teaming (MUM-T) is a military concept that employs unmanned aerial systems 
(UASs) in support of traditional manned aircraft. The current ratio of manned to unmanned aircraft in 
MUM-T operations is one to one with a goal to expand to multiple UASs to further enhance the capability, 
but this imposes significant challenges on the operator. To address these challenges, this research 
implemented automated UAS behaviors combined with a pilot-vehicle interface tailored to provide 
supervisory control over multiple UASs. Results demonstrated that this combination of technologies allows 
a single crewmember to effectively manage up to three UASs while executing complex MUM-T tactical 
missions with manageable workload, improved situational awareness, and improved mission performance.
Experimental results also identified areas where the current implementations can be further refined.
Manned-Unmanned Teaming (MUM-T) is a military 
warfighting concept that teams manned aircraft with 
Unmanned Aerial Systems (UASs). The goal of MUM-T is to 
increase Situational Awareness (SA) and survivability by 
positioning a UAS downrange while the manned aircraft 
remains in a secure position. Recent fielding of the Army’s 
AH-64E Apache has transitioned MUM-T from concept to 
reality, allowing Apache crewmembers to receive and control 
the sensor payload, weapons, and flight path of a single UAS.
To further enhance the effectiveness of MUM-T operations,
the Department of Defense desires to expand the control ratio 
to team a single manned aircraft with multiple UASs
(Department of Defense, 2013). Providing the ability to 
control multiple UASs without imposing excessive workload 
requires the development of a new automated UAS
employment concept and an advanced cockpit tailored for 
MUM-T operations (Taylor & Turpin, 2015). The challenge is 
to identify the appropriate level of automation and pilotvehicle interface design that best facilitates mission 
performance while maintaining a manageable level of 
workload for the air crewmembers (Peters et al., 2015).
The purpose of this study was to develop interface design
and automated UAS behaviors that would enable a 
crewmember to manage their own aircraft sensor and weapons 
payloads while also managing the flight path, sensors, and 
onboard weapons of multiple UASs operating together as a 
team. An evaluation of this system quantified its impact on 
mission effectiveness, workload, and SA.
METHOD
Simulation Capabilities
Manned platform and capabilities. The manned 
crewstation simulated in the experiment was the copilot 
gunner position of a generic attack helicopter. The subject 
pilot seated in this crewstation acted as the Air Mission 
Commander (AMC) of an air weapons team consisting of the 
manned platform teamed with up to three UASs. There were 
no flight controls available; the AMC navigated via waypoint 
management. The manned platform was equipped with a 
slewable Electro-Optical (EO) sensor with targeting laser 
designator, and laser-guided Hellfire missiles.
UAS platforms and capabilities. Two models of fielded 
Army UASs were used in the simulation: the MQ-1C Gray 
Eagle and the RQ-7B Shadow. Both UAS platforms were 
equipped with a slewable EO sensor with laser designator, 
while the Gray Eagle also had Hellfire missiles. Throughout 
the mission scenarios the AMC maintained full Level of 
Interoperability (LOI) 4 capability (controlling the sensor 
payload and UAS position in space) at all times with exclusive 
authority and control of the UAS platforms. All missions 
began with the supporting UAS(s) in flight performing a loiter 
maneuver, maintaining a continuous datalink with the manned 
platform. Airspace deconfliction was automatic with no 
interaction with air traffic control. There were no simulated 
system failures and fuel and weapons were unlimited.
Automated behaviors. Four automated UAS behaviors 
were available using a system called Delegation of Control 
(DelCon), analogous to a football coach calling a play for a 
team. A set of simple high level commands triggered a set of 
complex UAS actions in support of the high level command. 
To maintain flexibility within dynamic missions a DelCon 
play could be modified, paused, or cancelled during execution, 
allowing an operator to maintain supervisory control over 
multiple UASs with minimal additional workload. The 
DelCon concept was validated during previous laboratory 
simulations (Fern & Shively, 2009) as well as a live flight 
demonstration at Ft. Hunter Liggett, CA in 2013. The DelCon 
plays are described below:
Point reconnaissance (recon). DelCon allowed the AMC 
to specify one or more Point of Interest (POI) locations on the 
digital map. Once the POI locations were selected the AMC 
could further specify the viewing conditions of the point (e.g.,
view from the north, orbit around the POI), or allow a path 
planning algorithm to determine the most efficient viewing 
conditions. If there were multiple POIs and multiple UASs
selected to execute the recon, DelCon would automatically 
distribute the taskload and specify which UAS would cover 
each POI. The DelCon system also reconfigured the UAS task 
Not subject to U.S. copyright restrictions. DOI 10.1177/1541931213601485
Proceedings of the Human Factors and Ergonomics Society 2017 Annual Meeting 78

---
**[Page 2]**
*(This page contains a figure/chart/image not captured in text)*

assignment if a POI or UAS was added or removed during 
mission execution. During execution, DelCon automatically 
generated and executed flight routes for each UAS while also
aiming the sensor payload at each POI.
Area recon. The DelCon system was capable of executing 
an area recon with one or more assigned UAS assets. The area 
was defined using map graphics in pre-mission planning or 
during mission execution. Once an area was defined and one 
or more UASs were assigned, the DelCon system divided the 
area into sub-regions and assigned them to the UAS assets to 
search. The DelCon system generated flight paths for each 
UAS and controlled the sensor on each UAS to search the 
terrain. The DelCon system automatically reconfigured the 
regions assigned to each UAS if an asset was added to or 
removed during execution.
Route recon. A route recon could be assigned to one or 
more UASs for DelCon execution. Once assigned, the route 
was divided up equally between the assigned UASs. The flight 
routes were purposely offset from the ground route under 
surveillance by 1-2 km to minimize the chance of exposing the 
route to the enemy. UAS sensors automatically scanned along 
the route as the flight routes were executed. If a UAS was 
reassigned during the route recon the remaining assets 
reconfigured their air routes to cover the vacated section of the 
route.
Safe air volume weapons engagement. Once a target was
identified the DelCon system could facilitate a weapons 
engagement. The AMC specified the intended target, the 
shooting platform, and the designating platform. The shooter 
and designator could be the manned aircraft or any UAS with 
the necessary payload. DelCon identified a firing position and 
designating position for each aircraft within geometric 
constraints for a Hellfire engagement, considering 
minimum/maximum missile firing range, the no-fly zone 
along the missile flight path, and angular constraints for the 
laser designator. The result was an optimum firing solution 
without need for the AMC to remember and calculate complex 
geometric constraints. Once all supporting aircraft were in 
position, the system required the AMC to manually arm and 
fire the laser designator and missile.
Aided target recognition. The DelCon system did more 
than assist the AMC in controlling UAS assets, it also assisted
in the processing of incoming sensor imagery. This was a 
critical component, as once the UAS control functions were 
highly automated, the AMC’s ability to process the incoming 
sensor video information became the bottleneck in the system. 
To reduce information processing demands on the AMC, all 
sensor imagery was processed by an Aided Target 
Recognition (ATR) system that helped to detect targets of 
interest. The ATR simulated an image recognition process that 
is capable of discriminating people and vehicles from 
background imagery. The ATR process was simulated because 
existing systems have not yet reached the level of reliability 
necessary to adequately reduce workload (Sager & Hoff, 
2014). Although the process was simulated, ATR performance 
was constrained to avoid providing an unrealistic capability. 
Before detecting a target, the ATR system ensured that the 
target was within the sensor field of view, was unobstructed 
by other objects (e.g. terrain, buildings, vegetation), and 
subtended an adequate visual angle at the UAS sensor to be 
detectable (set to perform slightly worse than a human). Once 
a target was detected during a DelCon recon mission, the UAS 
sensor automatically locked onto and tracked the target and 
notified the AMC that a target had been detected with visual 
and auditory alerts. The AMC then determined whether to 
ignore the target (break lock and continue the automated 
search), continue tracking the target, or initiate an 
engagement.
Pilot-Vehicle Interface Cockpit Design
Out the Window (OTW) view. The OTW scene was 
presented on a 60” flat screen LED monitor. With multiple 
sensor views of the outside world available on the cockpit 
displays, the AMC rarely used the OTW scene as a reference. 
Although infrequently used, the OTW scene was provided to 
improve immersion in the simulated environment.
Multi-sensor display. The sensor display was the primary 
reference for the AMC to see what was being imaged by all of 
the aircraft sensors. The sensor display was a 22” capacitive 
touchscreen. The border around each sensor was color coded 
to reflect which aircraft was generating the image. The 
primary sensor selected for viewing and interaction was a 
17.5” diagonal portion of the sensor display. The remaining 
sensor views were each shrunk to a 5.75” view and vertically 
stacked on the right side of the primary view (Figure 1). The 
AMC could change the primary sensor by either pressing one 
of four buttons on the hand controller, or by touching one of 
the secondary sensor views on the sensor display. The AMC 
could slew and zoom the primary sensor view using joysticks
on the hand controller.
Figure 1. Cockpit Controls and Displays
Digital map tactical information display. The map display 
was positioned to the right of the sensor display and used the 
same display hardware. The digital map showed the current 
position of each teamed air vehicle along with their flight 
routes and sensor footprints, all appropriately color coded to 
Proceedings of the Human Factors and Ergonomics Society 2017 Annual Meeting 79

---
**[Page 3]**

match the sensor display. A toolbar was displayed on the left 
side of the map that provided the utilities for interacting with 
the map. Each utility is described below:
Interact tool. The interact tool allowed the map to be 
repositioned to view other areas in the map database. The 
interact tool was also used to tap a vehicle for more details and 
to tap/drag and edit existing waypoints.
Air waypoint tool. The AMC could tap the map to create 
a waypoint route for the current active air vehicle. Multiple 
waypoints could be created by repeatedly tapping on the map 
without having to select the waypoint tool after each tap. 
POI tool. The AMC selected the POI tool and then tapped
on the map to create a new POI or edit an existing POI.
Route of interest tool. The AMC selected the route of 
interest tool and then tapped two or more locations on the map 
to create a route, or selected an existing route to be modified.
Area of interest tool. The AMC selected the area of 
interest tool icon then tapped on the map to create an area. The 
area could be stretched or expanded to any desired size by 
touching and dragging a corner. Priority regions could be 
created inside the larger area, which were colored in red for 
high priority or yellow for low priority. During a DelCon area 
recon, high priority regions were scanned more frequently 
than regions of lower priority.
Zoom tool. Tapping on the zoom tool icon zoomed the 
map in (+) or out (-) showing more or less detail until the 
desired level was achieved. Software limitations required the 
use of single touch interactions rather than the traditional 
multi-touch pinch-to-zoom interaction.
Hand controller. The hand controller was mounted to an 
adjustable arm, allowing the AMC to position/angle it to their 
preference. The hardware, a UGCS-400 from Kutta 
Technologies, included a 6.5” touchscreen display, two small 
joysticks on either side, two trigger buttons on top, and eight 
additional buttons on the front. The touchscreen provided a 
graphical user interface to create or modify a DelCon mission 
and manage advanced sensor and weapon functions. The 
physical joysticks, triggers, and buttons performed dedicated 
sensor control functions.
Sensor control. The right joystick controlled the sensor 
slew (azimuth and elevation angle). The left joystick 
controlled the continuous zoom factor of the sensor.
Image auto-track (IAT). IAT was used to lock the sensor 
to a target. The left trigger button toggled IAT on and off. In 
manual control, the AMC moved the sensor crosshair over the 
target and pushed the left trigger button to engage IAT. During 
DelCon mission execution, the IAT automatically locked on to 
track a suspected target and await the AMC’s response.
DelCon mission creation. The hand controller touchscreen 
enabled the AMC to create, monitor, and modify DelCon 
missions. To create a new mission, the AMC first selected the 
desired behavior, then selected an objective (the points, route, 
area, or target of interest) and assigned UAS assets to the 
mission, and finally specified mission parameters (UAS 
altitude, ATR behavior: detect people/vehicles). A summary 
was presented for the AMC’s final approval before the 
mission was executed. Once a mission was active, the AMC 
could modify the configuration (objective, assets, and 
parameters) or terminate the mission at any time. The DelCon 
system could execute multiple concurrent missions, but a UAS 
could only be assigned to a single mission at a time.
Pause/resume DelCon behavior. The AMC could pause a 
vehicle’s execution of a DelCon mission by pushing the right 
trigger button. While paused, the pilot could take manual 
control of the sensor and look at objects of interest. Once the 
reason for the pause was satisfied, pushing the right trigger 
again resumed the DelCon mission.
Communications. Communications between the AMC,
the pilot on the flight controls, and the Tactical Operations 
Center were accomplished using a commercial headset and 
voice over IP connection. A continuous open mic was used to 
make communication easy and to minimize push-to-talk 
hardware requirements. An attempt was made to keep the 
communications between the participant AMC and all other 
team members as realistic as possible to help create a feeling 
of tactical realism in the simulation.
Experiment Execution
Experiment design. A 2x2 within-subjects design was 
used to evaluate the impact of autonomy (DelCon present or 
absent) and number of teamed UASs (one, a Gray Eagle, or 
three, a Gray Eagle and two Shadows) on mission 
performance, workload, and SA. The experiment occurred
over two days. Day one consisted of training, including 
classroom instruction, hands-on interface instruction, and four 
practice missions. Day two began with two practice missions, 
followed by four experimental missions, and ending with an 
in-depth debrief interview.
Dependent measures. Objective measures of mission 
performance were recorded as mean time to complete primary 
mission tasks: point recon, route recon, area recon, and target 
engagement. An additional measure of sensor utilization was 
also computed. A sensor was considered utilized when it met 
multiple conditions: sensor footprint area was less than 0.5km2
(to ensure the sensor was adequately zoomed); speed of the 
sensor center point over the terrain was less than 2,000km/h 
(to ensure the imagery was stable enough for the AMC to 
process); and, if the sensor was stationary relative to the 
terrain, a target was present within the sensor view. With these 
conditions, a sensor was only considered to be utilized if it 
was actively gathering useful information for the AMC –
either conducting recon in search of a target, or conducting 
surveillance of a known target. Sensor utilization was 
calculated as the sum of the utilization of all sensors (the 
manned platform and all teamed UASs), resulting in a 
maximum value of 2.0 with a single UAS and 4.0 with three 
UASs. The same utilization conditions were also used to 
calculate the percentage of an area of interest covered during a 
recon mission.
Subjective ratings of AMC workload and SA were 
measured using the Bedford Workload Scale (Roscoe & Ellis, 
1990) and the China Lake Situational Awareness Scale (Hicks, 
Durbin, Morris, & Davis, 2014), administered after each 
Proceedings of the Human Factors and Ergonomics Society 2017 Annual Meeting 80

---
**[Page 4]**

mission. These measures were selected in part for their 
simplicity: each provides a single global metric of workload 
and SA, respectively. More detailed subjective measures of 
workload (NASA-TLX) and SA (Situational Awareness 
Rating Technique; SART) were also collected, but limited 
space prevented their inclusion in this report.
Participants. Eight pilots participated in the experiment. 
All participants were military rated helicopter experimental 
test pilots and line unit pilots with combat experience. The 
participants had an average of 3,430 flight hours, all had 
experience conducting recon and surveillance missions, and 
six participants had prior MUM-T experience.
Mission scenarios. The terrain database used to support 
the scenarios was a VBS3 generated 13 km x 13 km, high 
resolution terrain with cultural features representative of the 
Pakistan/Afghanistan border region. The terrain included a 
mix of mountains, flat, and hilly areas with a road network and 
small villages. The mission scenarios were based on real 
missions that required a combination of recon, surveillance, 
and weapons engagements. Four data collection missions were 
used: 1) area recon for a single high value target; 2) deliberate 
attack supporting a downed aircraft crew extraction; 3) point 
recon supporting a hostage rescue; and 4) route security and 
close combat attack for the capture of a high value target. The 
duration of each mission was typically 20-35 minutes. The 
pairing of missions with each experimental condition was 
counterbalanced between participants.
RESULTS
Table 1. Dependent Measure Means and Standard Deviations
Without DelCon With DelCon
1 UAS 3 UAS 1 UAS 3 UAS
Point Recon Duration (sec) 506.00
132.94
546.00
135.77
1348.0
817.42
552.00
209.30
Route Recon Duration (sec) 298.50
36.06
269.50
186.97
93.25
21.57
108.00
14.14
Area Recon Duration (sec) 126.00
6.36
206.25
51.27
659.75
609.17
283.00
320.32
Target Engagement 
Duration (sec)
134.13
24.57
94.25
13.79
206.00
7.42
201.38
40.48
Missiles Fired Outside of 
Constraints (%)
100
0.00
50
0.00
12.5
17.7
37.5
17.7
Sensor Utilization 1.19
0.33
2.08
0.53
1.28
0.23
2.85
0.29
Area of Interest Coverage 
(%)
73.5
13.44
65.5
13.44
94.0
2.83
85.0
21.21
Bedford Workload 3.75
1.17
4.50
2.00
3.69
0.88
4.00
1.51
China Lake SA 1.88
0.35
2.13
0.64
1.75
0.71
2.00
0.76
Means and standard deviations (in italics) for each dependent measure within 
each experimental condition.
Due to limited sample size, experimental results were 
evaluated through trends in descriptive statistics (Table 1).
Where applicable, effect sizes are provided to illustrate the 
practical impact of the effects. For all duration measures lower 
values indicate better performance. For sensor utilization 
larger values indicate better use of the available equipment. 
Lower Bedford workload ratings (on a scale of 1-10) indicate 
lower workload, and lower China Lake values (on a scale of 1-
5) indicate greater SA.
CONCLUSIONS
In conclusion, using the DelCon system did enable 
participants to utilize UAS assets much more than manual 
control, as shown by the increased sensor utilization (d = 
1.25). Participants’ efficiency of use, however, varied 
depending on the specific mission task, with some DelCon 
behaviors clearly requiring further improvement. Despite 
increased utilization, participants also reported moderately 
lower levels of workload (d = -0.20) when using DelCon 
relative to manual control. SA ratings were also moderately 
better (d = -0.21) with DelCon than without, but the 
magnitude of difference was such that additional analysis of 
more detailed measures is necessary to better understand the 
effect.
Point recon duration was generally similar with or without 
the DelCon system active, with the exception of a single 
outlier participant which greatly increased average duration in 
the DelCon with one UAS condition. The other point recon
times show no substantial effect of number of UAS or level of 
autonomy on task performance. This can be attributed to the 
task consisting primarily of waiting for vehicles to arrive at 
their points of interest. The AMC can direct a UAS to a 
specified point and then shift attention to a different task while 
that UAS is enroute. This provides for easier coordination of 
assets and little discernable advantage of an automated aid.
Additionally, the viewing constraints used by DelCon (sensor 
look-down angle, stand-off range) were more restrictive than 
those used by participants during manually controlled 
missions. The more stringent positioning requirements 
resulted in longer aircraft transit times, negating any benefit of 
the automation.
Route recon performance was much faster (d = -2.83) 
when using the DelCon system with both one and three UAS 
assets. Execution of route recon is less ambiguous than point 
recon, allowing the DelCon system to execute the task in the 
same manner as a human operator, with the added efficiency 
of manipulating multiple sensors simultaneously. Although 
task duration with DelCon was slightly slower with three UAS 
than one, it is important to note that the three UAS condition 
provided multiple UAS to the AMC but left task assignment to 
the operator. In the three UAS with DelCon condition 
participants often assigned multiple UAS to perform separate 
tasks in parallel rather than serially assign all assets to one task 
at a time.
Area recon duration was considerably slower with the 
DelCon system (d = 1.24), particularly with a single UAS. The 
specific targets to be identified in this scenario were pickup 
truck vehicles, and the task ended after a target was detected.
The participants in manual conditions all correctly realized 
Proceedings of the Human Factors and Ergonomics Society 2017 Annual Meeting 81

---
**[Page 5]**

targets would be most likely found on a road, but DelCon did 
not. This resulted in a sub-optimal search pattern which failed 
to acquire the targets as quickly by scanning terrain 
inaccessible to the target vehicles, as evidenced by its greater 
area of interest coverage percentage but slower performance.
For target engagement missions, the results again showed 
much slower performance using the DelCon system (d = 4.15), 
with the lowest means resulting from the No DelCon/3 UAS 
condition. When manually positioning assets for recon many 
participants anticipated potential engagements, arranging their 
UASs such that they were already in appropriate firing 
positions to engage detected threats. Conversely, the DelCon 
system did not anticipate potential engagements when 
positioning UASs for recon. In fact, the flight pattern used to 
conduct DelCon recon typically resulted in the UAS being 
very poorly positioned to support an engagement, increasing
engagement response times. However, the DelCon system did 
result in a much lower rate of missiles fired outside of safety 
constraints (d = -5.65), so although participants performed 
faster without DelCon they were at greater risk of fratricide 
and missing the target.
Moving forward, there are ways to improve on these 
results and streamline performance. Researchers must 
continue to identify strategies used by human operators that 
can be incorporated into DelCon behaviors. For example, 
viewing constraints must be relaxed in the point recon
behavior to more closely match those used in manually 
executed missions. Similarly, specialized search strategies, 
such as focusing on roads when searching for vehicles, must 
be included in the area recon behavior. For all recon
behaviors, assets must be positioned such that they can easily 
engage targets detected within the search area. With these 
enhancements, the DelCon system will perform more similarly 
to a human operator, with the benefit of being capable of 
conducting multiple tasks simultaneously without the 
interference which results from the human’s limited cognitive 
resources.
The interface can also be improved. For instance, one 
suggestion is that participants who locate a target they wish to 
engage while in a recon mission should be able to 
automatically set up a target engagement with a single button 
push. This would reduce the overhead complexity of trying to 
determine which other assets can be interrupted (if any), 
directing those assets to appropriate designating or firing 
positions, and then waiting while the assets are in transit. 
Separately, the map interface is also prone to excessive clutter 
if many labeled objects (i.e., stored targets) exist in a small 
area, as happens frequently in complex missions. Participants 
also had difficulty tracking the progress of multiple 
autonomous UASs conducting recon missions, so a novel 
method of visualizing sensor coverage history on the map is 
planned to improve SA. Additionally, a redesigned or 
simplified representation of the safe area volume during target 
engagement may reduce incidents of missiles fired outside of 
constraints.
Although the current implementation of the DelCon 
system and surrounding interface improves UAS sensor 
utilization while also reducing workload, the incorporation of
these improvements is expected to further increase usability,
efficiency, and mission performance. While current
autonomous behaviors improve sensor utilization, they lack 
the human operator’s expert strategies to employ the assets 
efficiently. Continued effort to more closely align autonomous 
behaviors with experienced operator techniques and strategies 
is critical to allow an AMC to maximize the force-multiplying 
potential of the MUM-T concept.
ACKNOWLEDGEMENT
DISTRIBUTION A. Approved for public release:
distribution unlimited (PR #2719). This project is sponsored 
by the U.S. Army Research Office and the Regents of the 
University of California, through Contract Number W911NF09-D-0001 for the Institute for Collaborative 
BioTechnologies. The information presented does not 
necessarily reflect the position or the policy of the 
Government or the Regents of the University of California, 
and no official endorsement should be inferred.
REFERENCES
Department of Defense. (2013). Unmanned systems integrated 
roadmap: FY2013-2038. Reference 14-S-0553. Retrieved 
from http://archive.defense.gov/pubs/DOD-USRM2013.pdf
Fern, L., & Shively, R. (2009). A comparison of varying levels 
of automation on the supervisory control of multiple 
UASs. Proceedings of AUVSI’s Unmanned Systems
North America, Washington, DC.
Hicks, J., Durbin, D., Morris, A., & Davis, B. (2014). A 
summary of crew workload and situational awareness 
ratings for U.S. Army aviation aircraft (Report #ARLTR-6955). Aberdeen Proving Ground, MD: U.S. Army 
Research Laboratory.
Peters, J., Srivastava, V., Taylor, G., Surana, A., Bullo, F., & 
Eckstein, M. (2015). Human supervisory control of 
robotic teams: Integrating cognitive modeling with 
engineering design. Control Systems, IEEE, 35(6), 57-80.
Roscoe, A., & Ellis, G. (1990). A subjective rating scale for 
assessing pilot workload in flight: A decade of practical 
use (Report #90019). Bedford, UK: Royal Aerospace 
Establishment.
Sager, H., & Hoff, W. (2014). Pedestrian detection in lowresolution videos. IEEE Conference on Applications of 
Computer Vision, Steamboat Springs, CO.
Taylor, G., & Turpin, T. (2015). Army aviation MannedUnmanned Teaming (MUM-T): Past, present, and future.
Proceedings of the 18th International Symposium on 
Aviation Psychology, 560-565.
Proceedings of the Human Factors and Ergonomics Society 2017 Annual Meeting 82