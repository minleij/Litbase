# SA-Tracer A tool for assessment of UAV swarm operator SA during mission execution

*Source file: SA-Tracer_A_tool_for_assessment_of_UAV_swarm_operator_SA_during_mission_execution.pdf — 9 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

SA-Tracer: A Tool for Assessment of UAV Swarm
Operator SA during Mission Execution
Florian Frische and Andreas L¨udtke
OFFIS - Institute for Information Technology
Oldenburg, Germany
Abstract—Maintenance of Situation Awareness (SA) during
supervision of a swarm of highly autonomous Unmanned Aerial
Vehicles (UAV) is a complex and visually demanding process.
A solution for supporting UAV operators are Intelligent SA-
Adaptive Interfaces (ISAAI), which dynamically adapt to the
individual SA needs of operators. However, the successful deploy-
ment of ISAAIs depends on a suitable tool for assessing operator
SA during mission execution. In this paper we present the tool
SA-Tracer. SA-Tracer implements a formal situation model and
analyses the scanning behaviour of UAV swarm operators in
order to infer and assess SA on a formal basis. We present
results of a ﬁrst experiment performed in order to evaluate the
suitability of SA-Tracer for the intended context of use and the
validity of SA assessments produced by the tool.
I. INTRODUCTION
Today, typically a team of two or more human operators
operates one Unmanned Aerial Vehicle (UAV) via dedicated
Human Machine Interfaces (HMI) [1]. However, it is of high
interest for civil and military surveillance missions to let only
one human operator operate a swarm of many UAVs [2], [3]
(see Fig. 1). The expected beneﬁts are, e.g., reduced costs for
personnel, higher system reliability and resilience, and better
coverage of large areas. A UAV swarm could, e.g., be used to
scan a broad coastal area after a naval accident faster in order
to safe human.
The key for the development of this future concept of
operations is a high level of autonomy as it reduces the time
needed to operate each UAV [4] and the cognitive workload
[3]. Due to the high level of autonomy the operator will be
pushed into the role of a supervisor in charge of high level
planning tasks. Therefore, the operator needs good situation
awareness (SA) at any time of the mission.
Endsley [5] deﬁned SA as a state of knowledge in-
cluding the perception of the elements in the environment
(SAlevel1), the comprehension of their meaning in terms of
goals (SAlevel2) and the projection of their status in the near
future (SAlevel3). These levels build upon each other: SAlevel1
is a requirement for SAlevel2, and SAlevel2 is a requirement
for SAlevel3.
Research has shown that human operators have signiﬁcant
difﬁculties in effectively overseeing and interacting with au-
tomated systems [3]. In fact, maintaining good SA in context
of automated systems is a complex and visually demanding
process and loosing SA can have hazardous consequences.
Experiments have shown that poor SA is a major cause of
accidents in the aviation domain. For example, Jones and
Fig. 1.
UAV operator supervising an autonomous UAV swarm on a portable
ground control station
Endsley [6] showed that poor SA accounts for more than
70% of human errors of commercial airline pilots and air
trafﬁc controllers. Furthermore, 80% of these errors were
related to SAlevel1. The operation of UAVs is very related
to manned aviation and air trafﬁc controller tasks. Thus, it is
not surprising that poor SA also accounts for human errors
during UAV missions. For example, a study by Barnes and
Matz [7] indicated that poor SA was related to errors in a series
of simulated UAV missions. A recent experiment conducted
by Cummings et al. in a UAV swarm simulation enviroment
supports these ﬁndings [8].
A solution to support UAV swarm operators to maintain
good SA during mission execution are Intelligent Adaptive
Interfaces (IAI). An IAI is a speciﬁc HMI that changes its
characteristics relative to external events in real-time in order
to improve the performance of the human-machine system [9].
The idea of using IAIs is not new for the aviation domain.
Examples are cognitive cockpit systems, such as COGPIT [10]
and CASSY/CAMA [11], which couple a situation assessment
module and a pilot state estimator to provide the appropriate
information at the appropriate time at the appropriate place.
In [9], an IAI was presented, which distributed pertinent tasks
between a UAV swarm operator and the automation based on
the estimation of workload. It was shown that the workload-
adaptive interface signiﬁcantly reduced operator workload and
- as a side-effect - also improved operator SA. However, we
978-1-4673-2437-3/13/$31.00 ©2013 IEEE
2013 IEEE International Multi-Disciplinary Conference on Cognitive Methods in Situation Awareness and Decision Support (CogSIMA), San Diego
203
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 2]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 2.
The ISAAI detects an SA-gap associated with the information object
UAV2 (Malfunction(UAV2) = FALSE) and guides visual attention from the
information object UAV1 (t1) to UAV2 (t2) in order to improve the aware-
ness of the operator for the actual malfunction state (Malfunction(UAV2) =
TRUE)
believe that improving operator SA is such an important issue
that it should be more than just a side-effect.
We envision developing an Intelligent SA-Adaptive Inter-
face (ISAAI) to support UAV swarm operators maintaining
good SA during mission execution. Basically, this ISAAI
should perform three steps: ﬁrst the ISAAI should determine
the subjective SA state of the operator. Second, the ISAAI
should assess operator SA in a very granular way allowing to
identify critical breakdowns and speciﬁc gaps in SA. Third,
the ISAAI should systematically adapt its characteristics to ﬁt
better to the individual SA needs of the operator. Speciﬁcally,
the envisioned ISAAI should guide visual attention (using
visual stimuli) of the operator to information objects associated
with SA-breakdowns and SA-gaps, in order to eliminate them
on-the-ﬂy (see Fig. 2).
However, the successful deployment of the ISAAI depends
on a suitable tool for assessing operator SA during mission
execution. This tool has to fulﬁl speciﬁc requirements. To
give just a few examples, the tool should be applicable (1)
automatically (without the presence of human experts), (2)
unobtrusively (to avoid distraction of operators during mission
execution), (3) online ( to allow the adaptation of the ISAAI
during mission execution), and (4) in real working environ-
ments. In addition, the tool should (5) track operator SA
continuously (as the need for an adaptation can be given at any
time), and (6) assess operator SA without delay (to provide the
needed adaptations of ISAAIs at the right moment). Finally,
the tool should (7) determine and assess SA on a very granular
level allowing to detect SA-breakdowns and speciﬁc SA-gaps.
In this paper, we present SA-Tracer, a tool for the assess-
ment of operator SA facing these speciﬁc requirements. SA-
Tracer implements a formal situation model and analyses the
scanning behaviour of UAV swarm operators in order to infer
and assess SA on a formal basis. We present results of a ﬁrst
experiment performed in order to evaluate the suitability of
SA-Tracer for the intended context of use and the validity of
SA assessments produced by the tool.
II. RELATED WORK
We performed an extensive literature review to assess exist-
ing techniques. A classiﬁcation of techniques can be made
by the characteristics ’direct’ and ’indirect’. While direct
techniques try to ﬁnd immediate evidence on the SA state of
operators (e.g., by applying probes or questionnaires), indirect
techniques try to infer the SA state based on observable
indications [12]. We concluded that direct techniques, such
as the Situation Awareness Global Assessment Technique
(SAGAT) [13], provide valid assessments of SA on a granular
level but are not suitable for the intended application, e.g., due
to their intrusiveness.
However, we found that indirect techniques are a promis-
ing alternative. An example is the Situation Awareness Be-
haviourally Anchored Rating Scale (SABARS), which uses ob-
servable motor actions of operators as indications of operator
SA [14]. An experiment conducted to evaluate SA of military
personnel during ﬁeld exercises has shown that SABARS
provides valid SA assessments, is unobtrusive, applicable
online and in real environments. To some extent, SABARS
even allows evaluating SA continuously and without delay.
Although SABARS is applied by human experts, we could
imagine that the concept of SABARS can be implemented
into a software using sensors for tracking actions. However,
the general problem of tracking motor actions in context
of a supervisory task (such as the operation of our highly
autonomous UAV swarm) is that observable actions are rare.
A. Eye Movement-Based Techniques
Instead of tracking motor actions recent experiments per-
formed in the aviation domain have shown that it is also
possible to use eye movements (recorded with an eye tracker)
as SA indications. The theoretic foundation of this approach is
the eye-mind hypothesis, which states that where humans look
at and what they think tends to be the same [15]. For example,
Moore [16] analysed the ﬁxation rates and durations of air
trafﬁc controllers and found that long and frequent ﬁxations on
important aircrafts reveal better SA. Further more, the analysis
of the spatial ﬁxation density using the Nearest Neighbour
Index (NNI) [17] has shown that air trafﬁc controllers using a
focussed scanning strategy (low NNI values) have better SA.
An experiment performed with aircraft pilots by Merve,
Dijk and Zon [18] supports Moore’s results. In their ex-
periment, pilots had to scan speciﬁc ﬂight displays to ﬁnd
the cause of a randomly inserted system malfunction. Pilots
performing a focussed scanning strategy with higher ﬁxation
204
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 3]**

durations on relevant displays found the causes of malfunc-
tions faster. Furthermore, they found that the deviation from a
regular scanning pattern can be used as a measure of loss of
SA.
B. Model-Based Techniques
According to the SEEV model, visual scanning is driven by
four parameters: (1) the saliency of objects on an HMI, (2)
the effort required to re-orient attention to another location, (3)
the expectancy of information at a given location and (4) the
value of information in context of the pertinent tasks [19]. Hart
et al. [20] integrated the SEEV model into the Man-Machine
Integration Design and Analysis System (MIDAS) in order to
predict subjective SA of virtual pilots and to assess virtual
pilot SA. SA has been quantiﬁed using values reaching from
0 (= poor SA) to 1 (= correct SA). The online application
of the system allowed calculating a continuous SA-trace in
order to detect SA-breakdowns and SA-gaps. However, as a
simulation environment MIDAS cannot be used to assess SA
of human pilots in real working environments.
In [21] a comprehension-based cognitive model of SA
has been proposed. The model puts focus on the cognitive
processes underlying the development of SA using empirically
conﬁrmed models and theories from cognitive psychology.
The basis of the proposed model is a queue of visual input
information, which activates knowledge stored in the memory
that is linked to the perceived information. In a series of
experiments conducted with drivers certain aspects of the
model have been evaluated. However, to our knowledge the
actual implementation of the model is pending.
In [22], an eye movement based theoretical model was
used to infer SA of real UAV operators with regard to se-
lected events occurring during mission execution. Pre-deﬁned,
situation-speciﬁc eye movement patterns were used as objec-
tive baseline in order to assess actually observed operator eye
movements. The technique is a ﬁrst step towards applying
eye movement analysis for assessing real operator SA during
mission execution. However, the technique does not calculate
a continuous SA-trace and is not granular enough to allow
detecting concrete SA-gaps.
III. SITUATION MODEL
In this section, we present a formal situation model. The
model is the core of SA-Tracer and based on three general
presumptions: a situation refers to (1) a situated operator, (2)
a concrete point in time, and (3) is determined by a set of
environment elements and a set of pertinent goals. Based on
these presumptions, we formally deﬁne the situation sit of an
operator op at a concrete point in time t as a tuple, which is
presented in (1):
sitop(t) =< E, G, s(E(t)), PG(t), RE(t) >
(1)
where E is a set of k environment elements e, which
determines the overall information space of the supervised
system:
E = e1, ..., ek
(2)
G is a set of l goals g, which determines the overall space
of operator goals:
G = g1, ..., gl
(3)
s(E(t)) is a concrete environment state comprised of a set
of k element-value pairs:
s(E(t)) = (e1, v1), ..., (ek, vk)
(4)
PG(t) is a set of m goals g, where PG(t) ⊆G and each
g ∈PG(t) is pertinent in context of s(E(t)):
PG(t) = g1, ..., gm
(5)
and RE(t) is a set of n environment elements, where
RE(t) ⊆E and each e ∈RE(t) is associated with at least
one g ∈PG(t):
RE(t) = e1, ..., en.
(6)
For different reasons, there can be deviations between the
objective state of an operator’s situation sitobj(t) and its
subjective state sitsub(t). While sitobj(t) represents what the
operator should be aware of, sitsub(t) represents what the
operator is actually aware of. Formally, we deﬁne sitobj(t)
as shown in (7):
sitobj(t) =< E, G, sobj(E(t)), PGobj(t), REobj(t) >
(7)
where sobj(E(t)) is the objective, actual system state,
PGobj(t) is the set of pertinent goals associated with
sobj(E(t)), and REobj(t) is the set of relevant environment el-
ements associated with PGobj(t). Further, we deﬁne sitsub(t)
as shown in (8):
sitsub(t) =< E, G, ssub(E(t)), PGsub(t), REsub(t) >
(8)
where ssub(E(t)) is the subjectively perceived system
state, PGsub(t) is the set of pertinent goals associated with
ssub(E(t)), and REsub(t) is the set of relevant environment
elements associated with PGsub(t). Reasons for deviations
between sitobj(t) and sitsub(t) are, e.g., cognitive limitations
(e.g., memory decay) or spatial constraints (e.g., environment
elements are not in the visual ﬁeld).
The situation model represents the environment elements
needed for the assessment of SAlevel1 and the goals needed
for the assessment of SAlevel2. In general, SA assessments are
performed by comparing the similarity between sitobj(t) and
sitsub(t). In the Venn diagram depicted in Fig. 3, sitobj(t) ∩
sitsub(t) is the set representing the common features, sitobj(t)
\sitsub(t) is the set representing the features unique to
sitobj(t), and sitsub(t) \sitobj(t) is the set representing the
features unique to sitsub(t).
205
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 3.
Assessment of operator SA
The
detailed
analysis
of
speciﬁc
deviations
between
sitobj(t) and sitsub(t) allows detecting individual SA-gaps.
An SA-gap with regard to SAlevel1 is the incorrect aware-
ness of an operator for a relevant environment element e ∈
REobj(t). An SA-gap with regard to SAlevel2 is the incorrect
awareness of an operator for a pertinent goal g ∈PGobj(t).
In order to detect SA-gaps with regard to SAlevel1 we de-
ﬁne for each e ∈E a threshold δe to perform a binary
classiﬁcation (’SA-gap’ or ’¬SA-gap’) of deviations between
ssub(REobj(t)) and sobj(REobj(t))). We determine SA-gaps
with regard to SAlevel2 by checking for each goal g the
condition: g ∈(PGobj(t) ∩PGsub(t)).
An example is shown in Fig. 4: if an unidentiﬁed
aircraft enters the mission area of the supervised UAV
swarm (e2=’aircraft.location’, v2=’near’), the goal of the
operator is from an objective point of view to identify
the aircraft (g2=’identify’), which is linked to an action
(a2=’communicate’). However, if the operator does not scan
the aircraft on the HMI, then he might neither be aware of
the relevant information (deviation between sobj(REobj(t))
and ssub(REobj(t))), nor the pertinent goal (deviation between
PGobj(t) and PGsub(t)). Consequently, the operator does not
perform the appropriate action.
In order to assess SAlevel1 more globally, we deﬁned
a function simlevel1 to quantify the similarity between
sobj(REobj(t)) and ssub(REobj(t)). The function is formally
deﬁned in (9):
simlevel1(sobj(REobj(t)), ssub(REobj(t))) →vlevel1
(9)
where vlevel1 ∈[0; 1]. Low values for vlevel1 reﬂect low
SAlevel1 and high values reﬂect high SAlevel1. In order to
assess SAlevel2 more globally we deﬁned a function simlevel2
to quantify the similarity between PGobj(t) and PGsub(t).
The function is formally deﬁned in (10):
simlevel2(PGobj(t), PGsub(t)) →vlevel2
(10)
where vlevel2 ∈[0; 1]. Low values for vlevel2 reﬂect low
SAlevel2 and high values reﬂect high SAlevel2. The consecu-
tive application of simlevel1 and simlevel2 allows tracing SA
over time and to detect critical SA-breakdowns.
IV. SA-TRACER
In this section, we present SA-Tracer. SA-Tracer analyses
system data recorded by the Ground Control Station (GCS) in
Fig. 4.
Deviations between sitobj(t) and sitsub(t)
context of operator goals to determine sitobj(t). Furthermore,
SA-Tracer analyses ﬁxations of operators (recorded by an eye
tracker) in context of focussed information objects (displayed
on the HMI) to infer sitsub(t). The overall system architecture
is depicted in Fig. 5.
The sets E and G are pre-deﬁned and used as the basis for
determining sitobj(t) as well as sitsub(t). The determination
of REobj(t) and PGobj(t) - given E, G and sobj(E(t)) -
is rather simple. However, inferring ssub(E(t)) based on the
analysis of eye movements is a complex process.
A. Inference of ssub(E(t))
The process for inferring ssub(E(t)) based on the analysis
of eye movements consists of three steps (see Fig. 6).
In Step 1, SA-Tracer identiﬁes ﬁxations of information
objects O, which are associated with the environment elements
E. Therefore, we deﬁned a set of areas of interest AOI
covering speciﬁc regions of the HMI. For each glance point
the information objects Oaoi ∈O covered by the regarded
area aoi ∈AOI are determined. Comparable to the I-AOI
algorithm [23], our algorithm for ﬁxation detection maps
sequences (≥100ms) of glance points falling on a certain
information object o ∈O to a ﬁxation φo, formally deﬁned in
(11):
φo = (tbegin, tnow)
(11)
where tbegin is the begin of the ﬁxation and tnow is the
current point in time.
In Step 2, SA-Tracer infers for each φo the perceptibility
of the associated information elements eo ∈E. According
to the SEEV model [19], visual scanning is driven by four
parameters: (1) the Saliency of objects on the HMI, (2) the
Effort required to re-orient attention to another location, (3)
the Expectancy of information at a given location and (4) the
Value of information in context of the pertinent goals. We use
a Bayesian Classiﬁer to infer for each individual environment
element eo associated with φo its current perceptibility πe as
a function of pertinent goals (= SEEV parameter ’Value of
information’). The classiﬁer is built based on a priori estima-
tions provided by experts. A threshold θπ is used to decide at
which perceptibility level ssub(E(t)) will be updated.
206
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 5]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 5.
Overall system architecture
In Step 3, SA-Tracer updates the values of selected environ-
ment elements in ssub(E(t)). Because ssub(E(t)) is part of the
memory of an operator, memory processes, such as forgetting
play an important role. In order to simulate forgetting, SA-
Tracer allocates a clock to each environment element which
starts decrementing immediately after an environment element
is updated. When the time of the clock allocated to a certain
environment element is expired, the value of the environment
element in ssub(E(t)) is deleted. The current decay time is 10
seconds. Using a clock as decay function is rough and will be
improved in later versions of the tool.
B. Determination of PGsub(t) and REsub(t)
SA-Tracer determines PGsub(t) based on a comparison
of ssub(E(t)) to G, as each g ∈G is associated with
speciﬁc environmental conditions. The status of a goal is set to
’pertinent’, when the awareness of the operator for the current
environment state matches these conditions. Furthermore, SA-
Tracer determines REsub(t) by checking the associations of
goals to environment elements.
V. EXPERIMENT
We performed an experiment with students acting as UAV
swarm operators. The experiments have been performed to
evaluate (1) the validity of SA assessments generated by SA-
Tracer and (2) the suitability of SA-Tracer for the future
deployment of ISAAIs.
A. Method
The experiments have been performed with participants act-
ing as UAV swarm operators within a simulation environment.
The objective of the mission was to supervise a UAV swarm
consisting of three UAVs extinguishing multiple ﬁre sources
in a certain landscape, which was inaccessible by human ﬁre
ﬁghters using ordinary equipment. In order to extinguish the
ﬁre sources each UAV had to load water at a water source
Fig. 6.
Process for inference of ssub(E(t))
and unload water at one of the ﬁre sources. During mission
execution each UAV had to frequently recharge energy at
a base. In summary, each UAV had to switch dynamically
between three goals:
1) Reﬁll Water
2) Extinguish Fire
3) Recharge Energy
Due to the high level of autonomy, the operator could not
control the goal selection of the UAVs. However, the operator
was instructed that maintenance of SA is crucial because UAVs
could have technical malfunctions while executing the ﬁre
ﬁghting mission. In the case of a malfunction the operator
had to resolve the malfunction remotely by pressing a speciﬁc
button on the HMI. In summary the goals of the operator were
deﬁned as follows:
1) Supervise UAV swarm
2) Resolve malfuction of UAV 1
3) Resolve malfuction of UAV 2
4) Resolve malfuction of UAV 3
While goal 1 was continuously activated, the goals 2-4 were
event-based.
1) Human Machine Interface: In order to supervise the
UAV swarm operators used a dedicated HMI. The HMI
consisted of three status displays - one per UAV - which were
arranged in a horizontal line. An example is depicted in Fig.
7. Each status display consisted of 6 information objects:
• Status indicator for goal ’Recharge Energy’ (o1)
• Status indicator for goal ’Reﬁll Water’ (o2)
• Status indicator for goal ’Extinguish Fire’ (o3)
207
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 7.
Status display of a single UAV
• Status indicator for UAV malfunction (o4)
• Status bar for energy level (o5)
• Status bar for water level (o6)
For each UAV 6 environment elements were deﬁned:
• Status (true or false) of goal ’Recharge Energy’ (e1)
• Status (true or false) of goal ’Reﬁll Water’ (e2)
• Status (true or false) of goal ’Extinguish Fire’ (e3)
• Status (true or false) of UAV malfunction (e4)
• Status ([0,100]%) of energy level (e5)
• Status ([0,100]%) of water level (e6)
Each information object was associated with an environment
element:
• o1 →e1
• o2 →e2
• o3 →e3
• o4 →e4
• o5 →e5
• o6 →e6
The status of each goal was indicated by a lamp (green
= ’true’, black = ’false’). The status of a malfunction was
also indicated by a lamp (red = ’true’, black = ’false’). Each
lamp was labelled with a letter indicating its function (’E’ =
Recharge Energy, ’F’ = Extinguish Fire, ’W’ = Reﬁll Water,
’M’ = Malfunction Status). The status indicators were arranged
in a cyclic frame surrounding two status bars, which indicated
the current level of energy (yellow) and water (blue).
2) Equipment: We used the Dikablis head mounted eye
tracker to track the eye movements of operators. The eye
tracker allows analysing glance points in context of pre-deﬁned
AOIs at runtime. The HMI was presented using an LED
projector with a full HD resolution. The HMI was scaled to
a diagonal screen size of 2 meters. Participants used a mouse
device to interact with the HMI.
3) Participants: 10 students (6 female) enrolled at the
University of Oldenburg took part in the experiment for a
monetary compensation. They were aged 20 to 31 years
(mean=25.2, SD=3.52).
4) Scenarios: The experiment consisted of 9 scenarios,
each lasting 2 minutes. The scenarios 1 to 3 did not contain
UAV malfunctions. In the scenarios 4 to 9, 1 to 3 UAV
Fig. 8.
Deﬁnition of AOIs for a UAV status display
malfunctions were triggered. There was never more than
one malfunction triggered at the same time. Each participant
participated to each scenario resulting in 90 (10 participants *
9 scenarios) datasets.
5) Procedure: The participants were seated 2.5 meters in
front of the HMI. The distance ensured that participants could
supervise all three UAV status displays without head move-
ments. Then, participants were introduced to the objective of
the mission, their role as UAV swarm operator and the HMI.
After the introduction, the participants were calibrated for the
eye tracker and performed a short training session to get a
feeling for wearing the eye tracking device, their tasks and the
HMI. After training was completed, the ﬁrst scenario started.
During each scenario, an instructor continuously supervised
the eye tracking calibration to ensure correct eye movement
records. After each scenario the HMI was blinded for 2
seconds followed by a scenario debrieﬁng. The debrieﬁngs
were performed to capture the participants’ subjective picture
of the environment. Therefore, the HMI was shown again but
without any state indications. The participants had to mentally
recall and restore the last state of each UAV by clicking with
the mouse device on the UAV state indications of the HMI.
After each debrieﬁng a short break was made and then the
next scenario was started.
B. Results
For each UAV status display a general AOI covering o1 to o6
and 6 sub-AOIs, each covering exactly one information object,
were deﬁned (see Fig. 8). Because the display items were very
close to each other, sub-AOIs overlapped at marginal areas.
Consequently, it was possible that more than one sub-AOI
was focussed at the same time. The deﬁnition of general AOIs
allowed us to allocate eye movements to UAV status displays
even though no ﬁxation of sub-AOIs was detected.
1) Data Quality: The eye tracker’s calibration was per-
formed very carefully, resulting in high quality data with
an average of 94% hitting AOIs. However, the data of one
208
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 9.
Percentage Dwell Time of participants on the HMI
Fig. 10.
Fixation lengths of participants on the HMI
participant had to be excluded for the analysis as technical
problems with the eye tracker occurred during the experiment.
2) Data Analysis: The average percentage dwell time per
AOI for all participants during the experiment is shown in
Fig. 9. Because sub-AOIs could overlap at marginal areas, the
percentage dwell time on the sub-AOIs sums up to 122%. This
shows that more than one sub-AOI was hit multiple times. The
focus of overall dwells of the participants was on the central
status display (UAV 2) with an almost equal distribution for
status displays to the left (UAV 1) and to the right (UAV 3). In
average, each AOI was visited by at least 2% of the time. In
Fig. 10, the distribution of ﬁxation lengths for 5 different time
periods is presented. The performance of the UAV supervision
task was characterized by short ﬁxations between 100ms and
300ms.
3) Validation: We validated SA-Tracer with regard to its
capability to infer the operator’s subjective picture of the
environment state ssub(E(t)), to detect actual SA-gaps and
to assess SA globally using the functions simlevel1 and
simlevel2. The baseline used for the validation was given by
the debrieﬁng data. Each dataset of the debrieﬁng data was
a deﬁned environment state referring to the last system state
of the simulation (=ssubdebriefing(E(tend))). We deﬁned for
each of the 18 environment elements a threshold δe for the
binary classiﬁcation of SA-gaps (cf. Section III). Because the
status of e1 to e4 was either true or false each deviation
TABLE I
CONFUSION MATRIX
SA-Tracer (θπ=.3)
SA-Gap
¬SA-Gap
Total
Debrieﬁng
SA-Gap
927 (85.6%)
156 (14.4%)
1083
¬SA-Gap
141 (37.6%)
234 (62.4%)
375
Total
1068
390
1458
Fig. 11.
Level 1 values of a participant calculated based on debrieﬁng data
and the predicted mental representation
between the objective and subjective state was classiﬁed as
an SA-gap. For e5 and e6 a deviation of 10% was accepted.
Then, we applied δe to the debrieﬁng data, resulting in a
1458 (9 participants * 9 scenarios * 18 environment ele-
ments) classiﬁcations. The same procedure was applied to the
environment state (=ssubSA−T racer(E(tend))) inferred by SA-
Tracer. We assumed that SA-Tracer would correctly classify
SA-gaps. We systematically tested the performance of SA-
Tracer for different instantiations of θπ (cf. Section IV-A).
The best performance was found for θπ=.3. The confusion
matrix showing the accuracy of detected SA-gaps is depicted
in Table. I. SA-Tracer correctly classiﬁes approx. 86% of
actual SA-gaps and 62.4% of the actual ¬SA-gaps. In order to
quantify the predictive power of SA-Tracer, we used Mathew’s
Correlation Coefﬁcient (MCC), which is a measure of the
quality of binary classiﬁcations. The result (MCC = .43)
shows that SA-Tracer correlates with the actual data rather
well.
We applyed simlevel1 to globally assess SAlevel1 with
regard to the debrieﬁng data and to SA-Tracer data. The
result were two samples of 81 (9 participants * 9 scenar-
ios) quantitative values (vlevel1debriefing and vlevel1SA−T racer).
Both samples are depicted in Fig. 11. Pearson’s Correlation
Coefﬁcient shows that SA-Tracer assessments ﬁt rather well
with the debrieﬁng data (r=.55).
As described in Section IV-B, SA-Tracer assesses SAlevel2
by checking the conditions that have to be fulﬁlled for being
aware of pertinent goals against ssub(E(t)). In our experiment,
being aware of the goal ’Resolve malfunction of UAV 1’,
209
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 8]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 12.
SA Traces for level 1 and level 2 of one of the participants during
a scenario with 3 malfunction events
’Resolve malfunction of UAV 2’ or ’Resolve malfunction of
UAV 3’ requires a ﬁxation of the malfunction indicator of UAV
1, UAV 2 or UAV 3 while a malfunction is present. When
the malfunction indicator was ﬁxated, the status of the goal
changed to ’pertinent’. When the malfunction was correctly
resolved, the red light indicating the malfunction turned off.
When, the operator noticed this change, the status of the goal
was changed again to ’not pertinent’. All participants correctly
resolved the malfunctions immediately after a ﬁxation on the
relevant malfunction indicator was detected. The time needed
by the operators for detecting malfunctions varied between
0.4 and 10.2 seconds (mean=2.42, SD=1.72). Exemplarily,
Fig. 12 shows the SA traces (SAlevel1, SAlevel2) referring
to participant 5. Overall, there were neither malfunctions that
were resolved without a ﬁxation on a malfunction indicator,
nor malfunctions that have not been resolved although there
was a ﬁxation. Thus, we assume that SA-Tracer correctly
assessed SAlevel2. However, further analyses are necessary.
VI. CONCLUSIONS
In this paper, we presented SA-Tracer - a tool for assessment
of operator SA during mission execution. We performed an
experiment with 10 UAV operators in order to validate the
performance of our tool. The assessments for level 1 were
validated using correlation analyses. As SA-Tracer is a ﬁrst
prototype the results (MCC = .43, r=.55) are rather promis-
ing.
SA-Tracer works automatically. Using an eye tracker for
assessing SA is an unobtrusive alternative to direct techniques
[22]. SA-Tracer calculates continuous traces of operator SA
online and without delay. Although we applied SA-Tracer in
an experimental simulation environment, we believe that its
application in a real working environment would be possible.
Thus, we believe that SA-Tracer will be a suitable tool for the
deployment of future ISAAIs.
The results presented in this paper were obtained using a
simple HMI without moving UAV objects on a mission map.
We plan to perform further experiments with a more realistic
HMI for UAV swarm operations including a mission map and
moving UAV objects.
SA-Tracer could be improved in different ways. We men-
tioned that memory processes play an important role for the
inference of ssub(E(t)). Currently, SA-Tracer uses a simple
mechanism to simulate forgetting. This mechanism consist of
a clock which deletes values in ssub(E(t)) if the life cycle
of values is expired. A better solution could be integrating
a memory model inspired by cognitive architectures such
as ACT-R [24], which has shown to be v valid model of
some aspects of human cognitive processes. The Bayesian
classiﬁer used to calculate the perceptibility of environment
elements is rather simple. We plan extending the classiﬁer
by integrating the SEEV parameter ’Saliency of information
objects’. Further, the intergation of Tversky’s feature contrast
model [25] could be an option to improve the global assess-
ment of SA. Currently, SA-Tracer sets the status of goals to
’pertinent’, whenever the conditions for being aware of these
goals are fulﬁlled. This approach might be called naive as the
correct perception of environment elements must not mean
that operators actually activate the correct goals. A solution
could be collecting further indications after the conditions
are fulﬁlled in order to assess whether the operator actually
activated the correct goals.
ACKNOWLEDGMENT
This research is conducted within the European project
D3CoS and funded by ARTEMIS-JU and national authorities
under grant agreement no. 269336
REFERENCES
[1] R. R. Murphy and J. L. Burke, “The safe human-robot ratio,” in
Human-Robot Interactions in Future Military Operations, M. Barnes and
F. Jentsch, Eds.
Brookﬁeld, VT, USA: Ashgate Publishing Company,
2010, pp. 31 – 52.
[2] H. H. Brian, B. Mclaughlan, and M. Baker, “Swarm control in unmanned
aerial vehicles,” in Proceedings of International Conference on Artiﬁcial
Intelligence (IC-AI), CSREA.
Press, 2005.
[3] M. R. Endsley, B. Bolte, and D. G. Jones, Designing for Situation
Awareness: An Approach to User-Centered Design. Taylor and Francis,
2003.
[4] J. Crandall, M. Goodrich, J. Olsen, D.R., and C. Nielsen, “Validat-
ing human-robot interaction schemes in multitasking environments,”
Systems, Man and Cybernetics, Part A: Systems and Humans, IEEE
Transactions on, vol. 35, no. 4, pp. 438 – 449, july 2005.
[5] M. R. Endsley, “Toward a theory of situation awareness,” Human
Factors, vol. 37, no. 1, pp. 32–64, 1995.
[6] D. G. Jones and M. R. Endsley, “Sources of situation awareness errors
in aviation.” Aviation space and environmental medicine, vol. 67, no. 6,
pp. 507–512, 1996.
[7] M. Mouloua, Gilson, J. R., Kring, and P. Hancock, “Workload, situation
awareness, and teaming issues for UAV/UCAV operations,” in Proceed-
ings of the Human Factors and Ergonomics Society, vol. 45, 2001, pp.
162–165.
[8] M. L. Cummings and P. J. Mitchell, “Predicting controller capacity in
supervisory control of multiple uavs,” Trans. Sys. Man Cyber. Part A,
vol. 38, no. 2, pp. 451–460, Mar. 2008.
[9] M. Hou, R. Kobierski, and M. Brown, “Intelligent adaptive interfaces for
the control of multiple uavs,” Engineering, vol. 1, no. 3, pp. 327–362,
2007.
[10] R. Taylor, H. Howells, and D. Watson, “The cognitive cockpit: Op-
erational requirements and technical challenge,” in Contemporary Er-
gonomics 2000, P. McCabe, S. Robertson, and M. Hansen, Eds.
CRC
Press Inc, 2000, pp. 57–66.
210
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:03 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 9]**

[11] R. Onken, “The cognitive cockpit assistant systems cassy/cama,” SAE
International, 1999.
[12] B. McGuinness, “Quantitative analysis of situational awareness (quasa):
Applying signal detection theory to true/false probes and self-ratings,”
Command and Control Research and Technology Symposium, 2004.
[13] M. R. Endsley, Situation awareness global assessment technique
(SAGAT).
IEEE, 1988, vol. 3, pp. 789–795.
[14] L. Strater, Measures of platoon leader situation awareness in virtual
decision-making exercises, ser. Research report.
U.S. Army Research
Institute for the Behavioral and Social Sciences, 2001.
[15] M. A. Just and P. A. Carpenter, “A theory of reading: from eye ﬁxations
to comprehension.” Psychological Review, vol. 87, no. 4, pp. 329–354,
1980.
[16] K. S. Moore, “Comparison of eye movement data to direct measures of
situation awareness for development of a novel measurement technique
in dynamic, uncontrolled test environments,” Ph.D. dissertation, 2009.
[17] M. Camilli, R. Nacchia, M. Terenzi, and F. Di Nocera, “Astef: a simple
tool for examining ﬁxations,” Behavior Research Methods, vol. 40, no. 2,
pp. 373–382, 2008.
[18] K. van de Merwe, H. van Dijk, and R. Zon, “Eye movements as an
indicator of situation awareness in a ﬂight simulator experiment,” The
International Journal of Aviation Psychology, vol. 22, no. 1, pp. 78–95,
2012.
[19] B. Gore, B. Hooey, C. Wickens, and S. Scott-Nash, “A computational
implementation of a human attention guiding mechanism in midas v5,”
in Digital Human Modeling, ser. Lecture Notes in Computer Science,
V. Duffy, Ed. Springer Berlin Heidelberg, 2009, vol. 5620, pp. 237–246.
[20] S. Hart, D. Dahn, A. Atencio, and M. Dalal, “Evaluation and application
of midas v2.0,” in Proceedings of the Society of Automotive Engineers
(SAE) World Aviation Congress, 2001.
[21] M. Baumann and J. Krems, “A comprehension based cognitive model
of situation awareness,” in Digital Human Modeling, ser. Lecture Notes
in Computer Science, V. Duffy, Ed.
Springer Berlin Heidelberg, 2009,
vol. 5620, pp. 192–201.
[22] R. M. Ratwani, J. M. McCurry, and J. G. Trafton, “Single operator,
multiple robots: an eye movement based theoretic model of operator
situation awareness,” in Proceedings of the 5th ACM/IEEE international
conference on Human-robot interaction, ser. HRI ’10.
Piscataway, NJ,
USA: IEEE Press, 2010, pp. 235–242.
[23] D. D. Salvucci and J. H. Goldberg, “Identifying ﬁxations and saccades in
eye-tracking protocols,” Proceedings of the symposium on Eye tracking
research applications ETRA 00, vol. 469, no. 1, pp. 71–78, 2000.
[24] J. R. Anderson, L. M. Reder, and C. Lebiere, “Working memory:
activation limitations on retrieval.” Cognitive Psychology, vol. 30, no. 3,
pp. 221–256, 1996.
[25] A. Tversky, “Features of similarity,” Psychological Review, vol. 84,
no. 4, pp. 327–352, July 1977.
211
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:03 UTC from IEEE Xplore.  Restrictions apply. 
