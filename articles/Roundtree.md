# Roundtree

*Source file: Roundtree.pdf — 50 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

Vol.:(0123456789)
Swarm Intelligence (2021) 15:237–286
https://doi.org/10.1007/s11721-021-00194-6
1 3
Human‑collective visualization transparency
Karina A. Roundtree1 · Jason R. Cody2 · Jennifer Leaf3 · H. Onan Demirel1 · 
Julie A. Adams3
Accepted: 10 May 2021 / Published online: 3 June 2021
© The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2021
Abstract
Interest in collective robotic systems has increased rapidly due to the potential benefts that 
can be ofered to operators, such as increased safety and support, who perform challenging tasks in high-risk environments. The limited human-collective transparency research 
has focused on how the design of the models (i.e., algorithms), visualizations, and control 
mechanisms infuence human-collective behaviors. Traditional collective visualizations 
have shown all of the individual entities composing a collective, which may become problematic as collectives scale in size and heterogeneity, and tasks become more demanding. 
Human operators can become overloaded with information, which will negatively afect 
their understanding of the collective’s current state and overall behaviors, which can cause 
poor teaming performance. This manuscript contributes to the human-collective domain 
by analyzing how visualization transparency infuences remote supervision of collectives. 
The visualization transparency analysis expands traditional transparency assessments by 
focusing on how operators with diferent individual capabilities are impacted, their comprehension, the interface usability, and the human-collective team’s performance. Metrics 
that efectively assess visualization transparency of collectives are identifed, and design 
guidance can inform future real-world human-collective systems designs. The individual 
agent and abstract screen-based visualizations were analyzed while remotely supervising 
sequential best-of-n decision-making tasks involving four collectives, composed of 200 
entities each, 800 in total. The abstract visualization provided better transparency by enabling operators with diferent individual diferences and capabilities to perform relatively 
the same and promoted higher human-collective performance.
Keywords Transparency · Visualization · Collectives · Human–robot interaction
1 Introduction
The design of human-collective robotic systems, which are comprised of human operators and large (i.e., hundreds or thousands of entities) robotic systems that exhibit biologically inspired behaviors, must leverage fundamental human factors visualization principles in order to aid accurate perception and comprehension of information that informs 
* Karina A. Roundtree 
roundtrk@oregonstate.edu
Extended author information available on the last page of the article

---
**[Page 2]**
*(This page contains a figure/chart/image not captured in text)*

238 Swarm Intelligence (2021) 15:237–286
1 3
operator actions. Transparency, the principle of providing easily exchangeable information to enhance comprehension (Roundtree et al. 2019b), can help attain meaningful and 
insightful information exchanges between the operator and the collective. Integrating transparency into the human-collective system design, such as implementing visualization techniques, can help limit poor operator behaviors and improve the human-collective system’s 
overall efectiveness. Achieving transparency becomes more challenging as the collective 
system’s scale changes, and the amount of information needed increases in order to understand the collective’s current, or planned actions. Providing too much, or too little transparency may overload, or underload, respectively, the operator and negatively afect the 
desired outcomes, similar to the arousal–performance trade-of in the Yerkes–Dodson law 
(Yerkes and Dodson 1908). Designers of collective systems, which are composed of large 
groups (i.e., hundreds or thousands of entities) of simplifed individual robotic entities, will 
experience challenges due to the quantity and quality of the information provided by the 
individual entities. There is a need to investigate how system components, such as the visualization, impact human-collective behaviors (i.e., human-collective interactions and performance) in order to achieve transparency for realistic collective use scenarios.
Collective robotic systems that emulate a bee colony searching for a new hive location 
exhibit characteristics of both biological spatial swarms (Brambilla et al. 2013) and colonies (Gordon 1999). A subset of the colony leaves to search for the daughter colony’s new 
hive (Seeley 2010). The subset of bees fy to a nearby tree branch, where they wait while 
scout bees search the surrounding area. During the initial fight, the bees exhibit spatial 
swarm behaviors, similar to those found in schools of fsh (Couzin et al. 2005) and focks 
of birds (Ballerini et al. 2008). Scout bees fnd possible hive locations and evaluate each 
option. The scouts return to the waiting colony in order to begin a selection process (i.e., 
colony behavior) entailing debate and building consensus on the best hive location (i.e., 
best-of-n (Valentini et al. 2017)). After completing a consensus decision-making process, 
the bees travel to the new hive location, transitioning from colony behaviors to spatial 
swarm behaviors. The bees transition to colony behaviors at the new hive.
Collective robotic system attributes, such as global intelligence and emergent behaviors, 
are advantageous for task completion, because collectives are: (1) scalable (i.e., can change 
in size) (Brambilla et al. 2013), (2) resilient to failures (i.e., responsibilities can be redistributed to other collective entities) (Bayindir and Şahin 2007), and (3) fexible in varying 
environments (Hein et  al. 2015; Komareji and Boufanais 2013), as well as the type of 
robotic entities (i.e., heterogeneous members). Collectives have many proposed applications to aid human operators in conducting challenging tasks, such as environmental monitoring, exploration, search and rescue missions, infrastructure support, and protection for 
military applications (Şahin and Spears 2005). Adding a human operator, who may possess 
information that a collective does not, can positively infuence the collective’s consensus 
decision-making process by minimizing the time to make decisions and ensuring the collective selects a higher valued option.
The complexity of human-collective systems challenges designers to determine an 
appropriate quantity and quality of information necessary to support an accurate perception of the collective’s state, comprehension of what the collective is doing currently and 
why, as well as what the collective plans to do in the future. Investigations analyzing the 
system design elements, such as models (Cody et al. 2021), visualizations, operator control 
mechanisms, and the interactions (Roundtree et al. 2020) that transpire at the junction of 
these components, are necessary in order to understand how to achieve transparency for 
human-collective systems. This manuscript analyzed visualization transparency provided 
to a single human supervisor (Scholtz 2003) using a traditional collective representation,

---
**[Page 3]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 239
1 3
Individual Agents (IA) (Roundtree et al. 2019a), and an abstract Collective (Cody 2018) 
representation. The human-collective system incorporated four hub-based collectives, each 
tasked with making a series of sequential best-of-n decisions (Valentini et al. 2017). Each 
collective was to choose the best option from a set of n options, as described in the honeybee nest site search example (Seeley 2010). The objective was to determine which visualization achieved better transparency by evaluating how the visualized information impacted 
operators with diferent individual capabilities, their comprehension, the interface usability, 
and the human-collective team’s performance. Focusing on the visualization is necessary, 
considering the means of communication and interaction with remote collectives will only 
occur via a screen-based interface. Realistic use scenarios will rely heavily on the operator’s visual sensory system. Understanding how the visualization design, such as the use of 
information windows, icons, or colors to represent diferent collective states, impacts the 
operator’s ability to positively infuence the collective’s decision-making process is necessary to inform transparency focused design guidelines for human-collective systems.
2 Related work
Factors that afect transparency, or are infuenced by transparency, such as explainability, 
usability, and performance, that can be measured to assess the visualizations are discussed. 
Understanding the transparency factors, which originated in the human-machine and 
human-robot domains, and how they infuence the human-collective system is necessary in 
order to inform design decisions. A review of transparency research focused on designing 
and evaluating collective visualizations with respect to methods of achieving transparency 
is presented. The collective visualization transparency literature included research focused 
on systems that enabled interaction with large collectives (i.e., hundreds of thousands of 
entities) remotely navigating in large environments. The primary and most frequent interface types that accurately support remote supervision are screen-based. Other interfaces, 
such as augmented reality (e.g., Chen et al. 2020), have been considered; however, these 
types of interfaces are not discussed due to the small number of entities (e.g., 20) that composed these systems.
2.1 Transparency factors
Transparency has been defned as the communication (Mercado et al. 2016), process (Nedbal et al. 2013), method (Lyons et al. 2017), mechanism (Theodorou et al. 2017), property 
(Selkowitz et al. 2015), concept (Hepworth et al. 2020), emergent characteristic (Ososky 
et al. 2014), explanation (Kim and Hinds 2006), and quality (Chen et al. 2014) of an interface to support operator comprehension of a system’s intent. Chen et al.’s transparency definition (Chen et al. 2014) is commonly used in the robotics domain and uses the Situation 
awareness-based Agent Transparency (SAT) framework, which leverages the human operator trust calibration 3Ps model (purpose, process, and performance) with performance history (Lee and See 2004), Endsley’s situation awareness (SA) model (Endsley 1995), and 
the Beliefs, Desires, and Intentions Agent framework (Rao and Georgef 1995), in order to 
achieve transparency.
Transparency for this manuscript builds on Chen et  al.’s defnition and is defned as 
the principle of providing information that is easy to use (Kaltenbach and Dolgov 2017) 
in an exchange between human operators’ and collectives to promote comprehension

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

240 Swarm Intelligence (2021) 15:237–286
1 3
(Alarcon et al. 2017; Lyons 2013; Mark and Kobsa 2005), intent, roles, interactions (Chen 
et al. 2018), performance (Chen et al. 2014), future plans, and reasoning processes (Helldin 2014; Theodorou et al. 2017). The term principle describes the process of identifying 
what factors afect and are infuenced by transparency, why those factors are important, 
how the factors may infuence one another, and how to design a system to achieve transparency. A subset of transparency factors that originated from human–machine literature 
(Roundtree et al. 2019b), shown in Fig. 1, will be used to assess the visualization transparency. Six factors impact transparency directly and are represented as blue ovals connected 
to the transparency node by solid black lines. The three highest total degree (number of in 
degree + number of out degree) direct factors are explainability, usability, and performance 
(dark blue). Information and understanding (light blue) are not considered high degree factors, because explainability uses information to communicate and promote understanding. 
Observable, the ability to be perceived, was not considered a high degree factor due to the 
low number of in and out connections. Explainability and usability, which is a multifaceted 
quality that infuences the operator’s perception of a system, are used for the implementation of transparency in the visualization. Performance can be used to assess the visualization transparency by determining how well a human-collective team was able to produce 
an output when executing a task under particular conditions (Alarcon et al. 2017).
The yellow rectangles represent factors that impact visualization transparency indirectly. The timing and quantity of information visualized on an interface, such as collective status or feedback, require consideration of the human operator’s capability limitations 
(Entin et al. 1996), system limitations, as well as task and environmental impacts, in order 
to be explainable (Atoyan et al. 2006). Human-collective efciency and efectiveness can 
be improved by visualizing information, such as predicted collective states, in a clear and 
cohesive manner that helps alleviate the time and efort an operator must exert to integrate 
information in order to draw conclusions (John et al. 2005) and justify particular actions 
(Fox et  al. 2017). Poor judgments may occur if the operator lacks an understanding of 
what the collective is doing due to poor visualization usability, which may cause operator 
dissatisfaction. Visualizations that do not provide needed information to the operator and 
Fig. 1 Concept map showing a subset of direct and indirect transparency factors (Roundtree et al. 2019b) 
assessed in this human-collective evaluation

---
**[Page 5]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 241
1 3
system control mechanisms to efectively infuence collective behavior will hinder humancollective performance, lower operator situational awareness (SA), impact workload negatively, and potentially compromise safety of the human-collective team. Understanding the 
relationships between the direct and indirect factors, and their relationship to transparency, 
is needed in order to assess metrics that can quantify good design of human-collective 
visualizations.
2.2 Collective visualization transparency
Three design methods that have been used frequently to optimize transparency and desired 
outcomes (i.e., efective team interactions and high performance) in traditional humanmachine systems are: (1) provide system features, such as status, feedback, planning mechanisms, and engagement prompts, (2) use specifc guidelines, such as Gestalt principles, 
to design a system, or (3) train the operators and system (Roundtree et  al. 2019b). The 
majority of the collective visualization transparency literature has focused primarily on 
the frst two design methods of providing system features and using specifc guidelines to 
design the collective visualizations. Most evaluations used training, the third method, only 
to teach operators how to interact with their specifc systems (Brown et al. 2016; Nagavalli et al. 2015), but did not analyze how diferent training strategies may impact transparency. More training may be required for diferent collective visualizations due to difculties understanding the presented information. Determining what strategies have been used 
and their associated outcome success rates in remote teaming with collectives, as well as 
methods that can be evaluated more in depth, such as training, will aid in the development 
of transparency guidelines for collective visualizations.
The collective transparency literature that uses traditional collective visualizations 
(i.e., showing the position of all individual entities) has focused on assessing operator 
understanding of collective behavior and human-collective performance. A variety of 
individual collective entity features have been visualized for operators, including current and predicted future position (Walker et  al. 2012) and heading direction (Brown 
et  al. 2016), health (i.e., speed, strength, and capability Haas et  al. 2009), and status 
(Hussein et al. 2020). The most commonly used visual icon for an individual collective 
entity has been a circle, where directional information was observed either as the entity 
moves across a 2-D space, or the circle also encompassed a line pointing in the heading direction. Displaying information redundantly, such as the use of written messages 
(e.g., recommendations), a numeric value of UAVs supporting the message, and highlighting the supporting UAVs using specifc color coding are efective ways to implement transparency. A visualization that leveraged displaying information redundantly 
improved reliance behavior by enabling operators to accurately accept or reject recommendations; however, the increase in transparency resulted in longer response times. 
(Hussein et al. 2020). The use of multimodal cues (i.e., visual collective state color coding and written messages, spoken messages, and vibrations) aided operators in the identifcation and response of signals during a reconnaissance mission (99.9% accuracy), as 
well as shorter response times, and lower workload. Sharing collective information via 
multimodal cues may alleviate an operator’s high visual loads when managing multiple tasks on various displays by increasing SA (Haas et al. 2009) and promoting better 
transparency. Operators’ using a visualization incorporating Gestalt-based design principles perceived and approximated optimal swarm performance faster than operators

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

242 Swarm Intelligence (2021) 15:237–286
1 3
using visualizations containing only individual entity position information (Nagavalli 
et  al. 2015). Increased visualization transparency enabled operators to learn when to 
approximate optimal input timing.
Information latency, which occurs due to communication bandwidth limitations, and 
neglect benevolence, the time allowed for a collective to stabilize before issuing new 
operator commands, on operator understanding of future collective behavior are important considerations (Walker et al. 2012). Latency afected operators’ ability to control a 
collective, but providing additional transparency via a predictive visualization, which 
showed the predicted location of each individual entity 20 s into the future, mitigated 
these efects. Operators using the predictive visualization with latency performed as 
well as operators who experienced no latency. Transparency of human-collective systems can be improved by implementing predictive visualizations of the collective and its 
entities by allowing the operator more time to think about their future actions. Operators 
will be able to balance span, the number of individual collective entities they interact 
with, and persistence, the duration of the interactions with visualizations that provide 
heading information (Brown et al. 2016). Aspects, such as the presence or absence of 
Couzin et al.’s communication model states (Couzin et al. 2002), visualized individual 
collective entities’ velocity, and individual operator characteristics, such as gender, have 
impacted the identifcation of swarming behavior (Harvey et al. 2018). Understanding 
the infuence of factors is necessary to promote perception and comprehension of collective behavior to inform future operator actions.
Abstract visualizations of collectives have been proposed to improve operator understanding and infuence positive collective behavior. Radial visualizations, using the 
SAT model (Chen et  al. 2014) and heuristic evaluations analyzing the application of 
collective metrics on visualizations (Manning et  al. 2015), as well as glyphs (Walker 
et al. 2019), bounding ellipses (Walker et al. 2016), convex hulls, and directed arrows 
(Roundtree et al. 2018) have been assessed. Similar system features provided in the traditional visualizations were conveyed using the abstract visualizations. The radial visualizations promoted perception (SAT Level 1) by displaying mission (Crandall et  al. 
2017) and collective state information (Ashcraft et al. 2019), such as the direction the 
entities left the hub to explore environmental targets. Predictions of future collective 
headings (SAT Level 3) that were provided by elongating the radial display in the direction of more collective support aided operator actions. Visualizations providing predictive information are needed to achieve transparency for human-collective systems, 
regardless if the visualization is traditional or abstract. Operators using a glyph were 
able to acquire information regarding the collective’s power levels, task type, and the 
number of individual entities, via one icon (Walker et  al. 2019). Additional information about particular system features was accessible via pop-up windows. Designers of 
abstract collective visualizations can ensure transparency by providing redundant information via the collective icon and using supplementary information windows. Conficting results were found for evaluations assessing whether traditional or abstract visualizations aided operators better during diferent tasks. Abstract visualizations during 
a go-to and avoid task in the presence or absence of obstacles (Roundtree et al. 2018) 
performed worse than the traditional visualizations, while abstract visualizations performed as well or better when perceiving biological collective structure (Seifert et al. 
2015) and under variable bandwidth conditions (Walker et al. 2016). Further analysis is 
needed in order to determine which collective visualization will promote better transparency for a common task by investigating how transparency factors infuence humancollective behaviors.

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 243
1 3
3 Human‑collective task
The human-collective task involved a single human operator who supervised and assisted 
four robotic collectives that performed a sequential best-of-n decision-making task, where 
the human-collective team chose the best target option (e.g., best area for occupation) from 
a fnite set of n options (Valentini et al. 2017). The human-collective team performed two 
sequential decisions per collective (moved the collective to a new hub site). The decisionmaking task entailed (1) the identifcation and (2) selection of the highest valued target 
within a 500 m detection range of the current hub, (3) the collective hub moved to the 
selected target, and (4) initiated the second target selection decision. The consensus decision-making task required a quorum detection mechanism to estimate when the highest 
valued target was identifed by 30% of the collective (Cody 2018). Each collective of 200 
simulated Unmanned Aerial Vehicles searched an urban area of approximately 2 km2
.
The four collective hubs were visible at the start of each trial. Targets became visible 
as each was discovered by a collective’s entities, which performed correlated random 
walks when exploring the environment. The target’s location was identifed (100% successful detection) when the individual collective entities were within sensory range (12.8 
cm) and the value was assessed (10% random noise assessment). The target’s existence was 
established when the collective entities returned to their respective hub in a straight line 
to report the target’s location and value. Over time the motion of the individual collective 
entities emulated that of ants following pheromone trails and a straight link was formed 
between the collective and respective targets. The simulated motion and thickness of the 
link, which indicated how many individual collective entities were traveling to and from 
targets, only perceptible on the Individual Agents visualization, may have aided operator 
perception and comprehension of collective support for specifc targets. The collectives 
were only allowed to discover and occupy targets within their search range, but some targets were within proximity of multiple hubs. A collective’s designated search area changed 
after it moved to a new target to establish the new hub site. The operator was instructed to 
prevent multiple collectives merging by not permitting their respective hubs to move to the 
same target. When a collective moved to a target, the hub moved to the target location, and 
the target was no longer visible to the operator or available to other collectives. The collective that moved its hub to a target’s location frst, when two collectives were investigating 
the same target, moved to the target location, while the second collective returned to its 
previous location. Both collectives made a decision when a merge occurred, even though 
only one collective moved its hub to the respective target location.
The interface design requirements, related to collective autonomy, control, and transparency, are: (1) enable the operator to estimate the collectives’ decision-making process, 
(2) identify appropriate controls to infuence the decision-making process, and 3) implement the desired controls (Cody 2018). Two out of three algorithmic models (M2 and M3) 
assessed by Cody et al. (2021) were used in this evaluation. A sequential best-of-n decision-making model (M2) adapted an existing model (M1) (Reina et al. 2015), to base decisions on the target’s quality (i.e., value) and compensated for a collective’s bias toward targets that are close, known as environmental bias, in order to make quality decisions within 
a maximum exploration range. The M1 did not consider environmental bias, which can 
result in selecting lower value targets closer to the collective hub instead of higher value 
targets located further away. Information exchanges between a collective’s entities were 
restricted inside the hub, to mimic honeybees. Episodic queuing cleared messages when 
the collective entities transitioned to diferent states, which resulted in more successful and

---
**[Page 8]**
*(This page contains a figure/chart/image not captured in text)*

244 Swarm Intelligence (2021) 15:237–286
1 3
faster decision completion (Cody et al. 2021). Interaction delay and interaction frequency 
were added as bias reduction methods in order to consider a target’s distance from the collective hub and increase interactions among the collectives’ entities regarding possible hub 
site locations (Cody et al. 2021). Interaction delay improved the success of choosing the 
ground truth best targets, and interaction frequency improved decision time. The baseline 
model (M3) allows the collective entities to search and investigate potential targets, but was 
unable to build consensus. The operator was required to infuence the consensus-building 
element and select that fnal target, based on the consensus. Simulations were ran without 
an operator for the M2 model in order to understand the operator’s infuence on collective 
behavior, referred to as M2 SIM. The M3 model required operator infuence in order to perform the decision-making task; thus, simulation-only analysis was not conducted.
The interface controls allowed the operator to alter the collectives’ internal states and 
their levels of autonomy, throughout the sequential best-of-n selection process. The collective’s entities were in one of four states. Uncommitted entities explored the environment 
searching for targets, and were recruited by other entities while inside of the collective’s 
hub. Collective entities that favored a target reassessed the target’s value periodically, and 
attempted to recruit other entities within the collective’s hub to investigate the specifed target. Collective entities were committed to a particular target once a quorum of support was 
detected, or after interacting with another committed entity. Executing collective entities 
moved from the collective’s current hub location to the selected target’s location. A collective operated at a high level of autonomy by executing actions associated with potential 
targets independently. The operator was able to infuence the collective’s actions in order 
to aid better decision-making, efectively lowering the level of autonomy. Communication 
from the operator with the collective’s entities occurred inside the hub in order to simulate 
limited real-world communication capabilities. The control mechanisms, for infuencing 
the collective, were communicated to the specifed hub.
The two visualizations were designed considering how specifc design elements can 
promote transparency by providing particular types of information (i.e., a transparency factor). The relationships between the design elements and the transparency factors in Fig. 1, 
as well as the implications of particular design elements on the transparency factors, are 
emphasized using italics. The visualizations were evaluated in order to determine which 
visualization provided better transparency by facilitating the operator’s perception of the 
collectives’ states, comprehension of the collectives’ decision-making processes, and 
means to infuence future collectives’ actions. The analysis will substantiate what design 
elements promote transparency and inform design guidelines that can be used for future 
human-collective systems.
3.1 Individual agents interface
The individual agents (IA) interface, see Fig. 2, exemplifes a traditional collective visualization by displaying the location of all the individual collective entities (Roundtree 
et al. 2019a). The interface was divided into three primary areas: (1) the central map, (2) 
the collective request area, and (3) the monitor area. The map, located at the center of 
the interface visualizes the respective hubs, their individual entities, discovered targets, 
and other associated information. A static central map was used to provide ecological 
validity and emulate a task of searching an urban environment for potential locations 
of interest. Understanding the environment’s composition and how it may infuence 
particular collective behavior is necessary to develop an accurate mental model of the

---
**[Page 9]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 245
1 3
working environment and can impact the operator’s decision-making and mission performance. Both the collectives and targets were rectangular boxes with distinguishing 
identifers located at the center of the icon. The collectives had Roman numeral identifers (I–IV), while the targets used integers (0–15). Discovered targets initially were 
white and transitioned to a green color when at least two individual collective entities 
evaluated the target. The highest valued targets were a bright opaque green (e.g., Target 
0 in Fig. 2), while lower valued targets had a more translucent green color (e.g., Target 
9 in Fig. 2). Targets that were within the collective’s 500 m search range had diferent 
colored outlines, depending on the collective’s state: explored targets that were not currently favored had yellow outlines, explored targets that were favored had white outlines 
(e.g., Target 12 in Fig. 2), and targets that were abandoned have red outlines (e.g., Target 13 in Fig. 2).
The individual collective entities began each trial by exploring the environment in an 
uncommitted state, which transitioned to favoring as targets were assessed and supported. 
The individual collective entities committed to a target once 30% of the collective (60 entities) favored a particular target. The collective executed a move to the selected target’s 
location once 50% of the collective (100 entities) favored the target. The individual collective entities’ state information was conveyed via individual collective entity color coding: 
uncommitted (yellow), favoring (green), committed (blue), and executing (blue). A legend 
of the collective entities’ and target border colors was provided in the lower right-hand 
corner, see Fig. 2, in order to alleviate workload. The number of individual collective entities in a particular state, or supporting a target was provided via the collective hub and 
target information pop-up displays, which provided detailed information, represented as 
gray rectangular boxes, displayed directly on the map in Fig. 2. The information displays, 
when accessed, appeared in a particular location relative to the respective collective’s hub 
or target. The operator was able to move the information displays by dragging the pop-up 
display to a desired location.
Fig. 2 Individual agents (IA) interface two and half minutes into a trail, showing four collectives (rectangles with Roman numerals), and the sixteen discovered targets (rectangles with integers). The target’s value 
is represented by the green color, where higher values were brighter. The legend in the lower right corner 
identifes the individual collective entity state information and target range information (color fgure online)

---
**[Page 10]**
*(This page contains a figure/chart/image not captured in text)*

246 Swarm Intelligence (2021) 15:237–286
1 3
The operator had the ability to infuence an individual collectives’ current state via 
the collective request area, located on the lower left-hand side of Fig. 2. The investigate
command permitted increasing a collective’s support for an operator specifc target. Ten 
uncommitted entities (5% of the collective population) transitioned to the favoring state 
after receiving and acknowledging the investigate command. Additional support for the 
same target was achieved by reissuing the investigate command repeatedly. The abandon 
command reduced a collective’s support for a specifc target by transitioning favoring individual entities to the uncommitted state. The abandon command only needed to be issued 
once in order for the collective to ignore a specifed target. A collective’s entities stopped 
exploring alternative targets and moved to the operator selected target when the decide
command was issued, which was a valid request when at least 30% of the collective supported the operator specifed target. The process to issue a command required selection of 
the desired command from the drop down menu, followed by the selection of the desired 
collective and target, and the request was completed by clicking on the commit button. The 
reset button cleared entered information, allowing the operator to request new information. The highlight agents selection box identifed which individual entities belonged to a 
particular collective. When the highlight agents box was selected, the specifc individual 
collective entities associated with a hub were highlighted with a white border to distinguish 
them from the other entities. The highlight was deactivated by deselecting the highlight 
agents selection box, which removed the check mark.
The collective assignments area logged the operator’s issued commands, shown in the 
upper right-hand corner of the monitor area in Fig. 2. The log displayed what commands 
were issued with respect to particular collectives and targets, for example, Collective I: 
Abandon Target 3. The green and red circles next to each command signifed whether the 
command was completed (red) or currently active (green). An investigate command initially had a green circle and transitioned to red once ten individual entities received and 
acknowledged the investigate command for a particular target. Issued abandon commands 
for a particular collective and target remained active. Once a collective reached a decision, all prior commands associated with that particular collective were removed from the 
collective assignments log. The only command the operator was able to cancel was the 
abandon command, which required selecting the desired abandon command, in Fig. 2, the 
“Collective I: Abandon Target 3”, and selecting the cancel assignment button.
System messages, located between the collective assignments and legend shown on the 
right-hand side of the monitor area in Fig. 2, indicated the actions taken by the operator 
and collectives. The illegal message was displayed when an operator requested an invalid 
command, and justifed why the requested action was not viable. Three situations resulted 
in illegal messages. The frst arose when the operator attempted to issue an investigate 
command for targets that were outside of the collective’s search region. The second situation occurred when the operator attempted to abandon newly discovered targets that did not 
have an assigned value (white targets). The last message arose when operators attempted to 
issue decide commands when less than 30% of the collective supported a target.
3.2 Collective interface
The Collective interface, shown in Fig. 3, provides an abstract visualization that does not 
represent individual collectives’ entities (Cody et al. 2021). The Collective interface was 
divided into the same three primary areas as the IA interface. The static map was the same 
image used in the IA visualization. Due to diferences in the display monitors (IA: 1920

---
**[Page 11]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 247
1 3
× 1080 vs. Collective: Unknown) and the visualization systems (IA: Unity vs. Collective: 
QT) the image placement may have appeared slightly diferent. Precautions associated with 
zooming into the image and image placement relative to the interface were taken in order 
to maintain relatively consistent sized collective and target icons, as well as the information 
windows. The operator’s visual angle, which infuences the perception of objects, may have 
been afected by the display monitor, as well as the distance between the operator and the 
respective monitor. The distance between the operator and display monitor was not measured for either IA or Collective evaluation, since the operator’s comfort was a priority during the evaluation sessions. Future evaluations can use the same sized display monitors in 
order to mitigate diferences in perception; however, limiting the operator’s position relative to the display monitor is not recommended, since it may negatively impact their ability 
to perform the task.
The Collective interface functionality was the same as the IA interface, excluding the 
highlight agents function since the individual collective entities were not visualized. Only 
the visualization design diferences of the Collective interface are discussed and include 
the collective and target icons, state information, as well as some modifcations to the collective and target outlines. The collectives were represented as gray and white rectangles 
with four quadrants and Roman numeral identifers located at the top center of the icon. 
Collective state information was conveyed via the collective icon’s quadrants, color coding, 
and information windows. The collective icon’s contained four state quadrants [uncommitted (U), favoring (F), committed (C), and executing (X)], which represented the number 
of individual entities currently in each state, where a brighter white quadrant equated to 
larger numbers of individual collective entities. The square target icons had integer identifers positioned on the upper right hand corner. Targets contained two sections, where the 
top green section represented the target’s value, where the brighter and more opaque the 
green, the higher the value (e.g., Target 8 in Fig. 3). The blue section indicated the number 
Fig. 3 Collective interface mid-way through a trail scenario, showing the current locations of the four 
collectives (rectangles with Roman numerals) and the locations of the discovered targets (green and blue 
squares with integer identifers). The top half of each target indicates the target’s relative value (green) and 
the bottom half indicates the support of the highest supporting collective (blue). The legend in the upper 
left hand corner identifes the target range information (color fgure online)

---
**[Page 12]**
*(This page contains a figure/chart/image not captured in text)*

248 Swarm Intelligence (2021) 15:237–286
1 3
of individual entities favoring a particular target, where the brighter and more opaque the 
blue, the higher the number of collective entities (e.g., Target 12 in Fig. 3).
The collective interface operated similar to the IA interface with some distinctions. A 
target was outlined in blue, Target 0 in Fig. 3, when the collective’s support exceeded 30%. 
The target transitioned to a green outline, and the collective was outlined in green when the 
collective began executing a move to the target’s location. The collective’s outline moved 
from the hub to the target’s location to indicate the hub’s transition to the selected target. 
The interface’s legend appeared in the upper left corner, see Fig. 3.
4 Experimental design
The primary research question was to determine which visualization achieved better transparency. A between-visualization analysis was used to analyze the data between the IA and 
Collective visualizations. Four secondary questions were developed in order to investigate 
how the visualization impacted a direct transparency factor, exclusive of trust. The frst 
research question (R1) focused on understanding how the visualization infuenced the operator. Individual diferences, such as experience level, will impact an operator’s ability to 
interact with the visualization efectively and cause diferent responses (e.g., loss of SA). A 
visualization that can aid operators with diferent capabilities is desired. The explainability 
factor was encompassed in R2, which explored whether the visualization promoted operator comprehension. Perception and comprehension of the visualized information are necessary to inform actions. Understanding which visualization promoted better usability, R3, 
will aid designers in promoting efective transparency in human-collective systems. The 
fnal research question, R4, assessed which visualization promoted better human-collective 
performance. A system that performs a task quickly, safely, and successfully is ideal.
The independent variables included the between visualization variable, IA versus Collective, and trial difculty (overall, easy, and hard). Trials that had a larger number of high 
valued targets in closer proximity to a collective’s hub were deemed easy, while hard trials 
placed high valued targets further away from the hub. The dependent variable details are 
embedded into the sections associated with each research question.
4.1 Experimental procedure
The experimental procedure for both evaluations began with a demographic questionnaire, 
followed by the Mental Rotations test (Vandenberg and Kuse 1978), after which the participants received training and practiced using the interface. Two practice sessions occurred 
prior to each trial in order to ensure familiarity with the underlying sequential best-of-n
(M2) and baseline (M3) models. The M2 model trial was always completed frst during the 
IA evaluation, in order to alleviate any learning efects from using M3. The Collective evaluation randomized the order of the M1 and M2 models, which were always presented before 
the M3 model. The researchers used the same scripts to instruct the participants that the 
objective was to aid each collective in selecting and moving to the highest valued target 
two sequential times. A trial began once the respective practice session was completed. 
Each trial was divided into two components (one easy and one hard) of approximately ten 
minutes each. Splitting each trial into two components allowed the simulation environment 
to reset with 16 new (not initially visible) targets. The easy and hard trial orderings were 
randomly assigned, and counterbalanced across the participants. The SA probe questions

---
**[Page 13]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 249
1 3
(Cody 2018), intended to serve as a secondary task, were asked beginning at 50 s into 
the trial and were repeated at one-minute increments. Six SA probes were asked during 
each trial component, or twelve per trial. The trial was terminated once the team completed 
eight decisions, two per collective, or once six decisions were made, if the trial length 
exceeded the ten-minute limit. Decision times were not limited. A post-trial questionnaire 
was completed after each trial and the post-experiment questionnaire was completed before 
the evaluation termination.
Both evaluations were conducted in a faculty ofce with a similar furniture confguration. All participants sat, in an adjustable chair, in front of a computer monitor with 
access to a keyboard and mouse when performing the evaluation tasks. The participant and 
researcher were the only two individuals in the room throughout the evaluation in order to 
ensure privacy and mitigate distractions. It is possible that slight diferences in the room 
size, lighting, and temperature may have infuenced diferent operator behaviors, but care 
was taken to remove these variables.
4.2 Participants
The participants from both evaluations completed a demographic questionnaire, which collected information regarding age, gender, education level, weekly hours on a desktop or 
laptop (0, less than 3, 3–8, and more than 8), and their video game profciency from little 
to no profciency (1) to high profciency (7). The Mental Rotation Assessment (Vandenberg and Kuse 1978) required participants to judge three-dimensional object orientation 
to assess spatial reasoning within a scoring range of 0 (low) to 24 (high). Efective spatial 
reasoning enables participants to understand what objects are, how the objects move in a 
particular space, and where the objects are located. The mode is reported in parenthesis for 
questions that required selection to a group.
4.2.1 IA evaluation
Fourteen females and nineteen males (33 total) completed the IA evaluation at Oregon 
State University. The predominant (25) age range was between 18 and 30 years, with seven 
participants in the 31 and 50 range and one participant being 60 and older. Many participants were in the process of obtaining (8) or had an undergraduate degree (13), a master’s 
degree (9), or a doctorate degree (1). The mean number of weekly hours participant’s used 
a desktop or laptop was 3.79, with a standard deviation (SD) = 0.5, median (med) = 4, 
minimum (min) = 2, and maximum (max) = 4. Participants ranked video game profciency 
as mean 4.61 (SD = 1.93, med = 5, min = 1, max = 7). The Mental Rotation Assessment 
(Vandenberg and Kuse 1978) mean was 12.36 (SD = 5.85, med = 12, min = 3, and max = 
24) (Roundtree et al. 2019a).
4.2.2 Collective evaluation
Twenty-eight participants, 15 females and 13 males, from Vanderbilt University, completed 
the Collective evaluation. The majority of participants (24) were between 18 and 30 years 
old, with four between 31 and 50. Most of the participants completed high school and 
were in the process of obtaining (11) or had completed an undergraduate degree (13). The 
weekly hours participant’s used a desktop or laptop was slightly higher than that of the IA 
(mean = 3.86, SD = 0.45, med = 4, min = 2, and max = 4). The participants’ video game

---
**[Page 14]**
*(This page contains a figure/chart/image not captured in text)*

250 Swarm Intelligence (2021) 15:237–286
1 3
profciency was ranked lower than the IA (mean = 3.61, SD = 2.23, med = 2.5, min = 1, 
and max = 7). The participants’ Mental Rotations Assessment scores were also slightly 
lower (mean = 10.93, SD = 5.58, med = 10, min = 1, and max = 24) (Roundtree et al. 
2019a).
4.3 Analysis
Five participants were excluded from the IA evaluation due to inconsistent methodology 
(1) and software failure (4). The between-visualization analysis is based on 56 participants 
from both evaluations. The frst twelve decisions made per participant using the M2 model 
were analyzed. The majority of the objective metrics were analyzed by SA level (overall (SAO), perception (SA1), comprehension (SA2), and projection (SA3)), decision difculty (overall, easy, and hard), timing with respect to a SA probe question [15 s before 
asking (B), while being asked (W), or during response (D) to a SA probe question], or per 
participant. Nonparametric statistical methods, including Mann–Whitney–Wilcoxon tests 
with one degree of freedom and Spearman Correlations, were calculated due to a lack of 
normality. The correlations were with respect to SA probe accuracy and selection success 
rate. The Collective evaluation data were reanalyzed using the same methods. Secondary 
research question’s hypotheses, associated metrics, results, and discussion are provided in 
Sects. 5–8.
5 R1: Visualization infuence on human operator
Understanding how the visualization infuenced the operator, R1, is necessary to determine if the transparency embedded into the system design aided operators with diferent 
capabilities. The associated objective-dependent variables were (1) the operator’s ability 
to infuence the collective in order to choose the highest target value, (2) SA, (3) visualization clutter, and (4) the operator’s spatial reasoning capability (Mental Rotations Assessment). The specifc direct and indirect transparency factors related to R1 are identifed in 
Fig. 4. The relationship between the variables and the corresponding hypotheses, and the 
direct and indirect transparency factors, is presented in Table 1. Additional relationships 
Fig. 4 R1 concept map of the assessed direct and indirect transparency factors

---
**[Page 15]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 251
1 3
Table 1 Visualization infuence on the human operator objective (obj) and subjective (subj) variables (vars), relationship to the (H), as well as the associated direct and indirect transparency factors, are presented in Fig. 1Obj vars H Transparency factors
Direct Indirect
Explainability Observable Performance Under- standing Usability Capability Efective- ness Predict- ability SA Satisfaction Timing Workload
Target value H1 ✓
SA probe accuracy H1 ✓ ✓ ✓ ✓ ✓ ✓ ✓Local clutter H1 ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓Global clutter H1 ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓Mental rotations 
assessment
H2 ✓ ✓
Subj vars Weekly hours 
on a desktop or laptop
H2 ✓ ✓
 Video Game 
Profciency
H2 ✓ ✓
 NASA task load 
index
H1, H3 ✓ ✓ ✓ ✓ ✓ ✓
 3-D situational 
awareness rating technique
H1 ✓ ✓ ✓ ✓ ✓

---
**[Page 16]**
*(This page contains a figure/chart/image not captured in text)*

252 Swarm Intelligence (2021) 15:237–286
1 3
(not identifed in Fig. 1) between the variable and the direct or indirect transparency factors 
are identifed due to correlation analyses.
Operators may have performed diferently depending on their individual diferences. 
It was hypothesized (H1) that operators using the Collective visualization will experience 
signifcantly higher SA and lower workload. SA represents an operator’s ability to perceive and comprehend information in order to project future actions that must be taken in 
order to fulfll a task (Endsley 1995). Usability infuences the perception of information 
(Roundtree et al. 2019b) and will impact workload, which is the amount of stress an operator experiences in order to accomplish a task during a particular duration of time (Wickens et  al. 2004). It was hypothesized (H2) that operators with diferent individual capabilities will not perform signifcantly diferent using the Collective visualization. An ideal 
visualization will enable operators with diferent capabilities to perceive, comprehend, and 
infuence collectives relatively the same. Training can alleviate any disparities between 
operators, but is only intended to supplement the system’s design. The operator’s attitude 
and sentiments toward a system, which is dependent on system usability, provide essential 
information related to the system’s design (Kizilcec 2016). Good designs promote higher 
operator satisfaction. It was hypothesized (H3) that operators using the Collective visualization will experience signifcantly less frustration (i.e., higher satisfaction).
5.1 Metrics and results
Assessing variables, such as the selected target value for each human-collective decision, 
is necessary in order to determine whether operators were able to perceive the target value 
correctly and infuence the collectives positively. The objective of the human-collective 
team was to select the highest valued target for each decision from a range of target values 
(67 to 100). The selected target value is the average of all target’s respective values that 
were selected by the human-collective teams during a trial. The descriptive statistics for 
the selected target value per decision difculty (Dec Dif) are shown in Table 2. Operators 
using the Collective interface were able to infuence the collective to choose higher valued 
targets, regardless of decision difculty, on average; however, the Mann–Whitney–Wilcoxon test identifed no signifcant efects between visualizations for the selected target 
value.
The SA-dependent variable was SA probe accuracy, which is the percentage of correctly 
answered SA probes questions used to assess the operator’s SA during a trial (Cody 2018). 
Each question corresponded to the three SA levels: perception, comprehension, and projection (Endsley 1995). Participants were asked fve SA1, four SA2, and three SA3 questions. 
The SA1 questions determined the operator’s ability to perceive information about the 
Table 2 Selected target value 
descriptive statistics by decision 
difculty, where the maximum 
possible value was 100 and the 
minimum possible value was 67
Dec dif Mean (SD) Med (min/max)
IA Overall 90.29 (7.11) 95 (67/97)
Easy 90.21 (7.29) 95 (67/97)
Hard 90.4 (6.88) 94 (68/96)
Coll Overall 92.05 (5.08) 95 (68/96)
Easy 92.09 (5.54) 95 (68/96)
Hard 92 (4.5) 95 (78/96)

---
**[Page 17]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 253
1 3
collectives and targets, such as “What collectives are investigating Target 3?” The operator’s comprehension of information was represented by the SA2 questions, such as “Which 
Collective has achieved a majority support for Target 7?” SA3 questions related to the operator’s ability to estimate the collectives’ future state, such as “Will support for Target 1 
decrease?” An overall SA value, SAO, represented the percent of correctly answered SA 
probes out of 12 total. The SA probe accuracy descriptive statistics are shown in Table 3
(Roundtree et al. 2019a). Operators using the Collective visualization had higher SA probe 
accuracy, regardless of the SA level. The Mann–Whitney–Wilcoxon tests (n = 56) found 
highly signifcant efects between visualizations for SAO (U = 702, 𝜌 < 0.001) and SA1 (U
= 714.5, 𝜌 < 0.001). Moderately signifcant efects were found for SA2 (U = 572.5, 𝜌 < 
0.01) and SA3 (U = 554, 𝜌 < 0.01).
Local and global clutter percentages were analyzed for each SA probe question. Clutter is 
defned as the area occupied by objects on a display, relative to the total area of the display 
(Wickens et al. 2004). Presenting too much information in close proximity to one another will 
require the operator to search longer for information (Wickens et al. 2004) and can negatively 
infuence the accuracy of the SA probe questions. Area coverage for each 2-D item was calculated by the number of pixels the item covered on the computer visualization. The conversion 
between meters and pixels was used to determine where items were in the environment and 
was diferent for each visualization due to diferences in the monitor displays. The conversion was determined using screen shots of both visualizations. One meter for the IA visualization was approximately 1.97 pixels per meter, and the Collective visualization was approximately 2.3 pixels per meter. The local clutter percentage variable was the percentage of area 
obstructed by items that were displayed within the 500 m (i.e., approximately 254 pixels for 
the IA visualization and 218 pixels for the Collective visualization) circular radius from the 
center of the collective, or target of interest in the SA probe question. Collective IV, for example, is the collective of interest in the following SA probe question: “What is the highest value 
target available to Collective IV?” The items obstructing the 500 m radius when using the IA 
visualization, in Fig. 2, for the previous SA probe question are: the Collective IV, Targets 9 
and 12–15, and 200 individual entities. Some SA probe questions encompassed more than one 
collective or target of interest, which required calculating the local clutter percentage for each 
collective or target and summing the values together. All calculations frst required converting 
meters into pixels in order to ensure equivalent units. The Collective visualization computer 
display size was unknown; therefore, local and global clutter percentage calculations use the 
corresponding item and computer display dimensions from the IA visualization. Future clutter 
Table 3 SA probe accuracy (%) 
descriptive statistics by SA level Level Mean (SD) Med (min/max)
IA SAO 65.3 (18.87) 68.33 (16.67/83.33)
SA1 58.57 (23.05) 60 (20/100)
SA2 72.32 (21.88) 75 (25/100)
SA3 65.48 (34.52) 66.67 (0/100)
Coll SAO 89.88 (10.96) 91.67 (58.33/100)
SA1 91.67 (11.11) 100 (66.67/100)
SA2 88.39 (14.6) 100 (60/100)
SA3 89.88 (20.46) 100 (33.33/

---
**[Page 18]**
*(This page contains a figure/chart/image not captured in text)*

254 Swarm Intelligence (2021) 15:237–286
1 3
assessments will require the display dimensions in order to mitigate the potential error introduced in this evaluation. Local clutter (%) was calculated using Eq. 1:
where LHA represents the area corresponding to the number of collective hubs (2464 
pixels2
 per hub) inside the 500 m radius. The area corresponding to the number of highlighted targets (2350 pixels2
 per highlighted target), which have outlines and are in range 
of the currently selected collective, is represented as LHTA, while the targets that are not 
highlighted (1720 pixels2
 per target) are denoted as LTA. LAICE represents the area corresponding to the number of individual collective entities (64 pixels2
 per agent) inside of 
the 500 m radius and was excluded from the Collective visualization local clutter percentage calculation, because no individual entities were displayed. The individual collective 
entities were confned to the 500 m search radius around their respective collective hub; 
therefore, the calculation assumes that the 200 entities associated with each collective 
are inside of the local radius. The area corresponding to the number of target information 
pop-up windows (32,922 pixels2
 per target information pop-up window) is represented as 
LTIW, and the corresponding collective information pop-up windows (25,740 pixels2
 per 
collective information pop-up window) are represented as LCIW. Only target or collective 
information pop-up windows that belong to targets or collectives inside of the 500 m radius 
are considered. The Collective evaluation did not record which particular collective information pop-up windows were visible; therefore, LCIW is excluded from the local clutter 
percentage calculation for the Collective visualization.
The local clutter (%) descriptive statistics 15 s before asking, while being asked, and during a SA probe response are provided in Table 4. The Collective evaluation did not record the 
SA probe response time; therefore, the average response time per SA level from the IA evaluation was used for all calculations during response to a SA probe question. The maximum 
local clutter percentage was 177%, which indicated that the area covered by the associated 
items of the collective or target of interest in the SA probe exceeded the 500 m radius. Local 
clutter percentages larger than 100% were attributed to the area covered by the collective and 
target information pop-up windows. The location of the information pop-up windows was not 
recorded; therefore, the maximum area coverage was considered when information pop-up 
windows did not occlude items in the environment. The maximum area coverage condition 
was not refective of the real trial environment, where information pop-up windows covered 
items on the central map. The IA visualization had lower local clutter, regardless of when the 
metric was collected for SAO, SA1, and SA3. No correlations were found between local clutter 
and SA probe accuracy.
The global clutter, calculated using Eq. 2, was the percentage of area obstructed by all 
objects displayed on the IA computer display (20,736,00 pixels2
), since the Collective computer display was unknown.
where ICA represents the area of the static interface components (493,414 pixels2
), which 
encompass the program bar, the Microsoft Windows program bar, the select trial button, the collective request area, and the monitor area. GHA represents the area covered 
by Collectives I-IV (9856 pixels2
), which were visible throughout the trial duration. The 
area corresponding to the number of highlighted targets (2350 pixels2
 per highlighted 
Local Clutter = (1) ∑(LHA + LHTA + LTA + LAICE + LTIW + LCIW
𝜋 ⋅ 5002
)
⋅ 100,
(2)
Global Clutter =
(ICA + GHA + GHTA + GTA + GAICE + GTIW + GCIW
2073600
)
⋅ 100

---
**[Page 19]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 255
1 3
target), which have outlines and are in range of the selected collective, is represented as 
GHTA. Remaining targets that are not highlighted (1720 pixels2
 per target) are represented 
as GTA. GAICE represents the area encompassed by 800 individual collective entities 
(51,200 pixels2
), which was only considered for the IA visualization. The area corresponding to the number of target information pop-up windows (32922 pixels2
 per target information pop-up window) is represented as GTIW, and the corresponding collective information 
pop-up windows is represented as GCIW (25740 pixels2
 per collective information pop-up 
window).
The global clutter (%) descriptive statistics 15 s before asking, while being asked, and 
during response to a SA probe question are shown in Table 5. The IA visualization had 
lower global clutter, regardless of when the metric was assessed across all SA levels. The 
Mann–Whitney–Wilcoxon tests found highly signifcant efects between visualizations 
when responding to a SA probe question (n = 670) for SAO (U = 64,442, 𝜌 < 0.001). Moderate signifcant efects were found for SAO 15 s before asking (U = 64,188, 𝜌 < 0.01) and 
while being asked a SA probe question (U = 63,728, 𝜌 < 0.01). Signifcant efects were 
found 15 s before asking a SA probe question for SA1 (n = 294, U = 12,487, 𝜌 = 0.02) and 
SA3 (n = 152, U = 3445.5, 𝜌 = 0.03); while being asked a SA probe question for SA1 (n = 
294, U = 12,301, 𝜌 = 0.03) and SA3 (n = 152, U = 3452, 𝜌 = 0.05); and during the response 
to a SA probe question for SA1 (n = 294, U = 12,216, 𝜌 = 0.04). The Spearman correlation 
Table 4 Local clutter (%) 
descriptive statistics 15 s before 
asking (B), while being asked 
(W), and during response (D) to 
SA probe question by SA level
Time Level Mean (SD) Med (min/max)
IA B SAO 33.6 (21.66) 26.13 (9/124)
SA1 30.79 (19.53) 24.4 (9/122.33)
SA2 41.54 (24.39) 37.75 (9/124)
SA3 28.61 (19.36) 22.23 (9.08/97.7)
W SAO 34.42 (22.16) 28 (9/124)
SA1 31.91 (20.54) 25 (9/122)
SA2 41.67 (24.74) 37.17 (9/124)
SA3 29.73 (19.54) 24.21 (9/97.67)
D SAO 34.26 (22.25) 27.5 (8/124)
SA1 31.84 (20.61) 24.83 (9/122)
SA2 41.28 (24.96) 36.5 (8/124)
SA3 29.68 (19.6) 24 (9/98)
Coll B SAO 35.42 (28.08) 25.44 (9/177)
SA1 34.09 (29.09) 24.04 (9/151.9)
SA2 35.81 (27.53) 26.86 (10.3/177)
SA3 37.98 (26.78) 28.23 (10.4/131.5)
W SAO 35.37 (28.78) 25.75 (9/176.5)
SA1 34.24 (30.37) 23.63 (9/176.5)
SA2 36.47 (26.76) 27.4 (10.2/130.4)
SA3 36.35 (28.27) 27.25 (9/147.56)
D SAO 35.6 (29.19) 25.8 (9/176.4)
SA1 34.29 (29.84) 25 (9/176.4)
SA2 36.55 (27.98) 27 (10/130)
SA3 37.24 (29.86) 26.57 (9

---
**[Page 20]**
*(This page contains a figure/chart/image not captured in text)*

256 Swarm Intelligence (2021) 15:237–286
1 3
analysis found a weak correlation for the Collective visualization for SA1 between global 
clutter 15 s before asking a SA probe question and SA probe accuracy (r = 0.16, 𝜌 = 0.05).
The Mental Rotations Assessment (Vandenberg and Kuse 1978), which assessed the 
operator’s spatial reasoning, identifed no signifcant efects between visualizations. A 
Spearman correlation analysis revealed weak correlations between the Mental Rotations 
Assessment and SA probe accuracy when using the IA visualization for SAO (r = 0.17, 𝜌
< 0.01), SA1 (r = 0.18, 𝜌 = 0.03), and SA2 (r = 0.27, 𝜌 < 0.01). The Mann–Whitney–Wilcoxon tests identifed no signifcant efects between visualizations for the weekly hours 
spent using a desktop or laptop and video game profciency. Weak correlations were found 
between weekly hours using a desktop or laptop and SA probe accuracy for the IA visualization for SAO (r = 0.12, 𝜌 = 0.04) and SA1 (r = 0.21, 𝜌 = 0.01), as well as when using the 
Collective visualization for SA2 (r = 0.21, 𝜌 = 0.02). No correlations were found between 
video game profciency and SA probe accuracy.
The NASA Task Load Index (NASA-TLX) assessed the six workload subscales and the 
weighted overall workload (Hart and Staveland 1988). The descriptive statistics for the 
NASA-TLX demands imposed on the operator are presented in Table  6. The Collective 
visualization imposed a lower overall workload, had lower physical and temporal demands, 
and caused less frustration (Cody et al. 2021). The IA visualization imposed a lower mental demand, which had a signifcant efect between visualizations (n = 56, U = 515, 𝜌 = 
Table 5 Global clutter (%) 
descriptive statistics 15 s before 
asking (B), while being asked 
(W), and during response (D) to 
SA probe question by SA level
Time Level Mean (SD) Med (min/max)
IA B SAO 30.2 (3.06) 28.83 (27/40.22)
SA1 29.88 (2.8) 28.5 (27/40.22)
SA2 30.41 (3.05) 29.1 (27/40)
SA3 30.45 (3.45) 28.85 (27/40)
W SAO 30.25 (3.13) 29 (27/40)
SA1 29.95 (2.91) 28.58 (27/40)
SA2 30.41 (3.12) 29 (27/40)
SA3 30.52 (3.49) 29 (27/40)
D SAO 30.09 (3.02) 29 (27/40)
SA1 29.83 (2.81) 28.5 (27/40)
SA2 30.22 (3) 29 (27/40)
SA3 30.37 (3.38) 28.79 (27/40)
Coll B SAO 31.37 (4.97) 29.21 (27.88/53)
SA1 31.38 (5) 29.13 (28/52.4)
SA2 31.25 (5.09) 29.21 (27.88/53)
SA3 31.56 (4.76) 29.54 (28/52)
W SAO 31.43 (5.13) 29.17 (28/53)
SA1 31.24 (5.26) 29 (28/53)
SA2 31.52 (5.2) 29.22 (28/51.8)
SA3 31.69 (4.78) 29.75 (28/48)
D SAO 31.41 (5.15) 29 (28/53)
SA1 31.43 (5.43) 29 (28/53)
SA2 31.34 (5.08) 29 (28/51.5)
SA3 31.49 (4.66) 29.31

---
**[Page 21]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 257
1 3
0.04) and less efort. The IA visualization had higher performance with a highly signifcant 
efect between visualizations (n = 56, U = 159.5, 𝜌 < 0.001).
The 3-D Situational Awareness Rating Technique (SART) measured the operator’s perceived situational understanding (SU), demand on attentional resources (DAR), and supply of attentional resources (SAR) (Selcon et al. 1991). An overall score was calculated 
using the standard calculation. The SART descriptive statistics are presented in Table  7
(Cody et  al. 2021; Roundtree et  al. 2019a). The minimum SART score was − 1, which 
was unexpected as a negative score requires the supply of attentional resources to exceed 
the demand on attentional resources and a low perceived situational understanding. Both 
of these conditions are highly unlikely. The Collective visualization had a higher overall 
score, more situational understanding, high demands of attentional resources (although 
nearly the same as the IA visualization), and more supply of attentional resources, compared to the IA visualization. The Mann–Whitney–Wilcoxon test indicated moderately signifcant efects between visualizations for the overall score (n = 56, U = 560, 𝜌 < 0.01), 
situational understanding (n = 56, U = 561, 𝜌 < 0.01), and supply of attentional resources 
(n = 56, U = 561, 𝜌 < 0.01).
A summary of R1’s hypotheses with associated signifcant results is provided in Table 8.
Table 6 NASA-TLX descriptive 
statistics Subscales Mean (SD) Med (min/max)
IA Overall 62.14 (14.81) 65.67 (24/85.67)
Mental 19.25 (8.8) 20 (0/33.33)
Physical 1.68 (3.32) 0 (0/13)
Temporal 11.75 (8.24) 9.67 (0/28.33)
Performance 10.69 (5.87) 8.83 (2.67/25)
Efort 11.35 (6.68) 11 (2.67/28.33)
Frustration 7.43 (8.36) 4.67 (0/33.33)
Coll Overall 57.06 (16.47) 56.83 (5.67/83.33)
Mental 23.58 (6.34) 25 (3/31.67)
Physical 0.46 (1.17) 0 (0/4.67)
Temporal 10.94 (7.67) 10.33 (0/24)
Performance 5.1 (4.7) 3.67 (0/21.33)
Efort 12.32 (6.26) 13 (2/25.33)
Frustration 4.65 (6.84) 1.83 (0/30)
Table 7 SART descriptive 
statistics (1-low, 7-high) Dimensions Mean (SD) Med (min/max)
IA Overall 4.64 (2.6) 4.5 (− 1/10)
SU 4.96 (1.53) 5 (2/7)
DAR 5.04 (1.2) 5 (2/7)
SAR 4.71 (1.36) 5 (1/7)
Coll Overall 6.68 (2.26) 6.5 (3/13)
SU 6.07 (0.9) 6 (4/7)
DAR 5.07 (1.18) 5 (1/6)
SAR 5.68 (1.09) 6 (

---
**[Page 22]**
*(This page contains a figure/chart/image not captured in text)*

258 Swarm Intelligence (2021) 15:237–286
1 3
5.2 Discussion
Relationships to the transparency factors provided in Table 8 are emphasized using italics. 
The analysis of how visualization infuenced operators suggests that the Collective visualization promoted better transparency. The variables that directly supported H1 are the SA
performance (i.e., accuracy) and SART. H1 was supported, because operators using the 
Collective visualization had signifcantly higher objective and subjective SA and lower 
overall workload. Transparency embedded into the Collective visualization, via explainable color-coded icons and outlines, state information identifed on the collective icon, 
information provided in the collective and target information pop-up windows, and feedback provided in the Collective Assignments and System Messages areas, promoted better observability, comprehension, and predictability of future collective behaviors, making 
the overall human-collective team more efective. The Collective operators, however, had 
more local and global clutter, even if collective pop-up windows were not considered in 
the local clutter calculation for the Collective visualization. Clutter was mainly attributed 
to the number of collective and target information pop-up windows that were visible. The 
increased clutter has both positive and negative implications for transparency. Clutter, from 
a usability perspective, is not ideal if operators are unable to perform their tasks efectively. The Collective operators who had more global clutter were able to answer higher 
SA performance, which suggests that operators were not hindered by the clutter and performed better than their counterparts. The dependence on having the collective and target 
Table 8 A synopsis of R1’s hypotheses associated with signifcant results
The SA probe timings are all timings (AT), 15 s before asking (B), while being asked (W), and during 
response (D) to a SA probe question. Hypotheses that were fully supported (black bold text), partially supported (black text), and not supported (gray bold text) are identifed. Results for which no statistical tests 
were conducted are shown as merged cells containing hashmarks
Variable Sub-variable Between visual. Correlation
IA Coll
SA probe accuracy SAO H1 –
SA1 H1
SA2 H1
SA3 H1
Global clutter SAO H1 − AT
SA1 H1 − AT H1 − B
SA3 H1 − AT
Mental rotation assessment SAO – H2
SA1 H2
Weekly hours on desktop or laptop SAO H2
SA1 H2
SA2 H2
NASA-TLX Mental H1 –
Perform H1
SART Overall H1
SU H1
SAR H1

---
**[Page 23]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 259
1 3
information pop-up windows visible suggests that the collective state information provided 
on the collective icon was not as efective as the information pop-up window and there is 
a need to provide support information on the target icons. Other design strategies must be 
investigated to improve the efcacy of the collective and target icons for the Collective 
visualization. Further analyses are required to determine what contributed to more mental demand, more efort, and less perceived performance using the Collective visualization and whether the additional stress may have been experienced due to positive aspects, 
such as operators being highly motivated to complete their tasks. The Collective visualization may have required more operator efort in order to understand what the collective 
was doing compared to the IA visualization that showed the dynamic behavior emerging. 
Collective operators may have been distracted by the secondary SA probe question task and 
required more time to refocus their attention on the collective behaviors.
The Mental Rotation Assessment and video-game profciency results supported H2, 
since operators with diferent capabilities did not perform signifcantly diferent using 
the Collective visualization. One exception to the hypotheses was that more experienced 
operators may have performed better due to their extensive use of computers, which may 
have led to faster and more accurate interpretations of information (Wickens et al. 2004) 
(i.e., diferent types of iconography), or easier access to the supplemental information. 
Since the exception was observed in both evaluations, the behavior is inherent to working 
with a computer interface, rather than a particular visualization. Using an abstract collective visualization will mitigate the need for particular operator capabilities to perform the 
sequential best-of-n decision-making task. Collective operators experienced less frustration, which supports H3. Dissatisfaction (i.e., frustration) transpires when the system is 
not transparent and prohibits the operator from understanding what is happening, or there 
is too much clutter and the visualization appears noisy (Preece and Rogers 2007). The 
abstract visualization may be a solution to mitigate dissatisfaction.
The transparency embedded in the Collective visualization supported operators with 
diferent capabilities better than the IA visualization. A transparent human-collective system will mitigate the need for operators to have specifc capabilities in order to efectively
interact with the system and perform tasks. Investigations are needed to determine what 
visualization usability characteristics contributed to higher mental demand in order to alleviate workload.
6 R2: Visualization promotion of human operator comprehension
The explainability direct transparency factor was encompassed in R2, which was interested 
in determining whether the visualization promoted operator comprehension, by embedding 
transparency into the system design. Perception and comprehension of the presented information are necessary to inform future operator actions. The associated objective dependent 
variables were (1) SA, (2) collective and target left- or right-clicks, (3) the percentage of 
times the highest value target was abandoned, and (4) whether the information pop-up window was open when a target was abandoned. The specifc direct and indirect transparency 
factors related to R2 are shown in Fig. 5. The relationship between the variables and the 
corresponding hypotheses, and the direct and indirect transparency factors, is presented in 
Table 9. Relationships between the variable and the direct or indirect transparency factors 
that are not shown in Fig. 1 were identifed after conducting correlation analyses.

---
**[Page 24]**
*(This page contains a figure/chart/image not captured in text)*

260 Swarm Intelligence (2021) 15:237–286
1 3
Thirteen human factors display design principles, associated with perceptual operations, 
mental models, human attention, and memory (Wickens et al. 2004), which suggest that 
information must be legible, clear, concise, organized, easily accessible, and consistent. 
Providing information, such as the collective state, on the collective icon, rather than using 
all of the individual collective entities is more clear, concise, organized, and consistent; 
therefore, it was hypothesized (H4) that operators will have a better understanding of the 
information provided by the Collective visualization. Providing information redundantly 
via icons, colors, messages, and the collective and target information pop-up windows can 
aid operator comprehension and justify their future actions. It was hypothesized (H5) that 
the Collective visualization provided information used to accurately justify actions. An 
ideal visualization will enable operators to perceive and comprehend information that is 
explainable, which will support taking accurate future actions.
6.1 Metrics and results
The operator had access to supplementary information that was not continually displayed, 
such as diferent colored target borders that identifed which targets were in range and had 
been abandoned, or information pop-up windows that provided collective state and target 
support information, in order to aid comprehension (SA2) of collective behavior and inform 
particular actions. The results of SA probe accuracy, which is the percentage of correctly 
answered SA probes questions used to assess the operator’s SA during a trial, identifed 
that operators using the Collective visualization had higher SA probe accuracy, regardless 
of the SA level. Further details regarding the statistical tests are provided in Metrics and 
Results Sect. 5.1 of R1.
Collective left-clicks identifed targets that were in range of a collective (i.e., white borders indicated that the individual collective entities were investigating the target, while yellow indicated no investigation), whether the targets had been abandoned (i.e., red borders), 
and was the frst click required to issue a command. The number of collective left-clicks 
descriptive statistics 15 s before asking, while being asked, and during response to a SA 
Fig. 5 R2 concept map of the assessed direct and indirect transparency factors

---
**[Page 25]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 261
1 3
Table 9 Visualization promotion of human operator comprehension objective (obj) and subjective (subj) variables (vars), relationship to the hypotheses (H), as well as the associated direct and indirect transparency factors, are presented in Fig. 1Obj vars H Transparency factors
Direct Indirect
Explainability Information Observable Performance Understanding Usability Capability Efectiveness Justifcation Predict- ability SA
SA probe 
accuracy
H4 ✓ ✓ ✓ ✓ ✓ ✓ ✓
Collective 
left-clicks by SA level
H5 ✓ ✓ ✓ ✓
Target rightclicks by SA 
level
H5 ✓ ✓ ✓ ✓ ✓
Highest value 
target abandoned
H4, 
H5
✓ ✓ ✓ ✓ ✓
Abandoned 
target information window open
H5 ✓ ✓ ✓ ✓ ✓
Subj vars
 SART H4 ✓ ✓ ✓ ✓ ✓ Post-trial 
performance and understanding
H4 ✓ ✓ ✓ ✓

---
**[Page 26]**
*(This page contains a figure/chart/image not captured in text)*

262 Swarm Intelligence (2021) 15:237–286
1 3
probe question is shown in Table 10. Operators using the IA visualization had fewer collective left-clicks, regardless of when the metric was assessed for all SA levels, except for SAO
during response to a SA probe question. The Mann–Whitney–Wilcoxon tests found highly 
signifcant efects between visualizations for SAO (n = 664) 15 s before asking a SA probe 
question (U = 64,213, 𝜌 < 0.001), while being asked a SA probe question (U = 67,670, 𝜌 < 
0.001), and during response to a SA probe question (U = 64,,710, 𝜌 < 0.001). A highly signifcant efect was also found when responding to a SA probe question for SA2 (n = 223, U
= 8317, 𝜌 < 0.001). Moderate signifcant efects were found for SA1 (n = 290) 15 s before 
asking a SA probe question (U = 12,534, 𝜌 < 0.01), while being asked a SA probe question (U = 12,043, 𝜌 < 0.01), and during response to a SA probe question (U = 12,414, 𝜌 < 
0.01). An additional moderate signifcant efect was found while being asked a SA probe 
question for SA3 (n = 151, U = 3472, 𝜌 < 0.01). Signifcant efects were found 15 s before 
asking a SA probe question for SA2 (n = 223, U = 7210.5, 𝜌 = 0.04) and during response 
to a SA probe question for SA3 (n = 151, U = 3489, 𝜌 = 0.01). No correlations were found 
between the number of collective left-clicks and SA probe accuracy.
Target right-clicks allowed the operator to open or close target information pop-up windows, which provided the percentage of support each collective had for a respective target. 
Operators may have used the support information to justify issuing commands. The number of target right-clicks descriptive statistics 15 s before asking, while being asked, and 
Table 10 Collective left-clicks 
descriptive statistics 15 s before 
asking (B), while being asked 
(W), and during response (D) to 
SA probe question by SA level
Time Level Mean (SD) Med (min/max)
IA B SAO 1.64 (1.84) 1 (0/12)
SA1 1.53 (1.75) 1 (0/11)
SA2 1.78 (1.9) 1 (0/12)
SA3 1.65 (1.92) 1 (0/9)
W SAO 0.49 (0.76) 0 (0/5)
SA1 0.3 (0.6) 0 (0/3)
SA2 0.42 (0.77) 0 (0/4)
SA3 0.33 (0.61) 0 (0/3)
D SAO 1.68 (1.79) 1 (0/11)
SA1 1.14 (1.46) 1 (0/7)
SA2 1.46 (1.8) 1 (0/10)
SA3 1.53 (1.98) 1 (0/9)
Coll B SAO 1.95 (1.57) 2 (0/9)
SA1 1.88 (1.47) 2 (0/8)
SA2 2.13 (1.68) 2 (0/9)
SA3 1.83 (1.61) 1 (0/7)
W SAO 0.69 (0.88) 0 (0/5)
SA1 0.51 (0.79) 0 (0/5)
SA2 0.91 (0.89) 1 (0/4)
SA3 0.73 (0.96) 0 (0/4)
D SAO 1.52 (1.21) 1 (0/6)
SA1 1.32 (1.02) 1 (0/4)
SA2 1.57 (1.21) 1 (0/5)
SA3 1.89 (1.4

---
**[Page 27]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 263
1 3
during response to a SA probe question is presented in Table 11. The Collective visualization had fewer target right-clicks for all SA levels, 15 s before asking and during response 
to a SA probe question, while the IA visualization had fewer while being asked a SA probe 
question. The Mann–Whitney–Wilcoxon test found no signifcant efects between visualizations for the number of target right-clicks. The Spearman correlation analysis revealed 
weak correlations between the number of target right-clicks and SA probe accuracy for the 
IA visualization 15 s before asking a SA probe question for SAO (r = 0.17, 𝜌 < 0.01) and 
for SA2 (r = 0.37, 𝜌 < 0.001).
The abandon command enabled operators to select a collective to discontinue investigating a particular target. Ideally lower valued targets were abandoned, since the objective 
was to aid each collective in selecting and moving to the highest valued target two sequential times. The percentage of times the highest value target was abandoned per participant 
is shown in Table 12. Operators using the IA visualization abandoned the highest value 
target less frequently, but no signifcant efects were found between the visualizations.
The percentage of times an abandoned target information pop-up window was open per 
participant was evaluated and is represented in Table 13. The operator may have used the 
support information in order to justify abandoning a particular target. Participants using the 
IA visualization had fewer abandoned target information pop-up windows open, compared 
Table 11 Target right-clicks 
descriptive statistics 15 s before 
asking (B), while being asked 
(W), and during response (D) to 
SA probe question by SA level
Time Level Mean (SD) Med (min/max)
IA B SAO 1.68 (2.38) 1 (0/13)
SA1 1.92 (2.62) 1 (0/13)
SA2 1.28 (1.91) 1 (0/11)
SA3 1.8 (2.5) 1 (0/12)
W SAO 0.37 (0.79) 0 (0/7)
SA1 0.44 (0.74) 0 (0/4)
SA2 0.31 (0.67) 0 (0/3)
SA3 0.37 (0.75) 0 (0/3)
D SAO 1.07 (1.77) 0 (0/10)
SA1 1.11 (1.69) 0 (0/10)
SA2 1.1 (1.75) 0 (0/9)
SA3 1.68 (2.24) 1 (0/10)
Coll B SAO 1.52 (2.41) 1 (0/18)
SA1 1.79 (2.71) 1 (0/18)
SA2 1.17 (1.94) 0 (0/10)
SA3 1.49 (2.35) 0 (0/11)
W SAO 0.5 (1) 0 (0/9)
SA1 0.49 (0.86) 0 (0/4)
SA2 0.55 (1.31) 0 (0/9)
SA3 0.44 (0.69) 0 (0/2)
D SAO 0.99 (1.7) 0 (0/11)
SA1 1.01 (1.74) 0 (0/11)
SA2 0.84 (1.44) 0 (0/9)
SA3 1.21 (1.98) 0 (0/

---
**[Page 28]**
*(This page contains a figure/chart/image not captured in text)*

264 Swarm Intelligence (2021) 15:237–286
1 3
to the Collective visualization operators. No signifcant efects were found between 
visualizations.
The SART results, which measured the operator’s perceived situational understanding, 
demand on attentional resources, and supply of attentional resources (Selcon et al. 1991), 
were ranked higher for the Collective visualization compared to the IA. The statistical test 
details are provided in Sect. 5.1.
The post-trial questionnaire assessed the operators’ understanding of the collective 
behavior, never (1) to always (7), and their ability to choose the best target for each decision, never (1) to always (7). The post-trial performance and understanding subjective 
descriptive statistics are shown in Table 14 (Cody 2018). Performance and understanding 
were higher for operators using the Collective visualization. The Mann–Whitney–Wilcoxon test found a signifcant efect between visualizations for understanding (n = 56, U = 
513, 𝜌 = 0.04).
A summary of R2’s hypotheses with associated signifcant results is provided in 
Table 15.
Table 12 Highest value target 
abandoned (%) descriptive 
statistics per participant by 
decision difculty
Dec Dif Mean (SD) Med (min/max)
IA Overall 32.36 (29.53) 26 (0/100)
Easy 31.2 (27.17) 25 (0/75)
Hard 42.1 (40.53) 23 (0/100)
Coll Overall 43.6 (31.94) 38 (0/100)
Easy 33.25 (35.96) 27 (0/100)
Hard 48.72 (36.85) 38 (0/100)
Table 13 Abandoned target 
information pop-up window open 
(%) descriptive statistics per 
participant by decision difculty
Dec Dif Mean (SD) Med (min/max)
IA Overall 23.86 (31.43) 10.5 (0/100)
Easy 22.2 (30.95) 13 (0/100)
Hard 28.7 (37.89) 8.5 (0/100)
Coll Overall 33.8 (34.9) 15 (0/100)
Easy 30.7 (37.85) 15 (0/100)
Hard 36.08 (40.87) 14 (0/100)
Table 14 Post-trial performance 
and understanding model ranking 
descriptive statistics (1-low, 
7-high)
Metric Mean (SD) Med (min/max)
IA Performance 5.25 (1.69) 6 (2/7)
Understanding 4.89 (1.75) 5 (1/7)
Coll Performance 5.54 (1.29) 6 (3/7)
Understanding 5.82 (1.16) 6 (3/7

---
**[Page 29]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 265
1 3
6.2 Discussion
The analysis of how visualization promoted operator comprehension (i.e., the operator’s 
capability of understanding) identifed advantages and disadvantages associated with both 
visualizations. The Collective visualization promoted higher comprehension and SA; however, because the Collective operators abandoned the highest value target more frequently, 
H4 was not supported. Inefective identifers, such as the distinction between particular 
roman numerals and integers, may have caused poor observability and IA operator confusion. Ensuring that identifers are unique and distinct, such as integers versus letters, will 
improve system explainability and may mitigate misunderstanding. The target value for 
the Collective visualization may not have been salient enough to distinguish it from other 
potential targets. Further investigations are required to determine if the target value must 
use the entire collective hub icon area, similar to the IA visualization, in order to be recognizable, and to establish what levels of obscurity are needed to ensure that target values are 
distinguishable from one another.
The use of target borders (collective left-clicks), information pop-up windows (target 
right-clicks), and target value were assessed to determine if operators used these types of 
information to accurately justify actions. Collective right-clicks, which opened and closed 
collective information pop-up windows, 15 s before asking, while being asked, and during 
response to a SA probe question, were not analyzed, because the collective evaluation did 
not indicate which collective was selected via the right-click. None of the metrics supported H5, because the information provided by the Collective visualization did not justify accurate actions. Collective left-clicks did not support or hinder SA performance (i.e., 
accuracy) for either visualization, but fewer target right-clicks 15 s before asking a SA
probe question supported higher SAO and SA2 probe accuracy for operators using the IA 
visualization. The operators may have learned to anticipate when SA probe questions were 
going to be asked and took preventative actions, by opening or closing target information
windows, which resulted in higher SA performance. The use of target information popup windows aided Collective visualization users to abandon targets more than 30% of the 
Table 15 A synopsis of R2’s 
hypotheses associated with 
signifcant results. The SA probe 
timings are all timings (AT), 15 
s before asking (B), while being 
asked (W), and during response 
(D) to a SA probe question
Variable Sub-variable Between visual. Correlation
IA Coll.
SA probe accuracy SAO H4 –
SA1 H4
SA2 H4
SA3 H4
Collective left-clicks SAO H5 − AT
SA1 H5 − AT
SA2 H5 − B, W
SA3 H5 − W, D
Target right-clicks SAO H5 − B
SA2 H5 − B
SART Overall H4 –
SU H4
SAR H4
Post-trial Unders. H4

---
**[Page 30]**
*(This page contains a figure/chart/image not captured in text)*

266 Swarm Intelligence (2021) 15:237–286
1 3
time. Further analysis using technology, such as an eye-tracker, may provide more accurate 
metrics to determine operator comprehension during SA probe questions by identifying 
exactly where an operator is focusing their attention.
The transparency embedded in the Collective visualization did not provide the operator with better comprehension, nor did it hinder it compared to the IA visualization. 
Both visualizations infuenced operator comprehension diferently. Further investigations are needed in order to understand how to embed transparency into the system better and identify whether those strategies worked. Unique and distinct information may 
need to be presented on diferent icons, or use diferent presentation strategies, such as 
colors versus patterns, in order to mitigate confusion and improve system usability. The 
target value on the Collective visualization, for example, was on the same icon as the 
collective support and may have challenged operator perception, comprehension, and 
predictability. The information provided by both of the visualizations in general did not 
justify actions.
7 R3: Visualization usability
Understanding which visualization promoted better usability, R3, is necessary to determine which characteristics promote efective transparency in human-collective systems. 
The associated objective-dependent variables were (1) visualization clutter, (2) Euclidean distance, (3) collective and target left- and right-clicks, (4) metrics associated with 
abandoned targets, and (5) the time between the committed state and an issued decide 
command. The specifc direct and indirect transparency factors related to R3 are shown 
in Fig. 6. The relationship between the variables and the corresponding hypotheses, as 
well as the direct and indirect transparency factors, is presented in Table 16. Additional 
relationships that are not identifed in Fig. 1 between the variable and the direct or indirect transparency factors are provided after conducting correlation analyses.
The goal of usability is to design systems that are efective, efcient, safe to use, have 
good utility, easy to learn, and are memorable (Preece and Rogers 2007). Good usability 
is necessary to ensure operator perception and comprehension of the information presented on a visualization and to promote efective interactions. It was hypothesized (H6) 
Fig. 6 R3 concept map of the assessed direct and indirect transparency factors

---
**[Page 31]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 267
1 3
Table 16 Visualization usability objective (obj) variables (vars), relationship to the hypotheses (H), as well as the associated direct and indirect transparency factors, are presented in Fig. 1
Obj vars H Transparency factors
Direct Indirect
Explainability Information Observable Performance Understanding Usability Efectiveness Justifcation Predictability SA Timing
Local clutter H6 ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
Global clutter H6 ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓Euclidean distance 
between SA probe interest and clicks
H7 ✓ ✓
Sum of Euclidean 
distance between clicks
H7 ✓ ✓
Collective left-clicks 
per participant
H7 ✓ ✓ ✓
Collective right-clicks 
per Participant
H7 ✓ ✓ ✓ ✓
Target left-clicks per 
participant
H7 ✓ ✓
Target right-clicks per 
participant
H7 ✓ ✓ ✓ ✓
Highest value target 
abandoned
H6 ✓ ✓ ✓ ✓ ✓
Abandoned target 
information window open
H6 ✓ ✓ ✓ ✓ ✓
Abandon requests 
exceeded abandoned targets
H6 ✓ ✓ ✓ ✓
Time between commit 
state and issued decide command
H6 ✓ ✓ ✓ ✓ ✓ ✓

---
**[Page 32]**
*(This page contains a figure/chart/image not captured in text)*

268 Swarm Intelligence (2021) 15:237–286
1 3
that the Collective visualization will promote better usability by being more predictable 
and explainable. Providing information that is explainable may aid operator comprehension, while predictable information may expedite operator actions. An ideal system will 
not require constant operator interaction to perform well; therefore, it was hypothesized 
(H7) that operators using the Collective visualization will require fewer interactions.
7.1 Metrics and results
Many system characteristics were available to the operators in order to aid task completion. 
The IA visualization had both lower local clutter percentage, which was the percentage 
of area obstructed by items displayed within the 500 m circular radius of a collective, or 
target, and global clutter percentage, which was the percentage of area obstructed by all 
objects displayed on the visualization. Operators using the IA visualization had fewer collective and target information pop-up windows open throughout the trial. The statistical 
test details are provided in Sect. 5.1.
The Euclidean distance (pixels) between the focus of the SA probe question and where 
the operator was interacting with the visualization indicated where operators focused their 
attention and identifed what information was currently being perceived, because no eyetracker was used. Euclidean distance can be used to assess the efectiveness of the object 
placements on the display. Larger distances are not ideal, because more time (Gillan et al. 
1992) and efort is required to locate and interact with the object. The frst requirement 
of calculating the Euclidean distance was to determine what the collective, or target of 
interest was in a SA probe question. For example, Target 3 is the target of interest for the 
following question: “What collectives are investigating Target 3?” The second requirement 
was to determine where the operator was interacting with the system. The Euclidean distance between Target 3 and the operator’s current interaction (i.e., click), which was Collective IV, is identifed by a dashed orange line in Fig. 7. The Euclidean distance between 
SA probe interest and clicks descriptive statistics 15 s before asking, while being asked, 
and during response to a SA probe question are presented in Table 17. Operators using the 
IA visualization had shorter Euclidean distances between the SA probe interest and their 
clicks with the visualization, regardless of when the metric was assessed for all SA levels. 
The Mann–Whitney–Wilcoxon tests found a moderate signifcant efect between visualizations while being asked a SA probe question for SAO (n = 464, U = 31,052, 𝜌 < 0.01). 
Highly signifcant efects were found between visualizations 15 s before asking a SA probe 
question for SAO (n = 557, U = 43,303, 𝜌 = 0.02) and for SA1 (n = 273, U = 10,577, 𝜌 = 
0.05), while being asked a SA probe question for SA1 (n = 229, U = 7645, 𝜌 = 0.01), and 
during response to a SA probe for SAO (n = 499, U = 35,029, 𝜌 = 0.02). The Spearman 
correlation analysis revealed a weak correlation between the Euclidean distance between 
the SA probe’s focus interest and the clicks and SA probe accuracy for the IA visualization 
15 s before asking a SA probe question for SA1 (r = − 0.18, 𝜌 = 0.04).
The sum Euclidean distance (pixels) between clicks was the sum of all distances 
between the operator’s current interaction and the immediately previous interaction. For 
example, if an operator interacted with the visualization four times while a SA probe question was being asked, the sum Euclidean distance is the sum between interactions one and 
two, interactions two and three, and interactions three and four. The operators may have 
had multiple interactions while the experimenter was reading a SA probe question. These 
interactions may have been related to completing a previous action or to attain information to aid comprehension and answer the SA probe question. The summation of Eucl

---
**[Page 33]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 269
1 3
distances between clicks indicates how efective the placement of objects was on the visualization. Larger sum distances suggest that the information operators were seeking was 
either not as easily accessible or further away from the collective or target related to the 
SA probe. The sum of Euclidean distance between clicks descriptive statistics 15 s before 
asking, while being asked, and during response to a SA probe question is presented in 
Table 18. Operators using the Collective visualization had smaller sums of Euclidean distance between their interactions, regardless of when the metric was assessed for all SA levels, with two exceptions. The IA visualization had a smaller sum for SA1 while being asked 
and during response to a SA probe question. The Mann–Whitney–Wilcoxon test found no 
signifcant efects between visualizations. The Spearman correlation analysis found weak 
correlations between the sum of Euclidean distance between clicks and SA probe accuracy 
for the IA visualization 15 s before asking a SA probe question for SA2 (r = 0.2, 𝜌 = 0.04) 
and during response to a SA probe question for SAO (r = 0.14, 𝜌 = 0.02). Weak correlations were found for the Collective visualization while being asked a SA probe question for 
SAO (r = − 0.13, 𝜌 = 0.05) and for SA1 (r = − 0.2, 𝜌 = 0.05).
Collective and target left- and right-clicks were examined per participant. Target leftclicks were the second click required in the process of issuing commands, but did not provide supplementary information. The number of collective and target left- and right-clicks 
descriptive statistics is presented in Table  19. Operators using the IA visualization had 
fewer collective and target left-clicks, while those using the Collective visualization had 
fewer collective and target right-clicks. The Mann–Whitney–Wilcoxon test identifed no 
signifcant efects between visualizations.
Metrics showing how operators used the abandon command were assessed. IA operators 
had lower percentages of times the highest value target was abandoned and lower percentages of times an abandoned target information pop-up window was open per participant. The statistical analyses of both metrics are provided in Sect. 6.1. Instances may have 
occurred when the operator accidentally issued an undesired abandon command or repeatedly issued the abandon command, although the command only needed to be issued once; 
Fig. 7 Example of Euclidean distance between SA probe interest (Target 3) and clicks (Collective IV), 
denoted by an orange dashed

---
**[Page 34]**
*(This page contains a figure/chart/image not captured in text)*

270 Swarm Intelligence (2021) 15:237–286
1 3
hence, the percent of times abandon commands exceeded abandoned targets was examined and the descriptive statistics are shown in Table 20. Operators using the IA visualization had fewer repeated abandon commands for all decision difculties, compared to those 
using the Collective visualization. The Mann–Whitney–Wilcoxon test found no signifcant 
efects between visualizations.
The time diference (minutes) between the committed state and issued decide command
assessed the operator’s ability to predict the collective’s future state changing from the 
committed state (30% support for a target) to executing (50% support for a target). The time 
diference between the committed state and when an operator issued a decide command 
descriptive statistics is shown in Table  21. Operators using the Collective visualization 
had smaller time diferences between the committed state and issued decide commands 
for overall and easy decisions; however, operators using the IA visualization had smaller 
time diferences for hard decisions. The Mann–Whitney–Wilcoxon test found no signifcant efects between visualizations.
A summary of R3’s hypotheses with associated signifcant results is provided in 
Table 22.
Table 17 Euclidean distance 
between SA probe interest 
and clicks (pixels) descriptive 
statistics 15 s before asking 
(B), while being asked (W), and 
during response (D) to SA probe 
question by SA level
Time Level Mean (SD) Med (min/max)
IA B SAO 767 (263) 768 (183/1426)
SA1 760 (252) 765 (269/1426)
SA2 769 (282) 788 (184/1312)
SA3 783 (263) 757 (183/1261)
W SAO 758 (292) 745 (74/1637)
SA1 754 (285) 745 (140/1637)
SA2 768 (316) 782 (160/1383)
SA3 754 (275) 731 (74/1329)
D SAO 764 (299) 758 (74/1637)
SA1 761 (297) 747 (161/1637)
SA2 775 (319) 778 (160/1381)
SA3 758 (278) 750 (74/1284)
Coll B SAO 821 (256) 856 (222/1471)
SA1 826 (264) 828 (250/1471)
SA2 813 (235) 865 (317/1330)
SA3 822 (271) 873 (222/1244)
W SAO 851 (294) 860 (280/1745)
SA1 846 (283) 863 (282/1745)
SA2 880 (300) 869 (280/1696)
SA3 824 (315) 788 (315/1469)
D SAO 828 (274) 820 (258/1546)
SA1 828 (279) 819 (367/1485)
SA2 845 (276) 863 (258/1546)
SA3 800 (261) 797 (315/1379)

---
**[Page 35]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 271
1 3
7.2 Discussion
The analysis of which visualization promoted better usability was inconclusive, because 
both visualizations had advantages and disadvantages. The Collective visualization’s predictability justifed operators issuing decide commands faster, once the collective was 
committed, compared to those using the IA visualization. H6 was not supported; however, 
because the Collective operators abandoned the highest value target more frequently, and 
there was a higher percentage of abandon commands, which exceeded the number of abandoned targets. Collective operators had more local and global clutter, which suggests that 
Collective operators relied on the information pop-up windows to answer the SA probe 
questions more than IA operators. Sixteen of twenty-four SA probe questions relied on 
information provided in the information pop-up windows. The collective and target icons, 
as well as the target outlines, were intended to aid Collective operators to answer the SA 
probe questions correctly; however, the operators needed to use the information pop-up 
windows in order to see the numeric values for the collective support and behaviors in 
order to answer questions regarding target support from a specifc collective, or multiple 
collectives. An example question, such as “What collectives are investigating Target 3?” 
in Fig. 3, will require using the target information pop-up window, because Target 3 is in 
range of Collective I and III. A target information pop-up window is not required for Target 
Table 18 Sum of Euclidean 
distance between clicks (pixels) 
descriptive statistics 15 s before 
asking (B), while being asked 
(W), and during response (D) to 
SA probe question by SA level
Time Level Mean (SD) Med (min/max)
IA B SAO 3386 (2912) 2500 (0/21115)
SA1 3185 (2665) 2476 (0/18465)
SA2 3389 (3091) 2469 (0/21115)
SA3 3733 (3071) 2902 (246/17324)
W SAO 1749 (1780) 1251 (0/12162)
SA1 1387 (1329) 986 (0/6777)
SA2 2030 (2054) 1478 (0/12162)
SA3 1975 (1955) 1362 (0/8949)
D SAO 1383 (1417) 935 (0/9315)
SA1 1089 (1108) 794 (0/4999)
SA2 1606 (1610) 1310 (0/9315)
SA3 1583 (1534) 1212 (0/6728)
Coll B SAO 3187 (1984) 2834 (0/9690)
SA1 3085 (1911) 2611 (0/8898)
SA2 3235 (2049) 3041 (0/9690)
SA3 3332 (2048) 3098 (196/8911)
W SAO 1741 (1323) 1435 (0/6323)
SA1 1778 (1437) 1380 (0/5920)
SA2 1693 (1093) 1619 (0/4411)
SA3 1744 (1434) 1371 (0/6323)
D SAO 1219 (944) 1047 (0/4428)
SA1 1175 (993) 995 (0/4278)
SA2 1177 (801) 1075 (0/4085)
SA3 1373 (1041) 1161 (65/4428)

---
**[Page 36]**
*(This page contains a figure/chart/image not captured in text)*

272 Swarm Intelligence (2021) 15:237–286
1 3
1, in Fig. 3, since it is only in range of Collective I. The need to use information pop-up 
windows contributed to the Collective visualization clutter. The operators may have preferred the numeric value representations (e.g., more explainable) versus the other visualization techniques, which may have contributed to their reliance on the information pop-up 
windows.
The IA operators may have had an advantage, by deducing the same information as 
the Collective operators gained from the information pop-up windows, by observing the 
dynamic behavior of the individual entities. Relying on information pop-up windows is 
not ideal and suggests that improvements must be made to the collective icon to ensure 
the collective’s state is more understandable. Usability modifcations, such as indicating 
the highest supporting collective on the target icon, instead of only showing that there 
was support through the use of color and opacity, may increase the target icon’s efectiveness and reduce reliance of the information pop-up windows. Additional experimental design modifcations can ensure a more even distribution of questions that may rely 
on other information providing visualization features, such as the icons, system messages, or collective assignments versus information pop-up windows. Operators using 
Table 19 Number of collective 
and target left- and right-clicks 
per participant descriptive 
statistics
Clicks Mean (SD) Med (min/max)
IA Collective left 107.6 (49.89) 104 (5/235)
Collective right 30.64 (20.98) 27.5 (0/85)
Target left 97.64 (58.78) 83 (5/251)
Target right 97.18 (82.79) 68.5 (4/352)
Coll Collective left 121.96 (47.4) 130.5 (35/212)
Collective right 30.57 (31.95) 19.5 (7/164)
Target left 185.6 (64.32) 202 (62/290)
Target right 82.39 (60.22) 75 (23/278)
Table 20 Percentage of times 
abandon commands exceeded 
abandoned targets per participant 
descriptive statistics
Dec dif Mean (SD) Med (min/max)
IA Overall 1.18 (3.02) 0 (0/12)
Easy 0.4 (1.55) 0 (0/6)
Hard 1.35 (4) 0 (0/16)
Coll Overall 2.68 (6.27) 0 (0/22)
Easy 2.05 (5.06) 0 (0/15)
Hard 3.08 (7.74) 0 (0/25)
Table 21 Time diference 
(min) between committed state 
and issued decide request per 
participant descriptive statistics
Dec dif Mean (SD) Med (min/max)
IA Overall 0.68 (0.27) 0.62 (0.42/1.78)
Easy 0.7 (0.47) 0.63 (0.32/2.56)
Hard 0.72 (0.21) 0.66 (0.41/1.15)
Coll Overall 0.65 (0.15) 0.63 (0.45/1.18)
Easy 0.56 (0.14) 0.58 (0.27/0.88)
Hard 0.78 (0.3) 0.75 (0.47/1.99)

---
**[Page 37]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 273
1 3
target information pop-up windows to verify that a target was abandoned by a collective 
may have been confused if the reported target support was greater than zero. The operators may have reissued additional abandon commands in order to reduce the collective 
support to zero, although only one abandon command was needed. There were instances 
during the trial when a few individual collective entities became lost, when the collective hub was transitioning to a new location, and never moved with the hub. The 
lost entities may have continued to explore a now abandoned target, because they never 
received the message to abandon the target, which was only communicated inside of 
the hub. Strategies, such as reporting zero percent support when an abandon command 
is issued, may help mitigate erroneous issuing of repeated abandon commands, which 
was experienced up to 25% for some operators. IA operators may have also experienced 
confusion if they saw individual collective entities still travelling to an abandoned target. Not displaying lost entities after a specifc period of time once a collective hub has 
moved to a new location may also reduce the number of reissued abandon commands.
SA1 probe questions that inquired about objects nearby were answered more accurately than those that were further away when using the IA visualization. Asking SA 
probe questions about objects at various distances from the operator’s focal point is necessary in order to understand how clutter, or moving individual collective entities, may 
afect the operator’s ability to identify objects and answer questions correctly. Smaller 
sum of Euclidean distances between interactions suggests Collective operators may have 
had fewer interactions. Further analysis is required to determine whether more interactions were needed for operators to answer SA probe questions correctly and improve 
decision performance. H7 was not supported by the analysis. The IA operators may have 
issued fewer commands, or did not rely on target borders as much as the Collective 
operators. Issuing more commands suggests that Collective operators may have wanted 
more control over decision-making, which may have occurred due to lower trust, or misunderstanding collective behavior. Further investigations are needed in order to understand how the model and control mechanisms may interact with the visualization of 
collectives to infuence operator behavior. The efectiveness of the system design will 
be dependent on all system characteristics working together to promote optimal humancollective performance.
Table 22 A synopsis of R3’s hypotheses associated with signifcant results
The SA probe timings are all timings (AT), 15 s Before asking (B), While being asked (W), and During 
response (D) to a SA probe question
Variable Sub-variable Between visual. Correlation
IA Coll.
Global clutter SAO H6 − AT
SA1 H6 − AT H6 − B
SA3 H6 − B, W
Euclidean distance between SA probe interest and clicks
SAO H7 − AT
SA1 H7 − B, W H7 − B
Sum of Euclidean distance between clicks SAO H7 − D H7 − W
SA1 H7 − W
SA2 H7 − B

---
**[Page 38]**
*(This page contains a figure/chart/image not captured in text)*

274 Swarm Intelligence (2021) 15:237–286
1 3
The transparency embedded in the Collective visualization did not support the best 
overall system usability. The IA visualization promoted less clutter by alleviating the need 
to use the collective and target information pop-up windows as often and promoted fewer 
interactions. Usability and explainability modifcations to the Collective visualization are 
needed in order to mitigate undesired operator behaviors, such as the highest value target 
being abandoned, as well as reduce the reliance on the information windows. Transparency embedded into the Collective visualization, via the collective hub icons for example, must represent the same types of information provided in the information windows. 
The assumption that fewer interactions are optimal may not be accurate for all situations. 
Understanding strategies and justifcations for more interactions is necessary in order to 
promote transparency that aids operators during particular situations and results in higher 
human-collective performance.
8 R4: Visualization infuence on human‑collective performance
Assessing which visualization promoted better human-collective performance, R4, is necessary to determine whether the system transparency aided task completion. An ideal system performs a task quickly, safely, and successfully. The associated objective dependent 
variables were (1) decision time, (2) selection success rate, and (3) SA probe accuracy. The 
specifc direct and indirect transparency factors related to R4 are shown in Fig. 8. The relationship between the variables and the corresponding hypotheses, as well as the direct and 
indirect transparency factors, is presented in Table 23. Additional relationships between the 
variable and the direct or indirect transparency factors, not in Fig. 1, are provided due to 
correlation analyses.
Performance of the human-collective team can be used to assess the efects of visualization transparency on the team’s ability to fulfll tasks. An ideal system design desires high 
performance rates. It was hypothesized (H8) that the human-collective performance, efectiveness, efciency, and timing will be better using the Collective visualization.
8.1 Metrics and results
The length of time it took the human-collective team to reach a decision, decision time
(minutes), was examined. Consensus decision-making models are inherently slow, which is 
undesirable in realistic use scenarios. Adding an operator into the loop permits the human 
to infuence the decision and has the potential to minimize decision time. The decision 
time descriptive statistics per decision are shown in Table 24 (Cody et al. 2021; Roundtree 
et al. 2019a). Collective operators had faster decision times for overall, easy, and hard decisions compared to the IA operators. Both visualizations had faster human-collective decision times compared to the simulation. The Collective visualization simulation had slightly 
faster decision times for overall and easy decisions, while the IA visualization simulation 
had faster decision times for hard decisions. The Mann–Whitney–Wilcoxon test found 
signifcant efects between visualizations with human operators for overall (n = 672, U
= 50,921, 𝜌 = 0.03), easy (n = 375, U = 15,452, 𝜌 = 0.04), and hard decisions (n = 297, 
U = 9521, 𝜌 = 0.04). Highly signifcant efects were found between human operators and 
the simulation for the IA visualization overall (n = 672, U = 74,005, 𝜌 < 0.001), easy (n = 
481, U = 37,414, 𝜌 < 0.001), and hard decisions (n = 384, U = 23,194, 𝜌 < 0.001) an

---
**[Page 39]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 275
1 3
the Collective visualization overall (n = 672, U = 79,468, 𝜌 < 0.001), easy (n = 461, U = 
38,786, 𝜌 < 0.001), and hard decisions (n = 392, U = 26,887, 𝜌 < 0.001).
The selection success rate was the number of correct decisions (the collective moved to 
the highest valued target) relative to the total number of decisions. Selection success rate 
descriptive statistics per decision are shown in Table 25 (Cody et al. 2021; Roundtree et al. 
2019a). Collective operators had higher selection success rates for all decision difculties. 
The human-collective teams had higher selection success rates for both visualizations for 
all decision difculties compared to the simulation. The Collective simulation had higher 
selection success rates for overall and hard decisions, while the IA simulation had higher 
selection success rates for easy decisions. The Mann–Whitney–Wilcoxon test found highly 
signifcant efects between visualizations with human operators for overall (n = 672, U = 
64,008, 𝜌 < 0.001) and easy decisions (n = 375, U = 19845, 𝜌 < 0.001). A moderate signifcant efect between visualizations with human operators was found for hard decisions (n
= 297, U = 12,761, 𝜌 < 0.01). Highly signifcant efects were found between human operators and simulation for the IA visualization overall (n = 672, U = 34,650, 𝜌 < 0.001), easy 
(n = 481, U = 18,242, 𝜌 < 0.001), and hard decisions (n = 384, U = 13,088, 𝜌 < 0.001) and 
for the Collective visualization overall (n = 672, U = 22,162, 𝜌 < 0.001), easy (n = 461, U
= 10,795, 𝜌 < 0.001), and hard decisions (n = 392, U = 9449.5, 𝜌 < 0.001).
The Spearman correlation analysis revealed a moderate correlation between humancollective team decision time and selection success rate using the IA visualization for easy 
decisions (r = − 0.42, 𝜌 < 0.001). Weak correlations were revealed between the humancollective team decision time and selection success rate using the IA visualization for overall decisions (r = − 0.27, 𝜌 < 0.001) and when using the Collective visualization for overall 
(r = − 0.11, 𝜌 = 0.05), easy (r = − 0.18, 𝜌 = 0.02), and hard decisions (r = 0.18, 𝜌 = 0.03). 
Moderate correlations were revealed between simulation decision time and selection success rate using the IA visualization for overall decisions (r = − 0.53, 𝜌 < 0.001) and when 
using the Collective visualization for overall (r = − 0.57, 𝜌 < 0.001) and easy decisions (r
= − 0.44, 𝜌 < 0.001). Weak correlations were revealed between simulation decision time 
and selection success rate using the IA visualization for easy (r = − 0.35, 𝜌 < 0.001) and 
hard decisions (r = − 0.14, 𝜌 = 0.03).
SA probe accuracy, which is the percentage of correctly answered SA probes questions 
used to assess the operator’s SA during a trial, results identifed that Collective operators 
Fig. 8 R4 concept map of the assessed direct and indirec

---
**[Page 40]**
*(This page contains a figure/chart/image not captured in text)*

276 Swarm Intelligence (2021) 15:237–286
1 3
Table 23 Visualization infuence on human-collective performance objective (obj) and subjective (subj) variables (vars), relationship to the hypothesis (H8), as well as the 
associated direct and indirect transparency factors, are presented in Fig. 1
Obj vars Transparency factors
Direct Indirect
Explainability Observable Performance Understanding Capability Efectiveness Efciency Predictability SA Timing
Decision time per decision ✓ ✓ ✓ ✓
Selection success rate per decision ✓ ✓SA probe accuracy ✓ ✓ ✓ ✓ ✓ ✓ ✓Mental rotation assessment ✓ ✓Subj varsWeekly hours on a desktop or laptop ✓ ✓Video game profciency ✓ ✓Post-trial performance and understanding ✓ ✓ ✓ ✓

---
**[Page 41]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 277
1 3
had higher SA probe accuracy, regardless of the SA level. Further details about the statistical tests are provided in Sect. 5.1.
Additional Spearman correlation analyses were conducted to see if any correlations 
were identifed between the weekly hours that participants’ used a desktop or laptop, video 
game profciency, the mental rotations assessment, and selection success rate. A weak correlation was found between weekly hours participants’ used a desktop or laptop and selection success rate for the IA visualization (r = 0.16, 𝜌 = 0.02).
The post-trial performance and understanding questionnaire results, assessed the participants’ understanding of the collective behavior and their ability to choose the best target 
for each decision, were ranked higher for the Collective visualization compared to the IA. 
The statistical test details are provided in Sect. 6.1.
A summary of R4’s hypotheses with associated signifcant results is provided in 
Table 26.
Table 24 Decision time 
(minutes) descriptive statistics 
per decision difculty
Dec dif Mean (SD) Med (min/max)
IA M2 Overall 4.32 (1.83) 3.94 (1.74/15.94)
Easy 3.77 (1.63) 3.38 (1.74/13.47)
Hard 5.09 (1.82) 4.68 (1.86/15.94)
M2SIM Overall 4.8 (1.1) 4.82 (2.46/7.68)
Easy 4.19 (1.06) 4.07 (2.46/8.85)
Hard 5.73 (1.26) 5.54 (3.43/10.15)
Coll M2 Overall 3.97 (1.37) 3.64 (1.83/9.94)
Easy 3.37 (1.23) 3.09 (1.83/9.94)
Hard 4.67 (1.2) 4.57 (2.46/8.81)
M2 SIM Overall 4.79 (1.11) 4.79 (2.49/7.7)
Easy 4.17 (0.93) 4.1 (2.49/7.55)
Hard 5.77 (1.38) 5.62 (3.67/10.25)
Table 25 Selection success rate 
(%) descriptive statistics per 
decision difculty
Dec dif Mean (SD) Med (min/max)
IA M2 Overall 75 (43.37) 100 (0/100)
Easy 81.44 (38.98) 100 (0/100)
Hard 66.2 (47.47) 100 (0/100)
M2SIM Overall 73.69 (19.01) 70 (20/100)
Easy 77.15 (27.12) 85.71 (0/100)
Hard 62.05 (27.17) 66.67 (0/100)
Coll M2 Overall 88.39 (32.08) 100 (0/100)
Easy 94.44 (22.97) 100 (0/100)
Hard 81.41 (39.03) 100 (0/100)
M2SIM Overall 74.58 (18.39) 70 (20/100)
Easy 76.7 (26.87) 83.33 (0/100)
Hard 64.04 (26.38) 66.67 (0/100

---
**[Page 42]**
*(This page contains a figure/chart/image not captured in text)*

278 Swarm Intelligence (2021) 15:237–286
1 3
8.2 Discussion
The analysis suggests that the Collective visualization promoted better human-collective 
performance. H8 was supported, because the Collective visualization enabled higher selection success rates, SA performance, as well as higher subjective performance. Operators 
using the Collective visualization were more efcient by making signifcantly faster decisions and having higher selection success rates compared to the IA visualization. Realistic human-collective user scenarios will require high performance in short decision times, 
especially in proposed high-risk environments. Longer decision times contributed to higher 
success rates for both visualizations for overall decisions and for easy decisions for the 
IA visualization; however, faster decision times contributed to higher selection success 
for hard decisions using the Collective visualization. The design of an efective humancollective system must enable the human-collective team to fulfll primary objectives, 
without hindering other metrics, such as decision time. Devoting more time to ensure high 
task performance is a common trade-of behavior observed in teams. Expedited decisions 
may have occurred if higher valued targets were more observable further away from other 
objects (less clutter), making them more salient, or if impatient operators were able to predict future collective behaviors and infuenced collectives more to make decisions faster. 
The explainability of the information pop-up windows aided Collective operators to answer 
more SA probe questions accurately. The Collective visualization enabled operators with 
diferent capabilities to perform relatively the same, unlike the IA visualization, which 
found that individuals with more weekly desktop or laptop exposure had higher selection 
success rates.
The transparency embedded in the Collective visualization promoted the fastest decision times, selection success rates, and SA performance. Strategies, such as providing 
control mechanisms to undo actions that had negative infuence on collective behaviors, 
and providing supplementary information, promoted transparency. Understanding what 
Table 26 A synopsis of R4’s hypothesis (H8) associated with signifcant results
The SA probe timings are all timings (AT), 15 s Before asking (B), While being asked (W), and During 
response (D) to a SA probe questionThe SA probe timings are all timings (AT), 15 s Before asking (B), 
While being asked (W), and during response (D) to a SA probe question
Variable Sub-variable Between visual. Correlation
IA Coll.
Decision time Overall H8 H8 H8
Easy H8 H8
Hard H8 H8
Selection success rate Overall H8 –
Easy H8
Hard H8
SA probe accuracy SAO H8
SA1 H8
SA2 H8
SA3 H8
Weekly hours on desktop or laptop SA1 H8
Post-trial Unders. H8 –

---
**[Page 43]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 279
1 3
interactions contributed to higher performance is necessary to determine what operator 
strategies are most efective and efcient, as well as identify what visualization characteristics are leveraged in order to perform the task.
9 Discussion
The research objective was to determine which visualization achieved better transparency, to identify what metrics were useful in determining better transparency, and to create design guidance for human-collective systems. The analysis indicated that the Collective visualization provided better transparency, because operators with diferent individual 
capabilities performed similarly for both the primary and secondary tasks, and the humancollective team performed better. The fnding that an abstract collective provided better 
visualization transparency compared to a traditional collective visualization challenges 
the human-collective interaction community to design non-traditional visualizations that 
embed transparency in ways that maintain SA, mitigate workload, promote understanding 
and functionality, as well as have high performance.
A variety of the metrics proved to efectively assess visualization transparency and the 
infuence it has on operators with diferent individual capabilities, operator comprehension, 
system usability, and human-collective performance, which are the second and third contributions of this manuscript. The Mental Rotations Assessment, NASA-TLX, and SART 
were useful individual operator capability metrics when determining the infuence of the 
visualization on the operator and can be easily used in other collective evaluations. Operator experience (e.g., weekly hours on a desktop or laptop) and expertise (e.g., video game 
profciency) can indicate the desired operator knowledge in order to interact with the collective system efectively. The infuence of visualization on human operator comprehension and visualization usability requires further investigation in order to better understand
the infuence of operator interactions and identify more reliable metrics to assess operator 
understanding. Using correlations between an operator’s interactions and SA probe accuracy can be used to inform designers whether the actions taken by operators aided their 
responses, but does not necessarily provide insight regarding comprehension. The use of 
eye-tracking technology can provide improved insight regarding operator comprehension 
and usability by recording where the operator was looking 15 s before asking, while being 
asked, and during response to a SA probe question. Where operators are looking on the 
visualization prior to taking action will indicate what types of information the operator was 
potentially perceiving and comprehending, the difculty to identify the desired information due to visualization clutter, and the duration of time devoted to looking at particular 
information. Clutter will greatly impact an operator’s ability to perceive and comprehend 
information on the visualization and is an informative metric to use when assessing transparency for human-collective systems.
The reliance on collective and target information pop-up windows contributed to the 
majority of clutter for both visualizations and suggests alterations to design recommendations for future human-collective systems. Providing supplementary information, via 
information pop-up windows, is necessary to enable successful human-collective behaviors; however, other strategies must be implemented to improve the efcacy of the collective icon. Indicating which collective state is most supported, by displaying either U, F, 
C, or X, instead of the status of all four states, may be more advantageous to the operator. 
The target a collective is favoring, committed, or executing may also be displayed on the

---
**[Page 44]**
*(This page contains a figure/chart/image not captured in text)*

280 Swarm Intelligence (2021) 15:237–286
1 3
collective icon. For example, if a collective is favoring Target 8, the collective icon can 
show F8, which stands for Favoring Target 8. Providing the most supported state and target 
may enable the operator to quickly understand what the collective is doing and determine 
if interventions, or more support is needed to ensure successful decision-making. Showing 
the predominant collective state; however, requires the operator to remember what U, F, 
C, and X stand for, which can be mitigated by adding this information to the legend. Bolding the predominant state letter on the current collective icon can be used as an alternative 
design change to improve the operator’s understanding of the most supported collective 
state. The perceived mental demand and efort associated with the Collective visualization 
may decrease with strategies that make the collective state more obvious to the operator.
The dynamic and streamlined behavior of the individual collective entities on the IA 
visualization may have aided operator understanding of collective behavior, mitigating 
the need to access as many information pop-up windows. Displaying all of the individual 
collective entities is not ideal as collectives become larger in size. The increased number 
of entities will contribute to more clutter, potentially hindering the operator’s perception 
and comprehension. Using iconography, such as arrows pointing in the direction of the 
most supported target, or providing predicted hub locations, may be design strategies that 
can improve operator understanding for abstract collective visualizations. Further analysis 
is needed to verify the efectiveness of the proposed strategies. The consistent improvement in decision time and selection success rate across all decision difculties suggests 
that using visualizations that show all the individual collective entities does not contribute to better human-collective performance. The Collective visualization enabled better 
human-collective performance, which is valuable as collective systems become more complex, with improved capabilities and the utilization of heterogeneous collectives. Presenting individual collective entities may have caused more stress, or confusion, and required 
operators to slow down the collective decision-making process in order to attain higher 
selection success rates. SA probe accuracy, selection success rates, and decision times were 
useful metrics that can be easily used in other collective system evaluations.
Indicating target value through the use of color and opacity was a successful transparency implementation and metric to assess. Further analysis is required to determine if the 
entire target icon must represent the target value to be more perceivable, since operators 
using the Collective visualization, which used half of the target icon to represent the value 
and the other half to represent support from the highest supporting collective, abandoned 
the highest value target more frequently. Opacity levels must also be validated to ensure 
distinction of low-, medium-, and high-valued targets from one another. Reiterating the 
task objective, to choose and move each collective to the highest value target for each 
decision, numerous times during training may help mitigate operator misunderstanding. 
Improvements can be made to the collective and target information pop-up windows in 
order to decrease the number of reissued abandon commands for operators who relied and 
verifed abandonment using the information pop-up windows. When an abandon command 
is issued the corresponding target information pop-up window can immediately report 
zero support, instead of the actual collective support, which corresponds closer to operators’ mental models. A red bar can be overlaid on the particular collective that abandoned 
the target as a secondary measure to ensure the operator understands the collective status. 
Operators can focus their attention on collective support values that are not highlighted 
in red, in case the current target is the highest value target for another nearby collective. 
Using metrics, such as the number of times abandoned requests exceed abandoned targets, 
can be used as an error metric for collective systems.

---
**[Page 45]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 281
1 3
Design guidance recommendations, in Table  27, were created from the analysis for 
human-collective system visualizations supporting a best-of-n sequential decision-making 
task. The design guidance, inspired from standards in the human-machine interaction literature, represents the frst set of human-collective system design guidelines that demonstrate best practices when supervising multiple collectives. The guidelines propose strategies for particular design elements, substantiated by the analysis in this manuscript, to 
improve transparency, which can help maintain operator SA of the collective behaviors. 
The guidelines were created to consider the complex challenges associated with collectives, such as emergent behaviors, biological behaviors, and the quantity of information 
due to the large number of individual collective entities, that are not typically considered 
in traditional human-machine design guidance. The recommendations are applicable irrespective of visualization type. The majority of the recommendations indicate that the use 
of color to distinguish objects from one another, or convey particular information, can be 
useful, as long as the operator’s cognitive capacity is not exceeded. Other design strategies, 
such as the use of patterns, may need to be considered if operators are color blind. Several 
recommendations suggest providing particular information, such as collective behaviors 
and state information, operator actions, and system messages, in order to facilitate operator understanding. Further investigations are needed in order to determine the efectiveness of the following design recommendations for real-world scenarios where bandwidth 
limitations occur. Understanding how information latency and inaccurate collective state 
Table 27 Human-collective visualization design guidance
Design guidance
1. Provide detailed supplemental information to the operator, such as the use of
information pop-up windows.
2. Provide information about the system and operator actions, such as the use of system
messages and collective assignments windows.
3. The use of color and diferent opacity is an efective method of conveying a nonnumeric value.
4. The use of colored borders is an efective method of distinguishing objects in the
environment.
5. Provide a legend detailing information in order to alleviate memory demands of the
operator.
6. Use distinct and unique identifers for objects in the environment, such as integers
versus letters.
7. Provide information about collective behavior that coincides with operator mental
models of operation, such as abandoning a target will result in zero individual
collective entity support.
8. Indicate the status of operator commands, such as a red indicator to denote
completion of a command and green to denote an ongoing state.
9. Provide the projected state of a collective, such as a dynamic moving border.
10. Limit the number of colors used to seven plus or minus two, which is consistent with
human cognitive capacity (Miller 1956).
11. Provide perceivable collective state information, such as the use of color to denote
diferent states.

---
**[Page 46]**
*(This page contains a figure/chart/image not captured in text)*

282 Swarm Intelligence (2021) 15:237–286
1 3
information negatively infuence human-collective behavior is essential to design a resilient transparent visualization.
Visualization transparency for human-collective systems can be achieved via diferent 
design strategies and must be assessed holistically by understanding how diferent factors 
impact transparency and are infuenced by transparency. The four secondary research questions assessed four categories of transparency factors that contribute to an efective system: 
(1) diferent operator individual capabilities, (2) operator comprehension , (3) visualization 
usability, and (4) human-collective team performance. An ideal visualization will enable 
operators with diferent individual capabilities to perform relatively the same, promote 
operator comprehension, be usable, and promote high human-collective performance. The 
Collective visualization enabled operators with diferent individual capabilities to perform 
relatively the same and promoted better human-collective performance. The IA visualization enabled operators to perceive collective behaviors and collective support for particular 
targets more readily than the Collective visualization, where operators used the collective 
and target information pop-up windows to afrm these types of collective behaviors. As 
collective systems grow in size, visualizations that show all of the individual collective 
entities will cause perceptual and comprehension challenges, as well as infuence operator 
actions negatively, because too many individual collective entities will clutter the display. 
The same advantageous observation (i.e., dynamically seeing collective behaviors and support) from this analysis may not occur with large collectives (> 10,000). Abstract collective visualizations designed using the provided guidelines may help promote better transparency, than visualizations showing all of the individual collective entities and enable 
efective human-collective teams.
10 Conclusion
Designers of human-collective systems continue to debate what visualization is needed 
to represent collectives best and provide transparency of the collective behaviors to the 
operators. This manuscript evaluates a traditional and abstract collective visualization for 
a sequential best-of-n decision-making task with four collectives, each consisting of 200 
individual collective entities. The visualization transparency is evaluated with respect to 
how the visualization impacts the human operators, operator comprehension, usability, and 
human-collective performance. The Collective visualization was considered more transparent, because operators with varying individual diferences and capabilities were able to 
perform similarly in both the primary and secondary tasks, and the human-collective performance was higher compared to the IA visualization. Additional interaction analysis and 
metrics are needed to evaluate which visualization promoted better operator comprehension and usability. Designers must build collective systems that are efective regardless of 
how large the collective size may become, how simple or complex the collective behaviors 
are, and how real-world use scenarios, such as bandwidth limitations, may impact the system. Visualizations that show all of the individual collective entities will challenge operators’ ability to perceive and comprehend information in order to inform actions. Abstract 
collective visualizations may be more resilient to real-world scenarios, and provide transparency to enable efective human-collective teams.
Supplementary Information The online version supplementary material available at https://doi.org/10.
1007/s11721-021-00194-6.

---
**[Page 47]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 283
1 3
Acknowledgements The US Ofce of Naval Research Awards N000141613025, N000141210987, and 
N00014161302, supported this efort. The work of Jason R. Cody was fully supported by the United States 
Military Academy and the United States Army Advanced Civil Schooling program.
Declarations
Confict of interest The authors declare they have no confict of interest.
References
Alarcon, G. M., Gamble, R., Jessup, S. A., Walter, C., Ryan, T. J., Wood, D. W., et al. (2017). Application 
of the heuristic-systematic model to computer code trustworthiness: The infuence of reputation and 
transparency. Cogent Psychology, 4, 1–22. https://doi.org/10.1080/23311908.2017.1389640.
Ashcraft, C. C., Goodrich, M. A., & Crandall, J. W. (2019). Moderating operator infuence in human-swarm 
systems. In IEEE international conference on systems, man and cybernetics (pp. 4275–4282). https://
doi.org/10.1109/SMC.2019.8914592.
Atoyan, H., Duquet, J. R., & Robert, J. M. (2006). Trust in new decision aid systems. In Conference on 
l’Interaction Homme-Machine (pp. 115–122). https://doi.org/10.1145/1132736.1132751.
Ballerini, M., Cabibbo, N., Candelier, R., Cavagna, A., Cisbani, E., Giardina, I., et al. (2008). Interaction 
ruling animal collective behavior depends on topological rather than metric distance: Evidence from a 
feld study. Proceedings of the National Academy of Sciences, 105(4), 1232–1237. https://doi.org/10.
1073/pnas.0711437105.
Bayindir, L., & Şahin, E. (2007). A review of studies in swarm robotics. Turkish Journal of Electrical Engineering & Computer Sciences, 15(2), 115–147.
Brambilla, M., Ferrante, E., Birattari, M., & Dorigo, M. (2013). Swarm robotics: A review from the swarm 
engineering perspective. Swarm Intelligence, 7(1), 1–41. https://doi.org/10.1007/s11721-012-0075-2.
Brown, D. S., Goodrich, M., Jung, S. Y., & Kerman, S. (2016). Two invariants of human–swarm interaction. 
Journal of Human-Robot Interaction, 5(1), 1–31. https://doi.org/10.5898/JHRI.5.1.Brown.
Chen, J. Y. C., Procci, K., Boyce, M., Wright, J. L., Garcia, A., & Barnes, M. J. (2014). Situation awarenessbased agent transparency. Technical report. ARL-TR-6905, U.S. Army Research Laboratory, Aberdeen 
Proving Ground, MD. https://www.researchgate.net/publication/264963346_Situation_AwarenessBased_Agent_Transparency. Accessed 18 September 2018
Chen, J. Y. C., Lakhmani, S. G., Stowers, K., Selkowitz, A. R., Wright, J. L., & Barnes, M. J. (2018). 
Situation awareness-based agent transparency and human-autonomy teaming efectiveness. Theoretical Issues in Ergonomics Science, 19(3), 259–282. https://doi.org/10.1080/1463922X.2017.1315750.
Chen, M., Zhang, P., Wu, Z., & Chen, X. (2020). A multichannel human–swarm robot interaction system 
in augmented reality. Virtual Reality & Intelligent Hardware, 2(6), 518–533. https://doi.org/10.1016/j.
vrih.2020.05.006.
Cody, J. R. (2018). Discrete consensus decisions in human-collective teams. PhD thesis, Vanderbilt University, Vanderbilt University, Nashville, TN, USA. https://etd.library.vanderbilt.edu/etd-04032018-
164817. Accessed 18 September 2018
Cody, J. R., Roundtree, K. A., & Adams, J. A. (2021). Human-collective collaboration target selection. 
Transactions on Human-Robot Interaction, 10(2), 1–29. https://doi.org/10.1145/3442679.
Couzin, I. D., Krause, J., James, R., Ruxton, G. D., & Franks, N. R. (2002). Collective memory and spatial 
sorting in animal groups. Journal of Theoretical Biology, 218(1), 1–11. https://doi.org/10.1006/jtbi.
2002.3065.
Couzin, I. D., Krause, J., Franks, N. R., & Levin, S. A. (2005). Efective leadership and decision-making in 
animal groups on the move. Nature, 433, 513–516. https://doi.org/10.1038/nature03236.
Crandall, J. W., Anderson, N., Ashcraft, C., Grosh, J., Henderson, J., McClellan, J., et al. (2017). Humanswarm interaction as shared control: Achieving fexible fault-tolerant systems. In International conference on engineering psychology and cognitive ergonomics (pp. 266–284). https://doi.org/10.1007/
978-3-319-58472-0_21.
Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems. Human Factors: The 
Journal of the Human Factors and Ergonomics Society, 37(1), 32–64. https://doi.org/10.1518/00187
2095779049543.

---
**[Page 48]**
*(This page contains a figure/chart/image not captured in text)*

284 Swarm Intelligence (2021) 15:237–286
1 3
Entin, E. B., Entin, E. E., & Serfaty, D. (1996). Optimizing aided target-recognition performance. In Human 
factors and ergonomics society annual meeting (pp. 233–237). https://doi.org/10.1177/1541931296
04000419.
Fox, M., Long, D., & Magazzeni, D. (2017). Explainable planning. arXiv:170910256, https://arxiv.org/abs/
1709.10256.
Gillan, D. J., Holden, K., Adam, S., Rudisill, M., & Magee, L. (1992). How should Fitts’ Law be applied 
to human–computer interaction? Interacting with Computers, 4(3), 291–313. https://doi.org/10.1016/
0953-5438(92)90019-c.
Gordon, D. M. (1999). Ants at work: How an insect society is organized. Oxford, UK: Simon and Schuster.
Haas, E., Fields, M., Hill, S., & Stachowiak, C. (2009). Extreme scalability: Designing interfaces and algorithms for soldier-robotic swarm interaction. Tech. Rep. ARL-TR-4800, U.S. Army Research Laboratory, Aberdeen Proving Ground, MD, URL https://apps.dtic.mil/sti/pdfs/ADA498162.pdf.
Hart, S. G., & Staveland, L. E. (1988). Development of NASA-TLX (task load index): Results of empirical and theoretical research. Advances in Psychology, 52, 139–183. https://doi.org/10.1016/S0166-
4115(08)62386-9.
Harvey, J., Merrick, K. E., & Abbass, H. A. (2018). Assessing human judgment of computationally generated swarming behavior. Frontiers in Robotics and AI, 5(13), 1–13. https://doi.org/10.3389/frobt.2018.
00013.
Hein, A. M., Rosenthal, S. B., Hagstrom, G. I., Berdahl, A., Torney, C. J., & Couzin, I. D. (2015). The evolution of distributed sensing and collective computation in animal populations. Ecology, Genomics and 
Evolutionary Biology, 4, 1–59. https://doi.org/10.7554/eLife.10955.
Helldin, T. (2014). Transparency for future semi-automated systems: Efects of transparency on operator 
performance, workload and trust. PhD thesis. Örebro University, Örebro University. https://www.
diva-portal.org/smash/get/diva2:710832/FULLTEXT02.
Hepworth, A. J., Baxter, D. P., Hussein, A., Yaxley, K. J., Debie, E., & Abbass, H. A. (2020). Humanswarm-teaming transparency and trust architecture. IEEE/CAA Journal of Automatica Sinica. 
https://doi.org/10.1109/JAS.2020.1003545.
Hussein, A., Elsawah, S., & Abbass, H. A. (2020). The reliability and transparency bases on trust in 
human-swarm interaction: Principles and implications. Ergonomics, 63(9), 1116–1132. https://doi.
org/10.1080/00140139.2020.1764112.
John, S. M., Smallman, H. S., & Manes, D.I. (2005). Recovery from interruptions to a dynamic monitoring task: The beguiling utility of instant replay. In Human factors and ergonomics society annual 
meeting (pp. 473–477). https://doi.org/10.1177/154193120504900355.
Kaltenbach, E., & Dolgov, I. (2017). On the dual nature of transparency and reliability: Rethinking factors that shape trust in automation. In Human factors and ergonomics society annual meeting (pp. 
308–312). https://doi.org/10.1177/1541931213601558.
Kim, T., & Hinds, P. (2006). Who should I blame? Efects of autonomy and transparency on attributions 
in human-robot interaction. In IEEE international symposium on robot and human interactive communication (pp. 80–85). https://doi.org/10.1109/ROMAN.2006.314398.
Kizilcec, R. F. (2016). How much information?: Efects of transparency on trust in an algorithmic interface. In Conference on human factors in computing systems (pp. 2390–2395). https://doi.org/10.
1145/2858036.2858402.
Komareji, M., & Boufanais, R. (2013). Resilience and controllability of dynamic collective behaviors. 
PLoS ONE, 8(12), 1–15. https://doi.org/10.1371/journal.pone.0082578.
Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. Human Factors: The Journal of the Human Factors and Ergonomics Society, 46(1), 50–80. https://doi.org/10.
1518/hfes.46.1.50_30392.
Lyons, J. B. (2013). Being transparent about transparency: A model for human-robot interaction. In 
AAAI Spring Sympsium: Trust and Autonomous Systems (pp. 48–53), URL https://www.resea
rchgate.net/publication/286961455_Being_transparent_about_transparency_A_model_for_humanrobot_interaction.
Lyons, J. B., Sadler, G. G., Koltai, K., Battiste, H., Ho, N. T., Hofmann, L. C., et al. (2017). Shaping 
trust through transparent design: Theoretical and experimental guidelines. Advances in Human Factors in Robots and Unmanned Systems, 499, 127–136. https://doi.org/10.1007/978-3-319-41959-6_
11.
Manning, M. D., Harriott, C. E., Hayes, S. T., Adams, J. A., & Seifert, A. E. (2015). Heuristic evaluation of swarm metrics’ efectiveness. In ACM/IEEE International Conference on Human-Robot 
Interaction Extended Abstracts (pp. 17–18), https://doi.org/10.1145/2701973.2702046.
Mark, G., & Kobsa, A. (2005). The efects of collaboration and system transparency on CIVE usage: An 
empirical study and model. Presence, 14(1), 60–80. https://doi.org/10.1162/1054746053890279.

---
**[Page 49]**
*(This page contains a figure/chart/image not captured in text)*

Swarm Intelligence (2021) 15:237–286 285
1 3
Mercado, J. E., Rupp, M. A., Chen, J. Y. C., Barnes, M. J., Barber, D., & Procci, K. (2016). Intelligent agent transparency in human-agent teaming for multi-UXV management. Human Factors: The 
Journal of the Human Factors and Ergonomics Society, 58(3), 401–415. https://doi.org/10.1177/
0018720815621206.
Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on capacity for processing information. Psychological Review, 63(2), 81–97. https://doi.org/10.1037/h0043158.
Nagavalli, S., Chen, S. Y., Lewis, M., Chakraborty, N., & Sycara, K. (2015). Bounds of neglect benevolence in input timing for human interaction with robotic swarms. In ACM/IEEE international conference on human–robot interaction (pp. 197–204). https://doi.org/10.1145/2696454.2696470.
Nedbal, D., Auinger, A., & Hochmeier, A. (2013). Addressing transparency, communication and participation in enterprise 2.0 projects. Procedia Technology, 9, 676–686. https://doi.org/10.1016/j.protcy.
2013.12.075.
Ososky, S., Sanders, T., Jentsch, F., Hancock, P., & Chen, J. Y. C. (2014). Determinants of system transparency and its infuence on trust in and reliance on unmanned robotic systems. In The international society for optical engineering (pp. 1–12). https://www.researchgate.net/publication/27149
5823_Determinants_of_system_transparency_and_its_infuence_on_trust_in_and_reliance_on_
unmanned_robotic_systems. Accessed 18 September 2018
Preece, J., & Rogers, Y. (2007). Interaction Design: Beyond Human–Computer Interaction. West Sussex, England: Wiley.
Rao, A. S., & Georgef, M. P. (1995). Bdi agents: From theory to practice. In International conference on 
multiagent systems (pp. 312–319).https://www.aaai.org/Papers/ICMAS/1995/ICMAS95-042.pdf.
Reina, A., Valentini, G., Fernández-Oto, C., Dorigo, M., & Trianni, V. (2015). A design pattern for decentralised decision making. PLoS ONE, 10(10), 1–18. https://doi.org/10.1371/journal.pone.0140950.
Roundtree, K. A., Manning, M. D., & Adams, J. A. (2018). Analysis of human-swarm visualizations. In 
Human factors and ergonomics society annual meeting (pp. 287–291). https://doi.org/10.1177/15419
31218621066.
Roundtree, K. A., Cody, J. R., Leaf, J., Demirel, H. O., & Adams, J. A. (2019a). Visualization design for 
human-collective teams. In Human factors and ergonomics society annual meeting (pp. 417–421). 
https://doi.org/10.1177/1071181319631028.
Roundtree, K. A., Goodrich, M. A., & Adams, J. A. (2019b). Transparency: Transitioning from humanmachine systems to human-swarm systems. Journal of Cognitive Engineering and Decision Making, 
13(3), 171–195. https://doi.org/10.1177/1555343419842776.
Roundtree, K. A., Cody, J. R., Leaf, J., Demirel, H. O., & Adams, J. A. (2020). Transparency’s infuence on 
human–collective interactions. arXiv:200909859 URL https://arxiv.org/abs/2009.09859.
Scholtz, J. (2003). Theory and evaluation of human robot interactions. In Hawaii international conference 
on system sciences. https://doi.org/10.1109/HICSS.2003.1174284.
Seeley, T. D. (2010). Honeybee democracy. Princeton, NJ: Princeton University Press.
Seifert, A. E., Hayes, S. T., Harriott, C. E., & Adams, J. A. (2015). Motion perception of biological swarms. 
In Annual cognitive science society meeting (pp. 2128–2133). https://cogsci.mindmodeling.org/2015/
papers/0367/paper0367.pdf.
Selcon, S. J., Taylor, R. M., & Koritsas, E. (1991). Workload or situational awareness? TLX vs. SART for 
aerospace systems design evaluation. In Human factors and ergonomics society annual meeting (pp. 
62–66). https://doi.org/10.1518/107118191786755706.
Selkowitz, A. R., Lakhmani, S. G., Chen, J. Y. C., & Boyce, M. (2015). The efects of agent transparency 
on human interaction with an autonomous robotic agent. In Human factors and ergonomics society 
annual meeting (pp. 806–810). https://doi.org/10.1177/1541931215591246.
Şahin, E., & Spears, W. M. (2005). Swarm Robotics. New York, NY: Springer.
Theodorou, A., Wortham, R. H., & Bryson, J. J. (2017). Designing and implementing transparency for real 
time inspection of autonomous robots. Connection Science, 29(3), 230–241. https://doi.org/10.1080/
09540091.2017.1310182.
Valentini, G., Ferrante, E., & Dorigo, M. (2017). The best-of-n problem in robot swarms: Formalization, 
state of the art, and novel perspectives. Frontiers in Robotics and AI, 4, 1–9. https://doi.org/10.3389/
frobt.2017.00009.
Vandenberg, S. G., & Kuse, A. R. (1978). Mental rotations, a group test of three-dimensional spatial visualization. Perceptual and Motor Skills, 47(2), 599–604. https://doi.org/10.2466/pms.1978.47.2.599.
Walker, P., Nunanally, S., Lewis, M., Kolling, A., Chakraborty, N., & Sycara, K. (2012). Neglect benevolence in human control of swarms in the presence of latency. In IEEE international conference on systems, man, and cybernetics (pp. 3009–3014). https://doi.org/10.1109/ICSMC.2012.6378253.

---
**[Page 50]**
*(This page contains a figure/chart/image not captured in text)*

286 Swarm Intelligence (2021) 15:237–286
1 3
Walker, P., Lewis, M., & Sycara, K. (2016). The efect of display type on operator prediction of future 
swarm states. In IEEE International Conference on Systems, Man, and Cybernetics (pp. 2521–2526), 
URL https://www.ri.cmu.edu/pub_fles/2016/10/walker2016efect.pdf.
Walker, P., Miller, C., Mueller, J., Sycara, K., & Lewis, M. (2019). A playbook-based interface for human 
control of swarms (pp. 61–88). Boca Raton, FL: CRC Press.
Wickens, C. D., Lee, J. D., Liu, Y., & Becker, S. E. G. (2004). An introduction to human factors engineering. Upper Saddle River, NJ: Pearson Prentice Hall.
Yerkes, R. M., & Dodson, J. D. (1908). The relation of strength of stimulus to rapidity of habit-formation. 
Journal of Comparative Neurology of Psychology, 18, 459–482. https://doi.org/10.1002/cne.92018
0503.
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional afliations.
Authors and Afliations
Karina A. Roundtree1 · Jason R. Cody2 · Jennifer Leaf3 · H. Onan Demirel1 · 
Julie A. Adams3
Jason R. Cody 
jason.cody@westpoint.edu
Jennifer Leaf 
leaf@oregonstate.edu
H. Onan Demirel 
onan.demirel@oregonstate.edu
Julie A. Adams 
julie.a.adams@oregonstate.edu
1 Mechanical, Industrial, and Manufacturing Engineering, Oregon State University, Corvallis, 
OR 97331, USA
2 Electrical Engineering and Computer Science, United States Military Academy, West Point, 
NY 10996, USA
3 Collaborative Robotics and Intelligent Systems Institute, Oregon State University, Corvallis, 
OR 97331, USA