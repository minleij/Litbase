# Burkle

*Source file: Burkle.pdf — 15 pages*


---
**[Page 1]**

J Intell Robot Syst (2011) 61:339–353
DOI 10.1007/s10846-010-9492-x
Towards Autonomous Micro UAV Swarms
Axel Bürkle · Florian Segor · Matthias Kollmann
Received: 1 February 2010 / Accepted: 1 September 2010 / Published online: 27 October 2010
© Springer Science+Business Media B.V. 2010
Abstract Micro Unmanned Aerial Vehicles (UAVs) such as quadrocopters have
gained great popularity over the last years, both as a research platform and in various
application fields. However, some complex application scenarios call for the forma-
tion of swarms consisting of multiple drones. In this paper a platform for the creation
of such swarms is presented. It is based on commercially available quadrocopters
enhanced with on-board processing and communication units enabling full autonomy
of individual drones. Furthermore, a generic ground control station is presented that
serves as integration platform. It allows the seamless coordination of different kinds
of sensor platforms.
Keywords UAVs · Micro drones · Swarms · Ground control station
1 Introduction
Since the introduction of quadrocopters a few years ago, the use of micro UAVs
has gained great popularity. Today there is a variety of available models ranging
from rather inexpensive kits for self-assembly to sophisticated professional solutions.
The advantages of micro VTOL (Vertical Take-Off and Landing) UAVs over
bigger drones like MALE (Medium Altitude Long Endurance) or HALE (High
Altitude Long Endurance) UAVs are obvious: They are more cost-efficient, easier to
A. Bürkle (B) · F. Segor · M. Kollmann
Optronik, Systemtechnik und Bildauswertung, Fraunhofer IOSB,
Fraunhoferstraße 1, 76131 Karlsruhe, Germany
e-mail: axel.buerkle@iosb.fraunhofer.de
URL: www.iosb.fraunhofer.de
F. Segor
e-mail: ﬂorian.segor@iosb.fraunhofer.de
M. Kollmann
e-mail: matthias.kollmann@iosb.fraunhofer.de

---
**[Page 2]**

340
J Intell Robot Syst (2011) 61:339–353
transport and can be deployed in shorter time. With micro UAVs it is also possible to
access narrow areas that are inaccessible to larger drones, especially in urban terrain.
Another advantage of VTOL UAVs, such as quadrocopters, is their ability to hover
above a point of interest.
However, micro UAVs exhibit limitations due to their size. Their payload is
usually only a few hundred grams allowing just light and compact sensors. What
kind of sensor is best suited for a specific mission, e.g. optical or infrared camera
has to be planned beforehand. Today, quadrocopters are teleoperated through a
remote control or a ground station. In both cases, the operational range is limited
by the communication link to the operator. Obstacles like trees or buildings between
remote control and drone further reduce this range. Furthermore, micro UAVs have
a rather short endurance.
Most of these limitations can be eased by employing teams or swarms of cooper-
ating UAVs. On top of that, some complex monitoring and surveillance applications
can only be implemented with groups of flying platforms. While the control of
a single micro UAV is already well understood and a wide range of commercial
products are available, the use of multiple platforms simultaneously still needs
investigation. This paper presents ongoing work on the development and simulation
of autonomous devices and strategies for the formation of swarms of micro UAVs.
In the following section, an overview of possible application scenarios for micro
UAVs is given with special regard to swarms of micro drones. After a short survey of
related work the apparatus used for this work is presented. It consists of a modified
commercial flight platform and a self-made ground control station. Communication
and control of the micro UAVs is realized through a programmable video camera
in combination with a WiFi module integrated into the drones. An agent-based
framework for the realization of different coordination strategies and a simulation
environment are presented. This paper closes with a summary and discussion of
future work.
2 Application Scenarios
In a recent Frost & Sulivan report [5], application scenarios for UAV platforms are
divided into military and civil applications. According to this report micro UAVs
are already used in vast and diverse civil applications. Some of the tasks that can
be supported with UAVs in general include but are not limited to: enhancing
agricultural practices, police surveillance, pollution control, environment monitoring,
fighting fires, inspecting dams, pipelines or electric lines, video surveillance, motion
picture film work, cross border and harbor patrol, light cargo transportation, natural
disaster inspection, search and rescue, and mine detection.
Obviously some of these tasks are not suitable for micro UAVs due to their limited
operating range and payload. With groups or swarms of micro UAVs it is possible to
realize scenarios that are inefficient or even not feasible with a single micro drone.
In the following some application scenarios for micro UAV swarms are presented.
Military users such as tactical units on patrol missions can apply micro UAVs for
intelligence, surveillance and reconnaissance tasks. Swarms bring the capability of
coordinated area surveillance. Also, the application of micro UAVs in “military op-
erations in urban terrain” (MOUT) is publically discussed. Currently, the capability

---
**[Page 3]**
*(This page contains a figure/chart/image not captured in text)*

J Intell Robot Syst (2011) 61:339–353
341
to safely look into buildings is a highly requested feature. Such a feature is not yet
ready available but is actively investigated e.g. in the DARPA program VisiBuilding
[16]. The use of micro UAVs acting as relay node into buildings is also discussed.
In the civil domain in the event of a big incident there is a need for an immediate
situation picture to support the rescue forces in making decisions. The search for
buried people after building collapses or the clarification of fires at big factories or
chemical plants are possible scenarios. Only in the minority of cases the rescue forces
can rely on an already available sensor infrastructure at the incident site. If there
were sensors available, there is a significant chance they will have been destroyed
or at least partially corrupted. A transportable sensor system that can be deployed
quickly and inexpensively to the site of the event can close this gap. Especially in
time-critical rescue operations swarms help to significantly speed up the collection of
a highly up-to-date situation picture from the air. Figure 1 shows an example picture
generated with our UAV system.
Micro UAVs, in combination with other sensors, are also employed for the
protection of military camps, convoys, industrial premises and other safety critical
infrastructures. In such security applications the perimeter or outer fence could be
monitored by movement detectors (e.g. visual or passive infrared). Micro UAVs
such as quadrocopters can patrol areas of interest. In case of a perimeter violation
quadrocopters could be directed to the place of the event in order to follow and
monitor a potential intruder. Several cases could raise the demand for a swarm of
quadrocopters in such a situation.
•
A quadrocopter loses connection to the ground control station because it moved
too far or the signals are blocked by an obstacle. In a group of quadrocopters,
one of them can be “parked” in reach of the ground control station and act as
relay station.
Fig. 1 A high-resolution
situation picture (ca. 9,500 ×
9,000 pixel)

---
**[Page 4]**

342
J Intell Robot Syst (2011) 61:339–353
•
Several intruders enter the site. They later split up, each taking different direc-
tions. A single drone would have to decide which person to follow, while a swarm
of UAVs can form subgroups and track each intruder individually.
•
The duration of surveillance exceeds battery life time. In a team assignments can
be planned accordingly and another quadrocopter can take over the task of an
out-of-battery drone.
•
A threat has to be monitored with different sensor types. For example, an
intruder who is tracked visually suddenly places an object. Besides the visual
sensor some CBRNE (chemical, biological, radiological, nuclear, and explosive)
detection devices are needed. Since the payload of a single quadrocopter is very
limited a swarm could carry different sensors.
•
Multi-sensor capability can also be used to visually control the action of different
drones. For example an infrared sensor equipped quadrocopter could be em-
ployed by the operator located in the ground control station to navigate a
chemical sensor equipped micro UAV through a dark building.
These cases illustrate that there is a need for forming swarms of micro UAVs.
The coordination with other sensor platforms, such as UGVs (Unmanned ground
vehicles) or stationary sensors, adds further value to the system.
3 Related Work
The cooperative control of teams or swarms of UAVs makes high demands on the
flight platform and requires new control strategies. With an increasing number of
team members manual control becomes more and more impractical if not impossible.
A general approach is to equip the UAVs with a certain amount of autonomy. This
requires capabilities such as communication between drones, autonomous real-time
navigation, sensing, and collision avoidance. With recent advances in corresponding
areas, those capabilities can be integrated into micro UAVs. The following section
gives an overview of research efforts in building collaborative micro UAVs.
The projects Flying Gridswarms and UltraSwarm [6, 11], both carried out at
the University of Essex, investigated the flocking of a group of MAVs (Micro or
Miniature Aerial Vehicles) for the purpose of solving tasks by making use of the
unique advantages of swarms. While Flying Gridswarms used a fixed wing platform,
UltraSwarm aimed at building an indoor flocking system using small co-axial rotor
helicopters. The key idea is using biologically inspired rules of group behaviour
(flocking) to enable a group of UAVs to control its own motion. The swarm members
wirelessly network to form a single powerful computing resource.
The chosen aerial platform for the UltraSwarm project was an off-the-shelf model
helicopter. Due to their low costs swarms can be built at reasonable costs. The
platform was fitted with an onboard computer and a miniature wireless video camera.
To compensate for the additional weight it was necessary to upgrade the motors and
batteries.
The ongoing μDRONES (Micro Drone autonomous navigation for environment
sensing) project [10], funded by the European Commission under the 6th Frame-

---
**[Page 5]**

J Intell Robot Syst (2011) 61:339–353
343
work Programme, aims at developing a small size UAV designed for autonomous
inspection and survey tasks in urban area. The core of the project is focused
on the development of software and hardware modules providing autonomy to a
small size drone in terms of navigation, localization and robustness to unexpected
events. Key research areas are the development of a mission control system with
an intuitive human-machine interface, the development of perception and command
algorithms allowing a more efficient flight autonomy and development of a micro
UAV prototype.
The MIT (Massachusetts Institute of Technology) project RAVEN (Real time
indoor Autonomous Vehicle test ENvironment) [14, 15] primarily deals with the
research on automated supervision systems for autonomous swarms. To allow multi-
day autonomous system operations software-agent health management techniques
are being developed to increase the reliability of autonomous systems. The coor-
dination of the single swarm members is supported and their state is supervised.
The aim is to create an adaptable management system that can react to changes
and that is able to avoid or solve problems. An indoor test bed was created that
allows operating several UAVs and UGVs autonomously in a swarm. It provides a
defined surrounding in which algorithms and system components can be validated.
The swarm logic is implemented on ground-based computers. Position control is
done visually through an external camera system.
The AirShield project (Airborne Remote Sensing for Hazard Inspection by
Network Enabled Lightweight Drones) [1, 2], which is part of the national secu-
rity research program funded by the German Federal Ministry of Education and
Research (BMBF), focuses on the development of an autonomous swarm of micro
UAVs to support emergency units and improve the information basis in case of huge
disasters. The aim is to detect potentially leaking CBRNE-contaminants in their
spatial extent and to carry out danger analysis with the help of these data without
endangering human life. The swarm is supported by a highly flexible communication
system, which allows communication between the swarm members and between the
swarm and the ground station.
The focus of SUAAVE (Sensing, Unmanned, Autonomous Aerial VEhicles) [13]
lies in the creation and control of swarms of helicopter UAVs that are individually
autonomous but collaboratively self-organize. The project investigates the principles
underlying the control of clouds of networked resource-limited UAVs that are
targeted towards achieving a global objective in an efficient manner.
While Flying Gridswarms and UltraSwarm suffer from the limitations of the
chosen aerial platform, our approach is based on highly reliable and expandable
UAVs. Whereas μDRONES focuses on the platform and autonomous navigation
of a single UAV, we look at the operation and collaboration of a group of UAVs.
The project RAVEN shows promising results and has progressed very far. It regards,
however, a pure indoor test bed and, hence, possesses a rather academic character.
By the use of a commercial off-the-shelf flight platform and the orientation towards
a realistic scenario, the AirShield project is very promising and also showed first
results. However the application possibilities are strongly limited by the focus on
only one predefined mission type. SUAAVE follows an approach similar to ours.
Their project is still at an early stage, though.

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

344
J Intell Robot Syst (2011) 61:339–353
4 Platform
The development of our UAV swarm is based on a modified commercial flight
platform and a self-made ground control station. The following sections describe
these two elements of the platform.
4.1 Flight Platform
A lot of effort has been put into the selection of the flight platform. A platform that
already comes with a range of sensors, an advanced control system and autonomous
flight features significantly reduces the effort necessary to realize a cooperative
swarm of micro drones. Furthermore, when it comes to flying autonomously, the
system has to be highly reliable and possess sophisticated safety features in case of
malfunction or unexpected events.
Other essential prerequisites are the possibility to add new sensors and payloads
and the ability to interface with the UAV’s control system in order to allow
autonomous flight. A platform that fulfils these requirements is the quadrocopter
AR100-B by AirRobot (see Fig. 2). It can be both controlled from the ground control
station through a command uplink and by its payload through a serial interface. The
latter feature was used to realize autonomous navigating (see Section 5).
4.2 Ground Control Station
The ground control station developed by Fraunhofer IOSB within the project AM-
FIS [8] is an adaptable prototype system for managing sensor data acquisition with
stationary sensors, mobile ad hoc networks, and mobile sensor platforms (Fig. 3). The
main tasks of the ground control station are to work as an ergonomic user interface
and a data integration hub between multiple sensors possibly mounted on moving
platforms such as micro UAVs, ground vehicles or underwater vessels, and a super-
ordinated control centre. The system includes means to control different mobile
platforms (among them the AirRobot quadrocopters) to direct those to potentially
interesting locations in order to cope with large or no prior sensor equipped areas.
Through its generic design the system is able to link with a wide range of sensors,
and can be equipped with electric-optical or infrared cameras, with movement
dispatch riders, acoustic, chemical or radiation sensors depending on the opera-
tional aim. The AMFIS system is scalable and can be extended to any number
Fig. 2 A quadrocopter serves
as flight platform

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

J Intell Robot Syst (2011) 61:339–353
345
Fig. 3
A modular ground control station serves as integration platform for various sensors and
sensor carriers
of workstations. Due to this fact several sensor platforms can be coordinated and
controlled at the same time. The most different sensor platforms can be handled in
a similar manner by a standardized pilot’s working station that in turn minimizes the
training expenditure of the staff and raises the operational safety. The user interface
is automatically adapted according to the sensor or sensor platform at hand.
Data fusion belongs to the most important tasks of a multi sensor system. Without
merging the data from different sensors the use of such a system is very limited.
Linking data of sensors that complement each other can generate an entire situation
picture. All information gathered during the operation is immediately available to
the crew of the ground control station in which a GIS-supported, dynamic situation
representation plays a central role. At the same time all received data is archived
and stored into databases, e.g. a CSD (Coalition Shared Data) [4] or SSD (SOBCAH
Shared Data) [3]. This serves the perpetuation of evidence and allows an additional
subsequent analysis of the events.
The open interface concept supports the integration of AMFIS in existing security
systems so that data can be exchanged on a real-time basis with other guidance,
supervision or evaluation systems. Mission planning, manual and automatic vehicle
guidance, sensor control, local and temporal linking (coalescence) of sensor data,
the coordination of the people on duty, reporting and the communication with
the leading headquarters in the situation center belongs to the other tasks of a
reconnaissance system. Combination of sensor events and appropriate actions are
implemented by predefined rules with an easy to use production system.
The user interface of the ground control station at Fraunhofer IOSB consists of
three workstations (Fig. 4). Basically, the system is designed that each display can be
used to interact with each function allocated by AMFIS. The standard setup consists

---
**[Page 8]**
*(This page contains a figure/chart/image not captured in text)*

346
J Intell Robot Syst (2011) 61:339–353
Fig. 4
Ground control station at Fraunhofer IOSB
of two workstations for one operator each, and one situation awareness display in
between that supports both operators. The duties of the two operators can be divided
into sensor and vehicle control, called pilot working place, and data fusion, archiving,
exploitation and coordination tasks.
The user interface of the latter working place primarily provides a function for
the visualization of sensor data streams. Therefore the operator gains access to
the accumulated data. His task is to obtain and keep an overview of the situation
and to inform the higher authorities about important discoveries and provide the
associated data so that external systems or personnel can utilize that information.
It is incumbent on him to mark important data amounts and to add additional
information when necessary. Furthermore he is the link to the pilot and coordinates
and supports the pilot in his work. The analyst as well as the pilot relies on the central
geographical information system-supported situation representation that provides an
overview of the whole local situation. The geographical relation is established here
and the situation and position of the sensors and sensor platforms can be visualized.
This includes for example the footprints of cameras or the position and heading of
UAVs or UGVs.
The pilot’s workstation is designed to control many different sensor platforms.
It is not clear from the start which sensor platforms will be used in the future and
it is also not clear which situation information will be provided by the different
systems or which information is needed to control the future platforms in a proper
way. For this purpose the pilot workstation provides a completely adaptable user
interface which allows selectively activating or deactivating the required displays. An
artificial horizon for example is completely useless in order to control a stationary
swiveling camera but very helpful for controlling an airborne drone. The surface
can be adapted to the particular circumstances and is configurable for a wide range
of standard applications. No matter what sensor platform the user is currently
controlling or supervising, the task is the same. He does not have to switch between
different proprietary control stations. The user interface is identical except for
individual volitional or necessary adaptations.

---
**[Page 9]**
*(This page contains a figure/chart/image not captured in text)*

J Intell Robot Syst (2011) 61:339–353
347
5 Towards Autonomy
In order to enable the UAVs to navigate autonomously, some enhancements to the
AirRobot quadrocopters had to be made. Furthermore, a framework to implement
cooperation strategies was necessary.
5.1 UAV Control Hardware
To allow a high degree of autonomy, the quadrocopter should be controlled by
a processing unit that is carried as a payload. Due to space, weight and power
constraints of the payload, this module has to be small, lightweight and energy-
efficient. On the other hand, a camera as sensor system should not be left out.
An elegant solution is the use of a “smart” camera, i.e. a camera that not only
captures images but also processes them. Processing power and functionalities of
modern smart cameras are comparable to PCs. Even though smart cameras became
more compact in recent years, they usually still are too heavy to be carried by
a quadrocopter such as the AR100-B. In most applications, smart cameras are
stationary where their weight is of minor importance. However, a few models are
available as board cameras, i.e. without casing and the usual plugs and sockets (see
Fig. 5, left). Thus, their size and weight are limited to a minimum. The camera chosen
has a freely programmable DSP (400 MHz, 3,200 MIPS), a real-time operating
system and several interfaces (Ethernet, I2C, RS232). With its weight of only 60 g
(without lens), its compact size and a power consumption of 2.4 W it is suitable to
replace the standard video camera payload.
The camera can directly communicate with the drone’s controller through a serial
interface. The camera receives and processes status information from the UAV such
as position, altitude or battery power, and is able to take control by sending basic
control commands or GPS waypoints.
A drawback of the board camera is its lack of an analogue video output thus
rendering the quadrocopter’s built-in video downlink useless. Image data is only
available through the camera’s Ethernet interface. To enable communication be-
tween the smart camera and the ground control station, a tiny WiFi module was
integrated into the payload. The WiFi communication link allows to stream live
Fig. 5
A programmable camera module (left) controls the UAV. It has been integrated into a
payload unit (right)

---
**[Page 10]**

348
J Intell Robot Syst (2011) 61:339–353
video images, still shots and status information from the UAV to the ground control
station. Furthermore, programs can be rapidly uploaded to the camera during
operation.
Currently, the so enhanced UAVs are able to perform basic maneuvers, such as
take-off, fly to position, and landing, autonomously. Furthermore, a software module
was implemented, that calculates the footprint of the camera, i.e. the geographic
coordinates of the current field of view. In the future we will also use the camera’s
image processing capabilities to generate further control information to be able
to carry out more complicated flight maneuvers. Important research subjects are
the recognition and avoidance of obstacles (see and avoid), the tracking of moving
objects and the point-exact landing on a defined landing point. As a safety feature,
it is always possible for the operator to override autonomous control and take over
manually.
5.2 Communication Infrastructure
For a single UAV communication usually consists of two dedicated channels, an
uplink channel for control commands and a downlink channel for video and status
information. In present UAVs each of these channels has its own communication
technique in a special frequency band. In complex scenarios that require multiple
UAVs there have to be twice as many RF channels as UAVs used. These channels
are all point-to-point connections which see the other UAVs only as interferer, if at
all. There is no channel between two UAVs; all communication goes via the base
station.
Besides this direct control of UAVs there is a more abstract way which can use
the benefits of an intelligent payload. As input the group of UAVs receives complex
tasks which they will fulfill autonomously. This kind of control however brings the
standard system with up- and downlink to its limits because it poses demands which
cannot be fulfilled with the standard communication:
•
No interference between communication of multiple UAVs (ideally: use of
multihopping)
•
Adding UAVs to the swarm must not require a new RF channel
•
Opening of data channels to transmit the results to the base-station
•
Opening of control channels to transmit any kind of commands to the UAV
•
Sending broadcast messages to all UAVs
•
Opening direct communication channels between UAVs
In addition to the new demands the standard requirements for UAVs still have to
hold:
•
Monitor the status of every UAV in the air
•
Manual control of every UAV as fallback function
To fulfill these needs the (video-) downlink is replaced by a module capable of using
networking communications. In our prototype we use a WiFi module because of its
high data rates and good range, though other technologies might be feasible, too. The
UAV’s uplink channel is retained as fallback control option in case of an emergency.
With the WiFi network we implemented a communication solution that meets the
demands listed above. This solution differentiates between UAV and base-station,

---
**[Page 11]**
*(This page contains a figure/chart/image not captured in text)*

J Intell Robot Syst (2011) 61:339–353
349
i.e. the ground control station. There is only one base-station within the network. A
base-station monitors the status of every UAV assigned to it. It also acts as gateway
to other system components.
Our communication setup uses four types of channels (cf. Fig. 6):
•
Broadcast channel
a channel which offers random access to every subscriber in the network
•
Control channel
a dedicated channel between a UAV and the base-station to transmit status
information from the UAV and to receive commands from the base-station
•
Data channel
a dedicated channel between UAV and the base-station to send results of task
i.e. images
•
Co-op channel
this channel is opened between two UAVs if one of them needs assistance to
finish a task
5.2.1 Broadcast Channel
The broadcast channel is mainly used for initializing the other channels. If a UAV
is not assigned to a base-station it will look for a base-station on this channel. Also
if a UAV needs assistance to finish a job, e.g. when its battery runs low or it needs
a UAV with another sensor, the UAV calls for assistance on this channel. Through
the broadcast channel it is possible to reach all UAVs with a single message. If a
UAV, for example, detects an obstacle it can inform all other UAVs in the group.
Another main feature of this channel is communicating new tasks. When this task is
transmitted to the whole group instead of a single UAV, the decision, which UAV
best fits the needs for this task, can be done by the group.
Fig. 6
Communication channels between UAVs and base-station

---
**[Page 12]**

350
J Intell Robot Syst (2011) 61:339–353
5.2.2 Control Channel
The control channel is a dedicated channel between a UAV and a base-station. Over
this channel a UAV sends its status as well as an “Alive” Message. With these data
it is possible to monitor the UAVs in the base-station. The second feature of this
channel is a command uplink to the UAV. It can be used to transmit tasks as well as
to configure the UAV. Reconfiguring can be done by changing internal parameters
of the UAV or by uploading new software modules.
5.2.3 Data Channel
The data channel sends results (usually video images) to the base-station. The format
of the data has to be predefined.
5.2.4 Co-op Channel
The co-op channel is opened between two UAVs. If the UAV has a task, which
cannot be done on its own, it seeks a wingman over the broadcast channel. If there
is an idle UAV which can assist a co-op channel is opened between the two drones.
Over this channel the UAV has the possibility to send subtasks to the wingman. After
completion it receives the results over the co-op channel.
Replacing the standard downlink with a networking module is a big step towards
autonomy of each UAV. With this adaptive communication solution it is possible
to set up an expandable network of UAVs. The implemented channels provide
communication links between all subscribers in the net.
5.3 UAV Control Software
A multi-agent system architecture was designed to implement team collaboration.
In this framework, the individual entities in a team of UAVs are represented by
software agents. The agents implement the properties and logic of their physical
counterparts.
An agent is “...any entity that can be viewed as perceiving its environment through
sensors and acting upon its environment through effectors” [12]. Incorporating that
“An agent is a computer system, situated in some environment, that is capable of
flexible autonomous action in order to meet its design objectives” [7], a multi-agent
system seems to perfectly meet the challenges of realizing an intelligent swarm of
autonomous UAVs.
Software agents are computational systems that inhabit some complex dynamic
environment, sense and act autonomously in this environment, and by doing so,
realize a set of goals or tasks for which they are designed [9]. Hence, they meet the
major requirements for a suitable architectural framework: to support the integration
and cooperation of autonomous, context-aware entities in a complex environment.
The agent-based approach allows a natural system modelling approach facilitating
the integration of flight platforms, sensors, actuators and services. The core-agents of
the multi-agent system presented in this paper are based on the following three agent
classes:
•
Teamleader Agent: A team leader agent controls a group of agents consisting
of at least one agent. It coordinates higher tasks and assigns sub-tasks to team

---
**[Page 13]**
*(This page contains a figure/chart/image not captured in text)*

J Intell Robot Syst (2011) 61:339–353
351
members. A team leader is always aware of the positions and capabilities of all
team members. A team leader itself can be controlled by a superordinate team
leader.
•
Copter Agent: A copter agent represents an individual drone and models the
general characteristics of a quadrocopter. Each copter agent is assigned to a team
leader on initialization. The corresponding team leader agent can access status
data of the copter agent, such as the drone’s current position.
•
Sensor Agent: A sensor agent represents a sensor and is assigned to a copter
agent. It implements the properties of the corresponding sensor.
Concrete implementations of these abstract classes are realized by combining a
copter agent with a sensor agent. For example, an IR-Camera-Copter agent rep-
resents a quadrocopter with an infrared camera. It is an aggregation of a copter
agent and an IR-Camera agent. Both agents implement the concrete properties of
the entities they represent.
Furthermore, a Communication Agent is responsible for the communication
between agents. It implements the underlying communication protocol and network
settings.
6 Simulation and Evaluation
In order to assess different cooperation strategies for teams of UAVs, a simulation
tool has been developed. Modeling and visualization of scenarios was done using a
computer game engine with corresponding editing tools. An interface to the engine
has been implemented. It allows full control of the implemented entities as well as
feedback from the virtual world.
An example scenario that simulates an intrusion has been realized (see Fig. 7).
Besides the UAVs and the actors in the scenario, also sensors have been modeled.
Different kinds of sensors such as motion detectors, cameras, ultra sonic or LIDAR
Fig. 7 A simulation
environment for evaluation of
cooperation strategies

---
**[Page 14]**
*(This page contains a figure/chart/image not captured in text)*

352
J Intell Robot Syst (2011) 61:339–353
Fig. 8
A first swarm up in the air
(light detection and ranging) sensors can be modeled with their specific characteris-
tics. The simulation tool can determine if an object lies within the range of a sensor.
This helps evaluate and optimize the use of different sensing techniques.
The intelligence of team members is implemented in software agents as described
in the previous section. They interface with the simulation engine using the same
control command interface as the actual quadrocopters. That way, the simulation
can be transferred to the real world without changes to the agents (Fig. 8).
7 Conclusion and Future Work
Forming teams of micro UAVs opens up a vast array of new application fields.
However, the coordination of multiple drones requires advanced control strategies
and an extended degree of autonomy of the individual UAVs.
Our approach is to equip commercial micro drones with “smart” cameras that
control the UAVs. The drones are integrated into a modular sensor network whose
central part is an adaptable ground control station. An adaptive communication
infrastructure has been presented that provides communication links between all
drones and the ground control station.
Currently, we use a simulation tool to test and evaluate different team collabora-
tion strategies, sensor techniques, as well as collision avoidance and path planning
algorithms. In the future, we will raise the level of autonomy by implementing vision
algorithms on the camera. Possible capabilities range from tracking of objects to the
detection of suspicious behavior.
Additionally we will transfer the up to now in the simulation validated collab-
oration strategies into the real world. The technical adaptations for this are far
progressed. The proof of the functionality of the developed agent-based swarm under
real conditions is still pending.
Acknowledgements
The work presented in this paper was partially funded by the Fraunhofer
Gesellschaft. The authors would like to thank their colleagues and students for their contribution, es-
pecially Sandro Leuchter, Thomas Partmann, Sven Müller, Martin Grzesiak, Christian Großkinsky,
and Constantin Leue.

---
**[Page 15]**

J Intell Robot Syst (2011) 61:339–353
353
References
1. Daniel, K., Dusza, B., Lewandowski, A., Wietfeld, C.: AirShield: a system-of-systems MUAV
remote sensing architecture for disaster response. In: IEEE International Systems Conference
(SysCon). Vancouver (2009)
2. Daniel, K., Dusza, B., Wietfeld, C.: Mesh network for CBRNE reconnaissance with MUAV
swarms. In: 4th Conference on Safety and Security Systems in Europe. Potsdam (2009)
3. Essendorfer, B., Monari, E., Wanning, H.: An integrated system for border surveillance. In: Ege,
R. (ed.) ICONS 2009: The Fourth International Conference on Systems, 1–6 March 2009. Gosier,
Guadeloupe/France (2009)
4. Essendorfer, B., Müller, W.: Interoperable sharing of data with the Coalition Shared Data (CSD)
server. In: North Atlantic Treaty Organization (NATO)/Research and Technology Organization
(RTO): C3I in Crisis, Emergency and Consequence Management (2009)
5. Frost & Sullivan: Advances in platform technologies for unmanned aerial vehicles. Technical
Insights Report D1B0, San Antonio, TX (2009)
6. Holland, O., Woods, J., De Nardi, R., Clark, A.: Beyond swarm intelligence: the ultraswarm. In:
Proceedings of the IEEE Swarm Intelligence Symposium (SIS2005) (2005)
7. Jennings, N.R., Sycara, K., Wooldridge, M.: A roadmap of agent research and development.
Auton Agent Multi-Agent Syst 1(1), 7–38 (1998)
8. Leuchter, S., Partmann, T., Berger, L., Blum, E.J., Schönbein, R.: Karlsruhe generic agile ground
station. In: Beyerer J. (ed.) Future Security. 2nd Security Research Conference, 12th–14th
September 2007, Karlsruhe, Germany. Fraunhofer Defense and Security Alliance, pp. 159–162.
Universitätsverlag, Karlsruhe (2007)
9. Maes, P.: Agents that reduce work and information overload. Commun. ACM 37(7), 30–40
(1994). ISSN 0001-0782
10. The μDRONES Project: http://www.ist-microdrones.org (2010)
11. De Nardi, R., Holland, O., Woods, J., Clark, A.: Swarmav: A swarm of miniature aerial vehicles.
In: Proceedings of the 21st Bristol International UAV Systems Conference (2006)
12. Russell, S.J., Norvig, P.: Artificial Intelligence: A Modern Approach. Prentice Hall, ISBN
9780137903955 (2003)
13. Teacy, W.T.L., Nie, J., McClean, S., Parr, G., Hailes, S., Julier, S., Trigoni, N., Cameron, S.:
Collaborative sensing by unmanned aerial vehicles. In: Proceedings of the 3rd International
Workshop on Agent Technology for Sensor Networks. Budapest, Hungary (2009)
14. Valenti, M., Bethke, B., Daniel, D., How, J.P., Vian, J.: The MIT indoor multi-vehicle flight
testbed. In: Proceedings of the IEEE International Conference on Robotics and Automation,
2007, Roma, Italy (2007)
15. Valenti, M., Bethke, B., Fiore, G., How, J., Feron, E.: Indoor multi-vehicle flight testbed for fault
detection, isolation, and recovery. In: AIAA Conference on Guidance, Navigation and Control,
August 2006, Keystone, CO, AIAA-2006-6200
16. The VisiBuilding program: http://www.darpa.mil/sto/programs/visibuilding/ (2010)
