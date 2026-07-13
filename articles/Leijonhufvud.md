# Leijonhufvud

*Source file: Leijonhufvud.pdf — 112 pages*


---
**[Page 1]**

Linköpings universitet
SE–581 83 Linköping
+46 13 28 10 00 , www.liu.se
Linköping University | Department of Computer and Information Science
Bachelor’s thesis, 16 ECTS | Kognitionsvetenskap
Spring term 2026 | LIU-IDA/KOGVET-G–26/003–SE
Meaningful human control in
drone swarms
Minna Leijonhufvud
Supervisor : Wilhelm Brodin
Examiner : Björn Johansson
External supervisor : Martin Castor

---
**[Page 2]**

Upphovsrätt
Detta dokument hålls tillgängligt på Internet - eller dess framtida ersättare - under 25 år från publicer-
ingsdatum under förutsättning att inga extraordinära omständigheter uppstår.
Tillgång till dokumentet innebär tillstånd för var och en att läsa, ladda ner, skriva ut enstaka ko-
pior för enskilt bruk och att använda det oförändrat för ickekommersiell forskning och för undervis-
ning. Överföring av upphovsrätten vid en senare tidpunkt kan inte upphäva detta tillstånd. All annan
användning av dokumentet kräver upphovsmannens medgivande. För att garantera äktheten, säker-
heten och tillgängligheten finns lösningar av teknisk och administrativ art.
Upphovsmannens ideella rätt innefattar rätt att bli nämnd som upphovsman i den omfattning som
god sed kräver vid användning av dokumentet på ovan beskrivna sätt samt skydd mot att dokumentet
ändras eller presenteras i sådan form eller i sådant sammanhang som är kränkande för upphovsman-
nens litterära eller konstnärliga anseende eller egenart.
För ytterligare information om Linköping University Electronic Press se förlagets hemsida
http://www.ep.liu.se/.
Copyright
The publishers will keep this document online on the Internet - or its possible replacement - for a
period of 25 years starting from the date of publication barring exceptional circumstances.
The online availability of the document implies permanent permission for anyone to read, to down-
load, or to print out single copies for his/hers own use and to use it unchanged for non-commercial
research and educational purpose. Subsequent transfers of copyright cannot revoke this permission.
All other uses of the document are conditional upon the consent of the copyright owner. The publisher
has taken technical and administrative measures to assure authenticity, security and accessibility.
According to intellectual property law the author has the right to be mentioned when his/her work
is accessed as described above and to be protected against infringement.
For additional information about the Linköping University Electronic Press and its procedures
for publication and for assurance of document integrity, please refer to its www home page:
http://www.ep.liu.se/.
© Minna Leijonhufvud

---
**[Page 3]**

Abstract
As autonomous drone swarms are increasingly considered for military applications,
ensuring that humans retain meaningful control over their behavior becomes both a legal
and ethical imperative. The concept of Meaningful Human Control (MHC) has emerged
as a central framework for addressing this challenge, yet it remains largely untested in
concrete operational contexts, and the parallel field of human-swarm interaction has de-
veloped without systematic reference to MHC’s requirements. This study bridges that
gap. Using a simulation-based user study in a military surveillance scenario, five par-
ticipants operated a semi-autonomous drone swarm through a Graphical User Interface.
Their interactions were recorded and analyzed using the Critical Decision Method, and
the resulting control failures were mapped to a consolidated MHC framework. The study
makes two principal contributions. First, it identifies 32 specific control limitations across
six themes and maps these to the technical and socio-technical layers of a consolidated
MHC model, demonstrating concretely where the system falls short of MHC’s conditions
and where those conditions are themselves underspecified. Second, it introduces the dis-
tinction between Hard and Soft MHC. Hard MHC refers to binary requirements and
functions that must exist for meaningful control to be possible at all. Soft MHC refers
to the quality and operational usability of those functions, capturing the design-mediated
failures that requirements alone cannot capture. Together, these contributions advance
the operationalization of MHC.

---
**[Page 4]**

Acknowledgments
I met Martin Castor at WARA-PS last year. After I enthusiastically proclaimed that I would
love to work with drone swarms in the future, he gave me his card.
A few months after
we agreed that he was going to be my supervisor for my bachelor’s thesis, and he was most
generous in allowing me to use GEISTT AB’s simulation technology. Castor has been nothing
but kind, and I want to thank him not only for the opportunity he gave me, but also for
the time he spent discussing the study’s methodology, keeping track of my progress, and the
organizational work he did to ensure my trials could be performed successfully.
After meeting Castor, I wrote to Björn Johansson, who had previously been my professor
in a course about systems thinking, a course without which this project would likely never
have happened. When I proposed my idea for the thesis, he accepted my invitation to be my
supervisor. We have bonded over fantasy books and he has continually read my work, taking
time to give his insight on structure, content, and language, shaping my research questions,
while cheering me on. I want to thank Johansson both for his contributions to this project
and as a formative professor in my education.
To the five participants who generously gave their time and thoughtful insights, and also
welcomed me at the lunch table in Sundbyberg, I give my sincerest thanks.
I also want to thank my personal support network, that I have spent the majority of my
8-hour workdays over the past months with. They have cheered me on, listened to my frus-
trations, and answered stupid questions that should never have been uttered. So to Joachim,
Banafsha, Sorre, Ramón, Abudi, Matthias (the French), Mattias (the Swedish), and Koryun,
as well as an extended group of wonderful friends: you brighten my days, lighten my load, and
bring meaning to routine. Thank you.
iv

---
**[Page 5]**

Contents
Abstract
iii
Acknowledgments
iv
Contents
v
1
Introduction
1
1.1
Research question & purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2
2
Related Work
3
2.1
Meaningful human control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
2.2
Human-Swarm interaction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.3
The approach of this study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
3
Method
13
3.1
Simulation environment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
3.2
Human-Machine Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
3.3
Drone swarm path planning algorithms
. . . . . . . . . . . . . . . . . . . . . . . .
23
3.4
Simulated setting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
3.5
Experiment design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
3.6
Participants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
3.7
Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
3.8
Analytical approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
3.9
Ethics
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
4
Results
30
4.1
Timeline summaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
4.2
Human control within the system . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
4.3
Control failures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
36
4.4
Mapping between MHC and control issues . . . . . . . . . . . . . . . . . . . . . . .
43
5
Discussion
46
5.1
RQ1: How is human control performed and maintained within the system?
. .
46
5.2
RQ2: When does human control fail within the system? . . . . . . . . . . . . . .
47
5.3
RQ3: How can the system failures be compared to principles of human control?
48
5.4
Discussion of theory
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
5.5
Discussion of method
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
5.6
Future research . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
54
6
Conclusion
55
Bibliography
56
A Participant Consent Form
62
v

---
**[Page 6]**

B Introduction to the HMI
65
C Introduction to the task (Scenario 1 and 2)
77
D Introduction to the task (Scenario 3)
79
E Inject timelines
82
F CDM Probes
84
G Timelines
88
vi

---
**[Page 7]**

1
Introduction
The concept of coordinated unmanned aerial vehicles (UAV’s) is becoming increasingly rel-
evant. Their potential to revolutionize surveillance situations, search and rescue, policing,
and warfare has prompted research on how these swarms can be included in rescue opera-
tions(Abdellatif et al., 2025; Horyna et al., 2023; Ruetten et al., 2020), defense command
structures (Chen, 2023; Zhang et al., 2023), and policing (Arranz et al., 2023; Priya et al.,
2024). The potential of swarms to serve as agile first-responders (Abdellatif et al., 2025), as
eﬀicient intelligence gatherers (Cho et al., 2020), and travelers to areas that would otherwise
elude operations due to their being dangerous to humans or otherwise inaccessible (Abdellatif
et al., 2025; Horyna et al., 2023). Within defense surveillance situations, swarms could serve
as an automatic threat detection system, gathering multi-modal data to create enriched intel,
with a fraction of the staﬀing of traditional surveillance.
As swarms become more capable, however, the question of how decisions are made within
these systems becomes increasingly important. Semi-autonomous swarms often do not simply
execute predefined commands; they respond dynamically to their environments (Hulianytskyi,
2026), and as such, decisions that would otherwise be made by humans are increasingly del-
egated to the system itself. This creates two distinct but interrelated challenges that cannot
be addressed in isolation from each other.
The first is a practical challenge of interface design. Tackling the practical challenges of
designing human-autonomy interfaces is the human-autonomy interaction field, more specif-
ically, for swarms, the human-swarm interaction field. Due to the novelty of swarms, this
field is young and quick-moving. No consensus on what these interfaces should look like can
be found, though some agreement on the necessity of switching between different levels of
control(Bjurling et al., 2020), like higher-level tactical directing of drones and manual control,
can be found(Kolling et al., 2016).
The second challenge is a moral and legal one. As no system is infallible, situations will
inevitably arise where these systems fail. When these failures occur, it remains paramount
that a human can be held responsible for that failure. Otherwise, an accountability gap(Smith,
2022; Taddeo & Blanchard, 2022; Verdiesen, Aler Tubella, & Dignum, 2021), will be created
where the human can not be said to be responsible, because they were not meaningfully
involved in that failure, and the autonomous agent that gave rise to the failure can also not
be said to be responsible, as that would require it to be a moral agent, which it is not (Asaro,
1

---
**[Page 8]**

1.1.
Research question & purpose
2012; Geiß & Lahmann, 2017). The design of semi-autonomous systems, especially in sensitive
contexts, is therefore not only a question of practicality, but a moral one.
To tackle the issues of legality and morality of swarms and similar autonomous systems,
it remains paramount to formulate requirements, recommendations, and legislation that can
regulate the immoral and unjust uses of the technology. To this end, the concept of Meaningful
Human Control (MHC) has been proposed(UNIDIR, 2014; U.S.
Department of Defense,
2012; Watch, 2012)(ICRC, 2017). The international community has seemingly agreed on it’s
importance, but has yet to settle on a definition(Ekelhof & Persi Paoli, 2020) . It instead,
has primarily worked as an agreement on a research direction that focuses on ensuring that
humans remain in control over AI (“Context Appropriate Human Involvement Across the AI
System Lifecycle,” 2025). Attempts at defining the concept and the necessary conditions for
achieving it have, however, been made. For example, by NATO’s focus group that created the
7 dimensions of meaningful human control(Boardman & Butcher, 2019; “Context Appropriate
Human Involvement Across the AI System Lifecycle,” 2025), which describes 7 dimensions, or
qualities of the human-machine system that together create MHC. Verdiesen, Aler Tubella, and
Dignum (2021) also created a framework for the concept that presents a more comprehensive
view of it, including socio-technical considerations, and governance considerations.
Despite the clear relevance of both of these challenges to each other, the MHC frameworks
and the human-swarm interaction research have largely developed in parallel, without being
explicitly connected. MHC frameworks are largely untested in specific practical use cases,
and human-swarm interaction research has progressed largely without the evaluative lens that
MHC could provide (Miller et al., 2023). To develop both fields further, it is necessary to
situate MHC within specific human autonomy use cases, and to allow the insights from those
use cases to inform the frameworks in return.
1.1
Research question & purpose
This study aims to situate the frameworks of MHC in the use case of military surveillance
with swarm technology, and reason about the limitations and possible future developments for
both human-swarm interaction research and MHC as a concept.
To do this, A simulation-based research environment developed by the partner company of
this study, GEISTT, is used to perform user tests. Participant interaction with the simulated
Graphical User Interface (GUI), and the autonomous swarm is recorded, and a post-interview
is performed in the form of the critical decision method. These interactions are then analyzed,
and the results are compared to a perfunctory framework of MHC that was created by merg-
ing NATO’s 7 dimensions of MHC (“Context Appropriate Human Involvement Across the
AI System Lifecycle,” 2025) with the Comprehensive Human Oversight Framework (CHOF)
(Verdiesen, Aler Tubella, & Dignum, 2021).
The following three research questions, meant to build on each other, were formulated:
1. How is human control performed and maintained within the system?
2. When does human control fail within the system?
3. How do the system failures map to the frameworks of meaningful human control?
What the results imply for both the development of the interface used in the study as well
as MHC as a concept will then be discussed in an explorative manner based on the answers
to these questions.
2

---
**[Page 9]**

2
Related Work
This study sits at the intersection of two distinct but interrelated bodies of literature. The
first concerns the moral, legal, and philosophical debate around meaningful human control over
autonomous systems, and the frameworks that have been developed in an attempt to define
and operationalize the concept. The second is the human-automation interaction literature,
and more specifically, the subfield of human-swarm interaction, which addresses the practi-
cal challenges of designing and evaluating operator control over autonomous swarm systems.
These two bodies of literature have largely developed in parallel, and connecting them is the
central aim of this study. The following section, therefore, first presents the background and
key frameworks of MHC, before turning to the human-swarm interaction literature and the
practical challenges it has identified. The section closes by outlining how the insights from
both are brought together in the approach of this study.
2.1
Meaningful human control
MHC has emerged as an influential concept in debates concerning the governance of au-
tonomous systems. The concept is frequently invoked as a means of ensuring that humans
retain an appropriate degree of involvement, responsibility, and oversight when decisions are
increasingly delegated to machines. Most of the international community seemingly agrees
on the importance of the concept, and it has been underlined by human rights organizations
(Watch, 2012), NGO’s (Article 36, 2013; ICRC, 2017), militaries (U.S. Department of Defense,
2012), the United Nations (UNIDIR, 2014), NATO (Boardman & Butcher, 2019; “Context Ap-
propriate Human Involvement Across the AI System Lifecycle,” 2025), as well as in academia
(Booker, 2025; Sparrow, 2007; Verdiesen, Aler Tubella, & Dignum, 2021).
Despite the near-unanimous agreement on MHC’s importance, the international community
is still grappling with the challenge of defining the concept (Ekelhof & Persi Paoli, 2020). This
ambiguity has motivated the development of a number of frameworks that seek to clarify and
operationalize the concept. Before examining these frameworks, however, it is necessary to
understand the concerns that gave rise to meaningful human control in the first place.
3

---
**[Page 10]**

2.1.
Meaningful human control
2.1.1
Why meaningful human control?
As automation and robotics research is quickly progressing, concerns that have long been
present about the technology’s application in sensitive systems are becoming increasingly rele-
vant. As militaries have communicated interest in harnessing the technology (Defence Science
Board, 2012; des Armées, 2019) and as these systems are put into development(Saab, 2024),
the reality of “killer robots”(Sparrow, 2007), is now not only a hypothetical concern, but a
pressing ethical and legal conundrum.
The issues of such robots have been extensively outlined in both legal and philosophical
accounts. Amoroso and Tamburrini (2020) summarizes these concerns as primarily revolving
around technical limitations of autonomous systems that may prevent the systems from com-
plying with international law, responsibility ascription challenges, violation of human dignity as
life-or-death decisions are delegated to technology, and the unique risks autonomous weapons
systems pose to international stability and peace(Amoroso & Tamburrini, 2020). Most of these
will be expanded on below. The last two points are undeniably important when discussing
moral and legal issues regarding autonomous systems and can not be ignored, but will not be
expanded on below, as they have limited value for the study’s aims.
2.1.1.1
Technological limitations
When specifically discussing technological limitations to automation, the inevitable question is
how to overcome them. The known limitations to autonomous systems are many and varied.
There are known computational optimization diﬀiculties in weapon-target assignment systems,
complexities in mechanical systems integration, and limitations in materials science (Sanghvi,
2025) as well as contextual and moral judgment, adversarial robustness, and explainability of
decisions (Longpre et al., 2022). In multi-agent systems, challenges include security, optimal
agent communication, localization methods, task allocation in decentralized control structures,
fault detection, optimal learning algorithms, and coordinated and goal-oriented control (Dorri
et al., 2018).
The need for meaningful human control is thus partly dictated by the quality of the tech-
nology. Indeed, there may be situations in the future where an autonomous system, making
its own informed decisions based on complex data, might perform better than a human would
have in the situation, having to make the choice (Cummings, 2019). Based on the quality and
performance of this type of system, some therefore argue that proper system authentication
is more important and more actionable than meaningful human control (Cummings, 2019).
2.1.1.2
Responsibility ascription challenges
No matter how well a system is authenticated, failure is still inevitable. When failures happen,
it remains paramount to maintain the possibility of assigning accountability. Autonomous
systems pose a challenge to this as they become increasingly agentic, thereby excluding humans
from decision-making. Concerns of humans essentially operating as “moral crumple zones”
when failures occur have been raised (Elish, 2019), meaning that operators may lack the
ability, awareness, and foresight to oversee and control an autonomous system’s behavior, yet
may still be held accountable for its failures. This constitutes what authors Smith (2022),
Taddeo and Blanchard (2022), and Verdiesen, Aler Tubella, and Dignum (2021) would call
an ”accountability gap”, that is, a gap where accountability can not correctly be ascribed to
a human. Similar concerns have been raised by a milieu of writers ever since the reality of
autonomous weapon systems became viable (Arkin et al., 2012; Asaro, 2012; Matthias, 2004;
McDougall, 2019; Sparrow, 2016).
Some propose that this responsibility gap could be closed by superior responsibility (Miller
et al., 2023), meaning that the individual who chooses to use a technology should be held
responsible for its failures. This approach has been criticized because it demands a superior-
4

---
**[Page 11]**

2.1.
Meaningful human control
subordinate relationship that is absent when using weapons, thereby legally disqualifying the
perspective (Spadaro, 2024).
Another approach to closing the accountability gap would be to assign accountability to
the autonomous agent. This concept is thoroughly criticized and holds little weight in legal
and ethical debates. It has been well established that machines of any kind cannot be held
accountable in life-or-death situations, both on legal and ethical grounds (Asaro, 2012; Geiß
& Lahmann, 2017). This will be maintained, so long as machines can not be said to be moral
agents (Shin, 2025). Imbuing automation with any form of morality has been widely criticized
and may not be computationally viable(Arnold & Scheutz, 2016).
Assigning autonomous
agents any type of accountability is therefore largely out of the question and would likely
require overhauls of the general view of accountability and morality.
The problem of the accountability gap is unlikely to be closed without human involvement
in the decision-making of automation. This involvement also needs to be meaningful, in that
the human must have control, not only in name, but in practice.
What constitutes such
meaningful control, however, is far from self-evident. The concerns of technological limitations
and responsibility gaps point to the need for a concept that can define appropriate human
involvement legally and ethically. MHC sets out to do exactly this, yet what it requires in
practice remains an open question.
2.1.2
Defining MHC
The lack of clear definition of MHC creates ambiguity in how the concept should be applied
for lawmaking and legislation (Kwik, 2022; Santoni De Sio & Van Den Hoven, 2018), making it
unclear when a system can be said to facilitate MHC. In extension, it is unclear how MHC can
be tested, evaluated, and considered in design. Defining the concept thus remains a central
challenge.
In recent years, a few different frameworks, aiming to describe MHC have been produced.
Some frameworks focus primarily on operator control and the necessary factors for facilitating
that, such as NATO’s dimensions of human control (Boardman & Butcher, 2019) and the
layered oversight framework (Booker, 2025). Others take a broader approach, aiming to com-
prehensively describe automated system regulation and control, such as NATO HFM 330’s
RTG Life cycle Framework (“Context Appropriate Human Involvement Across the AI Sys-
tem Lifecycle,” 2025). Similarly to “Context Appropriate Human Involvement Across the AI
System Lifecycle” (2025), Verdiesen, Aler Tubella, and Dignum (2021) defined a framework
to include three layers of control: governance, socio-technical, and technical, called the Com-
prehensive Human Oversight framework(CHOF). CHOF offers a formalized framework for
analyzing how different governance layers interact to create challenges to meaningful human
control, which, coupled with NATO’s dimensions of human control, will serve as the basis for
this study. It must, however, remain clear that the framework and the dimensions used are
likely to be iterated on in the future, and a consensus is yet to be reached.
2.1.2.1
Dimensions of human control
NATO’s framework of human control (Boardman & Butcher, 2019) outlines six key dimensions
of operator control over an autonomous system.
These include that the operator has 1)
freedom of choice, 2) the ability to impact the system’s behavior, 3) time to decide to engage,
4) suﬀicient situational understanding, 5) suﬀicient understanding of the system, and 6) the
ability to predict the system's behavior.
The dimension of freedom of choice captures both direct and indirect ways the system
can limit the operator’s freedom of choice. The operator could be directly limited by not
being offered the option of a course of action or by a function being inaccessible. Similarly,
the operator’s freedom of choice can be indirectly limited by incomprehensible or inaccessible
information.
Information may also become inaccessible due to high workloads, which can
5

---
**[Page 12]**

2.1.
Meaningful human control
overload the operator’s cognitive capacity, leading to poor situational awareness and forcing
the operator to rely on the system to make decisions in whole or in part.
Even cultural
aspects can limit freedom of choice, as norms or fear may lead to judgments against operators
for choosing alternative courses of action.
The ability to impact the system’s behavior concerns the operator’s ability to affect the
system in meaningful ways, whether preemptively, before deployment, manually, or intermit-
tently.
The third dimension, that the human time to decide to engage with the system and alter
its behavior, is the temporal dimension of the framework. Meaning that the human has a
suﬀicient amount of time to process relevant information and perform relevant tasks. This may
become an issue as the system’s perception, processing, decision, and execution loop exceeds
that of the human, which would force the operator to practice control at impossible speeds.
This highlights that human-in-the-loop solutions may not always be possible, necessitating
before-the-loop control.
The fourth dimension is the operator’s situational understanding.
To make informed,
good, and responsible decisions, the operator needs to understand the situational context of
that decision. Possible issues include a lack of information about the situation and inaccuracies
in the information. This dimension is closely related to the first condition, as many of the
same issues can limit it as well, such as overwhelming workloads and inaccessible information.
The fifth dimension encompasses the operator’s understanding of the system. It captures
how well a human can understand the system’s states, capabilities, and limitations to effec-
tively monitor quality and understand the rationale behind the decisions and recommendations
made.
The last dimension is that the human should be able to predict the system’s behavior and
the environment’s effects. This includes how the system will react under different circumstances
and in response to different inputs.
Thematically, this dimension is clearly related to the
fifth dimension, as knowledge of the system and of how it works is necessary for success in
this dimension. Similarly, it relates to the fourth dimension, as predicting behavior requires
awareness of the situation in the first place.
2.1.2.2
Comprehensive human oversight framework (CHOF)
CHOF connects the concepts of responsibility, accountability, control, and oversight to create
a framework of human oversight within autonomous weapons systems in three levels: (gov-
ernance, socio-technical, and technical). These different layers are then further divided into
temporal categories (Before deployment, During deployment, and After deployment) to con-
nect the framework to conceptions of both ex ante and Ex post accountability.
The different layers and the temporal categories can be found in Figure 2.1. The conditions
on each layer are further expanded upon in (Verdiesen, Santoni De Sio, & Dignum, 2021). At
the technical layer, the conditions required for meaningful human control are: the ability
to, pre-deployment, provide the right input to the system to limit behaviors and prepare for
deployment. The presence of healthy feedback mechanisms during deployment is also central,
allowing the operator to both give the correct and appropriate direction to the system and
receive the right feedback to compare output with goals during deployment.
The socio-technical covers the psychological and motivational conditions required for sys-
tem control. The human operator should be able to set the appropriate control measures
before deployment and have a clear understanding of the systems’ limitations and capabilities.
During deployment, they should be able to engage meaningfully with the system, understand
what’s going on to effectively supervise it, and maintain ongoing control. After deployment,
the operator should be able to inspect and assess the system’s behavior and account for its
actions.
6

---
**[Page 13]**
*(This page contains a figure/chart/image not captured in text)*

2.1.
Meaningful human control
Table 2.1
The Comprehensive Human Oversight Framework
The governance layer describes political and institutional conditions to establish meaningful
human control.
As this study focuses on operator–system interaction during deployment,
governance-level mechanisms are acknowledged but excluded from empirical analysis.
Boardman and Butcher (2019) offers a perspective on how human control can be practiced
on the different levels of CHOF. Creating a table of examples of how human control can be
applied across CHOF’s layers.
In Table 2.2, we can see that the human-machine interaction component of the framework
is lost in the interpretation presented in (“Context Appropriate Human Involvement Across
the AI System Lifecycle,” 2025).
2.1.2.3
Consolidating the frameworks
The theory has briefly presented the moral, legal, and philosophical reasons of MHC, as well as
two frameworks of MHC. The first one is NATO’s framework of human control (Boardman &
Butcher, 2019), which focuses on a narrower human-machine-interaction perspective on MHC.
The second is the Comprehensive Human Oversight framework(Verdiesen, Santoni De Sio, &
Dignum, 2021), which takes a broader approach to MHC, applying the concept across the
technology’s life cycle at three levels.
These two frameworks can be consolidated, one offering more depth, and the other more
breadth, by populating the CHOF layers with NATO’s dimensions of MHC. As a basis, I have
used “Context Appropriate Human Involvement Across the AI System Lifecycle” (2025)’s
examples, also presented in the theory, though it is primarily on the governance and socio-
technical layers, as the technical layer needs to be more geared towards HMI for this study.
The consolidated framework of MHC can be seen in Table 2.3.
7

---
**[Page 14]**
*(This page contains a figure/chart/image not captured in text)*

2.2.
Human-Swarm interaction
Figure 2.2
Interpretation of CHOF (“Context Appropriate Human Involvement Across the AI System
Lifecycle,” 2025)
Note. (“Context Appropriate Human Involvement Across the AI System Lifecycle,” 2025)
define ways of exercising control on each layer and section of the original CHOF.
2.2
Human-Swarm interaction
The MHC frameworks presented above are largely legal and moral in nature, and mark the ef-
forts to operationalize the concept. Complementing them is a large body of human-automation
research, spanning from the 1970s, when automation first emerged, to the present day, when
the field has expanded rapidly. The human factors literature has long been in the business of
describing human control at multiple levels, and the magnitude of the practical challenge of
MHC crystallizes within it.
Some challenges seem to recur across the field of human-autonomy interaction and are
often paradoxical. Some of these were outlined as early as the 1980s by Bainbridge (1983) and
remain relevant. Among the most documented are issues of vigilance and automation compla-
cency, where operators monitoring highly automated systems tend toward passive observation
rather than active engagement, leading to degraded response capacity when failures occur
(Molloy & Parasuraman, 1996; Parasuraman & Manzey, 2010). Related to this is the issue of
skill degradation, in which operators who rarely exercise direct control progressively lose the
proficiency required to do so (Casner et al., 2014; Volz et al., 2016). A further well-established
8

---
**[Page 15]**
*(This page contains a figure/chart/image not captured in text)*

2.2.
Human-Swarm interaction
Figure 2.3
Examples of conditions for human control across layers
Note. (“Context Appropriate Human Involvement Across the AI System Lifecycle,” 2025)
define ways of exercising control on each layer and section of the original CHOF
challenge is situational awareness (Endsley, 2019). Situational awareness was defined by End-
sley (1995) as the perception of environmental elements, the comprehension of their meaning,
and the projection of their future status. Maintaining suﬀicient situational awareness while
delegating an increasing share of decision-making to automation is one of the central tensions
in the field. Finally, workload presents a paradoxical challenge: automation is often intro-
duced to reduce operator workload, but in complex multi-system environments, it can instead
introduce new demands for monitoring, mode management, and intervention, resulting in a
harder-to-manage workload rather than simply a lower one (Parasuraman et al., 2000).
These challenges are in a trade-off relationship with one another, where improving one
dimension often worsens another; no perfect solution exists. Though some of these princi-
ples can be generalized, human control looks different across different use cases and types of
autonomous technology. There is limited value in discussing human-automation design at an
abstract level, as the discussion must be situated in a specific use case to allow for deeper under-
9

---
**[Page 16]**

2.2.
Human-Swarm interaction
standing. In this study, the use case is swarming technology, and within the human-autonomy
interaction field, the relevant subfield is human-swarm interaction. An overview of this field
can be found in Kolling et al. (2016), which surveys the state of interaction paradigms, scala-
bility challenges, and operator workload problems as they arise specifically in swarm systems.
Kolling et al. (2016).
2.2.1
Swarm characteristics and their MHC challenges
To understand how meaningful human control can be maintained in swarm systems, it is
first necessary to examine the characteristics that distinguish swarms from other autonomous
technologies. Several features that make swarms operationally attractive also create challenges
for human oversight, predictability, accountability, and intervention. The following subsections
discuss the most relevant characteristics of swarm systems and analyze their implications for
meaningful human control.
2.2.1.1
Decentralized control
Swarms are often not built around a central control node; instead, each drone follows relatively
simple rules and responds to its immediate environment (Hulianytskyi, 2026). This means that
each drone does not need to share its situational understanding with the others, and there is
not necessarily a control hierarchy within the swarm (Hulianytskyi, 2026). Control is instead
distributed. The consequences of this will be explained in following sections.
2.2.1.2
Emergent behavior and unpredictability
The decentralized nature of swarming technologies is part of their appeal and purpose, as
it allows for emergent behaviors, that is, collective behaviors that arise from the interaction
between nodes in a system that are not explicitly programmed. One such example is flocking,
in which each individual drone has rules governing how it should behave relative to its partners,
giving rise to specific flocking formations (Rouff et al., 2004). However, these types of emergent
behaviors cannot be predicted precisely, as they are, per definition, not fully specified in
advance. This poses as a direct challenge to predictability and reliability(Trusilo, 2023). The
more dynamic an algorithm becomes, the less predictable it also becomes, meaning that there
is an inescapable tension between emergence and predictability. This is a problem for MHC
because, as we have seen in the previous section, predictability is a necessary condition for it.
2.2.1.3
Scalability, Speed of operation and operator workload
The decentralized structure of swarms makes them technically scalable, meaning that more
drones can easily be added to the existing swarm without altering the basic logic (Rouff et al.,
2004). However, the same is not true where there is human-swarm teaming. Increasing the
number of drones within a swarm quickly increases the workload demands placed on the human
operator, a challenge documented extensively in multi-robot human factors research(Humann
& Pollard, 2019).
Any automation necessitates some distribution of control from the human to the system,
but with decentralized control, this is exacerbated.
The speed at which a swarm can perceive, process, and act on information can also exceed
human reaction time. This can make real-time human authorization, which is a feature of
human-in-the-loop solutions, practically impossible(Lazaros et al., 2026). This reinforces the
importance of the temporal dimension of MHC described in NATO's framework: if system
speed makes timely human authorization impossible, the basis for meaningful control becomes
increasingly thin (Boardman & Butcher, 2019). Together, these two characteristics of scal-
ability and the speed of operation create the most direct and specific challenges to MHC in
swarm systems.
10

---
**[Page 17]**

2.3.
The approach of this study
2.2.1.4
Traceability
Beyond scalability and speed, the decentralized nature of swarms creates challenges for the
traceability of individual decisions. Because each drone acts according to local rules rather
than centralized commands, swarm behavior is an emergent consequence of agent interactions,
making it diﬀicult to relate individual drone actions to global swarm outcomes(Abeywickrama
et al., 2023; Coppola et al., 2021).
Even if such reconstruction is technically possible, no
human will have directly authorized that specific action, as operators typically direct swarms
at a higher level of abstraction than at individual drone behavior.
This limits the ability
to perform the kind of post-deployment review that both CHOF and basic accountability
requirements demand and will limit the system’s transparency. This poses a direct obstacle
to the post-deployment layer of the consolidated framework presented in Section 2.1.2.3 and
raises governance issues, as transparency is often considered necessary for ethical governance
(Winfield & Jirotka, 2018).
2.2.2
Designing human control over swarm-based systems
As the challenges of swarms related to decentralized control, scalability, and speed of opera-
tion make direct modes of control non-viable, some form of abstraction of control is necessary.
One proposed solution is supervisory control. In Supervisory control, the human operator does
not directly and continuously control a system, but instead plans, programs, and monitors an
automated subsystem that carries out the actual execution of tasks, as defined by Sheridan
(1992). In other paradigms, like adjustable autonomy (Mostafa et al., 2019), the human oper-
ator primarily performs a higher order of control, but depending on the situation, might make
more specific decisions, such as taking over manual control of one drone. The different levels at
which control can be practiced have been defined, for example, in Parasuraman et al. (2000). It
has been established that effective human-swarm interaction may require the operator to move
across these levels (Bjurling et al., 2020). Divband Soorati et al. (2021) showed that high-level
visualization, in the form of a heatmap instead of visualizing each drone in a swarm, may
be more effective. Kolling et al. (2016) identified 4 common ways of communicating operator
intent in the human-swarm interaction literature. These are: 1) switching between algorithms
that implement desired swarm behaviors, 2) changing parameters of a swarm control algo-
rithm, 3) indirect control of the swarm via environmental influences like marking interesting
areas with pheromones, and 4) controlling selected swarm members, typically called leaders.
Beyond these, there is also academic interest in VR-based interfaces(Asavasirikulkij & Hanif,
2023) and gesture-based intent communication(Ding et al., 2026).
Most studies on human-swarm interaction simulate swarms(Hocraffer & Nam, 2017),
though no recent meta-analysis has been found to support this claim. Direct comparisons
have been done between fully machine-led swarms and human-led ones (Hocraffer & Nam,
2017). Metrics that have been used is task performance (Fang et al., 2025; Kolling et al.,
2013), Objective and subjective situational awareness measures (Divband Soorati et al., 2021;
Wattearachchi et al., 2025), and subjective measures of workload (Menda et al., 2011), com-
paratively assessing usability between different visualizations (Divband Soorati et al., 2021),
or modes of control (Kolling et al., 2013).
2.3
The approach of this study
MHC frameworks, particularly CHOF and NATO's dimensions of human control, provide an
account of the conditions necessary for meaningful control, but have been developed at a
theoretical level and remain largely untested in specific practical use cases. It is therefore
unclear how, and whether, the concept applies when situated within the concrete realities of a
swarm operator’s working environment. Human-swarm interaction research, on the other hand,
has developed a rich set of practical findings and interface proposals, but has not systematically
11

---
**[Page 18]**

2.3.
The approach of this study
evaluated these against the requirements of MHC. The result is that the field has produced
solutions to practical challenges without a principled framework for evaluating whether those
solutions are suﬀicient from a control and accountability perspective.
To address this, the present study proposes a practical approach that uses insights from
a user study in a simulated military surveillance scenario to evaluate both the system under
study and the MHC frameworks themselves. The insights gained from established research
on human-autonomy and human-swarm interactions are used to directly evaluate and reason
about meaningful human control. At the same time, the insights gained inform and refine the
consolidated MHC framework presented in Section 2.1.2.3, aiming to make it more concrete
and applicable to the specific challenges of swarm systems. The expectation is not that the
framework will be proven or disproven, but that the process of situating it in a specific use case
will reveal where it is currently under-specified and where it needs to be further developed as
the field matures.
12

---
**[Page 19]**

3
Method
3.1
Simulation environment
Strid et al. (2024) developed the simulation environment and the related software that will
be used for the present study. The project was initiated by the Swedish Defense Materiel
Administration (FMV) within the framework of the FM FoT Military Innovation Program
(MIP), and was carried out through an assignment to GEISTT AB. The environment is built
on top of Unity's game engine, using terrain data (including roads, bodies of water, and islands)
from WARA-PS.
The system allows for studies of drone swarms and human interaction with them by pro-
viding a simulation environment with the ability to handle pre-planned simulated scenarios, a
HMI, a data logging system and Autonomous agent logic for swarming behaviors.
The environment was designed and developed based on a military surveillance scenario,
which the scenarios used in the experiments of this study further develop. The specifics of the
scenarios will be presented in a later section.
3.1.1
System delimitation
The design of the environment is built on a few assumptions of the technical capabilities of
the drone swarm and operational parameters.
1. The drones have wireless encrypted communication with the human swarm operator and
between the drones
2. The drones have the ability to see and avoid obstacles such as terrain, trees, branches,
power lines, etc.
3. The amount of interference with the swarm's communication is none or limited, meaning
that two-way communication between drones and operator are maintained.
4. The drones in the swarm are equipped with positioning systems such as GPS
5. Each drone has one or more sensors (camera, IR camera, radar, or lidar) with high
quality object identification (e.g. person, vehicle).
13

---
**[Page 20]**
*(This page contains a figure/chart/image not captured in text)*

3.2.
Human-Machine Interface
Strid et al. (2024) also point out that drones can be steered through multiple different algo-
rithms, and that each come with its’ own trade-offs. In this environment, only two algorithms
have been implemented. These algorithms will also be presented in a later section.
3.2
Human-Machine Interface
The Human-Machine interface (HMI) enables an operator to control and monitor a swarm
of autonomous drones and is integrated with the environment. This section will detail the
underlying control strategies implemented in the HMI, which modes of control are available
to the operator, and interactive elements and information panels available.
3.2.1
HMI Overview
The main interface is organized into a set of panels, each responsible for a distinct aspect of
swarm management. The panel layout cannot be adjusted during operation.
Figure 3.1
Interface Overview
Note. Figure A shows the interface that the participants are met by at the beginning of the
scenario. The panels are numbered: 1) the resource panel, 2) the zones panel, 3) the tracking
policy panel, 4) the events panel, 5) the alerts panel, 6) the plays panel, 7) the map, 8) the
live camera feed.
The eight main panels can be seen in Figure 3.1 are:
1. Resources: Shows the operator's available drones and their current status, i.e., whether
they are active on a mission or docked at the docking station.
2. Zones: Manages the geographic areas used to control mission execution and regulate
automated drone behavior.
3. Tracking Policy: Controls how the automation responds to detected objects.
The
operator can define how many drones should be assigned to track a given sensor object,
along with any applicable conditions.
4. Events: Presents a running list of system-generated events reflecting ongoing activity
across the swarm.
5. Alerts: Displays and manages any alerts raised by the system, allowing the operator to
review and respond to them.
6. Plays: Manages functions relating to mission plays, and both their creation and execu-
tion.
14

---
**[Page 21]**
*(This page contains a figure/chart/image not captured in text)*

3.2.
Human-Machine Interface
7. Map: Displays map information for the operational area and ongoing tasks.
8. Live Camera feed: Displays a selected drone's live camera footage
The map is the primary informational feed, together with the alerts, events panels, the
resource panel, and live camera feed. The Zones, Tracking Policy, and Plays panels together
allow the operator to control the drone swarm.
Each panel will be detailed in the following sections. First the informational panels will be
covered, and then the control panels.
3.2.2
Informational panels
3.2.2.1
Map
The map is the central panel of the interface and constitutes the primary informational field.
Figure 3.2
The map panel
Note. The map during an instance in the simulation
The map panel, shown in Figure 3.2, displays relevant information for the operational area.
The main elements represented are:
15

---
**[Page 22]**
*(This page contains a figure/chart/image not captured in text)*

3.2.
Human-Machine Interface
• Drone positions, indicated by gray circles.
• Zones. The zones are managed in the zone panel (see more in the zones section). Each
zone is color-coded by type and annotated with mission information. In the example in
Figure J, the active search area is marked with blue, and the no-entry zone around the
sensitive site is marked red.
• Drone nests, marking the location of docking stations.
• Sensor objects, represented by white squares. Objects that are currently being tracked
by a drone are filled in, outlined when they are not, and gray when they are no longer
within sensor coverage. Clicking a sensor object on the map highlights the corresponding
entry in the plays panels sensor object list (read more under the plays section), and vice
versa.
• Alerts, marked by a red triangle that turns gray once acknowledged by the operator.
No example can be seen in Figure J, but it can be seen in a later section in Figure E
instead.
• Current sensor coverage, indicated by shading on the map around the drones.
The map is intentionally kept sparse, displaying only information that is strictly geograph-
ically relevant, while all other information is handled by the dedicated panels better suited to
that content.
The map view can be navigated through the mission and alerts panels, which pan the map
to a selected object's position. The map can also be automatically zoomed out to a view that
encompasses all active mission areas.
3.2.2.2
Events
The event panel is placed below the map, and the Tracking Policy panels in the interface.
Figure 3.3
The events panel
Note. The events panel during an instance in the simulation
The event panel, shown in Figure 3.3, displays events generated by the system and functions
as an activity log in a list format. Each row in the list shows the type of event that has occurred
16

---
**[Page 23]**
*(This page contains a figure/chart/image not captured in text)*

3.2.
Human-Machine Interface
(ex.stopped tracking seen in Figure D), the time of occurrence (ex. “a minute ago” seen in
Figure D) and the source of the event (ex. “Drone ID: 30” seen in Figure D).
The events that are displayed in the events panel include:
• a drone detecting a new object
• a drone ceasing to track an object
• a drone activating its camera feed.
3.2.2.3
Alerts
The Alerts panel is placed to the right of the events panel.
Figure 3.4
The alerts panel
Note. The alerts panel with an alert placed inside it.
Alerts are, like events, also generated by the system and are displayed in a list format. For
each alert, the operator receives a summary of what occurred, when and where it happened,
and any additional relevant information, as can be seen in Figure 3.4.
The main purpose of the alerts panel is to notify the operator when something important
happens that may require the operator's attention. It also works as a to-do log, where the
operator can mark the alerts that they are seeing to by pressing the “acknowledge” button.
By clicking on the view button, further functionality becomes available to the operator.
The further functionality can be seen in Figure 3.5 The severity level of the alert can be
adjusted by pressing either the “Decrease” or “Escalate” buttons. The “Communicate” button
currently does not have any functionality, but in the future it could function as a coordination
resource for use cases where multiple operators are working together. In the text field to the
left, the operator can leave notes.
Along with being listed in the alerts panels, alerts are also displayed on the map by marking
the spot the alert occurred with a warning sign. See Figure 3.6 for reference.
17

---
**[Page 24]**
*(This page contains a figure/chart/image not captured in text)*

3.2.
Human-Machine Interface
Figure 3.5
Pressing View and altering the alert
Note. illustrates what expanding an alert looks like
Figure 3.6
Alert on the map and the alerts panel
Note. The Alerts panel as well as an alert placed on the map
3.2.2.4
Resources
The Resources panel, is placed at the top of the interface.
The resource panel displays the total number of available drones and their current allocation
across active plays. Figure B, shows an example where 60% of the 30 drones are available
for allocation, and 40% of the drones are occupied in the play called Swarm 0. For more
information about plays, see it’s allocated section.
The launching and recovering of drones is automatic and does not require oversight. An
ongoing launch or recovery is indicated by adding an arrow pointing up or down where the
dash is placed in the example presented in Figure 3.7.
18

---
**[Page 25]**
*(This page contains a figure/chart/image not captured in text)*

3.2.
Human-Machine Interface
Figure 3.7
The resources panel
Note. The resources panel during an instance in the simulation
3.2.2.5
The Live Camera Feed
The camera feed panel takes up the entire right side of the interface. There is no functionality
available in this panel; instead, it only displays information in the form of live camera footage
directly from a selected drone.
At the start of the simulation, the feed displays camera footage from the boat that consti-
tutes the DroneBay, where drones are held when they are not deployed on a mission.
The operator can click on the drones in the map, selecting them, and then click on the
camera-button within the plays-panel, or use the drone-icons within the plays-panel to switch
between the camera feeds of different drones.
3.2.3
Control panels
The interface is organized around four broad categories of control principles, as described
by J. W. Crandall et al. (2017) parametric control, whereby the operator adjusts parameters
governing drone behavior; associative control, whereby the operator directly influences indi-
vidual drones which in turn affect the rest of the swarm; environmental control, whereby the
operator modifies the virtual environment that the drones sense and respond to; and strategic
control, whereby the operator issues high-level mission commands. The implemented inter-
face deliberately incorporates at least one mechanism from each of these categories, ensuring
that the operator is afforded multiple modes of interaction with the swarm depending on the
operational context.
3.2.3.1
Plays
The plays panel is placed to the right in the interface. In the plays panel, the operator can
define and monitor current and past “plays”. Each play constitutes a defined area where the
swarms will operate, as well as a surveillance pattern that the drones will adopt.
To create a play, the operator presses the “Surveillance” button at the top of the panel,
seen in Figure H. Pressing “Patrol” or “Delivery” currently does nothing, but could in the
future be developed to entail another type of behavior than the one used in this use case.
After clicking the “surveillance” button, the fields, buttons, and controls displayed in Figure
3.8 becomes visible. In these controls, the operator can set Maximum and minimum flight
altitude of the drones. These controls currently do not alter the drones behavior. The operator
also assigns the play with a zone, that needs to be created in the zones panel beforehand (see
the next section for more information). The zone defines in what area the play is to take place.
The operator also assigns the number of drones that will be deployed to the zone and used for
the play as well as the search algorithm the drone swarm will be using. These algorithms will
be described in a later section. The last parameter set by the operator is the energy strategy,
that can either be Relay, or All-in. These are currently not implemented and do not alter the
behavior of the drones.
The last step to creating a play is clicking the “Calculate” button, which configures the
play and deploys the necessary drones.
After a play has been created it can be monitored in the plays panel.
19

---
**[Page 26]**
*(This page contains a figure/chart/image not captured in text)*

3.2.
Human-Machine Interface
Figure 3.8
Creating a play in the plays panel
Note. The panel used for creating a play that becomes available after clicking the ”surveillance”
button
Active missions are displayed as a list, with each mission represented by its own card. In
Figure 3.9, an example of such a card can be seen.
The upmost part of the card is the title. In Figure 3.9, there is only one card active,
otherwise it would have a title with a number based on the order in comparison to other plays
that it was created.
Below the title, each card shows key mission information, including total elapsed time,
mission state, swarm ID, mission area (the chosen zone), the swarm control algorithm used,
and current sensor coverage of the assigned area.
Below the mission information there is a resources sub-panel. It displays the drones active
in the swarm assigned to the play. Drones actively searching the area are represented by a
circle under “Scanning”, while drones actively tracking an object are represented by a red eye
icon under “Tracking”. These are the drone tracking icons that can also be used when switching
to another live camera feed.
Below the resources sub-panel, a list of all detected objects found during a play is displayed,
the sensor objects list. Each sensor object is listed with its type (person, vehicle, boat, or
unknown), the number of drones currently tracking it, and its assigned policy level. The list
can be sorted by any field in ascending or descending order.
Selecting an object expands a details section beneath the list, revealing additional infor-
mation and control options. In Figure 3.9, the top object listed as type “Person” has been
chosen. The additional information displayed includes the time elapsed since the object was
last detected by a drone, the classification confidence of the object type, and its estimated size.
The object's policy level can be adjusted via the drop down menu that contains all available
policies.
20

---
**[Page 27]**
*(This page contains a figure/chart/image not captured in text)*

3.2.
Human-Machine Interface
Figure 3.9
Ongoing mission in the plays panel
Note. What the plays panel looks like when a play has been defined and is ongoing
Two additional buttons are provided: one to center the map view on the selected object's
position, and one to activate the camera feed of the selected drone that is currently tracking.
This allows the operator to view the scene through the drone's sensors when additional in-
formation is needed to decide on continued tracking or other actions. The operator can also
terminate an active mission through this panel by pressing “Cancel”. This will initiate the
retrieval of the drones associated with the mission
3.2.3.2
Zones
The Zones panel is placed on the left side of the map.
21

---
**[Page 28]**
*(This page contains a figure/chart/image not captured in text)*

3.2.
Human-Machine Interface
Figure 3.10
The Zone panel
Note. What the zones panel looks like when a few Areas of Interest has been defined. All
zones names SO X are search zones that can be used in the plays panel
The zones panel manages the geographic boundaries that govern mission execution. The
panel is structured as a list, where each defined zone occupies a row. An example of the layout
is presented in Figure 3.10. The boundaries defined in a zone can function as a search area for
plays, a restriction zone around protected objects, or a no-fly zone.
Zones can be created by pressing the small plus signs in the top-right corner of the panel.
A zone can also be given a name in the “Title” field, and two parameters can be altered:
1) Block Size and 2) Decay. These alter how the algorithm behaves. The block size parameter
alters the size that a drone can be said to currently occupy, and the decay defines how long an
area can be said to still be covered after the drone has left. For a description of how these are
implemented see Figure 3.3. These factors alter how quickly and where drones aim to cover
for each other.
On the map, active zones are color-coded by type, and zones with ongoing missions display
a summary label indicating mission type, current phase, number of active drones, and number
of detected objects.
3.2.3.3
Tracking Policy
The Tracking Policy panel is placed right under the Zones panel.
22

---
**[Page 29]**
*(This page contains a figure/chart/image not captured in text)*

3.3.
Drone swarm path planning algorithms
Figure 3.11
The tracking policy panel
Note. To the left are the current available tracking policies, and their conditions. To the right
is the drone count that describes the number of drones the policy affect
Figure 3.11 displays the tracking policy panel. Here, the user can practice policy-based
control over the drones. Each policy has a name and a specified number of drones that it
affects.
These policies can currently not be altered by the operator, but are predefined. However,
the operator can alter the tracking policy of specific sensor objects.
Setting the tracking
policy to ignore means that the drone currently tracking that sensor object will release and
stop tracking it. Low priority is the go-to setting, meaning that when a drone starts tracking
a sensor object, it will keep doing so until that object leaves the defined search area. Neutral
means the same thing as low priority, except that two drones will be assigned to tracking
the object. Important and Very important both mean that the assigned drones will continue
tracking, even when the object leaves the defined search area. The difference between them
is that Important assigns four drones to that sensor object, while Very Important assigns five
drones.
3.3
Drone swarm path planning algorithms
The system has two different drone swarm path planning algorithms available. The first is a
Particle Swarm Optimization (PSO) algorithm, and the second is the Snake algorithm.
PSO was first created by Kennedy and Eberhart (1995) and is inspired by the collective
movements of birds and other biological agents. This means that no agent decides the move-
ment of the swarm as a whole; instead, coordination is emergent. The path any individual
drone takes is not a result of an explicit instruction. The drone's steering is decided by two fac-
23

---
**[Page 30]**

3.4.
Simulated setting
tors: its own historically best-known position, and the best-known position discovered across
the swarm as a whole with the help of a cost-function tied to each position.
In this implementation, The cost function is based on the simulated 3D world, where each
flight through a cubic 3D block updates the cost function with a negative increment for the
block’s position. Blocks where no drones have been present have a neutral value of zero, while
blocks where objects have been detected are assigned a positive value. This practically means
that drones will be dissuaded from revisiting places they have already been to, and is likely to
revisit places where objects have been detected.
To ensure that drones sometimes revisit positions they have already been to, the negative
cost decays with time, returning to the zero-value. The time this takes to do is configured
with the “Decay” parameter, which can be found within the HMI. Adjustments to the decay
parameter result in different search behaviors, ranging from the area being scanned only once
when decay is low, to repeatedly returning to the same 3D blocks when decay is high.
Similarly the size of the blocks that the algorithm uses can also be configured, and is also
present within the HMI.
The snake algorithm is essentially a parallel shifted line search algorithm. It divides the
simulated 3D world into smaller, contiguous cubic 3D blocks. These blocks define the search
area for the drones. The blocks are then arranged in a snake-like line of parallel line segments.
These segments are then divided and delegated to the different drones in the swarm. When
all blocks have been visited, the algorithm continues by finding the closest unscanned part of
the assigned line segment.
3.4
Simulated setting
The simulated setting is an area outside of Västervik, Sweden, around Gränsö slott.
The
setting includes three fictional security-sensitive sites. The area that the setting includes, as
well as the positioning of the sites, can be seen in Image A.
The site located to the north in Figure 3.12 was presented to the participants as an im-
portant military communications location and was called “The house”. The site located by
Gränsö Slott as a military storage unit called “the chateau”, and the site located to the east
as an important telemast called “the eastern cape”.
Within the setting, there are fictional boats, people, and cars moving along predefined
trajectories. These objects are most of the time animated to suit realistic movement patterns,
though rendering issues do occur. These objects serve the purpose of the noise produced by
everyday activity in natural surveillance situations.
Along the noise, injected sequences, only activated once during a given scenario, were
designed. These all included at least one vehicle, and an antagonist. Due to implementation
limitations, all antagonists have the same Unity prefab, i.e physical design, as well as the same
animations, meaning that they all look the same.
Each site has a no-entry zone around it of around 300 m. All scenarios also include a no-fly
zone above Västervik to the west in Figure 3.12.
3.5
Experiment design
The experiment performed have the form of user study tests, where each participant is given
a scenario, and their behavior observed.
The duration of the scenarios vary, in order to
accommodate the participant’s schedules. Participants that had more time for the execution
of the trial, were given the longer scenarios, while participants that had less time available
were given the shorter scenarios.
24

---
**[Page 31]**
*(This page contains a figure/chart/image not captured in text)*

3.5.
Experiment design
Figure 3.12
Map of the simulated setting
Note. The real world corollary of the simulated environment, with the fictional security sen-
sitive sites marked with the red dot. Screenshot taken from google maps.
3.5.1
Tasks and Scenarios
All scenarios enact surface surveillance of the peninsula, the surrounding archipelago and the
three security-sensitive sites. The goal of the operator in each scenario is to detect and report
any potential threats to the three security-sensitive sites as early as possible. To accomplish
this goal, the operator has 50 drones with autonomous swarming that can be steered through
the interface.
3.5.1.1
Scenario 1
Scenario 1 is 1h long. 40 minutes into the scenario, all sites are attacked at the same time by
one boat, and one antagonist each.
25

---
**[Page 32]**
*(This page contains a figure/chart/image not captured in text)*

3.6.
Participants
3.5.1.2
Scenario 2
Scenario 2 is 1 hour and 30 min long. 1 hour into the scenario, two boats and two antagonists
attack the site called the house. While this attack is happening, slightly after, the attack on
the chateau site is initiated by car.
3.5.1.3
Scenario 3
Scenario 3 is 1 hour long. Within the first 10 minutes, a military exercise is initiated, where
the warship docked by the chateau makes itself out into the waters to the east of the peninsula,
and back towards its original docking position. The exercise finishes at 40 minutes into the
scenario, 30 minutes after it started. After 50 minutes, an attack on the eastern cape site is
initiated.
3.5.2
Physical set-up
The experiment took place in a small meeting room.
Figure 3.13
Experiment setup
Note. The room where trials were performed
The room where the trials were performed can be seen in Figure 3.13Participants were
positioned at a table with a broad monitor and a keyboard. The researcher was behind the
participant to the right, and activated the injects and monitored the developments from there.
3.6
Participants
The study originally had 6 participants, but as there was one dropout, the final participation
number was 5 participants. The participants are all employees at GEISTT AB, and were
26

---
**[Page 33]**

3.7.
Procedure
selected through convenience sampling. Some participants have had involvement in developing
some part of the simulation environment used in the study, though direct experiences vary.
One participant had no previous experience with the system. All participants are male, and
26-50 years old. All participants come from a computer engineering background.
3.7
Procedure
The study was executed in 6 steps: 1) written consent, 2) introduction to the HMI, 3) trial
run, 4) Introduction to the task, 5) simulation, 6) post-experiment semi-structured interview.
In the first step, participants were welcomed and given the consent form. The consent form
can be found in its entirety in Appendix A.
When the participant had signed the consent form, the participant was given a written brief
introduction to the study, as well as given a written description of the HMI. This document
can be found in Appendix B.
After reading the HMI introduction, participants took part in a trial run. The duration of
it varied, as participants were given as much time as they needed to familiarize themselves with
the interface and try all the controls. The trial run was performed in the same environment
and in the same basic scenario as the actual simulation. Meaning that all the noise in the
later simulation was present in the trial run as well. Participants also had the chance to ask
the researcher for any clarification.
After the trial run, participants were given an introduction to the task based on their
assigned scenario. The task introduction for scenario 1&2 is the same and can be found in
Appendix C, and the introduction to scenario 3 can be found in Appendix D.
When they had read the instructions, the participants were asked if they were ready to
initiate the simulation. After confirming, the simulation started, and participants were asked
to talk aloud and describe what they were doing while they performed their tasks. The different
participants experienced their assigned scenario. The order in which injects were activated and
their timing in relation to each other can be found within the Injects timeline document in
Appendix E.
Following scenario completion, a semi-structured interview was conducted using principles
from the Critical Decision Method. Participants received access to video data collected during
the trial and were asked to reconstruct the scenario chronologically, identify key decision
points, describe the cues they attended to, the alternative courses of action considered, and
the perceived uncertainties. Probing questions were used to elicit cognitive and control-related
considerations underlying their actions.
3.7.1
Critical Decision Method
The critical decision method has been extensively used in HF research as a form of cognitive
task analysis in critical incidents, and has been described in multiple publications. (B. Crandall
et al., 2006) describe the method in depth. The method maps an incident based on a person's
experience through retrospection guided by probe questions. The main purpose of these probes
is to gain an understanding of the cognitive demands and the critical cognitive tasks of an
incident.
Normally, CDM is conducted by two researchers, but I performed it alone, and
filmed the interviews to enable me to access any information not noted during the interview
in hindsight.
A CDM interview is conducted in four “sweeps”. One sweep constitutes one pass over the
incident. Each sweep focuses on specific types of information, and builds on previous sweeps,
and thus iteratively deepens the interview’s questioning. The four sweeps are: 1) Incident
Identification, 2) Timeline Verification, 3) Deepening, 4) “What If” Queries.
The first step of incident identification entails identifying a suitable incident for analysis.
Usually this is a non-routine events, or challenging incidents that have the greatest potential
of unveiling cognitive demands that go beyond background- or routine procedural knowledge.
27

---
**[Page 34]**

3.8.
Analytical approach
Due to the nature of this study, an incident will not be chosen entirely by the participant,
instead the interviewee will have access to video-data recorded during the trail, and will based
on that choose a relevant episode. The participant will then be asked to briefly account for
the episode, from start to finish.
The second sweep, Timeline Verification, begins promptly after the first one. The aim of
the second seep is to expand the account given in the first sweep, verifying in what order events
happened. To facilitate this process, participants had access to video recording of the trail.
The main focus was on mapping points when the participant accessed relevant information,
or where their situational understanding shifted, when decisions were made and when the
participant acted. Timing of these different points were noted.
The third sweep, Deepening, entails asking probing questions to understand the cognitive
processes and states of the participant. Participants were asked about what information they
used to make decisions, their goals and priorities at a given moment, strategies and methods
used, alternative courses of action, relevant previous experiences or knowledge, understanding
of consequences, how they imagined events to unfold and other predictions as well as how sure
they were of their decisions. An extended list of example probes can be found in Appendix F.
The last sweep consists of posing hypotheticals based on the incident. Key aspects of the
incident are used to hypothesize about what would have changed had that aspect changed,
extending the interview beyond the specific episode. A specific focus was given to hypothetical
scenarios about technology malfunctions, like a lack of coverage, malfunctioning sensors, or
damaged drone-steering systems. The prepared hypotheticals can also be found in Appendix
F.
3.7.2
Data collection & Data handling
During the simulation, a screen recording was made of the participant's screen, and their
voice was captured through a webcam. The screen recording and web-cam recording were
performed through X software. The interview was recorded with an external mic connected
to the researcher's computer. The audio software used was Audacity.
The video footage was stored locally on a laptop during analysis, as well as interview audio
recordings. Interview audio was first transcribed with the use of Word’s AI transcription tool,
and then revised manually. The transcriptions are rough in the interest of time, and sometimes
need to be supplemented with the audio to be understandable.
3.8
Analytical approach
The material was analyzed based on common practice within CDM(B. Crandall et al., 2006).
What stands out is the implementation of video-footage into the approach, this allows for
verified and detailed timelines that does not rely solely on the participants recounting of
events.
The first step of analysis was creating written timelines of each trial. This was done by first
watching and annotating the video-footage, noting down any important sequences, decisions,
or observations. As the participant were asked to talk during their trial, their commentary
was also noted. These observations were then unified into written accounts.
When the video footage had been reviewed, transcriptions of interview data were tagged
based on interesting sequences. These could be reflections about participants' abilities, feelings,
described through processes not voiced during the trial, and explanations of behavior. These
observations were then consolidated with the written timelines, enriching the account with
cognitive processes and subjective considerations. These finished timelines can be found in
Appendix G. These written timelines then became the basis for all further analysis.
The second step of analysis was overviewing the written timelines. This was done with two
passes. In the first pass, methods of control and surveillance were identified and tagged. In
the second pass, control issues and frustrations relating to control were tagged. These control
28

---
**[Page 35]**

3.9.
Ethics
methods and control issues were than added into a Figma board, where the third step of
analysis could commence.
In the third step, multiple analytical activities were performed iteratively. The goals of
this analytical step were to identify the activities that the participants performed, how they
performed them, and when these activities were less effective than they could have been.
Control methods and issues were compared across participants.
Furthermore, the control
issues were grouped into themes.
This analysis was then used to support reasoning about meaningful human control and to
what extent it was maintained throughout interaction. Connecting the different issues to the
levels within the expanded CHOF framework presented in the Related Works section. The
issues in doing this were also noted.
3.9
Ethics
The study adheres to the recommendations of good research ethics and practice described
in The European Code of Conduct for Research Integrity to the best of my abilities.
Participants were asked to give their informed consent before participation and could withdraw
it at any time. None of the participants' safety was ever in jeopardy, either mental or physical.
Data was anonymized through numbering participants and transcribing audio recordings. No
personal data was stored, except for these audio recordings.
3.9.1
AI usage
Beyond the usage of words transcription tool described in Section 3.7.2, AI was used sparingly
in the creation of the report. Claude was used to aid in structuring the text. Consensus, along
traditional methods of search were used to find suitable references. AI was never used for any
part of the analysis, and the words in the report are my own.
29

---
**[Page 36]**

4
Results
The first section of the results provides a brief overview of the different participants’ time-
lines, which can be found in Appendix G. After this, the different alerts that the participants
experienced are outlined. The next section of the results describe human control within the
system. Based on these results the different identified control issues are presented in Section
4.3. These issues are then mapped to the consolidated MHC framework presented in Section
2.1.2.3.
4.1
Timeline summaries
Participant 1 took part in scenario 1.
Participant 1 was the only participant who received
no alert for any injected breaches, in this case 3. His trial has one primary phase, which is
surveillance, and three smaller planning phases. He does not perform any large re-planning
sections. The interview of this participant was 1 h 1 min 56 sec long.
Participant 2 took part in scenario 1. Participant 2’s trial is characterized by repeated
frustrations with the limitations imposed by the HMI, stopping him from making decisions.
These frustrations permeate all phases of the trial.
These include 1) Planning, 2) Active
Surveillance, 3) re-planning, 4) Inactive surveillance, 5) the incident. The interview of this
participant was 1 h, 3 min, 6 sec long.
Participant 3 took part in scenario 2 and was mostly characterized by restlessness, which he
showed through experimenting with the interface. The trial can be divided into 5 phases. 1) a
short planning phase, 2) surveillance, 3) increased restlessness, 4) further increased restlessness
and play, and 5) the incident. The interview of this participant was 1 h 20 min 35 sec long.
Participant 4 took part of scenario 2. Usually this entails the chateau, and the house to be
attacked at the same time, but due to a technical malfunction with the simulation software the
chateau was never attacked. This participants trial is marked by extensive re-planning periods
trying to improve the drones behaviors. Participant 4’s trial can be divided into 6 different
phases/activities: 1) Planning, 2) Area Familiarization, 3) Re-Planning, 4) Overviewing &
Improving Drone Behavior, and 5) The incident. The fourth phase is the most extensive one.
The Interview with this participant was 1 h 18 min 38 sec long.
Participant 5 took part in scenario 3. This participant was the most unfamiliar with the
interface. This scenario is also different from the others due to the military exercise initiated
10 minuted into the trial.
This divides the trail into a 10 minute long pre-exercise, con-
30

---
**[Page 37]**

4.2.
Human control within the system
sisting primarily of planning, a 30-minute-long exercise phase, a surveillance and re-planning
phase and lastly an incident phase before returning to the normal surveillance patterns before
terminating the trial. The interview of this participant was 1 h 28 min 25 sec long.
4.1.1
Alerts during the trials
Most participants experienced multiple alerts and incidents during the trial.
Table 4.1
Alert Reception and Incident Detection Across Participants
Participant
Lost-Tracking Alerts
Incident Alerts
Incidents Identified
P1
None
None
0 of 3
P2
Chateau (person)
All incidents
3 of 3
P3
Chateau (person)
1 of 3 (Scenario 2)
2 of 3a
P4
Eastern cape (person)
1 of 2
1 of 2
P5
Chateau (person), fields (person)
1 of 1 (Scenario 3)
1 of 1
Note. Incident counts reflect only those active during each participant’s trial.
aParticipant 3 identified a second incident through the map without receiving an alert.
The alerts and the incidents experienced by the different participants can be seen in Table
4.1. All participants, except participant 4, received a lost-tracking alert related to the disap-
pearance of a person close to the chateau, which was built into the scenario. Participant 4
received another lost-tracking alert connected to a person around the eastern cape as a result
of placing the sensor objects tracking policy to very important. Participant 5 received an
additional lost-tracking alert later in his trial related to the disappearance of a person walking
the fields in the middle of the peninsula.
Notably, Participant 1 received no incident-related alerts whatsoever, as his drones failed
to register the relevant sensor objects entirely. The other participant with the same scenario,
Participant 2 received alerts for all incidents. Participant 3 stands out as the only participant
to identify an incident without receiving an alert, doing so through the map.
4.2
Human control within the system
Control within the system can be described in levels of increasing specificity. The first level
will be why participants are performing the identified activities, i.e., the task and its relevant
goals. The second will be what they are doing on a high level, including the panels used
in the HMI, the activities performed, and the phases of the trials identified during the CDM
interviews. The third, and last level will be how participants perform the activities outlined
in the earlier section and their varied methods.
As a basis is the Figma board in Figure 4.1 relating to the methods and processes partic-
ipants performed. The board allows for comparison of methods across participants, as well
as reasoning about the number of re-planning actions participants make. Every instance of
judging a sensor object has not been noted down, as it did not seem relevant. However, every
re-planning event identified was noted. The results will refer to the board when relevant.
4.2.1
Why
The overarching role of the human within the system is a high-level form of control. The
human is tasked with an overview of the available sensor objects, directing the drones to areas
of interest and changing the tracking policy of especially interesting sensor objects. When
incidents happen, they are expected to report these incidents to higher command (in this
31

---
**[Page 38]**
*(This page contains a figure/chart/image not captured in text)*

4.2.
Human control within the system
Figure 4.1
Figma Board Collecting the Methods and Processes Across Participants
Note. Each box correlates to participants 1–5 and is numbered based on the related participant.
The methods and processes identified can be found within the bubbles, which are color-coordinated
according to the activity they belong to: yellow indicates planning processes that are tactical in
nature, red indicates planning processes related to improving drone behavior, green indicates sensor
object judgment and threat detection, blue indicates accessing the camera, and pink indicates alert
handling. Within each box are also the zones that the participants used at the beginning and at the
end of the trial.
instance, the researcher). These results are not identified based on the board in Figure 4.1,
but are a direct consequence of the task itself.
The goals of the participants are largely uniform. The identified sub-goals that participants
shared are: 1) controlling drone distribution and zone coverage, 2) judging sensor objects
reasonably and safely, 3) handling alerts quickly, and 4) tactically distributing drones. These
goals largely correlate to the activities found in the board, but since accessing the camera is
not a goal in and of itself, but rather a means to an end, it has been excluded.
4.2.2
What
To perform these responsibilities, the participants use the available HMI. The participants use
the zone-panel to define zones, the plays-panel to define missions and deploy drones to zones,
the map, as well as the sensor object-lists within plays to identify and surveil sensor objects
and gain access to live drone footage. The alerts panel and backend system, as well as sensor
object qualities displayed on the map and camera feed, are used to judge if sensor objects
constitute threats or not. No participant referred to the event panel of the event displayed
during the trials, likely meaning that it was the only panel not used by the participants. The
resource panel was sometimes referred to by the participants in noting when a swarm had
been retrieved from a canceled mission, or when commenting on its design, but it varied across
trials.
32

---
**[Page 39]**

4.2.
Human control within the system
The activities of the participants are, similar to their goals, largely uniform. The identified
activities, which can also be found on the board in Figure 4.1, are: 1) accessing a specific
drone's camera feed, 2) controlling drone distribution and zone coverage, 3) judging sensor
objects, 4) handling alerts, and 5) tactically distributing drones. These different activities are
performed in an alternating manner, where controlling drone distribution and zone coverage
is sometimes interrupted by assessing sensor objects, or general surveillance is interrupted by
an alert, moving the participant to threat detection.
When overviewing the timelines, it becomes clear that the trials are always initiated by a
planning phase, where the foundational areas of interest and plays are created. In all trials,
except one, these initial zones are later iterated on a re-planning phase, as the participant
familiarize themselves with the task, though the duration and frequency of these phases varies
largely. All trials have some type of surveillance phase, where the participant is primarily
assessing different sensor objects. All, except one trial, also has an incident phase where the
drones catch and alert for intrusions into the no-entry zones around the security-sensitive sites,
prompting the participant to track the threat.
4.2.3
How
How participants performed different activities within the system will be presented based on
the activities identified in the previous section.
4.2.3.1
Accessing the camera feed
There are three primary methods that the participants use to access the camera, which different
participants use in different situations and to different degrees. One is clicking on the sensor
objects presented on the map and then scrolling to the relevant play in the plays panel to be
able to press the camera button on that play. The participants primarily using this method
were participants 1 and 2. These participants also barely used the second method, which was
to use the drone and tracking symbols in the plays panel. The participants primarily using
this method were participants 3, 4, and 5. They used this method to be able to quickly look
through all sensor objects within a play. Sometimes, however, the last method was used, which
was using the sensor object list to identify a specific object by clicking and selecting it, and
gaining access to camera footage of it by pressing the camera button.
4.2.3.2
Judging sensor objects
Participants made differing choices regarding the tracking policy of sensor objects. Participant
1 placed no objects in movement to ignore. This could possibly have been influenced by the
participant’s placement of zones, missing a lot of the noise in the scene, thus having relatively
few identified sensor objects to surveil. The only object that he ignores is the warship docked
in the harbor, which he judges to be friendly.
Participant 4 outlines his reasoning in choosing to ignore, increase the tracking policy,
or pay more attention to a sensor object. He explains that the most important factors are
proximity, direction, context, and established patterns of behavior.
This last factor only
becomes available to him when he has established a status quo; it could not have been used
at the beginning of the trial.
He uses the pool boy object placed close to the chateau as an example of his reasoning:
He was bathing, but it was. Yeah, but then fairly close. You don’t know what he
has in that backpack like, so he still like- just that, even if he looks innocent and
isn’t doing anything right now and is just walking around there it can just take
like a minute for him to react and go (Participant 4, Interview)
Participant 5 gives another perspective on the reasons for altering the tracking policy of sensor
objects. For example, during the trial, he becomes increasingly suspicious of the sailboats
33

---
**[Page 40]**

4.2.
Human control within the system
outside the house. He identifies multiple different boats, but chunks them together as one
boat. Raising his concerns to me, he says that the sailboat outside the house is very suspicious,
since it has driven past it multiple times.
However, this situation happened early on in the simulation, and during the interview, he
explains that he notices objects walking around in circles and so on, taking him slightly out
of the situation.
It was like a bit of roleplay, like, because I understand the technology in that the
cars turn around and it would have been weird if it was for real. Yeah like, a car
drives and turns and three people just walk in a circle around a protected object.
(Participant 5, Interviews)
He also describes how that made him take into account the nature of the experiment when
judging sensor objects. Therefore, it’s likely that the recurrence of sensor objects became less
of a factor at the end of the experiment.
4.2.3.3
Handling alerts
Consistent across all trials and alerts is an initial attempt to understand what originated the
alert. Participant 1 did this by first reading the alert card, but most participants' first objective
was receiving a direct camera view of the sensor object that caused it. Also, the participants
either zoom in and click on view within the alert card to get a closer map view of the alert.
Thus, no participant keeps track of multiple alerts at once. Only participants 3 and 4 identify
incidents through the map. If specific sensor objects connected to the alert are identified,
then the participant moves to place that object as very important. Only participant number
4 successfully placed the getaway vehicle’s tracking policy to very important, but participant
2, 3, and 5 placed the relevant individual’s tracking policy to very important, but lost track
of the relevant sensor objects when they disappeared into a getaway vehicle.
4.2.3.4
Tactical distribution of drones
All participants, except one, start the planning phase by defining one zone for each security-
sensitive site. The outlier here is participant 4, who creates a large zone covering both the
chateau and the house, since these sites are closer together than the eastern cape. After about
7 minutes, he decides to re-plan and have one zone for each site, like the rest of the participants.
The sizes of the zones vary, where participant 1 has the largest overall zones, and participants
2 and 5 have the smallest zones.
The participants’ zones can be seen in Figure 4.2. Participant 3 was the only participant to
begin by placing larger zones outside of the immediate zones around the security sensitive sites,
though participants two and one also added larger zones around the security sensitive sites.
Participant one motivates the choice by explaining that he wanted to have more of an overview
of the incoming sensor objects, and participant two realizes that there are sensor objects just
outside of his zones and therefore decides to draw a new zone around his security-sensitive
sites that are larger.
This is in direct opposition to the reasoning of participant 4, He decides to redraw his
original larger zone covering both the house and the chateau into two zones because the larger
zone caught too much noise. At another point, he realizes there are sensor objects outside of
his zone, and is about to draw a new zone to catch them, but decides against it because: “the
zones were drawn that way for a reason”, likely reasoning that he will catch them when and if
the sensor objects move towards the sites.
In regard to the shape of the zone, participants four and two take into account or note
the available access points and roads. For example, participant 4 notes it as a reason for
re-planning the shape of his zones. Similarly, participant 2 explains that he drew the original
34

---
**[Page 41]**
*(This page contains a figure/chart/image not captured in text)*

4.2.
Human control within the system
Figure 4.2
Participants’ Initial Zone Configurations
Participant 1
Participant 2
Participant 3
Participant 4
Participant 5
zones based on the roads around the sites. However, participants have limited environmental
knowledge, as participant 4 points out.
Participants also make varying decisions in regards to dividing drones across zones. Par-
ticipant 2 sends all his zones out from the start, deciding the number of drones per zone based
on the size of the zones. Participant 1 sends out 10 drones
The different drone distribution and if participants hold drones in reserve have repercussions
for how dynamically participants can alter their plays, which will be shown in the next section.
4.2.3.5
Controlling drone distribution and zone coverage
Participants spent varying amounts of time trying to fix and alter the distribution of drones,
and increase the zone coverage. However, all participants noted both the flocking behaviors of
the drones and coverage issues within their trials, and took some action to address them.
The most common methods of addressing clustering and coverage issues include increasing
the number of drones deployed to a specific zone with poor coverage, altering the search
algorithm for the play of a zone, and adjusting the decay of a specified search area. Participants
5 and 2, took the least number of actions to alter flocking and clustering behavior. Participant
5 altered the search algorithm once to snake on one of his plays. Similarly, participant 3 only
increases the decay of one of his zones during his trial to 160 from 30. Participant 1 increases
decay on two of his zones from 30 to 300 when he realizes that the drones are flocking inland in
his zones, leaving the waterways unpatrolled. He also cancels an ongoing mission, waits until
the drones are retrieved, leaving an entire area of interest uncovered, and then creates a new
play that contains more drones. In the interview, he reasons that it would have been better
first to create a new play and then cancel the ongoing one to maintain coverage, a tactic
35

---
**[Page 42]**

4.3.
Control failures
participant 4 used multiple times. This tactic, however, relies on having drones in reserve,
which becomes a problem for both participants 4 and 2.
Participants 2 and 4 exhibit the most unique control behaviors within this activity. Par-
ticipant 2 deployed all his drones at the start of his trial and kept them deployed for most of
the trial. This left him with no option but to pull in one of his missions, then send out a new
play when he wanted to alter the number of drones within a zone, or change which search zone
to use. This is an issue that the participant notes multiple times, leading him to postpone
altering his zones multiple times, which is similar to all other participants who also listed
losing coverage as a risk when altering plays. What is special about participant 2’s behavior
is how he uses his zones. This participant first had smaller search zones around his sites, but
later redrew larger ones around them. It is within these larger zones that he notices that the
drones are flocking inland, leaving the no-entry zone around the house site unpatrolled. To
combat this, he first identifies that he needs drones, since he has none in reserve. Therefore,
he decides to cancel one of his missions, wait until it’s retrieved, and then send out a new play
to the same zone but with fewer drones. He then sends the remaining drones to his original,
smaller search area around the house, ensuring that the no-entry zone is somewhat covered.
He thus has one smaller internal zone, around the no-entry zone, overlapping with a larger
search zone.
Participant 4 had the most extensive re-planning phase, using multiple methods with re-
peated attempts to improve swarm behavior.
Participant 4 had drones in reserve at the
beginning, but created new plays for the same search zones to increase the number of drones
when he noticed they were not properly covered, leaving him with only five drones in reserve.
This also led him to have two ongoing plays within the same zone, a unique situation across
trials. When still not satisfied with the flocking behaviors of the drones, the participant tries
altering the algorithm of his play multiple times. Afterward, he realizes that he has two swarms
in the same zone, and reasons that it might affect how well the drones coordinate. This leads
him to cancel one of the plays in the search area around the Eastern Cape. Since he judges
he does not have enough drones in reserve to send out a larger mission to the eastern cape
zone, he waits for the drones to be retrieved. Then, he sends out a larger mission and cancels
the ongoing one. Showing how he reasons about his resources and ensures that the area stays
actively covered as much as possible.
Participant 4 also experiments with the usage of decay to improve swarm behavior. In
the interview, he explains that he has seen video illustrations of decay within the algorithm
during internal demos, and reasons that decreasing decay should lead to the drones spreading
out more. During the trial, however, he realized the opposite was true.
4.3
Control failures
The participants experienced different issues and commented on varying problems. Often,
they corroborate each other in that, where one participant's control was affected, another
participant might comment on the same issue without facing any problematic interactions
because of it. In other instances, the control issues are connected to the method participants
used to perform the system activities. The issues identified are grouped into six themes: 1)
Camera feed issues, 2) Overview, 3) Zones and plays functionality, 4) Tracking behaviors,
5) Clustering, coverage, and controlling swarm behavior, and lastly 6) Alerts and situational
awareness during incidents.
The identified themes are merged versions of the 16 control issue themes identified in the
Figma board related to control issues found in Figure 4.3.
4.3.1
Camera feed issues
Participants 2 and 3 both experienced issues with the limited functionality of the live camera
feed. Participant 2 was trying to survey a sensor object, but the drone was placed too far away
36

---
**[Page 43]**
*(This page contains a figure/chart/image not captured in text)*

4.3.
Control failures
Figure 4.3
Control Issues Identified by the Participants
Note. Issues are color-coded based on the participants: pink for Participant 1, purple for
Participant 2, blue for Participant 3, teal for Participant 4, and green for Participant 5.
Arrows connect related issues, either thematically between participants, or as connections
between related issues between themes. Suggestions from participants are placed outside of
the thematic boxes.
37

---
**[Page 44]**

4.3.
Control failures
from the objects, which made it hard for him to see them, and he commented that he would
have liked to be able to zoom. Participant 3 experienced another limitation as he wanted to
look around the drone's immediate surroundings, but could not angle the camera as he wanted.
The inability to zoom, as well as angle the drone camera, is a control limitation.
Participants also commented on the fact that the map did not show which drone they were
accessing when using the camera feed. This was primarily an issue for Participant 2, as he
identified sensor objects within the camera feed that his deployed drones had not identified.
This made him want to explore that area further, but since he did not correlate the camera
feed and the map, he was unable to identify where on the map these sensor objects were,
stopping his inquiries before they started. No other participants were directly limited by this,
but it was noted by participant 4, who compared the geography of the camera feed to the map
to identify where the drone was pointing its camera. In the interviews, he also commented
that some type of corollary or marking of the angle of the perceptive field of drones would be
beneficial.
There were repeated and frequent issues with accessing the camera feed of specific
drones.
But some participants struggled more than others, depending on the method they
used. Participants 1, 2, and 3 primarily used the map to access the cameras of specific drones
(See 4.2.3.1). This came with two primary issues. The first issue is trying to click on moving
objects, as participants would sometimes miss, and would have to wait for the object to stop
before being able to access the camera. For example, during the incident phase, participant
2 was able to identify a person running towards the sensitive site, but missed the moving
sensor object dot on the map multiple times, before accessing the wanted camera feed when
the person stopped. Secondly, accessing the camera feed through the map took an unneces-
sarily long amount of time. The participants using the tracking icons could, through one click,
switch between different drones, while participants using the map required multiple clicks and
scrolling. When scrolling, participants had issues with identifying which play contained the
sensor object in question and the camera button they needed.
The main method of Participants 4 and 5 was using the tracking icons in the plays panel
to look at sensor objects through the camera feed, occasionally using the sensor object list
when accessing specific sensor objects. This primarily created issues in differentiating between
sensor objects if there were multiple of the same type.
4.3.2
Differentiating sensor objects
Differentiating sensor objects was not only an issue when accessing the camera.
Actually,
the clearest example of this does not occur when accessing the camera feed, but rather when
changing the tracking policy of a specific sensor object. During the incident phase of participant
4, he first fails to place the wanted boats tracking policy, since he does not differentiate between
the two boats in the sensor objects list. Participant 5 does something similar during the later
sections of the military exercise taking place during his trial. He wants to ignore a boat within
his MISSION zone, but mistakes the row in the sensor object list, and instead alters the
tracking policy of the warship engaged with the exercise, leaving it un-surveilled and removing
it from the map.
Issues in differentiating sensor objects also affect the situational assessment that partici-
pants make. Participant 5 mistook different sailboats, viewing them both on the map, in the
sensor object list, and in the camera feed as the same boat, making him highly suspicious
of a circulating sailboat that did not exist. Participant 3 had a similar scenario; Around 10
minutes into the trial of participant 3, notes a car moving away from the chateau on the map.
He comments that “now the car is leaving, or it’s another.. or?”, “the car” refers to the white
car parked in the parking slot outside the chateau. He then sees that a white car is still parked
in the parking slot in the same spot and concludes that two white cars changed places. He
comments that this is highly suspicious and marks the parked white car as very important.
38

---
**[Page 45]**

4.3.
Control failures
In reality, neither of the cars was a threat, and they also did not change places, marking an
incongruent situational assessment.
4.3.3
Alerts and Situational awareness
The faulty situational awareness of participants reaches beyond issues of differentiating be-
tween sensor objects. It was a recurring issue when handling alerts, as participants had a
limited understanding of the system. This limited understanding bears its head again when
assessing the participants’ ability to overview and their environmental understanding. Lastly,
it can also be seen when participants are assessing incidents, as no clear image of the events
that happen on the ground.
4.3.3.1
Handling alerts
The handling of alerts was a recurring challenge for the participants.
Both Participant 5
and Participant 4 outline that they were confused by the alert card during the first alert.
Participant 4 further describes that he had not seen it during the practice run, and found
it unintuitive. His reasoning about how the alert card works also displays how his confusion
persisted even at the end of the trial.
It was like a little unintuitive with the actual, because I thought that if I ac-
knowledge then it disappears (the alert card), but you had to click on it and then
acknowledge.
No, but I, it’s a bit of small things and shit...
...Also like here,
view for me, then this one opens, decrease and so. I click on view, then this one
(extended view) should pop up. But view I think centers on... (Participant 4,
Interview)
This quote illustrates, how even at the end of the trial, it is still unclear to Participant 4
exactly how the alert card works. He is still trying to figure out exactly how it works.
Similarly, participant 2 explains how he abandoned alerts when the path of action became
unclear. On his first alert, he would have liked to steer the drone to look closer around the
alerted area, but due to manual steering being unavailable and no other options for further
inquiry existing to him, he was forced to abandon the alert.
Participant 2 seems to have had continued issues during the later parts of the trial. He
seemed confused about how he was supposed to handle the alerts, what his role was, and the
role of the researcher.
4.3.3.2
Overview
Participants sometimes had lacking overview. Participant 3 raises concerns during the surveil-
lance phase of his trial, commenting that he is concerned that he might miss something while
being zoomed in on a specific site. This concern is a reality in the trial of Participant 2.
Participant 2, does not register the remainder of the alerts before the incident he is seeing has
passed, and he zooms out to see the rest of the map. His following confusion then connects us
back to the issue of confusion in handling alerts. Once again, the participant seems confused
as to what he can do, as he can see no sensor objects on the map, and has no way of exploring
the different alerts he’s presented with. Thus, the issue of a lack of overview couples with the
previous issue of lacking an actionable path forward.
The overview issue again becomes relevant in a tactical sense. Participant 4 explains that
he has limited environmental knowledge. He knows what the environment around the chateau
looks like, but he has never seen the other two security-sensitive sites, either in reality or
during the trial. He also has no knowledge of what fills the empty spaces on the map, as he
only has the roads to go on. He explains that this might have altered how he drew his zones,
which is likely true for the participants as well. This, together with the confusion in relation
39

---
**[Page 46]**

4.3.
Control failures
to alerts, paints a picture that the participants' lack of training had a negative impact on their
ability to control the drones.
4.3.3.3
Situational awareness during incidents
As outlined earlier, not all participants received an alert for the incidents that occurred, which
stands as a direct technical limitation to the participants’ situational awareness. However, even
when receiving proper alerting and handling the incident as expected, situational awareness is
limited. Participant 4, was the only participant to follow both getaway vehicles, making him
one of the more successful participants in his surveillance. When prompted to describe what
he thinks happened during the incident, he says:
I don’t know, that’s a good question. I assume like that there was a boat here
now that I saw that maybe was dropping off, but it feels very. I don’t know that
it dropped off the one (the antagonist) who blew up the house and that this one
(the other boat) is an escape route, and like, but. I have a hard time, it feels very
strange to have two boats in the same or on two different sides of the peninsula.
(Participant 4, Interview)
Here, Participant 4, illustrates the diﬀiculty of fully understanding what is happening based on
the information he received, even in hindsight, when he has had time to review the simulation
footage.
Participants also missed relevant information presented to them. When participant 3 is
handling the alert, the second boat can be seen approaching on the map, which he does
not note.
However, he does catch the person running towards the security-sensitive site.
Interestingly, no alert is raised by the system when this person enters the no-entry zone.
Possibly, constituting another technical flaw that may limit situational awareness.
4.3.4
Tracking behaviors
Beyond the apparent misses of identifying and alerting for possible intrusions into the no-entry
zones, there were recurring issues with how tracking was handled within the system. Drones
would repeatedly identify the threatening boat or vehicle connected to the incident, identify
that a person has jumped out of it, but instead of following the person, it keeps tracking the
now stagnant vehicle, leaving the person running untracked. This happened to Participant 3
during the incident phase: when a boat arrived at the site, dropping off a person who was left
untracked, as well as to participant 4: when the second boat arrived at the house and dropped
off a person.
Tracking behaviors and the inability to switch between interesting sensor objects also be-
came an issue when the antagonist disappeared into the getaway vehicle. Participants 2, 3,
and 5 experienced similar issues. They all correctly identified the threatening antagonist and
increased the tracking policy of the related sensor object. However, when he disappeared into
the car or boat, the system would note that the getaway vehicle was a sensor-object, but not
track it. This seems like the primary limiting factor for participants 2, 3, and 5 in successfully
tracking the getaway vehicle.
4.3.5
Clustering, coverage, and controlling swarm behavior
The drones often displayed unwanted flocking behaviors or did not cover the intended area.
These were behaviors that the participants repeatedly tried to improve. As noted earlier, all
participants noted the flocking behavior and took some action to improve it. Though they
sometimes felt like their efforts were successful, as in the case of participant 5, when he altered
the swarming algorithm to snake from PSO, it is hard to verify that it is the case. Participant
4, who took the most actions to fix the swarming behavior with inconclusive results at the
40

---
**[Page 47]**

4.3.
Control failures
end of the trial, but reasoned that in the future, he could have done better because he now
understands decay and would increase it to have the drones spread out more.
However, for the participants who increased decay rather than lowered it (Participants 1
and 3), it is also unclear whether this was the desired result based on the data. This is a
serious issue for control as it puts into question if participants can achieve the desired effects,
and whether controls have the function participants think they do.
Participants displayed multiple signs of lacking an understanding of the system, sometimes
causing distrust in it. Beyond commenting on disliking the flocking behavior of drones, par-
ticipant 2 also said that he did not really trust the coverage stat displayed in the plays panel.
Explaining that coverage is said to be high, but that he did not feel like the area was cov-
ered due to the clustering behaviors. Participant 4 also wonders at how coverage is actually
calculated, to figure out if it matches the reality, and directly states that ”I felt like I never
really got a grip of it” (Participant 4, Interviews) regarding the swarms behavior. He also
explains that he has no clear understanding of the algorithms, though the fact that flocking
behaviors exist makes sense to him since PSO is inspired by the behavior of birds. However,
other emergent behaviors like collecting inland in the zone or flying in lines did not make much
sense to him. Similar sentiments are reflected by Participant 5, who wonders how algorithms
work in the context of setting an untracked sensor object to very important: Does that lead
to allocated drones going in that direction to see to them? This is not the case and illustrates
the misunderstandings that are frequent during the trials.
4.3.6
Zones and plays functionality
In many instances, participants expressed that the control offered to them was lacking in
functionality. Most directly, it was regarding the zones and plays panels that lack the func-
tionality to delete zones. Direct remarks were made by participants 1 and 2, but this affected
all participants to some extent, as all expected to be able to delete zones, and then assessed
when they realized the functionality was not available. Direct remarks were also made on the
inability to alter created zones by participants 1, 2, 3, and 5. Most express a desire to alter
zones, which they are unable to.
Participants also highlighted the lack of functionality regarding the modes of control avail-
able to them. Participants 1, 2, and 5 all made direct comments on the lack of manual control.
Participants 1, 2, 4, and 5 also commented on adding ways of highlighting important areas
within a zone, to make the drones pay more attention to it. Reflecting a desire for further
control of the drones.
There were also indirect issues with the design of these panels identified when comparing
mistakes across trials. Participants 3 and 4 both mix up zones when creating a new play,
sending drones to the wrong zone, indicating that the design of this section of the plays panel
might increase the risk of this. Similar issues also exist across participants. Participant 4
cancels the wrong play, connected to an unintended zone, and Participant 1 renames the
wrong zone without realizing it, leading him to also send drones to the wrong zone. It thus
seems like keeping track of the zones is a repeating challenge for the participants.
4.3.7
Control Failure summary
In summary, 32 control issues were identified in the study. They have been collected into a
list for ease, and numbered in the order that they appear in the results. The identified control
issues were:
1. No ability to zoom the camera view in the live camera feed
2. No ability to angle or pan the camera in the live camera feed
3. No map-to-feed correlation (impossible to tell which drone is being viewed or where it
points on the map)
41

---
**[Page 48]**

4.3.
Control failures
4. Diﬀiculty clicking on moving objects on the map to access their camera feed
5. Accessing the camera via the map required many clicks and scrolling
6. Hard to identify which play contained the relevant sensor object and camera button
when scrolling
7. Identical labels for sensor objects of the same type caused mix-ups when accessing the
camera feed
8. Mix-ups when changing tracking policies, leading to the wrong object being altered
9. Mistaking one sensor object for another led to faulty situational assessments
10. Alert cards were confusing and unintuitive
11. No clear path of action after raising an alert
12. Manual steering was unavailable, leaving no way to investigate an alerted area further
13. Unclear role definition after raising a concern with the researcher
14. Risk of missing events when zoomed in on a specific site
15. Limited environmental and tactical knowledge of the surveilled areas due to a lack of
training
16. Not all participants received alerts for incidents that occurred (technical limitation)
17. Relevant information shown on the map was sometimes missed during incidents
18. No alert was raised by the system when a person entered the no-entry zone (possible
technical flaw)
19. Drones continued tracking stationary vehicles instead of following persons who exited
them
20. Get-away vehicles were registered as sensor objects but not tracked
21. Unwanted flocking and clustering behavior
22. Uncertainty about whether control inputs (e.g. adjusting decay, switching algorithm)
had the intended effect
23. Distrust in the coverage statistic displayed in the plays panel
24. Limited understanding of how the algorithms work and why certain emergent behaviors
occur
25. Misunderstanding of how setting a sensor object as ”very important” affects drone allo-
cation
26. No option to delete zones
27. No option to edit or alter created zones
28. No manual drone control available
29. No way to highlight important areas within a zone to direct drone attention
30. Panel design possibly caused participants to send drones to the wrong zone when creating
a new play
31. Panel design possibly caused participants to cancel the wrong play
32. Panel design possibly caused participants to rename the wrong zone
42

---
**[Page 49]**
*(This page contains a figure/chart/image not captured in text)*

4.4.
Mapping between MHC and control issues
4.4
Mapping between MHC and control issues
The issues of control were mapped to the model presented in Section 2.1.2.3. The result will
be presented based on the layers of this framework.
4.4.1
Technical Layer
The first layer is the technical layer.
This layer will be presented based in the temporal
dimension of the framework. First presenting the pre-deployment conditions, and then the
conditions within the during-deployment section and lastly the post-deployment section.
Figure 4.4
The Technical Layer of the Model of MHC Used
Note. Shows the technical layer and the conditions of each temporal stage in it.
4.4.1.1
Before deployment
Both of the pre-deployment conditions seen in Figure 4.4 of MHC are compromised in the
system.
Most apparently, participants of the study do not have a clear understanding of
the system (condition 2: The operator has suﬀicient understanding of the system, the task,
and the environment).
There is multiple technical confusion, such as how algorithms and
decay affect the behavior of drones. There were also cases of confusion with the interface,
especially early in the trial, such as how the alert cards work. Participant 4 and 5, clearly
state that their understanding of the system develops during the trial in interviews. Participant
4 explains that he is gaining an understanding of what different control settings mean, while
Participant 5 explains that he had to figure out the allowed shape of zones, how tracking
worked, and other basic functionality. This indicates that the participants can not be seen
as experts and that they were poorly prepared for their task. Furthermore, the environment
was specifically brought up as a limiting factor to the ability to plan suitable zones for the
task. The task was also ill-defined in some respects, as participants had no clear path of action
during alerts, and were unsure what to do after notifying the researcher of threats. Based on
these understanding gaps, it seems like the lack of scaffolding around the task was as much of
an issue as the activities of the task itself. Scaffolding like clear SOPs, proper education, and
predefined protocols could go a long way toward addressing these issues. The lack of guidance
was, in and of itself, a clear limiting factor to understanding.
On a similar note, the lack of strategic and tactical theory is likely to have affected the
outcomes of the system. Participants used varied zone designs, some of which are likely to
be more effective than others. The question of whether proper constraints were set on the
43

---
**[Page 50]**

4.4.
Mapping between MHC and control issues
system before the trial thus comes into question (condition 1: Proper constraints have been
set on the system). When zones and plays are defined, little to no interaction is necessary with
the system; these are strategic decisions rather than dynamic, operational ones. Leaving this
decision to individual operators may be unsound, as having well-planned and tactically sound
zones could likely go a long way in improving the system's outcomes.
4.4.1.2
During deployment
The principles within the deployment section of the technical layer are the most connected to
direct control of the system and can be found within Figure 4.4.
The first principle is that the operator has freedom of choice. The issues identified that
could relate to this dimension were when participant 2 was forced to abandon alerts due to no
further actions being available to him, and when participant 5 lost track of the warship and
had no other option but to wait until it was detected again by the drones. Both situations
are examples where the participants wanted to make a choice that was not an option based
on design.
The second principle is the ability to impact the system's behavior. The system at hand
has clear shortcomings in this regard as it is lacking the ability to manually control the drones,
alter and delete zones, highlight important areas of the zones, and ability to zoom and angle the
drone cameras. The issues of limiting the drone clustering behaviors is also a clear limitation
to this dimension.
The third dimension of is suﬀicient time to engage. Most clearly, time was limited when
handling an alert, as the participants only handled one incident at a time. Beyond that, it
seems like participants had enough time to perform their duties.
The fourth dimension is suﬀicient situational understanding. The issues mapped to this di-
mension are that participants had issues with differentiating sensor objects, especially through
the sensor objects panel. These issues led to mix-ups when changing tracking policies, as well
as faulty situational assessments during incidents.
More damning are the limitations that
make certain information completely unavailable. The fact that not all participants received
alerts for the incidents that occurred, and the drones had recurring issues in tracking relevant
objects, is a more direct limitation to an operator's situational awareness.
The last principle is the ability to predict system behaviors. This dimension becomes rele-
vant for the issue of whether or not control inputs (adjusting decay and switching algorithms)
have the intended effects. Here, participants seem to disagree. Some are pleased with their
control attempts, while for example participant 4 is not, and repeatedly go back to improve
behavior. If Their control attempts are actually effective is unclear within the data.
4.4.1.3
Post deployment
The relevant condition found within the technical layer (presented in Figure 4.4 for this study
is that operators need to be able to explain and account for the system’s actions, as well
as the possibility to verify outputs and behaviors after deployments. The first principle is
somewhat integrated into the system. In the post-trial interview, participants were explicitly
asked to explain and account for the system's behaviors.
It seems like most participants
could explain why they behaved as they did and explain their reasoning, but when explaining
how the system worked, multiple points of confusion came up, which can be reflected in the
issues in understanding how the system actually works. When asked if they would feel okay
defending the performance and behaviors of themselves and the system in court, all participants
either said no, or yes with a caveat that all system functions and obvious errors need to be
implemented or fixed properly. No participant felt that they were fully responsible for the
system's performance during the trial.
The ability to verify outputs and behaviors in hindsight is limited. Through recording the
trial, participants are able to reassess their behavior and the behavior of the system. However,
44

---
**[Page 51]**
*(This page contains a figure/chart/image not captured in text)*

4.4.
Mapping between MHC and control issues
the information is the same as during the trial; there is no additional information that can
confirm if what is shown is correct. Relevant errors that might need verification are if the
drones have tagged sensor objects correctly, if any drone at any point lost connection, and
if there were sensor objects within drone views that were not added to the map. This could
help verify when and if incidents have been missed or verify the sequence of events during
incidents. The need was also noted by some participants. Participant 3 states that one can
assume that all drone camera footage will be saved and that it can be used to properly verify
what happened.
Participant 2 notes that it would be nice to access the recorded camera
footage to get an understanding of his first alert.
4.4.2
Socio-technical
The socio-technical layer is the second layer of the model presented in Section 2.1.2.3. The
socio-technical layer was not observed in this study, but due to its interactions with the tech-
nical layer, it is nonetheless relevant.
Figure 4.5
The Socio-Technical Layer of the Model of MHC Used
Note. Shows the socio-technical layer and the conditions of each temporal stage in it. From
left: before deployment, to right: after deployment.
The first point in the pre-deployment section seen in Figure 4.5 is obviously not fulfilled
based on earlier results. For MHC to be fulfilled in the case of this system, further education of
the operators is necessary. In the same vein, for a properly human-centered design approach,
the training methods and the ability of operators to develop expertise need consideration. To
fulfill the second criterion in the socio-technical layer, the first must thus be fulfilled. The
last criterion is also part of a human-centered design approach and is being considered in the
creation of the system, through user tests, and extensive research before design at GEISTT
AB.
The deployment section of the socio-technical layer also highlights considerations for fu-
ture development. As the system in its current state is not implemented into an organizational
culture, there is no basis for analyzing it, meaning that the first criterion here is outside of
the scope. Standard Operating Procedures are, however, directly relevant to experiences of
confusion that the participants expressed, and would likely improve interaction. Apportion-
ment and recording of who is responsible/accountable for AI effects may be primarily relevant
when the system is implemented within an organization, but participant 4 did discuss needing
clarification of what exactly he would be responsible for in relation to the question of being
accountable for the system's performance.
None of the post-deployment requirements is relevant under the scope of the current study.
45

---
**[Page 52]**

5
Discussion
The discussion will start by summarizing the findings of the different research questions and
connecting them to previous research, problematizing and explaining them when necessary.
This will then lead to a discussion of the theory. Then, the method and its limitations will be
discussed, followed by future research directions.
5.1
RQ1: How is human control performed and maintained within
the system?
The results illustrate the activities the participants shared, as well as the varied methods used
to perform them. The activities the participants performed were 1) accessing a specific drone’s
camera feed, 2) controlling drone distribution and zone coverage, 3) judging sensor objects,
4) handling alerts, and 5) tactically distributing drones. Camera access was achieved through
three distinct methods: some participants primarily navigated using the map and play panel,
while others favored the drone and tracking symbols within plays. Sensor object judgment was
similarly varied, with participants weighing factors such as proximity, direction, context, and
established behavioral patterns differently depending on their individual reasoning strategies.
Alert handling was more consistent, with all participants first attempting to locate the source of
the alert, typically by seeking a direct camera view, before adjusting the relevant sensor object’s
tracking policy. Tactical planning followed a broadly shared structure, in which all trials began
with an initial planning phase, followed by at least one re-planning phase, though the frequency
and extent of re-planning differed across participants. Efforts to address drone clustering and
coverage gaps were also universal, though the methods and frequency of intervention ranged
from a single algorithm adjustment to extensive iterative re-planning, as was the case with
participant 4.
The participants perform control in predicted ways based on the interface design.
All
methods of altering drone behavior were used. These methods are also in line with common
methods for communicating operator intent to the swarm identified in Kolling et al. (2016),
like 1) switching between algorithms that implement desired swarm behaviors, 2) changing
parameters of a swarm control algorithm, in this case by altering decay, and 3) indirect control
of the swarm via environmental influences, in this case by defining geographical zones. As
Bjurling et al. (2020) described, participants also interacted across swarm levels by accessing
46

---
**[Page 53]**

5.2.
RQ2: When does human control fail within the system?
specific drone equipment, such as the drone’s cameras, handling sub-swarms through the plays-
panel, and performing resource allocation over the entire swarm.
5.2
RQ2: When does human control fail within the system?
The participants encountered a range of control issues, grouped into six themes. Camera feed
limitations, such as the inability to zoom or adjust the camera angle and the lack of a clear link
between the camera feed and the map, were recurring sources of frustration that made targeted
surveillance harder. Differentiating sensor objects was also a recurring challenge, which in some
cases led to incorrect situational assessments and unintended changes to tracking policies.
Handling alerts was confusing for several participants, who were at times unsure of what to
do after an alert was raised or what their role was. A lack of overview meant that participants
would sometimes miss alerts or have limited knowledge of the areas they were surveilling. All of
these issues are essentially related to situational awareness, which connects back to the well-
established challenges of maintaining situational awareness in human-autonomy interaction
(Endsley, 2019), and they highlight that these issues are not generalizable across interfaces
but are directly related to interface details.
Tracking behaviors were also a source of friction, as drones would, in some cases, fail to
follow people of interest, and get-away vehicles were not always tracked due to the underlying
tracking logic. These tracking issues are not an interface issue, but are directly related to
programmed behaviors. This highlights the need for a human-centered perspective on au-
tomation, even in the development of algorithms, as established by prior literature (Bhila,
2024; Güneysu, 2024). Similarly, Swarm behaviors, such as excessive flocking, were recurrent
issues and may have affected the system’s performance. This illustrates the double-edged na-
ture of emergent behaviors, as detrimental emergent behaviors arise from the same underlying
mechanisms as beneficial ones. Improving these detrimental behaviors may improve system
performance.
It was often unclear whether the changes participants made, such as adjusting decay or
switching algorithms, had the intended effect of spreading out the drones to avoid detrimental
emergent behaviors.
In some cases, this leads to distrust in the system.
The reason for
this vagueness is likely rooted in the characteristics of swarms. As outlined in the related
works, flocking and clustering are emergent behaviors and therefore not strictly predictable.
Emergent behaviors are also situated and context-specific. These characteristics mean that
feedback to control actions can not be given directly. Improvements to emergent behaviors
are instead necessarily assessed by surveying situational and dynamic behaviors, making the
feedback hard to interpret and non-actionable. The results of this study thus reinforce previous
literature on the challenges of surveilling emergent behaviors.
Finally, the zones and plays panel was missing features that participants expected, such
as the ability to delete or edit zones. This is a clear example of missing functionality that
should reasonably exist within the system. The plays panel also had additional indirect issues,
as its design seems to have contributed to repeated errors in zone management, once again
illustrating the level of detail at which control issues appear.
Participants also wanted greater control over the drone’s behavior, such as specifying areas
of interest within search zones and manually controlling specific drones in specific situations.
This could expand the available modes of communicating intent on the third point Kolling et al.
(2016) identified, for example, by using pheromone-based control. Manual control seems rea-
sonable in this case due to the tracking issues and the need for more targeted reconnaissance.
Beyond that, it is unclear whether additional control modes would improve system perfor-
mance, as operator intervention is not always beneficial to swarm performance and might even
harm it(Liu et al., 2019).
The question of whether the operator’s actions are necessary for system performance is
also relevant to the participants’ control actions observed in the trials. In the results, it is
47

---
**[Page 54]**

5.3.
RQ3: How can the system failures be compared to principles of human control?
unclear whether participants’ actions had the intended effect, so it is also unclear whether
participants succeeded in improving system performance. What is clear is that participants
wanted to intervene; it is less clear whether that intervention had a meaningful effect, and it
might have harmed performance.
5.3
RQ3: How can the system failures be compared to principles of
human control?
The issues identified in RQ2 were corroborated with the timeline accounts of the participants'
trials and could be mapped to the different sections of the expanded CHOF model proposed
in Section 2.1.2.3. Due to the expansive nature of this question, the results will be discussed
in the same structure as the results in Section 4.4 to improve coherence. First, the results of
the mapping between the data and the model’s technical layer will be presented, from pre-
deployment through deployment to post-deployment. Then, the shorter results from mapping
the socio-technical layer will be presented before proceeding to a discussion of MHC as a
concept.
5.3.1
The technical layer: pre-deployment
Within the technical layer, the pre-deployment conditions are the most clearly unmet. Partic-
ipants demonstrated insuﬀicient understanding of the system, the task, and the environment,
with confusion around core functionalities such as how decay and algorithms affect drone
behavior, and how alert cards operate. This lack of understanding appears to be as much a
consequence of insuﬀicient scaffolding, such as the absence of clear SOPs, predefined protocols,
and proper training, as it is of the system’s interface. The absence of strategic and tactical
guidance further compounded these issues, as participants were left to independently define
zones and plays with no established framework to guide their decisions. These results show
that the participants were unprepared for the task and that further education is necessary for
future operators to meet the MHC criteria.
To improve these misunderstandings, the roles of operators need to be clearly defined, as
well as SOP’s and other standard procedures. Operators need to be properly introduced to
the environment they are meant to surveil, including the most likely points of attack, road
layouts, and what constitutes normal activity. In the same vein, operators need to be educated
in threat detection and on how contextual clues could hint at a possible threat. Participants'
understanding of the algorithms and their parameters also needs to improve. Here lies an
inherent challenge due to the emergent behaviors discussed previously.
5.3.2
Technical Layer: during deployment
During deployment, the conditions are more ambiguous and harder to map cleanly to individual
issues. Freedom of choice was compromised in specific instances, such as when participants had
no available action to take after an alert, or when a sensor object was lost, and there was no
means to reacquire it. The ability to impact system behavior was similarly limited by missing
functionality, including the inability to manually control drones, alter or delete zones, adjust
camera angles, or affect drone behavior. Situational understanding was frequently incomplete,
particularly when differentiating between sensor objects, leading to mix-ups in tracking policy
adjustments and faulty assessments during incidents. Information was also sometimes directly
unavailable, as not all participants received alerts about incidents, and the drones had recurring
issues tracking relevant objects. The ability to predict system behavior also proved uncertain,
as the effects of control inputs such as adjusting decay or switching algorithms were not always
consistent with participants’ expectations.
Many of the dimensions found within the MHC model are worth problematizing, as it
affects which issues or problems should be placed within them. The first dimension of freedom
48

---
**[Page 55]**

5.3.
RQ3: How can the system failures be compared to principles of human control?
of choice is diﬀicult to interpret, as it is always limited to some extent. In a direct sense,
automation might force the participant to make certain decisions, but indirectly, the design and
the system also shape what choices are even considered. This is in line with good design, which
is meant to guide the user towards good decisions through the affordances it provides (Hartson,
2003). However, the dimension also applies to situations where objects are completely missed
by the system. This issue limits freedom of choice by not even offering the choice to begin
with. However, if this is included, the steering algorithm could also be seen as an infringement
on freedom of choice, as the operator is not offered the choice of where drones should fly.
Including this into the principle would risk bloating the concept. However, it also seems to
be the most likely way freedom may be limited within a system. If it is not considered, the
operators’ freedoms could be infringed upon simply by hiding their choices from them. That
being said, to control a swarm, the operator cannot manually steer all drones; a higher level of
control is not an option; it is a necessity. Designing the types of choices an operator must make
within the system is a required part of defining the operator’s role and making the system
usable.
Just like the first dimension, the second dimension of the ability to affect system behavior is
also largely ambiguous. In the most direct sense, it could mean that the necessary functionality
must be available to the operator to decide what the system will do (Boardman & Butcher,
2019), which correlates well with the identified issues in this study. Another interpretation
could be that the operator should have the ability to direct what the system will not do and to
constrain the system temporally, geographically, or by permitted behaviors/actions (Boardman
& Butcher, 2019). The interface has all of these implemented to some extent, for example,
limiting drone searches by zone, deciding when plays should end by canceling missions, and
limiting tracking of sensor objects through altered tracking policies. However, mapping any of
the issues identified in this study to this interpretation is challenging, as none of them neatly
fit within it. A third interpretation of the ability to impact the system’s behavior could also
refer to a wider set of factors, like the operator’s skill in relation to the system, whether the
control modes available do what the operators think that they do, and whether the operator
is not overloaded or indirectly unable to control the system. If this interpretation is used, the
other dimensions become relevant, making it broad and diﬀicult to map to individual issues.
Almost any control issue could be related to it; for example, the diﬀiculties in accessing the
camera feed through the map.
The third dimension, appropriate situational awareness, is ambiguous because it is hard
to judge whether situational awareness is insuﬀicient. This is equally an issue for the two
previously discussed dimensions. Attending to the different issues identified in the study would
likely improve these dimensions, though it is not technically realistic to expect issues to never
appear. To exemplify this, the cases in which the drones did not correctly identify relevant
sensor objects are largely unavoidable, so long as coverage is not perfect, which is impossible.
Defining what is “appropriate” is therefore of utmost importance, as the dimensions of MHC
can otherwise not be used to disqualify systems from use.
5.3.3
Technical layer: Post-deployment
In the post-deployment section, the relevant conditions are that operators can explain and
account for the system’s actions and that there is the possibility to verify outputs and be-
haviors. Regarding the first condition, most participants in this study could account for their
own reasoning and decisions, but struggled to explain the system’s behavior. No participant
felt entirely responsible for the system’s performance. The participants’ feelings on this point
should be considered, as they may otherwise be dissuaded from using the technology for fear
of being legally accountable for actions they do not feel are their own. This challenge is re-
flected in the literature on trust in automation, which establishes trust as a prerequisite for the
adoption of automation (Troath, 2025; Verdiesen & Dignum, 2023). The participants’ sense of
accountability does, therefore, to some extent map onto the appropriate level of legal respon-
49

---
**[Page 56]**

5.4.
Discussion of theory
sibility they should hold. Nevertheless, the self-serving bias, where successes are attributed to
internal qualities, while failures are attributed to external factors, might pose as a limitation
to that in some cases (Dong & Bocian, 2024; Lei & Rau, 2021).
The second condition, the ability to verify outputs and behaviors in hindsight, was limited
because no additional information beyond what was available during the trial could be accessed
afterward. The operator is thus unable to verify if control actions were successful, or if sensor
objects were correctly classified, and so on. This is a clear infringement on MHC. Therefore,
implementing methods to verify and assess drone behavior in hindsight is recommended.
5.3.4
Socio-technical layer
Within the socio-technical layer, the pre-deployment criteria are unmet, as adequate opera-
tor training and the development of expertise are not currently addressed. The deployment
criteria, including SOPs and a clear apportionment of responsibility, are directly relevant to
the confusion participants expressed during trials but remain outside the scope of the cur-
rent system’s implementation. For discussion of the point of further education, please see the
discussion of the operator’s understanding of the system in Section 5.3.1. None of the post-
deployment socio-technical criteria fell within the scope of the study, and no issues could be
mapped to them.
5.4
Discussion of theory
The findings discussed above speak not only to the performance of the system under study but
also raise broader questions about the theoretical frameworks used to evaluate it. Throughout
the process of mapping results to the consolidated CHOF model, it became clear that the
limitations identified are not exclusively those of the system but also those of the frameworks
themselves. Several dimensions proved diﬀicult to apply cleanly to the realities of the operator’s
working environment, and the conditions described by the model were, in many cases, too
loosely defined to serve as clear evaluative criteria. This is something the larger community
around MHC is aware of, as the concept is not yet fully defined.
The following section,
therefore, examines what the results of this study reveal about MHC as a concept: its current
utility, its limitations, and the directions in which it may need to develop. Given the use of a
consolidated framework in this study, this section will begin by discussing the limitations and
issues with that framework before expanding to a more general discussion.
5.4.1
Critique of the Extended CHOF model
The present study used a consolidated framework to explore the MHC and the drone-swarm
operator interface. This limits how well general insights map to the general conception of
MHC. It also becomes relevant to discuss how well this consolidation was made. This section
will therefore first explain the current issues in the consolidated model, and then explore how
well insights map to the underlying frameworks.
The most direct issue is that the dimensions of MHC (“Context Appropriate Human In-
volvement Across the AI System Lifecycle,” 2025) do not always neatly map to the different
areas of CHOF. The primary issue is the dimension of operator understanding. In this study,
the dimension was placed in the pre-deployment section of the technical layer, as operator un-
derstanding must come before deployment. The operator’s understanding, however, relies on
aspects of the socio-technical layer, for example, training and SOPs. Aspects of this dimension
thus pertain to the socio-technical layer.
The system understanding dimension has also been partially expanded for the use case.
The original wording is “the operator has suﬀicient understanding of the system, but to specify
it and suit the wording of the paper, I have added that operators also need an understanding
of the task and environment. The original wording could encapsulate this, but since “the
50

---
**[Page 57]**

5.4.
Discussion of theory
system” refers exclusively to the technical system in the paper, this addition was made to
avoid confusion. Beyond these interpretations, other dimensions are left in their original form
and placed in the deployment section. This means that discussion around these dimensions
applies directly to the dimensions “Context Appropriate Human Involvement Across the AI
System Lifecycle” (2025) defined.
Discussion also largely applies to the CHOF framework. With the caveat that the CHOF
model is also interpreted based on “Context Appropriate Human Involvement Across the AI
System Lifecycle” (2025), but the wording is changed from ways of controlling automation
across the life cycle to conditions. Furthermore, many of these conditions only apply to sys-
tems that are already implemented into operations, with operator training, and a surrounding
workplace culture. As these do not exist in the examined drone-control system, they can not
be evaluated.
5.4.2
The current and potential value of MHC
Despite the attempt to define MHC and make it operational, the results of this study show that
the concept is not yet definitional. Many of the dimensions of MHC(“Context Appropriate
Human Involvement Across the AI System Lifecycle,” 2025) are defined by terms such as
“the right level of X” and
“An acceptable amount of Y”, or rely on concepts that are not
binary or easily nominalized, such as “Freedom of choice”, and abilities that operators need
to have. When these concepts are not at all present within a system, as was the case with the
participants in this study, who clearly expressed that they did not have the expertise required
to feel comfortable using the system, the issue may become obvious. However, judging the
acceptability of the degree of different qualities is more challenging. For example, judging if a
participant’s level of situational awareness was “acceptable” is a question of interpretation.
The interpretative nature of MHC is not necessarily a flaw.
It might be essential for
applying it to the intended systems. These systems are interactional in nature and vary widely,
meaning that simple requirements may not capture their nuance. To illustrate this fact, Design
might cause operators to make predictable mistakes, such as with the zone selection tool when
creating plays in the current system. Functionality might exist, but the design affects the
quality of that functionality. The value of MHC can thus not only be definitional, but also
has to be analytical to suit its use cases.
For MHC’s value, however, whether analytical or definitional, the model requires greater
detail. Definitionally, the requirements need to vary according to the use case, as challenges
will vary.
Analytically, increased detail could minimize the information lost and improve
analytical quality. Currently, MHC is summarizing an extensive body of HF literature while
also demanding contextual interpretation. The concept thus cannot stand on its own without
a larger body of HF literature to support it, whereas the analysis could be performed solely
based on the HF literature, making the concept somewhat redundant for evaluatory use in its
current state.
The value of MHC could be educational. The concept has the potential to exemplify and
highlight the interactional challenges that autonomous systems face. This is necessary because
people outside the human-automation interaction field need to be aware of these challenges
to ensure the approach remains human-centered. If the pressing issues are to be addressed,
engineers, lawmakers, and designers alike need to adopt a human-centered perspective.
The framework can also be used to guide development. In the current study, multiple
points that need to be implemented before the system can be fielded have been identified,
such as defined SOPs and a thorough exploration of the system’s optimal use. In this way, the
framework can work as a to-do list to some extent.
Due to the interpretative nature of MHC, it may need to be applied to systems continually
and reevaluated as the system is used. It may take on a form where companies and developers
are required to continuously monitor and motivate the presence of MHC within their systems
51

---
**[Page 58]**

5.4.
Discussion of theory
to maintain their legality. Errors will inevitably happen, and taking swift action, both legally
and within companies and stakeholders, is paramount.
5.4.3
Developing the MHC model
The discussion above highlights how MHC currently serves multiple purposes. There is an
attempt to use it as a basis for requirements, making definitive statements about what is
necessary to achieve MHC, while also serving as a basis for development. Less discussed is
the possible analytical value of MHC, where it can be used as an interpretative tool to assess
where quality falters and educate on the complexities of automated systems.
5.4.3.1
Hard- & Soft MHC
To address these differing ways of handling MHC, I propose Hard and Soft MHC. Hard MHC
refers to binary, concrete requirements, i.e., the functions that must exist within a system for
meaningful control to be possible at all. The absence of a way to verify drone behaviors in
hindsight, identified in this study, is one such example: either the functionality exists, or it
does not. Soft MHC, on the other hand, concerns the quality with which those functions are
implemented and used. A system may technically allow operators to access camera feeds, but
the design of that access may be so cumbersome as to render it practically insuﬀicient. Rather
than resolving the interpretative challenges of MHC, this distinction instead delimits them:
hard MHC narrows the space of what must exist, while soft MHC governs the analytical and
evaluative work of assessing how well those conditions are met in practice.
Introducing Hard & Soft MHC could delineate what is, and what is not, suitable wording
for the different counterparts. Interpretative wording like “appropriate” and “acceptable” is
not suitable for Hard requirements, as they are not binary and clear.
However, they are
appropriate for Soft considerations, where a system must be analyzed at an interactional level
to be understood.
Soft frameworks could incorporate common human-automation interaction concepts such as
Situational Awareness, Workload considerations, Affordances, Vigilance issues, and different
levels of cognitive control, and describe how they interact with each other. It could serve
as a collection of considerations and challenges to weigh when designing human-autonomy
interaction. Hard MHC would consist of recommendations and requirements and come in a
more checklist-like format.
5.4.3.2
Specifying the model
Whether MHC is used in the Hard or Soft sense, the discussion also highlights a fundamental
tension within MHC as it currently stands: the concept is broad enough to apply across a
wide range of systems and use cases, but too loosely defined to function as a clear evaluatory
or legal standard in any specific one.
The model thus necessarily needs to be adapted to
specific use-cases and applications. In the case of military surveillance, the study offers a few
possible conditions. It seems necessary that operators have knowledge of the area they are
surveilling. They must know what the sites look like, their immediate environments, and the
most likely points of intrusion. The ability to take manual control of drones seems necessary
for the use case, as well as possibly that operators should not be forced to handle multiple,
unrelated alerts at the same time, as they are likely to be overloaded. Access to camera feeds
from different drones and to different sensor objects needs to be intuitive and easily accessible.
During intrusions, the operator needs to be able to access more specific information about the
incident, and have intuitive ways of managing the incident.
52

---
**[Page 59]**

5.5.
Discussion of method
5.5
Discussion of method
The methods used in this study warrant reflection on both their suitability for the research
questions and the practical limitations that arose during execution. This section discusses the
simulation environment as a research context, the experiment design and its shortcomings, the
CDM as an evaluatory method, and finally reflects on the analytical approach taken by the
study.
5.5.1
Simulation environment
The simulation environment effectively captured and simulated the use of the interface in
a military surveillance scenario.
However, there were several instances where realism and
rendering issues caused disruptions. Some sensor objects were not always rendered, leaving
participants unsure what the drones were tracking and whether there was an error in the
simulation. The paths of certain sensor objects were also noted, as participants realized that
some moved around in circles or lingered unnaturally. Terrain was not always immediately
rendered. This could have lowered immersion for some participants.
The prefab, or the look of the antagonist, was always the same, which may have led
participants to use it to judge whether a sensor object was a true threat. The coordination
of injects and other disappearing objects was not perfect, which led to objects sometimes
disappearing into thin air without explanation.
Despite these limitations in ecological validity, the study was performed successfully. The
simulation behaved differently across participants, which works well with the case-based struc-
ture of the study. Sometimes, errors in the simulation were interpreted as errors by the drones,
which is not an issue for the study. These issues would have been more damning if the method-
ology required increased controllability.
5.5.2
Experiment design and execution
The experiment design is based on scenarios. These scenarios were effective in capturing the
activity of swarm control, but sometimes did not fully live up to their design intent. The
scenarios were designed to include long periods of low activity to introduce vigilance-related
issues and create differences in workload across the trial. It is unclear from the results whether
this was successful; however, in a natural scenario, these periods of inactivity would no doubt
be longer. Introducing longer periods of inactivity might thus alter some of the results and
introduce noticeable vigilance issues.
The execution of trials was sometimes inconsistent. Participants received slightly different
introductions to the interface. Later participants received more clarification and had more
guidance during their introductory test run of the interface.
This may have caused some
differences in control behaviors. A malfunction in the simulation also altered the scenario for
Participant 4. He was meant to experience the entirety of scenario 2, but as the inject that was
meant to attack the chateau malfunctioned, he only experienced the two injects on the house.
Similarly to the inconsistencies in the simulation between participants, these inconsistencies
are not detrimental to the study, as the trials are not meant to be fully controlled.
5.5.3
Participants
The small, largely homogeneous cohort studied is a clear limitation on the methodology and
limits generalization. Most notably, in actual military operations, users would have different
backgrounds from the participants in this study. They would have even less knowledge of the
system, given the same introduction, and would have a less technical perspective. This could
possibly further exacerbate the issues related to system understanding.
The fact that the participants were part of the company that developed the simulation
environment and interface introduces a social desirability bias beyond what would have existed
53

---
**[Page 60]**

5.6.
Future research
had they not been stakeholders in the product they tested. The risk that they view the interface
and the environment favorably, or skew the results based on previous reflection, is likely. Other
control issues may have appeared had the cohort been different.
5.5.4
CDM as a method for studying MHC and interfaces
The use of CDM suits the study’s design, as it is a case-based interview technique. The use
of screen-recorded footage also mitigated many of the method’s limitations, as participants’
reasoning could be grounded in their observations of their own behavior, rather than relying
solely on memory. Limitations to CDM do, however, remain, as participants are still required
to explain their behavior in hindsight, especially when their live commentary is lacking or
unclear. Some behaviors do not have clear explanations, which may have forced participants
to rationalize, essentially making up reasons for their behaviors.
The interview prompts provided insight into participants’ cognitive processes, reasoning,
and experiences. The exact insight gained is naturally different and varies in its type. To
control for participants’ experiences with the simulation, more targeted questions about their
experiences with it could have been asked.
5.5.5
Analytical approach
The usage of CDM allows for sense-making activities that are connected to the varied research
questions posed by the studies, adapting the analysis to the questions. This enables a focused
analysis of the material and suits the explorative approach of the study.
Other methods of analysis were considered, for example, an interactional framework like
the JCF-S framework(Lundberg & Johansson, 2021).
These would be especially useful in
answering the first research question in greater detail. These methods were excluded in the
interest of time and because they are less useful in answering the remaining two research
questions. The issues of interaction in the study are often connected to the lack of interaction
with the system, not to the interaction in and of itself, for example, when functionality is
lacking or when information is hidden. Therefore, solely interactional methods are incomplete
in describing challenges and reasoning about MHC.
5.6
Future research
Future research should investigate additional use cases, systems, and participant groups in
relation to MHC. Given the novelty of the approach, its largely untapped potential across
new contexts and system types warrants explicit attention. Particular priority should be given
to tasks in sensitive domains, such as medical and military applications, and these should
be systematically examined through the lens of MHC. In parallel, domain experts in these
fields should be involved in empirical studies to obtain a more comprehensive understanding
of design challenges grounded in professional practice.
To support such work, a more robust MHC framework tailored to these types of studies
should be developed. The consolidated model used in this study could be expanded, selectively
reduced, or even restructured around the concepts of hard and soft MHC. Finally, method-
ological approaches for applying MHC across diverse use cases should be further explored and
refined.
54

---
**[Page 61]**

6
Conclusion
The results of this study identify the activities and methods that participants performed when
using the HMI, as well as 32 limitations to control specific to the interface.
These issues
were then mapped to a MHC model, illustrating the model's limitations, which is primarily
specificity. The study propose a few conditions that may help in adapting MHC towards the
specific use case of drone-swarms in ground surveillance. The value of the model is identified as
not yet being definitional, but analytical in nature. The study introduces the concept of hard
and soft MHC. Hard MHC refers to the conception of MHC as conditions and requirements,
i.e the functions that must exist within a system for meaningful control to be possible at all.
Whether post-deployment verification of drone behavior is technically available, or whether
operators can interrupt or override system actions, are Hard MHC questions. Soft MHC, by
contrast, concerns the quality with which those functions are implemented and whether they
remain genuinely usable under operational conditions.
A system could satisfy every Hard
MHC requirement and still fail to provide meaningful control if interface design systematically
obscures options, degrades situational awareness, or makes operator intervention impractical
in practice. These two types of MHC could serve different purposes and be designed accord-
ingly. The distinction matters not only analytically but practically: Hard MHC lends itself to
checklists and regulation, while Soft MHC calls for the kind of situated, iterative evaluation
that user studies like this one are suited to provide.
55

---
**[Page 62]**

Bibliography
Abdellatif, A. A., Elmancy, A., Mohamed, A., Massoud, A., Lebda, W., & Naji, K. K. (2025).
PDSR: Eﬀicient UAV deployment for swift and accurate post-disaster search and
rescue. IEEE Internet of Things Magazine, 8(3), 149–156. https://doi.org/10.1109/
IOTM.001.2400139
Abeywickrama, D. B., Wilson, J., Lee, S., Chance, G., Winter, P. D., Manzini, A., Habli, I.,
Windsor, S., Hauert, S., & Eder, K. (2023). AERoS: Assurance of emergent behaviour
in autonomous robotic swarms. In J. Guiochet, S. Tonetta, E. Schoitsch, M. Roy, & F.
Bitsch (Eds.), Computer safety, reliability, and security. SAFECOMP 2023 workshops
(pp. 341–354, Vol. 14182). Springer Nature Switzerland. https://doi.org/10.1007/978-
3-031-40953-0_28
Amoroso, D., & Tamburrini, G. (2020). Autonomous weapons systems and meaningful human
control: Ethical and legal issues. Current Robotics Reports, 1(4), 187–194. https://
doi.org/10.1007/s43154-020-00024-3
Arkin, R. C., Ulam, P., & Wagner, A. R. (2012). Moral decision making in autonomous systems:
Enforcement, moral emotions, dignity, trust, and deception. Proceedings of the IEEE,
100(3), 571–589. https://doi.org/10.1109/JPROC.2011.2173265
Arnold, T., & Scheutz, M. (2016). Against the moral turing test: Accountable design and the
moral reasoning of autonomous systems. Ethics and Information Technology, 18(2),
103–115. https://doi.org/10.1007/s10676-016-9389-x
Arranz, R., Carramiñana, D., Miguel, G. D., Besada, J. A., & Bernardos, A. M. (2023).
Application of deep reinforcement learning to UAV swarming for ground surveillance.
Sensors, 23(21), 8766. https://doi.org/10.3390/s23218766
Article 36. (2013). Killer robots: UK government policy on fully autonomous weapons (Policy
paper).
Asaro, P. (2012). On banning autonomous weapon systems: Human rights, automation, and
the dehumanization of lethal decision-making. International Review of the Red Cross,
94(886), 687–709. https://doi.org/10.1017/S1816383112000768
Asavasirikulkij, C., & Hanif, M. (2023). Human workload evaluation of drone swarm formation
control using virtual reality interface. Companion of the 2023 ACM/IEEE Interna-
tional Conference on Human-Robot Interaction, 132–136. https://doi.org/10.1145/
3568294.3580057
Bainbridge, L. (1983). Ironies of automation. Automatica, 19(6), 775–779. https://doi.org/10.
1016/0005-1098(83)90046-8
56

---
**[Page 63]**

Bibliography
Bhila, I. (2024). Putting algorithmic bias on top of the agenda in the discussions on autonomous
weapons systems. Digital War, 5(3), 201–212. https://doi.org/10.1057/s42984-024-
00094-z
Bjurling, O., Granlund, R., Alfredson, J., Arvola, M., & Ziemke, T. (2020). Drone swarms in
forest firefighting: A local development case study of multi-level human-swarm inter-
action. Proceedings of the 11th Nordic Conference on Human-Computer Interaction:
Shaping Experiences, Shaping Society, 1–7. https://doi.org/10.1145/3419249.3421239
Boardman, M., & Butcher, F. (2019). An exploration of maintaining human control in AI
enabled systems and the challenges of achieving it. https://doi.org/10.14339/STO-
MP-IST-178-07-PDF
Booker, J. O. (2025). War machines of tomorrow: Accountability and oversight in the age of
lethal autonomous weapon systems. In H. R. Arabnia, L. Deligiannidis, F. Shenavar-
masouleh, S. Amirian, & F. Ghareh Mohammadi (Eds.), Computational science and
computational intelligence (pp. 213–223, Vol. 2510). Springer Nature Switzerland.
https://doi.org/10.1007/978-3-031-94956-2_17
Casner, S. M., Geven, R. W., Recker, M. P., & Schooler, J. W. (2014). The retention of
manual flying skills in the automated cockpit. Human Factors: The Journal of the
Human Factors and Ergonomics Society, 56(8), 1506–1516. https://doi.org/10.1177/
0018720814535628
Chen, Z.-H. (2023). Based on intelligent attack and defense command technology system for
multi-rotor TiltingVertical takeoff and landing swarm UAVs. 2023 IEEE International
Conference on e-Business Engineering (ICEBE), 276–280. https://doi.org/10.1109/
ICEBE59045.2023.00012
Cho, J., Sung, J., Yoon, J., & Lee, H. (2020). Towards persistent surveillance and reconnais-
sance using a connected swarm of multiple UAVs. IEEE Access, 8, 157906–157917.
https://doi.org/10.1109/ACCESS.2020.3019963
Context appropriate human involvement across the AI system lifecycle [Human Factors and
Medicine Panel]. (2025). https://doi.org/10.14339/MP-HFM-377-14-PDF
Coppola, M., Guo, J., Gill, E., & de Croon, G. C. H. E. (2021). A model-based framework for
learning transparent swarm behaviors. https://doi.org/10.48550/ARXIV.2103.05343
Crandall, B., Klein, G., & Hoffman, R. (2006). Working minds: A practitioner’s guide to
cognitive task analysis.
Crandall, J. W., Anderson, N., Ashcraft, C., Grosh, J., Henderson, J., McClellan, J., Neupane,
A., & Goodrich, M. A. (2017). Human-swarm interaction as shared control: Achieving
flexible fault-tolerant systems. In D. Harris (Ed.), Engineering psychology and cognitive
ergonomics: Performance, emotion and situation awareness (pp. 266–284, Vol. 10275).
Springer International Publishing. https://doi.org/10.1007/978-3-319-58472-0_21
Cummings, M. (2019). Lethal autonomous weapons: Meaningful human control or meaningful
human certification? [opinion]. IEEE Technology and Society Magazine, 38(4), 20–26.
https://doi.org/10.1109/MTS.2019.2948438
Defence Science Board. (2012, July 12). TASK FORCE REPORT: The role of autonomy in
DoD systems (Task force report). Department of defense. Wahington, USA.
des Armées, M. (2019, January 1). L’intelligence artificielle au service de la défense (Etude et
rapport). Ministère des Armées. Paris, France.
Ding, Y., Li, X., Yuan, M., & Xiang, W. (2026). From control to command: A bimanual
mimetic gesture interface for drone swarm maneuvering in distracted environments.
Proceedings of the Extended Abstracts of the 2026 CHI Conference on Human Factors
in Computing Systems, 1–5. https://doi.org/10.1145/3772363.3798696
Divband Soorati, M., Clark, J., Ghofrani, J., Tarapore, D., & Ramchurn, S. D. (2021). De-
signing a user-centered interaction interface for human–swarm teaming. Drones, 5(4),
131. https://doi.org/10.3390/drones5040131
Dong, M., & Bocian, K. (2024). Responsibility gaps and self-interest bias: People attribute
moral responsibility to AI for their own but not others’ transgressions. Journal of
57

---
**[Page 64]**

Bibliography
Experimental Social Psychology, 111, 104584. https://doi.org/10.1016/j.jesp.2023.
104584
Dorri, A., Kanhere, S. S., & Jurdak, R. (2018). Multi-agent systems: A survey. IEEE Access,
6, 28573–28593. https://doi.org/10.1109/ACCESS.2018.2831228
Ekelhof, M., & Persi Paoli, G. (2020). The human element in decisions about the use of force.
United Nations Institute for Disarmament Research. Geneva.
Elish, M. C. (2019). Moral crumple zones: Cautionary tales in human-robot interaction. Engag-
ing Science, Technology, and Society, 5, 40–60. https://doi.org/10.17351/ests2019.260
Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems. Human
Factors: The Journal of the Human Factors and Ergonomics Society, 37(1), 32–64.
https://doi.org/10.1518/001872095779049543
Endsley, M. (2019). Human-automation interaction and the challenge of maintaining situation
awareness in future autonomous vehicles. In Human performance in automated and
autonomous systems (1st ed.). CRC Press. https://doi.org/https://doi.org/10.1201/
9780429458330
Fang, Z., Qin, J., Qin, J., Ma, Q., Han, R., & Liu, Q. (2025). Eye movement-based human–
swarm interaction for coverage control of mobile robots with constraints. IEEE Trans-
actions on Industrial Electronics, 72(6), 6454–6464. https://doi.org/10.1109/TIE.
2024.3497343
Geiß, R., & Lahmann, H. (2017, October 27). Autonomous weapons systems: A paradigm
shift for the law of armed conflict? In J. D. Ohlin (Ed.), Research handbook on remote
warfare. Edward Elgar Publishing. https://doi.org/10.4337/9781784716998.00023
Güneysu, G. (2024). Lethal autonomous weapon systems and automation bias. Yuridika, 39(3),
395–424. https://doi.org/10.20473/ydk.v39i3.55188
Hartson, R. (2003). Cognitive, physical, sensory, and functional affordances in interaction
design. Behaviour & Information Technology, 22(5), 315–338. https://doi.org/10.
1080/01449290310001592587
Hocraffer, A., & Nam, C. S. (2017). A meta-analysis of human-system interfaces in unmanned
aerial vehicle (UAV) swarm management. Applied Ergonomics, 58, 66–80. https://doi.
org/10.1016/j.apergo.2016.05.011
Horyna, J., Baca, T., Walter, V., Albani, D., Hert, D., Ferrante, E., & Saska, M. (2023).
Decentralized swarms of unmanned aerial vehicles for search and rescue operations
without explicit communication. Autonomous Robots, 47(1), 77–93. https://doi.org/
10.1007/s10514-022-10066-5
Hulianytskyi, L. F. (2026). UAV swarms and their characteristics. Cybernetics and Systems
Analysis, 62(2), 241–254. https://doi.org/10.1007/s10559-026-00861-8
Humann, J., & Pollard, K. A. (2019). Human factors in the scalability of multirobot operation:
A review and simulation. 2019 IEEE International Conference on Systems, Man and
Cybernetics (SMC), 700–707. https://doi.org/10.1109/SMC.2019.8913876
ICRC. (2017). Ethics and autonomous weapon systems: An ethical basis for human control?
(Article). International Committee of the Red Cross. Geneva.
Kennedy, J., & Eberhart, R. (1995). Particle swarm optimization. Proceedings of ICNN’95 -
International Conference on Neural Networks, 4, 1942–1948. https://doi.org/10.1109/
ICNN.1995.488968
Kolling, A., Sycara, K., Nunnally, S., & Lewis, M. (2013). Human swarm interaction: An ex-
perimental study of two types of interaction with foraging swarms. Journal of Human-
Robot Interaction, 2(2), 103–128. https://doi.org/10.5898/JHRI.2.2.Kolling
Kolling, A., Walker, P., Chakraborty, N., Sycara, K., & Lewis, M. (2016). Human interaction
with robot swarms: A survey. IEEE Transactions on Human-Machine Systems, 46(1),
9–26. https://doi.org/10.1109/THMS.2015.2480801
Kwik, J. (2022). A practicable operationalisation of meaningful human control. Laws, 11(3),
43. https://doi.org/10.3390/laws11030043
58

---
**[Page 65]**

Bibliography
Lazaros, K., Vrahatis, A. G., & Kotsiantis, S. (2026). Human-in-the-loop artificial intelligence:
A systematic review of concepts, methods, and applications. Entropy, 28(4), 377.
https://doi.org/10.3390/e28040377
Lei, X., & Rau, P.-L. P. (2021). Should i blame the human or the robot? attribution within a
human–robot group. International Journal of Social Robotics, 13(2), 363–377. https:
//doi.org/10.1007/s12369-020-00645-w
Liu, R., Cai, Z., Lewis, M., Lyons, J., & Sycara, K. (2019). Trust repair in human-swarm
teams+. 2019 28th IEEE International Conference on Robot and Human Interactive
Communication (RO-MAN), 1–6. https://doi.org/10.1109/RO-MAN46459.2019.
8956420
Longpre, S., Storm, M., & Shah, R. (2022). Lethal autonomous weapons systems & artificial
intelligence: Trends, challenges, and policies. MIT Science Policy Review, 3. https:
//doi.org/10.38105/spr.360apm5typ
Lundberg, J., & Johansson, B. J. E. (2021). A framework for describing interaction between hu-
man operators and autonomous, automated, and manual control systems. Cognition,
Technology & Work, 23(3), 381–401. https://doi.org/10.1007/s10111-020-00637-w
Matthias, A. (2004). The responsibility gap: Ascribing responsibility for the actions of learning
automata. Ethics and Information Technology, 6(3), 175–183. https://doi.org/10.
1007/s10676-004-3422-1
McDougall, C. (2019). Autonomous weapon systems and accountability: Putting the cart be-
fore the horse. Melbourne Journal of International Law. Retrieved February 13, 2026,
from https://www.austlii.edu.au/au/journals/MelbJIL/2019/4.html#Heading405
Menda, J., Hing, J. T., Ayaz, H., Shewokis, P. A., Izzetoglu, K., Onaral, B., & Oh, P. (2011).
Optical brain imaging to enhance UAV operator training, evaluation, and interface
development. Journal of Intelligent & Robotic Systems, 61(1), 423–443. https://doi.
org/10.1007/s10846-010-9507-7
Miller, C., Draper, M., van Diggelen, J., Heijnen, M., Shively, R. J., Flemisch, F., Baltzer, M.,
Woltjer, R., Boardman, M., Devitt, K., Pacaux-Lemoine, M.-P., & Parry, E. (2023,
July 27). Meaningful human control of AI-based systems workshop: Technical eval-
uation report, thematic perspectives and associated scenarios. https://doi.org/10.
14339/STO-MP-HFM-322-ALL-PDF
Molloy, R., & Parasuraman, R. (1996). Monitoring an automated system for a single fail-
ure: Vigilance and task complexity effects. Human Factors: The Journal of the Hu-
man Factors and Ergonomics Society, 38(2), 311–322. https://doi.org/10.1177/
001872089606380211
Mostafa, S. A., Ahmad, M. S., & Mustapha, A. (2019). Adjustable autonomy: A systematic
literature review. Artificial Intelligence Review, 51(2), 149–186. https://doi.org/10.
1007/s10462-017-9560-8
Parasuraman, R., Sheridan, T., & Wickens, C. (2000). A model for types and levels of human
interaction with automation. IEEE Transactions on Systems, Man, and Cybernetics -
Part A: Systems and Humans, 30(3), 286–297. https://doi.org/10.1109/3468.844354
Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation:
An attentional integration. Human Factors: The Journal of the Human Factors and
Ergonomics Society, 52(3), 381–410. https://doi.org/10.1177/0018720810376055
Priya, A., Kumar, S., & Kumar, S. (2024). Surveillance using 5g based drone swarm system
for forest area. 2024 IEEE Students Conference on Engineering and Systems (SCES),
1–5. https://doi.org/10.1109/SCES61914.2024.10652563
Rouff, C., Vanderbilt, A., Hinchey, M., Truszkowski, W., & Rash, J. (2004). Verification of
emergent behaviors in swarm-based systems. Proceedings. 11th IEEE International
Conference and Workshop on the Engineering of Computer-Based Systems, 2004.,
443–448. https://doi.org/10.1109/ECBS.2004.1316730
Ruetten, L., Regis, P. A., Feil-Seifer, D., & Sengupta, S. (2020). Area-optimized UAV swarm
network for search and rescue operations. 2020 10th Annual Computing and Commu-
59

---
**[Page 66]**

Bibliography
nication Workshop and Conference (CCWC), 0613–0618. https://doi.org/10.1109/
CCWC47524.2020.9031197
Saab. (2024, November 7). Saab’s autonomous swarm technology used in landmark AUKUS
trial [Press releases]. https://www.saab.com/newsroom/press-releases/2024/saabs-
autonomous-swarm-technology-used-in-landmark-aukus-trial
Sanghvi, V. (2025). Autonomous weapons systems: An analytical review of technological capa-
bilities, operational challenges, and mitigation strategies. American Journal of Student
Research, 13–27. https://doi.org/10.70251/HYJR2348.361327
Santoni De Sio, F., & Van Den Hoven, J. (2018). Meaningful human control over autonomous
systems: A philosophical account. Frontiers in Robotics and AI, 5, 15. https://doi.
org/10.3389/frobt.2018.00015
Sheridan, T. B. (1992). Telerobotics, automation, and human supervisory control. MIT Press.
Shin, D. (2025). Can AI have a sense of morality? AI & SOCIETY, 40(6), 4169–4170. https:
//doi.org/10.1007/s00146-025-02476-7
Smith, P. T. (2022). Resolving responsibility gaps for lethal autonomous weapon systems.
Frontiers in Big Data, 5, 1038507. https://doi.org/10.3389/fdata.2022.1038507
Spadaro, A. (2024). A weapon is no subordinate. Journal of International Criminal Justice,
21(5), 1119–1136. https://doi.org/10.1093/jicj/mqad025
Sparrow, R. (2007). Killer robots. Journal of Applied Philosophy, 24(1), 62–77. https://doi.
org/10.1111/j.1468-5930.2007.00346.x
Sparrow, R. (2016). Robots and respect: Assessing the case against autonomous weapon
systems. Ethics & International Affairs, 30(1), 93–116. https://doi.org/10.1017/
S0892679415000647
Strid, E., Tschanz, D., Castor, M., Insulander, M., & Borgvall, J. (2024). Slutrap-
port simuleringsbaserad konceptdemo (Slutleverans FoT Militärt Innovationsprogram
No. 50097537). FMV.
Taddeo, M., & Blanchard, A. (2022). Ascribing moral responsibility for the actions of au-
tonomous weapons systems: A moral gambit. SSRN Electronic Journal. https://doi.
org/10.2139/ssrn.4096934
Troath, S. (2025). Trusting technology to wage war: The politics of trust and ethics in the
development of robotics, autonomous systems, and artificial intelligence. Critical Mil-
itary Studies, 11(1), 59–77. https://doi.org/10.1080/23337486.2024.2362074
Trusilo, D. (2023). Autonomous AI systems in conflict: Emergent behavior and its impact on
predictability and reliability. Journal of Military Ethics, 22(1), 2–17. https://doi.org/
10.1080/15027570.2023.2213985
UNIDIR. (2014). The weaponization of increasingly autonomous technologies: Considering how
meaningful human control might move the discussion forward. UN. Geneva.
U.S. Department of Defense. (2012, November 21). AUTONOMY IN WEAPON SYSTEMS
(DOD DIRECTIVE 3000.09). Oﬀice of the Under Secretary of Defense for Policy.
Washington.
Verdiesen, I., Aler Tubella, A., & Dignum, V. (2021). Integrating comprehensive human over-
sight in drone deployment: A conceptual framework applied to the case of military
surveillance drones. Information, 12(9), 385. https://doi.org/10.3390/info12090385
Verdiesen, I., & Dignum, V. (2023). Value elicitation on a scenario of autonomous weapon
system deployment: A qualitative study based on the value deliberation process. AI
and Ethics, 3(3), 887–900. https://doi.org/10.1007/s43681-022-00211-2
Verdiesen, I., Santoni De Sio, F., & Dignum, V. (2021). Accountability and control over au-
tonomous weapon systems: A framework for comprehensive human oversight. Minds
and Machines, 31(1), 137–163. https://doi.org/10.1007/s11023-020-09532-9
Volz, K., Yang, E., Dudley, R., Lynch, E., Dropps, M., & Dorneich, M. C. (2016). An evaluation
of cognitive skill degradation in information automation. Proceedings of the Human
Factors and Ergonomics Society Annual Meeting, 60(1), 191–195. https://doi.org/10.
1177/1541931213601043
60

---
**[Page 67]**

Bibliography
Watch, H. R. (2012, November 19). Losing humanity: The case against killer robots. Human
Rights Watch. https://www.hrw.org/report/2012/11/19/losing-humanity/case-
against-killer-robots
Wattearachchi, W. D., Lakshika, E., Kasmarik, K., & Barlow, M. (2025). A study on human-
swarm interaction: A framework for assessing situation awareness and task perfor-
mance. https://doi.org/10.48550/ARXIV.2503.14810
Winfield, A. F. T., & Jirotka, M. (2018). Ethical governance is essential to building trust in
robotics and artificial intelligence systems. Philosophical Transactions of the Royal
Society A: Mathematical, Physical and Engineering Sciences, 376(2133), 20180085.
https://doi.org/10.1098/rsta.2018.0085
Zhang, J., Han, K., Zhang, P., Hou, Z., & Ye, L. (2023). A survey on joint-operation application
for unmanned swarm formations under a complex confrontation environment. Journal
of Systems Engineering and Electronics, 34(6), 1432–1446. https://doi.org/10.23919/
JSEE.2023.000162
61

---
**[Page 68]**

A
Participant Consent Form
62

---
**[Page 69]**

Participant Consent Form 
Study Title: Control in Military Surveillance with a Drone Swarm 
Researcher: Minna Leijonhufvud, Department of Computer and Information Science (IDA), 
Linköping University 
 
It is important that you read through the following document carefully.  
It will inform you of the project you are invited to take part in, how your personal information will 
be handled, and what your participation entails. 
 
About the Study 
You are invited to take part in a research study that explores how humans interact with 
autonomous drone swarms during military surveillance. This study aims to understand the 
concept of meaningful human control in this context, and to inform the design of safe human-
machine interfaces as well as guidelines and legislation for autonomous military systems. 
If you agree to take part, you will be asked to control a virtual drone swarm using a human-
machine interface (HMI) to monitor a virtual archipelago that contains three sensitive sites. 
During the task, threats to these sites may occur, which you will report to the researcher. This 
surveillance task will take approximately 90 minutes. After the task, you will participate in a 
semi-structured interview about your experience, which may last between 30 and 90 minutes. 
Overall, your participation will take around 2.5 to 3 hours. 
During the surveillance task, the computer monitor you will be using will be screen recorded, 
and notes will be taken throughout. During the interview, audio will be recorded, and what you 
say may be transcribed for analysis with the use of AI.  
Confidentiality 
All data will be anonymized, and only the data collected during the task, and the interview will be 
stored. When the project is concluded, the data collected and generated during the project will 
be stored securely at Linköpings University for at least 10 years for archival purposes. No 
unauthorized people will be allowed to access the data. If the material is deemed to have lasting 
historical value, it may be preserved in perpetuity.  
Both the video recordings and audio recordings collected will fall under the category of personal 
information. Thus, your rights are defined in EU data protection regulations and national 
supplementary legislation. You have the right to: 
• 
withdraw your consent without affecting the lawfulness of processing personal data that 
took place in accordance with this consent before it was withdrawn 
• 
request access to your personal data 
• 
have your personal data corrected 

---
**[Page 70]**
*(This page contains a figure/chart/image not captured in text)*

• 
have your personal data deleted 
• 
have the processing of your personal data limited. 
Under certain circumstances, the Data Protection Regulation and supplementary national 
legislation allow delimiting these rights. The right to access one's data can, for example, be 
limited by confidentiality requirements, and the right to have data deleted can be limited by rules 
regarding archiving. 
If you want to invoke any of these rights, then contact Minna Leijonhufvud 
(minnaleij@gmail.com). 
You have the right to complain to the Swedish Privacy Protection Agency (imy.se). 
Voluntary Participation 
Your participation is completely voluntary. You may choose to withdraw at any time without any 
consequences, and your decision will not affect your relationship with the researcher, your 
employer, or Linköping University. 
There is no compensation for participation. 
Results 
The study’s results will be published in a report, a presentation, and possibly in academic 
journals or conferences.  
Questions or Concerns 
If you have any questions about the study or your rights as a participant, you can contact Minna 
Leijonhufvud at the Department of Computer and Information Science (IDA), Linköping 
University. Email: minle060@student.liu.se or minnaleij@gmail.com  
Consent 
By signing below, you confirm that you have read and understood this information, that you have 
had the chance to ask questions, and that you agree to participate voluntarily. 
 
 
 I consent to my participation in the study and the storage of my data. 
 
 
____________________________                                                                            ____________________________ 
Underskrift                                                                                                                  Namnförtydligande 
 
____________________________ 
Datum 

---
**[Page 71]**

B
Introduction to the HMI
65

---
**[Page 72]**

Introduction 
 
You will now get instructions about your task and what you will be doing during the 
experiment. Please read through the instructions carefully.  
 
The first part of this experiment is familiarizing yourself with the HMI that you will use during 
the experiment. The HMI is designed for operating a drone swarm in a military surveillance 
use case. After familiarizing yourself with the interface, you will be presented with the 
specific drone surveillance task that you will be performing within a simulation. This 
surveillance task will last up to 90 minutes, and it is designed to simulate a real-world 
scenario in which you are the operator. After 90 minutes have passed, you will participate in 
a semi-structured interview to discuss your experience during the simulation. 
 
You will familiarize yourself with the HMI in two main steps. First, you will read through the 
description of the interface below. Then, you will practice using the interface through a short 
test run of the simulation. The map and the interface will be identical to the one that will be 
used during your task in the later parts of this trial. The purpose of this is for you to become 
familiar using the controls described below, and preparing you for the task.  
 
When you feel you have a sufficient understanding of the HMI, you will be given the 
instructions for the task you will be performing. 
 

---
**[Page 73]**
*(This page contains a figure/chart/image not captured in text)*

HMI description 
 
What the HMI looks like at the start of the simulation 
The interface is divided into eight panels. Each panel handles a specific part of your job. 
Some panels give you information, and others let you control the drones. 
Information panels — these tell you what is happening: 
●​ Map — shows you the operational area and where everything is 
●​ Events — a running log of things the drones have done 
●​ Alerts — notifications about things that may require your attention 
●​ Resources — shows you how many drones you have and how they are currently 
deployed 
●​ Videofeed — a live camera feed from a camera in the scene.  
Control panels — these let you direct the drones: 
●​ Zones — lets you define areas on the map for the drones to operate in or avoid 
●​ Tracking Policy — predefined rules for how drones respond to detected objects 
●​ Plays — lets you create and manage surveillance missions 
Each panel is described in detail below. 
 

---
**[Page 74]**
*(This page contains a figure/chart/image not captured in text)*

Information Panels 
Map 
 
Example of the map in session 
The map is the main panel of the interface. It gives you a live view of the operational area 
and shows you everything that is happening spatially. The following elements are displayed 
on the map: 
●​ Gray circles — the current position of each drone in the swarm. 
●​ Colored zones — areas you have defined. Blue areas indicate active search areas, 
and red areas indicate no-entry zones around the sensitive sites. You can add your 
own zones using the Zones panel. 
●​ Drone nest — the icon showing where drones are launched from and returned to (in 
this scenario, a boat). 
●​ White squares — detected objects (people, vehicles, or boats). A filled white square 
means a drone is currently tracking the object. An outlined square means it has been 
spotted but is not currently being tracked. A gray square means the object has 
moved out of sensor range. 
●​ Red triangles — active alerts. These turn gray once you have acknowledged them. 
See the Alerts section for more information. 
●​ Shading on the map — indicates where the drones' sensors currently have 
coverage. 
You can click on any detected object on the map to jump to its entry in the Plays panel, 
where you can find more details about it. 
The restriction zones currently set are minimal. A no-fly zone is placed above Västervik, and 
a no-entry zone is placed around the immediate surroundings of the sensitive sites. During 
your task, more zones will need to be added to define which areas the drones should surveil.

---
**[Page 75]**
*(This page contains a figure/chart/image not captured in text)*

Events & Alerts 
 
 
What the event log looks like at the start of the simulation 
The Events panel is a live activity log. Every time something notable happens in the swarm, 
a new entry appears here.  
Events 
The left side of the events panel displays swarm events that you do not need to act on — 
they are there to help you keep track of what the swarm is doing. 
Entries here show: 
●​ What happened — for example, "stopped tracking" 
●​ When it happened — for example, "a minute ago" 
●​ Which drone it was — for example, "Drone ID: 30" 
Examples of events you will see include a drone spotting a new object, a drone stopping its 
tracking of an object, or a drone activating its camera. 
Here is an example of what the left side of the event panel could look like in session: 
 
Example of events in the event log 

---
**[Page 76]**
*(This page contains a figure/chart/image not captured in text)*

Alerts 
The right side of the events panel displays alerts.  
Alerts notify you when something important happens that may require your attention. Unlike 
events, alerts are specifically designed to flag situations that are potentially critical — for 
example, a person entering a restricted zone or a drone losing contact with the system. 
This is an example of what it could look like in session: 
 
 
Example of what an alert looks like under the events log. 
Each alert shows a summary of what happened, when it happened, and where. You can: 
●​ Press Acknowledge to mark an alert as seen. The alert will then turn gray on both 
the panel and the map. 
●​ Press View to expand the alert and access additional options (see the image below): 
○​ Decrease / Escalate — adjust the severity level of the alert. 
○​ Text field — leave notes about the alert. 
○​ Communicate — not currently active, but intended for future use in 
multi-operator scenarios. 
 
What an expanded alert looks like 
Alerts also appear on the map as red triangles at the location where they occurred: 
 
No Alerts will appear during the test run, but might pop up during your later task.  
 

---
**[Page 77]**
*(This page contains a figure/chart/image not captured in text)*

Resources 
 
Example of what the resource panel could look like in session 
The Resources panel is located at the top of the interface and gives you a quick overview of 
your drone assets. It shows: 
●​ The total number of drones you have available.  
●​ Shows how many drones are currently deployed on a mission versus available for 
new tasks. 
In the example shown above, 18 out of 30 drones are available, and 12 are occupied in a 
mission called "Swarm 0." 
Drones are launched and recovered automatically — you do not need to manage this 
manually. If a launch or recovery is currently in progress, a small upward or downward arrow 
will appear next to the drone nest icon in that panel. 
Videofeed 
 
The videofeed at the start of the simulation 
 
The large right panel of the interface shows a live video feed.  
 
At the start of the simulation, the feed displays camera footage from the boat that constitutes 
the DroneBay, where drones are held when they are not deployed on a mission.  
 
You can click on the drones in the map to see their camera footage. For example, if you wish 
to take a closer look at the object they have detected. 
 

---
**[Page 78]**
*(This page contains a figure/chart/image not captured in text)*

Control Panels 
Zones 
 
Example of what the Zones panel could look like in session 
The Zones panel lets you define geographic areas on the map, and they are the backbone of 
controlling what area drones will surveil. These areas tell the drones where they are allowed 
to search, where they must not go, and where protected sites are located.  
They also control what will be alerted. Any newly detected sensor object within a restricted 
area (a “red” zone on the map) will raise an alert.    
A zone must be created before you can assign it to a mission. 
To create a zone: 
1.​ Press the small + button in the top-right corner of the Zones panel. 
2.​ Give the zone a name in the Title field. 
3.​ Draw the zone boundaries directly on the map by clicking and dragging. 
4.​ To finish drawing, click again on the ending boundary-node.  
In the example above, 4 Areas of Interest have been defined in this way and have been 
given the names: SO1, SO2, SO3 & SO4. 
To edit an existing zone: 
●​ Press the small pen icon next to the zone you want to modify. You can then adjust 
the boundaries on the map. 
Each zone can be assigned a type — for example, a search area, a no-entry zone around a 
sensitive site, or a no-fly zone. Zones are color-coded on the map according to their type. 

---
**[Page 79]**
*(This page contains a figure/chart/image not captured in text)*

Zone parameters: 
●​ Block Size — defines how large an area a single drone is considered to cover at any 
given moment. A larger block size means the swarm considers more of the map as 
covered per drone. 
●​ Decay — defines how long an area remains marked as "covered" after a drone has 
left it. A shorter decay time causes drones to revisit areas more frequently. 
Both Zone parameters have preconfigured values that will work for your task, so these can, 
but do not need to be altered.  
Tracking Policy 
 
The tracking policy panel at the start of the simulation 
The Tracking Policy panel defined rules that govern how the drones behave when they 
detect an object. Rather than manually directing each drone, policies applies to the system 
automatically. 
You are not expected to edit these policies, but you can leverage them in session by 
applying them to specific sensor objects in the plays panel, as described in the next section. 
Each policy has: 
●​ A name to identify it. 
●​ A number of drones to assign to tracking when the policy is triggered. 
●​ One or more conditions that modify tracking behavior. 
Currently, the only condition applied is:  
●​ Stay in zone — the drone will only track an object while it remains within the defined 
mission area. If the object leaves the zone, tracking stops automatically. 
The Ignore policy removes any tracking behavior from a sensor object,  

---
**[Page 80]**
*(This page contains a figure/chart/image not captured in text)*

Plays 
The Plays panel is where you create and monitor surveillance missions. It is placed to the 
right of the HMI, left of the videofeed. A "play" is a mission that assigns a group of drones to 
search a defined zone using a chosen search pattern. 
In the overview picture from earlier, no plays have been defined. To start creating a play, 
press the surveillance button at the top of the panel, after which the following panel will pop 
up: 
 
Creating a play in the plays panel 
Step-by step to create a new play: 
1.​ Press the Surveillance button at the top of the panel. 
2.​ Configure the following settings: 
○​ Zone — select the area where the drones should operate. This zone must 
already exist in the Zones panel. 
○​ Number of drones — how many drones to assign to this mission. 
○​ Search algorithm — the pattern the drones will use to search the area. Two 
options are available and are described in a later section. 
○​ Energy strategy — choose between Relay and All-in. (Description to be 
added.) 
○​ Altitude — minimum and maximum flight altitude. (Note: these settings are 
currently not active.) 
3.​ Press Calculate to finalize and launch the mission.’ 
Once a mission is running, it appears as a card in the Plays panel. 

---
**[Page 81]**
*(This page contains a figure/chart/image not captured in text)*

Monitoring an active play: 
 
Example of a play’s card in the plays panel. 
Each card displays: 
●​ Elapsed time — how long the mission has been running. 
●​ Mission state — the current phase of the mission. 
●​ Swarm ID — the identifier for the drone group. 
●​ Zone — the area being searched. 
●​ Algorithm — the search pattern in use. 
●​ Sensor coverage — how much of the zone has been covered by the drones' 
sensors. 
Below this, a resources sub-panel shows the individual drones in the mission. Drones that 
are actively searching are shown as circles under Scanning. Drones that are currently 
following a detected object are shown as red eye icons under Tracking. If many drones are 
occupied with tracking, fewer drones are available to scan new areas. 

---
**[Page 82]**

Further down, a list of detected objects is shown. Each object entry displays: 
●​ Type — person, vehicle, boat, or unknown. 
●​ Number of tracking drones — how many drones are currently following this object? 
●​ Policy level — which tracking policy is applied to this object. 
You can click on any object in the list, or on the map, to expand a details panel showing: 
●​ Time since the object was last seen by a drone. 
●​ Classification confidence — how certain the system is about the object type. 
●​ Estimated size of the object. 
●​ A dropdown menu to change the object's assigned tracking policy. 
●​ A "Center map" button to pan the map to the object's location. 
●​ A "Camera" button to activate a live feed from a tracking drone, allowing you to view 
the object directly through the drone's sensors. 
To end a mission, press the Cancel button on the mission card. 
A summary of completed missions is shown at the bottom of the panel, listing the total 
duration, swarm ID, and zone name for each finished mission. 
 

---
**[Page 83]**

C
Introduction to the task
(Scenario 1 and 2)
77

---
**[Page 84]**
*(This page contains a figure/chart/image not captured in text)*

Introduction to the task 
During the last week, there have been several “strange incidents” at military sites across 
Sweden. Sites have been damaged by saboteurs, and unauthorized people have been seen 
in no-entry zones. The general security political situation has escalated, and the government 
has ordered the national guard to guard important military sites across the country. As a part 
of this, you have been tasked with surveilling a peninsula near Västervik that contains three 
security-sensitive sites.  
Operating a swarm of up to 50 semi-autonomous drones, through the HMI that you just 
familiarized yourself with, your objective is to detect and monitor any potential threats to the 
three security-sensitive sites. People, cars, and boats will be moving around the area as part 
of normal daily activity, meaning that it is your job to determine what constitutes a threat. 
When you identify a threat, notify the researcher and describe what you have found and 
where, then return to your task. 
Setting 
This is a map of the area you will be surveilling, with the 3 security-sensitive sites marked 
with three red circles: 
 
●​ The site located to the north is an important military communications location 
●​ The site located by Gränsö Slott is a military storage unit  
●​ The site located to the east is an important telemast. 

---
**[Page 85]**

D
Introduction to the task
(Scenario 3)
79

---
**[Page 86]**

Introduction to the task 
 
 
 
Task 
During the last week, there have been several “strange incidents” at military sites across 
Sweden. Sites have been damaged by saboteurs, and unauthorized people have been seen 
in no-entry zones. The general security political situation has escalated, and the government 
has ordered the national guard to guard important military sites across the country. As a part 
of this, you have been tasked with surveilling a peninsula near Västervik that contains three 
security-sensitive sites.  
Operating a swarm of up to 50 semi-autonomous drones, through the HMI that you just 
familiarized yourself with, your objective is to detect and monitor any potential threats to the 
three security-sensitive sites. People, cars, and boats will be moving around the area as part 
of normal daily activity, meaning that it is your job to determine what constitutes a threat. 
When you identify a threat, notify the researcher and describe what you have found and 
where, then return to your task. 
During your shift, a military exercise will also take place. A CB90 assault craft will depart 
from the security-sensitive site at Gränsö slott, navigate around the peninsula, and proceed 
east into open water before returning to base. You are expected to monitor the vessel's 
passage while maintaining your broader surveillance responsibilities. You will be notified 
before the exercise begins and given time to plan. When you are ready to proceed, notify the 
researcher and the exercise will be initiated. The route is marked on your map. 
 

---
**[Page 87]**
*(This page contains a figure/chart/image not captured in text)*

Setting 
This is a map of the area you will be surveilling, with the 3 security-sensitive sites marked 
with three red circles, and the approximate route of the military exercise is marked in yellow: 
 
●​ The site located to the north is an important military communications location 
●​ The site located by Gränsö Slott is a military storage unit  
●​ The site located to the east is an important sensor unit.  
 

---
**[Page 88]**

E
Inject timelines
82

---
**[Page 89]**

Inject timeline 
 
Scenario 1 
●​ Inject mot slottet aktiveras (10 min) 
●​ Inject mot östra udden aktiveras (10 min) 
Efter  1 min 30 sek aktiveras: inject mot huset 
●​ Inject mot huset 2 aktiveras (08.33) 
 
Scenario 2 
●​ Inject mot huset 2 aktiveras 
○​ :08:33 min till det att antagonisten hoppar på båten igen 
●​ Efter 1.30 sek: Inject mot huset 1 aktiveras (07.20 min till antagonisten hoppas på 
båten igen) 
●​ Efter 7.15 sek: Bil Inject mot slottet (2 min) 
 
Scenario 3 
●​ Efter 10 min: Stridsbåt åker ut mot vattnet 
●​ Efter cirka 45 min aktiveras switchen för båt attack mot östra udden 
 

---
**[Page 90]**

F
CDM Probes
84

---
**[Page 91]**

CDM 
Nu är det dags för den semi-strukturerade intervjun. Vi ska nu gå igenom det du nyss gjorde. 
Fokuset är på hur du upplevde situationen du befann dig i och varför du tog de beslut som 
du tog. Vi kommer gå igenom videoinspelningen i flera omgångar så att jag får en så 
helhetlig bild som möjligt av din upplevelse.   
 
För att börja med att skapa en första ansatts; om du skulle rapportera eller förklara vad som 
hände under ditt försök till en operatör som hade passet efter dig, hur hade du förklarat 
händelserna? Vad var det som hände? 
 
Om du skulle konstruera en timeline, hur skulle den se ut? 
 
Det första steget är att identifiera den delen av video-inspelningen vi tycker är mest 
intressant. Stora delar övervakning består av att vänta, så vart behövde du börja styra 
drönarna? Finns det flera intressanta sekvenser?   
 
Probes 
Runda 1: Vad hände? 
Runda 2: Vad gjordes? 
Runda 3: Varför gjordes det och baserat på vad? 
Runda 4: Vad kan förbättras, var det tillräckligt? 
Runda 5: what if? 
 
 
Information 
●​ Vilken information använde du när du fattade detta beslut eller gjorde denna 
bedömning? 
●​ Hur och var fick du tag på denna information? 
●​ Vad gjorde du med informationen? 
●​ Hur förstod du här svärmens beteende? Vad håller den på med? 
 
●​ Hade du tillräcklig information för att fatta ett beslut? 
●​ Hade du tillräckligt med information för att göra en bedömning? 
Mål och prioriteringar 
●​ Vilka var dina specifika mål och prioriteringar vid den här tidpunkten? 
●​ Vad var viktigast att åstadkomma i det här skedet av incidenten? 
●​ Hade du en bild av vad som var viktigast vid den här tidpunkten? 
Alternativ 

---
**[Page 92]**

●​ Vilka andra handlingsvägar övervägdes eller var tillgängliga för dig? 
●​ Hur valdes detta alternativ, eller varför avfärdades de andra? 
●​ Följde du någon regel när du valde detta alternativ? 
 
●​ Kände du att du hade kunnat agera annorlunda, i så fall på vilket sätt?  
Bedömning 
●​ Om du ombads beskriva situationen för någon annan vid det här tillfället – hur skulle 
du sammanfatta situationen? 
Risker 
●​ Villka såg du som de största riskerna när du tog beslutat? 
 
●​ Såg du några risker kopplat till autonomin i systemet kopplat till beslutet? 
●​ Var du orolig att du någon gång saknade information eller förmåga att styra 
systemet? 
Mentala modeller 
●​ Vad var de förväntade konsekvensera av den häråtgärden?  
●​ Hur förväntade du dig att händelseloppet skulle fortsätta? 
●​ Stämde förväntade konsekvenser överens med faktiska konsekvenser? 
Beslutsfattande 
●​ Vad fick dig att inse att detta var rätt sak att göra i det här skedet av incidenten? 
●​ Hur stor tidspress var inblandad i beslutet? 
 
●​ Hade du tillräckligt mycket tid för att fatta beslut?  
●​ Vad hade krävts för att göra beslutet lättare att ta? 
●​ Vad hade krävts för att du skulle kunna ta ett beslut? 
Kontroll 
●​ Vilken styrningsmetod används du mest? Varför? 
●​ Hade du tillräckliga verktyg för att styra svärmens beteende? Varför, varför inte? 
●​ Hade du förtroende på att styrningen skulle ha önskad effekt? 
●​ Hade du förtroende för att du kunde uppnå ditt mål med hjälp av verktygen du hade? 
 

---
**[Page 93]**

What if’s 
What if, Drone errors: malfunctioning sensors, less or more drones.  
-​
What if you had less drones? would this decision change? 
-​
What if the drones have less battery time? 
-​
What if drones lose connectivity?  
 
●​ Hur hade det känts att ta beslutet kring att skjuta när ett hot identifierats? 
●​ Hade du varit bekväm att försvara ditt beteende under uppgiften inför en kollega? 
Inför rätten? Varför, varför inte? 
○​ Med bakgrunden av vad som missades, ändras svaret?  
Sammanfattning 
Sammanfatta det deltagaren har sagt 
 

---
**[Page 94]**

G
Timelines
88

---
**[Page 95]**

Timelines 
Deltagare 1 
Participant1 took part in scenario 2.  Participant 1 was the only participant that recieved no 
alert for any of the two injected breaches of the security sensitive sites. His trial has one 
primary phase which is surveillance, and three smaller planning phases. He does not 
preform any large re-planning sections.  
 
The first few minutes of the trial is spent planning the zones and deploying drones to them. 
Each site is given it’s own zone and each zone gets 10 drones each. The zones are named 
based on the function they serve: Comms, Telemast, Storage. At 04.50 the initial planning 
phase is done and the long surveillance phase begins. a0 
 
Initially the participant is trying to get access to the camera, and is trying to do that through 
the sensor-object list, which does not work. At 05.15 he seemingly connects that the issue 
with being unable to click the camera button has to do with the sensorobject not being 
tracked. So he finds a mission that has tracking symbols, and reaches the camera for the 
first few sensorobjects.  
 
At 06.25 he comments that he wants to be able to comment on the sensorobjects. *** 
 
At 07.36 the most intense section of the trail commences, an alert pops up while he is 
clicking on the sensor-object list. He comments “oh shit” and notices the alert almost 
immedietly. 07.47 he clicks on view, at 08.05 he clicks acknowlege and the resolve at 08.08, 
and at 08.21 he is back to the main surveillance phase looking at sensorobjects. In the 
Interview he details that he read that the alert was in regards to the loss of tracking on a 
sensorobject, and that he thus judged that is was not a threat. 
 
At 10.17 he comments that he can not map which mission/play is the corresponding one on 
the map. After some issues he finds the comms zone listed within the mission.  
 
At 11.15 the participant concludes it seems to be calm, and returns to the surveillance 
phase. In the interview he reasons that a reason that he spend more or less time on an area 
is the number of sensorobjects. During the trial, only the Warship is set to ignore, since the 
other sensorobjects are seen as suspect enough to maintain drones on. He specifically lists 
objects not being stagnant, as a reason to maintain tracking.  
 
At 11.50 the participant sees that two cars are outside of the Comms zone, and thus decides 
at 11.55 to redraw that zone. He thus reinitieates the planning phase. At first he has a hard 
time finding the zone, and he then realizes that he can not alter or delete an existing zone. 
He then cancels the existing mission on the comms zone, waiting until they’re back, and at 
18.38 he draws a new zone, Comms Large, and deploys his drones there. In the interview, 
he describes how he viewed replanning the plays as a risk, as it leaves the zone 
unsurveiled. He also reasoned, that he realized in hindsight that he could have sent out the 

---
**[Page 96]**

new play while the old one was ongoing, instead of waiting until the drones got back, but he 
did not realize this during the trial. He is also clear that it would have been able if he was 
able to dynamically alter the number of drones in a play while it is ongoing, and that he 
similarly would have liked to be able to alter the borders of zones, and delete them after they 
have been defined.  
 
At 24.02 he is seemingly trying to figure out why so many drones are tracking one single 
sensor object by clicking through the sensor object list. He is seemingly confused by the fact 
that there are two drones on the same object. This, however, is an illusion, which he realizes 
at 25.54. Here, he comments that he was unsure because he was too far away on the map. 
 
At 26.30 he comments that he would like to be able to comment sensorobjects. 
 
27: press ignore på krigsskepp. In the interview the participant explains that he assumed that 
command knows that the warship is there, and that it is theirs. Otherwise, there is no reason 
for it to be there.  
 
At 43.47 he reinitieates the planning phase , pulling in the comms drones, and reassigning 
20 drones to the zone. This was seemingly because of the coverage, as he has commented 
on the drones behaviors before. 
 
At 45.27 he is still haveing issues accessing the camera of specific sensorobjects. 
 
At 55.54 the participant sees that the drones in the Telemast area are clustering inland, away 
from the security sensitive site. He also notices that his coverage of the zones are quite low, 
around 25%. Therefore, he decides to increase decay for the Storage zone to 300 at 57.52, 
the Comms zone to 300 at 58.36 
 
The rest of the trial is uneventful. 
 
When reasoning in generall about his level of control over the drones, he says that he would 
have preferred to be able to manually steer a drone in sections of the trial, to be able to look 
at specific areas more closely. He generally however, thinks that he had enough information 
to make decisions. 
 

---
**[Page 97]**

Deltagare 2 
Participant 2 took part in scenario 2. Participant 2’s trial is characterized by repeated 
frustrations with the limitations imposed by the HMI, stopping him from making decisions. 
These frustrations permeate all phases of the trial, which can be divided into 5 different 
phases. These include 1) Planning, 2) Active Surveillance, 3) re-planning, 4) Inactive 
surveillance, 5) the incident.  
 
The first phase, planning, starts by painting 3 separate search zones; one for each security 
sensitive sites. These are named based on the type of security sensitive site it is, so the 
zone around the house is named comlock (for communications location), the one around the 
chateou is named “Slottet”, and the one on the east cape is called “TeleMast”. The zones are 
defined based on the percieved access points. The participant highlights that the roads are 
therefore important. At 03.47, 30 drones are sent to the chateau and at 03.52 the participant 
send 15 drones to the house, altering the algorithm because the shape of the comlock zone 
is jagged. In the interview however, he refelects tha  does not think this lead to a visible 
difference.  The last zone, the TeleMast zone on the eastern cape receives the remaining 5 
drones, but the participant writes 15 in the Drone Count field and seemingly thinks that is the 
number of drones he has dispatched. At 04.50 the participant watches the map to verify that 
the drones have been deployed. At 05.18 the participant realizes that he might want to 
reallocate the drones and that he might want some surveillance over the inland roads, to get 
earlier warnings of objects entering the area, but he decides to do neither of these actions, 
because he will then need to call back the drones on the ongoing missions, loosing 
coverage.  
 
Around 05.50 the participant initiates the second phase. At 06.07 he tries dubbleclicking 
sensorobjects on the map in order to get access to it’s camera feed, when it doesn’t work he 
is delegated to scrolling through the plays-panel looking for a “Camera” button. I aid in 
navigating him in the interface by tipping him that he only needs to click once on the 
sensorobject. Around the same time, at 06.13 he finds the camera button in the plays panel 
and surveils the poolboy placed outside of the chateau. Then he continues by looking at all 
other sensorobjects found around the chateau, except the moving cars. The other zones 
have yet to find any sensorobjects. At 06.50 he concludes that everything seems normal. 
After which he continues surveil the area.  
 
At x he places the three people on a walk on ignore because he has looked at them too 
many times and decided they are unimportant.  
 
At 07.31 an alert pops up in the alerts panel, which he catches immediately. He clicks the 
view button on the alert, then clicks the sensorobject it concerns, and then the camera 
button, accessing the videofeed. He tries seeing what has happened, but the drone stops 
tracking the sensorobject and flies away at 07.43. He clicks the alert again, but since there is 
no drone tracking the object, he is unable to get a camerafeed. He tries multiple times, and 
then tries clicking the view button again. He then resolves the alert. At 07.57 he concludes 
that there must have been someone that disappeared. To reach this conclusion he might 
have read the alert message. At 08.11 he comments that he would have liked placing 
increased surveillance around that area, but since he does not want to redraw and replan his 
zone he does not and instead resolves the alert. In the Interview he describes that since he 

---
**[Page 98]**

had no way of controlling where the drones were flying, and no clear path of action, he was 
forced to abandon the alert, resolving it. After the alert has been resolved, the participant 
returns to their original surveillance behavior.  
 
During this he notices multiple limitations to the interface and comment on the. After the alert 
at 08.15 he comments that he would have liked to place a comment on the alert. At 09.15 He 
comments that he wants to be able to zoom in on sensorobjects in the camera feed to get a 
better view. At 10.15 he comments that he would like to place an automatic alarm if 
something enters a search zone in low activity zones like the TeleMast, or ComLock zones.  
 
At 12.55 he decides to try to alter his zones, but realizes at 13.16 that it is not possible, 
leading him to abandon the try. In the interview he describes that he regrets sending out all 
drone at the same time, as it forces him to remove coverage entirely from a site. This can be 
viewed as a slow start to phase 3; replanning. After the attempt however, he returns to his 
surveillance phase.  
 
At  13.31 he sees objects in the water that the drones do not pick up on currently. He 
comments that he wants to follow these objects, but he can not. He points out that he does 
not even know where the drone is currently placed in the map, as there is no corollary on the 
map showing which drones camerafeed we are looking at.  
 
At 14.39 he has looked through all sensorobjects that have been detected so far, and wants 
to be able to tag them, so that he does not forget what they are and goes back looking at 
them needlessly.  
 
At 17.15 he decides to define new search areas in order to detect more sensorobjects, and 
thus properly initiates the third phase of re-planning. He starts by defining a new zone. He 
wants to name the zone TeleMast 2, but instead renames the “Slottet” zone. He then cancels 
the old TeleMast mission by scrolling down to the mission in the plays panel and canceling. 
He then waits for the drones to arrive back at the nest. At 19.17 he comments that he is very 
unsure how far along the cancellation has gone. At 19.31 it is finished, but he is still looking 
for confirmation at 20.11, looking at the map. At 20.15 he decides to initiate the new mission. 
He creates a new play, at 20.30 he notices he only has 5 drones available. He decides to 
send them out anyway and does so at 20.39 to the old “Slottet” zone, now called TeleMast 2. 
What follows are a series of scrolling, zooming and clicking behaviors that is hard to 
determine the reason for. But at 22.04 the participant comments that he seems to have lost 
drones and that they have not been deployed to the newly defined zone. I share his 
assessment and go looking for technical help. 
 
The participant is helped in figuring out what has gone wrong and realizes the naming issue 
at 27.06. He names the earlier defined zone to “TeleMast 2” at 27.20, and renames the 
“slottet” zone to its original name at 27.40. He also realizes the numbering issue initiated at 
the start of the trial. At 28.51 the 5 drones are deployed to the correct zone called TeleMast 
2. After the technical issues have been solved, the participant returns to phase 2, of 
surveillance. When recalling this segment of the trial, he reflects that he is taken out of the 
scenario a bit, and that he steps into a engernerring roll, trying to understand if the 
simulation software has failed. He also reflects on inconsistent naming conventions within 
the HMI, like the top resource panel having different names than in the plays-panel, and the 

---
**[Page 99]**

plays panel not having the name of the zone as the title of the play, making it harder to find. 
He also explains how there is no connection between the map and tha plays panel, also 
making it harder to map the play to the zone.  
 
At 29.55 he comments that he would like to change the zones, but that he can not. At 30.06 
he decides to not change the zones to not loose coverage, but at 30.55 he decides to define 
a new zone, Comlock 2, but says that he won’t use it. At 30.58 he initiates defining the area, 
and he finishes at 31.12. At 31.54 he changes his mind and cancles the ongoing play in 
comlock 1, and at 32.48 he decides to define a new play for telecomm 2, but this time with 
less drones to have some in reserve. He send the drones out again at 33.23.  
 
After a while, at 33.42 he notices that the drones are congregating towards a single area in 
the new TeleMast 2 zone. To improve coverage around the east cape site, at 34.00, he 
sends 5 more drones go the original TeleMast site. In the interview, he describes that in this 
instance he is working around the system. A recurring theme in the interview is him bringing 
up that he was not pleased with how the drones were distributed across the search areas. 
He also describes how he did not trust that the entire area was properly covered, and that 
even though the sensor coverage is listed in the interface, it did not give him any further 
value. When defining the new search area, he forgets to press start, which he realizes at 
35.58 and thus clicks start. After redefining the area, and deploying drones to the inner zone, 
he feels confident that he will be able to find if anyone enters the restricted site.  
 
After this the participant becomes increasingly inactive, and no further re-planning is 
preformed, and he largely returns to phase 2. In the interview he describes how it was quite 
calm during this part and that he could then relax, and let the system work for him.  
 
At 36.53 he is still having issues with accessing the camera on tracked sensorobjects, as 
well as 38.04. At 38.43 he looks closely at sensorobjects that should have been ignored by 
the drones, that seemingly are still being tracked. There is no tracking icon, but the drones 
follow the objects on the map.  
 
At 47.13 de comments that it seems calm, and thus initiates an inactive surveillance phase, 
where he leans back and do not interact with the interface. 
 
At 51.29 he comments that he would like to remove the zones he is currently not using, but 
is unable to do so.  
 
At 51.13 he decides to cancel the internal ComLock zone. At 51.30 he decides to make a 
new zone called Comlock 2. At 51.54 he initiates a new play, which he starts at 52.29, 
sending 5 drones to the new zone around the house site.  
 
At 54.19, the first alert pops up, which initiates the last phase: The incident. The alert is 
percieved by the participant at 54.20, at which point he clicks view, sees the alert on the 
map, and clicks on the person running towards the sensitive site at the chateau on the map. 
He tries clicking on the sensorobject but misses. He then tries clicking view again, when 
nothing happens, and the person has momentarily stopped he is able to click the 
sensorobject (54.36), scroll through the plays panel, and press the camera button (at 54.40). 
At which point he can see the person running, placing something at the scene. Here he 

---
**[Page 100]**

decides it is an active threat (at 55.49) and notifies me of the incident. He also marks the 
person sensor object as very important to follow it (55.57). He then sees the person running 
towards the parkinglot, where a car has parked. The person disappears in the car (55.04), 
and since the car has not been identified by the drones as a sensor object, the participant is 
not able to follow the car. At 55.16 the participant notices this. At 55.49 the participant sees 
the rest of the alerts. At 55.51 he clicks view on the second top alert, at 56.19 he clicks on 
another alert, moving him on the map to the TeleMast zone where alerts have also popped 
up. At 56.37 the participant comments that he really doesn’t know what to do now since he 
does not have the ability to investigate further what happened at the alerts. For example, he 
would like to be able to manually steer drones to investigate if there are any sensorobjects 
that the drones have not picked up on.  
 
In hindsight he describes how he felt like he had limited opportunities to investigate and act 
in connection to alerts. He also describes how his attitude changed after the incident. For 
example, he felt like it was now more important to change his zones, but he still felt like he 
was unable to due to the risks. He recurringly reflects on alternative ways of allowing the 
operator to practice more control over the drones, like for example, being able to highlight 
important areas, scattering the drones at will.  
 
After the incident, the participant returns to passive surveillance.  
 
When asked if he would be comfortable in taking responisbility for his behavior in court or a 
similar scenario, he says that he would not be, as he does not feel comfortable with the 
interface.  
 
 

---
**[Page 101]**

Deltagare 3 
Participant 3 took part in scenario 1 and was mostly characterized by restlessness, which he 
showed through experimenting with the interface. The trial can be divided into 5 phases. 1) a 
short planning phase, 2) surveillance, 3) increased restlessness, 4) further increased 
restlessness and play, and 5) the incident. 
 
The first phase starts with the participant specifying three zones: Adam, placed around the 
chateau, Bertil, placed around the house, and Caesar, placed around the telemast. Each of 
these zones were given 10 drones each. At 02.52, the participant reasons that since he has 
20 drones more, he’s going to make larger zones that cover more of the inland to gain an 
overview of the areas surrounding the security-sensitive sites. Thus two more zones: David, 
placed along the road out from the chateau towards Västervik, and Erik, placed after the 
chatteau along that same road, were created at 03.07 and 04.08 respectively. At 04.35 the 
participant has deployed all his drones and initiate the second phase: surveillance. 
 
At 04.35 he looks through the sensorobjects displayed on the map, and finds the camera of 
the drones tracking them. At 05.40 He comments on the warship; “warship? that does not 
sound good”, and “have that been there all this time?”, but takes no further action. He then, 
at 05.45, asked if that is expected. I answer yes.  
 
At 06.55 he comments that he would like to have an autoscroll function so that when clicks 
on a sensorobject, the plays-panel autoscroll to that sensorobject, making it easier to find the 
camera. 
 
At 07.33 the first alert pops up, and almost simultaneously, the participant notices it. He 
clicks view. Notes that a drone has lost tracking of a person (07.47) through reading the 
alert, He reasons that this was probably a lost tracking alert for the person that was standing 
outside the floating sauna, and thus dismisses the alert as unimportant. At 07.54 he clicks 
acknowledge and resolve in quick succession.  
 
At 09.00 he comments that it would be nice to connect the plays-panel.  
 
At 09.11 the participant notes that something must have gone wrong when he deployed the 
drones because no drones have yet to reach Erik. He concludes that he must have clicked 
on the wrong button somewhere and decides to create a new play on 09.30. He is however 
interrupted by noting a moving car by the chateau.  
 
09.41 the participants notes a car moving away from the chateau on the map. He comments 
that “now the car is leaving, or it’s another.. or?”, the car referring to the car parked on the 
parkingslot outside of the chateau. At 09.45 he sees that a car is still parked on the 
parkingslot in the same spot and concludes that two white cars changed places, and 
comments that its suspicious and marks it as very important. When nothing further happens, 
he return to creating a new play, and does at 10.18. 
 
At 10.41 he comments that he feels like he has good oversight over his sensitive sites. 
 

---
**[Page 102]**

At 11.06 he decides that the suspicious car was probably not actually suspicious, and marks 
it as low priority instead. 
 
At 16.35 he comments that he would almost like to map views, when he zooms in to have 
general oversight even when he focuses on something else.  
 
At 13.37 the participant is getting visibly bored and restless, which I shall call the restless 
phase. The participant spends the majority of his trial in this phase, and includes things like 
him creating stories and talking about the characters in the simulation, and starting a “guess 
the car color”-game on the car sensorobjects in the section of the trail. However, he 
maintains surveillance and frequently looks at sensor-objects, some having become familiar 
to him. 
 
At 21.20 he comments that he can’t move the borders of the zones, and that he would like 
that. 
 
At 22.10 he is looking at two sensorobjects that he can not see in the camera feed. To gain 
access to the camerafeed he tries multiple times to click at the objects on the map, but since 
they are moving he misses a few times, before being able to access the camera. He reasons 
that these are people inside the house, or maybe they are walking underground, or the might 
be ghosts. Based on this I think he interpretes the situation as being a failure in the 
simulation.  
 
22.55 he comments on the behaviour of the drones and reasons that it might become better 
if he increases decay. At 23.05 he increases Bertil and Ceasar to have a 120 decay. 
 
At 33.45 he surveys the warship again, and decides that it is time to ignore it. He clicks on 
the warship in the sensorobject list, which closes the menu with the tracking policy control. 
He clicks again and is then able to alter the tracking policy.  
 
At 36.05 he realizes that his zones was pretty sloppily drawn, but since he is unable to alter 
the existing borders he abandons that mode of thinking. He also decides to release the 
people walking outside the chateau, and lowers the person marked to important to low 
priority again. 
 
The coming section is marked by increasing restlessness. At 38.30 he starts guessing which 
color car the sensor object he clicks on will be. At 47.10 he cancels Erik’s mission, since little 
is happening in that area, in order to send out less drones, ensuring that he has two over to 
play with. At 47.40 7 drones are thus redeployed to the Erik zone, and he has drawn a new 
area “point”, a small area in the middle of the field above the chateau, and sends the 
remaining 2 drones there. At 48.54 he comments that he would like to be able to look down 
on the area below him in the camera feed. At 49.05 he cancels the play on point because 
nothing is happening there. He then proceeds to draw a new section that he calls “provoke” 
right by the no-fly zone over västervik at 49.35 and he starts a new play there at 49.57.  
 
At 52.25 he comments that he would have liked to be able to tag or comment sensorobjects. 
At 57.37 he comments that there is no delete function for zones. 
 

---
**[Page 103]**

At 57.30 the participant starts playing with the zone types of point. And at 57.52 he says, 
“Ha! I know what Ill do”. at 58.52 he creates a new play that he sends to point, and when the 
drones have reached the zones at 58.45, he switches the zonetype from area of interest to 
no fly zone. Nothing happens. 
 
This type of play, of creating new zones and sending out drones to these new areas continue 
for a couple of minutes, until a alert pops up, thus initiating “the incident” phase. 
 
At 1.07.33 the alert pops up, which the participant catches almost immediately. He zooms in 
on the affected area, and sees that there’s a boat that has arrived to the house. At 1.07.41 
he gains access to a camera of the boat through the play panel. He reasons that there is a 
boat and a person at the site, and comments that it would be nice if the drones tracked the 
person. At 1.07.52 the other boat, and person involved in the play can be seen on the map, 
but this is not noticed by the participant. At 1.08.14 the participant identifies the other person 
involved and gets a camera view of them. He places this person to very important at 1.08.27, 
but since this sensorobject is removed from view, the drones do not follow any of the escape 
boats. After the incident, the participant goes through all alerts, acknowledging and resolving 
them, When they zoom out, there is no trace of that incident on the map, thus no alert had 
been produced for the other inject. 
 
 

---
**[Page 104]**

Deltagare 4 
Participant 4 took part of scenario 1. Usually this entails the chateau, and the house to be 
attacked at the same time, but due to a technical malfunction with the simulation software 
the chateau was never attacked. This participants trial is marked by extensive re-planning 
periods trying to improve the drones behaviors. Participant 4’s trial can be divided into 6 
different phases/activities: 1) Planning, 2) Area Familiarization, 3) Re-Planning, 4) Overview 
5) Improving Drone Behavior, and 6) The incident. Though phase 4 and 5 happen dispeared 
between eachother.  
 
The first phase lasts the first 2 minutes. During this phase, the participant chose to divide the 
drones across two different zones: where the first zone covered both the house and the 
chateau, because they are placed closer together, and the second zone covered the eastern 
cape. The first zone was named O1 and given 20 drones, and the second was named O2 
and given seven drones. In interviews he says that he was experimenting during this phase, 
and was still not entirely familiar with tha interface. His decisions are thus based on intuition 
and guessing rather than strategy. After sending out the drones to these areas, he started 
surveying the first sensor objects detected and initiated the second phase of area 
familiarization.  
 
At 02.10, the participant navigates himself to different sensor objects through the tracking 
icons in the plays-panel, accessing the camera of the drone tracking them. He identifies the 
warship positioned at the dock and decides it is not dangerous, but friendly, and chooses to 
change its tracking policy to ignore. He clicks at a row in the play-panels sensor object lists, 
hesitates, likely because no camera feed came up, and then again uses the tracking icons to 
access a camera. A person is surveyed at 02.25 and put to neutral because they are further 
away from the sites. The participant again tries to access the camera through the sensor 
object list, then tries the tracking icons between these sensorobjects. At 02.53 a car is 
surveyed and set to ignore because it is moving away from the chateau. The participant then 
clicks the first tracking icon, revisiting the person but quickly clicks to the next icon. At 03.00 
a person is identified at a dock by the hotel above the chateau, due to their greater proximity 
participant 4 choose to mark this person as very important. All sensorobjects of one zone are 
not surveyed in order, or at one time. Instead, the approach is unstructured. Not all 
sensorobjects are survey before 07.30, when an alert pops up. 
 
At 07.30 the participant is surveying a blue car driving towards the chateau when the first 
alert pops up in the alerts panel. At 07.39 the participant moves his mouse to the alerts 
panel, meaning that the alert has been percieved. Exactly when this object is perceived, or if 
it is through the map or the alert-panel is unclear both based on trial footage and interviews, 
At 07.50 the participant clicks the view button of the top alert, but nothing happens. He then 
clicks acknowledge, and view at 07.58; nothing happens. When he clicks again and nothing 
happens, he decides to look through the HMI instructions to see if it includes any relevant 
infromation. At 08.37 the participant tries to lower the importance of the alert through the 
decrease button. When that does not work, he decides to lower the importance of the sensor 
object.. At 09.13 the participant successfully decreases the importance of the alert, and then 
is able to resolve it. This alert was not interpreted as a threat and was not noted to the 
researcher.  
 

---
**[Page 105]**

Bring up camera, ser att det bara är en person på sin tomt, decreasar. 
 
Retrospectively, when the participant recount his experience he explains how he was 
surprised by the alert, especially as he had not seen what an alert would look like in the HMI 
introduction. He also wonders what type of alert it is and why there is one. Due to the 
distance from a security sensitive site he concludes that it likely isnt something dangerous. 
He explains how he was confused by how the resolve and decrease buttons work. He is also 
not sure exactly why the alert appeared. He guesses that it was because he put the person 
to important, but is unsure and says that the alert might have been a pre-planned part of the 
scenario. This passage of the trial is thus characterized by both a confusion about what 
actually happened, and confusion with the interface.   
 
The area familiarization activities are continued throughout the entire trial. Sometimes, 
interrupting other activities. But the goals of these activities differ throughout the trial. In the 
second phase, quick familiarization is prioritized. The goal is to quickly establish a base for 
which patterns are to be expected, these patterns are the used to understand future 
behavior.  
 
In the interviews the participant explains how he primarily relied on direction, proximity and 
context to decide if something is a threat or noise in this section of the trial. He lifts the 
poolboy as a clear example of his reasoning. He was hanging out very closely to the 
chateau, seemingly bathing, but since he is so close he could quickly decide to divert and 
enter the restricted zone, therefore he was still important to keep an eye on. 
 
At some point, the goals change to surveying alternative behaviors, and checking of objects 
deviate from the established pattern. This thus constitutes a separate phase: the overview 
phase. This phase is continues through out the rest of the trail, sometimes interrupting other 
activities. However, due to the higher familiarity of the sensor-objects, here he is also able to 
rely on normal patterns of behavior to decide if a sensorobject is important or not.  
 
After the second phase, at 09.45,the participant identifies that the zone around the chateau 
and the house catches a lot of noise. Thus, he initiate phase three, which is Re-planning. In 
the interview, the participant highlights their thinking further, describing that everything does 
not need to be surveiled, primarily because he can see that there are no roads in the middle 
of that larger area. He also describes how he drew the zones based on what he views as 
accesspoints to the sites, these primarily being roads, so it seems the environment was a 
recurring consideration. However, in a later part of the interview he highlights that his 
knowledge of the environment is limited. For exemple, he only really knows what the 
chateau looks like based on drone footage, the other sites he has no clear image of. At 
10.15 a new area is drawn around (X), and a second area drawn around the second object 
at 11.27, so that each security sensitive site has its own search area. Drones are then 
deployed to these areas at Y.  
 
When this re-planning is done, the overview phase is re-initiated. Then, it is interrupted again 
by the participant identifying a need for further re-planning in the form of more drones in O4 
at 18.30, due to the lack of sensor coverage. This is then immediately acted upon 18.32, 
where a new play is activated in the plays panel, and another batch of drones is sent to the 
area. This batch is as large as the first one (eight drones)  that was sent at O4. Since the 

---
**[Page 106]**

operator had drones left in reserve, this was done without having to cancel an ongoing 
mission and pulling in drones. After this the participant return to the overview phase.  
 
The overview phase is interrupted again by the participant identifying that O2 is too large for 
the amount of drones currently assigned, affecting sensorcoverage at 21.16. Thus, a new 
batch of drones is assigned to this area in the same way as in the first re-planning instance 
at 21.32. However, here the participant fails to alter the area to which he want to send the 
drones, and he thus send them to O4 instead of O2 as planned. The participant notes this 
lapse at 22.55. This leads to further actions, at 23.08 the created play is canceled, and a 
new play with the correct area specified is created as 28.18. After which the participant 
returns to overviewing the operations area.  
 
The fourth phase is also spread out over multiple parts of the trial. The forth phase is made 
up of all attempts, and activities related to improving the drones swarming behavior. This 
phase started at 30.22, where the participant notice that there are clustering behaviours in 
the swarm. He concludes that this might be because there are two separate swarms in O2, 
instead of just one. In the Interview, the participant clarifies that he does not identity this 
through the plays panel, but through the small textbubble next to the zone. Here he could 
see that the swarm number looked like there were multiple number overlapping, and drew 
the conclusion that there were multiple swarms on that area. Therefore, the participant 
decides to send out their remaining drones, to this area, at 32.15. And directly after, the old 
plays for that area are canceled. At 33.44 the participant notes that he is pleased for now. 
However, at 33.51, the participant notices that the drones have clustering behaviors in area 
Y, as well as in area Y at 33.57. To try to dissuade the drones from this, the participant 
decides to change the algorithm of area Y, to snake from PSO. At 34.35 the participant looks 
for confirmation that the behaviors changes, which is inconclusive, and the participant 
continues by returning to the overview phase at 35.03. 
 
In the Interview, the participant touches upon his struggles in understanding and controlling 
the swarms behavior. For example, he lifts that he does not have a clear understanding of 
the different algorithms used (Snake and PSO), as the HMI introduction only included a 
small comment on these. He highlight that it often felt like they had flocking behaviours, and 
reasons that it makes sense since PSO is inspired by the flocking hehaviors of animals like 
birds. However, he lifts that he often had a hard time understanding why they moved in the 
way that they moved, sometimes moving in lines or congregating at one area of the search 
zone. He noted that the sensor coverage shown in the HMI was sometimes marked as high, 
but that he sometimes did not trust this fully due to the flocking behaviors. On a similar note, 
he describes that it would be nice to know where the drones are going, as well as where 
thay have been. Proposing a heatmap of sorts, to mark where the drones have been 
recently.  
 
At 37.18 the participant notices that the drones are still clustering and flocking around a 
limited area of the chateau search area. A few seconds later, at 37.20 the participant decides 
to pull in the drones by canceling the play because the drones “might be tired”. However, he 
cancels the wrong mission, and pull in drones from O4 at 37.48. This mistake is identified at 
38.18 by the participant, and he then creates a new play for O4 at 38.33. However, he wait 
until the drones from the wrongly cancled play return so that he have more drones to deploy 

---
**[Page 107]**

in the new play, before clicking calculate and start. At 38.06 the participant successfully send 
out 18 drones to O4.  
 
As the clustering issue persists, the participant changes the algorithm of Area X swarm Y 
(finns ju flera plays för varje område?) at 40.59. he also seek to solve the problem through 
other venues; at 45.30 the participant looks through their zones to check if he has altered 
decay in any of them yet. he believe that he did alter it, which he did not. This might mean 
that the participant was thinking about trying to alter decay earlier but was distracted from 
making the choice. At 45.40 alters decay on zone Y. At 46.42, (det är om man skulle..? X). 
The participant again alters decay at 47.50, and he are unsure if there is actually an effect, 
but he say that it feels like it has an effect. The issues of clustering and coverage, however 
persist, which he note at 49.08 in regards to area X swarm Y. At 50.28 he also note that 
there are too few drones in O3, and pulls in the swarm from O3 at 50:13, waits until all 
drones have arrived back at the nest at 50.48, and he then deploys a new, larger swarm 
through pressing calculate at 51.22 and start at 51.29. At 55.06 decay on zone O3 is altered 
again and the participant then tries a higher decay at 1.00.07, and then a lower decay at 
1.07.10.  
 
The participant descroibes his reasoning around decay in the interview. He knew that decay 
might alter the swarms behavior based on earlier experience. For exemple, he has been part 
of the companies demos and such, and had seen visualization of how decay worked, so he 
reasoned that if he lowers decay, the drones would quicker have to come back and monitor 
the same area, and he thought that lowering decay might thus result in the drones 
distributing themselves more evenly in the search areas. However, he realized during his 
trail that it might be better to increase decay.   
 
At 56.49 a problem around the overview phase arises while the participant is clicking through 
the different drone cameras through the icons in the plays panel at 56.49. he open a camera 
of a drone that is not currently tracking a sensorobject, and uses the camera feed coupled 
with the map to identify the drones position at 56.55. 
 
1.07.29, the participant identifies a boat driving straight towards the house through the map. 
Since he now knows how boats usually drive around the site, he identifies this before an 
alert is raised. The alert is raised at (). in which he clicks at the alert message’s view, 
expecting to get a camera. When that does not work he needs to identify which play the 
object has been spotted in which he finds confusing, but he quite quickly identifies it to be 
the play in O4. He uses the plays panel (1.07.31), scrolls to the related mission in the area 
O4(1.07.43), and clicks a boat in the sensor object list, thereby receiving the desired video 
feed (1.07.44). At 1.08.01 the boat leaves the docking at speed which the participant sees, 
as well as the person that jumped unto the boat. This makes him think that the person has 
done something bad and that the alert needs to be of high priority. Quickly, the participant 
aims to mark the boat as very important, which he does through the sensor-objects list. He 
first marks another boat as “very important” (1.08.04), and then immediately (1.08.10) makes 
the intended boat as very important. In the interview he reasons that it was likely because he 
didnt get any feedback that the boat was followed, so he thought something went wrong and 
tried to mark it again on instinct, accessing the right boat. At 1.08.40 (??) the participant 
sees that both boats he marked is making their way away from the site and exclaims 
“There’s two boats?”. Making it clear that he was previously not aware of the fact, which he 

---
**[Page 108]**

also highlights in interviews. He decides that the boats should be followed and thus leaves 
them as marked as very important, while he starts seeing to the alert messages. At 1.09.08 
he tries to resolve the alert, but he is unable to. However, he brings out the extended view of 
the alert, writes a message (1:09:14), and is then able to resolve the alert.  
 
In hindsight, when asked to reason about what happened the participant guesses that there 
were two boats that might have been involved in the incident, and that one boat might have 
made sure the antagonist accessed the site through one side, while the other was his 
get-away, but he says that it feels weird to do it that way. But he says that he really does not 
know, and that it would be necessary to review camera footage around the scene afterwards 
to know for certain.  
 
 

---
**[Page 109]**

Deltagare 5 
The last participant took part in the last scenario. This participant was the most unfamiliar 
with the interface. This scenario is also different from the others due to the military exercise 
initiated 10 minuted into the trial. This divides the trail into a 10 minute long pre-exercise, 
consisting primarily of planning, a 30-minute-long exercise phase, a surveillance and 
replanning phase and lastly an incident phase before returning to the normal surveillance 
patterns before terminating the trial.  
 
This participant was less familiar with the HMI and simulation software then the rest of the 
participants which became clear during the interview. He outlines a few of the 
misunderstandings that he had in the beginning that later cleared up. Right in the beginning 
he didn’t know if he could have multiple plays active at the same time, but he quickly figured 
that out after starting. He also thought that the zones needed to be squares, but he also 
figured out that the zone shape could be different during the trial. This second 
misunderstanding shaped how he planned his zones in the beginning.  
 
The trial started with the planning phase, and in this phase the participant defines three 
different zones; POI1 placed around the house, POI2 placed around the chateau and POI3 
placed around the eastern cape. Due to the participants understanding about the shape of 
zones, all zones are squares. He also defines a fourth zone placed as a square in the waters 
to the south of the peninsula, and over the southern parts of the peninsula that he calls 
MISSION, which is the zone he will use during the military exercise later. In hindsight, the 
partcicpant tells me that he would have planned it differently if he got to do it again, instead 
planning the MISSION zone to follow the planned military exercise path. When all zones are 
defined he sends out 10 drones to each security sensitive sites (02.19).  
 
He then starts surveying the area and the sensor objects. He primarily uses the plays-panel 
to keep track of the detected sensor objects. He looks at the warship by the docks at 03.30 
and reasons that it is of low priority now, but that he will place it on very important when the 
exercise begins. He also looks at the poolboy by the chateau, navigating himself through the 
different sensorobjects using the drone icons in the plays panel. At 05.15 he scrolls through 
the plays panel and identifies that there are no sensorobjects close to the other sites as no 
sensorobjects have popped up in their corresponding lists.  
 
At 06.25 he comments that he just saw something happen by one of the other zones that he 
missed, as he sees a boat travel outside of the house. He also reasons (07.05) that he may 
have created too small of a zone for the house.  
 
The first alert pops up at 07.33. At this point he has the videofeed for the related 
sensorobject in view. He comments on the alert at 07.38. He comments that he has lost 
camera footage of the person on the jetty, and that the person has likely walked into the 
house close by. At 07.58 he clicks on view, and wants to investigate further, reasoning that it 
may have been a person spying on the military exercise. At 08.19 he reports the incident 
and leaves a comment in the alert. At 08.55 he has moved on. 
 
When reccounting his experience during the interview, he explains that he was initially 
confused about what he was expected to do when an alert popped up. So this initial alert 

---
**[Page 110]**

was like a trial-run. He for example figured out the available buttons like acknowledge and 
similar during this stage.  
 
At 09.00 he surveys a sailboat by the house and comments that it is not super suspect as 
there is a pier nearby and he moves on around 09.40. 
 
At 10.15 the military exercise is initiated and the trials' second phase commences. First the 
participant is prompted to affirm his readiness, which he does, and the warship sets out to 
sea at 10.29. In the interview, he describes how he felt ready for the mission when it was 
initiated, since he had planned beforehand. The first thing the participant does is increase 
the importance of the warship sensorobject to Very Important. When the warship leaves the 
area he notices that the drones follow the warship outside of ther administred zone, and 
comments that he did not know that previously. In hindsight he reasons that it would have 
been better if the drones following the warship had not been administered from the chatteau 
zone, since that leaves just 6 drones to defend that area. At 11.40 He deploys the remainder 
of his drones to the MISSION zone. He deemed this necessary due to the size of the zone 
he explains in the interview. 
 
At 12.36 he comments that the sailboat is very close to the house. He does not seem to 
notice that it is actually a different boat. He also identifies another sailboat through the plays 
panel, zooms in and out to find where the sensorobject is placed, first assuming it’s in the 
eastern cape, but at 13.07 he realizes that the sailboat is actually found within the MISSION 
zone. At 13.25 he comments that the sailboat by the house has been seen multiple times, 
which he views as very suspicious. He is seemingly still unaware that it is a different 
sailboat.  
 
At 15.03 he reflects that the MISSION zone is very large. At 18.07 He surveys a sailboat in 
the MISSION zone that is almost on the other side of the zone from the warship. He 
considers setting it to ignore, but refrains. At 20.11 he sees that two people have been 
spotted by the house, but that they are no longer followed. At 22.36 he lifts this issue more 
clearly to me, and at 23.12 he decides to change the trackingpolicy of these objects to 
Important to allow the drones to drive outside of the defined zone to track them. In the 
interview he says that he got the expected results, but also talks about how he is unsure how 
the alogirthmn works and if there are drones administered to the sensorobjects after he has 
changed it’s tracking policy, which is not how the algorithmn actually works. At first he 
thought it didn’t work but after a while he could see that it had.  
 
At 25.39 he notices that the warship has travelled outside of the bounds of the MISSION 
zone, but reasons that this is okay as he already has four drones on the warship due to it’s 
tracking policy. 
 
At 28.32 An alert pops up again, but this time within the MISSION zone. It is yet another lost 
tracking alert. He reads this at 28.35, and zooms in on the alert at 28.37. On the Alert the old 
message that he wrote in regards to the lost tracking alert is still visible. In the interview he 
explains that he read the comment and recognized it and therefore decided that it was the 
same alert and that he didn’t need to look into it further.  
 

---
**[Page 111]**

At 36.49 the participant aims to alter a boat in the mission zone to lowpriority, but instead he 
alters the warship to low priority, leaving it unsurveiled as it leaves the MISSION zone. At 
37.05 he exclaims “oh!”, noticing that the warship is no longer tracked he explains in the 
interview, looking through the surveillance panel. At 37.19 he comments that he has lost 
sight of the warship, and reasoned that it happened when he changed the tracking policy of 
another boat. Marking his confusion at the incident. In the interview he explains how he then 
simply had to wait to be able to find the warship again, so he therefore shifts his focus to 
general surveillance until a drone finds the warship again, which he is able to reidentify at 
39.00. And at 39.05 he alters the trackingpolicy of the warship again.  
 
When reflecting on losing track of the warship, he says that there is a technical limitation on 
the control and that he would have liked to be able to manually steer the drones in the area 
or if there was a possibility to highlight areas of the zone that the drones should prioritize. 
 
At 40.25 the warship reaches it’s original position and at 40.52 the military exercise is 
concluded and he starts the post-exercise phase. After the military exercise, the participant 
explains how he has more time to place on his other duties. At 41.22 he places the warship 
to ignore, since the exercise is concluded and he does not want any resources taken up by 
it. He also considers the distribution of drones within the zones, as he at 43.09 notices they 
cluster a lot in PO2. At 43.25 he reasons that it is probably because he does not have 
enough drones. This leads him to alter the algorithm in PO2 (chatteau) to snake. He explains 
that he doesn’t know the exact algorithm, but thinks this will spread out the drones more and 
thinks that he achieved the wanted results.  
 
At 48.10 he tries to gain a camera on the cars driving outside of the château, but since they 
are moving he tries clicking on the car and misses multiple times,. the car moving out of the 
zone, and then not being tracked anymore. In the interview he explains that there were a lot 
of objects and that he couldn’t get a hold of them as they were moving outside of the zone. 
He also says that he didn’t really understand the tracking logic, that sometimes the system 
tracks, and others not. 
 
At 48.58 the operator he decides to place the parked car to ignore because it has stood still 
the entire trial. 
 
At 50.10 he decides to create a larger zone inland, to get a better overview of the activity in 
the area. So at 50.34 he sends out the remaining 20 of his drones to the area. He then 
explores the sensorobjects that the drones find, and he looks at the person on the field (at 
51.45), he looks at the person on her pateo (at 52.01). He also surveys other sensorobjects, 
like a motorboat outside of the house. Looking at each object takes some time as he tries to 
get a sense of if they are a potential threat or not. However, in the interview he reflects that 
this zone was not very interesting.  
 
At 1h the participant uses the plays panel to finally get a camera on the cars moving outside 
of the chatteau.  
 
At 1.05.20 he comments that he would have liked to search even broader, as not much 
seems to happen within his inland zone. At 1.05.33 he thus creates a new zone. Here he 
has some issues in creating the zone as he creates a bit of a weird shape even though he 

---
**[Page 112]**

did not want to. At 1.07.21 he cancles the first mission and send out the 20 drones to the 
new zone.  
 
At 1.09.55 The incident phase is initiated as the first ALERT pops up. It is the promptly 
followed by another ALERT at 1.09.59. At 1.10.06 the participant comments that there’s a 
boat, seemingly having noticed the alert and the boat moving towards the eastern cape. 
1.10.19 he scrolls to the POI3 play-panel and access a camera on the boat at 1.10.13. At 
1.10.19 he notices that it is both a boat and a person by the eastern cape and notifies me of 
this. at 1.10.25 he places the person to very important in the tracking policy, but at 1.10.34 
the drone stops tracking, as the person disappears and the boat drives away.  
 
Afte the incident phase another low intensity surveillance phase commenses.   
 
During the interview,when prompted for how much he considered the simulation during the 
experiment he explains that it shaped his understanding of the sensorobjects. Forexample 
he consciously adapted a roleplaying mentality when he saw cars quickly trun around and 
watched some people walk around in circles around the sensitive sites. The simulation 
mostly affected his judgements around if objects where threats or not. He also explains how 
he got more confident with time, as he could more easily identify patterns. This meant that 
he was less sensitive to objects close to the security sensitive sites.  
 
When prompted about risks he reasons that coverage might be a possible issue. And that it 
is somewhat likely that he missed threats that are not direct, like people spying in the area. 
 
When prompted about his willingness to take responsibility for the results and his actions 
during the trial, he says yes, but with multple caveats. These are more experience with the 
HMI and the system, as well as all function being implemented, and further abilities to control 
the drone swarm. When asked if his answer would have changed if he had missed an attack, 
he also answers yes, because it means he must have done something wrong. 
 
