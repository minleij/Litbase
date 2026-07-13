# Howard 2006 Adapting Human Leadership Approaches for Role Allocation in Human-Robot Navigation Scenarios

*Source file: Howard_2006_Adapting_Human_Leadership_Approaches_for_Role_Allocation_in_Human-Robot_Navigation_Scenarios.pdf — 8 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

Copyright - World Automation Congress (WAC) 2006, July 24-26, Budapest, Hungary
ADAPTING HUMAN LEADERSHIP APPROACHES FOR ROLE ALLOCATION
IN HUMAN-ROBOT NAVIGATION SCENARIOS
Ayanna M. Howard
Gerardo Cruz
Human-Automation Systems (HumAnS) Lab
NASA's Jet Propulsion Laboratory
School of Electrical and Computer Engineering
California Institute of Technology
Georgia Institute of Technology, Atlanta, GA, USA
Pasadena, CA 91109-8099, USA
ABSTRACT
In this paper, we propose to examine the practices of leadership defined in human relationships
and model their use in maximizing performance for human-robot interaction scenarios. This
process involves first defining the human-robot space of interaction and mapping the situational
context in which human leadership styles are most fitting. We then determine which behavior,
for both the human and robot, is most appropriate in order to understand the proper roles for
human-robot integration.
From there, we model the necessary robot behavior for increasing
efficiency in human-robot interaction schemes. We conclude by discussing experimental results
derived from allocating roles in representative human-robot navigation scenarios.
1. INTRODUCTION
As the symbiotic relationship between humans and robots solidifies, robots are transitioning
from functioning solely in the research environment to becoming productive team members in
society. As such, research in human-robot interaction and the proper roles (or behaviors) for
integration become increasingly important. The first formal research in role allocation for human-
machine scenarios is addressed in [1], in which decisions between machine versus human control
are made based on a simple comparison of capabilities. Earlier work is also found in [2] in which
human and machine capabilities are scaled in order to determine when role transitions should
occur.
Olsen and Goodrich [3] develop a model to allocate roles in human-robot interaction
schemes based on assessment of the number of robots a single individual can control in a given
scenario. In [4], a human-centered approach is used to understand the role of human-robotic
teamwork in future human space exploration missions. In this work, a framework is developed in
which robots become functional tools that assist the human rather than replace the human
operator. In [5,6], the focus is to change roles by dynamically adjusting the autonomy of an
intelligent agent based on human physiological responses [5] and reasoning about the costs of
decisions [6]. Role allocation in human and robot teams is proposed in [7,8] using an analytical
framework that decomposes tasks into independent functional primitives and determines roles by
evaluating system performance. In [9-12], researchers have presented complementary taxonomies
that define various types of roles for enhancing the interaction between humans and robots.
Finally,
recent work presented
in
[13],
discusses performance
tradeoffs
in
incorporating
collaborative task roles for systems focused on humans interacting with aerial robotic vehicles.
Although previous research and schemes provide a paradigm in which to engage robots within
our society, to further understand the role of robots, we can look at the practices of leadership
defined in human relationships.
Different styles of leadership have been adopted to model the
interaction
of
leadership
within
the
organization
[14-16].
Among
these
are
directive,
transactional, transformational, and empowering leadership.
We can use these leadership
approaches, and the practices that surround them, to provide insight into the processes we can
adopt to engage our robot partners in the future.
In this paper, we discuss the adaptation of a paradigm pertaining to human leadership in
organizations to the arena of human-robot interaction. Specifically, we classify possible scenarios
involving human-robot navigation tasks and correlate them with scenarios that involve interaction
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:11:50 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 2]**
*(This page contains a figure/chart/image not captured in text)*

only between humans. We propose that to maximize navigation efficiency in a particular human-
robot interaction scheme, a leadership style should be employed that mirrors the leadership style
that would be used if only humans were involved. Moreover, high-level behaviors that both
human and robot should exhibit must be exhibited to maximize performance of the human-robot
teaming arrangement.
Through this process, we aim to provide a basis in which to improve our
approaches for human-robot team interaction within the environment [8].
2. LEADERSHIP STYLES IN HUMAN INTERACTION SCENARIOS
The role of leadership in human relationships has permeated throughout both the academic and
business communities. Investigation of the derivation of leadership, as well as its practice and
utilization, has enabled humans to increase their productivity and successfully interact with others
throughout their daily lives. Although there are a number of typologies that provide a framework
for
classifying
leadership
patterns,
the
dominant
types
include
directive,
transactional,
transformational, and empowering leadership [14]. Table I provides a representational diagram of
these leadership styles and their use in human organizations.
As depicted in Table I, directive leadership influences human behavior by relying on aspects of
command-and-control.
The utilization of directive leadership is typically based on legitimate
power
in which
the
leader occupies
a higher position
in the
organizational
hierarchy.
Transactional leadership involves using the concept of personal and material rewards to motivate
subordinates to achieve higher performance.
By aligning subordinate contribution to equitable
returns,
performance
can
be
appropriately
aligned
to
the
goals
of
the
organization.
Transformational leadership focuses on providing a global vision to unify disconnected tasks and
individuals into achieving a common goal. Through transformational leadership, subordinates are
motivated to increase productivity for the common good. Empowering leadership focuses on
transitioning subordinates from dependency on supervisory direction to self-driven behavior.
Leaders accomplish this practice by engaging all individuals in teamwork behavior as well as
encouraging self-improvement and self-leadership.
In [17], the concept of the socio-technical system was established to formalize the reciprocal
interrelationship between humans and machines. The theory states that humans can be made to
adjust to technologies and technologies can correspondingly be made to adjust to humans.
Following this theoretical vein, we elect to capitalize on the large body of research focused on
human organizations and transplant the theories to the human-robot interaction space. In this
manner, we can use understood practices of human leadership to adjust robot technologies to
respond to the familiar ways in which humans comfortably can embrace these technologies.
Leadership Style
Role of Leader
Situational Context
Directive
* Issue Commands
*
Crisis Situation
* Assign Goals
Subordinates are new to task
Transactional
* Monitor Performance
* Need
to
assess
and
dispense
awards
for
* Provide rewards
performance
Transformational
* Provide Vision
*
Need to change course of action
*
Need to unify group around long-term purpose
Empowering
* Encourage
teamwork,
self-
*
Need to develop new leaders
leadership, and development
*
Need to draw on subordinate's knowledge
Table I: Overview of leadership styles in human organizations [15]
3. LEADERSHIP STYLES IN HUMAN-ROBOT INTERACTION
To understand the role human leadership styles play in human-robot interaction scenarios, we
must first define the human-robot space of interaction and map the situational context in which
each leadership style is most appropriate. We must then determine which behavior, for both the
human and robot, is most appropriate. From there, we can draw on the wealth of knowledge in
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:11:50 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 3]**
*(This page contains a figure/chart/image not captured in text)*

the robotics research arena to determine techniques to enable the necessary robot behavior for
increasing performance in human-robot navigation scenarios.
We define a human-robot navigation scenario based on two dimensions - the goal and the
task. The goal defines the solution to a problem. In organizational scenarios, the goal is similar, in
nature, to measurable results. The task defines the actual steps required to achieve the goal. In
human organizations, this is defined as the actual job assignment. Each of these dimensions has
unique attributes. Task attributes have the following characteristics:
*
Known/Unknown: A known task is one in which both the inputs needed to perform the task
are defined, and progress toward goal achievement (output/results) can be measured. An
unknown task is one in which either parameter (input or output) cannot be determined.
For
example, a robot traversal task in which the robot must traverse from a known initial position
to an identifiable goal position is classified as known.
In this case, the robot can compare
starting and ending criteria to determine if the traversal task is near completion. In the
unknown
case,
a robot traversal
task can be
defined
in which the
goal
position
is
undetermined at task startup (for example, a buried landmine located at an unknown target
position).
In this case, the robot cannot directly determine whether it is making satisfactory
progress toward achieving the goal.
*
Individual/Collaborative: An individual task is one in which an agent can perform a task
(though it might be a collective sequence of tasks) without requiring assistance from any
other agent. A collaborative task is one in which an agent requires additional assistance from
another agent to perform their individual task. For example, a robot navigation task in which
the robot is required to locate a specified rock by navigating within a specified terrain region
is classified as individual.
If the robot requires the assistance of another robot to then
transport
the
specified
rock
to
another
location,
the
associated
task
is
classified
as
collaborative.
Goal attributes have the following characteristic:
*
Time Critical/Available: A time-critical goal is one in which results must be achieved in as
minimal time as possible. For example, a robot exploration task in which the robot must find
sources of energy to maintain its power becomes time-critical when its batteries are near
depletion. A time-available goal is one in which time is not a stringent resource constraint on
achieving results such as a robot exploration task with resources of unlimited solar power.
3.1. Situational Context of Leadership Style
Based on the attributes that define human-robot navigation scenarios, we now analyze the
situational context in which leadership styles can be mapped to the human-robot interaction
space.
Table II shows the descriptive relationship between situational context and the human-
robot interaction space.
Using this relationship, we can define the mapping between leadership
styles and the attributes that define human-robot navigation scenarios, as shown in Table III.
Situational Context
Human-Robot Interaction Space
Directive
*
Goal must be achieved in critical time
*
Crisis Situation
*
Tasks
must
be
taught
to
robot
agent
before
*
Subordinates are new to task
implementation
Transactional
*
Goal is divisible into individual tasks
* Need to assess/dispense awards
*
Tasks are achievable by individual robot agents
Transformational
*
Tasks are collaborative
*
Need to change course of action and
*
Goal achievement can be monitored by individual agents
unify group around long-term purpose
Empowering
*
Agents require information from others to determine
*
Need to develop new leaders
goal achievement
*
Need
to
draw
on
subordinate's
*
Tasks
are
collaborative and may
rely on
individual
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:11:50 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

knowledge
heterogeneous robot agents
Table II. Situational Context of Leadership Style
Directive
Transactional
Transformational
Empowering
|Goal
Time Critical
X
Gol
Time Available
X
X
X
Known
X
X
X
Task
Unknown
X
Task
~Individual
X
X
Collaborative
X
X
Table III. Leadership styles mapped to human-robot navigation scenarios
From Table II, we see that a human-robot navigation scenario that has a time-critical goal and
a known set of tasks to achieve the goal correlates to a crisis situation in which the leader is
responsible for issuing commands (or tasks).
Thus, such a human-robot navigation scenario can
be implemented more effectively by using practices from directive leadership. On the other hand,
if the goal is time-critical, but the task steps are unknown, the best one can do is to combine
elements of directive and empowering leadership to achieve success.
3.2 Leader and Follower Behavior
We assume that the leadership position in human-robot navigation scenarios is always held by the
human agent, and as such, the robot, in all cases, acts as the follower. Table IV combines the role
of the leader defined for the different leadership styles, and highlights the corresponding role of
the robot follower.
Leadership Style
Human Leader Behavior
Robot Follower Behavior
Directive
* Issue Commands
*
Follow commands issued by leader
* Assign Goals
Transactional
* Monitor Performance
*
Select the best task/goal
that provides the
* Provide rewards
highest reward (i.e. maximize reward function)
Transformational
* Provide Vision
*
Determine if task behavior is consistent with
goal
*
Maximize
individual
performance,
while
minimizing conflict with others
Empowering
* Encourage teamwork
*
Select tasks which maximize performance of
* Encourage follower leadership
overall team (i.e. if another robot has a higher
and development
performance value for task, do not select)
*
If failing to perform task, ask team-member
for assistance
*
If do not have skills to perform a task, learn
new capability from leader or team-member
Table IV. Human and robot behavior associated with leadership styles
Given the role of the robot subordinate, we can draw on the wealth of knowledge in the
robotics research arena and identify techniques (as well as challenges) that enable the necessary
robot behaviors.
In this paper, we will discuss and compare the directive and transactional
leadership styles.
4. EXPERIMENTAL RESULTS
4.1 Experimental Setup
To test the theory presented on leadership styles in human-robot navigation scenarios, we utilize
HumAnS-3D (Figure 1), a 3D virtual test environment that has been developed to allow human
access to a virtual representation of the world and control of a virtual robot [18]. The control
panel on HumAnS-3D allows the human operator to directly command the robot to move
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:11:50 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 5]**
*(This page contains a figure/chart/image not captured in text)*

forward, backward, and turn either left or right.
The graphical user interface also connects the
virtual robot, viewable by the human user, to the real robot for seamless integration with the real
world environment. Our assumption is that given the difference situational contexts, performance,
as defined in [8] (i.e. a function of workload on the human operator and time required to complete
a task) will be maximum if the appropriate leadership style is employed.
4.2 Modeling Directive Leadership
In the directive leadership scenario, a robot subordinate follows commands issued by the human
leader. To model directive leadership, a human user is required to directly command the robot
behaviors through tele-operation via the HumAnS-3D interface.
N;,.
iiiiiiiiiii _ -
_=_~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~E~N-
Lft
~
Figure 1. HumAnS-3D environment depicting virtual robot
4.3 Modeling Transactional Leadership
In the transactional leadership scenario, a robot subordinate selects the best task corresponding to
the highest reward.
It is the role of the human leader therefore to provide rewards that
correspondingly guide the robot to a desired goal solution. A technique to facilitate selection of
correct
robot
behavior
in
transactional
leadership
scenarios
is
genetic,
or
evolutionary,
algorithms.
Genetic algorithms are an adaptive method in which a search is performed to find a
set of behaviors that maximize an objective function [19]. In human-robot navigation scenarios,
the objective function can be defined by the human leader in order to guide the robot to the
desired goal solution.
To model the transactional leadership style within the domain of human-robot interaction, an
action-reward structure must be provided that is built upon a lower level communication scheme.
Using a traditional genetic algorithm would imply an action-reward behavior, but communication
between the human user and the robotic agent would be minimal.
In traditional genetic
algorithms, a user would provide a fitness function and the algorithm, after several generations,
would develop solutions to maximize fitness according to the provided fitness function. Though
this may be perceived as an action-reward type interaction, its rigid nature leads it away from
being a good model for transactional leadership. Hence, our proposed solution is a genetic
algorithm whose fitness function varies in real time and in accordance with a human leader's
desires. This avoids reprogramming fitness functions whenever the human leader desires to attain
a solution in an unforeseen manner.
In our application, the genetic algorithm begins with a pseudo-random initialization of 10
chromosomes (a solution path) consisting of 20 genes (a grid point in the environment). The
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:11:50 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

fitness function for finding an optimal solution is built on a combination of three functions. One
function provides a measure of how well a path reaches a desired target. The second provides a
measure of how well a path minimizes the distance traveled in reaching a desired target and the
third function measures how much of the environment is traversed, irrespective of the target.
During the initialization stage, each function is weighted equally to determine fitness. Through
operator use of the HumAnS-3D interface, however, these weights are altered as a function of
user feedback. The concept is that user preference would allow the fitness standard to be
dynamically allocated in real time.
For implementation, the system runs through iterations of the genetic algorithm, and displays
the five highest ranked paths to the user. The user then selects what they consider their top two
choices. The associated chromosomes are then reinserted into a completely new gene pool of a
new instance of the genetic algorithm. Hence, on the next run, convergence occurs at a faster rate
and an optimization function based on the statically weighted fitness function is designed. By
introducing this human-in-the-loop implementation, the user, in essence, acts as the dynamic
portion of the fitness standard.
4.4 Test Results
To validate our adaptation of the leadership paradigm, we execute the directive and transactional
leadership styles under different scenarios and then compare the corresponding performance
metrics for each experimental set. Workload was determined by using the NASA TLX subjective
assessment method' [20] and task performance was determined by monitoring execution time.
In each scenario, the mission defined for the human-robot team is as follows. There are 5
obstacle blocks and 3 target blocks located within the environment (Figure 2a). The environment
is defined by a lOx10 grid, with one block (target or obstacle) randomly positioned in one of the
grid cells. The user is required to visit the 3 target blocks while avoiding the 5 obstacle blocks
(Figure 2b). The human must implement the task under the 4 scenario types: directive/time
critical, transactional/time critical, directive/time available, and transactional/time available. For
the directive/time critical and transactional/time critical scenarios, the human is told that the task
must be completed within 4 minutes. For the directive/time available and transactional/time
available scenarios, the human is provided unlimited time to complete the task.
(a)
(b)
Figure 2. (a) Environment at task initialization. (b) Environment at task completion.
For the directive leadership style, the human directs the robot by directly controlling the
movement of the robot using the available Forward, Back, and Turn buttons on the HumAnS-3D
interface. For the transactional
leadership
style, the human directs the robot by providing
direction to the robot via path suggestions. In this case, the top five paths computed by the genetic
algorithm are provided as input to the user, and the user selects the two best paths for navigation.
The NASA TLX subjective assessmnelnt mnethod measures the relative importanlce of six factors (menltal demanld,
physical demanLd temporal demanLd efttort pertormance, frustrationr level) in determininLg how much workload a humanr
exeine
duin
tas
impemetaton
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:11:50 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

We ran through each scenario with our human participation set and recorded task execution
times. After each experimental run, we also provided the NASA TLX questionnaire to the human
operators to assess workload (i.e. stress on the human operator).
The normalization of the
execution times for each of the users was then computed such that:
Ph,n
ExecutionTime(h,n)
NormalizedExecutionTime (h,n)
Ph,n
(1)
pi,
i=1 j=I
where n designates the current scenario run, s designates the number of total runs, h designates
the human participant, k designates the total number of participants, and ExecutionTime is the
execution time associated with run n and human participant h.
In addition, the normalization of workload values computed from the NASA TLX workload
assessment method was calculated such that:
Oh,n
Workload(h,n)
NormalizedWorkload(h,n)
°h
(2)
EOh, j
j=1
where Workload is the workload values computed from the NASA TLX questionnaire associated
with human participant h and run n.
In Figure
3, we compare the performance and workload values computed for the four
scenarios. Performance, in this case, is computed as (1 - NormalizedExecutionTime), which
associates faster implementation times with better performance.
As we see from Figure 3, the
directive leadership style correlates to faster execution times than the transactional leadership
style, but results in higher workload on the human operator, which is perhaps the greatest
contributor to human error in many systems [21].
In directive leadership scenarios, a faster
execution time is more desired than reducing the workload on the human operator, so directive
behavior is more applicable to improving team efficiency. We note that instituting a time-factor
for completion of a scenario though only increases performance by 12.5% on average, but
increases workload by 18.5%. In transactional leadership styles, we want to minimize workload
(and thus human error), by allowing individual agents to achieve individual tasks. We have
shown that this is achievable through the use of behaviors associated with the transactional
leadership style.
Performance Comparison of Leadership Styles
Workload Comparison of Leadership Styles
ransa tional/TimeAvai
I
Transactional/TmeA
va!Iable
Directive/TimeAvaabl
D!rective T!meAvailable
TransactAonaA
ime Criticai
l
TransactionaI/Tim!e Critical
Directive/Time Critias
Directive/TIme CAitical
TransactonalTimeAvalabi
e...
TransactAonal/TimneAvailabeS
Transactional/ime Critical
Transactionel/Tirne Critica
Directive/Time AvallabAe
Directive/Timse Available
Directive/Time Ctit5ca
DiAretive/Timse Critical
0
0~2
OA
0.6
0.8
0
0.2
O.4
0.6
0.8
1
(a)
(b)
Figure 3. (a) Comparing performance values for the directive and transactional leadership styles.
(b) Comparing workload values for the directive and transactional leadership styles.
5. CONCLUtSIONS
In this paper, we have discussed the linkage between human leadership styles and human-
robot interaction scenarios,
We have adapted a leadership paradigm to employ different styles
gie
he vaiu
siutoa
contexts possible
Future efforts will focus on validating and
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:11:50 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 8]**
*(This page contains a figure/chart/image not captured in text)*

comparing the
other leadership
styles
of transformational
and empowering,
as
discussed
previously. By utilizing practices found in human relationships, we hope to improve our ability
to design human-robot systems for inclusion into our everyday lives.
6. ACKNOWLEDGEMENTS
This research was partly funded through the Draper Laboratory Research and Development
Program. We acknowledge the support of Dr. Craig Pearce at Peter F. Drucker Graduate School
of Management for his constructive suggestions and comments.
7. REFERENCES
1.P.M. Fitts, Human engineering for an effective air-navigation and traffic control system, Washington,
DC: National Academy of Sciences Archives, 1951.
2.H.E. Price, R. E., Maisano, and H.P VanCott, The allocation of function in man-machine systems: A
perspective and literature review, Oak Ridge National Laboratory, 1982.
3. D. R. Olsen, Jr., and M. A. Goodrich, "Metrics for evaluating human- robot interactions," Proceedings
of PERMIS 2003, September 2003.
4. M. Sierhuis, et. al., "Human-Agent Teamwork and Adjustable Autonomy in Practice," Proc. 7th Int.
Symp. on Artificial Intelligence, Robotics and Automation in Space, Nara, Japan, 2003.
5. P.
Rani,
N.
Sarkar,
and
C.
A.
Smith,
"Affect-sensitive
human-robot
cooperation-theory
and
experiments," Proc. of the Int. Conference on Robotics and Automation, pp. 2382-2387, 2003.
6. P. Scerri, D. Pynadath, and M. Tambe, "Towards adjustable autonomy for the real-world," Journal of Al
Research (JAIR), 2002, Volume 17, Pages 171-228.
7. A. Howard, "Role Allocation in Human-Robot Interaction Schemes for Mission Scenario Execution,"
IEEE Int. Conference on Robotics and Automation, May 2006.
8. A. Howard, "A Methodology to Assess Performance of Human-Robotic Systems in Achievement of
Collective Tasks," IEEE/RSJ Int. Conf. on Intelligent Robots and Systems, August 2005.
9. R. Parasuraman, T.B. Sheridan, and C.D. Wickens, "A model for types and levels of human interaction
with automation," IEEE Tran. on Systems, Man, and Cybernetics-Part A, 30(3), 286-297, 2000.
10. T. Fong and C. Thorpe, "Robot As Partner: Vehicle Teleoperation With Collaborative Control", Multi-
Robot Systems: From Swarms to Intelligent Automata, Kluwer, 2002.
11. D.J. Bruemmer and M. Walton, "Collaborative Tools for Mixed Teams of Humans and Robots,"
Multi-Robot Systems, Washington, D.C. March 2003
12.
J. Scholtz, "Human-Robot Interactions: Creating Synergistic Cyber Forces," Proceedings 2002 NRL
Workshop on Multi-Robot Systems, Washington, D. C., 2002.
13.
J. Malasky, L. Forest, "Experimental Evaluation of Human-Machine Collaboration in Resource
Allocation and Planning for Multiple UAVs," IEEE Int. Conf. on SMC, Oct. 2005.
14. C. Pearce, et. al., "Transactors, transformers and beyond: a multi-method development of a theoretical
typology of leadership," Journal of Management Development, 22(4), 2003.
15. H.P. Sims and C.C. Manz, Company of Heroes: Unleashing the Power of Self-Leadership, 1995.
16.
J. F. Cox, et. al. "Toward a Broader Leadership Development Agenda: Extending the Traditional
Transactional-Transformational Duality by Developing Directive, empowering, and Shared Leadership
Skills," The Future of Leadership Development, Eds. Murphy and Riggio, London, 2003.
17. E. Trist, "The Evolution of Socio-Technical Systems: A Conceptual Framework and an Action
Research Program," Issues in the Quality of Working Life, Vol. 2, Toronto, 1981.
18. A. M. Howard and W. Paul, "A 3D Virtual Environment for Exploratory Learning in Mobile Robot
Control," IEEE Int. Conference on Systems, Man, and Cybernetics, Oct. 2005.
19. L. Davis, Handbook of Genetic Algorithms, New York, Van Nostrand Reinhold, 1991.
20.
S. Hart and L. Staveland, "Development of the NASA-TLX: Results of empirical and theoretical
Research," In P. Hancock and N. Meshkati (Eds.), Human mental workload, Amsterdam, 1988.
21. B. Hahler, S. Dahl, R. Laughery, "Crewcut - A Tool for Modeling the Effects of High Workload on
Human Performance," Proc. of the Human Factors Society Conference, Maryland, 1991.
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:11:50 UTC from IEEE Xplore.  Restrictions apply. 
