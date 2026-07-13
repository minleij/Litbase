# Pechel-On the HumanMachine Interaction of Unmanned Aerial System Mission Specialists

*Source file: Pechel-On_the_HumanMachine_Interaction_of_Unmanned_Aerial_System_Mission_Specialists.pdf — 10 pages*


---
**[Page 1]**

IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 43, NO. 1, JANUARY 2013
53
On the Human–Machine Interaction of Unmanned
Aerial System Mission Specialists
Joshua Michael Peschel, Member, IEEE, and Robin Roberson Murphy, Fellow, IEEE
Abstract—This paper surveys the human–machine interaction
technologies supporting the Mission Specialist role in unmanned
aerial systems (UASs). The Mission Specialist role is one of three
formal human team member roles extracted from the UAS-related
literature (the others are Flight Director and Pilot), but unlike the
Pilot role, the interface needs have not been established. The in-
terfaces used by 17 micro, small, medium altitude long endurance
(MALE) and high altitude long endurance (HALE) platforms are
examined to determine 1) what type of user interface technologies
are present and/or available; 2) how the Mission Specialist cur-
rently or could interact with the user interface technology; and
3) what are the perceived positive and negative aspects of this
user interface technology in the context of the UAS human–robot
team roles. Micro and small UAVs pose signiﬁcant user interface
limitations for the Mission Specialist role and may produce unin-
tentional interaction conﬂicts between the Mission Specialist role
and the Pilot, potentially resulting in suboptimal performance and
loss of robustness. The survey is expected to serve as a reference
for future design and reﬁnement of user interfaces for UAS and a
foundation for better understanding human–robot interaction in
UAS.
Index Terms—Aircraft display human factors, user interface
human factors.
I. INTRODUCTION
T
HIS paper surveys the state of understanding and human–
machine interaction (HMI) practices of the role of the
human Mission Specialist in collecting mission data with an
unmanned aerial system (UAS). The UAS has recently expe-
rienced signiﬁcant technological advancement and permeation
into a myriad of modern domains [1], [2], especially military
and various search and rescue operations [3]–[6]. UAS opera-
tional integration is expected to continue due to the advantages
of human safety [7], [8], clandestine capabilities [9], [10], re-
mote access [11], [12], and high spatial resolution information
retrieval [13], [14].
Manuscript received June 14, 2011; revised August 20, 2012, accepted
August 29, 2012. Date of current version December 21, 2012. This work
was supported by the National Science Foundation under Grant IIS-1143713,
EAGER: Shared Visual Common Ground in Human–Robot Interaction for
Small Unmanned Aerial Systems. This paper was recommended by Associate
Editor T. Busch of the former IEEE Transactions on Systems, Man and Cyber-
netics, Part C: Applications and Reviews (2011 Impact Factor: 2.009).
J. M. Peschel is with the Department of Civil and Environmental Engineer-
ing, University of Illinois at Urbana-Champaign, Urbana, IL 61801-2352 USA
(email: peschel@illinois.edu).
R. R. Murphy is with the Center for Robot-Assisted Search and Rescue,
Department of Computer Science and Engineering, Texas A&M University,
College Station, TX 77843-3112 USA (email: murphy@cse.tamu.edu).
Color versions of one or more of the ﬁgures in this paper are available online
at http://ieeexplore.ieee.org.
Digital Object Identiﬁer 10.1109/TSMCC.2012.2220133
All UAS operations involve a human–robot team [15]–[18],
[21] and, thus, require HMI for better interfaces and for fun-
damental concerns such as reducing the human–robot ratio,
managing team organizational complexity, and increasing team
performance. For the purposes of this discussion, the UAS is de-
ﬁned as vehicle plus the human personnel primarily responsible
for UAS ﬂight, navigation, and acquisition of mission-related
information and will exclude consumers of information with-
out direct control over the payload or platform (referred to as
“knowledge workers” in [22]). Human team members may be
colocated with the unmanned aerial vehicle (UAV) platform or
at a remote location, and, depending on the type of UAV and
mission, can vary in number. Additionally, human team member
functional roles may overlap.
HMI research, which is a subcategory of traditional human
factors research [20], for speciﬁc UAS human team roles does
not appear in the literature, presenting a challenge for design-
ers and developers working with current and future unmanned
systems. The HMI knowledge void is a barrier to reducing the
human–robot crewing ratio through merging human team roles
and increasing UAV autonomy [23]–[25], increasing the number
of UAVs in a single UAS [26]–[28], and making UAS smaller,
more mobile, and available to more diverse domains [29], with-
out ﬁrst understanding how human team roles are actually inter-
acting. As Hobbs [30] points out, there have been no human fac-
tors analyses published on any mobile interfaces for unmanned
systems.
This study surveys the Mission Specialist role in UAS human–
robot teams appearing in over 40 papers covering 17 ﬁelded
systems, identifying the hardware and software interfaces. Re-
search and development to improve the HMI of UAS has largely
focused on ﬂight and navigation, i.e., the pilot role [31], [32]. An
HMI approach to support the acquisition of data and mission-
related information remains less well developed [30], [33], par-
ticularly for small-scale UAVs [34].
The remainder of this paper is organized as follows.
Section II provides an overview of UAS, including UAV op-
erational speciﬁcations and human-team roles described in the
literature. Section III gives a literature review of the hardware
and software interfaces currently used by the Mission Specialist
role in UAS human–robot teams. Section IV presents the HMI
ﬁndings for the UAS Mission Specialist role from the literature.
Finally, Section V presents the conclusions and future directions
for this paper. The work is expected to 1) serve as an introduc-
tion to UASs for HMI researchers; 2) a reference document for
unmanned system designers and developers; and 3) contribute
to a better understanding of human–robot interaction in UAS
(and in any robot being used for real-time data collection) by
identifying the human–machine interfaces used in practice.
2168-2291/$31.00 © 2012 IEEE
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:19:19 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 2]**
*(This page contains a figure/chart/image not captured in text)*

54
IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 43, NO. 1, JANUARY 2013
TABLE I
CLASSIFICATIONS OF SELECTED UAVS CURRENTLY IN OPERATION1
II. UNMANNED AERIAL SYSTEM HUMAN–ROBOT TEAMS
The survey will describe interfaces based on the category
of UAV and the role; the background is given here. UAVs are
divided into based on size, payload weight capacity, range, alti-
tude, and endurance. Three roles appear in the literature: Flight
Director, Pilot, and Mission Specialist.
A. Categories of Unmanned Aerial Vehicles
The composition of a UAS human–robot team depends
largely on the complexity of the UAV itself [35]. Therefore,
it is useful to provide a summary classiﬁcation framework of
UAVs. This paper will use the four-category classiﬁcation sys-
tem employed by the U.S. Air Force [36], [37], Army [38],
and Navy and Marine Corps [39]: micro, small, medium alti-
tude long endurance (MALE), and high altitude long endurance
(HALE). The categories are shown in Table I. It is noted that
for the purposes of this study, focus is restricted to subsonic and
suborbital UAVs.
Micro UAVs represent the smallest physical size, operational
range (distance of travel), altitude (elevation above ground or
sea level), and endurance (time of operation) of all UAVs, and
it is the vehicle type most commonly available for commercial
and civilian operations, such as wilderness and urban search
and rescue. Micro UAVs allow a human team, which is usually
colocated, to remotely navigate and visualize information in
environments where, for example, humans or other ground-
based robots are not practical. UAVs in the micro category are
traditionally of a rotor- or ﬁxed-wing design.
Small UAVs expand upon the operational range, altitude, and
endurance of the human–robot team without a signiﬁcant change
in the physical size of the vehicle. This would be important, for
example, to onsite military combat units who will colocate with
the vehicle, but need to maintain a large displacement distance
for reconnaissance operations. Increased levels of autonomy
are also found in small UAVs. One of the main differences in
terms of HMI between micro and small UAVs, besides an im-
provement in operational characteristics, is the dominance of
ﬁxed-wing vehicles and the increased payload weight capac-
ity for small UAVs; very few rotor-based vehicles have been
developed with small UAV (or higher) operational parameters.
MALE UAVs possess a signiﬁcantly larger endurance than
small UAVs and increased mission complexity. Consequently,
the size of the MALE vehicles also dramatically increases. The
increase in vehicle size permits a signiﬁcantly larger payload
weight capacity, which may consist of not only reconnaissance
sensor technology, as well as the ability to transport and re-
motely deliver munitions to identiﬁed targets. MALE UAVs are
typically not colocated with their primary human teams, as they
may require more specialized service and maintenance, as well
as more formal takeoff and landing areas.
HALE UAVs represent the largest and most complex UAVs
that have been developed to date. HALE UAVs mirror many of
the operational characteristics of modern manned military air-
craft in terms of their range, altitude, and endurance. The main
difference between MALE and HALE UAVs, besides opera-
tional characteristics, is the size of the vehicle and the associated
increased payload weight capacity.
B. Unmanned Aerial System Human Team Role Descriptions
There exists a diversity of human team role nomenclature
in the literature across the four UAV categories [16], [18], [19],
[23], [35], [41], [42]. However, certain human team member role
trends are identiﬁable and, generally, fall into one of three role
categories: Flight Director, Pilot, and the Mission Specialist.
These three role labels represent a synthesis from the literature
and are given in this paper to describe general role function
rather than preferred role identiﬁcation within any speciﬁc UAS.
A human team member role survey from the current literature
is provided for each of the four UAS groups (see Table II).
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:19:19 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 3]**
*(This page contains a figure/chart/image not captured in text)*

PESCHEL AND MURPHY: ON THE HUMAN–MACHINE INTERACTION OF UNMANNED AERIAL SYSTEM MISSION SPECIALISTS
55
TABLE II
HUMAN TEAM CHARACTERISTICS FOR THE FOUR GROUPS OF UASS
1) Flight Director: The Flight Director role is held by one
or more human team members responsible for directing the
mission and is described independently in [16], [18], [23], [41],
and [42]. Murphy et al. [18] deﬁne the role of a micro UAV
team Flight Director as the individual responsible for overall
safety of the team members (human and UAV). The Flight Di-
rector is in charge of mission situational awareness and has
the authority to terminate the operation at any point. Cooper
and Goodrich [23] describe for a micro UAV team, an Incident
Commander, who is solely in charge of managing the search ef-
fort. For the small UAV category, Oron-Gilad and Minkov [41]
ethnographically describe a Team Commander role. Serving as
the head of the human–robot team, the commander may com-
municate with other small UAV human–robot teams in the ﬁeld
or control stations and, in addition, monitor the technical condi-
tion of the vehicle. More complex situations described did arise
requiring an additional individual, a Mission Commander (MC),
to join the team in order to focus only on strategy and coordi-
nation. In the MALE UAV category, Cooke et al. [16] deﬁne
the role of a Data Exploitation, Mission Planning and Com-
munications Operator (DEMPC). This team member is solely
responsible for planning the actual mission as well as functions
as the navigator during the operation. Weeks [42] describes the
(MC) as generally the most senior member of the human team,
all of which are usually trained as Air Vehicle Operators (AVOs).
For HALE UAVs, Weeks [42] describes a more distributed com-
mand structure for a Global Hawk UAV operation. Here, an MC
is present for operation supervision and decision-making, but
there is an additional Mission Planner (MP) role that would be
responsible for developing the ﬂight plan.
2) Pilot: The degree to which one or more individuals is
responsible for ﬂight control activity varies. Murphy et al. [18]
deﬁne the role of a micro UAV Pilot as responsible for the vehi-
cle within line of sight, while Cooper and Goodrich [23] extends
the micro UAV Pilot role to include both aviation and naviga-
tion. Murphy et al. [18] indicate that the Pilot is responsible for
the general airworthiness of the UAV prior to and during ﬂight
and addresses maintenance issues of the vehicle. For the small
UAV category, higher levels of vehicle autonomy come into
play and the formal pilot role may transition to a separate offsite
operations control center. Oron-Gilad and Minkov [41] provide
detail on a Field Operator role that gives input as needed regard-
ing where the vehicle should ﬂy; however, this role appears to
have limited ﬂight control and navigation input capabilities. The
role of a MALE UAV pilot, as described by Cooke et al. [16],
is the AVO—the individual who ﬂies the UAV and is in control
of its heading, altitude, and airspeed. Cooke et al. also indicate
a navigation role overlap with their DEMPC, but it is noted
that the DEMPC does not participate with any actual piloting
duties. Weeks [42] also deﬁnes an AVO role that serves as an
internal pilot, controlling the MALE UAV from takeoff to land-
ing. When the MALE UAV enters autonomous mode, the AVO
monitors ﬂight and occasionally controls the vehicle during data
collection. In the HALE UAV category, Weeks [42] provides a
description of a Command and Control Operator (CCO). The
CCO, who is usually a trained pilot, is responsible for ﬂight
following, fault diagnosis, and mission monitoring.
3) Mission Specialist: The Mission Specialist is the team
member responsible for visual investigation and recording and,
in more advanced vehicle systems, delivery of an onboard pay-
load. It is a synthesis of roles observed by the authors in [16],
[18], [19], [23], [35], [41], and [42]. The Mission Specialist role
has two interesting components: the responsibility of the role
and the location of the role holder.
Murphy et al. [18] deﬁne the role of a micro UAV Mission
Specialist as a single human team member solely in charge of
collecting reconnaissance data, while Cooper and Goodrich [23]
denote a similar role as the Sensor Operator (SO) who directs
a gimbaled camera for scanning and imagery analysis. Micro
UAV mission-related activities include viewing the real-time
video output from the UAV camera, directing the Pilot for re-
connaissance, and adjusting the UAV camera settings for opti-
mal image capture. In the small UAV group, Oron-Gilad and
Minkov [41] describe an Operator role that is responsible for
looking at speciﬁc areas and targets to evaluate the occupancy
status of enemy troops and is focused on reconnaissance and the
tactical aspects of the UAV mission. Cooke et al. [16] deﬁne for a
MALE UAV system, the Payload Operator (PLO), whose main
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:19:19 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

56
IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 43, NO. 1, JANUARY 2013
TABLE III
REFERENCE SUMMARY OF HARDWARE-BASED HMI USED BY A MISSION SPECIALIST ROLE ON A UAS HUMAN–ROBOT TEAM
responsibility is to control the reconnaissance camera settings
and capture imagery. Weeks [42] describes three individual roles
that fall under the Mission Specialist classiﬁcation. The Primary
DEMPC Operator identiﬁes target sequences and best collec-
tion methods for the UAV. The second role, which is the SO, is
responsible for optimal sensor selection and target acquisition,
and carries out the directions of the DEMPC. A third ancillary
Mission Specialist-like role is described for a Synthetic Aper-
ture Radar (SAR) Operator, who is responsible solely for SAR
image capture and target identiﬁcation. In the case of HALE
UAV team roles, Weeks [42] indicates the presence of an image
quality control technician, however, does not elaborate nor re-
port information regarding other roles (e.g., DEMPC, SO, SAR,
etc.) on the human team. Others have implied that for HALE
UAVs, the Mission Specialist role may be present in some form
on a mission-speciﬁc basis [19], [35].
Regarding human team operation, two distinct categories of
UAS that are observed are: 1) onsite and 2) offsite. An onsite
UAV (micro and small) can generally be transported with the
human team for complete launch, control, and landing by the
human team. An offsite UAV (MALE and HALE) cannot be
transported with the human team; transport, launch, control,
and landing are done primarily via other persons at a separate
location. In the case of an onsite UAV, there are two categories
of human teams involved with a given mission: 1) active and 2)
passive. Onsite active human teams (micro and small) control
all aspects of the UAV in the ﬁeld. Onsite active team roles may
overlap. Onsite passive human teams (MALE and HALE) in
the ﬁeld tend to only interact with the UAV for activities such
as taking reconnaissance imagery, adjusting navigation, etc. For
onsite passive human teams, roles tend not to overlap. Offsite
human teams (MALE and HALE) tend to exclusively involve
some sort of ground control system (GCS) where team members
have clearly deﬁned roles.
III. UNMANNED AERIAL SYSTEM MISSION SPECIALIST
HUMAN–MACHINE INTERACTION
Seventeen UASs were identiﬁed for which either hardware
or software aspects of human machine interfacing have been
reported in the scientiﬁc or trade literature. These UASs are
examined for how the human team member in the Mission Spe-
cialist role speciﬁcally interacts with the computer technology
available during a UAV mission. The results are synthesized
into ﬁndings in the following section and populate Tables III
and IV.
A. Micro Unmanned Aerial System Mission Specialist
Human–Machine Interaction
The HMI for micro UAS is reported for seven systems. How-
ever, the Mission Specialist HMI is the least well documented
among all UAV categories, which may be due to diverse com-
mercial and civilian applications. Fig. 1 provides an example of
a Mission Specialist interacting with a micro UAV.
Murphy et al. [18] used a Like90 T-Rex rotary-wing micro
UAV in order to survey damage in post-Hurricane Katrina and
post-Hurricane Wilma operations. The Mission Specialist role
observed the real-time video feed from the T-Rex camera on
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:19:19 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 5]**
*(This page contains a figure/chart/image not captured in text)*

PESCHEL AND MURPHY: ON THE HUMAN–MACHINE INTERACTION OF UNMANNED AERIAL SYSTEM MISSION SPECIALISTS
57
TABLE IV
REFERENCE SUMMARY OF SOFTWARE-BASED HMI USED BY A MISSION SPECIALIST ROLE ON A UAS HUMAN–ROBOT TEAM
Fig. 1.
Example of a micro UAS Mission Specialist (Right) interacting with
an AirRobot AR100BUAV (Courtesy of Center for Robot-Assisted Search and
Rescue).
a separate display screen and used independent radio control
hardware for camera positioning. A second study by Murphy
et al. [18] during a separate post-Hurricane Katrina operation in-
volved the use of an iSENSYS IP-3 rotary wing mUAV. Here, the
Mission Specialist role wore a heads-up-display (HUD) for real-
time visualization and utilized radio control hardware for posi-
tioning of the payload camera. In a study on wilderness search
and rescue exercises, Cooper and Goodrich [23] employed the
use of experimental, custom ﬁxed-wing micro UAVs ﬁtted with
a gimbaled camera. The Mission Specialist visualized the video
feeds from the vehicle on a display screen and controlled the
camera settings using independent radio control hardware.
Although not formally studied in the literature, there are sev-
eral commercially available micro UAVs. User interaction with
these vehicles ranges from simple hardware-based radio control
to more sophisticated software-based control interfaces. Sky-
botix Technologies offers the CoaX, a coaxial helicopter capable
of general surveillance through a ﬁxed-mounted onboard cam-
era. An open-source application programming interface (API)
is available to allow for ﬂight control customization by one or
more team members; however, the onboard camera is not con-
trollable [43]. The Parrot AR.Drone is a quad-rotor UAV that
has both ﬁxed forward- and vertical-facing cameras. An open-
source API is also available. The AR.Drone is unique in that it
is controllable only with Apple iOS devices [29].
Larger micro UAVs include the AirRobot AR100B, which is
a quad-rotor micro UAV that includes an interchangeable pay-
load. The Pilot for ﬂight operations uses a hardware control in-
terface that also contains a small display screen that can project
real-time video when a camera is used as a payload. An API is
available for the AR100B for control (both ﬂight and camera)
customization; therefore, a Mission Specialist role could sepa-
rately interact with the vehicle for data gathering purposes on a
separate laptop device [44]. The Draganﬂyer X series of rotor-
based micro UAVs, produced by Draganﬂy Innovations, Inc., is
controlled primarily by a hardware interface with limited touch
screen interaction for ﬂight and navigation. An onboard camera
is also controllable using the same hardware interface, but video
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:19:19 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

58
IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 43, NO. 1, JANUARY 2013
Fig. 2.
Example of a small UAS Mission Specialist interacting with an AeroVi-
ronment Raven UAV (Courtesy of United States Department of Defense).
can be broadcast wirelessly to an HUD or a separate display sta-
tion, thereby allowing a Mission Specialist role the ability to
complete reconnaissance tasks [45]. Aeryon Labs has designed
the Scout, a quad-rotor vehicle with a hot-swappable payload
that may include a gimbaled camera. The Aeryon Scout is ca-
pable of beyond line-of-sight operations and uses exclusively
a touch-based software interface for ﬂight and navigation con-
trol. Real-time video and image data transmission during the
ﬂight is available (to any wireless display device) and a Mission
Specialist role could independently interact with the system to
control the camera and complete reconnaissance tasks using a
customized version of the touch screen interface [46].
B. Small Unmanned Aerial System Mission Specialist
Human–Machine Interaction
The interface technologies for the Mission Specialist role
have greater variety than that of micro UAS, in part because
team members are not always colocated.
Oron-Gilad and Minkov [41] provide two investigations of
combat units utilizing a small UAV during the Second Lebanon
War of 2006. Both studies indicated that the Mission Specialist
role interacted with a handheld touch screen device. Addition-
ally, there was a dedicated tablet laptop docked to the handheld
device. The control panel had traditional hardware setup for
interfacing, including a keyboard, trackball, and combination
mouse/joystick. It was implied that both the Pilot and Mission
Specialist roles had to share the same handheld device to inter-
act with the vehicle. Fig. 2 provides an example of a Mission
Specialist interacting with a small UAV.
Commercially available small UAVs typically come with pro-
prietary user interface technology. The ﬁxed-wing Raven, which
is produced by AeroVironment, has a common GCS that inter-
faces with all of the manufacturer’s UAV systems. The control
device consists of small handheld unit with dual joysticks for
ﬂight and navigation. A single small display screen is located
at the center of the handheld device, allowing for visualization
from onboard cameras. A hardware button-driven menu system
Fig. 3.
Example of a MALE UAS Mission Specialist (Right) interacting with
a General Atomics Predator UAV (Courtesy of United States Department of
Defense).
allows for camera control. Due to the increased level of auton-
omy in this system, the Pilot and Mission Specialist roles over-
lap, leading to a single operator being essentially responsible
for both roles [47]. AAI Corporation produces the ﬁxed-wing
shadow line of small UAVs. As with the Raven, the Shadow
has a portable GCS. Two operators visualize the mission activ-
ities using independent large displays screens. A full keyboard,
joystick, and button pad allows for a Mission Specialist role
to interface with the shadow vehicle [48]. Northrop Grumman
produces the Fire Scout, which is uniquely a large rotor-based
small UAV. Flight and navigation by two operators is accom-
plished through a proprietary control system (CS). Consisting
of four large display screens—two per operator—the CS dis-
plays payload imagery for reconnaissance that would fall under
the purview of responsibilities for the Mission Specialist role.
Interfacing is done through full keyboard, joystick, and button
pad controls [49].
C. MALE and HALE Unmanned Aerial System Mission
Specialist Human–Machine Interaction
The HMIs for MALE and HALE UAS are discussed together
due to operational similarity and the lower count of actual UAVs
across both categories. MALE and HALE UAV Mission Spe-
cialist operations generally rely on satellite communications
and involve some type of GCS that is not colocated with a hu-
man team on the ground, although there are exceptions. Fig. 3
provides an example of a Mission Specialist (right) interacting
with a MALE UAV, which is illustrative of HALE UAV Mission
Specialist interaction as well.
As with small UAVs, MALE and HALE UAV systems nor-
mally come with proprietary user interface technology for com-
mand and control. General Atomics, manufacturer of the Preda-
tor UAVs [50], [51], produces several types of GCS units, rang-
ing from permanent to highly mobile. Interaction by the Mission
Specialist at the GCS would involve one or more video display
screens, a full keyboard, joysticks and mice, and additional
ancillary button pads. General Atomics also produces a remote
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:19:19 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 7]**

PESCHEL AND MURPHY: ON THE HUMAN–MACHINE INTERACTION OF UNMANNED AERIAL SYSTEM MISSION SPECIALISTS
59
video terminal (RVT), which is essentially a rugged laptop de-
vice [52]. A Mission Specialist in the ﬁeld would presumably
have access to and control of real-time onboard camera imagery;
however, Hobbs [30] indicates that, to date, there have been no
human factors analyses published on any laptop-based inter-
faces for UAV systems. General Atomics also produces the Sky
Warrior and Reaper UAVs, which are extended range version
of the Predator UAV [53]. Interfacing by the Mission Specialist
would occur through an RVT and would be expected as similar
to that of the Predator UAV.
One simulation study for larger UAS describes aspects of
HMI. Cooke et al. [16] describe a MALE UAV investigation in
a synthetic task environment (STE). In the STE, a single MALE
UAV operator was positioned in a GCS-like environment with
three large display screens. A full keyboard and mouse were
used for interfacing, as well as a variety of pushbutton consoles.
The Mission Specialist role was responsible for identifying and
photographing targets during the simulation.
IV. UNMANNED AERIAL SYSTEM MISSION SPECIALIST
HUMAN–MACHINE INTERACTION FINDINGS
An analysis of the Mission Specialist role and user interface
technology found across all four groups of UAVs results in three
ﬁndings that the Mission Specialist has dedicated interfaces in
MALE and HALE UAS but not micro and small, MALE and
HALE UAS use software-based interfaces, while micro and
small rely on hardware-based interfaces, and the Mission Spe-
cialist and Pilot roles in micro and small UAS show a high
degree of overlap. The last ﬁnding suggests a technology inter-
action conﬂict that could develop between the Mission Specialist
and Pilot roles for micro and small UAS which would not arise
in the two larger UAS categories. The ﬁndings are based on
Tables III and IV.
Finding 1: The Pilot and Mission Specialist roles have dis-
tinctly different interfaces in all categories of UAS except for mi-
cro and small UAS, where the Mission Specialist either shares
the Pilot-centered display or has a mirrored replica. As seen
in Tables III and IV, there are two categories present for on-
site human teams: 1) Pilot-centered (active), and 2) Mission
Specialist-centered (passive). Pilot-centered technology (micro
and small) tends toward active control of the UAV. Mission
Specialist-centered technology (MALE and HALE) tends to-
ward passive controlling of the camera, taking reconnaissance
imagery, etc. Offsite human teams (MALE and HALE) consis-
tently use two separate control stations at which one (or more)
separate team member can conduct Mission Specialist-related
activities.
Finding 2: Mission Specialists in larger UAS tend to have
more sophisticated software-based interfaces to collect and in-
teract with images and video, while micro and small UAS are
generally limited to hardware-based interfaces. All four groups
of UAS involve some sort of hardware-based interface. In mi-
cro and small UAVs, hardware interfaces dominate. An onsite
active human team Mission Specialist tends to interface more
with hardware-based technology that is designed predominantly
for UAV control and navigation. A micro and small UAV Mis-
sion Specialist mostly uses handheld controllers that control
every aspect of the UAV. In the two smaller groups (micro and
small), the Mission Specialist was more likely to interact with
a limited set of hardware-based input, including only a joystick
and/or a predeﬁned pushbutton panel. The actual HMI involved
for the onsite active human team Mission Specialist, therefore,
may take the form of a simple designated pushbutton system for
camera angling, zoom, and image capture (e.g., the AirRobot
AR100B and DraganFlyer X series). An onsite passive and off-
site human team Mission Specialist tends to interface more with
both hardware-based and software-based interaction technology
that is designed more for Mission Specialist-centered activities.
Most Mission Specialist roles in this category use some sort of
standard computer (i.e., desktop or laptop) that has a design fo-
cus on taking reconnaissance imagery and, possibly, the ability
to make navigation adjustments.
In the two larger groups (MALE and HALE), a Mission Spe-
cialist used the full suite of hardware input devices, including a
joystick, keyboard, mouse, trackball, and some type of ancillary
pushbutton panel. The reasoning behind this is that a micro and
small Mission Specialist is more likely to be in a ﬁeld situation
rather than in a controlled GCS environment. In a GCS-based
operation, there is suitable workspace for a large set of input de-
vices. The added complexity of the MALE and HALE software
environment is also certainly a factor, necessitating a variety of
hardware input capabilities. In a ﬁeld situation, where micro and
small UAVs are colocated, mobility is a highly desired character-
istic and this will obviously reﬂect in the interface technology
UAV systems as there are normally secondary hardware con-
soles or mobile nonﬂight control interface devices available to
the Mission Specialist role; however, some human team member
changeover problems have arisen [30].
Some form of visual display, whether integrated directly into
the hardware controller or located at an adjacent or remote base
station, was present in all four of the UAV groups. For a Mis-
sion Specialist in ﬁeld-type scenarios, displays were generally
similar in dimension (14 in or smaller). In GCS operations,
for the two larger UAV groups, the visual displays were sig-
niﬁcantly larger (all greater than 14 in). Some smaller UAV
systems found (e.g., the iSENSYS IP-3 and the Aeryon Scout)
had HUD capabilities for real-time video feed visualization (al-
though, presumably, any of the UAVs with a standard video
signal output could, in theory, be integrated with commercially
available HUD or other ancillary display technologies). HUD
technologies did not appear to be utilized by the Mission Spe-
cialist role in the two larger UAV classes. This is most likely due
to the nature of the indoor work environment (i.e., controlled
lighting), the large visual display screens available, and fatigue
issues due to the extended nature of MALE and HALE mission
duration.
In terms of the software-based interactions of the Mission
Specialist role, all four groups were found to have at least one
use of static imagery, real-time video, and synthetic overlaying
of mission-related ancillary data, as part of the interfacing. Sim-
ple menu interaction (i.e., hardware driven menus) was found
to be more prevalent in the two smaller UAV groups, while
more complex menu interaction appeared in the higher two tier
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:19:19 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 8]**

60
IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 43, NO. 1, JANUARY 2013
categories. This is due to the greater complexity of interaction
required by the larger systems, as well as ties to the greater vari-
ety of hardware input devices available to the Mission Specialist
role. It should also be noted that platform-independent software
was observed to take into account a greater variety of hardware
inputs [58], [59].
Finding 3: The Mission Specialist role in micro and small
UAS has more overlap with the Pilot role, both in spatial prox-
imity and in coordinating functions, than with larger UAS. The
onsite active human team Mission Specialist found in micro and
small UAS tends to work side by side using a single controller
designed for a Pilot. This type of user interfacing would likely
impose a direct interface interaction conﬂict with the Pilot role.
The existing user interface design necessitates that the Pilot and
Mission Specialist roles overlap, which violates HMI principles
where interfaces are tailored to support distinct roles. For exam-
ple, in close proximity operations, such as urban or wilderness
search and rescue, for example, a Pilot may need to focus solely
on the ﬂight controls and collision avoidance rather than on
Mission Specialist tasks such as taking pictures [18], [23].
V. CONCLUSION
To summarize, three human team member roles (Flight Direc-
tor, Pilot, and Mission Specialist) were observed in all four op-
erational categories of UAS: micro, small, MALE, and HALE.
The current state of HMI practices for the role of the Mis-
sion Specialist responsible for data acquisition was surveyed
for 17 systems. The most signiﬁcant ﬁnding is that the Mis-
sion Specialist and Pilot roles for micro and small UAS, unlike
MALE and HALE UAS, share the Pilot interface. Sharing vi-
olates the HMI principle of dedicated interfaces for distinct
roles and suggests an interface interaction conﬂict that could
develop between the Mission Specialist and Pilot roles in micro
and small UAS leading to suboptimal performance and loss of
robustness.
The Mission Specialist in MALE and HALE UAS had a ded-
icated software or hardware interface but either shared or used
a mirror of the Pilot interface for small and micro UAS. Each
type of HMI technology consisted of an input mechanism and
an output mechanism. Hardware-based inputs included the use
of isotonic joysticks, keyboards, mice, trackballs, pushbutton
panels, and touch screens. Hardware-based outputs involved
heads-up and standard video displays of varying size. Software-
based inputs included both simple and complex menus, while
software-based outputs consisted of aerial imagery, real-time
video, and synthetic overlays. The ability to customize the soft-
ware interface (i.e., an available API) was also observed for
MALE and HALE interfaces.
The user interfaces for MALE and HALE UAS tend to be
software-based (e.g., menus, point-and-click, touch, etc.), while
the micro and small interfaces tend to be hardware-based (e.g.,
joystick, buttons, toggle switches, etc.). This dichotomy may
be because as the size, complexity, and offsite location of
team members in the UAS increase, the enterprise can support
a more complex software-based environment with supporting
hardware-based input devices.
The dichotomy between software- and hardware-based in-
terfaces impacts how the Mission Specialist interacts with the
other UAS roles and overall reliability. The Mission Specialist
role for micro and small UAVs shares the same hardware-based
interface with the Pilot role, essentially choosing highly mo-
bile hardware-based interfaces at the expense of role separation
which HMI principles indicate lead to better performance and
more reliable mission execution.
One danger in comparing interfaces across multiple classes of
UAS is reconciling differences in domains. However, the main
responsibility of the Mission Specialist for all UAS and domains
includes image and video data acquisition for decision-making,
providing a commonality for comparisons.
This survey suggests that more work is needed to create
greater user interface independence and ﬂexibility for the Mis-
sion Specialist role in a micro and smaller UAS. A set of UAS
human interface design recommendations should be developed
and tested to support optimal levels of independence and ﬂex-
ibility. In the future, it is anticipated that UAV technology, es-
pecially in the micro and small categories, will permit more
software-oriented customization for general operation and hu-
man interaction; therefore, understanding how to optimize in-
dividual and team performance through HMI will be important
for increasing performance and reducing manpower in UAS
operations.
ACKNOWLEDGMENT
The authors would like to thank the anonymous reviewers
and Ms. B. Duncan for their helpful suggestions during the
preparation of this paper.
REFERENCES
[1] L. R. Newcome, Unmanned Aviation: A Brief History of Unmanned Aerial
Vehicles.
Washington, DC: AIAA, 2004.
[2] N. J. Cooke and H. K. Pedersen,
“Unmanned aerial vehicles,” in
Handbook of Aviation Human Factors, J. A. Wise, V. D. Hopkin, and
D. J. Garland, Eds., 2nd ed.
Boca Raton, FL: CRC Press, 2009, pp. 18-
1–18-8.
[3] R. R. Murphy, E. Steimle, C. Grifﬁn, M. Hall, and K. Pratt, “Cooperative
use of unmanned sea surface and micro aerial vehicle at Hurricane Wilma,”
J. Field Robot., vol. 25, no. 1–2, pp. 164–180, 2008.
[4] M. A. Goodrich, B. S. Morse, D. Gerhardt, J. L. Cooper, J. Adams,
C. Humphrey, and M. Quigley, “Supporting wilderness search and res-
cue using a camera-equipped UAV,” J. Field Robot., vol. 25, no. 1–2,
pp. 89–110, 2009.
[5] J. A.
Adams,
C. M.
Humphrey,
M. A.
Goodrich,
J. L.
Cooper,
B. S. Morse, C. Engh, and N. Rasmussen, “Cognitive task analysis for
developing unmanned aerial vehicle wilderness search support,” J. Cog-
nit. Eng. Decis. Making, vol. 3, no. 1, pp. 1–26, 2009.
[6] B. T. Schreiber, D. R. Lyon, E. L. Martin, and H. A. Confer, “Impact of
prior ﬂight experience on learning Predator UAV operator skills,” U.S. Air
Force Res. Lab., Dayton, OH, Rep. AFRL-HE-AZ-TR-2002-0026, 2002.
[7] J. Blazakis, “Border security and unmanned aerial vehicles,” U.S. Congr.,
CRS Rep. RS21698, Jan. 2004.
[8] R. M. Taylor, “Human automation integration for supervisory control of
UAV’s,” in Proc. Virtual Media Military Appl. Meet., 2006, pp. 12-1–12-
10.
[9] D.A. Fulghum. (2005, Aug. 15). New technology promises leaps in UAV
warﬁghting capability, Aviation Week [Online]. Available: http://www.
aviationweek.com/aw/generic/story_generic.jsp?channel = awst &id =
news/08155p02.xml&headline=New 20Technology 20Promises 20Leaps
20in 20UAV 20Warﬁghting 20Capability
[10] J. R. Wilson. (2002, Jul.) UAVs and the human factor, Aerospace
America [Online]. Available: http://www.aiaa.org/aerospace/Article.cfm?
issuetocid=233&ArchiveIssueID=28
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:19:19 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 9]**

PESCHEL AND MURPHY: ON THE HUMAN–MACHINE INTERACTION OF UNMANNED AERIAL SYSTEM MISSION SPECIALISTS
61
[11] A. Rango, A. Laliberte, J. E. Herrick, C. Winters, and K. Havstad, “De-
velopment of an operational UAV/remote sensing capability for rangeland
management,” presented at the 23rd Int. Unmanned Aerial Veh. Syst.
Conf., Bristol, U.K., 2008.
[12] L. C. Trost, “Unmanned air vehicles (UAVs) for cooperative monitoring,”
Sandia National Laboratories, Albuquerque NM, Rep. SAND2000-0185,
2000. 2013.
[13] R. C. Hruska, G. D. Lancaster, J. L. Harbour, and S. J. Cherry, “Small UAV-
acquired, high resolution, georeferenced still imagery,” Idaho National
Laboratory, Idaho Falls, Rep. INL/CON-05-00235, 2005.
[14] L. F. Johnson, S. Herwitz, S. Dunagan, B. Lobitz, D. Sullivan, and R. Slye,
“Collection of ultra high spatial and spectral resolution image data over
California vinyards with a small UAV” in Proc. Int. Symp. Remote Sens.
Environ., 2003.
[15] M. J. Barnes, B. G. Knapp, B. W. Tillman, B. A. Walters, and D. Velicki,
“Crew systems analysis of unmanned aerial vehicle (UAV) future job and
tasking environments,” U.S. Army Res. Lab., Adelphi, MD, Rep. TR-
2081, 2000.
[16] N. J. Cooke, H. K. Pederson, O. Connor, J. C. Gorman, and D. Andrews,
“Acquiring team-level command and control skill for UAV operation,”
in Human Factors of Remotely Operated Vehicles, vol. 7, N. J. Cooke,
H. L. Pringle, H. K. Pedersen, and O. Connor, Eds.
Amsterdam, The
Netherlands: Elsevier, 2006, pp. 285–297.
[17] M.A. Goodrich, J. Cooper, J. A. Adams, C. Humphrey, R. Zeeman, and
B. G. Buss, “Using a mini-UAV to support wilderness search and rescue:
Practices for human–robot teaming,” in Proc. IEEE Int. Workshop Safety,
Security, Rescue Robot., Sep. 2007, pp. 1–6.
[18] R. R. Murphy, K. S. Pratt, and J. L. Burke, “Crew roles and operational
protocols for rotary-wing micro-UAVs in close urban environments,” in
Proc 3rd ACM/IEEE Int. Conf. Human-Robot Interaction, Mar. 2008,
pp. 73–80.
[19] M. Nas, “The changing face of the interface: An overview of UAS control
issues and controller certiﬁcation,” Unmanned Aircraft Technol. Appl.
Res. Work. Group 27, 2008.
[20] B. Schneiderman and C. Plaisant, Designing the User Interface: Strate-
gies for Effective Human-Computer Interaction, 5th ed.
Reading, MA:
Addison-Wesley, 2010, p. 4.
[21] C. E. Rash, P. A. LeDuc, and S. D. Manning, “Human factors in U.S.
military unmanned aerial vehicle accidents,” in Advances in Human
Performance and Cognitive Engineering Research, vol. 7, N. J. Cooke,
H. L. Pringle, H. K. Pedersen, and O. Connor, Eds.
New York: Else-
vier, 2006, pp. 117–131.
[22] R. R. Murphy and J. L. Burke, “From remote tool to shared roles,” in
Proc. IEEE Robot. Autom. Mag., vol. 15, no. 4, pp. 39–49, Dec. 2008.
[23] J. Cooper and M. A. Goodrich, “Towards combining UAV and sensor
operator roles in UAV-enabled visual search,” in Proc. 3rd ACM/IEEE Int.
Conf. Human-Robot Interaction, 2008, pp. 351–358.
[24] M. L. Cummings and P. J. Mitchell, “Managing multiple UAVs through
a timeline display,” in Proc. Amer. Inst. Aeronaut. Astronaut. In-
fotech@Aerospace Conf., Sep. 2005.
[25] M. L. Cummings, S. Bruni, S. Mercier, and P. J. Mitchell, “Automation
architecture for single operator-multiple UAV command and control,” Int.
Command Control J., vol. 1, no. 2, pp. 1–24, 2007.
[26] A. Burkle, F. Segor, and M. Kollmann, “Toward autonomous micro
UAV swarms,” J. Intell. Robot. Syst., vol. 61, no. 1–4, pp. 339–353,
2011.
[27] J. G. Manathara, P. B. Sujit, and R. W. Beard, “Multiple UAV coalitions
for a search and prosecute mission,” J. Intell. Robot. Syst., vol. 62, no. 1,
pp. 125–358, 2011.
[28] A. Tsourdos, B. A. White, and M. Shanmugavel, Cooperative Path Plan-
ning of Unmanned Aerial Vehicles.
New York: Wiley, 2011.
[29] Parrot. (2011). Parrot AR.Drone User Guide [Online]. Available:
http://www.parrot.com/fr/support/guidesutilisateur/ar.drone_user-guide_
uk.pdf
[30] A. Hobbs,
“Unmanned aircraft systems,” in Human Factors in Avia-
tion, E. Salas and D. Maurino, Eds., 2nd ed.
New York: Elsevier, 2010,
pp. 505–531.
[31] A. P. Tvaryanas, “Human systems integration in remotely piloted aircraft
operations,” Aviation, Space, Environ. Med., vol. 77, no. 12, pp. 1278–
1282, 2006.
[32] B. Walters and M. J. Barnes, “Modeling the effects of crew size and crew
fatigue on the control of tactical unmanned aerial vehicles (UAVs),” in
Proc. Winter Simul. Conf., 2000, pp. 920–924.
[33] N. J. Cooke and R. A. Chadwick, “Lessons learned from human-robotic
interactions on the ground and in the air,” in Proc. Human-Robot Int.
Future Military Oper., 2010, pp. 355–372.
[34] J. M. Peschel and R. R. Murphy, “Mission specialist interfaces in un-
manned aerial systems,” in Proc. 6th ACM/IEEE Int. Conf. Human-Robot
Interaction, 2011, pp. 225–226.
[35] R. Hopcroft, E. Burchat, and J. Vince, “Unmanned aerial vehicles for
maritime patrol: Human factors issues,” Aus. Def. Sci. Technol. Org.,
Canberra, Australia, Rep. DSTO-GD-0463, 2006.
[36] W. Bierbaum. (1995). “UAVs,” Air and Space Power J. Arch. [Online].
Available: http://www.airpower.maxwell.af.mil/airchronicles/cc/uav.html
[37] United States Air Force, United States Air Force unmanned aircraft sys-
tems ﬂight plan 2009–2047. (2009). [Online]. Available: http://www.
defense.gov/dodcmsshare/brieﬁngslide/339/090723-D-6570C-001.pdf
[38] United States Army, U.S. Army unmanned aircraft systems roadmap
2010–2035. (2010). [Online]. Available: http://www.fas.org/irp/program/
collect/uas-army.pdf
[39] Ofﬁce
of
the
United
States
Secretary
of
Defense,
Unmanned
aircraft system roadmap 2005–2030. (2005). [Online]. Available:
http://www.fas.org/irp/program/collect/uav_roadmap2005.pdf
[40] J. Cooper and M. A. Goodrich, “Integrating critical interface elements for
intuitive single-display aviation control of UAVs,” in Proc. SPIE Defense
Security Symp., 2006, vol. 6226.
[41] T. Oron-Gilad and Y. Minkov, “Remotely operated vehicles (ROVs) from
the bottom-up operational perspective,” in Proc. Human-Robot Int. Future
Military Oper., 2010, pp. 211–227.
[42] J. L. Weeks, “Unmanned aerial vehicle operator qualiﬁcations,” U.S.
Air Force Res. Lab., Dayton, OH, Rep. AFRL-HE-AZ-TR-2000–2002,
2000.
[43] Skybotix Technologies. (2011). CoaX Coaxial Helicopter Product Inf.
Sheet [Online]. Available: http://www.skybotix.com
[44] AirRobot. (2010). AirRobot AR100B Product Inf. Sheet [Online]. Avail-
able: http://www.airrobot-uk.com/air-robot-products.htm
[45] Draganﬂy Innovations, Inc. (2011). Draganﬂyer X Series Product Inf [On-
line]. Available: http://www.draganﬂy.com/industrial/products.php
[46] Aeryon Labs, Inc. (2011). Scout Product Inf. Sheet [Online]. Available:
http://www.aeryon.com/products/avs.html
[47] AeroVironment,
Inc.
(2011).
UAS:
Raven
[Online].
Available:
http://www.avinc.com/uas/small_uas/raven
[48] AAI Textron Systems,
Inc.
(2011). Shadow Tactical
Unmanned
Aircraft Syst. [Online]. Available: http://www.aaicorp.com/products/
uas/shadow_family.html
[49] Northrop Grumman Corporation (2011). Fire Scout Product Inf.
Sheet
[Online].
Available:
url-http://www.as.northropgrumman.com/
products/p6mq8bﬁrescout/index.html
[50] General Atomics Aeronautical Systems Inc. (2011). Predator Prod-
uct Inf. Sheet [Online]. Available: http://www.ga-asi.com/products/
aircraft/predator.php
[51] General Atomics Aeronautical Systems Inc. (2011). PredatorB Prod-
uct Inf. Sheet [Online]. Available: http://www.ga-asi.com/products/
aircraft/predator_b.php
[52] General Atomics Aeronautical Systems Inc. (2011). Remote Video
Terminal
Product
Inf.
Sheet
[Online].
Available:
http://www.ga-
asi.com/products/ground_control/rvt.php
[53] General Atomics Aeronautical Systems Inc., (2011). Sky Warrior
Product Inf. Sheet [Online]. Available: http://www.ga-asi.com/products/
aircraft/er-mp-uas.php
[54] Turkish Aerospace Industries, Inc. (2011). Anka Product Inf. Sheet [On-
line]. Available: http://www.tai.com.tr/taimain.aspx
[55] Israel Aerospace Industries Ltd. (2011). Heron 1 Product Inf. Sheet [On-
line].
Available:
http://www.iai.co.il/18900-16382-en/BusinessAreas_
UnmannedAirSystems_HeronFamily.aspx?btl=1
[56] Israel
Aerospace
Industries
Ltd.
(2011).
Heron
TP
Product
Inf.
Sheet
[Online].
Available:
http://www.iai.co.il/18900-37204-
en/BusinessAreas\UnmannedAirSystems_HeronFamily.aspx?btl=1
[57] Northrop
Grumman
Corporation.
(2011).
Global
Hawk
Product
Inf. Sheet [Online]. Available: http://www.as.northropgrumman.com/
products/ghrq4a/index.html
[58] FalconView.
(2011).
Frequently
Asked
Questions.
[Online].
Available:
http://www.falconview.org/trac/FalconView/wiki/Frequently
AskedQuestion
[59] MicroPilot Horizon. (2011). Product Inf. Sheet [Online]. Available:
http://www.micropilot.com/products-horizonmp.htm
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:19:19 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 10]**
*(This page contains a figure/chart/image not captured in text)*

62
IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 43, NO. 1, JANUARY 2013
Joshua Michael Peschel (M’12) received the B.S.
degree in biological systems engineering, the M.S. in
biological and agricultural engineering, and the Ph.D.
degree in computer science all from Texas A&M Uni-
versity, College Station, in 2001, 2004, and 2012,
respectively.
He is currently a Research Assistant Professor of
civil and environmental engineering with the Univer-
sity of Illinois at Urbana-Champaign, Urbana. His
research interests include human–computer interac-
tion, human–robot interaction, and artiﬁcial intelli-
gence applied to civil and environmental engineering systems.
Robin Roberson Murphy (F’10) received the
B.M.E. degree in mechanical engineering, and the
M.S. and Ph.D. degrees in computer Science all from
the Georgia Institute of Technology (Georgia Tech),
Atlanta, in 1980, 1989, and 1992, respectively.
She was a Rockwell International Doctoral Fellow
with Georgia Tech. She is the Raytheon Professor of
computer science and engineering with Texas A&M,
College Station, and directs the Center for Robot-
Assisted Search and Rescue. Her research interests
include artiﬁcial intelligence, human–robot interac-
tion, and heterogeneous teams of robots.
Dr. Murphy was awarded the Al Aube Outstanding Contributor Award by the
Association for Unmanned Vehicle Systems International Foundation in 2008,
for her insertion of ground, air, and sea robots for urban search and rescue at
the 9/11 World Trade Center disaster, Hurricanes Katrina and Charley, and the
Crandall Canyon Utah mine collapse.
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:19:19 UTC from IEEE Xplore.  Restrictions apply. 
