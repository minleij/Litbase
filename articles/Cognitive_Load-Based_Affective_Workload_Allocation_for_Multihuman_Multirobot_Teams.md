# Cognitive Load-Based Affective Workload Allocation for Multihuman Multirobot Teams

*Source file: Cognitive_Load-Based_Affective_Workload_Allocation_for_Multihuman_Multirobot_Teams.pdf — 14 pages*


---
**[Page 1]**

IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 55, NO. 1, FEBRUARY 2025
23
Cognitive Load-Based Affective Workload
Allocation for Multihuman Multirobot Teams
Wonse Jo
, Ruiqi Wang
, Graduate Student Member, IEEE, Baijian Yang
, Member, IEEE, Daniel Foti
,
Mo Rastgaar
, Senior Member, IEEE, and Byung-Cheol Min
, Senior Member, IEEE
Abstract—The interaction and collaboration between humans
and multiple robots represent a novel ﬁeld of research known as
human multirobot systems. Adequately designed systems within
this ﬁeld allow teams composed of both humans and robots to
work together effectively on tasks, such as monitoring, exploration,
and search and rescue operations. This article presents a deep
reinforcement learning-based affective workload allocation con-
troller speciﬁcally for multihuman multirobot teams. The pro-
posed controller can dynamically reallocate workloads based on
the performance of the operators during collaborative missions
with multirobot systems. The operators’ performances are eval-
uated through the scores of a self-reported questionnaire (i.e.,
subjective measurement) and the results of a deep learning-based
cognitive workload prediction algorithm that uses physiological
and behavioral data (i.e., objective measurement). To evaluate the
effectiveness of the proposed controller, we conduct an exploratory
user experiment with various allocation strategies. The user ex-
periment uses a multihuman multirobot CCTV monitoring task as
an example and carry out comprehensive real-world experiments
with 32 human subjects for both quantitative measurement and
qualitative analysis. Our results demonstrate the performance and
effectiveness of the proposed controller and highlight the impor-
tance of incorporating both subjective and objective measurements
of the operators’ cognitive workload as well as seeking consent for
workload transitions, to enhance the performance of multihuman
multirobot teams.
Index Terms—Affective computing, cognitive load, human–
robot interaction (HRI), multihuman multirobot (MH-MR) teams,
multirobot systems (MRSs), workload allocation.
Received 19 August 2023; revised 31 March 2024, 2 September 2024, and 29
October 2024; accepted 25 November 2024. Date of publication 27 December
2024; date of current version 5 February 2025. This work was supported by
the National Science Foundation under Grant IIS-1846221. This article was
recommended by Associate Editor Mark Pfaff. (Corresponding author: Byung-
Cheol Min.)
This work involved human subjects or animals in its research. Approval of
all ethical and experimental procedures and protocols was granted by Purdue
University Institutional Review Board (IRB) under Application No. IRB-2021-
1813.
Wonse Jo, Ruiqi Wang, Baijian Yang, and Byung-Cheol Min are with the
Department of Computer and Information Technology, Purdue University, West
Lafayette, IN 47906 USA (e-mail: jow@purdue.edu; wang5357@purdue.edu;
byang@purdue.edu; minb@purdue.edu).
Daniel Foti is with the Department of Psychological Sciences, Purdue Uni-
versity, West Lafayette, IN 47906 USA (e-mail: foti@purdue.edu).
Mo Rastgaar is with the School of Engineering Technology, Purdue Univer-
sity, West Lafayette, IN 47906 USA (e-mail: rastgaar@purdue.edu).
This
article
has
supplementary
material
provided
by
the
au-
thors
and
color
versions
of
one
or
more
ﬁgures
available
at
https://doi.org/10.1109/THMS.2024.3509223.
Digital Object Identiﬁer 10.1109/THMS.2024.3509223
I. INTRODUCTION
A
S artiﬁcial intelligence continues to advance, multirobot
systems (MRSs) are demonstrating consistent perfor-
mance and precision that surpasses human ability in various
large-scale operations, such as surveillance [1], search and res-
cue [2], and assembly [3]. However, compared to human’s capa-
bilities, MRS still has deﬁciencies in situational awareness (SA)
when it comes to effectively handling complex task dynamics
in the real world [4]. For example, adjusting the operation of
an MRS in a timely manner in response to new missions and
environmental changes can be challenging when operating the
systemforanextendedperiodoftime.Thisissueiscurrentlymit-
igated by having a human operator participate in task execution,
which improves efﬁciency. However, systems with many robots
can produce excessively high cognitive workload (CWL) for a
single human operator, making it difﬁcult for them to track each
robot’swork.Thiscanbeaddressedbyhavingmultipleoperators
in the loop to provide some level of supervision, resulting in a
multihuman multirobot (MH-MR) team.
While incorporating human operators as the core of the
decision-making process can signiﬁcantly improve the system’s
SA and ﬂexibility, it can also introduce more uncertainty and
complexity. Human affective conditions, such as CWL and emo-
tion, as well as performance, are inconsistent and susceptible
to internal or external factors [5], [6], [7]. Thus, optimizing
the performance of the entire MH-MR team, including optimal
workload and workload allocation among multiple humans, is
a crucial challenge. The system must monitor human affective
states and reallocate workload accordingly, such as the number
of robots to be supervised, to maintain each human in optimal
interaction conditions with robots [8], [9], [10].
While the workload allocation in MRS [11], [12], [13] and
the scheduling of tasks in human–autonomy collaboration [14],
[15], [16] have been well studied, there has been limited research
on the objective of optimally coordinating multiple humans in
MH-MR team. In the limited literature available, existing works
onworkloadallocationinMH-MRteamsthattakehumanfactors
into account are still in the preliminary stage and have several
drawbacks. Most methods only consider human performance
metrics or task difﬁculty as indicators reﬂecting human decision-
makingabilitywithoutconsideringindividualhumanCWL[17],
[18].
However, CWL, which measures the mental capacity required
to complete tasks [19], serves as a vital factor that inﬂuences
2168-2291 © 2024 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies.
Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 2]**
*(This page contains a figure/chart/image not captured in text)*

24
IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 55, NO. 1, FEBRUARY 2025
Fig. 1.
Conceptual illustration of the DRL-based AWAC for MH-MR teams. More details can be found at Session III or supplementary website.1
the human ability to process environmental information and
make decisions [20], [21], [22], [23]. Therefore, neglecting this
fundamental benchmark makes it difﬁcult to imitate and encode
unstructured human decision-making processes. For example, a
decrease in human performance could result from both cognitive
overload and underload on the task, making it challenging to
determine the optimal task reallocation strategy (e.g., increasing
or decreasing the current workload) without considering CWL.
Moreover, most existing approaches tend to build a model that
encodes the relationship between system attributes, including
contextual information and human factors, and the system per-
formance, to serve as one-step rules for determining the optimal
workload distribution [24], [25]. However, building a valid and
generalizable model is challenging due to the complexity of an
MH-MR team and the individual differences between humans
and task scenarios. In addition, current workload allocation
models are difﬁcult to deploy in realistic MH-MR task scenarios
as they mostly lack monitoring and assessment of contextual
information and human states, and have barely been validated
by real-world experiments.
To address these limitations (details in Section II), we propose
a deep reinforcement learning (DRL)-based affective workload
allocation controller (AWAC) for MH-MR teams, as illustrated
in Fig. 1, in where the affective workload refers to changing
the amount of the workload based on each human operator’s
task performance estimated from subjective and objective CWL
measurements [26], [27]. Thus, the proposed controller can
adaptively reallocate workloads based on the operators’ perfor-
mance during collaborative missions with the MRS. Operator
performance is estimated by self-reporting questionnaire scores
(i.e., subjective measurement) and the results of a deep learning
(DL)-based CWL prediction algorithm using physiological and
behavioral data (i.e., objective measurement). To evaluate our
proposed system, we use a closed-circuit television (CCTV)
monitoring task by an MH-MR team as an example and conduct
extensive real-world team-based user experiments for quantita-
tive measurement and qualitative analysis.
The main contributions of this article are as follows.
1) We design a data-driven human performance model
(HPM) to estimate the human operator’s mission per-
formance from CWL measurements. It can be adapted
to various applications by tuning parameters based on
empirical experiments.
2) We propose a DRL-based AWAC capable of adapting the
distributionofworkloadinresponsetovariationsinhuman
cognitive load and team performance.
3) We design and conduct an extensive real-world user study
in CCTV surveillance scenarios to validate the productiv-
ity and effectiveness of the proposed AWAC.
4) We investigate and furnish insightful analysis of various
workload allocation strategies for MH-MR teams.
The rest of this article is organized as follows. Section II
presents the background and related works. Section III provides
details of the proposed AWAC. Section IV describes the design
of a team-based monitoring task that was conducted to validate
the proposed controller. In Section V, we present the results
of the extensive user experiments and analyze the team perfor-
mance of the proposed affective workload allocation system.
Section VI discusses the ﬁndings of this study in depth. Finally,
Section VII concludes this article.
II. RELATED WORKS
In this section, we introduce the background of an overview
of existing research on workload allocation in MH-MR teams.
Workload allocation in MH-MR teams is a critical issue
for practical human–robot interaction (HRI) applications. It
is essential for mission completion and success, as it facili-
tates a clear division of workloads, increased efﬁciency and
productivity, reduced workload on individual operators, and
improved adaptability to changing circumstances in the work
environment [20]. Assigning tasks to the most-suitable human
operator helps avoid conﬂicts and enhances collaboration and
communication between human and robotic agents [25]. With
1[Online].
Available:
https://sites.google.com/view/affective-workload-
allocation
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 3]**

JO et al.: COGNITIVE LOAD-BASED AFFECTIVE WORKLOAD ALLOCATION FOR MULTIHUMAN MULTIROBOT TEAMS
25
a well-deﬁned workload allocation strategy, the MH-MR team
can work cohesively toward achieving the assigned missions.
Previous research has examined human-in-the-loop systems,
such as team organization, task scheduling [28], and studies on
SA in HRI [29]. Workload allocation strategies based on human
CWL [30] have also been researched to control autonomous
aerial vehicles [31], [32], and task performance and difﬁculty
of human operators have been studied to reallocate workloads
during missions [33]. However, these allocation strategies have
typically prioritized system output while overlooking the needs
of human operators. As a result, the majority of workload
allocation research has been limited to applications in MH-MR
teams in real-world settings.
According to [22], the utilization of human CWL is crucial
in HRI applications for maximizing the entire performance,
including productivity and effectiveness. This is because robotic
or autonomous systems can adjust their workloads and control
parameters (e.g., speed, control method) based on the human
operator’s condition, which can be affected by factors, such as
personal reasons, negative emotions, and unusual environments.
Two primary methods are used to measure human CWL: sub-
jective measurement and objective measurement.
Subjective measurement, such as self-reported ratings or
questionnaires, provides insight into the user’s perceived level of
CWLs related to factors such as motivation and prior experience.
However, it is difﬁcult to measure the operator’s CWL in real
time, and there is a high possibility of bias or fake CWL, which
is intentionally generated by human operators to reduce their
workload.
On the other hand, objective measurement, such as physio-
logical measures, provides a more quantiﬁable assessment of
CWL. They can reveal speciﬁc aspects of the interaction that
are causing increased mental effort, such as complex visual
displays or cognitively demanding tasks. Some studies in the
affective computing and HRI ﬁelds have used physiological
sensors to reﬂect the operator’s CWL or emotional states [34].
Other studies have utilized behavioral data, such as head pose,
eye blinking and gazing, as well as dynamic movement of the
input interfaces, to estimate affective states [35], [36]. However,
systems using objective measurement are vulnerable to malfunc-
tioning physiological sensors or behavioral monitoring devices,
which can result in inaccurate measurements of human CWL
and impair the overall system’s performance.
By incorporating both subjective and objective measure-
ments, the limitations of each method can be mitigated, resulting
in a more comprehensive understanding of the human’s CWL in
HRI applications. This, in turn, enables better-informed design
decisions and an enhanced overall user experience.
Subjective and objective CWL measurements, when used
in conjunction with reinforcement learning (RL), can serve
as a workload allocation controller for MH-MR teams. RL
optimizes workloads based on both measurements, allowing
for real-time allocation of tasks among multiple humans and
robots to achieve desired outcomes. This results in a more
effective and efﬁcient system that balances the needs of both
humans and robots. Furthermore, RL allows for adaptation to
changing conditions, which is crucial in dynamic and uncertain
HRI scenarios. Despite its potential beneﬁts, there is limited
understanding, and fewer studies that have explored the use of
bothmeasurementsandRLapproachesforMH-MRapplications
in real-world settings.
Previous research has predominantly focused on the use of RL
for workload allocation in HRI scenarios [37], [38]. These stud-
ies aimed to balance the workload between humans and robots
in collaborative tasks while considering factors, such as user
satisfaction, task efﬁciency, and cognitive load. Zhang et al. [37],
for instance, proposed an algorithm to optimize task allocation
in complex assembly operations. The algorithm was evaluated
through a virtual assembly of an alternator and showed great
potential in reducing human workload and improving efﬁciency
in human–robot collaboration tasks. Lim et al. [39] presented
a human–machine interface and interaction system to support
adaptive automation in unmanned aircraft systems. This system
uses a network of physiological sensors and machine learning
models to infer the user’s CWL in single human operator and
MRS scenarios, where the human operator is responsible for
coordinating the tasks of multiple UAVs. Ghadirzadeh et al. [38]
developed a data-efﬁcient RL framework for modeling physical
human–robot collaborations that enables the robot to learn how
to collaborate with a human operator. The framework reduces
uncertainty in the interaction using Gaussian processes, and op-
timal action selection is ensured through Bayesian optimization.
However, these approaches have primarily focused on op-
timizing task allocation in single HRI scenarios, which limits
the applicability of workload allocation research to real-world
collaborations involving multiple robots and human operators.
In addition, these approaches have not comprehensively con-
sidered the various conditions of the human operator and have
not taken into account the human operator’s CWL in collabo-
rative missions with multiple robots. Furthermore, the narrow
focus on speciﬁc learning models limits their ability to adapt to
unexpected situations.
III. AFFECTIVE WORKLOAD ALLOCATION CONTROLLER
In this section, we introduce our AWAC for MH-MR teams.
The AWAC aims to enable human operators to collaborate more
effectively with MRSs and teammates by intelligently assigning
appropriate workloads based on both subjective and objective
measurements of the CWL of the operator and their teammates.
For example, if one operator has a high CWL, the proposed
AWAC will assign more work to other operators to balance
the workload. The AWAC is designed to improve the efﬁciency
and effectiveness of MH-MR teams by mitigating the impact of
CWL on task performance. In addition, there is a supplementary
website including more details of the AWAC at.2
A. Problem Formulation
Although having knowledge of contextual information and
human conditions (e.g., CWL) can serve as a decision-making
foundation for the workload allocation problem, it is still a
2[Online].
Available:
https://sites.google.com/view/affective-workload-
allocation
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 4]**

26
IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 55, NO. 1, FEBRUARY 2025
challenging task to determine the ideal workload distribution,
given the complex nature of MH-MR teams. Unlike existing
model-based approaches that rely on a single-step allocation rule
model, we address the workload allocation in MH-MR teams as
a partially observable Markov decision process (POMDP) and
apply DRL to ﬁnd the optimal solution. The partial observability
arises from the limited ability of any affective prediction model
(APM) to accurately and completely predict continuous human
conditions during a task. The proposed POMDP for the affective
workload allocation in MH-MR teams is deﬁned as a tuple
(H, W, S, O, A, T , R, γ), where:
1) H := {h1,..., hn} is a ﬁnite set of n human agents;
2) W := {w1,..., wi} is a ﬁnite set of i tasks, e.g., the number
of robots to be supervised, to be assigned to n human
agents;
3) S := {Ss × So} is the joint human state observed,
including subjective CWL obtained by the self-reporting
questionnaire, Ss := {ss
1 × ...× ss
n}, and objective CWL
assessed by the APM, So := {so
1 × ...× so
n}, of the n
human agents;
4) O := {o1 × ...× oq} is the joint observation of the con-
textual information, e.g., current workload distribution,
performance metrics, and other important system charac-
teristics;
5) A := {a1 × ...× an} is the joint allocation decision by
assigning wi to hn;
6) T := P(s′ | s, a) is the state transition function;
7) R := fR(s × o, s′ × o′) is the reward function, which
gives immediate reward after the transition from s × o
to s′ × o′ by taking action a;
8) γ is the discount factor.
This formulation allows fundamental modeling of environ-
ment dynamics of the affective workload allocation problem
in MH-MR teams, and explicitly deﬁnes various attributes of
the team, such as the human state, including subjective and
objective CWLs, and contextual information, including perfor-
mance metrics, current workload distribution, and other sys-
tem characteristics. The goal of this POMDP is to ﬁnd the
optimal policy π∗: (s × o) →a that obtains maximum sys-
tem performance, i.e., the expected total discounted reward
E[∞
k=0 γkrt+k].Throughthisoptimizationprocess,theAWAC
algorithm learns to adaptively adjust workload distribution for
n human agents based on contextual information and human
conditions, including subjective and objective measurements of
CWLs, to maximize operational performance.
B. Data-Driven HPM
While the introduction of the POMDP and DRL can provide
a better chance to ﬁnd the optimal workload allocation strategy,
it requires a high volume of interaction rounds to reach good
performance. Therefore, a DRL model is typically trained in
a simulation environment to achieve results in a cost-effective
and timely manner. To build a sound simulation environment
for an MH-MR team, the key challenge is to build an HPM. that
can simulate human performance based on the human state and
serve as the transition function of the human state. To address
this challenge, we propose a data-driven HPM that estimates the
human operator’s current mission performance from the subjec-
tive and objective measurements of the CWLs. This HPM can be
easily adapted to various applications by tuning the parameters
of the equations derived from the empirical experiments.
For the generalized HPM, we applied the Yerkes–Dodson
law [40], which is a psychological principle that describes the
relationship between CWLs and mission performance. It states
that performance generally improves with increased CWLs, but
only up to a certain point. Beyond this point, further increases in
CWLs lead to a decline in performance. The law is represented
by an inverted-U shape as illustrated in Fig. S1 on Appendix
E, and can be mathematically described by the Gaussian dis-
tribution as (1), with the optimal level of CWLs for maximum
performance at the peak of the curve. The law helps explain why
too much CWLs can have a negative impact on performance and
why ﬁnding the right level of CWLs is important for optimal per-
formance. The Yerkes–Dodson law has been applied to various
ﬁelds to estimate human’s performance in HRI research [41]. We
also found a similar relationship between the operator’s CWLs
and mission performance in our previous study [42]
P(S) =
A
σ
√
2π e−(S−μ)2/2σ2
(1)
where area A is calculated using the trapezoidal rule: A =
n−1
i=0 (xi+1 −xi)(yi+1 −yi)/2. The maximum and minimum
values of Ss, So, and P are used in the calculation. The values
of σ and μ are determined by the type of mission and the mea-
surement methods used to evaluate human performance, such as
subjective measurement, PSs and objective measurement, PSo.
S is the measured CWL and serves as an input variable to convert
into P.
Then, the integrated human operator’s mission performance
model using PSs and PSo is estimated by
Phn = αpPSo + βpPSs.
(2)
Here, we added two weights (αp = 0.5, βp = 0.5) for the sen-
sitivity of the proposed controller and type of the mission. We
utilized both PSs and PSo, which are calculated by subjective
questionnaires and objective measurements of the CWL, re-
spectively, in order to protect against unexpected malfunctions
of the physiological sensors as the objective measurement and
fake answers of the subjective questionnaires made by human
operators intentionally.
In order to allocate the workloads based on the estimated
operator’s mission performance P, we developed the DRL-
based AWAC to ﬁnd optimal changes for multihuman operators
H, H ∈{h1, . . . , hn}, by comparing the current team mission
performance with the predicted next team mission performance
that reﬂects changes in the two variables of W, which are the
changed workloads of human agents
So
t+1 = So
t + Δw
Ss
t+1 = Ss
t + Δw
(3)
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 5]**

JO et al.: COGNITIVE LOAD-BASED AFFECTIVE WORKLOAD ALLOCATION FOR MULTIHUMAN MULTIROBOT TEAMS
27
Fig. 2.
Learning diagram of the proposed DRL model.
where Δw is the variance of the assigned workloads. The next
performance is estimated using (1) and (2), as
P(St+1) = αpP (So
t+1) + βpP (Ss
t+1) .
(4)
These values are utilized in the AWAC algorithm to assign
the optimal workloads based on each human operator’s perfor-
mance.
C. Proximal Policy Optimization for Workload Allocation
Based on the HPM, we built a DRL model to allocate optimal
workloads for enhancing team performance. To train our DRL
model, we assume that the objective measurement of the CWL
predicted by APM indicates the human operator’s CWL, and
there are no fake answers on the subjective measurement of the
CWL. Fig. 2 depicts the learning diagram used in the proposed
DRL model to ﬁnd optimal transitions of the workloads-based
human operators’ CWLs.
The state space (S) in the DRL model is designed to consider
individual CWLs measured by the self-reporting questionnaire
(Ss
hn) and by the predicted CWL by APM (So
hn), where n is
the number of the human operators and n ∈{1, . . . , n}. So
represents the objective CWL, and Ss represents the subjective
CWL. The action space (A) represents the assigned workloads
based on operators’ performance, A ∈(a1, . . . , an), which are
estimated based on operators’ So and Ss. We designed the team
mission performance-based reward (R) in order for the DRL
model to achieve high team mission performance by comparing
predicted performance after taking the next state (S′) and action
(A′) with the current state and action.
We built an environment to train our DRL model, utilizing the
predeﬁned state space S, action space A, and reward R, through
the use of OpenAI gym (see Algorithm S1 on Appendix C). This
was done in conjunction with our surveillance environment, as
depicted in Fig. 2. Using PPO, we trained the DRL model on the
environment to obtain the optimal policy π [43]. This process
is terminated if P ′
team is less than Pteam, or if the sum of the
assigned A falls outside the range of W. A total of 1000000
samples were used to train the DRL model using three episodes,
covering various workload allocation methods.
To validate the performance of our AWAC model, we com-
pared it with a random workload allocation method. Both mod-
els were provided with equivalent inputs (S) and subjected to
equivalent restrictions as used in the HPM, along with the sum
of workloads. We then measured the performance of each model
based on the inputs, repeated the experiment 10000 times, and
performed repeated measures ANOVA (rmANOVA) tests. Our
results indicate that the proposed model outperforms the random
workload allocation method (p < 0.01).
IV. CASE STUDY IN CCTV SURVEILLANCE SCENARIOS
In this section, we describe how the proposed AWAC can
be applied to real MH-MR CCTV surveillance scenarios and
how the AWAC, with various allocation methods, impacts team
performance through exploratory user experiments. Moreover,
this section explains the details of the CCTV monitoring task,
the design of the user experiment, and the overall system con-
ﬁguration used in the user experiment.
A. Team-Based CCTV Monitoring Task
To validate the proposed AWAC method, we designed a
team-based user experiment that involved the MH-MR CCTV
monitoring task, which required multiple human operators to
monitorandcontrolmultipleagents/robotssimultaneously.Such
surveillance missions are widely required in diverse MH-MR
system task scenarios, including security monitoring [44], air
trafﬁc management [45], and performance checking [46]. The
surveillance scenario is typical in real-world human–agent sys-
tems, in which human operators undertake a simultaneous
CCTV monitoring task while multiple sensors track them.
Based on the surveillance scenario, we built a generalized
surveillance environment and team-based user study that sup-
ported multihuman operators in conducting CCTV monitoring
tasks with MRSs as MH-MR teams, as illustrated in Fig. 3.
Two human subjects work together as a team to conduct a
simulated CCTV monitoring task together in an environment, as
shown in Fig. 3(b). Both human subjects have identical roles and
responsibilities in the team. During the CCTV monitoring task,
the MRS platform moved through the corridor [shown in red in
Fig. 3(a)] at a speed of approximately 300 mm/s and streamed
the room conditions to the participants’ screens to simulate a
CCTV monitoring task, as the participant’s monitor screen in
Fig. 3(b). The CCTV monitoring task is to click on the window
displaying a streaming camera view containing an abnormal
object, as illustrated in the right bottom of Fig. 3(a): abnormal
objects (e.g., skeleton objects) and normal objects. The objects
were randomly placed in separated rooms, as shown in the left
of Fig. 3(a), and differed in color and quantity. In the CCTV
monitoring task, one operator can monitor up to ﬁve cameras.
Thismaximumnumberofcameraviewswasdeterminedthrough
our previous experiment [42].
B. User Study Procedure
As illustrated in Fig. 4, the participants conducted the eight
tasks with random order (from Task A to H). This study was
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

28
IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 55, NO. 1, FEBRUARY 2025
Fig. 3.
Illustration of (a) MRS testbed for conducting surveillance missions
and (b) participants’ workspace and wearable biosensors (red) and behavioral-
monitoring devices (blue) used to collect physiological features and behavioral
data.
Fig. 4.
Experiment protocol used in the team-based user experiment involves
three phases: Baseline, main, and evaluation phases. In the main phase, a set is
repeated three times for the CCTV monitoring task. This procedure is repeated
eight times with different workload allocation methods randomly selected from
Task A to H.
designed as a 2 × 2 × 2 within-subject study. This user ex-
periment was reviewed and approved by the Purdue University
Institutional Review Board (IRB) (#IRB-2021-1813).
For the team-based user experiment, we recruited 32 par-
ticipants who met the health requirements (female: Nine and
male: 23; see more details about participant requirements on
Appendix B) for 16 teams and conducted the experiments to
validate the proposed AWAC, as shown in Fig. S3 on Appendix
E. The participants had an age range of 18–34 (Mean = 23.81,
S.D. = 4.17). Each participant was compensated $15 for their
time and efforts. To increase the subjects’ engagement in the
study, we provided additional compensation based on the overall
team’s scores on the given tasks.
Prior to starting the experiment, we explained the entire
experimental procedure to two participants and asked them to
ﬁll out an informed consent and a demographic questionnaire.
The participants were then instructed to wear two wearable
biosensors. The wearable biosensor data were utilized to predict
the participant’s objective CWL. After completing the survey
and sensor calibration process, we provided instructions for
each of the nine tasks (one training and eight main experiment
tasks). Each task consisted of three sets (total 300 s) and three
break times (total 60 s), as illustrated in Fig. 4. Then, partici-
pants performed a trial CCTV monitoring task using the CCTV
monitoring graphic user interface (GUI) program, as depicted
in Fig. S2 on Appendix E. The objective of the trial session was
to familiarize themselves with the experiment hardware and to
understand the CCTV monitoring tasks used in this experiment.
Then, the participants conducted one of the tasks for 360 s and
repeated it eight times under different experimental conditions.
After completing each task, participants were asked to evaluate
theiremotionalandcognitivestatesusingquestionnaires,suchas
self-assessment manikin (SAM), instantaneous self-assessment
(ISA), and NASA task load index (NASA-TLX) via the GUI
programs.
At the end of the user experiment, participants were in-
terviewed for approximately ﬁve minutes to gain insight into
their overall experience with our MH-MR AWAC system. The
interview began with a lead-off question (e.g., “Did you no-
tice any differences between the eight sessions? If so, what
were they?”) and was followed by several other questions
(e.g., “What are your thoughts on the ISA and ASs dur-
ing the mission?,” and “Which method do you prefer for
conducting this CCTV monitoring task: changing or ﬁxed
workloads?”).
C. Details of Tasks in the User Experiment
In Task A, two participants view a ﬁxed number of camera
views (e.g., three camera views). In Task B, two participants
discuss and decide on the allocation of workload (e.g., the
number of camera views) before starting the main task, known
as a consensus step, and view the ﬁxed number of camera views
based on the outcome of the discussion. In Task C and Task
D, AWAC adjusts the workloads based on the subjective CWL
reported by ISA, called ISA session (IS), with an additional
workload transition method known as approval session (AS)
used to seek consent from the other participant before changing
the workload. Task C has AS, while Task D does not. In Task E
and Task F, AWAC automatically adjusts the number of camera
views based on the objective CWL predicted by APM, called
prediction session (PS). Task E has AS, while Task F does not.
In Task G and Task H, AWAC automatically adjusts the number
of camera views based on both subjective and objective measure-
ments of the CWL (e.g., IS and PS). Task G has AS, while Task H
does not. The tasks are summarized in Table I. A supplementary
video that demonstrates the user study experiment can be found
at3 and/or on Appendix A.
3[Online]. Available: https://youtu.be/qrmAQqfdLZk
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 7]**

JO et al.: COGNITIVE LOAD-BASED AFFECTIVE WORKLOAD ALLOCATION FOR MULTIHUMAN MULTIROBOT TEAMS
29
TABLE I
SUMMARY OF TASKS USED IN THE USER EXPERIMENT
Fig. 5.
Illustration of the HPM calculated using the ISA score and predicted
CWL.
D. Tuning HPM Parameters
Using multimodal dataset for objective CWL assessment
on simultaneous tasks, called MOCAS [42], we analyzed the
results of the subjective and objective measurements of CWL,
obtained from ISA answers and APM prediction results. Then,
we tuned the parameters of (1) based on the empirical results
of the extensive MOCAS dataset. The tuned HPM can estimate
the current CCTV monitoring task performance of the human
operator from the subjective and objective measurements of
CWL. The correlation between performance and subjective and
objective CWL is illustrated in Fig. 5.
Each surveillance mission with MH-MR teams consists of
three sets. To achieve better performance in each episode, we
deﬁned the reward function as r = 0.33 if the next team mis-
sion performance (Pteamt+1) is greater than the current team
performance (Pteamt), and 0 otherwise. The Pteam is the mean
of all human operator’s mission performance, and Pteam′ is the
predicted team mission performance on the next step, calculated
by reﬂecting transitions in the number of camera views. We
assume that as the number of camera views (wi) increases, the
operator’s CWL (hn) and other state variables (So, Ss) will also
increase in the next step. The correlation between the number of
camera views and state variables was found through empirical
results from [27] and [42].
E. Overall System Conﬁguration
We developed a team-based surveillance system involving
two human operators and six multirobot platforms, as shown
in Fig. 6. The hardware conﬁguration used for the operators
in this user experiment is identical and is mainly comprised
of the APM, which serves as the main interface for reading
physiological signals and behavioral features, and measuring
the objective measurement of the CWL. The subjective and
objective measurements of CWL are then utilized as inputs for
AWAC to reallocate workload. In addition to the main interfaces,
additional subinterfaces were used to conduct the team-based
surveillance mission during the user experiment, as outlined in
the following.
1) Affective Measurement Tool: As illustrated in Fig. 6, we
developed the affective measurement tool (AMT) to measure
physiological and behavioral data from wearable biosensors and
behavior-monitoring devices, respectively. We utilize a robot
operating system 2 (ROS2)-based wearable biosensors pack-
age [47] to record human data over wearable biosensors for com-
municating with MRSs supporting ROS2. This package allows
for communication between wearable biosensors and MRSs
supporting ROS2. To provide real-time computing, support for
multiple robots, and reliable streaming data from various nodes,
each node in the biosensor package follows a standardized node
and topic structure.
In the AMT, raw physiological signals from wearable biosen-
sors are collected at a 100 Hz sampling rate, while behavioral
features from the facial view are extracted at a 30 Hz sampling
rate. This allows for efﬁcient and accurate measurement of
affective states. For the physiological signals, we used two
off-the-shelf wearable biosensors, the Empactica E4 and Emotiv
Insight, to collect physiological data, and a webcam (e.g., Intel
RealSense) to record behavioral data. The Emotiv Insight pro-
vides readings of ﬁve-channel EEGs, power spectrum (theta,
alpha, beta, and gamma), performance metrics, and motion
data, while the Empatica E4 provides readings of blood volume
pulse, galvanic skin response, heart rate, interbeat interval, skin
temperature, and motion data. These measurements allow us to
accurately and reliably capture affective states during collabo-
rative tasks with MRSs. For the behavioral data, we extracted
various features from the facial camera views, such as eye-aspect
ratio,facialactionunits,andfacialexpressions.Thesebehavioral
measurements provide insight into operator affective states and
can be used to complement the physiological data collected by
the wearable biosensors.
The data collected from wearable biosensors and behavioral
features from the facial camera views in the AMT are down-
sampled to a sampling rate of 100 Hz. These processed data are
then used as inputs to predict operator affective states in real
time. This process allows the team to effectively collaborate and
perform tasks efﬁciently, despite variations in operator affective
states. By leveraging the high temporal resolution of these
measurements, the AMT and APM can provide a detailed un-
derstanding of operator affective states and support the dynamic
allocation of workloads in real time.
2) Affective Prediction Model: As illustrated in Fig. 6, we
also use APM to predict CWLs from the objective measurement
of physiological and behavioral signals, which can range from
low to medium to high. We adopt the Husformer [48], an end-
to-end multimodal transformer framework for the recognition
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 8]**
*(This page contains a figure/chart/image not captured in text)*

30
IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 55, NO. 1, FEBRUARY 2025
Fig. 6.
System architecture for the MH-MR surveillance task. More details can be found at the supplementary website.4
of multimodal human cognitive load, for building the APM.
To make predictions of objective CWLs of operators, the APM
uses the multimodal biosignals collected through AMT as the
input, and predicts the objective cognitive load levels, i.e., low,
medium, and high, as the outputs at 100 Hz. We refer readers
to [48] for more details of the APM.
3) CCTV Monitoring GUI Program: The CCTV GUI Pro-
gram is the direct interface between the participant and the
MRS for conducting the surveillance task, as shown in Fig.
S2 on Appendix E. The CCTV GUI program displays multiple
windows of the camera views and team scores while performing
the task. The GUI starts with the setup screen to test communi-
cation among the wearable biosensors, behavioral monitoring
devices, and MRSs through ROS2. If there is no issue, the
GUI enters the preparation step, showing a black cross for 5 s,
followed by a 5s countdown timer. Then, the GUI enters the
main experiment step where the participant monitors multiple
camera views simultaneously, called the CCTV monitoring task,
to ﬁnd abnormal objects on the screens. In addition, only the
team scores are displayed on the GUI to reduce peer and time
pressures.
Each task consists of three sets, and each set takes 100 s,
with a break time of about 20 s between each set. The break
4[Online].
Available:
https://sites.google.com/view/affective-workload-
allocation
time is mainly used for reporting participant’s subjective CWL
through the IS for 10 s, and the other 10 s are for AS. However,
participants have break time if the current task does not require
collecting both values (such as Task A and B). After each task,
participants are redirected to three surveys, including SAM, ISA,
and NASA-TLX, where they respond based on their feelings and
thoughts about the entire task. We then repeated eight tasks for
90 min.
4) Object Detection Server: It performs the CCTV monitor-
ing task of detecting abnormal objects on the streaming video
from the multirobots displayed on the GUI program. The object
detection server (ODS) checks whether the human operator
detects abnormal or normal objects and provides audio feedback
to the human operator based on the results of the ODS. If human
operators detect an abnormal object, they are awarded one point
(e.g., reward). However, if they detect a normal object, they lose
three points (e.g., penalty). Based on our pilot test, we decided
on two points: a higher penalty point (–3) than the reward (+1), to
encourage careful consideration by human operators conducting
CCTV monitoring tasks. For detecting abnormal objects, we
used the object detection algorithm, which has an accuracy of
99.96% to detect abnormal objects among two classes (i.e.,
normal and abnormal objects).
5) Mission Score Server (MSS): It manages the rewards
(+1 point) and penalty (–3 points) based on the participant’s
performance in the CCTV monitoring task. The MSS works
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 9]**

JO et al.: COGNITIVE LOAD-BASED AFFECTIVE WORKLOAD ALLOCATION FOR MULTIHUMAN MULTIROBOT TEAMS
31
in conjunction with the ODS and GUI program during task
execution. The ODS updates the MSS by determining if the
human operator has completed the task correctly, while the GUI
program serves as the user’s direct interface and displays the
updated team score as the task is being carried out.
6) Multirobot System: The MRS consists of six ROS2-based
multirobot platforms, known as SMARTmBOT [49]. The MRS
consists of six ROS2-based multirobot platforms, which is an
open-source mobile robot platform. The Vicon motion capture
system tracks the robot’s locations, which uses reﬂective mark-
ers attached to the top of the robots. To perform the surveillance
mission, a pure-pursuit control algorithm was employed, allow-
ing the robot to repetitively travel between the start and goal
position [50].
V. RESULTS AND ANALYSIS
In this section, we present the ﬁndings from our exploratory
research. The user experiment is a team-based user study in-
volving two human operators and MRS. The main objective
of this experiment is to investigate the effect of the proposed
AWAC on team performance and to ﬁnd optimal workload
allocation strategies by comparing with various task allocation
strategies. Therefore, we adjusted a signiﬁcance level of α to
0.10 for statistical analysis, which can provide valuable insights
for future research regarding MH-MR teams. Table S1 and Table
S4 on Appendix F show the normalized team performance (or
obtained mission scores) of all the teams. We normalized the
raw team performance (P) by dividing it by the mean of the
team performance (μ); Pnorm = P/μ, in order to create standards
and transform data taken from different teams into a consistent
format.
A. AWAC Validation and Results
InordertoﬁndtheoptimalcombinationforAWAC(e.g.,ﬁxed,
PS, IS, andAS), wedividedteams intotwogroups: Tasks A, D, F,
H, and Tasks B, C, E, G, based on the presence of the AS. Then,
we performed the rmANOVA test to investigate the effects of
the proposed AWAC without AS on team performance. We then
conducted the post-hoc analysis using a paired parametric t-test
with Bonferroni correction to explore the contrasts among dif-
ferent workload allocation models [51]. The team performance
across Task A, D, F, and H was compared using mean scores and
standard deviations. Fig. 7(a) illustrates the team performance
of Task A, D, F, and H.
The rmANOVA analysis revealed signiﬁcant effects in the
dependent variable among the groups [F(3, 45) = 2.2134,
p = 0.0995, η2
p = 0.0813] with mean scores of 0.9564 for Task
A, 0.9645 for Task D, 1.0483 for Task F, and 1.0303 for Task
H (Table S2 on Appendix F). From the results of the post-hoc
tests, we observed that Task F demonstrated higher performance
than Task A [T(15) = –1.8182, p = 0.0891], although there are
signiﬁcant effects. Furthermore, Task H demonstrated higher
performance than Task D [T(15) = –2.1536, p = 0.0479].
However, no signiﬁcant differences were found between Task
A and D [T(15) = –0.1713, p = 0.8663], Task D and F [T(15)
= –1.6795, p =0.1138], and Task F and H [T(15) = 0.4053,
Fig. 7.
Results of the comparison experiment to validate the AWAC on four
tasks(TaskA,D,F,andH).(a)Distributionofteamperformanceonthefourtasks
used to validate the AWAC performance. (b) Mean team performance obtained
in each set (ﬁrst set, second set, and third set) of the four tasks.
p = 0.6909]. These results underscore task-speciﬁc variations in
team performance, with Task F and H generally demonstrating
better performance compared to Task A and D, although no
signiﬁcant difference emerged between Task F and H.
Based on the rmANOVA result, we conclude that Task F and
H, which utilized the proposed AWAC, produced higher team
performance scores than the baseline task (Task A). The mean
mission score in Task A was 372.25, but the other three tasks
using AWAC were 376.375, 403.875, and 402.125, respectively.
Therefore, we conﬁrmed the proposed AWAC’s effectiveness in
improving team performance by adaptively allocating the oper-
ator’s workload based on their affective state. Given the similar
team performance of Task A and Task D, we can assume that IS
does not signiﬁcantly affect the team performance compared to
PS used in Task F and H.
In order to more deeply investigate the performance of our
AWAC, we analyzed the team performance obtained in each
set of the task; each task in our user experiment has three sets,
as illustrated in Fig. 4. We calculated the team performance
obtained in the ﬁrst, second, and third sets, as illustrated in
Fig. 7(b). We observed that the team performance obtained
in each set of tasks with our AWAC (Task D, F, and H) was
higher than that of Task A without AWAC in the second set of
the missions [F(3, 45) = 2.5976, p = 0.0639, η2
p = 0.0931].
However, the team performance of Task D, F, and H decreased
in the next third set compared to Task A, but there was no
statistically signiﬁcant difference, so we could not say whether
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 10]**

32
IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 55, NO. 1, FEBRUARY 2025
Fig. 8.
Examples of workload allocation transitions generated by AWAC
during user experiments. (a) Operator A’s data. (b) Operator B’s data. Red
indicates ISA scores, blue indicates team performance, green indicates the
allocated camera number, and black indicates predicted CWL.
the team performance increased or decreased compared to the
previous set.
Thus, we can conclude that our AWAC plays a signiﬁcant
role in improving team performance. In addition, we observed
that the team performance of Task D suddenly dropped, which
may imply that the subjective CWL responses were inaccurate,
resulting in our AWAC reallocating the wrong workloads to
each operator. We also noticed that the performance of Task
A increased in the transition from the second set to the third
set, but the team performance remained lower than tasks with
AWAC. This observation suggests that our AWAC can effec-
tively maximize operator performance in a shorter time than
other allocation methods.
The subjective analysis of the effectiveness of the AWAC also
supports the results of the objective analysis. As illustrated in
Fig. S7 on Appendix E, we observed that the valence scores of
the SAM questionnaire in the task with our AWAC are positive.
This means that our AWAC can positively inﬂuence human
operator’s emotional states by inducing positive valence (e.g.,
happy), thereby improving the productivity and effectiveness of
the missions. This is consistent with the Yerke–Dodson law [40]
and other research ﬁndings [52].
Fig. 8 illustrates an example of workload reallocation
recorded during the user experiment while participants were
performing the CCTV monitoring task. The ﬁgure demonstrates
that our AWAC successfully reallocated the workload for each
participant based on their performance estimated from ISA
scores and predicted CWL.
B. Comparison of Workload Allocation Methods
Beyond validating the performance and effectiveness of the
AWAC, we investigated the effects of various workload allo-
cation methods on team performance for MH-MR teams. We
designed three sessions as mentioned in Table I; IS, PS, and
AS. The IS session measured the subjective CWL of human
operators using a ﬁve-point rating scale during the missions.
The PS session predicted the CWL of human operators using
DL-based APM. The AS session asked the human operator to
accept or reject the proposed workload transition. If the human
operator rejected the workload change, the workload would not
be altered.
To investigate the impact of the AWAC on team performance,
we conducted the rmANOVA test with signiﬁcance level of α
to 0.10 by comparing Task B, C, E, and G. We also conducted
post-hoc tests using a paired parametric t-test with Bonferroni
correction. Fig. S6 on Appendix E presents the team perfor-
mance of Task B, C, E, and G. The rmANOVA test showed
signiﬁcant effects: in the dependent variable among the groups
[F(3, 45) = 2.3585, p = 0.0842, η2
p = 0.0861] with Task B
having a mean of 1.0275, Task C with 0.9316, Task E with
1.0046, and Task G with 1.037 (Table S4 on Appendix F).
Based on the results of the team performance analysis, it can
be concluded that Task G, which utilized both IS and PS, can get
higher team performance than other tasks (Task B, C, and E). It
was also observed that the capability-based workload allocation
(Task B) can get more team performance than tasks that only
used IS or only used PS. Therefore, it can be suggested that
workload allocation methods that include AS should consider
both subjective and objective CWL (IS and PS) to optimize team
performance.
In the tasks without AS (Task A, D, F, and H), we performed
the rmANOVA test with signiﬁcance level of α to 0.10 to
comparetheeffectsoftheexperimentalconditionsofthetaskson
the team performance. Fig. 7(a) shows the distribution of team
performance on Task A, D, F, and H. The rmANOVA results
showed there are signiﬁcant effects on team performances based
on the conditions [F(3, 60) = 2.2139, p = 0.0995, η2
p = 0.0813].
The mean of Task A is 0.9564, the mean of Task D is 0.9645,
Task F is 1.048, and Task H is 1.03. Thus, we can conclude
that workload allocation methods without AS should consider
applying the objective operator’s CWL (e.g., PS) to maximize
the team performance.
We performed the rmANOVA test to compare the effects
of the experimental conditions of Task A and B on the team
performance. Fig. S5 on Appendix E shows the distribution
of team performance on both tasks. The rmANOVA revealed
no statistically signiﬁcant difference between the two tasks
[F(1, 30) = 1.5959, p = 0.2258, η2
p = 0.0640] . Therefore,
we can conclude that there is no difference between the task
allocation based on the operator’s capability (Task B) and the
counterbalanced task allocation (Task A).
C. Analysis of Subjective Questionnaires
After completing each task in the user experiment, partici-
pants were asked to rate their emotions and CWL using SAM,
ISA, and NASA-TLX. We conducted rmANOVA tests with a
signiﬁcance level of α to 0.10 on the results of the subjec-
tive questionnaires and found no statistically signiﬁcant differ-
ence between tasks in all questionnaires [F(7, 255) = 1.7411,
p = 0.3474]. However, we observed that Task G with PS and
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 11]**

JO et al.: COGNITIVE LOAD-BASED AFFECTIVE WORKLOAD ALLOCATION FOR MULTIHUMAN MULTIROBOT TEAMS
33
IS (Mean = 0.91, S.D. = 1.99) and Task E with PS (Mean =
0.91, S.D. = 2.07) had positive effects on the participant’s
emotions, especially valence, compared to the other tasks. The
SAM questionnaire’s valence values distribution is illustrated in
Fig. S7 on Appendix E.
D. Analysis of Postinterview
After completing all tasks, we conducted interviews with the
participants to gather feedback on our AWAC system. Most of
the participants preferred changing the workload for the CCTV
monitoring task rather than a ﬁxed workload. Some participants
reported that IS and AS were helpful in conducting missions
(see the extended postinterview analysis in Appendix D).
From the postinterview sessions, we interestingly observed
that some participants felt sorry for getting lower mission scores
compared to their teammates, especially if they were friends. In
order to investigate the effect of the friendship between two
operators on the team performance, we conducted a one-way
ANOVA test to compare the performance of two groups (e.g.,
Group A and Group B) in from Task A, which is our baseline of
the task allocation methods without any other control variables,
such as IS, PS, and AS. Group A consists of Teams 1, 7, 8,
9, and 10, those who know each other. Group B consists of
other teams, those who do not each other. According to the
results of the one-way ANOVA test, there is no signiﬁcant
difference between Group A and B [F(1, 15) = 0.0182, p =
0.8945, η2
p = 0.036; See Fig. S8]. This indicates that there is
no correlation between the friendship of two operators and the
team’s performance. Therefore, we can conclude that friendship
between team members does not affect team performance.
E. Summary of Findings
We validated the performance of the AWAC and found there
is a signiﬁcant difference at α to 0.10 from our exploratory user
experiment. The tasks with AWAC can achieve better team per-
formance scores compared to tasks without AWAC, suggesting
that reallocating the workload based on the operator’s CWL
for the team mission has positive effects on team performance.
Among the four tasks (Task A, D, F, and H), the task with the PS
achieved the best team performance, indicating that predicting
the operator’s CWL may play an important role in workload
allocation for MH-MR teams.
When AS was provided, having both the IS (i.e., subjective
measurement) and the PS (i.e., objective CWL measurement)
achieved the best team performance. In addition, having the PS
performedbetter thanhavingtheIS, suggestingthat theobjective
measurement may be a better option for achieving better team
performance. Furthermore, when the subjective and objective
sessions were not provided, and only AS was given, the perfor-
mance was better than when the subjective and objective mea-
surementswereprovidedseparately.Thissuggeststhatworkload
allocation through consultation among team members can be
more effective than workload allocation through subjective and
objective measurements. However, as mentioned previously, this
consultation-based approach was not better than when all three
sessions (AS, PS, and IS) were provided. In other words, the
best performance in the CCTV monitoring task introduced in
this study can be achieved by allocating the same workload in
the beginning and soon after implementing the proposed AWAC
with all three sessions.
VI. DISCUSSION
We introduced the DRL-based AWAC that enables human
operators to perform better with teammates and MRSs through
team-based user experiments in a CCTV surveillance scenario
involving MH-MR teams. The AWAC intelligently assigns ap-
propriate workloads based on individual and team performance
metrics, which are calculated using a combination of subjective
CWL reported through self-reporting questionnaires and objec-
tive CWL predicted by our DL-based APM. Furthermore, we
compared different workload allocation strategies for MH-MR
teams and found that consulting with team members to allocate
workload is more efﬁcient than relying solely on our AWAC,
which reﬂects both subjective and objective CWLs.
To evaluate the effectiveness of our AWAC, we conducted
an rmANOVA with a signiﬁcance level of α = 0.10 to analyze
the mission scores obtained during the experiments. The results
indicated that our proposed DRL-based AWAC led to better team
performance. However, the signiﬁcant effects were observed
only at α = 0.10 and not at the conventional α = 0.05, as
our study is exploratory, aimed at ﬁnding the optimal AWAC
settings (Task A to Task H) and investigating the effects of the
AWAC on team performance. The relatively small sample size
in our team-based user experiment also contributed to these
results. Although the statistical ﬁndings do not meet the α =
0.05, we observed signiﬁcant effects of using affective states on
team performance. In addition, our post-analysis showed that the
p-value decreased as more teams were included in the analysis
(from Teams 1–4, 1–8, 1–12, to 1–16), suggesting that further
research with a larger sample could yield more signiﬁcant results
(p < 0.05). Fig. S4 on Appendix E illustrates the reduction of
p-value with different numbers of teams.
In addition, generalization errors can occur in the proposed
HPM and the DL-based APM. The HPM estimates human
operators’ mission performance using both self-reported and
predicted CWL via the ISA and our DL prediction model,
respectively. To develop the HPM, we utilized the ISA scores
and predicted CWLs of human subjects from the dataset we
built in a previous study [42]. From the dataset, we observed
that the CWLs differ depending on the number of camera
views while performing the surveillance task, and there are
positive correlations between NASA-TLX and ISA scores (γ >
0.5). Therefore, we assumed that most participants had similar
CWLs depending on the number of camera views. For instance,
when performing our surveillance mission with one camera
view, their CWL is low, and if they use more camera views,
the CWL increases. We applied this knowledge to develop
the HPM.
The DL-based APM was also developed using the same
dataset collected from our previous experiment [42]. However,
due to participants’ facial masks, our facial feature extraction
programs failed to extract some of the facial features (such as eye
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 12]**

34
IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 55, NO. 1, FEBRUARY 2025
aspect ratio and action units) from the subjects. Therefore, we
only used 70% of the MOCAS dataset for training the DL-based
APM.Tocompensateforthesmallsizeofthetrainingdataset,we
applied K-fold cross-validation (K = 5), which is a resampling
technique that generates more data from a limited data sample.
Thus, we assumed that the prediction results could represent
the current human operator’s CWL while performing the CCTV
monitoring task.
To ensure the sensibility of the proposed DRL-based APM,
we added weights (α and β) to (2), which estimates human
performance using both subjective and objective measurements
of the CWL. During our team-based user experiment, we deﬁned
αp and βp as 0.5 each, which were decided based on our pilot
test. However, we may need to adjust these weights depending
on the accuracy of the DL-based prediction algorithm. If the
prediction results of the algorithm are reliable and high accuracy,
wemayneedtoincreasetheweightofβp toallocatetheworkload
appropriately based on the human operator’s performance.
In this research, we focused only on the number of camera
views as one of the primary factors (e.g., robot speed) that can
directly affect an operator’s CWL. Then, we utilized our HPM
to convert the operator’s CWLs into their performance, which
determines the operator’s workload allocation. This decision
was made to focus on validating the effectiveness of monitoring
human affective states on MH-MR team missions and ﬁnding
the optimal workload allocation methods for MH-MR teams.
However, we have identiﬁed another factor through previous
experiments, which is that the robot’s speed can also impact
mission scores. In a previous study [27], we observed that the
mission scores of participants were inﬂuenced by the robot speed
(p < 00.001).
Moreover, the proposed AWAC was only validated through
a user experiment involving two human operators and six mul-
tirobot platforms due to limitations in experiment space and
equipment, raising concerns about its scalability. However, this
issue can be addressed by expanding our DRL framework to
include more human operator actions (A) and states (S) or mul-
tirobot platforms related to the total workloads. It is important to
note that the number of human operators should be less than the
number of robot agents to effectively allocate workloads based
on operators’ performance for the mission.
Based on the results of our experiment, our proposed work-
load allocation method (AWAC) that considers both subjective
and objective CWL measurement (i.e., IS and PS) and incorpo-
rates the operator’s opinion on workload transition (i.e., AS) led
to better team performance compared to traditional workload
allocation methods (Task A). The most common workload allo-
cation method in our society is the capability-based workload al-
location under the agreement, which allocates workloads based
on the operator’s preference, ability, skills, experience, and so
on [53], [54]. However, capability-based workload allocation
methods are difﬁcult to handle sudden changes in the operator’s
capability during the mission, so Mina et al. [25] proposed
utilizing objective CWL measurement methods using physio-
logical sensors (i.e., PS) to overcome this drawback. They found
that CWL measurement-based workload allocation methods
outperformed traditional allocation methods, which was also ob-
served in our study. Speciﬁcally, objective-measurement-based
workload allocation (Task E) outperformed capability-based
workload allocation methods (Task C). Furthermore, we found
that our proposed allocation methods using both IS and PS (Task
G) outperformed traditional workload allocation methods (Task
B and C) and objective CWL measurement-based workload
allocation methods (Task E).
VII. CONCLUSION
We introduced the DRL-based AWAC that enables human
operators to perform better with teammates and MRSs. The
AWAC intelligently assigns appropriate workloads based on
individual and team performance metrics, which are calculated
using a combination of subjective CWL reported through the
ISA method and objective CWL predicted by our DL-based
affective physiological model. We evaluated the effectiveness
of our AWAC and HPM through team-based user experiments
on a CCTV surveillance scenario involving multihuman and
multirobot teams. We used rmANOVA to analyze the mission
scores obtained during the experiments, which showed that our
proposed DRL-based AWAC resulted in better team perfor-
mance. This indicates that workload allocation based on human
operators’ CWL is critical to improving team performance. Fur-
thermore, we compared different workload allocation strategies
for MH-MR teams in the experiment, and found that allocating
workload by consulting with team members is a more efﬁcient
method than relying solely on our AWAC that reﬂects subjective
and objective CWLs.
Our study highlighted the potential of the DRL-based AWAC
in improving team performance in MH-MR team, but future
research should focus on enhancing its robustness and applica-
bility. Future work will involve conducting experiments with a
larger and more diverse participant pool to improve the statistical
power and generalizability of the ﬁndings, which will help
validate the approach at a more signiﬁcance level α to 0.05.
In addition, more detailed comparisons between speciﬁc tasks,
particularly between Task A (ﬁxed workload) and Task G (full
AWAC), should be conducted to provide deeper insights into the
effects of our AWAC over traditional methods. Exploring the
scalability of the AWAC by testing it with larger MH-MR teams
and more complex MH-MR setups is also planned. Finally,
future studies should consider additional factors, such as robot
speed, to further reﬁne workload allocation and enhance overall
team performance. Addressing these areas will help to validate
the effectiveness of the AWAC more robustly and contribute to
the development of more efﬁcient workload allocation strategies
in HRI scenarios.
SUPPLEMENTARY MATERIALS
This PDF ﬁle includes: Appendix A. Supplementary Video
and Website; Appendix B. Participant Requirement; Appendix
C. Algorithm S1; Appendix D. Extended Postinterview Analy-
sis; Appendix E. Figures S1– S8; Appendix F. Tables S1– S4.
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 13]**

JO et al.: COGNITIVE LOAD-BASED AFFECTIVE WORKLOAD ALLOCATION FOR MULTIHUMAN MULTIROBOT TEAMS
35
ACKNOWLEDGMENT
The authors would like to thank the associate editor for
their insightful suggestions and anonymous reviewers for their
critical comments, which have greatly helped to improve the
quality of this article. Any opinions, ﬁndings, and conclusions
or recommendations expressed in this material are those of the
author(s) and do not necessarily reﬂect the views of the National
Science Foundation.
REFERENCES
[1] A. Kolling and S. Carpin, “Multi-robot surveillance: An improved algo-
rithm for the graph-clear problem,” in Proc. 2008 IEEE Int. Conf. Robot.
Automat., IEEE, 2008, pp. 2360–2365.
[2] C. Luo, A. P. Espinosa, D. Pranantha, and A. De Gloria, “Multi-robot
search and rescue team,” in Proc. 2011 IEEE Int. Symp. Safety, Secur.,
Rescue Robot., IEEE, 2011, pp. 296–301.
[3] D. Sun and J. K. Mills, “Adaptive synchronized control for coordination of
multirobot assembly tasks,” IEEE Trans. Robot. Automat., vol. 18, no. 4,
pp. 498–510, Aug. 2002.
[4] G. Hoffman and C. Breazeal, “Collaboration in human–robot teams,” in
Proc. AIAA 1st Intell. Syst. Tech. Conf., 2004, Paper no. 6434.
[5] J. Kolb, H. Ravichandar, and S. Chernova, “Leveraging cognitive states
in human–robot teaming,” in Proc. 1st IEEE Int. Conf. Robot Hum.
Interactive Commun., IEEE, 2022, pp. 792–799.
[6] B. L. Hooey, D. B. Kaber, J. A. Adams, T. W. Fong, and B. F. Gore, “The
underpinnings of workload in unmanned vehicle systems,” IEEE Trans.
Hum.-Mach. Syst., vol. 48, no. 5, pp. 452–467, Oct. 2018.
[7] J. B. Lyons and C. K. Stokes, “Human–human reliance in the context of
automation,” Hum. Factors, vol. 54, no. 1, pp. 112–121, 2012.
[8] A. Dahiya, A. M. Aroyo, K. Dautenhahn, and S. L. Smith, “A survey
of multi-agent human–robot interaction systems,” Robot. Auton. Syst.,
vol. 161, 2022, Art. no. 104335.
[9] M. J. Barnes, J. Y. Chen, and F. Jentsch, “Designing for mixed-initiative
interactions between human and autonomous systems in complex environ-
ments,” in Proc. 2015 IEEE Int. Conf. Syst., Man, Cybern., IEEE, 2015,
pp. 1386–1390.
[10] K. M. Feigh and A. R. Pritchett, “Requirements for effective function
allocation: A critical review,” J. Cogn. Eng. Decis. Mak., vol. 8, no. 1,
pp. 23–32, 2014.
[11] A. Khamis, A. Hussein, and A. Elmogy, “Multi-robot task allocation: A re-
view of the state-of-the-art,” Cooperative Robots Sensor Netw., vol. 2015,
pp. 31–51, 2015.
[12] B. Hardin and M. A. Goodrich, “On using mixed-initiative control: A per-
spective for managing large-scale robotic teams,” in Proc. 4th ACM/IEEE
Int. Conf. Hum. Robot Interact., 2009, pp. 165–172.
[13] C. A. Miller, H. B. Funk, M. Dorneich, and S. D. Whitlow, “A playbook
interface for mixed initiative control of multiple unmanned vehicle teams,”
in Proc. 21st Digit. Avionics Syst. Conf., IEEE, 2002, pp. 7E4–7E4, vol. 2.
[14] N. Creech, N. C. Pacheco, and S. Miles, “Resource allocation in dynamic
multiagent systems,” 2021, arXiv:2102.08317.
[15] R. S. Gutzwiller, D. S. Lange, J. Reeder, R. L. Morris, and O. Rodas,
“Human–computer collaboration in adaptive supervisory control and func-
tion allocation of autonomous system teams,” in Proc. Virtual, Augmented
Mixed Reality: 7th Int. Conf., VAMR 2015, Held Part HCI Int., Los
Angeles, CA, USA, Springer, 2015, pp. 447–456.
[16] G. Tokadli, M. C. Dorneich, and M. Matessa, “Evaluation of playbook del-
egation approach in human-autonomy teaming for single pilot operations,”
Int. J. Hum.–Comput. Interact., vol. 37, no. 7, pp. 703–716, 2021.
[17] M. IJtsma, L. M. Ma, A. R. Pritchett, and K. M. Feigh, “Computational
methodology for the allocation of work and interaction in human–robot
teams,” J. Cogn. Eng. Decis. Mak., vol. 13, no. 4, pp. 221–241, 2019.
[18] Z.TalebpourandA.Martinoli,“Adaptiverisk-basedreplanningforhuman-
aware multi-robot task allocation with local perception,” IEEE Robot.
Automat. Lett., vol. 4, no. 4, pp. 3790–3797, Oct. 2019.
[19] E. Debie et al., “Multimodal fusion for objective assessment of cognitive
workload: A review,” IEEE Trans. Cybern., vol. 51, no. 3, pp. 1542–1555,
Mar. 2021.
[20] C. E. Harriott, G. L. Buford, J. A. Adams, and T. Zhang, “Mental workload
and task performance in peer-based human–robot teams,” J. Hum.-Robot
Interact., vol. 4, no. 2, pp. 61–96, 2015.
[21] F. N. Biondi, A. Cacanindin, C. Douglas, and J. Cort, “Overloaded and
at work: Investigating the effect of cognitive workload on assembly task
performance,” Hum. Factors, vol. 63, no. 5, pp. 813–820, 2021.
[22] R. N. Roy, N. Drougard, T. Gateau, F. Dehais, and C. P. Chanel, “How
can physiological computing beneﬁt human–robot interaction?,” Robotics,
vol. 9, no. 4, 2020, Art. no. 100, doi: 10.3390/robotics9040100
[23] J. Heard, C. E. Harriott, and J. A. Adams, “A survey of workload
assessment algorithms,” IEEE Trans. Hum.-Mach. Syst., vol. 48, no. 5,
pp. 434–451, Oct. 2018.
[24] F. Fusaro, E. Lamon, E. De Momi, and A. Ajoudani, “An integrated
dynamic method for allocating roles and planning tasks for mixed human–
robot teams,” in Proc. 30th IEEE Int. Conf. Robot Hum. Interactive
Commun., IEEE, 2021, pp. 534–539.
[25] T. Mina, S. S. Kannan, W. Jo, and B.-C. Min, “Adaptive workload alloca-
tion for multi-human multi-robot teams for independent and homogeneous
tasks,” IEEE Access, vol. 8, pp. 152697–152712, 2020.
[26] S. Kalyuga, “Cognitive load theory: Implications for affective computing,”
in Proc. 24th Int. FLAIRS Conf., 2011.
[27] W. Jo, G.-E. Cha, D. Foti, and B.-C. Min, “Smart-teleload: A new graphic
user interface to generate affective loads for teleoperation,” SoftwareX,
vol. 26, 2024, Art. no. 101757.
[28] S.-Y.Chien,M.Lewis,S.Mehrotra,N.Brooks,andK.Sycara,“Scheduling
operator attention for multi-robot control,” in Proc. 2012 IEEE/RSJ Int.
Conf. Intell. Robots Syst., IEEE, 2012, pp. 473–479.
[29] J. L. Drury, J. Scholtz, and H. A. Yanco, “Awareness in human–robot
interactions,” in Proc. SMC’03 Conf. 2003 IEEE Int. Conf. Syst., Man
Cybern. Conf. Theme-Syst. Secur. Assurance, IEEE, 2003, pp. 912–918,
vol. 1.
[30] D. B. Kaber, C. M. Perry, N. Segall, C. K. McClernon, and L. J. Prinzel III,
“Situation awareness implications of adaptive automation for information
processing in an air trafﬁc control-related task,” Int. J. Ind. Ergonom.,
vol. 36, no. 5, pp. 447–462, 2006.
[31] L. J. Prinzel, F. G. Freeman, M. W. Scerbo, P. J. Mikulka, and A. T.
Pope,“Aclosed-loopsystemforexaminingpsychophysiologicalmeasures
for adaptive task allocation,” Int. J. Aviation Psychol., vol. 10, no. 4,
pp. 393–410, 2000.
[32] G. F. Wilson and C. A. Russell, “Operator functional state classiﬁcation
using multiple psychophysiological features in an air trafﬁc control task,”
Hum. Factors, vol. 45, no. 3, pp. 381–389, 2003.
[33] R. Parasuraman, M. Barnes, K. Cosenzo, and S. Mulgund, “Adap-
tive automation for human–robot teaming in future command and con-
trol systems,” Int. J. Command Control, vol. 1, no. 2, pp. 43–68,
2007.
[34] A. Rajavenkatanarayanan, H. R. Nambiappan, M. Kyrarini, and F. Make-
don, “Towards a real-time cognitive load assessment system for industrial
human–robot cooperation,” in Proc. 29th IEEE Int. Conf. Robot Hum.
Interactive Commun., 2020, pp. 698–705.
[35] V. Narayanan, B. M. Manoghar, V. S. Dorbala, D. Manocha, and A. Bera,
“ProxEmo: Gait-based emotion learning and multi-view proxemic fusion
for socially-aware robot navigation,” in Proc. 2020 IEEE/RSJ Int. Conf.
Intell. Robots Syst., IEEE, 2020, pp. 8200–8207.
[36] R. R. Sherry and F. E. Ritter, “Dynamic task allocation: Issues for imple-
menting adaptive intelligent automation,” Rep. no. ACS, vol. 2, 2002.
[37] R. Zhang, Q. Lv, J. Li, J. Bao, T. Liu, and S. Liu, “A reinforcement
learning method for human–robot collaboration in assembly tasks,” Robot.
Comput.- Integr. Manuf., vol. 73, 2022, Art. no. 102227.
[38] A. Ghadirzadeh, J. Bütepage, A. Maki, D. Kragic, and M. Björkman, “A
sensorimotor reinforcement learning framework for physical human–robot
interaction,” in Proc. 2016 IEEE/RSJ Int. Conf. Intell. Robots Syst., IEEE,
2016, pp. 2682–2688.
[39] Y. Lim et al., “Adaptive human–robot interactions for multiple un-
manned aerial vehicles,” Robotics, vol. 10, no. 1, p. 12, 2021, doi:
10.3390/robotics10010012.
[40] R. M. Yerkes et al., “The relation of strength of stimulus to rapidity
of habit-formation,” J. Comp. Neurol. Psychol., vol. 18, pp. 459–482,
1908.
[41] Y. T. Sam, “Investigating the relationship between stress, workload, and
performance in teleoperation tasks,” Ph.D. diss., Georgia Inst. Technol.,
2021.
[42] W. Jo, R. Wang, S. Sun, R. K. Senthilkumaran, D. Foti, and B.-C.
Min, “MOCAS: A multimodal dataset for objective cognitive workload
assessment on simultaneous tasks,” IEEE Trans. Affect. Comput., early
access, Jun. 13 2024, doi: 10.1109/TAFFC.2024.3414330.
[43] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov,“Proximal
policy optimization algorithms,” 2017, arXiv:1707.06347.
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 14]**
*(This page contains a figure/chart/image not captured in text)*

36
IEEE TRANSACTIONS ON HUMAN-MACHINE SYSTEMS, VOL. 55, NO. 1, FEBRUARY 2025
[44] R. Wang and B. Fang, “Affective computing and biometrics based HCI
surveillance system,” in Proc. 2008 Int. Symp. Inf. Sci. Eng., IEEE, 2008,
pp. 192–195, vol. 1.
[45] M. Pacaux-Lemoine and S. Debernard, “Common work space for human–
machine cooperation in air trafﬁc control,” Control Eng. Pract., vol. 10,
no. 5, pp. 571–576, 2002.
[46] K. Stowers, J. Oglesby, S. Sonesh, K. Leyva, C. Iwig, and E. Salas, “A
framework to guide the assessment of human–machine systems,” Hum.
Factors, vol. 59, no. 2, pp. 172–188, 2017.
[47] W. Jo, R. Wilson, J. Kim, S. McGuire, and B.-C. Min, “Toward a wearable
biosensor ecosystem on ROS 2 for real-time human–robot interaction
systems,” 2021, arXiv:2006.03784.
[48] R. Wang et al., “Husformer: A multimodal transformer for multimodal
human state recognition,” IEEE Trans. Cogn. Devel. Syst., vol. 16, no. 4,
pp. 1374–1390, Aug. 2024.
[49] W. Jo, J. Kim, R. Wang, J. Pan, R. K. Senthilkumaran, and B.-C. Min,
“SMARTmBOT: A ROS2-based low-cost and open-source mobile robot
platform,” 2022, arXiv:2203.08903.
[50] B. Paden, M. ˇCáp, S. Z. Yong, D. Yershov, and E. Frazzoli, “A survey of
motion planning and control techniques for self-driving urban vehicles,”
IEEE Trans. Intell. Veh., vol. 1, no. 1, pp. 33–55, Mar. 2016.
[51] R. E. Kirk, Experimental Design: Procedures for the Behavioral Sciences.
Grove, CA USA: Brooks/Cole Paciﬁc, 1974.
[52] N. Du et al., “Examining the effects of emotional valence and arousal on
takeover performance in conditionally automated driving,” Transp. Res.
Part C: Emerg. Technol., vol. 112, pp. 78–87, 2020.
[53] N. M. Moacdieh, S. P. Devlin, H. Jundi, and S. L. Riggs, “Effects of
workload and workload transitions on attention allocation in a dual-task
environment: Evidence from eye tracking metrics,” J. Cogn. Eng. Decis.
Mak., vol. 14, no. 2, pp. 132–151, 2020.
[54] D. H. Wigboldus, J. W. Sherman, H. L. Franzese, and A. V. Knippenberg,
“Capacity and comprehension: Spontaneous stereotyping under cognitive
load,” Social Cogn., vol. 22, no. 3, pp. 292–309, 2004.
Wonse Jo received the B.S. in robotics engineering
from Hoseo University, Cheonan, South Korea, in
2013, and the M.S. degree in electronic engineering
from the Kyung-Hee University, Seoul, South Korea,
in 2015. He is currently working toward the Ph.D.
degree in computer and information technology with
Purdue University, West Lafayette, IN, USA.
His research interests include social human–robot
interaction, affective robotics, human multirobot in-
teraction, robot perception, environmental robotics,
and ﬁeld robotics.
Ruiqi Wang (Graduate Student Member, IEEE) re-
ceived the B.E. degree in robotics engineering from
the Beijing University of Chemical Technology, Bei-
jing, China, in 2020. He is currently working to-
ward the Ph.D. degree in computer and informa-
tion technology with the Department of Computer
andInformationTechnology,PurdueUniversity,West
Lafayette, IN, USA.
His research interests include human–robot in-
teraction, affective robotics, and human-in-the-loop
robot learning.
Baijian Yang (Member, IEEE) received the B.S. and
M.S. degrees in automation (EECS) from Tsinghua
University, Beijing, China, in 1995 and 1998, respec-
tively, and the Ph.D. degree in computer science from
Michigan State University, East Lansing, MI, USA,
in 2002.
He is currently a Professor with the Department
of Computer and Information Technology, and an
Associate Dean for research with Purdue Polytech-
nic Institute, Purdue University, West Lafayette, IN,
USA. His research interests include cybersecurity,
data-driven security analytics, and applied machine learning.
Dr. Yang was a Steering Committee Member of IEEE Cybersecurity Initiative
between 2015 and 2017, and was a board Director of ATMAE from 2014 to 2016.
Daniel Foti received the B.A. degree in biomedical
engineering from Harvard University, Cambridge,
MA, USA, in 2006, and the M.A. degree in psychol-
ogy and the Ph.D. degree in clinical psychology from
Stony Brook University, Stony Brook, NY, USA, in
2008 and 2013, respectively.
He completed his predoctoral clinical internship
with McLean Hospital, Belmont, MA, USA. In 2013,
he was an Assistant Professor with the Department
of Psychological Sciences, Purdue University, West
Lafayette, IN, USA. He was promoted to Associate
Professor with tenure in 2018 and Full Professor in 2024. His research interests
include using psychophysiological measures to study cognition, emotion, and
reward, as well as abnormalities in these processes that are associated with
vulnerability to psychiatric illnesses.
Mo Rastgaar (Senior Member, IEEE) received the
B.S. degree from the Sharif University of Technology,
Tehran, Iran, in 1995, the M.S. degree from Tehran
Polytechnic, Tehran, Iran, in 1998, and the Ph.D.
degree from Virginia Polytechnic Institute and State
University, Blacksburg, VA, USA, in 2008, all in
mechanical engineering.
From 2008 to 2010, he was a Postdoctoral Asso-
ciate with the Newman Laboratory for Biomechanics
and Human Rehabilitation, Massachusetts Institute
of Technology, Cambridge, MA, USA. From 2011
to 2018, he was the Assistant Professor and Associate Professor with Michigan
Tech,Houghton,MI,USA.In2019,hejoinedPurdueUniversity,WestLafayette,
IN, USA, where he is currently an Associate Professor with Polytechnic Institute
and the Director of the Human-Interactive Robotics Lab.
Byung-Cheol Min (Senior Member, IEEE) received
the B.S. degree in electronics engineering and the
M.S. degree in electronics and radio engineering
from Kyung Hee University, Yongin, South Korea,
in 2008 and 2010, respectively, and the Ph.D. degree
in computer and information technology from Purdue
University, West Lafayette, IN, USA, in 2014.
He is currently an Associate Professor and the
University Faculty Scholar with the Department of
ComputerandInformationTechnologyandtheDirec-
tor of the SMART Laboratory and the Purdue Applied
AIResearchCenter,PurdueUniversity.Beforethis,hewasaPostdoctoralFellow
with the Robotics Institute, Carnegie Mellon University, Pittsburgh, PA, USA.
His research interests include multirobot systems, human–robot interaction, and
robot learning, with a focus on human–robot teaming.
Dr.MinwastherecipientoftheNSFCAREERAward,in2019;thePurduePPI
Outstanding Faculty in Discovery Award, in 2019; the Purdue CIT Outstanding
Graduate Mentor Award, in 2019; the Purdue Focus Award, in 2020; the Purdue
PPI Interdisciplinary Research Collaboration Award, in 2021; the Purdue Corps
of Engagement Award, in 2022. He was named a Purdue University Faculty
Scholar, in 2021.
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:25:08 UTC from IEEE Xplore.  Restrictions apply. 
