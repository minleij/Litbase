# JIAUND1

*Source file: JIAUND1.PDF — 24 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

International Journal of Human–Computer Interaction
ISSN: 1044-7318 (Print) 1532-7590 (Online) Journal homepage: www.tandfonline.com/journals/hihc20
Understanding Situation Awareness in Multi-UAV
Supervision: Effects of Environmental Complexity,
Interface Design, and Human–AI Differences
Lesong Jia, Kiran Shridhar Alva , Huao Li , Werner Hager , Lucia Romero ,
Timothy Albert Butler & Michael Lewis
To cite this article: Lesong Jia, Kiran Shridhar Alva , Huao Li , Werner Hager , Lucia Romero ,
Timothy Albert Butler & Michael Lewis (10 Feb 2026): Understanding Situation Awareness
in Multi-UAV Supervision: Effects of Environmental Complexity, Interface Design, and
Human–AI Differences, International Journal of Human–Computer Interaction, DOI:
10.1080/10447318.2026.2622580
To link to this article: https://doi.org/10.1080/10447318.2026.2622580
Published online: 10 Feb 2026.
Submit your article to this journal 
Article views: 113
View related articles
View Crossmark data
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=hihc20

---
**[Page 2]**

Understanding Situation Awareness in Multi-UAV Supervision: Effects
of Environmental Complexity, Interface Design, and Human–AI
Differences
Lesong Jia , Kiran Shridhar Alva, Huao Li, Werner Hager, Lucia Romero, Timothy Albert Butler
and Michael Lewis
School of Computing and Information, University of Pittsburgh, Pittsburgh, PA, USA
ABSTRACT
Situation Awareness (SA) is paramount for successful multi-UAV supervision, requiring
real-time integration of complex environmental dynamics and system states. However,
most prior research has centered on system-oriented monitoring tasks, including
tracking UAV positions and statuses, rather than supporting users in interpreting environmental information. To address this gap, we conducted a simulated wildfire monitoring study manipulating key environmental and interface factors and compared the
performance of human operators and GPT-4o across object-specific and global
queries. Human participants demonstrated significantly higher accuracy on object-specific tasks than on global queries, highlighting their strength in real-time perceptual
processing and the challenges of memory-based reasoning while the reverse was true
for GPT-4o. Across conditions, SA accuracy was lower at higher SA levels, under higher
target density, and in the presence of event clustering. Interface support in the form
of centralized layouts and retrospective access was effective in mitigating cognitive
load and enhancing SA accuracy.
KEYWORDS
Multi-UAV supervision;
situation awareness;
interface design; large
language models
1. Introduction
In time-critical domains such as wildfire monitoring (Bailon-Ruiz et al., 2022), search-and-rescue
(Alotaibi et al., 2019), and security surveillance (Yun et al., 2022), unmanned aerial vehicle (UAV) systems are increasingly used to provide rapid and flexible aerial coverage. As UAV autonomy advances,
operators are no longer required to manually control flight paths or avoid obstacles (Chen et al., 2023;
Chien et al., 2010; Lewis et al., 2010; Tang et al., 2022). Instead, they are tasked with supervising multiple autonomous UAVs while interpreting the visual information those UAVs return (Lewis, 2013).
This shift in responsibility has transformed the operator’s role from a manual controller into that of a
high-level information integrator who must build and maintain situation awareness (SA) across a complex and dynamic environment (Lewis, 2013; Lewis et al., 2010).
From the perspective of SA content, multi-UAV supervision requires two forms of situational awareness. System-oriented SA concerns awareness of UAV locations, trajectories, and operational status,
whereas environment-oriented SA involves interpreting the elements and events observed in the external scene (Endsley, 1995; MahmoudZadeh et al., 2024; Sarter & Woods, 2017). In many real-world
operations such as wildfire reconnaissance, UAVs follow largely autonomous and preplanned trajectories (Chandarana et al., 2021; Scherer et al., 2015; Yang et al., 2016). As a result, the operator’s primary
challenge shifts from controlling UAV behavior to interpreting and integrating environmental information from multiple asynchronous video feeds. However, prior work has predominantly emphasized system-oriented monitoring (Agrawal & Cleland-Huang, 2021; Mademlis et al., 2023; Porat et al., 2016;
Scherer et al., 2015), leaving environment-oriented SA in multi-UAV visual tasks comparatively
underexplored.
CONTACT Michael Lewis cmlewis@pitt.edu School of Computing and Information, University of Pittsburgh, Pittsburgh, PA
15260, USA.
 2026 Taylor & Francis Group, LLC
INTERNATIONAL JOURNAL OF HUMAN–COMPUTER INTERACTION
https://doi.org/10.1080/10447318.2026.2622580

---
**[Page 3]**

Against this background, understanding the factors that influence users’ SA and exploring the potential support enabled by recent advances in AI are essential for developing more effective multi-UAV
monitoring systems. Research in related domains such as autonomous driving offers useful insights
into factors that may influence SA, including environmental complexity, task demands, interface design,
and information layout (Jia et al., 2024; Jiang et al., 2023; Lu et al., 2017; Zhou et al., 2022). These factors can be broadly categorized into environmental and interface factors. At the same time, recent progress in large language models (LLMs) has introduced new possibilities for AI-based visual
interpretation and reasoning, raising questions about how such capabilities might support or even
replace human operators in complex surveillance tasks (Korteling et al., 2021; Raiaan et al., 2024; Xi
et al., 2025).
Building on the identified gaps in environment-oriented SA and the theoretical insights drawn from
related SA domains and recent LLM advancements, this study investigates the following research
questions:
RQ1: How do environmental factors such as target density and fire precedence affect users’ situation
awareness in multi-UAV supervision tasks?
RQ2: How do interface-related factors such as display layout and support for retrospective access influence users’ situation awareness?
RQ3: How does SA construction differ when multi-UAV observation tasks are performed by human
operators versus LLMs?
To address these questions, we conducted an experimental study using a simulated wildfire monitoring system, in which both human participants and LLMs supervised multiple UAVs scanning a
large forested area. Regarding environmental factors, we manipulated target density by varying the
number of relevant objects in the environment and manipulated fire precedence by changing the
temporal order between the wildfire and related targets. For interface-related factors, we manipulated the display layout by varying how video feeds and map elements were spatially arranged, and
we controlled retrospective access by enabling or disabling users’ ability to revisit previously
observed information. During the experiment, we measured object-specific and global SA using
SPAM-based (Situation Present Assessment Method) and SAGAT-based (Situation Awareness Global
Assessment Technique) queries, respectively. In addition, we qualitatively analyzed participants’
open-ended feedback to identify usage challenges and expectations for system improvement. The
findings highlight users’ need for dynamic support in maintaining SA and lead to actionable design
recommendations for future multi-UAV systems. We further discuss the potential for human–LLM
collaboration in such tasks.
Based on the above experiment and analysis, this study makes two primary contributions. First, it
provides a systematic examination of environment-oriented SA in multi-UAV visual monitoring,
addressing a key gap in prior research that has largely focused on system-oriented supervision. Second,
it offers a direct comparison between human operators and LLM-based agents, revealing fundamental
differences in how SA is constructed across agent types. Together, these contributions deepen the
understanding of SA in multi-UAV operations and inform the design of future human–AI collaborative
monitoring systems.
2. Related work
2.1. Multi-UAV supervision: Control-centric paradigms
Early research on multi-UAV systems has primarily emphasized control-centric paradigms, focusing on
path planning, task allocation, and UAV status monitoring to improve autonomy and reduce operator
workload under complex mission conditions (Agrawal & Cleland-Huang, 2021; Mademlis et al., 2023;
Parnell et al., 2023; Porat et al., 2016; Scherer et al., 2015). For example, Agrawal and Cleland-Huang
(2021) conducted a series of empirical studies with subject matter experts to explore operator capabilities in multi-UAV supervision and control scenarios. In their system design, users were primarily
2 L. JIA ET AL.

---
**[Page 4]**

tasked with supervising UAV status and mission execution, including monitoring health indicators, verifying task progress, and intervening when necessary, rather than interpreting the visual or contextual
data returned by UAVs. Similarly, Porat et al. (2016) explored Human-on-the-Loop paradigms in emergency response scenarios and proposed system-level improvements aimed at enhancing operator SA
through explanations of UAV autonomy. Their work evaluated user SA in such systems but also primarily focused on UAV behavior.
However, as noted by Lewis et al. (2010) and Lewis (2013), as UAV control becomes increasingly
automated, the system bottleneck has shifted from manual operation to effectively exploiting the information returned by the UAVs. This shift is particularly evident in remote sensing contexts such as
wildfire monitoring. Unlike urban search-and-rescue tasks that demand continuous UAV control and
frequent path replanning, wildfire reconnaissance typically operates on predefined UAV trajectories,
placing the operator’s primary focus on understanding the environment depicted in the UAV video
feeds (Chandarana et al., 2021). This shift also means that users’ SA demands move from system-oriented monitoring to environment-oriented understanding, which involves interpreting people, vehicles,
fires, and evolving risks in the scene.
Gugerty and Brooks (2004) point out that even interpreting video feeds from a single UAV can pose
significant SA challenges, particularly in terms of spatial orientation and contextual understanding.
These difficulties are magnified in multi-UAV settings, where users must cope with higher information
load, asynchronous viewpoints, and more complex cross-view integration. Yet despite their practical
importance, these environment-oriented SA challenges remain underexplored and insufficiently
addressed in current research.
2.2. Environment-oriented SA in visual monitoring tasks
According to the theory of Endsley (2021), environment-oriented SA can be conceptualized as a threelevel process. Level 1 SA involves the perception of relevant elements in the environment, such as
detecting people, vehicles, or fire. Level 2 entails comprehension of the current situation by understanding the implications of those elements, such as the spread status of a wildfire, whether a vehicle is
approaching a hazardous area, or whether a hiker is in potential danger. Level 3 SA requires projection,
involving the anticipation of how the situation may evolve, such as forecasting the spread direction of a
wildfire or determining whether a rescue operation may be necessary. In wildfire monitoring, higherlevel SA is essential for recognizing emerging threats and supporting timely containment or evacuation
decisions (Yang et al., 2016). At the same time, the higher-level SA depends on the accuracy of underlying perceptual judgments, errors at lower levels can cascade and impair operators’ ability to form reliable projections (Endsley, 2021). This interdependence underscores both the necessity and the difficulty
of supporting environment-oriented SA across all three levels in dynamic visual monitoring contexts.
Modeling user SA in different settings and understanding what forms of system support are needed
is therefore essential for identifying human capability limits and designing effective human–agent collaboration systems. Although environment-oriented SA in multi-UAV systems received limited attention, similar issues have been extensively studied in other domains such as autonomous driving (Jia
et al., 2024; Jia & Du, 2025; Lu et al., 2017; Zhou et al., 2024). Research in these areas shows that users’
ability to maintain SA is shaped by a number of contextual and interface-related factors. For example,
higher environmental complexity can increase attentional demands and degrade hazard detection (Jia
et al., 2024), while heavy task load or interruptions impair the integration of spatial and temporal cues
(Zhou et al., 2024). In addition, the organization of interface elements and the interaction modalities
provided by the system can shape how effectively users construct accurate mental models of the environment (Ding et al., 2024). Collectively, these elements, including environmental complexity, task
demands, interface components, and interface layout, can be understood as environmental or interface
factors, each of which has been shown to shape SA performance in specific operational contexts.
INTERNATIONAL JOURNAL OF HUMAN–COMPUTER INTERACTION 3

---
**[Page 5]**

2.3. The potential of AI in visual reasoning and surveillance
Recent advances in large language models (LLMs), particularly in visual reasoning, semantic understanding, and contextual interpretation, have enabled these models to interpret complex environments
in ways that increasingly resemble human understanding (Cong-Lem et al., 2025; Korteling et al., 2021;
Raiaan et al., 2024; Xi et al., 2025). For instance, studies on Visual Large Language Models demonstrate
their ability to integrate multimodal inputs, including text, imagery, and environmental cues, to perform general-purpose visual reasoning across both static and dynamic contexts (Zhang et al., 2024).
The study of Chen et al. (2024) also shows that these models extend beyond basic object recognition
and are capable of performing geometric and spatial reasoning in static images. Such capabilities open
new possibilities for supporting or even replacing humans in cognitively demanding tasks.
Traditionally, humans have been viewed as superior in tasks requiring creativity, common sense, and
complex problem-solving—such as developing tactical SA from multiple observations (Gavrilenko &
Morozova, 2018; Monroe, 2020). In contrast, machine contributions in surveillance have historically
been limited to aided target recognition (AiTR), where automated systems assist in detection and classification, but final judgments are left to human operators (Ling et al., 2024; Sterling & Jacobson, 2006;
Zhang et al., 2025). Given the rapid advancements in LLMs, it is now timely and valuable to empirically revisit these assumptions by directly comparing their performance with that of human operators in
a shared surveillance task. It is also necessary to explore how LLMs might contribute to multi-UAV
wildfire reconnaissance systems.
2.4. Comparative summary and research gap
Table 1 summarizes how prior work aligns with the key dimensions relevant to this research. As
shown, no existing study has jointly examined environment-oriented SA, multi-UAV visual monitoring,
and human–AI performance comparison within a unified framework, a gap that the present study directly addresses.
3. Method
3.1. System design and stimuli
We developed an interactive simulation environment to examine how users maintain SA while supervising multiple UAVs engaged in wildfire reconnaissance. Each UAV was scripted to follow a fixed
flight path across a large-scale forested area and was portrayed as autonomously scanning the terrain
for salient objects, such as hikers, vehicles, or signs of wildfire. While the UAVs could present highresolution visual data and flag potential points of interest, they were not capable of interpreting object
identity, assessing situational risk, or making contextual inferences. These higher-order reasoning tasks
were delegated entirely to the human operator. Users were required to click on each system-flagged target, review the associated zoomed-in footage, and annotate the object’s identity and contextual status
(e.g., movement direction, need for rescue). In the following sections, we describe the system in detail
from two perspectives: the user interface and the simulation design.
Table 1. Comparison of prior work and the present study.
Representative studies Environmental SA Human-AI comparison Multi-UAV context
Porat et al. (2016)   
Agrawal and Cleland-Huang (2021)   
SA studies in other domains
(Ding et al., 2024; Lu et al., 2017)   
AI-supported visual reasoning
(Ling et al., 2024; Zhang et al., 2025) Partial  
This study 
4 L. JIA ET AL.

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

3.1.1. Interface and interactive design
The experiment included four distinct interface conditions, designed to examine how layout and temporal access structure influence users’ ability to build and maintain SA. The four interfaces were labeled
as the Synchronous interface, the ASynchronous interface, the Synchronous-Ablated interface, and the
ASynchronous-Ablated interface. While these conditions differed in synchronization and feature availability, their core layout and interaction logic remained consistent. As illustrated in Figure 1, the
ASynchronous interface example shows that the system consists of two primary components: the Live
Video Feed panel and the Map Overview panel. The Live Video Feed Panel displayed real-time footage
from each UAV, with color-coded borders to help users distinguish among different sources. When a
UAV encountered a predefined important target, a red bounding box was overlaid on the video to
highlight it. The Map Overview Panel mirrored this information by placing an object marker at the
corresponding geographic location on the map. By clicking on a marker, users could view a zoomed-in
video of the target’s local context. At the same time, an annotation window appeared, prompting users
to evaluate the target based on the detailed footage and surrounding context. In addition, the map displayed the current position of each UAV and the area it was covering, using color-coded rectangles
that matched the borders of the video feeds.
As illustrated in Figure 2, both the Synchronous Interface and the two Ablated Interfaces were
adapted from the ASynchronous Interface, with modifications made according to their respective condition characteristics.
The primary difference between the Synchronous and ASynchronous conditions lies in the support
for retrospective access. In the asynchronous condition an icon is placed on the map when a target is
detected and the operator can view video of the transit over the target whenever the icon is selected. In
contrast, in the Synchronous Interface, users could access zoomed-in footage by clicking directly on the
red bounding box marking the important target within the live video feed (Figure 2(a)). This means
that once the target moves out of the current UAV’s field of view, users can no longer review its
detailed imagery. The corresponding object markers on the map were displayed only after the user
completed the annotation. The synchronous view encourages users to focus on immediate real-time
observations while the asynchronous view allows users to load balance across platforms to accommodate multiple contemporaneous targets.
Figure 1. The ASynchronous interface. The left panel shows live video feeds from six UAVs with color-coded borders,
while the right map panel displays the UAV footprints and system-flagged targets as clickable icons. Selecting a target
icon opens a zoomed-in video and an annotation window, allowing participants to provide SPAM-based object-specific
judgments.
INTERNATIONAL JOURNAL OF HUMAN–COMPUTER INTERACTION 5

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

Figure 2. The Synchronous interface and the two ablated variants. (a) The Synchronous interface. Zoomed-in views are
only available while a target remains in the current UAV’s field of view, limiting retrospective access. (b) The two
ablated interfaces. The live video panel is removed, and users can access zoomed-in views via map markers, with or
without temporal constraints depending on the condition.
6 L. JIA ET AL.

---
**[Page 8]**

The two Ablated conditions are shown in Figure 2(b). They shared a key modification: the removal
of the Live Video Feed Panel on the left side of the interface to reduce visual load and isolate the
effects of targeted, on-demand information access. Users no longer had access to continuous UAV
video streams and could only view the zoomed-in footage of targets by interacting with object markers
on the map. Compared to the ASynchronous-Ablated Interface, the Synchronous-Ablated Interface
retained the same temporal constraint found in its non-ablated counterpart: users could only access
zoomed-in footage for targets currently within a UAV’s field of view. If the UAV passed over a target
and the user did not complete the annotation in time, the corresponding map marker would disappear,
preventing any further interaction with that object.
3.1.2. Stimuli and scenario design
The experimental scenario simulated a multi-UAV wildfire reconnaissance mission over a forested
region modeled after the Cleveland National Forest to enhance ecological validity. Six UAVs flew side
by side from left to right at a constant speed, covering the entire target area within a 10-minute mission window. The simulation was set on January 8 2025, during a period of strong Santa Ana wind
activity. Drawing on wind condition maps from that date, historical wildfire data, and contextual geographic features such as roads, vegetation, and recreational zones, a team of six human-computer interaction researchers collaboratively designed and refined the spatial distribution of task-relevant elements
(Esri, n.d.; Ventusky, n.d.). The layout underwent multiple design iterations to strike a balance between
ecological realism and experimental control. Figure 3 illustrates the final scenario featured 45 targets
strategically distributed across the environment: 4 active wildfires, 13 vehicles, 23 hikers (including 3
near visible campfires), and 5 deliberately inserted false alarms (none).
The system integrated two complementary engines to enhance the realism of the simulation and
ensure flexible deployment: Unreal Engine for high-fidelity visual rendering and Unity for interface
development, experimental logic, and web-based distribution. As shown in Figure 1, the terrain of the
Cleveland National Forest was reconstructed in Unreal Engine using global 3D geospatial data via the
Cesium plugin. Guided by satellite imagery and the planned spatial layout of task-relevant elements,
the environment was populated with 3D assets such as vegetation, buildings, vehicles, and hikers, each
accompanied by context-appropriate animations to simulate plausible motion and behavior. We replicated aerial surveillance by configuring virtual cameras to match typical UAV-mounted camera specifications, including an 84 field of view and square 4K resolution (3840  3840 pixels) (DSLRPros, n. d.).
UAVs were simulated at an altitude of 2 km and equipped with 20 digital zoom capability
(DSLRPros, n. d.), allowing detailed inspection of the terrain. Based on this setup, both wide-area patrol
footage and zoomed-in target views were prerecorded for experimental use. The user interface and
interactive logic were then implemented in Unity, where the pre-rendered videos from Unreal were
uploaded to Google Cloud and streamed into the Unity application to simulate real-time reconnaissance feeds. Participant interactions, including camera movements and target selections, were logged
within Unity and uploaded via Unity Cloud Services for later analysis. The final Unity project was
exported as a WebGL build and deployed through Netlify, enabling seamless online access and centralized experiment distribution.
3.2. Experiment design and procedure
3.2.1. Human participant experiment
The design was mixed, consisting of a 4 (Interface Type; between-subjects)  2 (Query Scope; withinsubjects) structure, with additional nested manipulations of Target Density and Fire Precedence specific
to the respective query scopes. Interface Type was manipulated between participants, with each participant randomly assigned to one of four interface conditions: Synchronous, ASynchronous, SynchronousAblated, or ASynchronous-Ablated. As illustrated in Figure 3, within each interface condition, participants completed both object-specific queries, responding to each target as it appeared, and global
queries that summarized all relevant objects observed within a given measurement interval.
Given the distinct temporal and cognitive characteristics of the object-specific and global SA tasks,
separate within-subject factors were introduced for each. For object-specific queries, an additional
INTERNATIONAL JOURNAL OF HUMAN–COMPUTER INTERACTION 7

---
**[Page 9]**
*(This page contains a figure/chart/image not captured in text)*

within-subject factor was Target Density, which varied based on the number of targets appearing within
a given time window. Figure 3 illustrates the critical object locations and SAGAT query regions. The
environment was divided into nine vertical columns, each containing between 1 and 9 targets. Columns
with more than five targets were categorized as high-density, while those with fewer than four were
considered low-density. For global queries, a separate within-subject factor was Fire Precedence, defined
as the temporal order in which wildfires and related objects appeared. Each participant encountered
four global queries. In the first two, wildfires appeared before the associated objects, whereas in the latter two, the wildfires appeared afterward. Participants were instructed to respond only to newly
observed targets that had not been included in any previous queries.
During the experiment, participants first completed a consent form and demographic questionnaire,
followed by an interactive training session (Figure 4). The training introduced key interface components, target types (e.g., hiker, vehicle, wildfire), and sample annotations. Participants then proceeded
to the main task, which lasted approximately 10 min. During the task, six UAVs simultaneously
scanned the environment from left to right, and participants annotated detected targets or answered
global queries at designated points. At the end of the task, participants completed an open-ended questionnaire to provide feedback on task difficulty, interface usability, and system support for situational
awareness.
3.2.2. LLM evaluation
We conducted an exploratory evaluation using OpenAI’s GPT-4o model (OpenAI, n.d.) to examine
how an LLM might perform on similar SA tasks. We implemented a simulated observer agent using
the GPT API, structured to reflect the cognitive demands placed on human participants. The instructional materials given to human participants included task objectives, scenario context, map descriptions, and sample SA questions. The same information was encoded as system-level prompts to guide
the model’s responses.
Figure 3. Critical object locations and SAGAT query regions. The forested area is divided into nine vertical columns,
each containing a predefined set of targets. Shaded regions indicate the four areas corresponding to SAGAT-based global queries.
8 L. JIA ET AL.

---
**[Page 10]**
*(This page contains a figure/chart/image not captured in text)*

For object-specific annotation tasks (SPAM-based), the agent was sequentially provided with (1) the
annotation history of prior targets, (2) five evenly sampled frames from the current target’s zoomed-in
video, and (3) the object’s map location. For global SA queries (SAGAT-based), the agent received (1)
the spatial coordinates of all objects within the relevant query region and (2) five representative frames
for each object. In both cases, the model was prompted with the corresponding SA questions, requiring
it to respond to Level 1–3 queries (as listed in Table 2) by integrating visual and spatial information to
infer object identity, relationships, and potential risks.
Interface layout was not manipulated in the LLM evaluation. Unlike human participants, the LLM
was not affected by interface structure, as it could directly access system-highlighted video frames and
spatial metadata without the need for navigation or interface-based interaction. All queries were executed with the model in deterministic mode (temperature ¼ 0), producing stable, single-response outputs for each prompt.
3.3. Measurements
As shown in Table 2, object-specific local SA was measured using SPAM (Evans, 2017), which prompts
participants to make real-time judgments about the identity, spatial relation, and risk level of systemhighlighted targets without disrupting task flow. Participants responded based on the scenario’s current
state. Global SA was measured using the SAGAT (Endsley, 1988), in which the simulation was paused
at predefined moments and participants answered questions requiring recall and reasoning about multiple previously observed targets. The simulation then resumed from the same point. This SPAM–
SAGAT sequence also approximates cognitive patterns found in real-world monitoring tasks: operators
often make immediate, perceptual judgments during continuous observation and later integrate information across time or space when the situation allows or requires (Okoli et al., 2022). At the end of
the task, participants were asked to describe what they found most challenging.
3.4. Data analysis
For the quantitative data collected via SPAM and SAGAT, participants’ responses were scored for
accuracy based on ground truth annotations. Linear mixed-effects models were used to analyze the
effects of SA Level, Query Scope, Target Density, and Fire Precedence, as well as their interactions with
SA Level. Subject-level random intercepts were included to account for repeated measures. When significant fixed effects or interactions were found, post hoc analyses with Bonferroni correction were conducted to examine performance differences across task conditions and cognitive levels. Exploratory
analyses using the same statistical approach examined whether accuracy and error patterns differed by
Figure 4. Overview of the experimental procedure and task flow.
Table 2. Examples of SA questions by query Scope and SA level.
Query scope SA level Example query
Object-specific annotation (SPAM-based) Level 1: Perception What is this object? (Vehicle/hiker/wildfire/nothing)
Level 2: Comprehension Is this object approaching the wildfire? (for hiker/vehicle);
will it spread? (for wildfire)
Level 3: Projection Does this object need a warning or rescue? (for hiker/
vehicle); where might the fire spread? (for wildfire)
Global multi-object query (SAGAT-Based) Level 1: Perception How many targets were detected by UAV-X since the last
survey?
Level 2: Comprehension How many of those targets are moving toward the wildfire?
Level 3: Projection How many of the targets are likely to require warning or
rescue based on the situation?
INTERNATIONAL JOURNAL OF HUMAN–COMPUTER INTERACTION 9

---
**[Page 11]**

object category (e.g., wildfire, hiker, vehicle). In addition, we descriptively compared performance patterns between human participants and the GPT-4o model under matched task conditions, without conducting inferential tests due to the single-response nature of the model.
Open-ended responses were analyzed using inductive thematic coding by two independent coders.
All responses were first segmented into meaningful units and reviewed iteratively to identify recurring
themes related to task difficulty, interface usability, and SA support. A preliminary codebook was developed collaboratively, then refined through discussion and applied to a subset of responses to assess coding consistency. Inter-coder reliability was evaluated using Cohen’s Kappa, and any discrepancies were
resolved through consensus. The finalized codebook was subsequently used to annotate the full dataset
and summarize participants’ common challenges and design suggestions.
3.5. Participants
A power analysis conducted prior to data collection using GPower (effect size f ¼ 0.15, a ¼ 0.05,
power ¼ 0.95) indicated that a minimum of 272 participants would be required (Faul et al., 2007). We
recruited 400 participants (100 per interface condition) from the United States through the
CloudResearch platform, ensuring sufficient statistical power and balanced comparisons across conditions (Hartman et al., 2023). Each participant was randomly assigned to one interface condition and
restricted from participating in multiple conditions to prevent learning effects and cross-condition contamination. A total of 393 participants completed the study and provided usable data (97 in the
Synchronous condition, 98 in the ASynchronous condition, 99 in the Synchronous-Ablated condition,
and 99 in the ASynchronous-Ablated condition). The average participant age was 36.43 years (SD ¼
10.85), with 200 identifying as male and 200 as female across the final sample. The whole study lasted
approximately 30 min, and participants received $5 in compensation.
4. Results
4.1. Differences between SPAM-based local SA and SAGAT-based global SA
As shown in Figure 5, both the main effects of query scope, F(1, 393) ¼ 3163.43, p < 0.001, and interface condition, F(3, 393) ¼ 16.06, p < 0.001, on SA accuracy were significant. In addition, there was a
significant interaction between query scope and interface type, F(3, 393) ¼ 6.28, p < 0.001. Post-hoc
comparisons showed that, across all interface types, participants’ SA accuracy was significantly higher
for object-specific queries than for global queries, all ps < 0.001. Furthermore, for object-specific SA,
the Asynchronous interface, the Asynchronous-Ablated interface, and the Synchronous-Ablated interface resulted in significantly higher precision than the Synchronous interface, all ps < 0.001. For global
SA, however, no significant differences in accuracy were observed across interface types.
4.2. SPAM-based local SA and its influencing factors
4.2.1. Effects of task and interface factors on object-specific SA accuracy
SA accuracy in object-specific queries was significantly affected by interface type, F(1, 393) ¼ 12.79,
p < 0.001, target density, F(1, 1971) ¼ 857.75, p < 0.001, and SA level, F(2, 1971) ¼ 458.21, p < 0.001.
The interaction between target density and SA level was also significant, F(2, 1971) ¼ 28.16, p < 0.001.
However, no significant interactions were found between target density and interface type, F(3, 1971)
¼ 1.28, p ¼ 0.281, or between SA level and interface type, F(6, 1971) ¼ 0.43, p ¼ 0.860.
Post-hoc comparisons revealed two key patterns (Figure 6). On the one hand, SA accuracy was consistently higher in the low-density condition than in the high-density condition across all SA levels, all
ps < 0.001. On the other hand, within the low-density condition, SA accuracy declined significantly
from Level 1 to Level 2, p < 0.001 and from Level 1 to Level 3, p < 0.001, while the difference between
Level 2 and Level 3 was not significant, p ¼ 0.108. In contrast, under the high-density condition, all
pairwise differences between SA levels were significant, ps < 0.001, with the largest decline observed
between Level 1 and Level 3.
10 L. JIA ET AL.

---
**[Page 12]**
*(This page contains a figure/chart/image not captured in text)*

4.2.2. Patterns of annotation error types
We classified responses into three types to better understand user errors in object-specific queries:
Missed Annotations (failure to annotate a present object), Incorrect Annotations (labeling errors in
identity or status), and False Positive Annotations (annotating when no object was present). There were
significant main effects of error type, F(2, 786) ¼ 200.67, p < 0.001, and interface type, F(3, 393) ¼
14.79, p < 0.001, as well as a significant interaction between the two factors, F(6, 786) ¼ 18.61,
p < 0.001.
The specific patterns were shown in Figure 7. Within the Missed Annotations error type, post-hoc
comparisons showed that the Synchronous interface resulted in significantly more missed annotations
than all other interfaces, all ps < 0.001. In addition, while no significant difference was found between
the Asynchronous and Asynchronous-Ablated interfaces, p ¼ 0.897, both the difference between
Asynchronous and Synchronous-Ablated, p ¼ 0.026 and the difference between Asynchronous-Ablated
and Synchronous-Ablated, p ¼ 0.025, were statistically significant. However, no significant differences
across interface types were found for Incorrect Annotations or False Positive Annotations. Within each
Figure 5. SA accuracy across the two query scopes under four interface conditions. Bars show the mean accuracy for
each interface–query combination, with pairwise significance levels indicated above the comparisons. We use the following indications in all applicable figures and tables: p < 0.05 (), p < 0.01 (), and p < 0.001 (). Error bars represent ±2 standard errors.
Figure 6. Object-specific SA accuracy across target density and SA level. The bars represent mean accuracy for each
density–SA level combination, and significance markers denote pairwise differences within each condition.
INTERNATIONAL JOURNAL OF HUMAN–COMPUTER INTERACTION 11

---
**[Page 13]**
*(This page contains a figure/chart/image not captured in text)*

interface, pairwise contrasts revealed that False Positive Annotations were consistently more frequent
than both Incorrect Annotations and Missed Annotations, all ps < 0.001.
4.2.3. Target-specific variations in object-specific SA accuracy
To further examine object-specific SA across different types of targets, we compared participants’ SA
accuracy for queries involving vehicles, hikers, wildfires, and non-target areas. There were significant
main effects of interface type, F(3, 397) ¼ 9.43, p < 0.001, target type, F(3, 4367) ¼ 206.87, p < 0.001,
and SA level, F(2, 4367) ¼ 688.99, p < 0.001, as well as significant interactions between target type and
interface, F(9, 4367) ¼ 16.49, p < 0.001, and between target type and SA level, F(6, 4367) ¼ 303.22,
p < 0.001. However, the interaction between interface type and SA level was not significant, F(6, 4367)
¼ 1.35, p ¼ 0.229.
Regarding the interaction between interface type and target type (Figure 8(a)), pairwise comparisons
revealed that SA accuracy for Vehicle and Hiker targets was significantly lower in the Synchronous
interface than in all other interface types (ps < 0.001). In contrast, for Wildfire and None targets, no
significant differences in SA accuracy were observed across interfaces. As illustrated in Figure (8b),
across all interface conditions, SA accuracy for None targets was significantly higher than for the other
three target types, all ps < 0.001, and Wildfire targets were associated with higher accuracy than Hiker
targets, all ps < 0.05. More specifically, in Synchronous-Ablated and Synchronous interfaces, SA accuracy for Wildfire targets was significantly higher than for Vehicle targets, all ps < 0.001. Furthermore,
in the Synchronous-Ablated condition, accuracy for Wildfire targets also exceeded that for Hiker targets, p ¼ 0.0023.
Regarding the interaction between SA Level and target Type, on the one hand, pairwise comparisons
across SA levels revealed a consistent decline in performance from Level 1 to Level 3 for Vehicle,
Hiker, and Wildfire targets (Figure 9(a)). For these target types, SA accuracy decreased significantly
from Level 1 to Level 2 and from Level 2 to Level 3, all ps < 0.0001. In contrast, a different trend was
observed for None targets: SA accuracy was significantly lower at Level 1 compared to both Level 2
and Level 3, ps < 0.0001, with no significant difference between Level 2 and Level 3, p ¼ 0.56. On the
other hand, at SA Level 1, accuracy differed significantly across all four target types, all ps < 0.001,
with the highest performance for None, followed by Wildfire, Vehicle, and Hiker (Figure 9(b)). This
trend persisted across SA Levels 2 and 3, though some differences became non-significant. Specifically,
at Level 2, differences between Vehicle and Hiker and between Wildfire and None were not statistically
significant, ps > 0.05, while all other comparisons remained significant, ps < .001. At Level 3, the difference between Vehicle and Hiker was also not significant, p ¼ 0.552, though all remaining contrasts
were significant, ps < 0.001.
Figure 7. Annotation error patterns across interface types. Bars represent the mean frequency of each error type for
each interface condition. Significance markers indicate pairwise statistical differences within error types across interfaces.
12 L. JIA ET AL.

---
**[Page 14]**
*(This page contains a figure/chart/image not captured in text)*

4.3. SAGAT-based global SA and its influencing factors
Participants’ SA accuracy in response to global queries was significantly influenced by SA level, F(2,
4353) ¼ 125.83, p < 0.001, interface type, F(3, 393) ¼ 2.86, p ¼ 0.037, and fire precedence, F(1, 4353) ¼
6.58, p ¼ 0.010. A significant interaction was also observed between SA level and fire precedence, F(2,
4353) ¼ 72.90, p < 0.001. However, the interaction between interface type and fire precedence, F(3,
4353) ¼ 1.01, p ¼ 0.385, as well as the interaction between SA level and interface type, F(6, 4353) ¼
0.89, p ¼ 0.499, were not statistically significant.
As seen in Figure 10, while the previous analysis in the above section did not reveal a significant effect of interface type on SAGAT-based global SA accuracy, post-hoc analyses focusing specifically on SAGAT revealed a modest but statistically significant difference between the
Asynchronous-Ablated and Synchronous interfaces, p ¼ 0.032. However, no other pairwise comparisons among interface types reached significance, all ps > 0.1, indicating that interface effects under
SAGAT were limited.
SA accuracy patterns varied across SA levels depending on whether the wildfire appeared before or
after the related targets (Figure 11). When the wildfire appeared after the related targets, SA accuracy
declined consistently from Level 1 to Level 3, ps < 0.001. In contrast, when the wildfire appeared
before the related targets, SA accuracy at Level 1 was significantly lower than at both Level 2 and Level
Figure 8. SA accuracy by target type and interface type. The two subfigures use target type and interface type as the
horizontal axes to show different comparisons, with bars indicating mean accuracy and markers denoting significant
contrasts. S: Synchronous; AS: Asynchronous; S-Ablated: Synchronous-Ablated; AS-Ablated: Asynchronous-Ablated. (a) SA
accuracy differences across target types. (b) SA accuracy differences across interface types.
Figure 9. SA accuracy by target type and SA level. The two subfigures use target type and SA level as the horizontal
axes to show different comparisons, with bars indicating mean accuracy and markers denoting significant contrasts. (a)
SA accuracy differences across target types. (b) SA accuracy differences across SA levels.
INTERNATIONAL JOURNAL OF HUMAN–COMPUTER INTERACTION 13

---
**[Page 15]**
*(This page contains a figure/chart/image not captured in text)*

3, ps < 0.001, with Level 2 accuracy also exceeding that of Level 3, p < 0.001. Direct comparisons
between the two fire timing conditions revealed that SA accuracy was significantly higher when the
wildfire appeared after the targets than when it appeared before at both Level 1 (p < 0.001) and Level 3
(p ¼ 0.0028). However, this pattern reversed at Level 2, where accuracy was significantly higher when
the wildfire appeared before the targets, p < 0.001.
4.4. User-reported challenges across interface conditions
Open coding showed an already almost perfect level of initial agreement (j ¼ 0:91). The two coders
then reviewed and resolved the remaining discrepancies through discussion to produce the final coding
set. According to Table 3, qualitative analysis of the open-ended feedback identified four categories of
task-related difficulties, ranging from memory and cognitive demands to temporal pressure and spatial
interpretation challenges, highlighting core usability bottlenecks in dynamic multi-UAV supervision.
The distribution of these difficulty types across different interface conditions is illustrated in Figure 12.
Overall, memory demands were the most frequently reported challenge, followed by time pressure,
multitasking overload, and difficulties with directional and dynamic judgments. Notably, reports of
memory load and time pressure were more prevalent under the Synchronous and Synchronous-ablated
Figure 10. Comparison of global SA accuracy across interface types. Bars represent the mean SAGAT accuracy under
each interface condition, with significance markers denoting pairwise differences among interfaces.
Figure 11. Global SA accuracy across fire precedence and SA level. The two subfigures use fire precedence and SA level
as the horizontal axes to show different comparisons, with bars indicating mean accuracy and markers denoting significant contrasts. (a) SA Accuracy by SA Level and Fire Precedence. (b) SA Accuracy by Fire Precedence and SA Level.
14 L. JIA ET AL.

---
**[Page 16]**
*(This page contains a figure/chart/image not captured in text)*

interfaces. In contrast, multitasking overload and directional/dynamic judgment difficulties were
reported more frequently under the Asynchronous and Asynchronous-ablated interfaces.
4.5. Human-LLM comparison in SA tasks
Figure 13 shows the comparison results between human participants (under the better-performing
Asynchronous interface condition) and the LLM across the two query scopes. The results revealed distinct performance patterns. For Object-Specific Queries, the LLM demonstrated comparable performance to human participants at SA Level 1, but performed worse on SA Level 2 and Level 3 queries. In
contrast, for Global Queries, the LLM outperformed human users across all three SA levels.
5. Discussion
5.1. Cognitive constraints and task demands in SA construction during multi-UAV supervision
5.1.1. Limitations of human cognitive architecture
Our results revealed two important patterns in users’ SA performance that reflect fundamental limitations of human cognitive architecture.
First, participants achieved significantly higher accuracy in object-specific (local) queries than in global queries. This difference reflects the limits of human cognition: while local queries allow for realtime, perception-driven responses, global queries require memory-based reasoning and cross-target
integration, which depend on both working memory and retrieval and are more susceptible to overload.
Table 3. Categories of user-reported task challenges in multi-UAV supervision.
Category Description Representative quote
Memory load and recall limitation Users had to recall critical details (e.g.,
number, direction, type, UAV identifier)
after completing tasks, without access to
the map or past content.
“Trying to remember how many hikers or
vehicles were in UAV 4 box or UAV 5
box … why do I have to memorize
that?”
Fast task pace and time pressure Rapid UAV movement and frequent target
appearance made users feel rushed to
process all events in time.
“I didn’t have enough time to even finish
one annotation before several more
popped up.”
Cognitive load from multitasking Users were required to simultaneously
monitor multiple UAVs, recognize targets,
judge direction and threat, and complete
annotations.
“Too many task to do. I had to check
videos, identify hikers, judge if they were
in danger, and label them—all at the
same time.”
Directional and dynamic judgments Users struggled to determine whether a
target was moving toward fire or at risk,
especially when both UAVs and fires
were moving.
“It was hard to tell if the hiker was headed
into the fire, especially when the UAVs
and the fire were both moving. No clear
cues.”
Figure 12. Distribution of user-reported challenge types across interface conditions. The bars illustrate the relative frequency of each difficulty category was mentioned within each interface condition.
INTERNATIONAL JOURNAL OF HUMAN–COMPUTER INTERACTION 15

---
**[Page 17]**
*(This page contains a figure/chart/image not captured in text)*

According to dual-process theories, these memory- and retrieval-intensive operations engage the slower,
effortful analytical system, making users more prone to error in dynamic and high-pressure environments (Evans, 2017). Participants’ feedback further confirmed this difficulty, citing challenges in recalling past targets and expressing a need for system features to support both memory and retrieval, such
as visual histories or automated logging.
Second, participants’ accuracy decreased significantly as SA level increased, with the most pronounced decline observed at Level 3 (projection). This pattern aligns with Endsley’s model of SA
(Endsley, 2021), which posits that higher-level SA requires not only perception and comprehension but
also the ability to construct mental models and anticipate future developments. Such predictive reasoning imposes substantial cognitive demands and is more vulnerable to error, particularly in dynamic
environments. Participants also echoed this challenge in their qualitative feedback, noting that estimating fire spread or identifying which targets might require rescue was especially difficult when visual
information was incomplete or rapidly evolving. Some also described confusion regarding spatial relationships between targets and hazards, and difficulty processing multiple objects appearing
simultaneously.
Performance differences across interface designs suggest promising strategies for mitigating the
impact of memory and reasoning constraints. The Synchronous interface yielded the lowest accuracy in
both object-specific and global SA tasks, indicating that its layout and access limitations impeded effective SA construction. Specifically, although the live video feed panel provided additional elevation
imagery, the unmagnified views were often insufficient for detailed target inspection and introduced
extra cognitive demands. The need to shift attention between the live feed and the map also increased
task-switching costs. Furthermore, restricting access to previously seen areas placed additional burden
on working memory, as users were required to retain and reconstruct earlier observations without the
ability to revisit prior visual information. In contrast, interfaces that supported retrospective access or
reduced visual clutter helped users maintain situational continuity. These findings underscore the role
of interface design in managing cognitive load and highlight concrete directions for supporting SA
through structural affordances.
5.1.2. The dynamic nature of SA during multi-UAV supervision
Beyond fixed cognitive constraints, our results highlight the dynamic nature of SA as it unfolds over
time (Endsley, 1995; Smith & Hancock, 1995). Users’ SA performance varied not only by task type or
Figure 13. Comparison of SA accuracy between human participants and the LLM. The two subfigures compare
human and LLM performance across SA levels for object-specific and global queries, respectively, with bars representing
averaged performance. (a) SA Accuracy by SA Level and Fire Precedence. (b) SA Accuracy by Fire Precedence and SA
Level.
16 L. JIA ET AL.

---
**[Page 18]**

level, but also in response to evolving task conditions such as target density, target type, and the temporal order of critical events.
For instance, participants’ accuracy in annotating individual targets declined significantly when multiple objects appeared within a brief time window. As visual and cognitive load increased, users became
more prone to attentional lapses and selective encoding. Participants also reported feeling overwhelmed
when many elements competed for attention, noting difficulty in determining which objects were most
urgent or relevant.
Temporal structure further shaped SA outcomes because the order in which events appeared influenced how users allocated attention and constructed meaning. In global queries involving both wildfires
and targets, performance differed by whether the fire appeared before or after the objects. When the
fire appeared first, Level 1 accuracy decreased, likely because the fire’s high salience drew attention
away from subsequently presented targets, leading to incomplete perceptual encoding. In contrast, Level
2 accuracy improved under this condition, suggesting that early fire visibility provided an anchor for
interpreting spatial relationships and promoting more integrative reasoning. These results indicate that
cognitive strategies adapt to event sequencing: early salient cues may facilitate global integration while
simultaneously impairing local perception due to attentional competition.
In addition, the nature of observed objects influenced SA dynamics. Accuracy differed by target
type, with Hiker and Vehicle targets yielding lower performance, particularly in the Synchronous interface. When targets required more nuanced interpretation, such as posture, motion, or vulnerability,
interface constraints like limited contextual access and increased memory demands further impaired
SA. This variability adds to the potential volatility of SA in real-world settings, where users may
encounter diverse targets differing in type, size, color, and contextual relevance.
These findings illustrate that SA is not merely a function of task complexity or individual ability, but
also of how and when key information is introduced. Supporting SA therefore requires not only reducing cognitive load but also helping users manage attention dynamically and form coherent mental models as the situation evolves.
5.2. Distinct strengths of humans and LLMs in SA
The results revealed distinct strengths between human operators and the LLM in constructing SA,
depending on task type and SA level. Humans outperformed the LLM in object-specific tasks, especially
at Levels 2 and 3. In these tasks, contextual interpretation and real-time reasoning were critical. In contrast, the LLM demonstrated better performance in global, multi-object queries that required integrating
spatial patterns and projecting risks across multiple targets. This finding contrasts with prior
approaches that typically use machine learning for automated target detection while relying on human
operators to integrate information and make decisions, and suggests new possibilities for redistributing
tasks between humans and AI to better align with their respective strengths, especially in highly timecritical environments (Kim, 2023; Senoner et al., 2024).
On the one hand, the key factor underlying these differences is working memory. As we discussed,
human operators must rely on limited cognitive resources to retain and integrate information over
time, especially under multitasking or time pressure. This constraint likely contributed to the lower
accuracy observed in global queries and in projection-level SA tasks. LLMs, by contrast, are not subject
to the same memory limitations. They maintain access to all relevant input, such as sampled frames
and spatial metadata, through internal representations, enabling consistent access to distributed information throughout the reasoning process (Bubeck et al., 2023).
On the other hand, the LLM functions as a perceptual reasoning system trained on large-scale language and visual data. While it performs competitively in many SA tasks by extracting patterns, comparing spatial structures, and synthesizing distributed cues, it may still fall short when interpreting
ambiguous or context-dependent inputs. This limitation may be partly attributed to the absence of
human-like reasoning flexibility, as humans can dynamically engage both intuitive and deliberative
thinking processes, as described in dual-process theory (Evans, 2008; Frankish, 2010). Furthermore,
humans benefit from robust semantic grounding and extensive real-world knowledge built through
INTERNATIONAL JOURNAL OF HUMAN–COMPUTER INTERACTION 17

---
**[Page 19]**

embodied experience (Barsalou, 2008; Lake et al., 2017). These factors allow humans to contextualize
uncertainty and apply generalizable reasoning strategies in ways current LLMs cannot fully replicate
These findings suggest complementary roles for humans and LLMs in supervisory settings. While
humans excel in real-time perceptual judgment and semantic interpretation, LLMs can assist with
memory-intensive global reasoning by synthesizing spatial-temporal information. Effective collaboration
may depend on aligning each agent’s strengths with the appropriate SA subtask.
5.3. Design implications for supporting users in multi-UAV supervision tasks
Our findings reveal key challenges to SA in multi-UAV supervision, stemming from cognitive limitations, dynamic task conditions, and mismatches between user capabilities and system structures. These
insights inform three complementary design directions to better support users.
First, interface design should proactively reduce memory demands and support continuous comprehension. Among the tested layouts, the Synchronous interface which characterized by segregated views
and limited retrospective access led to the lowest SA performance. In contrast, layouts that supported
persistent access to prior targets or minimized visual clutter promoted more stable awareness. Future
designs should integrate structural elements such as snapshot panels, collapsible history timelines, or
dynamic filters to alleviate cognitive load and allow users to focus on relevant items without losing
access to broader context. Additionally, simple annotation tools or visual counters could help users
track progress and reduce the burden of internal recall during complex monitoring tasks.
Second, SA systems must account for the evolving demands of dynamic environments. User performance varied with target density, event precedence, and target type, all of which are often unpredictable in real-world missions. These fluctuations underscore the need for interfaces that adapt in real
time to shifting task complexity. Beyond providing visual cues or escalation mechanisms for overlooked
elements, systems can leverage behavioral indicators such as eye movements, fixation duration, or
physiological markers to predict SA states. Based on such predictions, interfaces could dynamically
adjust their presentation by highlighting uninspected areas, postponing non-urgent updates, or summarizing recent changes, thereby supporting effective attention allocation and coherent situational
understanding.
Finally, the complementary capabilities of human users and LLMs suggest promising directions for
hybrid supervisory systems. Humans are well suited for perceptual interpretation, risk judgment, and
context-sensitive reasoning, while LLMs can support tasks that require memory-intensive tracking,
multi-target comparison, and pattern-based inference. Future interfaces should enable division of labor
by assigning real-time interpretation and high-stakes decision-making to human operators, while offloading data summarization, status monitoring, or anomaly detection to AI agents.
5.4. Limitations and future work
While the present study provides insights into how task characteristics, interface design, and agent type
influence situation awareness in multi-UAV supervision, several limitations should be acknowledged.
First, our design introduced controlled event sequences and structured query modes to enable systematic manipulation of task factors, although with some randomization included to reduce predictability. In addition, the study relied on pre-rendered simulation videos. These settings may differ in some
respects from the visual conditions of real operations. Future work could collect video and event data
from actual wildfire missions to construct more realistic and ecologically grounded simulation environments. Future work could also build mappings between SA and physiological signals, enabling realtime, non-intrusive SA assessment without forced queries and supporting more natural and flexible
task execution. Second, while the findings may extend to highly automated multi-UAV missions, tasks
involving frequent route adjustments that require simultaneous system-oriented and environment-oriented SA may present additional challenges for future research. Third, the comparison involving LLMs
remains exploratory. On the one hand, the model used was a general-purpose, pre-trained agent without fine-tuning for SA tasks. On the other hand, in real deployments, LLM performance and usability
may depend on available computational resources, the format and variability of inputs, and potential
18 L. JIA ET AL.

---
**[Page 20]**

latency. Future work could incorporate these factors to more accurately assess LLM capabilities in
supervisory contexts and examine how users calibrate trust when collaborating with such agents.
Finally, the participants in this study were drawn from the general population rather than professional
UAV operators. While the findings offer foundational insights into environmental SA mechanisms,
future research should validate these results with expert operators and examine how operational experience shapes SA performance and human–AI collaboration in multi-UAV settings.
6. Conclusion
This study examined how environmental and interface-related factors shape users’ SA in multi-UAV
supervision and compared human performance with that of a LLM. By evaluating 393 participants and
GPT-4o in a simulated wildfire monitoring task involving both object-specific and global SA queries, we
identified key patterns that reflect the cognitive demands and design sensitivities of such systems. Human
participants demonstrated strong performance on object-specific tasks but showed marked declines in SA
accuracy as task complexity increased, particularly at higher SA levels and under high target density.
Interfaces that centralized key information and enabled retrospective access significantly improved performance, suggesting the importance of reducing memory load and supporting temporal integration. In
contrast, GPT-4o excelled in global, pattern-based queries but underperformed in context-sensitive object
interpretation, highlighting complementary strengths between humans and LLMs. These findings can be
generalized to opportunities for developing supportive interface features and enhancing real-time human–
AI collaboration. On the one hand, features such as map-embedded object summaries, retrospective
access, and timeline replay can be incorporated into monitoring interfaces. On the other hand, AI agents
can assist by tracking targets and summarizing patterns, and by generating attention cues that highlight
critical changes or emerging risks. By combining human strengths in interpretation with AI’s data-handling capabilities, hybrid systems can improve SA and mission performance in fast-paced environments.
This research provides empirical evidence and actionable insights for designing adaptive multi-UAV interfaces that account for users’ cognitive limitations, leverage complementary human–AI strengths, and
ultimately enhance SA and mission performance in dynamic, high-stakes environments. Future work
could advance this line of research by incorporating expert operators, more realistic and richer environments, and evaluations of fine-tuned LLMs into cognitive models. Studies should also account for deployment-related factors such as LLMs’ latency and computational limits.
Acknowledgments
The views and conclusions contained in this document are those of the authors and should not be interpreted as
representing the official policies, either expressed or implied, of the DEVCOM Analysis Center or the U.S.
Government. The U.S. Government is authorized to reproduce and distribute reprints for Government purposes
notwithstanding any copyright notation herein.
Ethical approval
This study was reviewed and approved by the Institutional Review Board at the University of Pittsburgh. All participants provided informed consent before participating in the study.
Author contributions
CRediT: Lesong Jia: Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Software,
Visualization, Writing – original draft, Writing – review & editing; Kiran Shridhar Alva: Conceptualization,
Methodology, Software, Validation; Huao Li: Conceptualization, Methodology, Validation; Werner Hager:
Conceptualization, Methodology, Validation; Lucia Romero: Conceptualization, Methodology, Validation;
Timothy Albert Butler: Conceptualization, Methodology, Validation; Michael Lewis: Conceptualization, Funding
acquisition, Methodology, Project administration, Resources, Supervision, Validation, Writing – original draft,
Writing – review & editing.
INTERNATIONAL JOURNAL OF HUMAN–COMPUTER INTERACTION 19

---
**[Page 21]**

Disclosure statement
No potential conflict of interest was reported by the author(s).
Funding
This research was sponsored by the DEVCOM Analysis Center and accomplished under Cooperative Agreement
Number W911NF-22-2-0001.
ORCID
Lesong Jia http://orcid.org/0000-0002-3950-0905
References
Agrawal, A., & Cleland-Huang, J. (2021). Explaining autonomous decisions in swarms of human-on-the-loop small
unmanned aerial systems. Proceedings of the AAAI Conference on Human Computation and Crowdsourcing,
9(1), 15–26. https://doi.org/10.1609/hcomp.v9i1.18936
Alotaibi, E. T., Alqefari, S. S., & Koubaa, A. (2019). LSAR: Multi-UAV collaboration for search and rescue missions. IEEE Access, 7, 55817–55832. https://doi.org/10.1109/ACCESS.2019.2912306
Bailon-Ruiz, R., Bit-Monnot, A., & Lacroix, S. (2022). Real-time wildfire monitoring with a fleet of uavs. Robotics
and Autonomous Systems, 152, 104071. https://doi.org/10.1016/j.robot.2022.104071
Barsalou, L. W. (2008). Grounded cognition. Annual Review of Psychology, 59(1), 617–645. https://doi.org/10.1146/
annurev.psych.59.103006.093639
Bubeck, S., Chandrasekaran, V., Eldan, R., Gehrke, J., Horvitz, E., Kamar, E., Lee, P., Lee, Y. T., Li, Y., Lundberg,
S., Nori, H., Palangi, H., Ribeiro, M., & Zhang, Y. (2023). Sparks of artificial general intelligence: Early experiments with gpt-4. arXiv: preprint arXiv:2303.12712. https://doi.org/10.48550/arXiv.2303.12712
Chandarana, M., Hughes, D., Lewis, M., Sycara, K., & Scherer, S. (2021). Planning and monitoring multi-job type
swarm search and service missions. Journal of Intelligent & Robotic Systems, 101(3), 1–14. https://doi.org/10.
1007/s10846-020-01272-3
Chen, B., Xu, Z., Kirmani, S., Ichter, B., Sadigh, D., Guibas, L., & Xia, F. (2024). Spatialvlm: Endowing vision-language models with spatial reasoning capabilities [Paper presentation]. Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition (pp. 14455–14465), Seattle, WA, USA. https://doi.org/10.1109/
CVPR52733.2024.01370
Chen, Z., Xiong, X., Wang, W., Xiao, Y., & Alfarraj, O. (2023). A blockchain-based multi-unmanned aerial vehicle
task processing system for situation awareness and real-time decision. Sustainability, 15(18), 13790. https://doi.
org/10.3390/su151813790
Chien, S.-Y., Wang, H., & Lewis, M. (2010). Human vs. algorithmic path planning for search and rescue by robot
teams. Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 54(4), 379–383. https://doi.
org/10.1177/154193121005400423
Cong-Lem, N., Soyoof, A., & Tsering, D. (2025). A systematic review of the limitations and associated opportunities of chatgpt. International Journal of Human–Computer Interaction, 41(7), 1–16. https://doi.org/10.1080/
10447318.2024.2344142
Ding, Y., Jia, L., & Du, N. (2024). One size does not fit all: Designing and evaluating criticality-adaptive displays in
highly automated vehicles [Paper presentation]. Proceedings of the 2024 CHI Conference on Human Factors in
Computing Systems (pp. 1–15), Honolulu, HI, USA. https://doi.org/10.1145/3613904.3642648
DSLRPros. (n.d). Professional drones & UAV solutions [Retrieved June 22, 2025]. https://www.dslrpros.com/
Endsley, M. R. (1988). Situation awareness global assessment technique (sagat) [Paper presentation]. Proceedings of
the IEEE 1988 National Aerospace and Electronics Conference (pp. 789–795), Dayton, OH, USA. https://doi.
org/10.1109/NAECON.1988.195097
Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems. Human Factors: The Journal of
the Human Factors and Ergonomics Society, 37(1), 32–64. https://doi.org/10.1518/001872095779049543
Endsley, M. R. (2021). Situation awareness. In G. Salvendy & W. Karwowski (Eds.), Handbook of human factors
and ergonomics (pp. 434–455). John Wiley & Sons. https://doi.org/10.1002/9781119636113.ch17
Esri (n.d). ArcGIS online [Retrieved June 22, 2025]. https://www.arcgis.com/
Evans, J. S. B. (2008). Dual-processing accounts of reasoning, judgment, and social cognition. Annual Review of
Psychology, 59(1), 255–278. https://doi.org/10.1146/annurev.psych.59.103006.093629
Evans, J. S. B. (2017). Dual process theory: Perspectives and problems. In J. S. B. T. Evans & K. Frankish (Eds.),
Dual Process Theory 2.0, 137–155. Routledge. https://doi.org/10.4324/9781315204550
20 L. JIA ET AL.

---
**[Page 22]**

Faul, F., Erdfelder, E., Lang, A.-G., & Buchner, A. (2007). G power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences. Behavior Research Methods, 39(2), 175–191. https://doi.
org/10.3758/BF03193146
Frankish, K. (2010). Dual-process and dual-system theories of reasoning. Philosophy Compass, 5(10), 914–926.
https://doi.org/10.1111/j.1747-9991.2010.00330.x
Gavrilenko, A., & Morozova, K. (2018). Machine common sense concept paper. arXiv preprint arXiv:1810.07528.
https://doi.org/10.48550/arXiv.1810.07528
Gugerty, L., & Brooks, J. (2004). Reference-frame misalignment and cardinal direction judgments: Group differences and strategies. Journal of Experimental Psychology–Applied, 10(2), 75–88. https://doi.org/10.1037/1076-898X.
10.2.75
Hartman, R., Moss, A. J., Jaffe, S. N., Rosenzweig, C., Litman, L., & Robinson, J. (2023). Introducing connect by
cloudresearch: Advancing online participant recruitment in the digital age. PsyArXiv preprint. https://doi.org/10.
31234/osf.io/ksgyr
Jia, L., & Du, N. (2025). Modeling driver situational awareness in takeover scenarios using multimodal data and
machine learning. International Journal of Human–Computer Interaction, 1–19. https://doi.org/10.1080/
10447318.2025.2546046
Jia, L., Huang, C., & Du, N. (2024). Drivers’ situational awareness of surrounding vehicles during takeovers:
Evidence from a driving simulator study. Transportation Research Part F: Traffic Psychology and Behaviour, 106,
340–355. https://doi.org/10.1016/j.trf.2024.08.016
Jiang, J., Karran, A. J., Coursaris, C. K., Leger, P.-M., & Beringer, J. (2023). A situation awareness perspective on
human-AI interaction: Tensions and opportunities. International Journal of Human–Computer Interaction,
39(9), 1789–1806. https://doi.org/10.1080/10447318.2022.2093863
Kim, H. (2023). Suggestions for ethical decision-making model through collaboration between human and AI. JINSTITUTE, 8, 12–22. https://doi.org/10.22471/ai.2023.8.12
Korteling, J. E., van de Boer-Visschedijk, G. C., Blankendaal, R. A., Boonekamp, R. C., & Eikelboom, A. R. (2021).
Human-versus artificial intelligence. Frontiers in Artificial Intelligence, 4, 622364. https://doi.org/10.3389/frai.
2021.622364
Lake, B. M., Ullman, T. D., Tenenbaum, J. B., & Gershman, S. J. (2017). Building machines that learn and think
like people. The Behavioral and Brain Sciences, 40, e253. https://doi.org/10.1017/S0140525X16001837
Lewis, M. (2013). Human interaction with multiple remote robots. Reviews of Human Factors and Ergonomics,
9(1), 131–174. https://doi.org/10.1177/1557234X13506688
Lewis, M., Wang, H., Chien, S. Y., Velagapudi, P., Scerri, P., & Sycara, K. (2010). Choosing autonomy modes for
multirobot search. Human Factors, 52(2), 225–233. https://doi.org/10.1177/0018720810366859
Lewis, M., Wang, H., Chien, S.-Y., Scerri, P., Velagapudi, P., Sycara, K., & Kane, B. (2010). Teams organization
and performance in multi-human/multi-robot teams [Paper presentation]. 2010 IEEE International Conference
on Systems, Man and Cybernetics (pp. 1617–1623), Istanbul, Turkey. https://doi.org/10.1109/ICSMC.2010.
5642379
Ling, S., Zhang, Y., & Du, N. (2024). More is not always better: Impacts of AI-generated confidence and explanations in human–automation interaction. Human Factors, 66(12), 2606–2620. https://doi.org/10.1177/
00187208241234810
Lu, Z., Coster, X., & De Winter, J. (2017). How much time do drivers need to obtain situation awareness? A
laboratory-based study of automated driving. Applied Ergonomics, 60, 293–304. https://doi.org/10.1016/j.apergo.
2016.12.003
Mademlis, I., Torres-Gonzalez, A., Capitan, J., Montagnuolo, M., Messina, A., Negro, F., Le Barz, C., Gonc¸alves,
T., Cunha, R., Guerreiro, B., Zhang, F., Boyle, S., Guerout, G., Tefas, A., Nikolaidis, N., Bull, D., & Pitas, I.
(2023). A multiple-UAV architecture for autonomous media production. Multimedia Tools and Applications,
82(2), 1905–1934. https://doi.org/10.1007/s11042-022-13319-8
MahmoudZadeh, S., Yazdani, A., Kalantari, Y., Ciftler, B., Aidarus, F., & Al Kadri, M. O. (2024). Holistic review
of UAV-centric situational awareness: Applications, limitations, and algorithmic challenges. Robotics, 13(8), 117.
https://doi.org/10.3390/robotics13080117
Monroe, D. (2020). Seeking artificial common sense. Communications of the ACM, 63(11), 14–16. https://doi.org/
10.1145/3422588
Okoli, J., Watt, J., & Weller, G. (2022). A naturalistic decision-making approach to managing non-routine fire
incidents: Evidence from expert firefighters. Journal of Risk Research, 25(2), 198–217. https://doi.org/10.1080/
13669877.2021.1936609
OpenAI. (n.d.). GPT-4o [Retrieved June 22, 2025]. https://platform.openai.com/
Parnell, K. J., Fischer, J. E., Clark, J. R., Bodenmann, A., Galvez Trigo, M. J., Brito, M. P., Divband Soorati, M.,
Plant, K. L., & Ramchurn, S. D. (2023). Trustworthy UAV relationships: Applying the schema action world taxonomy to UAVS and UAV swarm operations. International Journal of Human–Computer Interaction, 39(20),
4042–4058. https://doi.org/10.1080/10447318.2022.2108961
INTERNATIONAL JOURNAL OF HUMAN–COMPUTER INTERACTION 21

---
**[Page 23]**

Porat, T., Oron-Gilad, T., Rottem-Hovev, M., & Silbiger, J. (2016). Supervising and controlling unmanned systems:
A multi-phase study with subject matter experts. Frontiers in Psychology, 7, 568. https://doi.org/10.3389/fpsyg.
2016.00568
Raiaan, M. A. K., Mukta, M. S. H., Fatema, K., Fahad, N. M., Sakib, S., Mim, M. M. J., Ahmad, J., Ali, M. E., &
Azam, S. (2024). A review on large language models: Architectures, applications, taxonomies, open issues and
challenges. IEEE Access, 12, 26839–26874. https://doi.org/10.1109/ACCESS.2024.3365742
Sarter, N. B., & Woods, D. D. (2017). Situation awareness: A critical but ill-defined phenomenon. In E. Salas
(Ed.), Situational Awareness (pp. 445–458). Routledge. https://doi.org/10.4324/9781315087924
Scherer, J., Yahyanejad, S., Hayat, S., Yanmaz, E., Andre, T., Khan, A., Vukadinovic, V., Bettstetter, C.,
Hellwagner, H., & Rinner, B. (2015). An autonomous multi-UAV system for search and rescue [Paper presentation]. Proceedings of the First Workshop on Micro Aerial Vehicle Networks, Systems, and Applications for
Civilian Use (pp. 33–38), Florence, Italy. https://doi.org/10.1145/2750675.2750683
Senoner, J., Schallmoser, S., Kratzwald, B., Feuerriegel, S., & Netland, T. (2024). Explainable AI improves task performance in human–ai collaboration. Scientific Reports, 14(1), 31150. https://doi.org/10.1038/s41598-024-82501-9
Smith, K., & Hancock, P. A. (1995). Situation awareness is adaptive, externally directed consciousness. Human
Factors: The Journal of the Human Factors and Ergonomics Society, 37(1), 137–148. https://doi.org/10.1518/
001872095779049444
Sterling, B. S., Jacobson, C. N. (2006). A human factors analysis of aided target recognition technology (Tech. rep.
ARL-TR-3959) [Final report, Sep 2005–Sep 2006. Approved for public release; distribution is unlimited.]. Army
Research Laboratory, Human Research and Engineering Directorate. Aberdeen Proving Ground, MD. https://
apps.dtic.mil/sti/pdfs/ADA456440.pdf
Tang, J., Lao, S., & Wan, Y. (2022). Systematic review of collision-avoidance approaches for unmanned aerial
vehicles. IEEE Systems Journal, 16(3), 4356–4367. https://doi.org/10.1109/JSYST.2021.3101283
Ventusky. (n.d.). Weather forecast map [Retrieved June 22, 2025]. https://www.ventusky.com/
Xi, Z., Chen, W., Guo, X., He, W., Ding, Y., Hong, B., Zhang, M., Wang, J., Jin, S., Zhou, E., Zheng, R., Fan, X.,
Wang, X., Xiong, L., Zhou, Y., Wang, W., Jiang, C., Zou, Y., Liu, X., … Gui, T.,. (2025). The rise and potential
of large language model based agents: A survey. Science China Information Sciences, 68(2), 121101. https://doi.
org/10.1007/s11432-024-4222-0
Yang, C., Chen, J., & Su, G. (2016). Effective situational awareness to wildfire emergency command based on multimodel forecasting system [Paper presentation]. Proceedings of the Second ACM SIGSPATIALInternational
Workshop on the Use of GIS in Emergency Management (pp. 1–3), Burlingame, CA, USA. https://doi.org/10.
1145/3017611.3017612
Yun, W. J., Park, S., Kim, J., Shin, M., Jung, S., Mohaisen, D. A., & Kim, J.-H. (2022). Cooperative multiagent
deep reinforcement learning for reliable surveillance via autonomous multi-UAV control. IEEE Transactions on
Industrial Informatics, 18(10), 7086–7096. https://doi.org/10.1109/TII.2022.3143175
Zhang, J., Huang, J., Jin, S., & Lu, S. (2024). Vision-language models for vision tasks: A survey. IEEE Transactions
on Pattern Analysis and Machine Intelligence, 46(8), 5625–5644. https://doi.org/10.1109/TPAMI.2024.3369699
Zhang, J., Wang, Z., Chen, J., Wang, F., & Gao, L. (2025). An automated framework for abnormal target segmentation in levee scenarios using fusion of UAV-based infrared and visible imagery. Remote Sensing, 17(20), 3398.
https://doi.org/10.3390/rs17203398
Zhou, F., Yang, X. J., & De Winter, J. C. (2022). Using eye-tracking data to predict situation awareness in real
time during takeover transitions in conditionally automated driving. IEEE Transactions on Intelligent
Transportation Systems, 23(3), 2284–2295. https://doi.org/10.1109/TITS.2021.3069776
Zhou, K., Wang, C., Xie, S., Zhou, Y., Zhang, X., Wang, Y., & Tang, H. (2024). Effect of task interruption on the
situation awareness of air traffic controllers. PLOS One, 19(11), e0314183. https://doi.org/10.1371/journal.pone.
0314183
About the authors
Lesong Jia is a PhD student in Information Science at the University of Pittsburgh. He received his bachelor’s
and master’s degrees from Southeast University, China. His research interests include situation awareness,
human–computer interaction, and intelligent system design.
Kiran Shridhar Alva is a Software Engineer at Allegheny County and a former Research Assistant at the
University of Pittsburgh. She received an MSIS degree from the University of Pittsburgh. Her interests include
cloud computing, ETL pipelines, and database systems.
Huao Li is a Postdoctoral Fellow for Engineering Excellence in the Department of Aeronautics and Astronautics
and the Laboratory for Information and Decision Systems at MIT. He received his PhD from the University of
Pittsburgh. His research focuses on human-centered AI and human–agent collaboration.
22 L. JIA ET AL.

---
**[Page 24]**

Werner Hager is a PhD student in the Intelligent Systems Program at the University of Pittsburgh. His research
interests include physics-informed machine learning, computer vision, anomaly detection, and reinforcement
learning.
Lucia Romero is a graduate student researcher at the University of Pittsburgh. Her research focuses on human–
agent collaboration and multi-agent reinforcement learning. She received her bachelor’s degree in computer science from Arizona State University and is pursuing an MS in Information Science.
Timothy Albert Butler has a professional background in engineering leadership and operational environments.
He has served as a Fellow at the University of Pittsburgh.
Michael Lewis is a Professor in the Department of Informatics and Networked Systems at the University of
Pittsburgh. His research focuses on human interaction with intelligent automation, including human–robot interaction, human–agent teamwork, and visualization-based control interfaces.
INTERNATIONAL JOURNAL OF HUMAN–COMPUTER INTERACTION 23