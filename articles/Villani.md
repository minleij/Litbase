# Villani

*Source file: Villani.pdf — 16 pages*


---
**[Page 1]**

Autonomous Robots (2020) 44:601–616
https://doi.org/10.1007/s10514-019-09889-6
Humans interacting with multi-robot systems: a natural affect-based
approach
Valeria Villani1
· Beatrice Capelli1 · Cristian Secchi1 · Cesare Fantuzzi1 · Lorenzo Sabattini1
Received: 18 May 2018 / Accepted: 24 September 2019 / Published online: 22 October 2019
© Springer Science+Business Media, LLC, part of Springer Nature 2019
Abstract
This paper proposes a novel human–multi-robot-system interaction approach that enjoys two main features: natural interaction
and affect-based adaptation of robots behavior. Speciﬁcally, the proposed system enables interaction by means of a wrist-worn
device, such as a commercial smartwatch, which allows to track user’s movements and heart activity. Thus, on the one side,
the proposed system allows the user to intuitively drive the robots by establishing a natural mapping between wrist movements
and robots velocity. On the other side, the system estimates user’s mental fatigue during interaction by means of the analysis of
heart rate variability. The proposed interaction system adapts then the behavior of the multi-robot system when the interacting
user gets overwhelmed with the interaction and control task, which is then simpliﬁed. Experimental validation is provided,
to show the effectiveness of the proposed system. First, the natural and affect-based interaction are considered separately.
Then, the approach is tested considering a complex realistic scenario, which is simulated in virtual reality in order to get
an immersive and realistic interaction experience. The results of the experimental validation clearly show that the proposed
affect-based adaptive system leads to relieving the user’s fatigue and mental workload.
Keywords Human–multi-robot-system interaction · Natural ineraction · Affective robotics · Human–centred robotics
1 Introduction
This paper studies the problem of letting a human operator
interact with a multi-robot system in an intuitive and adaptive
manner that takes into account the cognitive effort of the user.
In this paper we achieve this by simplifying the interaction
task when it gets too complex and the user’s cognitive load
becomes unsustainable.
Recent technological developments in embedded com-
puting, sensing, communication systems and network tech-
nologies are leading to constantly increasing interest for
multi-robot systems. In fact, several complex problems can
be solved exploiting the capabilities of a team of robots,
This is one of the several papers published in Autonomous Robots
comprising the Special Issue on Multi-Robot and Multi-Agent Systems.
Electronic supplementary material
The online version of this article
(https://doi.org/10.1007/s10514-019-09889-6) contains
supplementary material, which is available to authorized users.
B Valeria Villani
valeria.villani@unimore.it
1
Department of Sciences and Methods for Engineering
(DISMI), University of Modena and Reggio Emilia, via G.
Amendola, 2, Reggio Emilia, Italy
achieving large computation, communication and sensing
capabilities exploiting limited-size devices. The majority of
current multi-robot systems applications can be found in
industrial domains, where they are mainly used for logistics
and automated goods transportation (Sabattini et al. 2018;
Andreasson et al. 2015; Fanti et al. 2015; Draganjac et al.
2016; Wurman et al. 2008), or in the agricultural domain,
where they are used for soil preparation, pesticide applica-
tion and harvesting (English et al. 2013; Ball et al. 2015).
However, considering the increasing popularity of small-size
mobile robotic platforms (ground, aerial, underwater, etc.),
multi-robot systems will likely become popular in domestic
applications in the near future.
Most of the research in the ﬁeld of multi-robot sys-
tems until now has been devoted, to the greatest extent, to
the design of proper control approaches to let the robots
achieve some common goals (Sabattini et al. 2015; Ren and
Beard 2005, 2008; Antonelli et al. 2014). However, those
approaches typically consider fully autonomous multi-robot
systems that are able to achieve basic and simple cooperative
behaviors,suchasaggregation,synchronization,coverage,or
formation control. Thus, in general, the presence of a human
operator is marginal in classical approaches.
123

---
**[Page 2]**

602
Autonomous Robots (2020) 44:601–616
The main motivation of this paper is to change this
approach, explicitly considering the possibility, for human
operators, to interact with multi-robot systems. The objec-
tive is that of dramatically increasing the capabilities of the
whole system. In fact, having a human interacting with a
multi-robot system allows to take full advantage of the oper-
ator’s ﬂexibility and skills, including high-level reasoning,
ability to deal with unexpected situations and solve them,
and ability to adapt to new goals (Kolling et al. 2016). Rel-
evant application scenarios include, for instance, search and
rescue operations in harsh and dynamic environments (which
are typically unstructured and unpredictable), or goods trans-
portation in production plants (where the presence of human
operators makes the system highly dynamic and difﬁcult to
predict). However, few works in the recent literature have
been proposed that consider the possibility of having a human
operator interacting with a multi-robot system.
As a drawback, it is worthwhile noting that the interaction
with such complex systems made by multiple robots is likely
to be quite demanding for the human operator, in terms of
cognitive burden. A great effort is required to achieve and
maintain proper situation awareness, while supervising the
system, providing the correct input to the correct robot(s) and
interpreting the feedback from the ﬁeld. Additionally, this
complexity increases with the number of robots and becomes
critical in remote interaction (Kolling et al. 2016). Thus, if
the interaction of a user with a multi-robot system is to be
designed, it is fundamental to focus not only on the effec-
tiveness of the interaction, but also, and most importantly,
on the ease of use for the operator and sustainability of the
interaction task, in terms of cognitive demand.
Hence, in this paper we propose a novel interaction
approach for multi-robot systems that lets the human intu-
itively interact with the robots, mimicking real-world behav-
ior. To this end, it exploits movements of user’s forearm and
gestures and establishes a mapping of forearm movements
into robots velocity commands. Mapping is chosen in a way
such that, to task the robots, the user has to perform actions
that correspond to daily practices in the physical world (e.g.,
rotate the wrist to turn the robots), as detailed in Sect. 5.1.
This allows interaction to be natural and intuitive. In addition,
the system takes into account the mental effort of the user and
changes its behavior accordingly, simplifying the interaction
task when it overloads user’s capabilities. This is achieved
resorting to affective robotics by monitoring user’s heart rate
variability (HRV). To the best of the authors’ knowledge, this
represents the ﬁrst example of a natural interaction system
that modulates the interaction with a team of robots taking
into account the operator’s mental strain. Preliminary results
on this topic were presented in Villani et al. (2017c).
In this paper we further extend this approach. In partic-
ular, we propose an algorithm for mental fatigue detection
based on HRV analysis and validate it for the use with a
portable everyday heart rate monitoring device. Moreover,
we extend the experimental validation of the proposed affect-
based human–multi-robot-system interaction approach, by
considering a complex application scenario in which a large
number of robots monitor a wide area and the human operator
has to supervise the whole team and is called for action upon
robots’ notiﬁcation (or request). In this context, we show that
the proposed affect-based interaction system has a positive
impact for the user. In fact, it leads to reducing mental work-
load and fatigue, even though it might lead to decrease of
performance, since adaptation might require reduction of the
functionalities or additional constraints.
The paper is organized as follows. In Sect. 2 we present
an overview on existing approaches to human–multi-robot-
systems interaction. Moreover, we provide the background
for detecting mental fatigue from HRV analysis. Then, in
Sect. 3 we introduce the proposed system and in Sect. 4
presentthealgorihtmformentalfatiguedetection.Thedetails
of how the proposed system is intended to control a multi-
robot system are provided in Sect. 5, both in terms of motion
control and adaptation to user’s mental stress. The validation
of the proposed natural and affective interaction with a team
of robots is presented in Sect. 6. Finally, Sect. 7 follows with
some concluding remarks.
2 Related work
2.1 Interaction with multi-robot systems
While a large body of literature on human–robot interac-
tion can be found in the literature, the case of interaction
with a multi-robot system is a relatively new problem, which
has been considered only in recent years. The recent survey
paper (Kolling et al. 2016) presents a complete overview of
themaininteractionapproachesandopenissues,highlighting
the speciﬁc characteristics that distinguish interaction with
multi-robot systems from general human–robot interaction.
In particular, multi-robot systems are very demanding for
human operators, in terms of mental workload, due to the
high dimensionality of their state space. This has been ana-
lyzed in Hocraffer and Nam (2017), where authors consider
the interaction of a human operator with a group of aerial
robots. The analysis is performed considering human factors
as the central element, and highlights the fact that the cog-
nitive burden caused by this kind of interaction is very large
and, to achieve an effective system, it is necessary to pro-
vide the robots with a certain degree of autonomy. In fact,
as stated in Podevijn et al. (2016), the psychophysiologi-
cal state of humans interacting with multi-robot systems is
directly correlated with the number of robots involved in the
interaction, with large groups associated to signiﬁcant levels
123

---
**[Page 3]**

Autonomous Robots (2020) 44:601–616
603
of stress. A possible solution foreseen by the authors is to
provide robots with some levels of autonomy.
Abstractionsneedtobedeﬁned,asstatedinDiaz-Mercado
et al. (2017), that scale gracefully with the number of robots,
and that make the overall multi-robot system understand-
able by the human operator. As stated in Dietz et al. (2017),
carefully deﬁning the autonomy and the motion patterns of
the robots is of help also for simplifying situation aware-
ness for human operators, with synchronized motion patterns
that are highlighted as easier to understand. It is worth not-
ing that situation awareness is of paramount importance,
when considering interaction with robotic systems: as shown
in Kapellmann-Zafra et al. (2016), interaction loses effective-
ness, when situation awareness is not complete, and partial
autonomy of the robots becomes necessary.
Situation awareness is particularly difﬁcult when consid-
ering remote interaction, that is when the human operator
does not share the robots environment. This is frequently
the case when considering teleoperation strategies, which
are a commonly considered human–multi-robot interaction
approach. For instance, (Franchi et al. 2012) proposed a
method that considers the human teleoperating the multi-
robot system as a whole: robots are provided with a certain
level of autonomy that allows them to avoid collisions
and loss of connectivity. Situation awareness is provided
to the operator in terms of an appropriately designed and
modulated force feedback, and a general-purpose haptic tele-
operation device is exploited. Conversely, (Diana et al. 2013)
exploits the concept of “deformable affordance”, introduc-
ing an ad-hoc deformable teleoperation device that is used
by the human operator to globally deﬁne the shape of the
multi-robot system: the stability of the interaction system is
discussed in de la Croix and Egerstedt (2015). This approach
moves towards the introduction of interaction paradigms
that are natural for the humans, and that can then be eas-
ily exploited. Along these lines, a strategy was introduced
in Gioioso et al. (2014), where authors consider a ﬂeet of
aerial robots whose objective is to interact with some envi-
ronmental objects: the teleoperation scheme is designed in
such a way that the human can control the aerial robots as
if they were her/his ﬁngers. A different approach is pro-
posed in Secchi et al. (2015), where the conductor-orchestra
paradigm is exploited to let the robots execute a set of pre-
deﬁned behaviors: the human operator acts as a conductor,
with speciﬁc gestures used for selecting the desired behavior.
This is achieved in a partially decentralized manner: as in Lin
and Liu (2017), only a portion of the robots can receive com-
mands from the human operator, while the remaining ones
are indirectly controlled through appropriately deﬁned inter-
robot coupling relationships.
A few works have recently appeared that, instead of con-
sidering remote interaction, provide solutions for proximal
interaction, in which the operator can observe the robots
directly and interact in a shared environment: this allows to
achieve high levels of situation awareness. In this scenario,
commonly used interaction strategies generally include ges-
tures, face and speech recognition (Gromov et al. 2016; Nagi
et al. 2014; Cacace et al. 2016a; Pourmehr et al. 2013).
Strategies that require face engagements, such as Nagi
et al. (2014) and Pourmehr et al. (2013), have the advantage
of not requiring the use of special devices or instruments,
since the user’s face is generally acquired by means of cam-
eras installed on the robots. However, these methods require
line of sight, which imposes a constraint on the physical area
where interaction can occur, and on the freedom of motion
of the user. This constraint can be relaxed considering alter-
native solutions, such as gesture recognition, as discussed
in Gromov et al. (2016) and Cacace et al. (2016a), or elec-
troencephalography, as discussed in Mondada et al. (2016).
InCacaceetal.(2016b)gesturesareusedincombinationwith
voice commands to orchestrate the team operations; therein
an handheld device is also used to receive back relevant infor-
mation from the robotic team. While these methods do not
require line of sight, they impose the use of several sensors to
be worn by the user, which are exploited to acquire and fuse
different physiological and dynamical data. The necessity to
wear such devices results generally cumbersome for the user
and, ultimately, impractical.
2.2 Detection of mental fatigue for affective
robotics
Affective robotics consists in combining robotics and affec-
tive computing to enhance the interaction of a human with
a robot by monitoring her/his affect and emotions. Indeed,
monitoring and interpreting nonverbal communication can
provideimportantinsightsaboutahumaninteractingwiththe
robot, thus making it possible to achieve implicit feedback
about the interaction (Braezal et al. 2016). To this end, eye
gaze (Rich et al. 2010), facial expression (Gunes et al. 2011),
voice, linguistic and paralinguistic (e.g., utterances) features
(Wilson and Lewandowska-Tomaszczyk 2014; Gunes et al.
2011), and physiological signals (Kulic and Croft 2007;
Bonarini et al. 2008) have been investigated as indices of
subject’s affective state, focus, attention and intent. Among
physiological signals, most of the studies have employed
brain, cardiac (heart rate), respiratory, galvanic skin response
and eye (pupil dilatation) data. Examples in this regard are
Ryu and Myung (2005), Brookhuis and de Waard (2010),
Wilson and Russell (2003), Rani et al. (2004) and Kulic and
Croft (2007). However, recording these signals requires that
obtrusive instrumentation is used, which makes it impracti-
cal in real operational environments. In such conditions the
goal is that of monitoring operator’s mental fatigue in real
working scenarios, that is in a manner that is non-invasive
and transparent to the user. To this end, the use of heart rate
123

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

604
Autonomous Robots (2020) 44:601–616
proves convenient since, in addition to electrocardiogram,
it can be recorded by commercial portable and non-invasive
wrist-worndevices,suchassmartwatchesandactivitytracker
wristbands. In this regard, it is worthwhile noting that it has
been shown that commercial wrist-worn devices provide an
accurateestimateofheartrate(Shcherbinaetal.2017;Wallen
et al. 2016). In both studies, photoplethysmography-derived
heart rate recorded by the non-invasive wrist-worn devices is
compared to the electrocardiogram, which is the gold stan-
dard for recording heart activity.
HRV is the variation over time of the interval between
consecutive heart beats. It is an established quantitative index
for the non-invasive assessment of autonomic nervous sys-
tem function. As a consequence, it is widely used to detect
a great variety of pathological and physiological conditions
(Acharya et al. 2006). Moreover, there is large part of lit-
erature showing that stress, in general terms, and cognitive
processing in particular, inﬂuence HRV (Bernardi et al. 2000;
Luque-Casado et al. 2013; Acharya et al. 2006; Castaldo
et al. 2015, 2016; Kulic and Croft 2007; Hoover et al. 2012;
Melillo et al. 2011; Gohara et al. 1996; Rani et al. 2002;
Thayer et al. 2012).
The analysis of HRV relies on the analysis of RR interval
time series, which is the series of occurrence times of heart
beats. It is typically denoted as RRk = Rk+1 −Rk, k =
1, 2, . . . , where Rk is the instant of occurrence of the k−th
heart beat. To quantify HRV, several metrics can be used,
mainly in the time and frequency domain (Task Force of
The European Society of Cardiology & The North American
Society of Pacing and Electrophysiology 1996). In particu-
lar, the most common statistical time domain metrics are: the
mean value and the standard deviation, denoted by RR and
SDRR in the following, of the RR series, the root mean square
of successive differences (RMSSD), and the percentage num-
ber of consecutive (normal) intervals differing by more than
50ms in the entire recording (pNN50). As regards the fre-
quency domain metrics, the most used ones are the power in
the low frequency band (LF, 0.04 −0.15 Hz), the power in
the high frequency band (HF, 0.15−0.40 Hz) and their ratio
(LF/HF ratio). More details can be found, for example, in
Task Force of The European Society of Cardiology & The
North American Society of Pacing and Electrophysiology
(1996) and Clifford et al. (2006). Furthermore, clinical stan-
dards require that metrics are calculated either on a short time
scale (namely short-term HRV) of about 5 min duration, or
over extremely long periods of time (namely long-term HRV)
usually lasting 24h (Task Force of The European Society of
Cardiology & The North American Society of Pacing and
Electrophysiology 1996).
The effect of stress on HRV is due to the fact that mental
stress is one of the factors contributing to sympathetic stim-
ulation, which is associated with the low frequency range of
heart rate. Thus, it has been found that LF is reduced under
mental fatigue, while HF is increased (Bernardi et al. 2000;
Acharya et al. 2006; Gohara et al. 1996; Rani et al. 2002).
As regards time domain metrics, the main reported changes
regard RR, SDNN and RMSSD, which are decreased under
mental stress (Castaldo et al. 2015).
In this paper we rely on the computation of RR as a
measure of HRV related to cognitive effort. In Sect. 4 the
algorithm for mental fatigue detection is presented and the
effectiveness of the use of the smartwatch in this regard is
assessed.
3 Proposed system
In this section we describe the proposed system for control-
ling and interacting with a ﬂeet of mobile robots in a natural
and adaptive manner. The resulting interaction approach
resembles user-centered design methodology since it enjoys
two main features. First, it establishes a natural interface
between the user and the multi-robot system, thus alleviating
the communication gap between the user and the robots, as
discussed in Villani et al. (2017b). Second, by implement-
ing affective robotics, the behavior of the team of robots is
adapted to the user by taking into account her/his mental
workload and simplifying interaction when it is exceeding
user’s capabilities.
To implement these features, we consider the use of a
multi-purposewearabledevice,(suchasasmartwatch)which
embeds the required sensors for tracking wristarm move-
ments and mental strain. Being worn on the user’s wrist, it
is not perceived as an encumbrance and does not limit the
user’s freedom of movement.
Figure 1 shows an overview of the proposed system.
Speciﬁcally, the wearable device is used to gather infor-
mation from the user in terms of motion of forearm and
mental workload. The former is measured as angular veloc-
Fig. 1 Architecture of the proposed system. A smartwatch is used to
implement a natural interface based on user’s forearm motion for affect-
based interaction with a multi-robot system
123

---
**[Page 5]**

Autonomous Robots (2020) 44:601–616
605
ity and linear acceleration, while the latter is measured from
the embedded heart rate sensor. The inertial data are then
translated into commands for the robots, whose behavior is
changedalsodependingonthedetectedcognitivestress.Ulti-
mately, the user can teleoperate the robots by simply moving
the forearm. Feedback information about the current position
and actual velocity of the robots can be exploited to imple-
ment autonomous behaviors, such as master-slave motion. A
feedback can be provided to the user in terms of vibration of
the wearable device and/or sound notiﬁcation (if available,
as in the case of a smartwatch), aiming at informing the user
whether one, several or many robots are teleoperated at that
moment, or mental stress has been detected.
Another interesting feature of the proposed interaction
framework is that it is quite general. Indeed, on the one
side, any commercial multi-purpose device equipped with
accelerometers, gyroscopes and heart rate sensors, such as
common wristbands for activity tracking, can be used to
replace the smartwatch, as discussed in Villani et al. (2017b).
On the other side, the approach holds valid for any interac-
tion system, provided that a suited mapping between user’s
forearm motion and interaction commands is found. Speciﬁ-
cally, it has been proposed for single aerial and ground robots
(Villani et al. 2017a,b, 2018c) and could be exploited for
interacting with industrial automatic machines, as in Villani
et al. (2016), in an enhanced scenario of affective computing
for inclusive work environment (Villani et al. 2018b).
4 Algorithm for non-invasive detection of
mental fatigue based on HRV
In this section we introduce a method for real-time detection
of mental fatigue by means of a smartwatch (or a similar
wrist-worn device).
4.1 Smartwatch-based detection of mental fatigue
To assess the suitability of heart rate recorded by means of
the smartwatch to detect mental fatigue, we performed some
tests in which subjects were exposed to sustained mental
workload and their heart rate was recorded. To this end, 21
subjects(15males,6females,age28.4±4.1y.o.)volunteered
to participate in the test. For each experiment, the subject was
asked to read a description of the experiment and sign a con-
sent form. After signing the consent form, the experimental
protocol was explained to the subject. Each recording ses-
sion lasted 10 min and was organized in two parts, each of
duration 5 min, which is the standard recording window for
short-term HRV analysis (Task Force of The European Soci-
ety of Cardiology & The North American Society of Pacing
and Electrophysiology 1996). First, the subject was asked
to sit for 5 min while resting, that is not being involved in
any mental nor physical activity. Second, for the following
5 min, the subject was asked to perform an arithmetical task
and a fast counting test, while listening to loud annoying
music. These were considered to induce mental fatigue and
anxiety, respectively, which are typical affects arising in HRI
when the task to accomplish is complex and/or challenging
situational conditions occur. The arithmetical task is a stres-
sor commonly used in the literature of stress detection (Rani
et al. 2002, 2004; Castaldo et al. 2015). In our experiments,
it consisted in solving mathematical operations of increas-
ing difﬁculty, with countdown and score penalty in case of
wrong answers. All the involved subjects reported signiﬁ-
cantly increased mental stress in the second part of the test.
To detect mental fatigue, we considered the parameters
most commonly used in the literature of stress detection. In
particular, with reference to Sect. 2.2, for each subject, the
following parameters were computed for the two recording
windows, namely rest and stress: RR, SDRR, RMSSD and
pNN50 in the time domain, and LF, HF and LF/HF ratio in
the frequency domain. RR series were visually inspected by
an expert to verify the absence of ectopic beats (Clifford and
Tarassenko 2005). HRV metrics were computed in MATLAB
exploiting the tool presented in Vollmer (2015).
Table 1 reports the numerical results of our analysis on
stress detection, which shows that the index RR is the only
metrics able to detect a change in the mental status of the
study participants. In particular, a statistically signiﬁcant
decrease of the RR value was noticeable while the subject
was exposed to mental stress, in accordance with the litera-
ture (Castaldo et al. 2015). However, although several works
in the literature found a change also in RMSSD, power in
the LF and HF bands and LF/HF ratio (Bernardi et al. 2000;
Castaldo et al. 2016; Rani et al. 2002; Gohara et al. 1996),
this was not reﬂected in our results, probably due to poor
time resolution (20 ms) of data provided by the smartwatch
sensor.
Moreover, we considered the effectiveness of the above
mentioned indexes in detecting mental stress on shorter
time intervals. Indeed, as mentioned in Sect. 2.2, while
standard short-term HRV analysis is usually performed on
5-min recordings (Task Force of The European Society of
Cardiology & The North American Society of Pacing and
Electrophysiology 1996), research is considering the oppor-
tunity of measuring HRV from shorter recordings, aiming
at a faster detection of cardiovascular associated diseases or
physiological conditions (Nussinovitch et al. 2011; Munoz
et al. 2015). Speciﬁcally, according to the methodology con-
sidered in Nussinovitch et al. (2011), for the two parts of the
tests, namely rest and stress, segments of duration 2.5 min
were randomly extracted from each of the 5-min RR series,
and the HRV metrics in the time and frequency domain were
computed. We ran a total of 1000 Monte Carlo trials ran-
domizing the beginning of the newly extracted RR series, for
123

---
**[Page 6]**

606
Autonomous Robots (2020) 44:601–616
Table 1 Results of HRV
analysis for mental fatigue
detection
HRV measure
Mean
± SD
Statistical signiﬁcance
RR (s)
Rest:
0.867
± 0.125
YES
Stress:
0.835
± 0.131
(p = 0.04 < 0.05)
SDRR (s)
Rest:
0.159
± 0.068
NO
Stress:
0.158
± 0.077
(p = 0.95 > 0.05)
RMSSD (s)
Rest:
0.159
± 0.089
NO
Stress:
0.168
± 0.095
(p = 0.71 > 0.05)
pNN50 (%)
Rest:
67.30
± 7.71
NO
Stress:
68.59
± 8.08
(p = 0.49 > 0.05)
LF (ms2)
Rest:
40.056
± 4.751
NO
Stress:
40.055
± 4.785
(p = 1.00 > 0.05)
HF (ms2)
Rest:
59.944
± 4.751
NO
Stress:
59.945
± 4.785
(p = 1.00 > 0.05)
LF/HF (ms2)
Rest:
0.678
± 0.132
NO
Stress:
0.680
± 0.156
(p = 0.96 > 0.05)
Fig. 2 Histogram of statistical signiﬁcance of RR as a metrics to dis-
criminate mental workload on 2.5-min RR series
each subject and condition (rest or stress). The RR param-
eter conﬁrms good performance in stress detection, since it
returns a noticeable difference between the rest and stress
conditions:
Rest: RR = 0.871 ± 0.135
Stress: RR = 0.844 ± 0.149 (p = 0.02 < 0.05)
(1)
averaged over the extracted 21×1000 segments of RR series
of duration 2.5 min. In particular, the difference between the
two conditions in all the subjects was statistically signiﬁcant
with p < 0.05 in 854 out of 1000 runs, of which 436 gave
p < 0.01. Figure 2 reports the histogram of p values returned
by the Monte Carlo simulation regarding the use of RR as a
metrics to detect changes in mental stress level on RR series
2.5 min long. On the contrary, in any of the 1000 trials, none
of the other parameters in Table 1 returned a statistically
signiﬁcant (p < 0.1) difference between the rest and stress
conditions.
These results motivate the use of the index RR to adapt the
robot behavior to the user’s mental workload in the proposed
framework for human–multi-robot-system interaction.
4.2 Real-time detection of mental fatigue
Given the ﬁndings presented above, in the following we
introduce the rule for HRV analysis for real-time detection
of mental stress by means of a smartwatch (or a similar
wrist-worn device), together with its experimental valida-
tion. Speciﬁcally, HRV is measured in terms of mean value
of successive RR intervals, namely RR, computed on sliding
windows of ﬁxed duration.
In particular, we consider non overlapping sliding win-
dows collecting the inter-beat intervals that have occurred in
the last T (w) = 150 s. Thus, the mean value of each win-
dow, namely RRi, where i refers to the current window, is
computed as:
RRi = 1
Ni

k∈wi
RRk
(2)
where wi is the ith window of duration T (w), whose cardi-
nality is Ni.
Mental fatigue is then detected by comparing the quan-
tities RRi and RRi−1, since an increase in the level of
cognitive effort is reﬂected in a decrease of RR. Speciﬁcally,
we consider the following stress detection law:
Algorithm 1 Stress detection law
if (state == rest) then
if (RRi < RRi−1 −Δr→s) ∧(RRi < Γr) then
state = stress;
end if
else
if (RRi > RRi−1 + Δs→r) ∧(RRi > Γs) then
state = rest;
end if
end if
123

---
**[Page 7]**
*(This page contains a figure/chart/image not captured in text)*

Autonomous Robots (2020) 44:601–616
607
where Δr→s and Δs→r are constants denoting the minimum
variation required to detect a change in mental workload level
(from rest to stress and vice versa, respectively), and Γr and
Γs are constants denoting a threshold on the value of RR, as
explained shortly after. In particular, we set Δr→s = 0.02 s
from the difference between the average values of RR in
the rest and stress conditions presented in Sect. 4.1. We set
Δs→r = 0.5Δr→s to take into account the hysteresis of
human body to switch between rest and stress: in simple
terms, it takes longer to recover from stress to rest than to
get into stress from a rest condition (Thayer et al. 2012; Clif-
ford et al. 2006). The conditions involving Γr, and Γs are
introduced to reduce misdetection of stress. In particular, for
those subjects exhibiting high or low RR, a condition of rest
or stress, respectively, should be identiﬁed, irrespective of a
decrease or increase of RR. Γr and Γs denote the thresholds
for which this condition applies, and their values have been
empirically set to the 70th percentile of the RR values for
the rest and stress conditions presented in Sect. 4.1 (2.5-min
RR series). In particular, Γr = 0.94 s and Γs = 0.74 s.
5 Control of a multi-robot system
In this section we present a possible architecture to control
a team of robots by means of wrist movements. The con-
trol scheme is adapted according to information about user’s
mental fatigue.
By moving her/his wrist, the user can provide two differ-
ent kinds of commands to move the robots. On the one side,
direct teleoperation can be established, by mapping (continu-
ous) wrist rotations in velocity commands for the robots. On
the other side, high-level commands can be sent to the robots
by means of (discrete) gestures. Moreover, when increased
mental effort is detected, the behavior of the whole system
is modiﬁed, to allow the user to pursue the interaction task.
Figure 3 provides the state machine for the proposed con-
trol approach, which is described more in detail in the next
paragraphs.
In the following we consider a team of wheeled mobile
robots, moving in a two-dimensional space. However, the
control scheme can be easily extended to robots in three-
dimensional space, as shown in Sect. 6.4.
5.1 Natural mapping: teleoperation
Direct teleoperation of robots is implemented by establishing
a natural mapping of wrist movements into robots veloc-
ities. Brieﬂy, wrist pitch and roll angles are measured by
the smartwatch and transformed in input commands for the
robots,intermsoflinearandangularvelocities.Suchvelocity
commands can be, then, either broadcasted to all the robots
of the ﬂeet, or sent to the master elements, in the case a
hierarchy is set in the team, such as a master-slave organiza-
tion. In this last case, the user commands have effect on top
level robots, whereas the others implement some predeﬁned
behaviors (e.g., follow a master by a certain distance or move
around the master).
Considering, without any loss of generality, differential
drive robots, the linear and angular velocity commands are
(a)
(b)
Fig. 3 State machine for the selection of the operational mode
123

---
**[Page 8]**

608
Autonomous Robots (2020) 44:601–616
computed as follows:
v = Kr ϑr,
ω = K p ϑp
(3)
where v and ω are the robots linear and angular veloc-
ity, Kr > 0 and K p > 0 are constants deﬁned in such
a way that the maximum angle that is achievable with the
motion of the wrist corresponds to the maximum velocity of
the mobile robot, ϑr ∈[−π/2, π/2] is the roll angle and
ϑp ∈[−π/2, π/2] is the pitch angle. Further details can be
found in Villani et al. (2017a).
5.2 High-level commands: selection of the
operational mode
Different operational modes can be implemented to provide
multiple (semi-)autonomous behaviors to the multi-robot
system. To switch among operational modes, we consider
the use of discrete gestures. These are detected from inertial
data recorded by the smartwatch (Villani et al. 2017b). In par-
ticular, without loss of generality, we consider the following
gestures:
– Circle movement in a circular shape,
– Up sharp movement upwards,
– Down sharp movement downwards,
– Left sharp movement to the left,
– Right sharp movement to the right.
These gestures can be associated to different semi-
autonomous behaviors of the robots, such as commanding
(all or some of) the robots to move towards a predeﬁned
location, move with a ﬁxed velocity, stop down or move to a
given distance from a team mate.
In the application considered in this paper we consider as
interaction task the exploration of a large area. In this sce-
nario, the multi-robot team can be split in several sub-teams,
each of whom is assigned to a different subarea. Sub-teams
can explore subareas autonomously and alert the user when
needed (e.g., when a ﬁre or someone to rescue is detected,
depending on the practical application scenario). The user
can then take the control of the sub-team that generated the
alert and teleoperate it to accurately explore the subarea and
take proper action. While this speeds up the coverage of large
areas, it causes an increase in mental workload for the user,
who has to supervise the robots even when they are mov-
ing autonomously. As a consequence, it is necessary to track
her/his cognitive effort and assist her/him when she/he is
overwhelmed by the task.
We implement this system by considering the state
machine in Fig. 3. Speciﬁcally, with reference to Fig. 3a
the system is initialized in the Autonomous state, in which
no interaction between the user and the multi-robot system
occurs. In this state, the robots can be controlled by means of
the internal, preprogrammed, control algorithm. If no control
algorithm is deﬁned, as in our case, the robots are stopped.
If a localization algorithm is exploited, the robots can be
programmed to perform all the required initialization, such
as building a map of the environment and/or searching for
markers.
From the Autonomous state, the user can start the teleop-
eration of the whole team of robots by means of the Circle
gesture. Thus, the system moves to the Teleoperation entire
TEAM state, where all the robots are commanded by the
user, by moving the forearm according to (3). From this state,
the user can select any subset of robots by performing one
of the other gestures, thus moving to the state Teleopera-
tion SUB-TEAM i, with i = 1, 2, 3, 4. While SUB-TEAM
i is teleoperated, the others are partially autonomous and
follow a predeﬁned motion law, which depends on the mea-
sured mental fatigue of the user, as reported in Fig. 3b. If
the user is found to be at rest, the robots in SUB-TEAMS j,
j = 1, 2, 3, 4, j̸ = i (i = 1inFig.3b),arepreprogrammedto
explore the surroundings autonomously, moving with a pre-
deﬁned velocity. When an increase in user’s cognitive effort
is found, the same robots are given full autonomy in order
to relief the user from their control and not overload her/his
mental burden: the task is simpliﬁed, thus letting the user
focusing only on SUB-TEAM i.
It is worthwhile noting that in Fig. 3a the association
between a subset of robots and its gesture is arbitrary. More-
over, the detection of a gesture is notiﬁed to the user by means
of a short vibration of the smartwatch. Additionally, a sound
feedback is provided, notifying the user of which robots will
be teleoperated henceforth.
6 Experimental validation
We implemented a set of experiments to validate the pro-
posed interaction approach: the general objective of the
experiments is to validate the effectiveness of the proposed
affect-based interaction approach in relieving the user’s men-
tal workload. For this purpose, three sets of experiments were
performed. First, we assessed the effectiveness of the natu-
ral smartwatch-based interaction. Then, we considered the
adaptation of robot’s behavior based on the detected mental
strain. Finally, we tested the feasibility of the control archi-
tecture in Fig. 3 considering a complex scenario, which was
simulated in virtual reality (VR).
Interaction with robots was implemented by using a Sam-
sung Gear S smartwatch (Samsung, South Korea), which
embeds accelerometers, gyroscopes and a heart rate moni-
tor sensor measuring heart rate in terms of beats per minute
and successive RR intervals.
123

---
**[Page 9]**
*(This page contains a figure/chart/image not captured in text)*

Autonomous Robots (2020) 44:601–616
609
Table 2 Summary of the experiments for the validation of the proposed interaction approach
Experiment
Aim
Task goal
Implementation
tools
Test subjects
Natural
interaction
To test the intuitiveness and
effectiveness of
smartwatch-based natural
mapping to control robots
motion by wrist
movements and gesture
Driving the robots to pre-
deﬁned targets and selecting
them one by one by means of
gestures
Smartwatch and 3 epuck
robots; comparison with joy-
pad and teleoperation device
12 users (4
female, 8 male,
26.4 ± 2.9y.o.)
Affect-based
adaptation of
robots behavior
To assess the adaptation of
robots behavior based on
the detection of user’s
mental fatigue
Driving the robots to targets
avoiding collisions
Smartwatch and 2 epuck
robots
4 users (1 female,
3 males,
30.5 ± 3.1y.o.)
Complex real
scenario
To assess the feasibility of
the proposed interaction
approach in a realistic
complex scenario
Extinguishing ﬁres and
defusing bombs by hand
gestures in different
districts, depending on
sub-teams of robots
calling for user’s attention
Smartwatch, VR headset,
hand pose tracker, 12
simulated aerial robots
30 users (9
female, 21
male,
25.5 ± 3.0y.o.)
A team of e-pucks, which are differential drive wheeled
mobile robots (Mondada et al. 2009), was used in the ﬁrst two
experiments. Due to the limited computation capabilities of
the elaboration unit utilized for the control of such robots, an
external computer was utilized to implement gesture recog-
nition and perform HRV analysis, and the architecture was
implemented by means of ROS (Quigley et al. 2009) and
MATLAB (MathWorks, USA). Wi-Fi was used for commu-
nicating with the smartwatch and bluetooth with the team of
robots.
In the third experiment, a ﬂeet of drones was rendered
in the virtual environment, as described in Sect. 6.4. The
virtual environment was developed in Unity (Unity Tech-
nologies, USA), a free game development platform with a
built-in physics and rendering engine. The Oculus Rift head-
set (Oculus VR, USA) was used for immersive VR. ROS was
used to interact with the smartwatch and detect wrist pose and
heart rate.
Table 2 reports a summary of the three experiments.
6.1 Description of the attached video
Extracts of the experimental validation are reported in the
attached video. The ﬁrst part of the video shows how the
proposed smartwatch-based natural interaction works, with
reference to (3). Second, experiments about natural interac-
tion described in Sect. 6.2 are shown. Third, the experiment
on adaptation of robots behavior based on affect detection,
which is described in Sect. 6.3, is shown. Finally, we show an
extract of the experiment in the realistic scenario simulated
in VR, as described in Sect. 6.4.
Fig. 4 Visiting a set of targets: experimental setup for the validation of
the natural interaction approach
6.2 Natural interaction system
The aim of this experiment was to test the intuitiveness and
effectiveness of natural mapping to control robots motion
by wrist movements and gestures, without considering the
cognitive burden for the user.
To this end, the set-up depicted in Fig. 4 was considered.
Speciﬁcally, the users were requested ﬁrst to drive both the
robots (A and B) to the green square, following the paths in
solid lines in the ﬁgure; then each of the two robots (A or B)
had to be selected and driven to one of the two green crosses,
while the other robot (B or A) moved autonomously in circle,
as shown by the dashed lines. The users used gestures to
teleoperate the two robots together (Circle) or robot A or B
alone (Up or Down, respectively). The haptic device laid on
a table placed in the left bottom corner of Fig. 4, close to the
starting point of the robots. When using the smartwatch and
the joypad, the user was free to follow the robots, as shown
in the attached video.
123

---
**[Page 10]**
*(This page contains a figure/chart/image not captured in text)*

610
Autonomous Robots (2020) 44:601–616
Table 3 Comparison of the proposed interaction system with a tra-
ditional joypad and a haptic device for teleoperation. Travel time is
averaged on twelve users
Device
Travel time (s)
Smartwatch
199.6
Joypad
280.1
Teleoperation device
214.5
A total of N = 12 (4 female, 8 male, 26.4±2.9 y.o.) ﬁrst-
time users were involved in the experiment. The proposed
interaction approach was compared to a common joypad for
videogaming and a haptic device for teleoperation, namely
the Touch (3D Systems, USA). For both these devices, the
selection of the two robots or only one of them was done by
pressingadifferent buttononthejoypador ontheendeffector
of the teleoperation device, respectively. Performance was
measured in terms of total travel time across the path in Fig. 4.
The results of the experiment are reported in Table 3, which
shows that the task was faster to accomplish when using the
natural interaction based on the smartwatch.
The choice of having two (sub-teams of) robots com-
manded independently was driven by the need to select them
with the haptic device. Indeed, while common joypads host
several buttons, at least as many as the gestures we are con-
sidering, this is not true for haptic devices. Speciﬁcally, the
one used in this experiment has two buttons, which were used
to select robot A or B to follow the dashed lines in Fig. 4.
To deal with a greater number of (sub-teams of) robots and
implement a state machine similar to that in Fig. 3, some
movements or gestures should be considered also in the case
of the haptic device, as ﬁrst proposed in Secchi et al. (2015).
This will increase the complexity of the interaction and, rea-
sonably, the travel time.
Moreover, it is worthwhile noting that, as regards the hap-
tic device for teleoperation, by observing users performing
the task, it was clear that they found quite easy the use of this
device since the path was simple and straight. Some effort
was only required to ﬁnd the correct orientation for the end
effector at the beginning of the task and to get familiar with
the different orientation between the user and robot A or B in
the second part of the task. In more complex paths, with turns
and different orientations between the user’s and robots refer-
ence system, the use of the haptic device becomes much less
intuitive, as reported in Villani et al. (2017b) with respect to
the control of a single robot. This is clear also in the attached
video, when, after selecting robot A, the user ﬁnds it difﬁcult
to ﬁnd out the correct orientation of the robot.
Further, the use of the haptic device implies that the user
cannot move close to the robots, but is constrained to a ﬁxed
position. On the other side, one of the main advantages of
the proposed interaction approach is that the user can move
Fig. 5 Layout of the experiment for testing the proposed natural inter-
action based on affective robotics
followingtherobots,thusembeddinginteractioninrealspace
and implementing a tangible user interface (Hornecker and
Buur 2006). Speciﬁcally, the distance between the user and
the robots is not due to the interaction device itself, but rather
to the application scenario (for instance, in the case of an
obstructed route). While this advantage could be achieved
with a wireless joypad, which however implies a hands-non-
free interaction, it cannot be achieved with haptic devices.
As regards the joypad, it is worthwhile remarking that
the proposed smartwatch-based interaction outperforms the
joypad, despite the latter being an ad hoc device, designed
and developed for this kind of applications. This suggests
that the proposed system not only guarantees hands-free
and infrastructure-less interaction, but the natural mapping
provides also advantages in terms of usability and ease of
interaction, with respect to common devices, as already
shown also in Villani et al. (2017b).
6.3 Adaptation of robots behavior based on affect
detection
To assess the second feature of the proposed interaction
approach, namely the adaptation of robots behavior based
on the detection of user’s mental fatigue, the scenario shown
in Fig. 5 has been considered. A total of N = 4 (1 female, 3
males, age 30.5 ± 3.1 y.o.) users were involved in the exper-
iment, which lasted 7.5 min per user.
Three mobile robots were initially located in the middle of
the arena, as shown in the scheme in the left panel of Fig. 5.
The goal of the experiment was to drive the robots in the yel-
low areas by means of the smartwatch. Once all the robots
had been driven in a yellow area, the user was asked to drive
them out and, then, in the other yellow area, and over again
until the end of the experiment. The robots had to be driven
one by one, by using the gestures Up, Down and Right to
select them individually. While a robot was teleoperated by
the user, the others moved randomly to simulate autonomous
exploration of the arena. When a condition of mental fatigue
was found according to Algorithm 1, the task was simpliﬁed
to relieve the user’s mental burden. Speciﬁcally, the user was
allowed to drive only one robot, while the other two imple-
mented consensus (Wurman et al. 2008) to follow the robot
123

---
**[Page 11]**
*(This page contains a figure/chart/image not captured in text)*

Autonomous Robots (2020) 44:601–616
611
Fig. 6 Districts reproduced in the experiment in VR
commanded by the user. As a consequence, the burden of
selecting each robot by gestures was eliminated and no col-
lisions could happen with the robots randomly moving; on
the other side, this simpliﬁcation led to the potential loss of
ﬁeld information recorded by the autonomous robots.
An extract of the experiment can be seen in the second
part of the attached video. In particular, the effort required
to drive the robots independently, while avoiding collisions,
can be noted, together with the ease of interaction when the
user is responsible only for one robot, which is followed by
the two others.
6.4 Complex realistic scenario
The aim of this experiment was to assess the feasibility and
validity of the interaction approach and control architecture
proposed in Fig. 3 in a complex realistic setting. To this end,
VR was exploited since it allows to reliably replicate complex
real use cases that cannot be otherwise considered in tamed
laboratory settings. Moreover, VR provides a totally immer-
sive environment where the user’s senses are under control
of the system, thus allowing to reliably replicate her/his per-
ception and reaction, as proved in Villani et al. (2018a).
A urban scenario was created, consisting of the four
residential districts shown in Fig. 6. These districts were
populated with targets, such as bombs and ﬁres, calling for
user’s attention. Aﬂeet of aerial robots surveilledthearea: the
robots were organized in four sub-teams (with three drones
in each). Each sub-team was then assigned to a different dis-
trict. The robots are supposed to be endowed with appropriate
sensors (e.g., heat sensors) to detect the targets. However,
user’s intervention is required to verify the detected target,
accurately locate it and then take proper action. The user can
teleoperate a sub-team at a time, according to Fig. 3, while
the other sub-teams are in charge of autonomous exploration
of a district to search for targets. When a target is detected
by the robots, a visual and auditory alert is sent to the user.
She/he can then decide to switch to the district calling for
attention or continue teleoperating the current sub-team, in
Fig. 7 Information shown to the user during the interaction task. The
arrows denote the four districts and represent the gesture associated to
each of them. Red arrows denote the districts where the robots have
currently detected a target, during autonomous exploration. The arrow
with green mark underneath denotes the district where the user is cur-
rently acting. In this example, the user is in the district associated to
the Left gesture and the robots ﬂying over it are currently detecting a
target. A target is also being detected by robots in the district associate
to the Down gesture. The user can, then, decide whether to explore the
target in the current district or move to the other district and extinguish
the ﬁre or defuse the bomb detected therein (Color ﬁgure online)
(a)
(b)
Fig. 8 Hand gestures to deactivate targets
the case that there are several targets being detected simulta-
neously. Gestures can be used to switch among districts. An
example of information prompted to the user during interac-
tion is shown in Fig. 7. To act on a target (i.e., extinguish a ﬁre
by delivering a water jet or defuse a bomb), hand gestures are
exploited. To this end, left hand pose is tracked by means of
a Leap Motion controller (Leap Motion, USA) mounted on
the VR headset. Figure 8 shows the hand gestures recognized
to deactivate targets.
During the task, the user’s cognitive burden is measured
and, when a condition of mental fatigue is detected, the task is
simpliﬁed. Speciﬁcally, the user is relieved of the supervision
of the other districts and can thus focus exclusively on the one
where she/he is currently. Visual and auditory alerts about the
districts other than the one the user is in are deactivated. The
robots in the other sub-teams are provided with full auton-
omy: when a target is detected, action is autonomously taken
to deactivate it, even in the case of misdetection or inaccurate
detection.
A total of N = 30 users (9 females, 21 males, age
25.5 ± 3.0y.o.) were enrolled in the experiments. Partici-
pants are researchers working at our engineering department,
in different research ﬁelds. All of them were completely new
to the experimental task and goals. At the beginning of the
123

---
**[Page 12]**
*(This page contains a figure/chart/image not captured in text)*

612
Autonomous Robots (2020) 44:601–616
Fig. 9 Organization of the experimental session in VR scenario
Fig. 10 Histogram of mental fatigue detection during the two recording
windows in the experiment in VR
experiment, each subject was asked to read a description of
theexperimentalprotocolandsignaconsentform.Theexper-
iment had a total duration of 7.5 min: in the ﬁrst 2.5 min,
baseline heart rate was recorded with the subject at rest; the
next 5 min consisted in the experiment in VR. In this inter-
val, mental fatigue was computed twice, after 2.5 min from
the beginning of the experiment and at the end. When men-
tal fatigue was found at 2.5 min, then adaptation of robots
behavior was implemented in the following time window,
according to Fig. 3b. The organization of the experimental
session is depicted in Fig. 9. At the end of the experiment,
test subjects were administrated a short questionnaire asking
for subjective reporting about the experiment.
In Fig. 10 we report the results of mental fatigue detection
during the experiment under analysis. In particular:
– 2userswerefoundatrest(i.e.,nomentalfatiguedetected)
during the whole experiment (ﬁrst bar in Fig. 10);
– 9 users were found at rest at the end of the ﬁrst recording
window, but exhibited mental fatigue at the end of the
experiment (second bar in Fig. 10);
– 4 users reported an increase in mental fatigue in the ﬁrst
recording window and a relief from this condition was
detected at the end of the experiment, as a consequence
of the provided adaptation of robots behavior (third bar
in Fig. 10);
– 15 users reported an increase in mental fatigue in the ﬁrst
recording window and this condition was conﬁrmed at
Fig. 11 The simpliﬁcation in the task introduced by affect-based adap-
tation of robots behavior was effective
the end of the experiment, despite of the adaptation of
robots behavior (fourth bar in Fig. 10).
Test subjects who experienced affect-based adaptation of
robots behavior (i.e., those in the last two groups in the list
above; 19 subjects over 30) were then asked whether they
found the interaction task easier after adaptation. Figure 11
reports the answers collected. In particular, it is worth-
while noting that also those subjects who experienced mental
fatigue during the whole experiment (i.e., those in the last
group; 15 subjects) still reported that they had found adapta-
tion useful, although their stress response did not change
when adaptation was provided. Among them, 8 subjects
answered strongly agree, 4 answered agree, and 3 neutral.
7 Conclusion
In this paper we introduced a novel approach to human–
multi-robot-system interaction. Customarily, research in
multi-robot systems has focused on letting the robots
autonomously collaborate among each other to achieve a
common goal. The intervention of a human operator has been
rarely considered, despite the fact that she/he could provide
high-level reasoning capabilities to the system. Additionally,
when the human interaction has been considered, systems
have generally been developed focusing on task execution
performance, paying only little attention to the intuitiveness
of the interaction from the user’s perspective and the conse-
quent cognitive effort due to the charge of supervising and
interacting with multiple robots.
In this paper we reversed this approach, focusing on how
the multi-robot system can accommodate the needs of the
user. This was achieved proposing an intuitive interaction
system, and adapting the behavior of the multi-robot system
to the user. The interaction is based on the use of a commer-
cial multi-purpose wearable device, such as a smartwatch,
that tracks wrist movements and heart activity. Natural map-
123

---
**[Page 13]**

Autonomous Robots (2020) 44:601–616
613
ping of forearm movements into robots motion commands
allows to intuitively drive the robots and gestures are used
to provide high-level commands to the team of robots. HRV
is considered to estimate user’s mental fatigue. Accordingly,
the robots behavior is adapted when an increase in user’s
mental fatigue is detected, thus simplifying the interaction
task.
The experimental validation of the proposed approach was
presented in the paper and in the attached video. Speciﬁ-
cally, we assessed the effectiveness of the concept of natural
interaction, and compared it to the use of a joypad and a
haptic device. Moreover, we tested the affective interaction
approach. A complex realistic scenario was implemented
in virtual reality in order to consider the effectiveness and
appropriateness of the proposed approach in practical situa-
tions requiring a human operator supervising a multi-robot
system.
A more extensive experimental validation of the system
will be performed as a future work. Further, we aim at study-
ing the possibility of a multi-modal interaction exploiting
speech inputs, to complement audio feedback, for example
as in Cacace et al. (2016b).
Moreover, further effort will be devoted to the analysis of
HRV to detect user’s mental fatigue. In particular, we aim at
studyinganddecouplingtheeffectthatphysicalfatiguemight
have on HRV and, hence, on mental fatigue detection. Addi-
tionally, for a more accurate detection of cognitive workload,
we are interested in studying the effect of task engagement
on heart activity. Speciﬁcally, as future work, we will investi-
gate whether disengagement, boredom and tiredness during
the execution of the interaction task affect HRV, thus leading
to false positives with respect to detected mental fatigue.
As a ﬁnal remark, in this paper we focused on the devel-
opment of an adaptive interaction system, with the objective
of accommodating user needs, in terms of fatigue and men-
tal workload. Providing assistance to the user has a positive
impact on her/his fatigue but, at the same time, decreases the
performance of the task to be executed. Future work will aim
at simultaneously considering task-related and user-centered
metrics, in order to ﬁnd a trade-off between assistance and
performance, and to relate the level of adaptation to task-
speciﬁc needs and constraints.
References
Acharya, U. R., Joseph, K. P., Kannathal, N., Lim, C. M., & Suri, J. S.
(2006). Heart rate variability: A review. Medical and Biological
Engineering and Computing, 44(12), 1031–1051.
Andreasson, H., Bouguerra, A., Cirillo, M., Dimitrov, D. N., Driankov,
D., Karlsson, L., et al. (2015). Autonomous transport vehicles:
Where we are and what is missing. IEEE Robotics Automa-
tion Magazine, 22(1), 64–75. https://doi.org/10.1109/MRA.2014.
2381357.
Antonelli, G., Arrichiello, F., Caccavale, F., & Marino, A. (2014).
Decentralized time-varying formation control for multi-robot
systems. The International Journal of Robotics Research, 33,
1029–1043.
Ball, D., Ross, P., English, A., Patten, T., Upcroft, B., Fitch, R., et al.
(2015). Robotics for sustainable broad-acre agriculture. In L.
Mejias, P. Corke, & J. Roberts (Eds.), Field and service robotics
(pp. 439–453). Cham: Springer.
Bernardi, L., Wdowczyk-Szulc, J., Valenti, C., Castoldi, S., Passino, C.,
Spadacini, G., et al. (2000). Effects of controlled breathing, mental
activity and mental stress with or without verbalization on heart
rate variability. Journal of the American College of Cardiology,
35(6), 1462–1469.
Bonarini, A., Mainardi, L., Matteucci, M., Tognetti, S., & Colombo,
R. (2008). Stress recognition in a robotic rehabilitation task. In
Robotic helpers: User interaction, interfaces and companions
in assistive and therapy robotics (pp. 41–48). A workshop at
ACM/IEEE HRI.
Braezal, C., Dautenhahn, K., & Kanda, T. (2016). Social robotics. In
B. Siciliano & O. Khatib (Eds.), Springer handbook of robotics,
chap 72 (2nd ed., pp. 1935–1971). New York: Springer.
Brookhuis, K. A., & de Waard, D. (2010). Monitoring drivers’ men-
tal workload in driving simulators using physiological measures.
Accident Analysis & Prevention, 42(3), 898–903.
Cacace, J., Caccavale, R., Finzi, A., & Lippiello, V. (2016a). Attentional
multimodal interface for multidrone search in the Alps. In IEEE
international conference on systems, man, and cybernetics (SMC)
(pp. 001178–001183). IEEE.
Cacace, J., Finzi, A., & Lippiello, V. (2016b). Implicit robot selection
for human multi-robot interaction in search and rescue missions. In
Proceedingsof IEEEinternational symposiumonrobot andhuman
interactive communication (RO-MAN) (pp. 803–808). IEEE.
Castaldo, R., Melillo, P., Bracale, U., Caserta, M., Triassi, M., & Pec-
chia, L. (2015). Acute mental stress assessment via short term HRV
analysis in healthy adults: A systematic review with meta-analysis.
Biomedical Signal Processing and Control, 18, 370–377.
Castaldo, R., Xu, W., Melillo, P., Pecchia, L., Santamaria, L., &
James, C. (2016). Detection of mental stress due to oral academic
examination via ultra-short-term HRV analysis. In Proceedings of
IEEE 38th annual international conference of the engineering in
medicine and biology society (EMBC) (pp. 3805–3808). IEEE.
Clifford, G. D., Azuaje, F., & McSharry, P. (Eds.). (2006). Advanced
methodsandtoolsforECGdataanalysis.Norwood:ArtechHouse,
Inc,
Clifford, G. D., & Tarassenko, L. (2005). Quantifying errors in spectral
estimates of HRV due to beat replacement and resampling. IEEE
Transactions on Biomedical Engineering, 52(4), 630–638.
de la Croix, JP., & Egerstedt, M. (2015). A control lyapunov function
approach to human–swarm interactions. In American control con-
ference (ACC), 2015 (pp. 4368–4373). IEEE.
Diana, M., de la Croix, JP., & Egerstedt, M. (2013). Deformable-
medium affordances for interacting with multi-robot systems. In
2013 IEEE/RSJ International conference on intelligent robots and
systems (IROS) (pp. 5252–5257). IEEE.
Diaz-Mercado, Y., Lee, S. G., & Egerstedt, M. (2017). Human–swarm
interactions via coverage of time-varying densities (pp. 357–385).
Cham: Springer.
Dietz, G., Washington, P., Kim, LH., & Follmer, S. et al. (2017). Human
perception of swarm robot motion. In Proceedings of the 2017
CHI conference extended abstracts on human factors in computing
systems (pp 2520–2527). ACM.
Draganjac, I., Mikli´c, D., Kovaˇci´c, Z., Vasiljevi´c, G., & Bogdan, S.
(2016). Decentralized control of multi-agv systems in autonomous
warehousing applications. IEEE Transactions on Automation Sci-
ence and Engineering, 13(4), 1433–1447.
123

---
**[Page 14]**

614
Autonomous Robots (2020) 44:601–616
English, A., Ball, D., Ross, P., Upcroft, B., Wyeth, G., & Corke, P.
(2013). Low cost localisation for agricultural robotics. In Proceed-
ings of 2013 Australasian conference on robotics & automation
(pp. 1–8). Australian Robotics & Automation Association.
Fanti, MP., Mangini, AM., Pedroncelli, G., & Ukovich, W. (2015).
Decentralized deadlock-free control for agv systems. In Ameri-
can control conference (ACC), 2015 (pp. 2414–2419). IEEE.
Franchi, A., Secchi, C., Son, H. I., Bulthoff, H. H., & Robuffo Giordano,
P. (2012). Bilateral teleoperation of groups of mobile robots with
time-varying topology. IEEE Transactions on Robotics, 28(5),
1019–1033.
Gioioso, G., Franchi, A., Salvietti, G., Scheggi, S., & Prattichizzo, D.
(2014). The ﬂying hand: A formation of UAVs for cooperative
aerial tele-manipulation. In 2014 IEEE International conference
on robotics and automation (ICRA) (pp. 4335–4341). IEEE.
Gohara, T., Mizuta, H., Takeuchi, I., Tsuda, O., Yana, K., Yanai, T., et al.
(1996). Heart rate variability change induced by the mental stress:
The effect of accumulated fatigue. In Proceedings of 15th southern
biomedical engineering conference (pp. 367–369). IEEE.
Gromov, B., Gambardella, LM., & Di Caro, GA. (2016). Wearable
multi-modal interface for human multi-robot interaction. In IEEE
international symposium on safety, security, and rescue robotics
(SSRR) (pp. 240–245). IEEE.
Gunes, H., Nicolaou, M. A., & Pantic, M. (2011). Continuous analysis
of affect from voice and face (pp. 255–291). London: Springer.
Hocraffer, A., & Nam, C. S. (2017). A meta-analysis of human-system
interfaces in unmanned aerial vehicle (UAV) swarm management.
Applied Ergonomics, 58, 66–80.
Hoover, A., Singh, A., Fishel-Brown, S., & Muth, E. (2012). Real-
time detection of workload changes using heart rate variability.
Biomedical Signal Processing and Control, 7(4), 333–341.
Hornecker, E., & Buur, J. (2006). Getting a grip on tangible interaction:
A framework on physical space and social interaction. In Proceed-
ings of the SIGCHI conference on human factors in computing
systems (CHI) (pp. 437–446). ACM Press.
Kapellmann-Zafra, G., Salomons, N., Kolling, A., & Groß, R. (2016).
Human–robot swarm interaction with limited situational aware-
ness. In M. Dorigo, M. Birattari, X. Li, M. López-Ibáñez, K.
Ohkura, C. Pinciroli, & T. Stützle (Eds.), Swarm intelligence (pp.
125–136). Cham: Springer International Publishing.
Kolling, A., Walker, P., Chakraborty, N., Sycara, K., & Lewis, M.
(2016). Human interaction with robot swarms: A survey. IEEE
Transactions on Human–Machine Systems, 46(1), 9–26.
Kulic, D., & Croft, E. A. (2007). Affective state estimation for
human–robot interaction. IEEE Transactions on Robotics, 23(5),
991–1000.
Lin, CW., & Liu, YC. (2017). Decentralized estimation and control for
bilateral teleoperation of mobile robot network with task abstrac-
tion. In Proceedings of IEEE international conference on robotics
and automation (ICRA) (pp. 5384–5391). IEEE.
Luque-Casado, A., Zabala, M., Morales, E., Mateo-March, M., &
Sanabria, D. (2013). Cognitive performance and heart rate vari-
ability: The inﬂuence of ﬁtness level. PloS ONE, 8(2), e56935.
Melillo, P., Bracale, M., & Pecchia, L. (2011). Nonlinear heart rate vari-
ability features for real-life stress detection. case study: Students
under stress due to university examination. Biomedical Engineer-
ing Online, 10(1), 96.
Mondada, F., Bonani, M., Raemy, X., Pugh, J., Cianci, C., Klaptocz, A.,
et al. (2009). The e-puck, a robot designed for education in engi-
neering. In Proceedings of 9th conference on autonomous robot
systems and competitions (vol. 1, pp. 59–65).
Mondada, L., Karim, M. E., & Mondada, F. (2016). Electroencephalog-
raphy as implicit communication channel for proximal interaction
between humans and robot swarms. Swarm Intelligence, 10(4),
247–265. https://doi.org/10.1007/s11721-016-0127-0.
Munoz, M. L., van Roon, A., Riese, H., Thio, C., Oostenbroek, E.,
Westrik, I., et al. (2015). Validity of (ultra-) short recordings for
heart rate variability measurements. PloS ONE, 10(9), e0138921.
Nagi, J., Giusti, A., Gambardella, LM., & Di Caro, GA. (2014).
Human–swarm interaction using spatial gestures. In IEEE/RSJ
International conference on intelligent robots and systems (IROS)
(pp. 3834–3841). IEEE.
Nussinovitch, U., Elishkevitz, K. P., Katz, K., Nussinovitch, M., Segev,
S., Volovitz, B., et al. (2011). Reliability of ultra-short ECG indices
for heart rate variability. Annals of Noninvasive Electrocardiology,
16(2), 117–122.
Podevijn, G., O’Grady, R., Mathews, N., Gilles, A., Fantini-Hauwel,
C., & Dorigo, M. (2016). Investigating the effect of increasing
robot group sizes on the human psychophysiological state in the
context of human–swarm interaction. Swarm Intelligence, 10(3),
193–210. https://doi.org/10.1007/s11721-016-0124-3.
Pourmehr, S., Monajjemi, VM., Vaughan, R., & Mori, G. (2013). “you
two! take off!”: Creating, modifying and commanding groups of
robots using face engagement and indirect speech in voice com-
mands. In IEEE/RSJ international conference on intelligent robots
and systems (IROS) (pp. 137–142). IEEE.
Quigley, M., Conley, K., Gerkey, B., Faust, J., Foote, T., Leibs, J., et al.
(2009). ROS: an open-source robot operating system. In: Proceed-
ing of ICRA workshop open source software (vol. 3, p. 5).
Rani, P., Sarkar, N., Smith, C. A., & Kirby, L. D. (2004). Anxiety detect-
ing robotic system-towards implicit human–robot collaboration.
Robotica, 22(1), 85–95.
Rani, P., Sims, J., Brackin, R., & Sarkar, N. (2002). Online stress detec-
tion using psychophysiological signals for implicit human–robot
cooperation. Robotica, 20(06), 673–685.
Ren, W., & Beard, R. W. (2005). Consensus seeking in multiagent
systems under dynamically changing interaction topologies. IEEE
Transactions on Automatic Control, 50(5), 655–661.
Ren, W., & Beard, R. W. (2008). Distributed consensus in multi-vehicle
cooperative control: Theory and applications. London: Springer.
Rich, C., Ponsler, B., Holroyd, A., & Sidner, CL. (2010). Recogniz-
ing engagement in human–robot interaction. In 5th ACM/IEEE
international conference on human–robot interaction (HRI) (pp.
375–382). IEEE.
Ryu, K., & Myung, R. (2005). Evaluation of mental workload with a
combined measure based on physiological indices during a dual
task of tracking and mental arithmetic. International Journal of
Industrial Ergonomics, 35(11), 991–1009.
Sabattini, L., Aikio, M., Beinschob, P., Boehning, M., Cardarelli,
E., Digani, V., et al. (2018). The pan-robots project: Advanced
automated guided vehicle systems for industrial logistics. IEEE
Robotics Automation Magazine, 25(1), 55–64.
Sabattini, L., Secchi, C., Cocetti, M., Levratti, A., & Fantuzzi, C. (2015).
Implementation of coordinated complex dynamic behaviors in
multi-robot systems. IEEE Transactions on Robotics, 31(4), 1018–
1032.
Secchi, C., Sabattini, L., & Fantuzzi, C. (2015). Conducting multi-robot
systems: Gestures for the passive teleoperation of multiple slaves.
In Proceedings of the IEEE/RSJ international conference on intel-
ligent robots and systems (IROS) Germany: Hamburg.
Shcherbina, A., Mattsson, C. M., Waggott, D., Salisbury, H., Christle, J.
W., Hastie, T., et al. (2017). Accuracy in wrist-worn, sensor-based
measurements of heart rate and energy expenditure in a diverse
cohort. Journal of Personalized Medicine, 7(2), 3.
Task Force of The European Society of Cardiology & The North Amer-
ican Society of Pacing and Electrophysiology. (1996). Heart rate
variability: Standards of measurement, physiological interpreta-
tion, and clinical use. European Heart Journal, 17, 354–381.
Thayer, J. F., Åhs, F., Fredrikson, M., Sollers, J. J., & Wager, T. D.
(2012). A meta-analysis of heart rate variability and neuroimaging
studies: Implications for heart rate variability as a marker of stress
123

---
**[Page 15]**
*(This page contains a figure/chart/image not captured in text)*

Autonomous Robots (2020) 44:601–616
615
and health. Neuroscience & Biobehavioral Reviews, 36(2), 747–
756.
Villani, V., Capelli, B., & Sabattini, L. (2018a). Use of virtual reality
for the evaluation of human–robot interaction systems in complex
scenarios. In IEEE (ed) 27th IEEE international symposium on
robot and human interactive communication (RO-MAN).
Villani, V., Sabattini, L., Battilani, N., & Fantuzzi, C. (2016).
Smartwatch–enhanced interaction with an advanced troubleshoot-
ing system for industrial machines. IFAC-PapersOnLine, 49(19),
277–282.
Villani, V., Sabattini, L., Czerniak, J. N., Mertens, A., & Fantuzzi,
C. (2018b). MATE robots simplifying my work: Beneﬁts and
socio-ethical implications. IEEE Robotics & Automation Maga-
zine, 25(1), 37–45.
Villani, V., Sabattini, L., Riggio, G., Levratti, A., Secchi, C., & Fan-
tuzzi, C. (2017a). Interacting with a mobile robot with a natural
infrastructure-less interface. In Proceedings of IFAC 20th world
congress international federation automation control IFAC IFAC-
PapersOnLine.
Villani, V., Sabattini, L., Riggio, G., Secchi, C., Minelli, M., & Fantuzzi,
C. (2017b). A natural infrastructure-less human–robot interaction
system. IEEE Robotics and Automation Letters, 2(3), 1640–1647.
Villani, V., Sabattini, L., Secchi, C., & Fantuzzi, C. (2017c). Natural
interaction based on affective robotics for multi-robot systems. In
International symposium on multi-robot and multi-agent systems
(MRS) (pp. 56–62). IEEE.
Villani, V., Sabattini, L., Secchi, C., & Fantuzzi, C. (2018c). A frame-
work for affect-based natural human–robot interaction. In IEEE
(ed)27thIEEEinternationalsymposiumonrobotandhumaninter-
active communication (RO-MAN).
Vollmer, M. (2015). A robust, simple and reliable measure of heart rate
variability using relative RR intervals. In Computing in cardiology
conference (CinC), 2015 (pp. 609–612). IEEE.
Wallen, M. P., Gomersall, S. R., Keating, S. E., Wisløff, U., & Coombes,
J. S. (2016). Accuracy of heart rate watches: Implications for
weight management. PLoS ONE, 11(5), e0154420.
Wilson, G. F., & Russell, C. A. (2003). Real-time assessment of mental
workload using psychophysiological measures and artiﬁcial neural
networks. Human factors, 45(4), 635–644.
Wilson, P. A., & Lewandowska-Tomaszczyk, B. (2014). Affective
robotics: Modelling and testing cultural prototypes. Cognitive
Computation, 6, 814–840.
Wurman, P. R., D’Andrea, R., & Mountz, M. (2008). Coordinating
hundreds of cooperative, autonomous vehicles in warehouses. AI
Magazine, 29(1), 9.
Publisher’s Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional afﬁliations.
Valeria Villani is Assistant Pro-
fessor at the Department of Sci-
ences and Methods for Engineer-
ing of the University of Modena
and Reggio Emilia since 2017.
She received her B.Sc. and M.Sc.
in Biomedical Engineering from
the
University
Campus
Bio-Medico of Rome in 2006 and
2009, respectively, and her Ph.D.
in
Biomedical
Engineering
from
the
University
Campus
Bio-Medico of Rome in 2013,
focusing on biomedical signal pro-
cessing, with emphasis on ECG
signals. She was the recipient of the Best Paper Award at ISABEL
2011 and the Mortara Fellowship at CinC 2014. Her research inter-
ests focus on the design of human-centred user interfaces for efﬁcient
cooperation between the human and industrial machines or robots and
biomedical signal processing for robot control and affective human–
robot interaction.
Beatrice Capelli is Research Fol-
low at the Department of Sci-
ences and Methods for Engineer-
ing of the University of Modena
and Reggio Emilia since 2018.
She received her B.Sc. and M.Sc.
in Mechatronic Engineering from
the University of Modena and
Reggio Emilia in 2015 and 2018,
respectively. Her research inter-
ests include human–robot inter-
action, multi-robot systems and
virtual
reality
applications
to
robotics.
Cristian Secchi received the M.Sc.
degree in Computer Science Engi-
neering, from the University of
Bologna, Italy, in 2000 and the
Ph.D. in Information Engineering,
from the University of Modena
and Reggio Emilia, Italy, in 2004.
He has been visiting student at the
University of Delft (NL) and at
the University of Twente (NL) in
2000 and in 2002 respectively. He
is currently an Associate Profes-
sor at the University of Modena
and Reggio Emilia. His research
deals with human–robot physical
interaction, telerobotics, mobile robotics and surgical robotics and he
has published more than 100 papers on international journals and con-
ferences. His Ph.D. thesis has been selected as one of he three ﬁnalists
of the 5th Georges Giralt Award for the best Ph.D. thesis on robotics
in Europe. He has been co-chair of the IEEE Robotics and Automa-
tion Society Technical Committee on Telerobotics for 2007–2012. He
has been a guest Editor for the Special Issue on Design and Con-
trol Methodologies in Telerobotics, published on Elsevier Mechatron-
ics in October 2010. He has served as Associate Editor of the IEEE
Robotics and Automation Magazine from January 2005 to December
2008. Since September 2012 he is serving as an Associate Editor of
the IEEE Transactions on Robotics and since June 2015 he is serving
as an Associate Editor for the IEEE Robotics and Automation Letters.
123

---
**[Page 16]**
*(This page contains a figure/chart/image not captured in text)*

616
Autonomous Robots (2020) 44:601–616
Cesare Fantuzzi received the M.S.
degree in electrical engineering
and the Ph.D. degree in system
engineering from the University
of Bologna, Bologna, Italy, in
1990 and 1995, respectively. From
1996 to 2000, he was an Assis-
tant Professor of Automatic Con-
trol with the University of Ferrara,
Ferrara, Italy, and from 2000 to
2006, he was an Associate Pro-
fessor of Automatic Control with
the Engineering Faculty in Reg-
gio Emilia, University of Modena
and Reggio Emilia, Reggio Emilia,
Italy, where he has been a Full Professor, since 2006. He has held a
variety of positions as the Project Leader in several applied research
programs developed in cooperation with small, large, and multina-
tional companies in the ﬁeld of packaging machinery builder and man-
ufacturing sector. His current research interests include theory and
application of discrete-event control for automatic machinery and in
the modeling and control of mechatronics system and robots.
Lorenzo Sabattini is an Assistant
Professor at the Department of
Sciences and Methods for Engi-
neering, University of Modena
and Reggio Emilia, Italy, since
2013. He received his B.Sc. and
M.Sc. in Mechatronic Engineer-
ing from the University of Mod-
ena and Reggio Emilia (Italy) in
2005 and 2007 respectively, and
his Ph.D. in Control Systems and
Operational Research from the
University of Bologna (Italy) in
2012. In 2010 he has been a Vis-
iting Researcher at the University
of Maryland, College Park, MD (USA). His main research interests
include multi-robot systems, decentralized estimation and control con-
trol, and mobile robotics. He is one of the founding co-chairs of the
IEEE RAS Technical Committee on Multi-Robot Systems: he has
served as the corresponding co-chair since its foundation, in 2014.
He has been serving as Associate Editor for the IEEE Robotics and
Automation Letters since 2015, and for IEEE Robotics and Automa-
tion Magazine since 2017.
123
