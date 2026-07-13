# Zhou

*Source file: Zhou.pdf — 13 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

Design and Artificial Intelligence 1 (2025) 100029
Contents lists available at ScienceDirect
Design and Artificial Intelligence
journal homepage: https://www.keaipublishing.com/en/journals/design-and-artificial-intelligence/
Full Length Article
Towards human-centered interaction with UAV swarms: Framework,
system design, and user study ✩
Zihong Zhoua,b, Pengjin Wei c, Zhiyi Wanga,b, Leyi Duana,b, Siyuan Hai a,b, Zuhang Zhanga,b,
Yujie Suna,b, Fuyong Fenga,b,∗
a Collective Intelligence & Collaboration Laboratory, Beijing 100072, China b China North Artificial Intelligence & Innovation Research Institute, Beijing 100072, China c Shanghai Aerospace Control Technology Institute, Shanghai 201109, China
a r t i c l e i n f o
Keywords:
Human-swarm interaction
Human-centered design
UAV swarm
Design method
a b s t r a c t
As unmanned aerial vehicle (UAV) swarms gain traction in military, logistics, and emergency response scenarios,
the demand for “one-to-many” UAV swarm controlling continues to grow, positioning human–swarm interaction
(HSI) as a critical area of UAV swarm research. However, existing UAV swarm control systems focus primarily on
autonomy and low-level control, often neglecting operator cognition and human factors at the interaction level.
This oversight frequently leads to high cognitive load and reduced control efficiency, particularly in scenarios
involving large-scale, heterogeneous information and complex task coordination. To address these challenges,
and drawing on extensive experience from existing UAV swarm control system projects, we propose a humancentered HSI interaction framework grounded in the classical observe–orient–decide–act (OODA) cognitive model
to represent the operator’s decision-making process. The framework introduces six HSI-adapted design principles
that guide system development across interaction workflows, interface layout, task representation mechanisms,
etc. Based on this framework, we develop an HSI prototype system that enables a single operator to control
more than 20 UAVs simultaneously. We then evaluate its performance through user studies across usability,
interaction efficiency, and cognitive support dimensions. Experimental results provide preliminary evidence that
the proposed approach may reduce operator cognitive load and contribute to improved control performance,
though further refinements are needed in specific interaction details and interface optimization.
1. Introduction
Unmanned aerial vehicle (UAV) swarms represent a class of multiagent systems composed of multiple UAVs operating in coordination to
accomplish complex tasks that are difficult or impossible for a single
UAV to complete. In recent years, UAV swarms have found increasing
application in domains such as military operations, logistics, emergency
response, and entertainment. These systems are progressively reshaping
human–technology and human–environment interactions from urban
lifestyles to the shape of the war. For instance, in military contexts, the
transformation is particularly striking: Soldiers now deploy large-scale
micro-drone swarms to conduct wide-area intelligence gathering, coordinated strikes, and long-range electronic interference, fundamentally
redefining modern combat operations in ways that have drawn global attention. Despite advances in autonomy, technical and ethical constraints
mean that the role of human operators in command decision-making,
intent expression, and anomaly handling remains indispensable in UAV
✩ Peer review under responsibility of Editorial Board of Design and Artificial Intelligence ∗ Corresponding author.
E-mail addresses: zihongzhou@163.com (Z. Zhou), ffymieluo@126.com (F. Feng).
swarm systems [1–6]. As a result, human–swarm interaction (HSI) has
emerged as a key research focus in UAV swarm system design. Central
challenges in HSI include the development of cognitive-friendly interaction mechanisms, reduction of operator workload, enhancement of
information visualization, and improvement of human–swarm collaboration effectiveness.
Current studies on UAV swarms largely concentrate on system’s autonomous capabilities, such as swarm control [7–11], task planning [12–
15], and autonomous obstacle avoidance [16–18]. Most system designs
prioritize enhancing autonomy, with insufficient attention to human factors and user-centered requirements [5,19–21]. As swarm sizes scale up,
the systems generate vast quantities of heterogeneous and multimodal
data, including visual, positional, postural, and auditory information
during task execution [21,22]. This deluge of information poses significant cognitive challenges to human operators, increasing the risk of
cognitive overload and loss of situational awareness [23–26]. Moreover,
under the “one-to-many” control paradigm, operators must frequently
https://doi.org/10.1016/j.daai.2025.100029
Received 22 July 2025; Received in revised form 26 August 2025; Accepted 1 September 2025
Available online 4 September 2025
3050-7413/Copyright © 2025 The Authors. Publishing services by Elsevier B.V. on behalf of Zhejiang University Press Co., Ltd. and KeAi Communications Co. Ltd.
This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/)

---
**[Page 2]**

Z. Zhou, P. Wei, Z. Wang et al. Design and Artificial Intelligence 1 (2025) 100029
switch between individual drones or sub-swarms while maintaining an
understanding of overall swarm behavior and performing localized interventions. This multi-level cognitive demand leads to operational inefficiencies and a heightened risk of human error [27–29]. Therefore,
there is an urgent need for human-centered HSI design methods that systematically address the above interaction challenges through carefully
designed interaction workflows, expressive information visualization,
and adaptive task allocation mechanisms.
To address these pressing challenges, we propose a human-centered
HSI framework for UAV swarm systems, targeting issues related to cognitive load and control inefficiency. The framework adopts the classical observe–orient–decide–act (OODA) model to represent the cognitive and decision-making processes of the operator and introduces six
HSI-adapted design principles to systematically guide interaction design
that facilitates efficient OODA loop iteration. Building on this framework, we developed an HSI prototype system, with specific focus on
interaction workflows, interface layouts, and task intent representation
mechanisms. Finally, we conducted both quantitative and qualitative
user studies to evaluate the system’s usability and performance, demonstrating its effectiveness and adaptability in supporting HSI.
2. Related work
2.1. Human–swarm interaction
UAV swarms are distributed autonomous systems inspired by natural collective intelligence, such as bird flocks and fish schools [30,31].
Through local sensing and the execution of simple behavioral rules, individual UAVs achieve emergent coordination, demonstrating strong flexibility and robustness. These systems are increasingly being deployed
in real-world scenarios such as search and rescue, reconnaissance, and
security patrols. As swarm sizes continue to grow, the challenge of designing efficient and controllable HSI mechanisms has become a critical research problem at the intersection of human–computer interaction
(HCI) and swarm intelligence. As the core of this interdisciplinary research direction, HSI has seen growing attention in recent years, with
notable progress in interaction modalities, situational awareness, task
planning, and operator mental models.
Interaction modalities. Researchers have explored emerging input
techniques such as speech [32–34], body gestures [35,36], hand movements [37–41], eye tracking [42,43], and brain–computer interfaces
[44,45] to enhance the control of unmanned systems. However, most
of these efforts focus on basic motion-level tasks—such as formation
transitions, obstacle avoidance, or low-level maneuvering—primarily in
single-drone or homogeneous swarm settings. These approaches struggle to support the flexible issuance of high-level, semantically rich commands for complex mission scenarios.
Situational awareness. Traditional swarm visualization techniques,
typically based on aggregating the status of individual agents, are increasingly insufficient for large-scale swarms. Such representations can
easily overwhelm the operator, leading to cognitive overload and a
breakdown in global awareness [23,24,26]. To address this, researchers
have explored new interface paradigms [19,24,46–48] and integrated
sensory modalities such as haptic feedback [49,50], augmented reality
(AR) [51,52], and mixed reality (MR) [53,54] to enhance the operator’s
multidimensional understanding of swarm behaviors.
Task planning. Recent advances have leveraged large language models (LLMs) to support real-time generation of group-level tasks and control instructions [55–59]. These approaches enable operators to interact
with swarms using intuitive natural language, significantly lowering the
barrier to complex task delegation. However, LLM-based planning still
faces challenges such as limited execution precision, reduced controllability, and high computational resource requirements, making it difficult
to apply in dynamic environments that demand real-time coordination
and swarm-level task management.
Mental models. Existing studies have examined key cognitive constructs, such as system transparency [1,60–62], trust [5,63–66], and explainability [67–70], that influence how operators interpret and predict
swarm behavior. Nonetheless, there remains a lack of systematic, actionable design theories and methodologies for addressing these cognitive
challenges in practical HSI system development.
2.2. Ground control station for multi-UAVs
As the central component of UAV swarm command and control
systems, the ground control station (GCS) plays a pivotal role in situational awareness, mission planning, flight supervision, and payload
management [71–73]. Its design has a direct impact on both the operational safety of the swarm and the effectiveness of mission execution.
In response to increasing mission complexity and the growing trend toward swarm-based operations, GCS platforms have evolved from simple
remote-control terminals into integrated, modular, and intelligent command platforms [71].
Recent research in this area has primarily focused on standardizing
system architectures and generalizing GCS functional modules. These
efforts aim to address issues such as tight coupling between software
functionalities, poor module reusability, and incompatibility caused by
differences in UAV configurations, all of which lead to repetitive development and integration challenges [74–77]. At the same time, a subset of studies has begun to explore GCS design from a human factors
perspective, with a focus on reducing operator cognitive load and optimizing interaction workflows to enhance situational understanding and
cognitive alignment during swarm task execution [78,79].
However, most existing GCS systems are designed for medium to
large-scale UAVs and are typically deployed in fixed or vehicle-mounted
formats, relying on multi-operator collaboration for effective operation.
Portable GCS solutions, on the other hand, are often limited to basic control over small, homogeneous UAV formations [72,80,81] and are inadequate for handling complex tasks that require flexible control, high-level
strategic intent expression, and robust cognitive support. In particular,
as swarm sizes increase and operational environments become more dynamic, conventional GCS architectures show significant limitations in
areas such as operator strategy modeling, recognition of cognitive states,
and support for task intent articulation. These shortcomings result in
overly complex interaction workflows and high barriers to effective operation. As such, there is a growing need to develop next-generation
GCS interaction architectures that support task abstraction, cognitive
compatibility, and seamless human–machine coordination. This represents a critical direction for advancing swarm command capabilities in
future UAV applications.
3. Research motivation
While recent human factors research on UAV swarm systems has
made meaningful progress in areas such as interaction modalities, visualization interfaces, and system transparency, significant challenges
remain in supporting complex operational demands in real-world task
environments.
The motivation for this research stems from the authors’ direct involvement in the design and development of a UAV swarm project
(Fig. 1) aimed at enabling “one-to-many” interactions between a single
operator and a large number of micro quadrotors, operated through a
portable GCS. Through the course of this project, it became increasingly
clear that the primary bottleneck to the practical deployment of UAV
swarm systems is no longer rooted in core technical capabilities—such
as formation control, target recognition, or autonomous obstacle avoidance—which have reached a relatively mature level. Instead, the critical challenge lies in the lack of a human-centered, cognitively grounded
interaction logic in existing HSI system design. This shortcoming significantly constrains human–swarm collaboration efficiency and places a
heavy cognitive burden on the operator.
2

---
**[Page 3]**
*(This page contains a figure/chart/image not captured in text)*

Z. Zhou, P. Wei, Z. Wang et al. Design and Artificial Intelligence 1 (2025) 100029
Fig. 1. A swarm of unmanned aerial vehicles (UAVs) preparing to execute a coordinated mission during system deployment.
During system implementation, several persistent interaction challenges emerged, including the high mental load of interpreting swarmlevel situational dynamics, the cumbersome nature of task orchestration, and the lack of flexibility in issuing control commands. A review
of existing systems, including several notable experiments from the U.S.
DARPA OFFSET program [5,52,54,82], revealed that these problems are
not isolated incidents but are pervasive in contemporary swarm control
interfaces. For example, in the domain of task orchestration, many current systems rely on rigid task workflows and linear command models,
lacking operator-friendly mechanisms to support asynchronous multitask scheduling or semantic task specification.
Moreover, the operator’s role in swarm control remains undertheorized and poorly modeled in existing systems. Many interfaces treat
the human merely as a command initiator or a passive supervisor rather
than a cognitive agent at the center of the decision-making loop. This
mischaracterization manifests in two major forms of overcompensation:
1. Over-reliance on automation: Some systems prioritize high degrees
of autonomy, reducing the operator’s involvement in goal-setting
and strategy formulation. Once a task is issued, the swarm executes it
with minimal human oversight, limiting transparency and eliminating meaningful points of intervention. As a result, operators struggle to predict swarm behavior or adaptively respond to unexpected
events, undermining system resilience.
2. Overexposure to low-level details: To improve transparency and interaction flexibility, other systems expose a large number of control
parameters and operational options. However, without appropriate
abstraction and layered control design, this overload of information
increases the operator’s cognitive effort across perception, reasoning, and decision-making phases, thereby reducing both task efficiency and execution consistency.
These challenges prompted us to reexamine the core demands of HSI
systems. Beyond improving functional integration and interaction efficiency, future systems must establish a cognitively supportive coordination mechanism grounded in the triadic relationship among the human,
the task, and the swarm.
Motivated by this insight, and informed by both practical development experience and theoretical reflection on existing work, this study
proposes a human-centered HSI framework. This framework centers on
the cognitive role of the operator in guiding swarm behavior and aims
to offer a theoretically grounded and practically implementable design
paradigm for next-generation HSI systems.
4. Human-centered human–swarm interaction framework
4.1. Leveraging the OODA model to guide cognition in human–swarm
interaction
To better understand the dynamic and complex interaction relationship between human operators and UAV swarms and to enhance the
adaptability and controllability of HSI systems from a human-centered
perspective, we adopt the classical OODA loop model [83,84] as a theoretical lens for modeling the operator’s cognitive and behavioral logic
throughout the interaction process.
Originally proposed by U.S. Air Force Colonel John Boyd, the OODA
model was developed to explain mechanisms of rapid decision-making
and tactical advantage in air combat scenarios. It has since been widely
applied in cognitive science, decision theory, and complex adaptive systems. The model emphasizes how individuals operating in dynamic and
high-uncertainty environments iteratively complete a decision-making
loop through continuous observation, orientation, decision, and action.
In the context of HSI, the efficiency of the OODA loop directly depends on the operator’s responsiveness and cognitive dominance in managing complex swarm tasks. Accelerating the OODA loop not only improves the speed of information processing and decision-making but
also reflects the system’s ability to establish an efficient perception–
comprehension–execution pipeline. Such a pipeline supports the operator in maintaining control and strategic leadership during high-intensity
mission scenarios.
Specifically, during the control of UAV swarms, the operator is constantly enacting a self-driven OODA loop: acquiring swarm and environmental status through the human–machine interface (Observe), analyzing and interpreting this information (Orient), formulating task strategies (Decide), and issuing commands via the interaction system (Act).
Therefore, the key to designing an effective HSI system lies in strengthening the responsiveness of each stage of the OODA loop, enabling its
seamless and high-frequency execution. This continuous cycle helps operators retain cognitive and strategic superiority throughout the course
of complex and adversarial missions.
4.2. OODA-oriented human–swarm interaction framework
Fig. 2 illustrates the proposed human-centered, OODA-oriented HSI
framework, designed to support efficient and continuous execution of
the operator’s OODA loop during UAV swarm control. The framework
is organized into four conceptual layers: the UAV Swarm layer, the
3

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

Z. Zhou, P. Wei, Z. Wang et al. Design and Artificial Intelligence 1 (2025) 100029
Fig. 2. Human-centered, observe–orient–decide–act (OODA)-oriented human–swarm interaction framework.
Human–Swarm Interface layer, the Methods & Principles layer, and the
Human’s OODA Loop layer.
Within the architecture of the Human–Swarm Interface layer, we
define five sequential information-processing layers that collectively abstract the end-to-end flow of information from raw swarm data input to
executable task command output. These five layers represent not merely
a static functional stack, but rather dynamic intermediaries that interact
closely with each phase of the operator’s OODA loop. The efficiency and
quality of each OODA phase are directly influenced by the design and
responsiveness of these layers. The five layers are as follows.
Situation Data Acquisition Layer. As the entry point of the system,
this layer is responsible for collecting real-time, multi-source data from
both the UAV swarm and the surrounding environment. Data sources
include individual flight status, onboard sensor readings, object recognition outputs, etc. Through a synchronized aggregation, these heterogeneous raw data form the perceptual foundation required for the Observe phase of the OODA loop. The completeness and timeliness of this
layer critically determine the boundary conditions for subsequent understanding and intention formulation.
Situation Visualization Layer. This layer is responsible for the structured processing and visual representation of raw data. By employing
cognitively supportive visualization techniques, such as layered overlays, heatmap zoning, semantic annotations, and alert popups, it generates multidimensional situational maps. These visualizations allow the
operator to quickly identify critical areas, monitor swarm states, and
detect potential threats within complex environments. The core function of this layer is to facilitate the transition from Observe to Orient
by enabling the operator to construct semantic and hierarchical mental
models of the operational context.
Task Intent Expression Layer. Serving as a bridge between environmental understanding and task generation, this layer provides structured mechanisms for expressing operator intent. Once situational understanding is achieved, the operator translates tactical goals into explicit task intentions. These high-level semantic task intentions are
mapped into structured task parameters via configurable mechanisms
such as parameterized task templates. This layer facilitates the transition from Orient to Decide and delivers precise inputs to the subsequent
planning module.
Task Planning Layer. Targeting swarm-level task execution, this
layer decomposes the parameterized task intentions and performs path
planning through manual input or automated planning algorithms. It
generates swarm-compatible action strategies based on current system
status and mission objectives. Outputs include flight trajectories, target assignments, sensor deployment plans, and payload resource allocations. This layer bridges the Decide and Act phases by converting
abstract task intentions into actionable plans, ensuring the operator’s
strategic goals are both operationally feasible and system-executable.
Execution and Control Layer. This final layer translates the planned
strategies into low-level hardware-executable commands for individual
UAVs, such as flight instructions, waypoint sequences, and payload release signals. The system also provides real-time feedback on task execution and supports exception handling. As the embodiment of the Act
phase in the OODA loop, this layer ensures that strategic intent is effectively executed and that interactive control remains closed-loop and
adaptive.
4.3. Design principles for accelerating the OODA loop
In HSI system design, it is not sufficient for the system to simply
meet task execution requirements. It must also establish a cognitively
efficient and interaction-effective channel for human–swarm collaboration. While we draw on established best practices in complex system interface design (e.g., layered situation displays, adaptive automation, adjustable levels of autonomy), our method lies in adapting and extending
them to the swarm context: We synthesize these practices with swarmspecific constraints (e.g., multi-agent coordination, heterogeneity, relational coupling) and operationalize them into six HSI-adapted design
principles grounded in the OODA loop. Unlike interfaces designed for
single-system control, our principles explicitly focus on the unique demands of UAV swarms, such as collective perception, distributed task
orchestration, and dynamic granularity of control.
4

---
**[Page 5]**
*(This page contains a figure/chart/image not captured in text)*

Z. Zhou, P. Wei, Z. Wang et al. Design and Artificial Intelligence 1 (2025) 100029
Fig. 3. Overview of the components in the human–UAV swarm interaction system.
The six HSI-adapted design principles illustrated in Fig. 2 serve as the
foundational methodological components of our proposed HSI framework. These principles address core elements such as information organization, intent expression, cognitive support, and control strategy.
Collectively, they can promote a tight coupling between the interface
architecture and the stages of the OODA loop, ultimately accelerating
the loop’s iteration efficiency. The principles are as follows.
Human-Centric Control Loop. While modern swarm systems have
achieved a degree of autonomous behavior, the interface design must
remain anchored in the operator’s cognitive process. Throughout all
phases of the OODA loop, the human should maintain a leading role
in perception, judgment, and strategic decision-making. Rather than
aiming to replace human decision-making, interaction design should
facilitate an assistive control loop that centers on human intent. Autonomy should remain embedded within a clearly defined, humandominant logic loop, thereby establishing an interpretable and controllable human–swarm cognitive collaboration model.
Aggregated & Layered Swarm Perception. Given the scale, heterogeneity, and relational dynamics of swarm information, the interface must support multi-layered situational representations, from
swarm-wide overviews and sub-team roles to inter-UAV communication/topology graphs, and down to individual vehicle states. This design supports operators to flexibly navigate between macro-level swarm
coordination and micro-level UAV diagnostics without losing contextual
continuity. By constructing abstraction layers that surface collective patterns, emergent anomalies, and heterogeneity-sensitive saliencies, the
system directs operator attention toward critical swarm dynamics and
abnormal group behaviors, thereby improving the efficiency of the Observe and Orient stages and reducing cognitive dispersion across largescale UAV collectives.
Task-Oriented Intent Abstraction. To reduce cognitive and operational load in complex mission scenarios, the interface should offer
structured and semantically driven mechanisms for intent expression.
Through modular, high-level interaction components, such as parameterized task templates, operators can focus on articulating mission goals
without being burdened by low-level configuration. This principle supports a shift from low-level operations to high-level semantic construction during the Orient and Decide phases, forming an abstract, goaldirected decision structure that improves the efficiency and scalability
of intent expression.
Task Transparency & Predictive Support. Operator trust and decision quality depend heavily on understanding and anticipating swarm
behavior. The interface should visualize the logical structure of tasks
and provide predictive cues about swarm behavior evolution, enabling
operators to simulate key states and potential transitions during task
execution. This “explainable–predictable–traceable” information model
strengthens shared understanding between human and swarm, enhances
task transparency, and improves confidence and foresight during the
Orient and Decide phases.
Multi-Task Orchestration & Asynchronous Execution. Swarm-based
multi-task operations often involve conflicts in priorities, resource contention, and timing dependencies. The interface should support structural modeling of task relationships, allowing operators to visually
and procedurally orchestrate task flows, including dependencies, triggers, priority rules, etc. Based on this, tasks should be executed asynchronously and autonomously as conditions are met, without requiring
constant human intervention. This principle allows operators to focus
on global strategy during the Decide phase while delegating execution
management to the system during the Act phase, reducing real-time operational load and enhancing system responsiveness and robustness.
Adaptive Control Granularity. In dynamic environments, different
tasks and contingencies demand varying levels of control. The interface should enable operators to flexibly transition across three levels of
control: macroscopic (directing the entire swarm), mesoscopic (coordinating specific task groups), and microscopic (intervening at the level of
an individual drone). This adaptive mechanism ensures that while overall automation is maintained, human intervention remains available for
critical junctures. It supports multi-level responsiveness in the Act phase,
enabling operators to intervene based on task urgency, environmental
complexity, or individual UAV performance, thereby preserving adaptability and responsiveness.
These principles are designed to strengthen the alignment between
HSI interface functions and the OODA loop, driving the evolution of
human–swarm systems toward greater efficiency, flexibility, and interpretability. Together, they aim to establish a theoretical foundation for
achieving genuinely human-centered HSI.
5. Human–swarm interaction system design
5.1. System overview
Based on the proposed interaction framework and design principles,
we developed a human–UAV swarm interaction system that enables a
single operator to flexibly and efficiently manage UAV swarms. The system implements core functionalities, including situational visualization,
swarm status monitoring, task planning, etc. As shown in Fig. 3, the
system architecture comprises the following major modules: Situation
Display, Swarm Monitor, Information Pusher, Task Scheduler, Video
Surveillance, Payload Controller, and Configuration Panel.
Situation Display. This module presents swarm-related information
through a graphical interface by loading 2D or 3D map data. It provides
intuitive visualizations of UAV positions, flight trajectories, mission ar5

---
**[Page 6]**

Z. Zhou, P. Wei, Z. Wang et al. Design and Artificial Intelligence 1 (2025) 100029
eas, no-fly zones, target locations, aerial imagery, etc., thereby making
critical situational information explicitly accessible. It also supports realtime preview and validation of mission planning outputs, such as target
assignments and preplanned routes. An integrated mission evaluation
tool enables operators to perform rapid in-map assessments—such as
target confirmation—creating a feedback loop within the mission execution cycle.
Swarm Monitor. This module displays structured data at both the
swarm and individual UAV levels. At the swarm level, it shows formation structure, communication topology, task phases, progress status,
etc. At the individual level, it presents detailed state data, including position, orientation, velocity, battery level, payload status, etc.
Information Pusher. Designed to assist in dynamic task execution,
this module provides real-time notifications of critical events, such as
communication dropouts, GPS failures, or battery warnings. It also delivers target-related information, including object type, coordinates,
recognition confidence, and source. A rule-based filtering mechanism
ensures that operators are alerted only to the most relevant and urgent
information, thereby reducing cognitive load during high-intensity missions.
Task Scheduler. This module includes a set of parameterized task
templates and a planning algorithm library. Templates cover a range of
task types, such as rendezvous, patrol, and return-to-base. Each template
is associated with semantic and coordinate parameters, which are automatically matched with backend algorithms. Operators can compose
complex mission sequences by combining templates, enabling high-level
abstraction and flexible task flow definition.
Video Surveillance. The system supports real-time display of visible
and infrared video streams, with up to two concurrent feeds. Operators
can switch video sources by clicking UAV or target IDs and interact
directly with the video interface to select, confirm, and track targets.
Payload Controller. This module provides fine-grained control of onboard payloads, including power switching, pod adjustment, and payload release operations.
Configuration Panel. This includes configuration options for navigation, joystick input, simulation, safety protocols, and interface preferences. Key safety features are centralized here, such as return-to-home
timeout after link loss, battery threshold alerts, geofencing parameters,
and no-fly zone definitions.
5.2. Interaction workflow design
The system establishes a full-cycle interaction workflow that supports UAV swarm operation across key stages, including situational
awareness, task planning, execution, and feedback-based adaptation.
This workflow is designed to maintain a continuous channel for operator intent expression and transparent system responsiveness, ensuring
that the human remains perceptually and cognitively in control throughout all phases of the mission. By integrating visual information display,
structured task construction, and multi-level control mechanisms, the
system provides a stable, efficient, and controllable interaction path,
supporting a human-centered cognitive loop and enhancing the overall
coordination efficiency of swarm task execution.
The interaction begins with the operator launching the system and
accessing the Configuration Panel to perform personalized settings such
as layout customization and joystick calibration. Basic safety parameters are also configured at this stage, including minimum flight altitude,
return-to-home timeouts for communication loss, battery thresholds,
camera settings, geofencing, and no-fly zones. These settings ensure that
subsequent operations remain within defined safety boundaries.
Once configured, the operator checks the UAV swarm status using
the Swarm Monitor module, confirming system stability in terms of GPS
positioning, altitude, attitude, and other key indicators. With the system
operationally ready, the operator uses the Situation Display module to
analyze the geographical context of the mission area, assess potential
target distributions, and interpret environmental factors, forming a preliminary task intent.
This intent is translated into concrete mission plans via the Task
Scheduler module. Through a graphical interface, the operator selects
and configures parameterized task templates—for example, rendezvous
or patrol missions—using map-based inputs to define parameters such
as altitude and area coverage. Real-time visualization of planned routes
is supported to help validate mission design. The system offers three
modes of task dispatch: full-sequence execution, stepwise task delivery,
and manual joystick-based control. This multi-modal execution design
provides flexibility for routine operations as well as real-time responses
to unforeseen conditions.
During task execution, the operator monitors mission progress via
the Situation Display and Video Surveillance modules while simultaneously receiving real-time updates from the Swarm Monitor and Information Pusher modules. These updates include performance metrics, anomaly alerts (e.g., GPS signal loss, battery warnings), and target recognition data, enabling comprehensive situational tracking and
operational control.
Upon identifying targets during the mission, the operator can initiate tracking directly from the Video Surveillance or issue corresponding
commands through the Payload Controller module. In scenarios involving multiple targets, the operator can invoke the system’s automated
task planner to optimize UAV–target assignments and rapidly dispatch
appropriate commands. The system also supports real-time adaptation
by allowing the operator to interrupt and reconfigure ongoing tasks,
thereby enabling on-the-fly strategy shifts in response to environmental
dynamics. Upon mission completion, the operator may review the results through visual playback of key flight paths and captured imagery
within the Situation Display module, providing support for post-mission
evaluation and future decision-making.
5.3. User interface design
The system is deployed on a portable GCS equipped with dual touchscreen displays. It supports multiple input modalities, including touch,
physical buttons, and joysticks, allowing it to accommodate diverse operational needs and mission environments. The user interface is divided
into two main views: the mission interface (Fig. 4) and the video interface (Fig. 5), displayed on separate screens to enable parallel management of mission planning and video surveillance. This design enhances
operational fluency and task responsiveness.
The mission interface centers around a map panel, which provides
an integrated display of key spatial information such as UAV swarm positions, flight trajectories, mission zones, and target locations. The upper
sidebar aggregates swarm-level status and alert information, while the
lower bar presents individual UAV state data (e.g., battery level, velocity, orientation). A collapsible design allows these panels to expand on
demand, reducing visual clutter. The left and right sidebars integrate
controls for task management, payload operation, target information,
and system settings. This layout ensures clear structuring of information types and control functions, allowing operators to efficiently access
relevant tools across different stages of a mission.
The task control panel offers a graphical interface for mission sequence planning. Operators can flexibly invoke preconfigured task templates—such as takeoff, rendezvous, or patrol—and define task parameters either through interactive map input or dedicated parameter panels.
This facilitates rapid construction, modification, and execution of mission structures and plans.
Overall, the interface design emphasizes hierarchical information organization and focused attention management. It retains a strong sense
of global situational awareness while enabling rapid access to critical
targets and localized status data. This layered and task-centered design
helps mitigate information overload and cognitive burden during complex swarm operations, ultimately improving operator control and responsiveness.
6

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

Z. Zhou, P. Wei, Z. Wang et al. Design and Artificial Intelligence 1 (2025) 100029
Fig. 4. Mission interface with map panel displaying swarm data and sidebars for target states, control functions, and other features.
Fig. 5. Video interface with panels for UAV video streams, alongside online UAV list, target list, and target-specific control commands.
5.4. Task intent expression mechanism
To enable efficient and low-cognitive-load swarm task deployment,
the system introduces a parameterized task template mechanism that
integrates both general-purpose and domain-specific templates. These
templates serve as structured configuration units for standardized expression and rapid generation of UAV swarm tasks, encapsulating
task intent in a semantic and parameterized format. Specifically, the
general-purpose templates are designed for fundamental swarm operations across diverse scenarios, such as takeoff, rendezvous, and formation control, emphasizing semantic standardization and high reusability. In contrast, the domain-specific templates are tailored to particular
operational contexts, including static/dynamic target reconnaissance,
3D structure search, and aerial patrol, thereby enhancing the system’s
adaptability and task diversity.
All templates are deeply integrated with the system’s backend task
planning algorithm library. Operators interact only with the high-level
semantic interface, entering relevant task parameters, while the system
7

---
**[Page 8]**

Z. Zhou, P. Wei, Z. Wang et al. Design and Artificial Intelligence 1 (2025) 100029
Table 1
Basic information of participants in the user study.
Participant ID Age Gender Professional background UAV operation experience
P1 25 Female Electrical engineering Expert
P2 27 Male Mechanical design Expert
P3 23 Male Industrial design Beginner
P4 28 Male Design studies Beginner
P5 29 Female Medical physics Novice
P6 27 Male Human–computer interaction Expert
P7 24 Male Command and control Expert
P8 29 Female Human–computer interaction Novice
P9 36 Male Digital art and design Novice
P10 28 Male Computer science and technology Beginner
automatically handles downstream processes such as task assignment,
path planning, and command preparation. This template-based design
standardizes mission definition, modularizes task reuse, and supports
flexible parameterization, significantly reducing the operator’s cognitive
load and operational complexity.
Building on this, the system incorporates a task sequence construction mechanism that enables operators to flexibly compose hierarchical
and logic-driven task flows using multiple task templates. This mechanism supports both the holistic representation of full mission workflows
and the parallel scheduling of sub-swarm units, as well as asynchronous
task dispatch. Operators can assign separate task sequences to different
subgroups or individual UAVs. Based on defined task conditions, each
UAV autonomously transitions through mission phases without requiring continuous operator intervention. This greatly improves the flexibility, scalability, and control efficiency of multi-UAV swarm operations.
6. User study
To systematically evaluate the effectiveness and adaptability of the
proposed human–UAV swarm interaction system in terms of usability
and interaction performance, we conducted a comprehensive user study
combining both quantitative evaluation and qualitative analysis.
6.1. Experimental setup
The experiment was conducted in an indoor simulated environment.
A virtual swarm of UAVs and predefined mission targets were configured
in the system backend. No actual UAV hardware was used during the
study.
Participants’ information. Participants were recruited via university
mailing lists and professional forums in UAV research, HCI, and design.
Eligibility required adults aged 20–40 with UAV-related experience or
relevant training in engineering, design, or human factors, except that
several novices with no prior experience were also deliberately included
to broaden diversity and assess system performance across different skill
levels. A total of 10 participants took part in the study (see Table 1),
representing a range of professional backgrounds and varying levels of
UAV operation experience. Based on their prior experience, participants
were categorized into three skill levels:
• Novice: No prior hands-on experience with any type of UAV.
• Beginner: Some experience in flying first-person view (FPV) or aerial
photography drones.
• Expert: Proficient in planning and executing missions using GCS or
graphical interfaces, either for single or multiple UAVs.
Pre-experimental training. Before the experiment, all participants
underwent a standardized 30-minute pre-experimental familiarization
session comprising (i) a tutorial on interface layout and core functions,
(ii) a guided demonstration of swarm task allocation and monitoring,
and (iii) a short exploratory practice. This ensured a comparable baseline understanding of the system while preserving differences in realworld expertise.
Experimental task and procedure. Each participant served as the
sole operator in an open-ended simulated military scenario (Fig. 6) using a virtual UAV swarm. The mission involved commanding 20 micro
reconnaissance–strike UAVs in Area D to: (i) reconnoitre suspected enemy groupings in Areas A and B (potentially including infantry, light
vehicles, and heavy armored vehicles), (ii) conduct pre-emptive strikes
on identified targets, and (iii) secure road infrastructure in Area C to
prevent enemy sabotage. This experiment focused on the system usability test rather than strict performance benchmarking; therefore, no fixed
execution criteria were imposed. Because both UAVs and targets were
simulated, after each command, the experimenter described the systemgenerated UAV behaviors to ensure that the participants correctly understood the outcomes of their inputs. Participants would evaluate situational data, plan tasks, issue swarm commands via the interface, and
subsequently complete a usability questionnaire followed by a semistructured interview.
6.2. Quantitative evaluation and analysis
To assess the overall usability of the system, we conducted a system
usability scale (SUS) [85] questionnaire with all 10 participants. The
final SUS score was 72.75, which corresponds to a B− grade, placing
the system above approximately 65%–69% of products. This indicates
that the system delivers acceptable usability performance, providing a
moderately positive user experience. The Fig. 7 presents the detailed
scores for each questionnaire item.
In terms of usability, 90% of participants agreed with Q3 (“I thought
the system was easy to use”) and Q9 (“I felt very confident using the
system”), while Q7 (“I think most people would learn to use this system
very quickly”) received 100% positive feedback. These results highlight
the system’s strengths in intuitive operation, confidence building, and
general user adaptability. Regarding learnability, Q4 (“I needed to learn
a lot of things before I could get going with this system”) received agreement from 60% of participants, suggesting that there is still a moderate learning curve when users first encounter the system. However, Q5
(“The functions of the system were well integrated”) and Q10 (“I needed
the support of a technical person to use this system”) received 80% and
70% positive responses, respectively, indicating that most users were
able to effectively understand and operate the system after a short acclimation period. In terms of overall acceptability, Q1, Q6, and Q9 all
received more than 80% positive feedback, suggesting a generally high
level of user approval and system acceptance.
In summary, the SUS results indicate that the proposed system
demonstrates generally good usability, reasonable learnability, and a
fair level of user acceptability. However, there is still room for improvement in reducing the initial learning barrier, particularly for novice
users.
6.3. Qualitative analysis
To gain deeper insight into users’ subjective experience with the system, we conducted semi-structured interviews with 10 participants from
8

---
**[Page 9]**
*(This page contains a figure/chart/image not captured in text)*

Z. Zhou, P. Wei, Z. Wang et al. Design and Artificial Intelligence 1 (2025) 100029
Fig. 6. Mission scenario and area settings.
Fig. 7. Detailed system usability scale (SUS) evaluation results.
diverse professional backgrounds and with varying levels of UAV operation experience. The interviews covered participants’ opinions on the
interface, interaction flow, task planning, and various other elements
influencing the interaction experience.
Interaction logic and usability. Most participants considered the
overall workflow intuitive and task-oriented. Expert participant P1 remarked, “Compared with typical UAV control software like QGroundControl1, which focuses heavily on low-level functions, this system is
more task-oriented, with a clean interface and low learning curve.” P2
echoed this view, adding, “The task-centric design effectively hides the
complexity of low-level control, allowing operators to focus on highlevel planning and command.” Beginner P3 commented, “The task templates are very user-friendly—mission planning feels efficient and is
great for beginners.” Expert P6 summarized the logic as “clear and con1 https://qgroundcontrol.com/
cise—core interactions can be broken down into three basic steps: selecting targets, assigning tasks, and issuing commands.” Even novice
participants without prior UAV experience (P5, P9) acknowledged that
the system helped lower the learning barrier and facilitated a smoother
onboarding process.
Flexibility in task expression. Despite the generally positive reception, several participants emphasized limited flexibility in expressing
certain complex or asymmetric mission intents. Expert P2 pointed out,
“For complex or emergency missions, the current approach—relying on
predefined templates and task sequences—can lack flexibility and responsiveness. It would help if frequently used functions like emergency
return or takeoff/landing were integrated directly into the map interface to reduce interaction steps.” The command and control expert (P7)
also noted, “Parameterized task templates help reduce cognitive load,
but their flexibility is constrained by specific mission types. The system
would benefit from a more comprehensive template library.” P5 added,
“When multiple UAVs fly near buildings, some need to detour or rise for
9

---
**[Page 10]**

Z. Zhou, P. Wei, Z. Wang et al. Design and Artificial Intelligence 1 (2025) 100029
reconnaissance, but current templates don’t support this kind of differentiated control.” This highlights a limitation in the system’s ability to
express nuanced or asymmetric task intentions. Additionally, beginner
P4 (from a design background) noted that “some task templates appear
to overlap or nest within each other, which can cause confusion. Each
template could be restructured as a distinct ‘meta-task’ unit to improve
clarity.”
Cognitive load, guidance, and novel interactions. Several novice
participants (P5, P8, P9) observed that while the interaction flow was
generally clear, the multi-step process, including template selection, task
sequence construction, and parameter configuration, still imposed a significant cognitive load. As P5 put it, “You need to mentally structure the
entire mission logic beforehand, which can still be quite demanding.”
P8 suggested, “Could the system use AI to recommend the next step after
a task is executed?”, indicating a desire for intelligent guidance mechanisms during interaction. P9 proposed adding voice or AR-based input
for setting flight altitudes, showing user interest in novel interaction
modalities.
Information push and batch processing mechanisms. Participants
from different experience levels (P2, P6, P8, P9) noted that as task complexity and alerts increase, the logic for information delivery could become overwhelming. P8 stated, “The system should be able to suggest
the next steps automatically—even if manual confirmation is needed,
there should be a one-click way to process all alerts and target updates.”
P5 added, “If the video interface supported batch processing of identified targets, it would greatly improve efficiency.” P2 and P9 both recommended organizing alerts by priority and relevance to help users focus
on the most critical information.
Swarm behavior predictability. Participants P4, P6, P7, P9, and P10
all appreciated the route visualization functionality. P4 said, “The preview of planned paths is very clear and helps me understand the sequence of mission steps.” P7 similarly noted, “Every mission step has an
explicit flight path, which improves predictability and understanding of
swarm behavior.”
User interface design. Although the interaction flow was generally
considered clear, multiple expert participants pointed out areas for user
interface improvement. P6 mentioned, “Interaction can still feel cumbersome on touchscreen hardware—the match between interaction methods and physical input devices needs enhancement.” Several participants (P3, P4, P9, P10) also noted inefficiencies in UAV selection. P3
and P10 commented, “There’s no way to group-select UAVs—you have
to click one by one.” P4 and P9 recommended, “Support box selection
or one-click selection of all UAVs involved in different tasks to improve
efficiency,” a need that becomes more acute in large-scale swarm operations. Additionally, P2, P3, and P9 expressed a desire for real-time UAV
status (e.g., idle, active) to be shown directly in the UAV list, to reduce
cognitive effort. P7 highlighted another pain point: “Currently, task templates can’t be reordered directly in the task sequence panel—you have
to switch interfaces to make adjustments.” P9 suggested that “Once the
task area is selected, the system should immediately show the planned
route without requiring an extra confirmation click.”
Scalability and real-world applicability. Expert users also raised
considerations regarding system scalability and applicability to professional scenarios. P2 noted that the system had not yet accounted for the
full complexity of heterogeneous swarm configurations. P6 remarked
that “this evaluation is based on simulated data, which differs significantly from real-world operations in outdoor environments.” P7 further
commented, “The system currently lacks formation awareness within
the swarm, meaning operators must manually avoid potential path conflicts.”
6.4. Experimental conclusion
In summary, analysis of both the SUS responses and semi-structured
interview feedback from 10 participants provides preliminary validation
of the proposed interaction framework and design principles. Participants generally agreed that the system was “simple in logic” and “easy
to understand.” The task-centered interaction paradigm effectively lowered the operational barrier and showed promising results in swarm path
visualization and structured task planning, indicating a certain degree
of practical value and application potential.
Nevertheless, the study also reveals a clear gap between interaction
design concepts and their actual implementation. While the framework
offers well-defined guidance for system development, translating these
high-level cognitive and interaction principles into concrete, functional
system components remains a challenge. This transformation gap, especially evident in areas like task flexibility and interface responsiveness, reflects the complexity of operationalizing human-centered design in real-world swarm control contexts. Addressing this gap will require further iterative refinement and engineering validation in future
work.
7. Discussion
7.1. Theoretical and methodological reflections
The study provides preliminary support for applying six HSI-adapted
design principles grounded in the OODA loop to human-centered HSI.
The Aggregated & Layered Swarm Perception principle enhanced situational visibility and supported the Observe–Orient transition, as reflected in users’ appreciation of swarm status aggregation and flying
route previews. Task templates lowered entry barriers and supported
effective high-level planning, but their limited expressiveness exposed
constraintsin representing asymmetric or emergent mission intents. This
suggests that the Task-Oriented Intent Abstraction principle requires
further refinement, particularly introducing scalable template mechanism and map-placed emergency panels. Task Transparency & Predictive Support was consistently valued, yet participants requested clearer
post-action explanations, highlighting the need to strengthen task transparency across OODA phases. Efficiency issues in UAV selection, state
monitoring, and task reordering reveal gaps in implementing MultiTask Orchestration & Asynchronous Execution and Adaptive Control
Granularity principle, which remain critical for seamless Decide–Act cycles. Importantly, the Human-Centric Control Loop principle was also
validated: While decision authority should remain with the operator,
lightweight intelligent aids such as next-step recommendations or automated prioritization can accelerate judgment without undermining human dominance in the loop. Overall, the framework proved conceptually
robust, but its practical validation depends on how effectively interface
primitives can mediate transitions between cognitive phases rather than
isolated functions.
7.2. Study limitations
Several limitations constrain the interpretation of the findings. The
size of participants in the experiment was limited and, although diverse in expertise, does not fully capture the breadth of operator populations or team-based scenarios. The study was conducted indoors using simulated UAVs and mission targets, meaning that environmental uncertainty, communication latency, and real hardware constraints
were not represented. The evaluation emphasized usability and subjective cognition rather than strict performance benchmarking, limiting
claims about operational effectiveness. Furthermore, while the design
principles provide comprehensive theoretical guidance, their translation into deployable features remains incomplete. User feedback consistently identified missing functions—richer task-expression flexibility,
intelligent guidance, priority-based alerting and batch processing, efficient UAV grouping, and formation awareness—that are essential for
realizing the full potential of human-centered swarm control. These issues reflect a broader transformation gap between principle-level design
and engineering implementation.
10

---
**[Page 11]**

Z. Zhou, P. Wei, Z. Wang et al. Design and Artificial Intelligence 1 (2025) 100029
7.3. Future work
Theoretically, the current framework primarily aligns the four discrete stages of the OODA loop with HSI. Future work should move
beyond this stage-to-stage correspondence, viewing OODA as a finergrained, iterative process with multiple feedback pathways. Such an
extension would enable a closer coupling between decision-making cycles and interaction processes, offering a stronger theoretical basis for
modeling human–swarm collaboration in dynamic environments. In
experimentation, future work should involve outdoor trials with real
UAV hardware, heterogeneous swarms, and formation-aware behaviors to ensure ecological validity, complemented by metrics explicitly
aligned with OODA transitions and cognitive demands, such as time-totransition, recovery efficiency, and operator workload. In system development, engineering priorities include modular template libraries, mapplaced emergency panel, mixed-initiative guidance with explainable
recommendations, voice/AR input for parameter specification, prioritybased alert management, batch target operations, group selection, and
in-panel task-sequence reordering. These features are expected to enhance task-expression flexibility, reduce interaction overhead, and enable high-frequency OODA cycles without undermining human primacy.
Beyond these targeted directions, the study highlights a broader transformation gap between interaction design concepts and their real-world
implementation. While the framework offers clear cognitive and design
principles, translating them into robust, functional components proved
challenging, especially in domains such as task flexibility and interface
responsiveness. Closing this gap will require iterative refinement, longitudinal testing in operational environments, and systematic engineering validation to ensure that human-centered design principles can scale
into deployable swarm systems.
8. Conclusion
This study aims to address key challenges in HSI, particularly the
high cognitive workload and low operational efficiency experienced by
operators in “one-to-many” UAV swarm control scenarios. We propose
a human-centered interaction framework oriented by the OODA cognitive model, integrated with six HSI-adapted design principles. Grounded
in real-world system development experience, the framework was instantiated into an HSI prototype system, with detailed implementations
across task intent expression, interface layout, and interaction workflow
design.
Through a comprehensive user study in an indoor simulated environment, the system demonstrated preliminary potential in supporting cognitive processing and improving operational efficiency. The user
study provided initial validation of the framework’s applicability and
the guiding value of its design principles. At the same time, the evaluation revealed limitations in interface presentation and interaction details, suggesting that future work should further enhance engineering
implementations. This would help align the system more closely with
operator cognition and improve usability in complex mission scenarios,
ultimately enabling more effective human–swarm collaboration.
Declaration of competing interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence
the work reported in this paper. This research was conducted independently and is not influenced by the company’s interests.
CRediT authorship contribution statement
Zihong Zhou: Writing – original draft, Software, Methodology,
Conceptualization. Pengjin Wei: Writing – original draft, Methodology. Zhiyi Wang: Validation, Software, Project administration. Leyi
Duan: Software, Investigation. Siyuan Hai: Validation, Software.
Zuhang Zhang: Validation, Software. Yujie Sun: Project administration. Fuyong Feng: Supervision, Funding acquisition.
Funding
This research was supported by the self-funded project from the
China North Artificial Intelligence & Innovation Research Institute
(Project No. QT04Q24038).
Ethics and compliance statement
All user studies reported in this paper were conducted in accordance
with institutional ethical guidelines. Participation was entirely voluntary, and all participants provided written informed consent prior to the
study. Participants were informed of the study’s purpose, procedures,
and their right to withdraw at any time without penalty. No personally identifiable or sensitive data were collected, and all responses were
anonymized for analysis.
References
[1] A.J. Hepworth, D.P. Baxter, A. Hussein, et al., Human-swarm-teaming transparency
and trust architecture, IEEE/CAA J. Autom. Sin. 8 (7) (2021) 1281–1295, doi:10.
1109/JAS.2020.1003545.
[2] A. Hussein, H. Abbass, Mixed initiative systems for human-swarm interaction: opportunities and challenges, in: Proceedings of the 2018 2nd Annual Systems Modelling
Conference (SMC), IEEE, 2018, pp. 1–8, doi:10.1109/SYSMC.2018.8509744.
[3] A. Hussein, L. Ghignone, T. Nguyen, et al., Characterization of indicators for adaptive human-swarm teaming, Front. Robot. AI 9 (2022) 9745958, doi:10.3389/frobt.
2022.745958.
[4] A. Kolling, P. Walker, N. Chakraborty, et al., Human interaction with robot swarms:
a survey, IEEE Trans. Hum. Mach. Syst. 46 (1) (2016) 9–26, doi:10.1109/THMS.
2015.2480801.
[5] J.B. Lyons, A. Capiola, J.A. Adams, et al., Examining the human-centred challenges
of human–swarm interaction, Phil. Trans. R. Soc. A. 383 (2289) (2025) 20240140,
doi:10.1098/rsta.2024.0140.
[6] W.D. Nothwang, M.J. McCourt, R.M. Robinson, et al., The human should be part of
the control loop? in: Proceedings of the 2016 Resilience Week (RWS), IEEE, 2016,
pp. 214–220, doi:10.1109/rweek.2016.7573336.
[7] X. Dong, Y. Li, C. Lu, et al., Time-varying Formation tracking for UAV swarm systems
with switching directed topologies, IEEE Trans. Neural Netw. Learn. Syst. 30 (12)
(2019) 3674–3685, doi:10.1109/TNNLS.2018.2873063.
[8] X. Fu, J. Pan, H. Wang, et al., A formation maintenance and reconstruction method of
UAV swarm based on distributed control, Aerosp. Sci. Technol. 104 (2020) 105981,
doi:10.1016/j.ast.2020.105981.
[9] J. Hou, X. Zhou, N. Pan, et al., Primitive-swarm: an ultra-lightweight and scalable
planner for large-scale aerial swarms, IEEE Trans. Robot. 41 (2025) 3629–3648,
doi:10.1109/TRO.2025.3573667.
[10] X. Zhou, X. Wen, Z. Wang, et al., Swarm of micro flying robots in the wild, Sci.
Robot. 7 (66) (2022) eabm5954, doi:10.1126/scirobotics.abm5954.
[11] X. Zhou, J. Zhu, H. Zhou, et al., EGO-swarm: a fully autonomous and decentralized
quadrotor swarm system in cluttered environments, in: Proceedings of the 2021 IEEE
International Conference on Robotics and Automation (ICRA), IEEE, 2021, pp. 4101–
4107, doi:10.1109/icra48506.2021.9561902.
[12] C. Hu, G. Qu, Y. Zhang, Pigeon-inspired fuzzy multi-objective task allocation of unmanned aerial vehicles for multi-target tracking, Appl. Soft Comput. 126 (2022)
109310, doi:10.1016/j.asoc.2022.109310.
[13] Y. Wang, J. Jiao, J. Liu, et al., A labor division artificial bee colony algorithm based
on behavioral development, Inf. Sci. 606 (2022) 152–172, doi:10.1016/j.ins.2022.
05.065.
[14] B. Wu, R. Xiao, Evolutionary attraction–repulsion algorithm embedded with LLM for
UAV task allocation, Adv. Eng. Inform. 66 (2025) 103428, doi:10.1016/j.aei.2025.
103428.
[15] T. Yang, P. Feng, Q. Guo, et al., AutoHMA-LLM: efficient task coordination and
execution in heterogeneous multi-agent systems using hybrid large language models,
IEEE Trans. Cogn. Commun. Netw. 11 (2) (2025) 987–998, doi:10.1109/TCCN.2025.
3528892.
[16] X. Chang, J. Wang, K. Li, et al., Research on multi-UAV autonomous obstacle avoidance algorithm integrating improved dynamic window approach and ORCA, Sci.
Rep. 15 (2025) 14646, doi:10.1038/s41598-025-99111-8.
[17] X. Fu, C. Zhi, D. Wu, Obstacle avoidance and collision avoidance of UAV swarm
based on improved VFH algorithm and information sharing strategy, Comput. Ind.
Eng. 186 (2023) 109761, doi:10.1016/j.cie.2023.109761.
[18] M. Li, Z. Huang, W. Bi, et al., A fish evasion behavior-based vector field histogram
method for obstacle avoidance of multi-UAVs, Aerosp. Sci. Technol. 159 (2025)
109974, doi:10.1016/j.ast.2025.109974.
[19] C. Fuchs, C. Borst, G.C.H.E. de Croon, et al., An ecological approach to the supervisory control of UAV swarms, Int. J. Micro Air Veh. 6 (4) (2014) 211–229,
doi:10.1260/1756-8293.6.4.211.
[20] D.J. Rea, S.H. Seo, Still not solved: a call for renewed focus on user-centered teleoperation interfaces, Front. Robot. AI 9 (2022) 704225, doi:10.3389/frobt.2022.704225.
11

---
**[Page 12]**

Z. Zhou, P. Wei, Z. Wang et al. Design and Artificial Intelligence 1 (2025) 100029
[21] W. Zhang, D. Feltner, J. Shirley, et al., Unmanned aerial vehicle control interface
design and cognitive workload: a constrained review and research framework, in:
Proceedings of the 2016 IEEE International Conference on Systems, Man, and Cybernetics (SMC), IEEE, 2017 001821–001826, doi:10.1109/SMC.2016.7844502.
[22] P.G. Fahlstrom, T.J. Gleason, Mohammad H Sadraey, Introduction to UAV Systems,
5th ed., John Wiley & Sons, Hoboken, NJ, 2022.
[23] S.S. Abdi, D.A. Paley, Safe operations of an aerial swarm via a cobot human swarm
interface, in: Proceedings of the 2023 IEEE International Conference on Robotics and
Automation (ICRA), IEEE, 2023, pp. 1701–1707, doi:10.1109/ICRA48891.2023.
10161343.
[24] A. Hocraffer, C.S. Nam, A meta-analysis of human-system interfaces in unmanned
aerial vehicle (UAV) swarm management, Appl. Ergon. 58 (2017) 66–80, doi:10.
1016/j.apergo.2016.05.011.
[25] J. Kaduk, M. Cavdan, K. Drewing, et al., From one to many: how active robot swarm
sizes influence human cognitive processes, in: Proceedings of the 2024 33rd IEEE International Conference on Robot and Human Interactive Communication (ROMAN),
IEEE, 2024, pp. 1207–1212, doi:10.1109/RO-MAN60168.2024.10731232.
[26] F. Saffre, H. Hildmann, H. Karvonen, The design challenges of drone swarm control, in: D. Harris, WC. Li (Eds.), Engineering Psychology and Cognitive Ergonomics.
HCII 2021. Lecture Notes in Computer Science, vol 12767, Springer, Cham, 2021,
pp. 408–426, doi:10.1007/978-3-030-77932-0_32.
[27] J.Y.C. Chen, M.J. Barnes, Human–agent teaming for multirobot control: a review of
human factors issues, IEEE Trans. Hum. Mach. Syst. 44 (1) (2014) 13–29, doi:10.
1109/THMS.2013.2293535.
[28] A. Kiesel, M. Steinhauser, M. Wendt, et al., Control and interference in task switching—a review, Psychol. Bull. 136 (5) (2010) 849–874, doi:10.1037/a0019842.
[29] P. Squire, G. Trafton, R. Parasuraman, Human control of multiple unmanned vehicles: effects of interface type on execution and task switching times, in: Proceedings of the 1st ACM SIGCHI/SIGART Conference on Human-Robot Interaction, ACM,
2006, pp. 26–32, doi:10.1145/1121241.1121248.
[30] A. Chakraborty, A.K. Kar, Swarm intelligence: a review of algorithms, in: S. Patnaik,
XS. Yang, K. Nakamatsu (Eds.), Nature-Inspired Computing and Optimization. Modeling and Optimization in Science and Technologies, vol 10, Springer, Cham, 2017,
pp. 475–494, doi:10.1007/978-3-319-50920-4_19.
[31] J. Kennedy, Swarm intelligence, in: A.Y. Zomaya (Ed.), Handbook of Nature-Inspired
and Innovative Computing, Springer, Boston, MA, 2006, pp. 187–219, doi:10.1007/
0-387-27705-6_6.
[32] P. Chaffey, R. Artstein, K. Georgila, et al., Human swarm interaction using plays,
audibles, and a virtual spokesperson, in: Proceedings of the Artificial Intelligence and
Machine Learning for Multi-Domain Operations Applications II, SPIE, 2020 Volume
11413, doi:10.1117/12.2557573.
[33] N. Couture, S. Bottecchia, S. Chaumette, et al., Using the soundpainting language
to fly a swarm of drones, in: J. Chen (Ed.), Advances in Human Factors in Robots
and Unmanned Systems. AHFE 2017. Advances in Intelligent Systems and Computing, vol 595, Springer, Cham, 2018, pp. 39–51, doi:10.1007/978-3-319-60384-
1_5.
[34] J. Hermann, M. Plückthun, A. Dogangün, et al., User-defined gesture and voice control in human-drone interaction for police operations, in: Proceedings of the Nordic
Human-Computer Interaction Conference, ACM, 2022 Article No. 41, doi:10.1145/
3546155.3546661.
[35] A. Baza, A. Gupta, E. Dorzhieva, et al., SwarMan: anthropomorphic swarm of drones
avatar with body tracking and deep learning-based gesture recognition, in: Proceedings of the 2022 IEEE International Conference on Systems, Man, and Cybernetics
(SMC), IEEE, 2022, pp. 1284–1289, doi:10.1109/SMC53654.2022.9945537.
[36] K. Higuchi, J. Rekimoto, Flying head: a head motion synchronization mechanism for
unmanned aerial vehicle control, in: Proceedings of the CHI ’13 Extended Abstracts
on Human Factors in Computing Systems, ACM, 2013, pp. 2029–2038, doi:10.1145/
2468356.2468721.
[37] K. Kim, J.H. Hong, K. Bae, et al., Extremely durable electrical impedance
tomography–based soft and ultrathin wearable e-skin for three-dimensional tactile
interfaces, Sci. Adv. 10 (38) (2024) eadr1099, doi:10.1126/sciadv.adr1099.
[38] L.H. Kim, D.S. Drew, V. Domova, et al., User-defined swarm robot control, in: Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems,
ACM, 2020, pp. 1–13, doi:10.1145/3313831.3376814.
[39] V. Serpiva, A. Fedoseev, S. Karaf, et al., OmniRace: 6D hand pose estimation for intuitive guidance of racing drone, in: Proceedings of the 2024 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), IEEE, 2024, pp. 2508–2513,
doi:10.1109/iros58592.2024.10801907.
[40] K. Tao, J. Yu, J. Zhang, et al., Deep-learning enabled active biomimetic multifunctional hydrogel electronic skin, ACS Nano 17 (16) (2023) 16160–16173,
doi:10.1021/acsnano.3c05253.
[41] C. Yiu, Y. Liu, W. Park, et al., Skin-interfaced multimodal sensing and tactile feedback system as enhanced human-machine interface for closed-loop drone control,
Sci. Adv. 11 (13) (2025) eadt6041, doi:10.1126/sciadv.adt6041.
[42] J. Jun, B. Zhao, P. Zhang, et al., Research on UAV control method based on eye
tracking, in: Proceedings of the 2021 33rd Chinese Control and Decision Conference
(CCDC), IEEE, 2021, pp. 3281–3286, doi:10.1109/ccdc52312.2021.9602071.
[43] M. Yang, J. Wang, Y. Gao, et al., Aim where you look: eye-tracking-based UAV control framework for automatic target aiming, IEEE Internet Things J 11 (12) (2024)
21250–21260, doi:10.1109/JIOT.2024.3390115.
[44] T. Deng, Z. Huo, L. Zhang, et al., A VR-based BCI interactive system for UAV swarm
control, Biomed. Signal Process. Control 85 (2023) 104944, doi:10.1016/j.bspc.
2023.104944.
[45] S. Liu, Z. Ming, M. Liu, et al., Remote-oriented brain-controlled unmanned aerial
vehicle for IoT, IEEE Internet Things J 11 (17) (2024) 29202–29214, doi:10.1109/
jiot.2024.3406837.
[46] M.Divband Soorati, J. Clark, J. Ghofrani, et al., Designing a user-centered interaction interface for human–swarm teaming, Drones 5 (4) (2021) 131, doi:10.3390/
drones5040131.
[47] M.F. Hinss, A.M. Brock, R.N. Roy, Cognitive effects of prolonged continuous humanmachine interaction: The case for mental state-based adaptive interfaces, Front. Neuroergon. 3 (2022) 935092, doi:10.3389/fnrgo.2022.935092.
[48] S. Lorite, A. Muñoz, J. Tornero, et al., Supervisory control interface design for unmanned aerial vehicles through GEDIS-UAV, in: M. Kurosu (Ed.), Human-Computer
Interaction. Human-Centred Design Approaches, Methods, Tools, and Environments.
HCI 2013. Lecture Notes in Computer Science, vol 8004, Springer, Berlin, Heidelberg, 2013, pp. 231–240, doi:10.1007/978-3-642-39232-0_26.
[49] B. Huang, Z. Wang, Q. Cheng, et al., AeroHaptix: a wearable vibrotactile feedback
system for enhancing collision avoidance in UAV teleoperation, IEEE Robot. Autom.
Lett. 10 (5) (2025) 4260–4267, doi:10.1109/LRA.2025.3548866.
[50] E. Tsykunov, R. Agishev, R. Ibrahimov, et al., SwarmTouch: guiding a swarm
of micro-quadrotors with impedance control using a wearable tactile interface, IEEE Trans. Haptics 12 (3) (2019) 363–374, doi:10.1109/TOH.2019.
2927338.
[51] M. Inoue, K. Takashima, K. Fujita, et al., BirdViewAR: surroundings-aware remote
drone piloting using an augmented third-person perspective, in: Proceedings of the
2023 CHI Conference on Human Factors in Computing Systems, ACM, 2023 Article
No. 31, doi:10.1145/3544548.3580681.
[52] B.M. Williamson, E.M. Taranta, Y.M. Moolenaar, et al., Command and control of a
large scale swarm using natural human interfaces, Field Robot 3 (2023) 301–322,
doi:10.55417/fr.2023009.
[53] A. Angelopoulos, A. Hale, H. Shaik, et al., Drone brush: mixed reality drone path
planning, in: Proceedings of the 2022 17th ACM/IEEE International Conference on
Human-Robot Interaction (HRI), IEEE, 2022, pp. 678–682, doi:10.1109/hri53351.
2022.9889504.
[54] C. Zhao, C. Zheng, L. Roldan, et al., Adaptable mixed-reality sensorimotor interface
for human-swarm teaming: person with limb loss case study and field experiments,
Field Robot 3 (2023) 243–265, doi:10.55417/fr.2023007.
[55] J. Cui, G. Liu, H. Wang, et al., TPML: task planning for multi-UAV system with large
language models, in: Proceedings of the 2024 IEEE 18th International Conference on
Control & Automation (ICCA), IEEE, 2024, pp. 886–891, doi:10.1109/ICCA62789.
2024.10591846.
[56] S. Javaid, H. Fahim, B. He, et al., Large language models for UAVs: current state and
pathways to the future, IEEE Open J. Veh. Technol. 5 (2024) 1166–1192, doi:10.
1109/OJVT.2024.3446799.
[57] Y. Li, N. Liao, G. Zhang, et al., Unmanned vehicle formation control based
on large language model, in: Proceedings of 2024 12th China Conference on
Command and Control. C2 2024. Lecture Notes in Electrical Engineering, vol
1267, Springer, Singapore, 2024, pp. 329–339, doi:10.1007/978-981-97-7774-
7_30.
[58] Y. Tian, F. Lin, Y. Li, et al., UAVs meet LLMs: Overviews and perspectives towards
agentic low-altitude mobility, Inf. Fusion 122 (2025) 103158, doi:10.1016/j.inffus.
2025.103158.
[59] H. Yu, C. Wang, L. Wu, et al., LLMSTP: empowering swarm task planning with large
language models, in: L. Liu, Y. Niu, W. Fu, et al. (Eds.), Proceedings of 4th 2024
International Conference on Autonomous Unmanned Systems (4th ICAUS 2024).
ICAUS 2024. Lecture Notes in Electrical Engineering, vol 1374, Springer, Singapore,
2025, pp. 500–510, doi:10.1007/978-981-96-3552-8_47.
[60] J.A. Adams, J.Y.C. Chen, M.A. Goodrich, Swarm transparency, in: Proceedings of
the Companion of the 2018 ACM/IEEE International Conference on Human-Robot
Interaction, ACM, 2018, pp. 45–46, doi:10.1145/3173386.3177008.
[61] A. Hussein, S. Elsawah, H.A. Abbass, The reliability and transparency bases of trust
in human-swarm interaction: principles and implications, Ergonomics 63 (9) (2020)
1116–1132, doi:10.1080/00140139.2020.1764112.
[62] W. Zhang, D. Feltner, D. Kaber, et al., Utility of functional transparency and usability
in UAV supervisory control interface design, Int. J. Soc. Robot. 13 (7) (2021) 1761–
1776, doi:10.1007/s12369-021-00757-x.
[63] A. Capiola, I.A. Hamdan, J.B. Lyons, et al., The effect of asset degradation on trust
in swarms: a reexamination of system-wide trust in human-swarm interaction, Hum.
Factors 66 (5) (2024) 1475–1489, doi:10.1177/00187208221145261.
[64] C. Nam, P. Walker, H. Li, et al., Models of trust in human control of swarms with
varied levels of autonomy, IEEE Trans. Hum. Mach. Syst. 50 (3) (2020) 194–204,
doi:10.1109/THMS.2019.2896845.
[65] K.J. Parnell, J.E. Fischer, J.R. Clark, et al., Trustworthy UAV relationships: applying
the schema action world taxonomy to UAVs and UAV swarm operations, Int. J. Hum.
39 (20) (2023) 4042–4058, doi:10.1080/10447318.2022.2108961.
[66] J. Wilson, G. Chance, P. Winter, et al., Trustworthy swarms, in: Proceedings of the
First International Symposium on Trustworthy Autonomous Systems, ACM, 2023
Article No. 10, doi:10.1145/3597512.3599705.
[67] A. Alharbi, I. Petrunin, D. Panagiotakopoulos, Assuring safe and efficient operation
of UAV using explainable machine learning, Drones 7 (5) (2023) 327, doi:10.3390/
drones7050327.
[68] D. Dissanayaka, T.R. Wanasinghe, R.G. Gosine, Explainable artificial intelligence for
autonomous UAV navigation, in: Proceedings of the 2024 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), IEEE, 2024, pp. 10439–10446,
doi:10.1109/IROS58592.2024.10801529.
[69] M. Gackowska-Kątek, P. Cofta, Explainable machine learning model of disorganisation in swarms of drones, Sci. Rep. 14 (2024) 22519, doi:10.1038/
s41598-024-73220-2.
[70] S. Rodriguez, V. Hilaire, A methodological approach for the analysis and design
of Human–Swarm interactions based upon feedback loops, Expert Syst. Appl. 217
(2023) 119482, doi:10.1016/j.eswa.2022.119482.
12

---
**[Page 13]**

Z. Zhou, P. Wei, Z. Wang et al. Design and Artificial Intelligence 1 (2025) 100029
[71] W.Z. He, Overview of the development of ground control station technology for
drones abroad, Autom. Instrum. (1) (2025) 1–5 https://link.cnki.net/doi/10.14016/
j.cnki.1001-9227.2025.01.001. (in Chinese).
[72] Y. Wang, Q. Zhou, M. Li, et al., Prototyping of UAV swarm control software,
Acta Aeronaut. Astronaut. Sin. 45 (20) (2024) 630678 (in Chinese), doi:10.7527/
S1000-6893.2024.30678.
[73] X. Xiang, Q. Tan, C. Wang, et al., Survey on key technologies of UAV advanced
ground stations, J. Natl. Univ. Def. Technol. 45 (2) (2023) 1–14 (in Chinese), doi:10.
11887/j.cn.202302001.
[74] X. Chen, H. Yang, Design of common software platform for UAV control station, Telecommun. Eng. 58 (7) (2018) 779–784 (in Chinese), doi:10.3969/j.issn.
1001-893x.2018.07.006.
[75] A. Chodorek, R.R. Chodorek, P. Sitek, UAV-based and WebRTC-based open universal
framework to monitor urban and industrial areas, Sensors 21 (12) (2021) 4061,
doi:10.3390/s21124061.
[76] W.Z. He, Research on software universalization of UAV ground control station, Mod.
Electron. Tech. 46 (20) (2023) 95–100 https://link.cnki.net/doi/10.16652/j.issn.
1004-373x.2023.20.018. (in Chinese).
[77] X. Liu, D. Cui, M. Xia, et al., Design of a configurable generic architecture for unmanned aerial vehicle flight control system application software, in: L. Yan, H. Duan,
Y. Deng (Eds.), Advances in Guidance, Navigation and Control. ICGNC 2024. Lecture Notes in Electrical Engineering, vol 1342, Springer, Singapore, 2025, pp. 33–42,
doi:10.1007/978-981-96-2220-7_4.
[78] L. Zhen, X. Wang, S. Liu, Application of human factors engineering in command
and control information system, in: Proceedings of the 5th China Conference on
Command and Control, CICC, 2017, pp. 62–66. (in Chinese).
[79] J. Zhang, X. Zhao, X. Wang, Man-machine ergonomics evaluation of static operation
interface of UAV ground station, Aircr. Des. 40 (04) (2020) 49–53+64 https://link.
cnki.net/doi/10.19555/j.cnki.1673-4599.2020.04.011 . (in Chinese).
[80] D. Perez, I. Maza, F. Caballero, et al., A ground control station for a multi-UAV
surveillance system: design and validation in field experiments, J. Intell. Rob. Syst.
69 (1–4) (2013) 119–130, doi:10.1007/s10846-012-9759-5.
[81] L. Wang, Q. Zhang, H. Zhu, Research of UAS common ground control station with
support of joint operations, J. Syst. Simul. 20 (22) (2008) 6171–6175 (in Chinese).
[82] T.H. Chung, R. Daniel, DARPA OFFSET: a vision for advanced swarm systems
through agile technology development and experimentation, Field Robot 3 (2023)
97–124, doi:10.55417/fr.2023003.
[83] B. Brehmer, The dynamic OODA loop: amalgamating Boyd’s OODA loop and the cybernetic approach to command and control, in: Proceedings of the 10th International
Command and Control Research Technology Symposium, CCRP, 2005.
[84] J. Johnson, Automating the OODA loop in the age of intelligent machines: reaffirming the role of humans in command-and-control decision-making in the digital age,
Def. Stud. 23 (1) (2023) 43–67, doi:10.1080/14702436.2022.2102486.
[85] J. Brooke, et al., SUS: A quick and dirty usability scale, in: P.W. Jordan, B. Thomas,
B.A. Weerdmeester, et al. (Eds.), Usability Evaluation in Industry, CRC Press, London, 1996, doi:10.1201/9781498710411-35.
13