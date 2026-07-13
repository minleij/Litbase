# cushing-et-al-2006-overview-detail-in-a-tomahawk-mission-to-platform-assignment-tool-applying-information-visualization

*Source file: cushing-et-al-2006-overview-detail-in-a-tomahawk-mission-to-platform-assignment-tool-applying-information-visualization.pdf — 14 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

Overview þ detail in a Tomahawk
Mission-to-Platform Assignment Tool:
applying information visualization in support
of an asset allocation planning task
John Cushing1
Lecha Dawn Janssen1
Stephen Allen1 and
Stephanie Guerlain1
1Deptartment of Systems and Information
Engineering, University of Virginia,
Charlottesville, VA, U.S.A.
Correspondence:
Stephanie Guerlain, Deptartment of Systems
and Information Engineering, University of
Virginia, PO Box 400747, Charlottesville, VA
22904-4747, U.S.A.
Tel: þ 1-434-924-4438;
Fax: þ 1-434-982-2972;
E-mail: guerlain@virginia.edu;
URL: www.sys.virginia.edu/hci
Received: 20 July 2004
Revised:
27 November 2005
Accepted: 27 November 2005
Online publication date: 9 March 2006
Abstract
Information visualization techniques such as overview þ detail displays have
traditionally been applied and studied in domains with static data sets
supporting information retrieval tasks. This study examines how these
techniques can be extended to the design of interfaces for decision support
systems (DSSs). Specifically, we developed a computerized decision support
tool to assist Naval Tomahawk Strike Coordinators in the complex process of
assigning a set of planned missions to a set of available launch platforms based
on a number of different constraints and objectives, and compared user
performance on two realistic scenarios (a within-subjects factor) across two
versions of this tool (a between-subjects factor). The first version of the Mission-
to-Platform Assignment Tool provided users with only a set of detail displays
when assigning missions, whereas the second version had an additional,
abstracted ‘overview’ display that allowed users to see the effect of early
decisions on later decisions. The results showed that subjects performing this
planning task with the overview þ details display version completed scenarios,
on average, 21% faster, with 22% fewer errors and with 74% fewer required
workspace navigation activities than a comparable group using just the detail
displays version. Subjects in the former group also rated their situational
awareness 14% higher than those subjects without the overview display.
Information Visualization (2006) 5, 1–14. doi:10.1057/palgrave.ivs.9500111
Keywords: Overview þ detail display; decision support system (DSS); information
visualization; planning; asset allocation; command and control
Introduction
Information visualization
Information visualization (IV) techniques can be applied by designers to
provide users with suitable external representations of abstract entities.1 IV
can free up mental processing for more meaningful interaction with the
material2 by reducing a user’s search for information, by aiding in the
detection of patterns, and by encoding information in a manipulable
medium.3 Traditionally, IV taxonomies, guidelines, and research have
focused on interactions with relatively static data sets in which the operator
sets the pace.4 Examples include the application of IV techniques for
document searching5,6 for viewing large graphs and networks,7 for working
with large visual documents,8 for geometric visualization,2 and for
Information Visualization (2006) 5, 1–14
& 2006 Palgrave Macmillan Ltd. All rights reserved 1473-8716 $30.00
www.palgrave-journals.com/ivs

---
**[Page 2]**
*(This page contains a figure/chart/image not captured in text)*

graphical rendering.9 In these types of tasks, the operator
is often interested in retrieving a subset of the available
information. This can be accomplished through a variety
of
manipulations,
including
overview,
zoom,
filter,
details-on-demand, relate, history, and extract,10 and is
facilitated by having multiple-window coordination11 to
coordinate different perspectives of the same information.
Window on a domain
Although IV has traditionally been applied and studied in
domains with static data sets, supporting information
retrieval tasks, we believe that IV techniques can be
extended to the design of user interfaces for decision
support systems (DSSs). DSSs are computer-based tools
intended to assist with decision- or problem-solving
tasks, typically by automating a portion of the task.
Examples of the role that a decision support system may
play in problem-solving include information integration,
alerting, critiquing, diagnosis, or process modeling.12 In
planning and scheduling tasks, user interaction with the
system may result in changes not only to a data set, but
possibly to the state of an external system, or outcome of
a process. Furthermore, in process control and command
and control systems, the supporting data are usually
changing, with or without user input.
Therefore, if we consider the user interface as a window
on the domain, it should not only support the user’s
ability to extract information about the domain, but it
should also facilitate the user’s ability to take actions to
perform tasks.13 Bjo¨rk et al.14 have also made this
distinction between two levels of interaction with a
system. The first level, manipulation of the way in which
the data are presented, supports the user’s ability to
extract information, and is accomplished through the
tasks proposed by Shneiderman (zoom, filter, extract,
etc.).10 The second level, which involves changing the
data itself, is supported by the user’s ability to make
predictions and take actions or to control the underlying
system. Interactions with a decision support system at
this second level might involve tasks such as planning,
scheduling, asset allocation, diagnosis and control.
Although it is not yet common, the application of IV
techniques to DSSs is not a novel concept. For example,
Andrienko & Andrienko15 applied the IV technique of
multiple window coordination to support the decision-
making processes associated with supervisory control of
an automated multiple-criteria decision-making tool.
Their discussion of how IV can be applied to such a
system uses a framework of the decision-making process
that includes three major phases, referred to as intelli-
gence (analyzing the situation and defining the pro-
blem), design (developing hypotheses and alternative
courses of action), and choice (evaluating the alternatives
and selecting a course of action) (Smith as cited in
Andrienko & Andrienko15). They found that the utility of
IV techniques reaches beyond the first stage of informa-
tion gathering (to which IV has traditionally been
applied), and can be extended to the design and choice
phases if it enables decision-makers to understand the
trade-offs involved in their decisions.
Overviews and details in decision support
Overview displays can support a variety of cognitive
functions by providing a common frame of reference for
team problem-solving, supporting quick assessment of a
system state, enabling rapid shifting between views, and
providing pre-attentive cues about where one should
focus next.16 A well-designed overview provides users
with an idea of the size of the data set or system space, an
understanding of how items in the space relate to one
another, and the ability to recognize objects of interest.6
Overview
displays
alone,
however,
do
not
provide
specific information about subcomponents or individual
items of interest. Detail displays can provide specific
information about these items but when navigating
through detail views of large data sets, users may get
lost, or focus only on a small portion of the display
space.11,16
To overcome the limitations associated with the use of
overview and detail displays alone, they can be used
together. Overview þ detail displays, which combine both
types, provide access to specific information (details), in
context of the ‘big picture’ (overview). The overview and
detail displays can be shown one at a time, known as
time-multiplexing, or at the same time in different parts
of the screen, known as space multiplexing.1 Providing
both views on the same screen may require more space,
but reduces the frequency of navigational switching. It
has been shown that users perform diagnosis better with
an integrated display where all information is displayed
in the same spatial area, as users have a better chance of
maintaining situational awareness.17
By definition, the content and appearance of the
overview and detail displays may differ;1 however in
conventional overview þ detail displays, the overview
tends to be a thumbnail or zoomed-out representation
of the details. The popularity of this type of over-
view þ detail display is apparent in the literature – it has
become so common that recommendations have been
developed for effective application of the ‘zoom factor,’
which is the magnification ratio between the larger and
smaller of the of the two windows in an overview þ detail
display.11,18 Some examples of these types of over-
view þ detail displays include image browsers,19 maps.18
and document viewers such as Adobe Acrobatt.
This use of zoom factors and thumbnails in the design
of overview þ detail displays is most appropriate in
domains where the data set can be represented literally
as a ‘big picture’ (in a graphical sense). Domains such as
image- and document-browsing, and map navigation
naturally lend themselves to this type of overview þ de-
tail display. The underlying data sets in these domains are
typically static, and bounded; therefore, a literal ‘big
picture’ exists and can serve as an overview. Additionally,
since the primary tasks associated with these domains are
based on a user’s need to search, review, or navigate
An overview þ detail asset allocation tool
John Cushing et al
2
Information Visualization

---
**[Page 3]**
*(This page contains a figure/chart/image not captured in text)*

through the data-space, this type of overview coupled
with a zoomed-in, detailed view supports the required
tasks.
In decision-support tasks (such as planning, schedul-
ing, asset allocation, diagnosis, and control tasks) an
effective set of overview þ detail displays may facilitate a
decision-maker’s ability to see the position of a potential
solution with respect to other feasible alternatives in an
abstract decision space, or ‘attribute’ space.15 Addition-
ally, DSSs may assist users in the management of dynamic
processes (e.g. see17,20–22), wherein the decisions and
possible
configurations
are
endless,
and
therefore
impossible to represent graphically in a zoomable overview.
As a result, an overview representation of this attribute
space may be a less literal interpretation of the ‘big
picture,’ but rather a representation of the information at
a higher level of abstraction. In these cases, an overview
may just focus on those attributes that are important
when comparing across a large solution space.
For example, if a decision-support tool is aiding
planning, scheduling or asset allocation tasks (user
interactions at the second level) the detail view may
represent the candidates available for allocation to a
specific slot, while the overview represents the view of
how an allocation impacts the overall system or decision-
space. By providing information about the impact one
decision makes on other subcomponents and/or the
larger system, an overview can facilitate a decision-
maker’s
ability
to
compare
alternatives
in
‘what-if’
analyses.
Simultaneously,
the
detail
space
provides
enough information about each attribute that the user
can view and manipulate options based on predeter-
mined criteria. In these cases, the representations of the
overview and detail displays may not resemble the same
literal ‘big picture’ at different magnifications. Instead,
the overview display may be designed to best support the
cognitive activities required to monitor the impact to the
system, while the details picture may provide specifics
about the available choices and their attributes. Both
displays may also take advantage of techniques such as
filtering, sorting, and linking, to support user interaction
on the first level. These techniques can help reduce
clutter and enable the user to focus on the elements s/he
deems important to the task at hand.
Overview þ detail in a Tomahawk
Mission-to-Platform Assignment Tool
Applying information visualization in support of an
asset allocation planning task
From a practical perspective, this research was specifically
aimed at developing user interface concepts that would
lead to a DSS designed to assist U.S. Navy personnel when
planning Tomahawk Missile Strikes. A ‘strike’ is a focused
attack effort to meet a military objective. Tomahawks are
long-range cruise missiles that can be launched from
offshore launch platforms, specifically Cruisers (CG),
Destroyers (DD, DDG) and Submarines (SSN). These
missiles can travel for up to 2 h covering several hundred
miles to reach a target with pinpoint accuracy, using
several onboard navigation facilities. Previous work has
focused on the design and evaluation of decision support
displays for in-flight monitoring and control.23–27 The
work presented here focuses on the design and evaluation
of displays to support the preplanning required to decide
which launch platforms will be responsible for firing
what missiles, at what time, and in what order, so as to
meet strike objectives.
From
a
theoretical
perspective,
this
research
was
specifically aimed at exploring the application of visua-
lization techniques to determine whether application of
overview þ detail displays can assist planners in making
faster, more effective asset allocation decisions given
common pitfalls in such tasks, such as making an early
asset allocation decision that negatively impacts the
overall solution. For Tomahawk strike planning, the
‘assets’ are considered to be the missiles onboard launch
platforms and the ‘demands’ are missions that need
missiles. The ‘constraints’ are the required launch time
window, the required launch location, the required
missile characteristics, etc.
Our hypothesis was that an effective overview would
support users in planning the order in which to make
asset assignments, so as to avoid making an arbitrary
assignment that would make infeasible a future assign-
ment. This dilemma is encountered when a future
demand can only be accomplished by a limited number
of assets due to the constraints of the problem (if, e.g. a
high-priority future mission can only be accomplished by
one platform based on missile inventories and platform
locations), yet those assets can also accomplish many
other missions, and may be chosen for those (and thus
depleted prior to the later assignments). If the user is
serially addressing each assignment, only working within
the trade space of a single assignment at a time, s/he may
not realize that by assigning that asset to the current
mission,
s/he
has
removed
the
only
asset able
to
accomplish
another
mission.
An
effective
overview
should help a user realize the impact of each decision
on future asset assignments.
The design process
We followed a human-centered systems design process to
develop the Tomahawk Mission-to-Platform Assignment
tool. The process began with a task and stakeholder
analysis, based on interviews with subject matter experts
and observations of training operations, to identify the
cognitive processes and actions required to achieve
various goals. This led to a set of functional design
requirements based on the tasks to be supported. The
requirements served as guidelines during the iterative
development and evaluation of user interface prototypes.
A final prototype was implemented with test scenarios,
and an experiment was conducted to specifically evaluate
the use of an overview to support the asset allocation
planning task.
An overview þ detail asset allocation tool
John Cushing et al
3
Information Visualization

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

Mission-to-platform assignment – task analysis
A mission is a detailed flight path from an initial,
preplanned waypoint, to a target of interest. Missions
are developed by highly trained mission planners, who
take into account terrain data, missile flight character-
istics, navigation data, no-fly zones and target character-
istics to develop a highly accurate flight path for a missile
to fly. A Tomahawk Strike Coordinator (TSC) is the
individual responsible for tasking mission planners to
create missions for the missiles to fly to reach targets of
interest. Launch platforms (Cruisers, Destroyers, and
Submarines) carry an inventory of different types of
missiles and can be tasked to download a mission into a
missile and launch it at a designated place and time to
successfully achieve a mission. The TSC assigns missions,
once developed, to platforms based on a set of criteria:
 Does the platform have the required mission data
onboard and, if not, is there a communications
mechanism and sufficient time available to send the
mission data to that platform?
 Does the platform have the right set of missiles
onboard to accomplish the mission?
 Can the missiles be launched in the appropriate time
frame (it takes a variable amount of time to select and
launch a missile from inventory).
 Can the platform be physically located in the asso-
ciated ‘launch basket’ (a geographical area) for that
mission (and for all the other missions assigned)?
Depending on the distances between launch baskets,
this could become problematic, but launch baskets are
often large enough that a platform can be in one
location and accomplish several missions.
 Given that these firm constraints can be satisfied, the
TSC might consider other criteria when assigning
missions to platform, such as future ‘salvo’ capabilities
(e.g. maximizing the number of missiles left on each
platform available to be launched simultaneously for
future strikes), or instead may want to ‘use up’ all
missiles on a platform if it is scheduled to leave the area
of operations. For example, the TSC has to consider the
time window during which submarines will be avail-
able to come to the surface to launch missiles (given
the need to remain submerged to meet other objec-
tives), the direction in which a surface ship needs to be
traveling to meet other objectives, and other charac-
teristics of the platforms such as the staff, experience
level, and level of technology available on each.
As evidenced by the results of the task analysis, the TSC
considers a variety of factors when assigning missions to
platforms. The computer system currently used by the
U.S. Navy (called the Personal Computer Mission Dis-
tribution System, or PC-MDS) gives TSCs the ability to
access a database of planned missions, match missions to
targets, and assign these missions to launch platforms to
execute Tomahawk missile strikes. Despite these capabil-
ities, however, it provides almost no support for making
the mission to platform assignments, beyond showing
missile availabilities for each platform. The assignment of
missions to platforms is only supported by the screen
shown in Figure 1, which allows a mission to be ‘dragged’
to a platform that has the appropriate type of missiles on
board for that mission. This screen does not provide the
TSC with a decision tool to compare alternative options
or evaluate decisions based on the criteria identified in
the task analysis. As a result, the user must keep track of
all relevant decision factors mentally or by taking notes.
It was observed and confirmed through interviews and
observations of training scenarios that missions are
Figure 1
Personal Computer Mission Distribution System (PC-MDS) Platform Assignment Tool.
An overview þ detail asset allocation tool
John Cushing et al
4
Information Visualization

---
**[Page 5]**
*(This page contains a figure/chart/image not captured in text)*

usually assigned ‘one at a time’ in a serial fashion, thus
potentially leading to the problem identified above.
Functional requirements of the assignment tool
Based on the task analysis, it was clear that the TSC
should be able to see why one platform is (or is not) a
candidate
based
on
its
mission
availability,
missile
availability, launch area constraints, and current opera-
tions status; and should also be able to compare the
feasibility of platform assignments based on constraints
such as time remaining in launch area, follow on salvo
capabilities, and ability to uniquely satisfy certain mis-
sions. The assignment tool should also give the TSC the
ability to conduct ‘what-if’ analyses, for example to try
different combinations of assignments and review the
potential impacts of decisions. This may be especially
helpful if it is anticipated that priorities or constraints
may change. Finally, the assignment tool should show
the TSC how one assignment impacts future assignments.
Iterative design
Based on the need to display specific attributes of the
missions, missiles, and platforms, it was clear that detail
views would be necessary; and based on the user’s need to
track the overall status of all missions and platforms, we
believed that an overview display would likely be helpful.
Prototypes evolved through two major iterations before
reaching the final prototype used for testing. Early
prototypes
were
mocked-up
using
Microsoft
Power-
Pointt. The final prototype was implemented in Javat
and is a fully functional simulation system, enabling the
creation of test scenarios and the ability for subjects to
‘solve’ the scenarios.
Prototype 1
An early version of the prototype provided
the user with two screens, positioned side-by-side. A
geographic display, provided on the left screen, was
intended to show the physical location of platforms and
targets and to enable ‘simulating’ strikes. The screen on
the right contained the mission assignment tool (see
Figure 2), with some of the features highlighted. The top
part of the screen (in gray) shows the date and time of the
last mission data update (MDU) sent to the platforms,
along with battle force information, for example the total
number of each of the three types of missiles in inventory
as compared to the number required for the set of
missions being assigned. (The three kinds of missiles
currently being flown are referred to as Block III-C, Block
III-D, and Block IV-E). The bottom third of the screen
allows the user to select which salvo (group of missions to
be flown together) to show. Currently Salvo 1 is selected,
so the operator can view the details of each mission in
that salvo. In Figure 2, the first mission of Salvo 1 is
currently selected, and the evaluation criteria for that
mission are compared across the set of available platforms
in the white, central area of the screen. This information
is shown in a matrix, with platforms forming the column
headings (e.g. ‘CG 58,’ ‘CG 64,’ ‘DD 982,’ etc.), and the
relevant criteria about the selected mission along the
Figure 2
Prototype 1 of the Mission-to-Platform Assignment Tool.
An overview þ detail asset allocation tool
John Cushing et al
5
Information Visualization

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

rows, e.g., whether the platform has the mission data
onboard, whether the platform has a sufficient number of
the right type of missiles for the selected mission, the
relative ‘cost’ of using those missiles (as calculated by an
as of yet to be determined algorithm), the distance of that
platform to the launch basket, the speed at which the
platform would have to sail in order to get to the launch
basket in time, the follow-on-salvo inventory that would
be remaining for that platform if the mission was
assigned, how many days the platform is remaining in
the theater of operations, and whether the platform is
‘busy’ due to other taskings.
A heuristic evaluation by the authors identified several
problems with this design. One problem is that the
matrix just described shows all information all the time,
even when some criteria would preclude a mission from
being assigned. For example, in Figure 2, only DD 988
and SSN 699 have the mission data available on board
and yet all the details are shown for each of the other
platforms (CG 58, CG 64, etc.), causing unnecessary
visual clutter and requiring extra cognitive effort to find
feasible assignments. Further, although this design allows
a user to see how one mission can or cannot be
accomplished by the available platforms, it is impossible
to see the impact that such an assignment would have on
the other missions to be assigned. This led to our second
prototype which addressed these two problems.
Prototype 2
Prototype 2 (shown in Figure 3) is a single
screen display that has an overview display in the top left
quadrant of the screen, a geographic display in the top
right quadrant of the screen, and a strike assignment
decision tool along the bottom half of the screen.
The strike assignment decision tool (a details display)
essentially combines the two matrices found in Prototype
1 into a single matrix that displays the platforms down
the left-hand side and all of the missions in a particular
salvo across the top (if there are more than five missions
in a salvo, the user has to scroll horizontally). In Figure 3,
the missions for Salvo 1 are being shown (the ‘Salvo 1’
button is highlighted at the far right). Missions 1-1H, 2-
1L, 3-1M, 4-1H, and 5-1M form the titles for five sections
of the matrix. Mission 1-1H is the first mission of the first
salvo. The ‘H’ indicates that it is a high-priority mission.
Figure 3
Prototype 2 of the Mission-to-Platform Assignment Tool.
An overview þ detail asset allocation tool
John Cushing et al
6
Information Visualization

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

It requires three Block IIIC missiles, 0 Block IIID missiles,
and 0 Block IVE missiles. (The boxes along the top of each
mission section indicate the total number of missiles
required for that mission.) Below that is a multi-column
format that allows the user to determine why one
platform is a better candidate than another for that
particular mission. These factors include whether or not
the platform has the mission data onboard (if not, an ‘N’
is displayed in the ‘MSN’ column), and whether or not it
can reach the launch area in time (if not, an ‘N’ is
displayed in the ‘LB’ column). The left side of the matrix
displays information about each platform, such as its
total inventory of each type of missile, the number of
days that platform will remain in the theater of opera-
tions, and whether the platform is currently performing
other operations that would prevent it from being
assigned a mission. If a platform meets all these factors
for a particular mission and has a sufficient number of
missiles of each type available to satisfy mission require-
ments, then these cells in the matrix are displayed in a
dark gray shade. If a platform otherwise meets all the
factors for a particular mission but only has enough
missiles to partially satisfy the mission requirements,
then these cells are displayed in a lighter gray shade with
the number that are available. Missile assignments can be
made by clicking on the appropriate cell in the matrix
(once for each missile assignment), which will cause the
number of required missiles to decrement, and the total
inventory of missiles for that platform to decrement.
Right-clicking will undo (delete) a missile assignment
from a launch platform. The user can make assignments
in any order, and can make as many changes as desired.
The assignment process is complete when the user clicks
on the Indigo button at the bottom right corner of the
screen. ‘Indigo’ is the term the Navy uses to define a
completed set of taskings assigned to a platform.
The benefit of this Assignment display as compared to
Prototype 1 is that it takes up less space and it allows the
user to see the impact of one assignment on up to four
others as an assignment is made. It highlights in darker
gray those platforms that can fully accomplish a mission
and,
as
assignments
are
made,
relevant
values
are
decremented and any other assignments that are no
longer feasible de-highlight as appropriate.
The second major addition to Prototype 2 is the
inclusion of an overview display in the upper left half
of the screen. The overview presents all the information
in the Assignment matrix but at an even higher level of
abstraction. It shows, in matrix form, salvos (sets of
missions to be accomplished together) across the top,
launch platforms down the side, and the feasible mission
assignments within each salvo/platform cell (although
no differentiation is made in this prototype between
partially feasible and fully feasible – if only partially
feasible, the missions are still displayed). The same
mission may be displayed multiple times in a column
indicating that multiple platforms are candidates for the
assignment. In the overview display, missions are color-
coded to differentiate between high, medium, and low
priority missions. The major purpose behind this design
was to allow the user to see the order in which to make
assignments and the impact of decisions on other
assignments. For example, in Figure 3, it can be seen
that Mission 1-4H, in the ‘Salvo 4’ column of the
Overview can only be assigned to CG 64. If the user did
not have the overview display available, it is possible that
s/he would ‘use up’ the CG 64 missiles or assign CG 64 to
missions that would cause it to sail too far away from the
launch basket for Mission 1-4H when assigning missions
for Salvos 1–3. With the overview, it is likely the user
would assign 1-4H first, even though it is part of
Salvo 4 (which is ‘down the road’ in time compared to
Salvos 1–3).
To make the assignment, the user can either click on
the ‘Salvo 4’ button on the bottom right or just click on 1-
4H in the Overview display, which will automatically
open Salvo 4 in the Assignment matrix at the bottom.
Once there, the user can see the details of the missiles
required and assign them by successively clicking on the
missiles to be assigned as described earlier. This may cause
other
potential
assignments
for
CG
64
to
become
infeasible. If it is due to the time/distance relationship,
then just clicking on one missile will ‘cause’ the platform
to be in a certain location in a certain time and therefore
potentially eliminate some assignments that are too far
away – these will cause the launch basket or ‘LB’ column
to fill in with an ‘N’ (meaning, ‘No’, it cannot make it
there in time). If distance is not a problem, then the
decrement in total inventory may cause certain other
potential mission assignments for that platform to no
longer be fully feasible. In this case, mission assignments
that were dark gray in the Assignment matrix will turn to
light gray and then potentially become blank if there is
no inventory left to satisfy another mission. At the same
time, as users are making assignments and certain
missions are no longer feasible for a platform, those
mission names disappear from the relevant cell in the
Overview Matrix.
Thus, the assignment display in the bottom half of the
screen facilitates interaction with the system on the
second level (database changes), whereas the overview
facilitates interaction on the first level (display manip-
ulation), providing the user with the ability to vary
display parameters for easier comparison of alternatives.
For example, the user has the ability to filter the overview
display based on priority and whether platforms can
partially or completely fulfill mission requirements. As
each mission is ‘assigned’ the system calculates the new
planned state of that platform (where it would be located
at what time, how many missiles of each type it would
have left, etc.). If mission assignments are made that
prevent other missions from occurring, these other
missions disappear from the overview and detail displays
as just described.
The idea behind the geographic display is that it would
help the TSC visualize the distance between a platform’s
An overview þ detail asset allocation tool
John Cushing et al
7
Information Visualization

---
**[Page 8]**
*(This page contains a figure/chart/image not captured in text)*

current location and a particular mission’s launch area.
However, it was unclear at this point how to make the
display interactive, particularly since assigning a mission
to a platform might require that platform to sail to a
different location. We were unable to devise an effective
way to show this dynamism in the planning stage, and
were also uncertain about whether such a display would
be helpful or just add unnecessary cognitive effort to try
to interpret.
In summary, the major advantages of Prototype 2 are
the design of an overview display (top left), and the
simultaneous availability of details for up to five missions
(shown in the bottom half of the screen). Additionally,
almost all information is available on a single screen
display, minimizing scrolling and navigational switching.
Among the disadvantages are that the display is very
number-intensive, the details view can only display up to
five missions for one salvo at a time, and the concept of a
dynamic geographic display was not fully implemented.
The final display
Owing to limited resources, we were unable to fully
design and implement the interactive map display, thus,
we decided to focus on implementing the overview þ de-
tail screens from Prototype 2. The system was implemen-
ted in Javat. We built a simulation engine to create
scenarios and run them, with all of the relevant data
about missile inventories, platform locations, etc. The
simulation engine tracks all the data and makes updates
appropriately as the scenarios are run. A screen shot of
the Mission-to-Platform Assignment Tool for a particular
scenario is shown in Figure 4. In place of the map display,
we added a bar graph display of platform characteristics,
which highlights the current missile inventory and days
remaining in theater for each platform. As assignments
are made, the bar graphs decrease allowing the user to see
how many missiles remain and how many have been
assigned. This might serve as a form of overview for the
platforms themselves, so users could get a ‘status at a
glance’ for platform inventory, time in theater, and battle
force status, although all of this information is already
displayed and updated numerically in the Assignment
display.
Some minor changes were made to the Assignment and
Overview displays from Prototype 2. The color coding of
the missions in the overview display were changed to
Figure 4
Final design of the Mission-to-Platform Assignment Tool – with overview display.
An overview þ detail asset allocation tool
John Cushing et al
8
Information Visualization

---
**[Page 9]**
*(This page contains a figure/chart/image not captured in text)*

match the color coding of the mission name in the
Assignment display, to provide better correspondence
between
the
two
displays.
Two
additional
filtering
options
were
provided
for
the
Overview,
allowing
users to only see assigned or unassigned missions as
desired. Further, we added color coding such that fully
assigned missions are highlighted in the overview display
(e.g. the four missions for Salvo 1 are completely
assigned). Finally, in the Assignment display, platforms
that can completely satisfy a mission are displayed in
white and platforms that can partially satisfy a mission
are displayed in dark gray. This way, feasible assignments
are the most salient, making for faster search times than
in our previous design, in which those platforms that
could only partially satisfy a mission stood out more.
Decision support tool evaluation – utility of an overview
Two versions of this final prototype were compared, with
the purpose of evaluating the utility of an overview
display in a resource allocation planning task. One
version was as described above, with all three coordinated
displays, and the other version was simply without the
overview display. In this version, static sponsor logos
were displayed in place of the overview display (see
Figure 5).
The
hypothesis
for
this
study
was
that
subjects
provided with the overview would be able to plan better
due to the availability of the overview, and would
therefore perform better in terms of taking less time,
making fewer errors (number of rule violations according
to ‘commander’s intent’), requiring fewer navigational
switches among salvo screens in the Assignment display,
and reporting higher situational awareness scores than
the non-overview group.
Experimental design
In order to test this hypothesis, we conducted a mixed
factorial experiment. ‘System’ was a between-subjects
factor with two levels: with an overview, or without an
overview. ‘Scenario’ was a within-subjects factor with two
levels: medium and high difficulty. The high-difficulty
scenario was defined as such because there was only one
way (we believe) to accomplish the assignments so as to
meet commander’s intent, and this required the planner
Figure 5
Final design of the Mission-to-Platform Assignment Tool – without overview display.
An overview þ detail asset allocation tool
John Cushing et al
9
Information Visualization

---
**[Page 10]**
*(This page contains a figure/chart/image not captured in text)*

to realize that ‘later’ missions (e.g. missions in Salvo 3)
required a certain platform to be available, thus the
subjects must avoid assigning missions for that platform
in other Salvos (e.g. Salvos 1 and 2).
Subjects
A
total
of
32
students
taking
a
human–
computer interaction course at the University of Virginia
(UVA) participated as subjects. (University students were
utilized as there is not a sufficient number of actual
trained TSCs to run a factorial experiment with them as
subjects.) The study protocol was approved by the UVA
Institutional Review Board.
Procedure
All subjects were first introduced to the task
and taught the functionality aspects of the display shown
in Figure 5. Specifically, subjects were trained on the task
of assigning missions to platforms with the mission
assignment tool, and were instructed on the ‘Comman-
der’s intent,’ defined as follows: Assign all high-priority
missions first, then medium priority, then low priority;
when all else is equal, first assign missions to launch
platforms with fewer days remaining in service; if there
are no other differences, use the launch platform which
will have the highest number of missiles remaining on
board after mission assignment. Avoid making ‘partial’
assignments if at all possible, for example each mission
requires a set of missiles, and it is preferable if one
platform can completely accomplish that mission rather
than having two or more platforms complete portions of
the mission.
Half of the subjects were randomly selected to stay and
receive additional instruction on how to interpret and
use the overview display (the version of the system
shown in Figure 4), and the other half of the subjects
were dismissed prior to this training.
Subjects were then individually scheduled for testing
within 2 weeks of training. During the test session, each
subject was asked to talk aloud during one ‘easy’ scenario
to enable the experimenter to ensure that the subject
understood the assignment rules and the use of the
interface. Subjects were then asked to conduct two test
scenarios, a ‘medium’ and a ‘hard’ scenario. Scenario order
was counterbalanced across subjects and subjects were not
told that one of the scenarios was expected to be harder.
Dependent
variables
were
time
to
complete
the
scenario, whether or not subjects followed ‘commander’s
intent’ (i.e. the number of violated rules as specified in
the scenario instructions), the number of navigational
‘switches’ between salvo screens in the Assignment
matrix and subjective scores of situation awareness and
confidence in results.
The simulation software tracked and reported the
number of navigational switches and amount of time
taken during a scenario. Rule violations were only
counted when a subject submitted a solution (thus rule
violations that were made during the problem-solving
process but then ‘undone’ were not counted). Situational
awareness and confidence in results were measured based
on subjects’ self-rating, on a scale from 1 (worst) to 10
(best) just after completion of the experiment. Descrip-
tive statistics, the two-way ANOVA and the difference in
proportions
tests
were
used
to
analyze
the
results
depending on the variables being analyzed. Significance
is reported at Po0.05.
Results
All subjects were able to complete the two test scenarios.
Figure 6 provides the descriptive statistics for the
dependent variable Time. A Kolmogorov–Smirnov test
showed that the time distribution was non-normal; thus
a natural logarithm transformation was performed. A
two-way ANOVA on these transformed data showed that
System, Scenario, and Subjects were all significant (see
Table 1) but the interactions were not. As expected, the
hard scenario took about 5 min longer, across all subjects,
than the medium scenario. Also as hypothesized, subjects
with the overview finished the scenarios faster (a mean of
27% faster for the medium scenario and 14% faster for
the
hard
scenario).
This
is
statistically
significant
(Po0.05).
Figure 7 provides the descriptive statistics for the
dependent variable Switches. Owing to the non-homo-
geneity of variances, a natural logarithm transformation
was performed. A two-way ANOVA (see Table 2) on these
transformed data showed that subjects with the overview
navigated across the assignment tool detail displays
significantly less (on the order of 71–76% less) for both
the medium and hard scenarios (Po0.001).
Without the overview, nine out of 32 subjects (28%)
had a rule violation; with the overview, two out of 32
subjects (6%) had a rule violation. This difference favors
the use of the overview display (P ¼ 0.01, difference of
proportions test). Situational awareness was rated higher
for subjects with the overview (7.971.4 vs 6.0672.8,
Figure 6
Descriptive statistics and box plot for the dependent
variable: time in minutes.
An overview þ detail asset allocation tool
John Cushing et al
10
Information Visualization

---
**[Page 11]**
*(This page contains a figure/chart/image not captured in text)*

P ¼ 0.023, two-tailed t-test, d.f. ¼ 30), but there was no
statistical difference for confidence in results (7.771.3 vs
7.971.6).
Subjects were also asked to comment on the displays
available to them in an open-ended discussion format
with the experimenter after they were done with the
experiment. For the Platform Characteristics bar graph
display, most subjects indicated that they did not use this
display at all.
For the Assignment display, a few suggestions were
made, such as changing the color scheme to correspond
to the priority of missions, similar to our color-coding
scheme in Prototype 2. Other suggestions were to be able
to sort missions by priority, to be able to assign all the
missiles for a mission at once, to make the Indigo button
a red color, to place platform information on the far right
as well as the far left of the matrix and/or to alter the
color of the rows of each of the platforms to make it easier
to see which row refers to which platform. Some subjects
also requested an algorithm to highlight a recommended
solution and to show warnings if the user makes a
infeasible or incorrect decision, perhaps reflecting the
difficulty or tediousness of performing the task manually.
For the Overview display, a few suggestions were also
made, such as to put all the high-priority, medium
priority, and low-priority missions into separate columns,
to underline missions with the fewest options, and to
have an algorithm rank the platforms.
Four subjects who were in the Overview group were
asked to come back a week later to solve another set of
scenarios, at which time the use of an off-body eyegaze
tracker
helped
determine
what
percentage
of
time
subjects used the various displays. The data showed that
subjects looked at the Platform Characteristics bar graph
display o2.8% of the time. Among these subjects, the
percent of time spent looking at the Overview display
ranged from 34.6 to 66.8% of the time.28
Finally, a lieutenant commander in the Navy, who is
responsible for training all TSCs in the Navy, provided his
insights on the system. He commented that the assign-
ment tool ‘gives the TSC a consolidated view of the
Table 1
ANOVA results for the dependent variable LN (time) (test of between-subjects effects)
Source
Type III sum of squares
d.f.
Mean square
F
Significance
Intercept
Hypothesis
2529.458
1
2529.458
7881.184
0.000
Error
9.628
30
0.321a
System
Hypothesis
1.391
1
1.391
4.335
0.046
Error
9.628
30
0.321a
Scenario
Hypothesis
1.075
1
1.075
6.475
0.016
Error
4.982
30
0.166b
Subject(System)
Hypothesis
9.628
30
0.321
1.933
0.038
Error
4.982
30
0.166b
System*Scenario
Hypothesis
0.151
1
0.151
0.908
0.348
Error
4.982
30
0.166b
aMS(Subject(System)).
bMS(Error).
Figure 7
Descriptive statistics and box plot for the dependent
variable: switches.
An overview þ detail asset allocation tool
John Cushing et al
11
Information Visualization

---
**[Page 12]**
*(This page contains a figure/chart/image not captured in text)*

assignment process’ that is not currently available with
PC-MDS and that, ‘with this tool, we can look into the
future, to see and correct potential problems.’
Discussion
The purpose of our Mission-to-Platform Assignment Tool
was to provide an operator with access to the attributes
required to make allocation decisions, and to provide a
means of comparing alternative solutions based on how
the overall objectives are impacted. The design philoso-
phy was to develop a visual representation that would aid
an operator in the manual support of allocations, so that
if/when assignment algorithms become
available to
support the process, operators would still be able to
maintain an understanding of the problem space, and
have an effective user interface for manual comparison.
Thus, although a few subjects requested such an algo-
rithm, this was not made available for this study. Future
studies might focus on the best way to support such a
mixed-initiative interaction.
In this non-traditional implementation of an over-
view þ detail display, the overview represents the ‘big
picture’ as an abstraction of the potential solution space,
rather than a literal ‘big picture’ or thumbnail of the
details display. Fundamentally, the overview and details
display represent the same decision space, as they both
show which platform(s) can accomplish which mis-
sion(s), although they focus at different levels of abstrac-
tion. The details display provides a comprehensive view
that includes the total number of missiles on each launch
platform, the number of assignments required for a
mission, and which missions can be partially or com-
pletely fulfilled by a platform; however, it only allows the
user to view one salvo at a time, and thus requires
navigational switching in order to plan or make compar-
isons across salvos or within salvos that have more than
five missions. The overview does not provide details
about partial assignments, missile availability, or mission
requirements, but provides a higher-level summary of
which platforms could accomplish which missions across
all salvos.
Expressed in the context of Smith’s decision-making
model,15 it appears that the details display facilitated the
phases of information gathering (intelligence) phase, and
developing possible options (design), which made it
sufficient on its own for users to provide mission
assignments. It was the addition of the overview display
that facilitated the phase of choice, by enabling the
decision-maker to understand the trade-offs involved in
each decision, thus reducing errors, time and navigation.
We
believe
that
these
improvements
were
enabled
primarily by the fact that subjects were able to plan with
the overview display, and then navigate directly to the
desired assignment page, rather than relying on the
assignment views as planning tools. The overview display
also allows a decision-maker to view the impact of an
asset allocation on the entire system (including the
remaining assignment needs), and to identify which
assets fulfill unique mission goals. Operators without the
overview did not have access to a high-level view
of the information, resulting in increased navigational
switching.
Without
an
overview,
these
participants
were also forced to track comparisons mentally, likely
resulting in the increased frequency of rule violations,
and the decreased situational awareness observed in this
group.
Table 2
ANOVA results for the dependent variable LN (switch) (test of between-subjects effects)
Source
Type III sum of squares
d.f.
Mean square
F
Significance
Intercept
Hypothesis
968.005
1
968.005
7881.184
0.000
Error
15.733
30
0.524a
System
Hypothesis
20.894
1
20.894
4.335
0.000
Error
15.733
30
0.524a
Scenario
Hypothesis
2.009
1
2.009
6.475
0.004
Error
6.221
30
0.207b
Subject(System)
Hypothesis
15.733
30
0.524
1.933
0.007
Error
6.221
30
0.207b
System*Scenario
Hypothesis
0.459
1
0.459
0.908
0.147
Error
6.221
30
0.207b
aMS(Subject(System)).
bMS(Error).
An overview þ detail asset allocation tool
John Cushing et al
12
Information Visualization

---
**[Page 13]**
*(This page contains a figure/chart/image not captured in text)*

Future work
The prototype used for the experiment was the result of
an iterative design process, which included regular
interaction with the U.S. Navy Tomahawk community.
Although the version of the prototype used for testing
has demonstrated significantly improved user perfor-
mance with the addition of an abstract overview display,
design improvements could continue to be made. Most
significantly, it is not clear how the tool can be scaled up
to accommodate larger strikes with more salvos and
platforms. Since participants indicated that they rarely
used the Platform Characteristics display, one possibility
might be to remove the Platform Characteristics display
and replace it with an extended overview that would
occupy the entire top half of the display, allowing for
strikes with more salvos in the horizontal direction, but
adding more platforms would still require additional
scrolling in the vertical direction.
Another overall improvement would be to increase the
coordination of the displays. Currently, for example,
clicking anywhere in the Salvo 1 column in the overview
will cause the details display to switch to that Salvo 1 as
well; however, it may be helpful to also highlight or
outline the selected region (Salvo 1) in the overview
display. Furthermore, this technique could be applied at
the level of the individual missions and platforms, so that
the selected platform and mission could be outlined the
overview and details displays, and the selected platform
would be outlined in the Platform Characteristics display.
Future design improvements to the overview display
might include: a representation of partially fulfilled
missions, the display of no longer feasible platforms as
assignments are made using a strike-through font (rather
than complete disappearance), and the ability for a user
to make mission assignments from the overview. This last
feature was purposely not allowed during this research, in
order to control experimental conditions across groups.
Future work also requires detailed review of the system
by expert military staff.
Conclusion
Planning tasks in domains such as dispatching, com-
mand and control, and other asset allocation domains
can be challenging, as assets allocated for one activity are
no longer available for others. The United States Navy,
when planning Tomahawk missile strikes, faces this type
of asset allocation challenge. In this paper, we described a
decision support system that aids Tomahawk planners in
their assignments of mission assignments to a set of
launch platforms, given the constraints of each launch
platform’s location, missile inventory, other tasking, time
in theater, commander’s intent, and future plans. In this
domain, early decisions constrain later decisions; thus it
is difficult to foresee all the interactions and implications
as resources are allocated.
The Mission-to-Platform Assignment Tool is a first
design of a decision support system that assists planners
by providing an algorithm that narrows the choices to
only those resources available for a particular assignment,
and by providing an interactive user interface that
supports comparison of the remaining alternatives, ‘what
if’ analysis, and evaluation of each decision in the
context of the overall impact on the system. The tool
provides an example of how IV can be applied in the
design of an interface that supports a planning task, and
provides interaction with a system at the two levels of
display manipulation and taking control actions. The
user interface applies an overview þ detail display, in
which the two detail views show the available missiles
(per mission, and per platform), and the overview display
allows the planner to quickly see the impact of asset
allocation assignments on future plans. In this system the
planning activity constantly changes the constraints of
the decision space.
In addition to demonstrating the process for develop-
ing an effective overview for a military planning task, this
study also supports previous findings that overview
displays are an effective display technique for improving
human performance.17,29,30 Furthermore, the results of
this study support previous findings15 that have shown
the utility of applied IV techniques to DSSs.
The specific techniques applied could likely transfer to
other tasks that require planning asset allocation strate-
gies based on a set of available resources that need to
satisfy an overall objective of fulfilling as many high,
medium and low priority subgoals as possible. Although
an optimization algorithm could easily identify the ‘best’
assignment for one objective, we demonstrate a working
prototype of a system that allows a user to remain ‘in the
loop’ through effective displays and organization of
information to meet task objectives.
Acknowledgments
This material is based upon work supported by the Naval
Surface Warfare Center, Dahlgren Division (NSWC/DD),
through a grant from the Office of Naval Research (ONR)
Knowledge, Superiority, and Assurance Future Naval Cap-
ability (KSA FNC) Program. Any opinions, findings, and
conclusions or recommendations expressed in this material
are those of the authors and do not necessarily reflect the
views of NSWC/DD or ONR.
References
1 Card SK, Mackinaly JD, Shneiderman B. Readings in Information
Visualization: Using Vision to Think. Morgan Kaufmann: San Francisco,
CA, 1999.
2 Sedig K, Rowhani S, Morey J, Liang H. Application of information
visualization techniques to the design of a mathematical mindtool: a
usability study. Information Visualization 2003; 3: 142–159.
An overview þ detail asset allocation tool
John Cushing et al
13
Information Visualization

---
**[Page 14]**
*(This page contains a figure/chart/image not captured in text)*

3 Card SK. Information visualization. In: Jacko J, Sears A (Eds). The
Human–Computer Interaction Handbook: Fundamentals, Evolving Tech-
nologies, and Emerging Applications. Erlbaum: Mahwah, NJ, 2003.
4 Rouse WB. Human–computer interaction in the control of dynamic
systems. Computing Surveys 1981; 13: 71–99.
5 Greene S, Marchionini G, Plaisant C, Shneiderman B. Previews and
overviews in digital libraries: designing surrogates to support visual
information seeking. Journal of the American Society for Information
Science 2000; 51: 380–393.
6 Suh B, Woodruff A, Rosenholtz R, Glass A. Popout prism: adding
perceptual principles to overview+detail document interfaces. Pro-
ceedings of ACM CHI 2002 Conference on Human Factors in
Computing Systems, 2002. Minneapolis, MN, 251–258.
7 Munzner T. Exploring large graphs in 3D hyperbolic space. IEEE
Computer Graphics and Applications 1998; 18: 18–23.
8 Baudisch P, Good N, Stewart P. Focus plus context screens:
combining display technology with visualization techniques. Pro-
ceedings of the ACM Symposium on User Interface Software and
Technology, 2001. Orlando, FL, 31–40.
9 Flider M, Bailey BP. An evaluation of techniques for controlling
focus+context screens. 2004 Conference on Graphics Interface 2004,
(London, Ontario, Canada) 135–144.
10 Shneiderman B. The eyes have it: a task by data type taxonomy for
information visualizations. 1996 IEEE Symposium on Visual Languages
1996, (Boulder, CO), IEEE, New York, 1996 336–343.
11 North
C,
Shneiderman
B.
A
taxonomy
of
multiple
window
coordinations, 1997, University of Maryland. CS-TR-3854.
12 Guerlain S, Smith PJ. Decision support in medical systems. In:
Parasuraman R, Mouloua M (Eds). Automation and Human Perfor-
mance.
Theory
and
Applications.
Lawrence
Erlbaum
Associates:
Mahwah, NJ, 1996; 385–406.
13 Roth EM, Patterson ES, Mumaw RJ. Cognitive engineering: issues in
user-centered system design. In: Marciniak JJ (Ed). Encyclopedia of
Software Engineering. Wiley-Interscience, John Wiley & Sons: New
York, 2002; 163–179.
14 Bjo¨rk S, Holmquist LE, Redstro¨m J. A Framework for Focus+Context
Visualization. IEEE Information Visualization, IEEE Press: New York,
1999.
15 Andrienko N, Andrienko G. Informed spatial decisions through
coordinated views. Information Visualization 2003; 2: 270–285.
16 Woods DD, Roth EM, Stubler WF, Mumaw RJ. Navigating through
large display networks in dynamic control applications. Proceedings of
the Human Factors Society 34th Annual Meeting 1990, (Orlando, FL),
Human Factors Society (Santa Monica, CA) 2001 396–399.
17 Burns CM. Putting it all together: improving display integration
through ecological displays. Human Factors 2000; 42: 226–241.
18 Hornbæk K, Bederson B, Plaisant C. Navigation patterns and
usability
of
zoomable
user
interfaces
with
and
without
an
overview. ACM Transactions on Computer–Human Interaction 2002;
9: 362–389.
19 Plaisant C, Carr D, Shneiderman B. Image-browser taxonomy and
guidelines for designers. IEEE Software 1995; 12: 21–32.
20 Guerlain S, Jamieson GA, Bullemer P, Blair R. The MPC elucidator: a
case study in the design for human-automation interaction. IEEE
Transactions on Systems, Man, and Cybernetics – Part A: Systems and
Humans 2002; 32: 25–40.
21 Jamieson G, Guerlain S. Operator interaction with model-based
predictive controllers in petrochemical refining. Human Performance,
Situation Awareness and Automation: User-Centered Design for the New
Millenium 2000, (Savannah, GA) 172–177.
22 Smoot ME, Bass EJ, Guerlain S, Pearson WR. Visualizations of near-
optimal protein sequence alignments. Information Visualization 2005;
4: 224–237.
23 Allen J, Interface Design and Team Structure in a Collaborative
Environment. Master’s Thesis, Department of Systems and Informa-
tion Engineering, University of Virginia: Charlottesville, VA 2004.
24 Cummings M, Guerlain S. Developing operator capacity estimates for
supervisory
control
of
autonomous
vehicles.
Human-Factors
(accepted for publication).
25 Cummings M, Designing decision support systems for a revolu-
tionary command and control domains.
Doctoral Dissertation,
Department of Systems and Information Engineering, University of
Virginia: Charlottesville, VA 2003.
26 O’Hargan K, Design of a Resource Allocation Planning System (RAPS).
Master’s Thesis, Department of Systems and Information Engineer-
ing, University of Virginia: Charlottesville, VA 2005.
27 Willis R, Tactical Tomahawk weapon control system user interface
analysis and design.
Master’s Thesis, Department of Systems and
Information Engineering, University of Virginia: Charlottesville, VA
2001.
28 Cushing J, A measurement of the effectiveness of an overview display
for the mission to launch platform assignment process essential to the
Tomahawk strike coordinator.
Master’s Thesis, Department of
Systems and Information Engineering, University of Virginia: Char-
lottesville, VA 2003.
29 North C, Shneiderman B. Snap-together visualization: can users
construct
and
operate
coordinated
visualizations?
International
Journal of Human Computer Studies 2000; 53: 715–739.
30 Rivera D, Chignell M, Davey E. Effect of overview displays on situation
assessment. Human Factors and Ergonomics Society 42nd Annual
Meeting 1998 (Chicago, IL), Human Factors and Ergonomics Society
(Santa Monica, CA) 1998, 258–262.
An overview þ detail asset allocation tool
John Cushing et al
14
Information Visualization
