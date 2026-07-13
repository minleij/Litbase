# Supporting human interaction with robust robot swarms

*Source file: Supporting_human_interaction_with_robust_robot_swarms.pdf — 6 pages*


---
**[Page 1]**
*(This page contains a figure/chart/image not captured in text)*

Supporting Human Interaction with Robust Robot 
Swarms 
Sean Kerman and Daniel Brown 
Brigham Young University 
Provo, UT 84602 
Email: sean.kerman@gmail.com. 
daniel. brown @byu.edu 
Abstract-In this paper we propose a bio-inspired model for a 
decentralized swarm of robots, similar to the model proposed by 
Couzin [5], that allows for dynamic task assignment and is robust 
to limited communication from a human. We provide evidence 
that the model has two fundamental attractors: a torus attractor 
and a flock attractor. Through simulation and mathematical 
analysis we investigate the stability of these attractors and show 
that a control input can be used to force the system to change 
from one attractor to the other. Finally, we generalize another of 
Couzin's ideas [4] and present the idea of a stakeholder agent. We 
show how a human operator can use stakeholders to responsively 
influence group behavior while maintaining group structure. 
I. INTRODUCTION 
Recently there have been large efforts to create control 
systems suitable for human control of multi-agent system. 
Often times in such systems it is difficult or impossible for 
the human to communicate with all the agents in the system, 
particularly when communication links are unreliable, or when 
bandwidth and power constraints limit communication to only 
a small subset of agents. One way of approaching these 
difficulties that has become popular in the literature is to apply 
principles found in biological swarm systems to robot systems. 
Despite the limited intelligence and abilities of each indi­
vidual agent, swarms are able to achieve collective intelligence 
greater than the sum of their parts [12]. Some examples are 
flocks of birds [1] and schools of fish [5]. Swarm models have 
been explored by researchers from a wide variety of fields 
including computer science, engineering, physics, and biology. 
Many of these swarm models fall into one of two categories, 
flocking [11], [13], [6], [10] or cycles [8], [7]. 
Flocking is characterized by all agents moving cohesively 
in approximately the same direction. Reynolds' seminal work 
in [11] modeled flocks using three fundamental regions of 
interaction: repulsion, orientation, and attraction. Using these 
three simple rules he was able to simulate realistic-looking 
flocking behavior. In [13] a simple consensus model is pre­
sented, with an associated proof of convergence to a flock in 
[6]. In [10] the authors provide a model using Reynolds' three 
rules of interaction, and provide mathematical guarantees that 
the group will converge to a lattice structure with all agents 
moving in the same direction. 
Cycles are characterized by all agents circling around a 
stationary point. A cycle is often called a torus. One prominent 
Michael A. Goodrich 
Computer Science Department 
Brigham Young University 
Provo, UT 84602 
Email: mike@cs.byu.edu 
model is the cyclic pursuit model [8]. This model is charac­
terized by agents in a ring topology pursuing one another to 
create a balanced cyclic group. 
A few models of particular interest [5], [9] demonstrate both 
flocking and cyclic behaviors. The model proposed by Couzin 
et al. [5] uses three regions of interaction similar to those 
proposed by Reynolds. Couzin showed that by varying the 
sizes of these three regions different group structures emerge 
including a torus structure-a type of cyclic group-and a 
flock. Couzin In [4] he also explored leading a flock with a 
small number of informed agents. This paper extends Couzin's 
work by exploring dynamic switching between group types 
and exploring leading torus and flock group types with an eye 
toward human input. Other work on leading swarms can be 
found in [10], [3]. 
In this paper we describe a decentralized model which is 
similar to Couzin's model [5] except we have smoothed out 
some of the switching nonlinearities and changed the dynamics 
to be more suitable for robot systems. We assume that a human 
can only influence a subset of the agents in the swarm. In 
Section II we present our model. In Section III we discuss the 
torus and flock attractors and through simulation demonstrate 
when the system converges to these attractors. In Section 
IV we consider a simplified model that uses only attraction 
and provide mathematical guarantees for convergence to a 
cyclic group. Finally, in Section V we present the notion 
of a stakeholder and show how a human operator can use 
stakeholders to cause the swarm to switch from one group 
type to another. We also demonstrate how stakeholders can be 
used to cause the swarm to track a time varying reference. 
II. MODEL 
Let i = 1,2, ... , N be a set of homogeneous agents with 
nonholonomic dynamics given by 
Xi= 
s·COS(Bi) 
'Iii = 
s . sin( Bi) 
(1) 
Oi = 
Wi 
where [Xi, YilT E ]R.2 is the ith agent's position, Bi E [-7r, 7r] 
is the angular heading of the agent, s is the constant agent 
speed, and Wi is the angular velocity control input. 
For simplicity we define: 
978-1-4673-0163-3112/$31.00 ©2012 IEEE 
197 
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:35 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 2]**
*(This page contains a figure/chart/image not captured in text)*

Vi = 
[COS(Bi), sin(Bi)V 
Ci = 
[x, y]T. 
(2) 
Let A( t) 
= aij (t) denote the sensory adjacency matrix 
where aij(t) 
= 1 means that agent j is visible to agent i 
at time t. Each aij(t) is determined at time t according to a 
Bernoulli random variable with parameter 
if dij(t) N 1 
otherwise 
where dij(t) is the Euclidean distance between agents i and 
j at time t. This method of choosing neighbors is similar to 
the random neighbor model used in [2] which replicated field 
observations of starlings [1]. This is relevant for robot systems 
because occlusions make visibility less likely with growing 
distance for visual sensors and interference makes sensing less 
likely with growing distance for radio or wifi-based sensors. 
Agents react to neighbors within three different zones: 
repulsion, orientation, and attraction. The neighbors in these 
zones are determined by 
ni = {j: Ilci -cjll::; Rr, aij = I} 
ni = {j: llei -cjll::; Ro, aij = I} 
(3) 
n't = {j : aij = I} 
where ni , ni , and n't are the sets of agent i's neighbors in the 
regions of repulsion, orientation, and attraction, respectively. 
The parameters Rr and Ro are the associated radii of repulsion 
and orientation. Note that this model allows for overlapping 
regions of repulsion, orientation, and attraction. This elimi­
nates the hard switch between the repulsion, orientation, and 
attraction forces seen in [5] that may be sensitive to sensor 
transients in real robots. 
The control input Wi is determined by first computing the 
repulsion, orientation, and attraction vectors 
U': 
• 
(4) 
(5) 
Wi = kex 
ex = atan2(ui) - Bi 
(8) 
(9) 
where k is a scalar gain and ex is the heading error. U s­
ing modulo 27r arithmetic we limit ex 
E [-7r, 7r]. Since 
max latan2( Ui) I = 7r, Wi is bounded by k7r. 
III. ATTRACTORS 
In order to define the two different attractors of the model 
we use two metrics of group behavior described in [5], namely 
group angular momentum, mgroup, and group polarization, 
Pgroup. Group angular momentum is a measure of the degree 
of rotation of the group about the group centroid and is 
calculated as 
The vector ric(t) is a unit vector pointing from the group 
centroid to the position of agent i and is given by 
(11) 
(12) 
where cg(t) is the group centroid. The term det[ric(t)lvi(t)] 
is the determinant of the 2 x 2 matrix with columns ric(t) and 
Vi(t) and is a two-dimensional analogue of the cross product. 
The mgroup of a swarm reaches a maximum value of 1 if all 
the agents are rotating around the group centroid in the same 
direction. 
Group polarization measures the degree of alignment among 
individuals within the group and is calculated as 
(13) 
U'! 
• 
Ilvi + 2::nr Vj II 
2::nf (Cj - Ci) 
II2::nf(Cj -ci)II' 
The Pgroup of a swarm reaches a maximum value of 1 when 
(6) 
all the agents have the same heading. 
Next, the desired heading vector Ui is computed as 
(7) 
Note that, because of the normalization in (5) and (6), ori­
entation and attraction forces are always equally weighted 
in the model. This keeps one of the two fundamental forces 
from overpowering the other. It also allows the exponentially 
growing repulsion vector to overpower the orientation and 
attraction forces as agents move closer together, which aids 
in collision avoidance. 
Finally, angular velocity, Wi, is computed as 
A. Torus Attractor 
This model can produce a torus formation as shown in 
Figure l(a). A torus is characterized by Pgroup close to zero, 
mgroup close to one, and a relatively stationary group centroid. 
One potential application of a torus is perimeter monitoring. 
B. Flock Attractor 
The other attractor that the model exhibits is a flock; see 
Figure 1 (b). A flock is characterized by Pgroup close to one 
and mgroup close to zero. Flock groups are useful for moving 
the swarm quickly from one location to another. 
198 
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:35 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 3]**
*(This page contains a figure/chart/image not captured in text)*

(a) Torus 
(b) Flock 
Fig. 1. 
100 agents in (a) torus formation; (b) flock formation. The agents' 
directions of travel are represented by straight lines emanating from the center 
of each agent. 
I, 
1\ 
" 
, 
, 
0.8 
' 
, 
0.6 
0.4 
0.
2 
1 
, 
, 
, 
, 
, 
\ 
\ 
, 
\ 
- Probabilty of Flock 
- - - Probability of Torus 
\ , 
, 
, 
, 
°0f--g
S----1h0----ilSjk-20----l
2S----m30 
Radius of Orientation 
Fig. 2. 
Average group moment and polarization as a function of radius of 
orientation. 
C. Group Expressiveness and Parameter Selection 
We desire to be able to switch between the torus and 
flock attractors without globally broadcasting parameters to 
the agents. To determine parameter values that allow both 
group types to emerge we ran a series of simulations using 
N = 100, k = .5, Rr = 1 and varied the the radius of 
orientation. Simulations were run for 200 seconds with a step 
size of t:l.t = 0.1. The radius of orientation was varied from 0 
to 30 in 1 unit increments. One hundred simulations were 
performed for each value of Ro. For each iteration agents 
were given random initial positions uniformly distributed over 
a lOx 10 square centered at the origin. Agents were also 
given random initial headings. The percentage of trials that 
converged to the torus attractor and the flock attractor were 
calculated for each value of Ro and are shown in Figure 2. 
As can be seen in the figure, the value Ro = 8 had an equal 
probability of converging to either attractor. Figures l(a) and 
l(b) show a torus and a flock formed with the parameter values 
listed above and Ro = 8. 
IV. ANALYSIS OF ATTRACTION DYNAMICS 
The previous section provided empirical evidence that both 
torus and flock behaviors can emerge using the system. In this 
section, we provide an example argument that these behaviors 
are formal attractors of the dynamic system. These attractors 
have associated regions of stability and are the foundation 
for claims of robustness of swarm behavior. To do this we 
Fig. 3. 
Coordinates for an agent (blue) attracted toward the centroid (red). 
consider a system based only on attraction (Ui = u'f) and 
prove convergence to a stable cycle. We assume a complete 
agent topology (aij = 1 \f i =f. j). Using this assumption the 
desired heading of agent i is 
1 
N 
Ui = N `)Cj - Ci) 
(14) 
#i 
which reduces to cg - Ci, where cg is the group centroid. 
Therefore, Ui points toward the centroid. 
A. Change of Variables 
We assume a stationary group centroid at the origin and, 
using a method similar to [8], we perform a change of variables 
r= Jx2+y2 
(15) 
a = 'l/Ji + 7r - e 
(16) 
where r is the distance from the group centroid and 'I/J = 
arctan (). Figure 3 shows how these variables relate to each 
agent. 
Computing equations for r and it we find that 
-s cos a 
1 -ssina - w 
r 
(17) 
(18) 
which describe an agent's dynamics in terms of its distance 
from the centroid r and the desired angle of orientation a. 
B. Stability of Equilibrium Points 
Solving for the equilibrium points of (17) and (18) we get 
2s 
 = ±L 
r = k7r' 
L< 
2 
(19) 
where we have restricted a to be in the interval [-7r, 7r] . These 
two equilibria define a clockwise and counterclockwise orbit 
about the fixed centroid with radius r = 2s/k7r. 
199 
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:35 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 4]**
*(This page contains a figure/chart/image not captured in text)*

Fig. 4. 
A cyclic group formed by an attraction only swarm. The group 
centroid is marked by an 'x'. 
We now investigate the stability of the equilibria by lin­
earizing equations (17) and (18) about the equilibrium points. 
Evaluating the Jacobian at r = 28/ k7r and a = 7r /2 and letting 
w = ka we have 
[ 
0 
s . 
-- SIn a 
r2 
8sina ] 1 
[
0 
!!cosa-k 
= _k2-rr2 
r 
(2s/k-rr,-rr/2) 
4s 
which has eigenValues with negative real parts. Therefore the 
equilibrium point is locally asymptotically stable. Linearizing 
about the other equilibrium point 
28 
r = k7r' 
gives a similar result. 
7r 
a= --2 
(21) 
This indicates that for a stationary group centroid all agents 
converge to either a clockwise or counterclockwise orbit about 
the group centroid with a fixed radius r = 28/k7r. 
To verify these results we simulated the simplified dynamics 
with k = 0.5, 8 = 5. The resulting formation is shown in 
Figure 4 and had a radius of approximately 20/7r as expected. 
This simulation suggests that the assumption of a stationary 
group centroid was well founded. 
V. LEADERSHIP 
A. Stakeholders 
To allow a human to influence a swarm's behavior we 
introduce a type of agent called a stakeholder. In [4], Couzin 
showed how a limited number of stakeholders can be used 
to influence the behavior of a flock. In this section we show 
that not only can stakeholders allow a human to control the 
direction of a flock, but that stakeholders can also be used to 
control a torus and dynamically switch between attractors. A 
stakeholder is an agent that is influenced by the group and also 
influenced by its interaction with a human operator. We assume 
that the human operator can broadcast a desired location to 
M M N stakeholder agents. By broadcasting a reference input 
to a limited number of agents a human may influence the 
movement of the swarm and even cause the group to switch 
attractors. 
A stakeholder has dynamics given by (1) and control input 
(8). The difference is that Ui is modified to allow a human 
operator to influence the stakeholder's behavior. This influence 
is added into the stakeholder attraction dynamics through a 
weighted sum as follows: 
sa 
pqi + (1 -p)u,!: 
U· = e-=--
-:----
-'--;-
-'--:-:-
, 
I lpqi + (1 -p)u'!:II ' 
(22) 
(23) 
where q E ]R.2 is the reference, p E [0, 1] is the priority of the 
reference input, and u'!: is given by Equation (6). Orientation 
and repulsion are given by equations (5) and (4) with 
(24) 
This allows human input to the system without eliminating 
inter-agent dynamics. 
B. Controlled Switch 
As mentioned above, one potential application of the torus 
group is perimeter monitoring and one potential application 
of the flock is to move the swarm quickly from one location 
to another. It is therefore desirable to be able to dynamically 
switch between attractors so that the human may have access 
to both capabilities. We investigated how M and p affect the 
potential for a human to cause the swarm to switch from one 
attractor to another. Simulations were run varying M over the 
interval 10 to 100 in 10 unit increments and p over the interval 
0.1 to 1 in 0.1 unit increments. Ten 200 second trials were 
performed for each parameter pair. Other parameters were 
N = 100, k = .5, Rr = 1, Ro = 8. 
To investigate switching from a torus to a flock we first 
initialized the group into a torus formation and then gave M 
stakeholders a distant fixed reference input to move toward. 
The final group polarization for each trial was recorded to 
determine if the group had successfully switched from a torus 
to a flock. The results of these simulations are shown in Figure 
5 where the probability of the group successfully switching 
from a torus to a flock by the end of any given 200 second 
trial is plotted as a function of M and p. When the torus did not 
switch to a flock, it either moved in formation in the general 
direction of the reference input or the group fragmented. 
To investigate switching from a flock to a torus we first 
initialized the group into a flock formation and then gave M 
stakeholders a fixed reference input at the origin. The final 
group moment for each trial was recorded to determine if the 
swarm had successfully switched from a flock to a torus. The 
results of these simulations are shown in Figure 6 where the 
probability of the group successfully switching from a flock to 
a torus is plotted as a function of M and p. When the flock did 
not switch to a torus, it either flew in a large clover like pattern 
centered at the reference point or the group fragmented. 
Examining Figures 5 and 6 we see that it is easier to switch 
from a torus to flock than vice versa. We also see from Figure 6 
that it is not necessarily desirable to set p = 1 because the lack 
of agent interaction induced by the coercive leadership strategy 
made it difficult for the agents to form a torus. However, if 
p < 0.4 then there was almost zero probability of transitioning 
200 
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:35 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 5]**
*(This page contains a figure/chart/image not captured in text)*

p 
Fig. 5. 
Probability of swarm switching from torus to flock when under 
human control for various values of M and p. 
0.5 
0 
100 
o 
0 
p 
Fig. 6. 
Probability of swarm switching from flock to torus when under 
human control for various values of M and p. 
from one attractor to the other. This provides evidence that the 
attractors are resilient in the presence of perturbations. We also 
notice that a human only needs to control 30 percent of the 
agents in the swarm to transition from a torus to a flock and 40 
percent to transition from a flock to a torus. This indicates that 
the control strategy is robust in the presence of communication 
dropouts. 
C. Path Following 
In the previous section we discussed switching from one 
attractor to the other. However, for many applications it is 
desirable to lead the swarm while keeping the group structure 
intact. We ran a series of simulations to determine whether 
or not these group types could be effectively moved without 
breaking formation. To do so we choose M = 50 and p = 0.8 
to ensure sufficient influence on the group without commu­
nicating with all the agents. We again use agent parameters 
N = 100, k 
= .5, Rr = 1, Ro = 8, but this time we introduce 
a time varying reference input with velocity 
q = Sq ' [1,Of 
(25) 
where Sq is the speed of the reference input. 
0.8 
! 
 0.6 
V 
e 
= 
.90.4 
 
0.2 
0.2 
0.4 
0.6 
Reference Velocity 
0.8 
Fig. 7. 
Average minimum group moment as a function of reference velocity 
when leading a torus. 
14 
12 
... 
<:> !: 10 
r.l 
:l 
= 8 
K 
&> 
-< 6 
l\, 
.. 
... 
" 4 
< 
0.2 
0.4 
0.6 
Reference Velocity 
0.8 
Fig. 8. Average distance from group centroid to reference input as a function 
of reference velocity when leading a torus. 
1) Torus Path Following : For torus formations Sq was 
varied from 0 to 1 in 0.1 unit intervals. Ten trials were 
performed for each parameter set. The lowest group moment 
achieved during each trial was recorded. If the minimum group 
moment was low it indicates that the torus did not successfully 
maintain formation during the trial. The average absolute 
distance from the group centroid to the reference input was 
also recorded. The average minimum group moment over the 
ten trials is plotted in Figure 7. From the figure we see that the 
torus formation was consistently maintained for Sq M 0.6. The 
average absolute distance from the group centroid over the 10 
trials is plotted in Figure 8. We see that error increases linearly 
with the speed. The decrease in error for a reference velocity 
greater than 0.7 is due to the torus briefly switching to a flock 
to catch up with the reference. Further investigation revealed 
that most of the error was due to a constant steady state error 
where the torus lagged consistently behind the reference input. 
These results indicate that torus groups are difficult to lead 
but are still responsive to human input for very low reference 
speeds. 
2) Flock Path Following : For flock formations Sq was 
varied from 4 to 5 in 0.1 unit intervals. Ten trials were 
201 
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:35 UTC from IEEE Xplore.  Restrictions apply. 

---
**[Page 6]**
*(This page contains a figure/chart/image not captured in text)*

0.8 
= 
J 
" ·S 0.6 
Q 
d B  0.4 
:9 
,. 
0.2 
4.2 
4.4 
4.6 
Reference Velocity 
4.8 
s 
Fig. 9. 
Average minimum group moment as a function of reference velocity 
when leading a flock. 
30 
s 
°4P
----4Q.2------4.R4-----4S.6----TU----JS 
Reference Velocity 
Fig. 10. Average distance from group centroid to reference input as a function 
of reference velocity when leading a flock. 
performed for each parameter set. The lowest group polariza­
tion achieved during each trial was recorded. If the minimum 
group polarization was low it indicates that the flock did not 
successfully maintain formation during the trial. The average 
minimum group polarization is plotted in Figure 9. From 
the figure we see that the flock formation was consistently 
maintained for Sq N 4.6. We investigated the lower values of 
Sq and found that the group briefly circled back to allow the 
reference input to catch up to the swarm. The average absolute 
distance from the group centroid over the 10 trials is plotted 
in Figure 10. We see that error is minimized when Sq 
= 4.8. 
These results suggest that flocks are responsive to human input 
and maintain their group structure for reference speeds near 
the agent speed. 
VI. SUMMARY 
In this paper we demonstrated a model with single integrator 
rotational dynamics. We demonstrated that this model has both 
a flock and torus attractor. We identified parameter values 
that allow the swarm to converge to either attractor with 
equal probability when starting from random initial conditions. 
Through a linear stability analysis we showed that for an 
attraction-only model the swarm converges to a cycle around a 
stationary centroid. We further showed that by using a limited 
number of stakeholders the swarm could be dynamically 
switched from one attractor to the other. We also identified 
control parameters that allowed stakeholders to lead both 
flock and torus group types while maintaining group structure. 
This satisfies the requirement of robust HSI systems, namely 
that a human can lead and switch between attractors of the 
system while only communicating with a subset of the agents. 
Future areas of research include more thorough mathematical 
guarantees on convergence to attractors, stability criteria, more 
advanced control strategies, exploration of model behavior 
for a wider range of parameter values, including the lowest 
number of agents for which the results in this paper hold, and 
implementation with real robot platforms. 
ACKNOWLEDGMENTS 
This work was partially supported by the ONR Science of 
Autonomy Program and by ARL's Robotics eTA Program. 
We appreciate the help of Dr. Jeff Humpherys from BYU's 
Mathematics department. 
REFERENCES 
[1] M. Ballerini, N. Cabibbo, R. Candelier, A. Cavagna, E. Cisbani, I. Giar­
dina, V. Lecomte, A. Orlandi, G. Parisi, A. Procaccini, et al. Interaction 
ruling animal collective behavior depends on topological rather than 
metric distance: Evidence from a field study. Proceedings of the National 
Academy of Sciences, 105(4):1232-1237,2008. 
[2] N.W.F. Bode, D.W. Franks, and A.1. Wood. Limited interactions in 
flocks: relating model simulations to empirical data. 
Journal of The 
Royal Society Interface, 8(55):301-304,2010. 
[3] L. Conradt, J. Krause, ID Couzin, and TJ Roper. " leading according to 
need" in self-organizing groups. The American Naturalist, 173(3):304-
312,2009. 
[4] 1.0. Couzin, J. Krause, N.R. Franks, and S.A. Levin. Effective lead­
ership and decision-making in animal groups on the move. 
Nature, 
433(7025):513-516, 2005. 
[5] 1.0. Couzin, J. Krause, R. James, G.D. Ruxton, and N.R. Franks. 
Collective memory and spatial sorting in animal groups. 
Journal of 
Theoretical Biology, 218(1):1-11, 2002. 
[6] A. Jadbabaie, J. Lin, and A.S. Morse. Coordination of groups of mobile 
autonomous agents using nearest neighbor rules. 
Automatic Control, 
IEEE Transactions on, 48(6):988-1001, 2003. 
[7] H. Levine, w.J. Rappel, and I. Cohen. Self-organization in systems of 
self-propelled particles. Physical Review E, 63(1):017101, 2000. 
[8] J.A. Marshall, M.E. Broucke, and B.A. Francis. 
Formations of ve­
hicles in cyclic pursuit. 
Automatic Control, IEEE Transactions on, 
49(11):1963-1974,2004. 
[9] L. Mier-y Teran-Romero, E. Forgoston, and I.B. Schwartz. 
Noise, 
bifurcations, and modeling of interacting particle systems. In Intelligent 
Robots and Systems (IROS), 20n IEEElRSJ International Conference 
on, pages 3905-3910. IEEE, 2011. 
[10] R. Olfati-Saber. Flocking for multi-agent dynamic systems: Algorithms 
and theory. Automatic Control, IEEE Transactions on, 51(3):401-420, 
2006. 
[11] C.W. Reynolds. Flocks, herds and schools: A distributed behavioral 
model. 
In ACM SIGGRAPH Computer Graphics, volume 21, pages 
25-34. ACM, 1987. 
[12] DJT Sumpter. The principles of collective animal behaviour. Philo­
sophical Transactions of the Royal Society B: Biological Sciences, 
361(1465):5-22, 2006. 
[13] T. Vicsek, A. Czir6k, E. Ben-Jacob, I. Cohen, and O. Shochet. Novel 
type of phase transition in a system of self-driven particles. Physical 
Review Letters, 75(6):1226-1229, 1995. 
202 
Authorized licensed use limited to: Linkoping University Library. Downloaded on July 10,2026 at 12:22:35 UTC from IEEE Xplore.  Restrictions apply. 
