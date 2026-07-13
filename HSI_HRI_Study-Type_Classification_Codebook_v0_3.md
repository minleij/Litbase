# HSI/HRI Study-Type Classification Codebook

*Living codebook for classifying the study/contribution type of articles in the human-swarm / human-robot interaction (HSI/HRI) literature review. This is the first analytic step applied to each article, ahead of the task-environment and team-structure dimensions in the companion Classification_Codebook.*

*Version 0.3  ·  Created 2026-07-10  ·  Last updated 2026-07-10  ·  Companion document to Classification_Codebook (task-environment/team dimensions) and Extracted_info.docx*

# 1. Purpose and Scope

This codebook defines a single dimension — Primary Study/Contribution Type — used to classify what kind of article is being reviewed before any other coding is attempted. It is the first step in the literature-review skill's workflow: given an article (typically converted to Markdown), the skill first determines what type of study or contribution the article represents, then (in later steps, governed by the companion Classification_Codebook) codes the task environment, team structure, and other HSI/HRI dimensions.

Separating study type out as its own first-pass codebook matters because swarm-robotics and HSI corpora mix fundamentally different kinds of contributions — pure algorithm papers with no human in the loop, human-subjects experiments, literature syntheses, conceptual frameworks, and system/demo papers — and many of the deeper HSI dimensions (e.g., team structure, human involvement level, coordination architecture) either do not apply, or apply differently, depending on which of these an article is. Knowing the study type up front also lets the corpus be filtered and summarized at a coarse level (e.g., "how many of the reviewed articles are user studies vs. simulation-only algorithm papers") before deeper coding begins.

This codebook is designed to be applied by a large language model (an instance of Claude, or a comparable model). It is a living document and is expected to evolve as it is applied to more articles, following the same amendment process as the companion Classification_Codebook (see Section 5).

# 2. How a Classifying Model Should Use This Codebook

- Unit of analysis: apply this codebook once per article, to determine its Primary Study/Contribution Type — i.e., the type that best characterizes the article's main claimed contribution, not every method incidentally mentioned in it.

- Evidence requirement: base the code on the article's stated contribution and methodology (typically visible in the abstract, introduction "contributions" list, and methods section), not on its title, keywords, or venue alone.

- Primary code is normally singular: unlike the dimensions in the companion Classification_Codebook, this dimension is designed so that one code should fit as the primary characterization of almost every article. Do not spread effort thin by tagging an article with many codes by default.

- Research-aim priority rule for User Study (added v0.2): because live human-subjects data is the most relevant contribution type for this project's research aim, assign User Study (3.1) whenever an article contains ANY user-study component, however small, informal, or lightly reported — a handful of informal observations, brief pilot/think-aloud feedback, a small number of personnel commenting on cognitive load, and so on all count, not just formally powered, statistically reported experiments. Where an article's main claimed contribution is something else (a system, an architecture, a framework) but it also reports real people interacting with or reacting to the system in any way, assign User Study as at least a Secondary code; if it is genuinely unclear which contribution the article foregrounds, default to Primary = User Study rather than the other code. This rule overrides the ordinary "primary contribution" framing elsewhere in this document specifically for User Study — it does not loosen any other code's definition.

- Secondary code when genuinely mixed: some articles legitimately combine two contribution types at comparable weight (e.g., a system/architecture paper whose second half reports a small formal user study; a framework/taxonomy paper that also runs a validating survey of experts). In that case, assign a Primary code (the article's main claimed contribution) and one Secondary code, and note in one sentence which part of the article each applies to. Do not assign a secondary code just because a method is mentioned in passing (e.g., an algorithm paper that cites a related survey in its introduction is not also a Meta-review/Survey).

- User Study sub-attributes: if (and only if) the Primary or Secondary code is User Study (Section 3.1), also assign its three sub-attributes — Setting (3.1.1), Measured Construct(s) (3.1.2), and Study Modality Flags (3.1.3) — using the same evidence standard. These do not apply to any other code.

- Not Applicable does not apply to this dimension: every reviewed article has some primary contribution type, so this dimension itself is never "Not Applicable." If the article's methodology section is too thin to tell which code fits, code "Not Described" and note what specific information (e.g., sample size, whether a task was performed) would resolve it.

- Unclear / Candidate New Code: if an article's contribution genuinely does not fit any code below (rather than fitting awkwardly at the seam between two codes, which the "Distinguish from" notes are meant to resolve), assign "Unclear / Candidate New Code" and describe the contribution in a short note, together with a proposed name and draft definition if one comes to mind. Do not silently stretch a code's definition to force a fit, and do not add a new code to this document on your own authority — propose it and wait for the user's decision, exactly as specified in the companion Classification_Codebook.

- Output format: report results as Primary code (-> Secondary code, if any) -> sub-attributes if User Study -> one- to two-sentence justification with a paraphrased (not quoted) textual basis -> page/section reference if available. Do not reproduce more than a short (<15 word) verbatim phrase from the source article when justifying a code.

- Definitions are authoritative: the definitions below take precedence over the model's own prior associations with terms like "survey," "framework," or "demonstration" from outside this project.

# 3. Dimension: Primary Study/Contribution Type

This dimension classifies the kind of study or contribution an article represents. The eleven codes below are intended to be mutually exclusive as primary characterizations (see the Decision Procedure, Section 3.12, and each code's "Distinguish from" notes for how to resolve seam cases), while allowing a single Secondary code per Section 2 when an article genuinely combines two at comparable weight.

## 3.1 Code: User Study

| **Definition** | A study in which human participants directly interact with, operate, or react to a robot/swarm system, or an interface representing one, while any data — formal or informal — is collected on their behavior, performance, or subjective state, in order to draw conclusions about human-swarm/human-robot interaction. As of v0.2, this includes informal or lightly reported evaluations, not only fully controlled, statistically reported experiments (see the Research-aim priority rule in Section 2). |
| --- | --- |
| **Key indicators** | Real people are described as performing, operating, or reacting to a task or system — this can range from a large, formally powered, statistically reported experiment down to a handful of personnel giving informal observations or think-aloud comments while using the system. Some form of data about that interaction is reported, however minimal: a stated N, quoted or paraphrased participant feedback, observed behavior, or any performance/workload/trust/SA-type measure. Distinct from an article that describes only what the system/hardware did, with no human reaction, behavior, or feedback reported at all (see Non-examples). |
| **Example** | Wattearachchi et al. (2025): 31 participants guided a 20-robot swarm to a target under three hazard conditions, with performance and subjective measures collected. At the informal end, Williams et al. (2023): ~15 military personnel and researchers gave qualitative feedback and cognitive-load observations during swarm stress tests — this now also counts as User Study per the v0.2 research-aim priority rule, even without a formal N or statistics. |
| **Distinguish from Expert Elicitation (3.2)** | A User Study has participants performing, operating, or reacting to the system itself, even informally; Expert Elicitation collects opinions, requirements, or reports from people who are not shown reacting to or operating the system in question (e.g., a requirements interview conducted independently of any task or demo). |
| **Distinguish from Simulation Benchmarking Study (3.5)** | A User Study requires a live human whose behavior/response is reported in some way, however informally; Simulation Benchmarking substitutes a human-performance model (or no human at all) for the real participant. |
| **Distinguish from Physical Robot Demonstration (3.4) and System/Architecture Paper (3.9)** | As of v0.2, if an article reports ANY real-person reaction to, feedback on, or observed behavior with the system — even a few informal comments — code User Study (per Section 2's research-aim priority rule), assigning the system-focused code (3.4 or 3.9) as Secondary if that is genuinely the article's main claimed contribution. Physical Robot Demonstration and System/Architecture Paper are reserved for articles with zero reported human reaction of any kind. |
| **Non-examples** | Interviews with operators about a fielded system where no task/demo is described as having been performed or reacted to (-> Expert Elicitation, 3.2); a hardware build-and-run report where literally no human reaction, feedback, or behavior is reported (-> Physical Robot Demonstration, 3.4, or System/Architecture Paper, 3.9). |

If the Primary or Secondary code is User Study, also assign the following three sub-attributes. They apply only to the User Study code and are not separate top-level dimension codes.

### 3.1.1 Sub-attribute: Setting

| **Simulated/Remote (incl. VR)** | The participant interacts with the system through a computer-based simulation, an online/remote/crowdsourced task, or a virtual-reality headset; no physical robot hardware is confirmed present. As of v0.2, this is the default Setting code — assign it whenever the text does not clearly and explicitly describe a physical-hardware Lab environment or a real-world Field deployment, since purely simulated and remote settings are the most common in this research area. |
| --- | --- |
| **Lab** | A controlled indoor/laboratory environment in which the article explicitly and clearly describes physical robot/vehicle hardware being present and used by participants (e.g., tabletop robots, hardware-in-the-loop rigs), as distinct from a purely computer-simulated task. Do not assign Lab on the strength of "laboratory study" phrasing alone if the task itself is a screen-based simulation — that is Simulated/Remote. |
| **Field** | A real-world or realistic operational environment (e.g., an outdoor test range, an actual worksite, an actual flight/vehicle deployment), explicitly described as such in the text, typically with physical hardware deployed outside a lab setting. |

Default rule (added v0.2): Simulated/Remote is the default code for this sub-attribute. Only assign Lab or Field when the text gives clear, explicit evidence of a physical-hardware indoor setting or a real-world operational deployment, respectively; absent that evidence, code Simulated/Remote rather than guessing between Lab and Field. This reflects that most studies in this literature use computer-based simulations rather than physical hardware, and keeps "Lab" reserved for its more specific, hardware-present sense rather than functioning as a catch-all.

Note: if more than one setting is genuinely used across distinct conditions or sub-studies in the same article (e.g., a simulation trial and a separate physical flight test), record all that apply and note which condition each corresponds to, rather than forcing a single code.

### 3.1.2 Sub-attribute: Primary Measured Construct(s)

| **Performance** | Objective task-outcome metrics: completion time, accuracy, target detections, mission success rate, and similar. |
| --- | --- |
| **Workload** | Measured operator workload, e.g., NASA-TLX or a comparable subjective scale, or a physiological workload proxy. |
| **Trust** | Measured operator trust in the robot/system, via a trust scale or a behavioral trust proxy such as compliance or reliance. |
| **Situation Awareness (SA)** | Measured operator situation awareness, e.g., via SAGAT, SART, or comparable SA probes. |
| **Other / Not Listed** | Any other primary construct measured that is not one of the above (e.g., usability, communication load, safety incidents, learning/training effects) — record the specific construct alongside this code. |

This sub-attribute is multi-select: assign every construct the article formally measures. Do not assign a construct that is only discussed conceptually without an associated measure.

### 3.1.3 Sub-attribute: Study Modality Flags

| **Wizard-of-Oz** | The robot/swarm's apparent autonomous behavior is in whole or in part simulated or puppeteered by a human — an experimenter or hidden operator — rather than being generated by genuinely autonomous software, regardless of whether this is disclosed to the participant. This covers both the classic covert form (a human stands in for the system's decision-making, typically undisclosed or downplayed to the participant) and a disclosed/transparent form in which the human's role in narrating or determining system behavior is made known to the participant as part of the study procedure (e.g., an experimenter verbally describing simulated system outputs to the participant after each action, rather than the system rendering them automatically end-to-end). Note in the justification which form applies (disclosed vs. covert), since the two carry different implications for participants' trust calibration and mental models even though both substitute human judgment for automated behavior generation. |
| --- |
| **Human-Swarm Teaming** | The study explicitly frames the interaction as a human working within or alongside a robot team as a collaborative teammate — with mutual, bidirectional coordination or shared task authority between the human and the multi-robot team — rather than one-directional supervisory control of an otherwise separately-scripted system. |

These two flags are independent of each other and of Setting/Measured Construct(s); assign either, both, or neither as supported by the text. Absence of both flags is the default and does not need to be stated.

## 3.2 Code: Expert Elicitation / Interview or Survey Study

| **Definition** | Qualitative or questionnaire-based data collection from operators, domain experts, or stakeholders, aimed at eliciting requirements, opinions, needs, or design guidance about human-swarm/human-robot systems — not a controlled experiment in which participants perform an experimental task with the system. |
| --- | --- |
| **Key indicators** | Interviews, focus groups, or questionnaires/surveys distributed to experts or stakeholders. Thematic analysis, requirements-gathering, or coded-response synthesis as the primary method. No manipulated independent variable and no task performance measured. |
| **Example** | Requirements-gathering interviews with military or search-and-rescue operators to inform a future swarm-interface design. |
| **Distinguish from User Study (3.1)** | Expert Elicitation collects opinions/reports; it does not involve participants performing a controlled, measured task with the system. |
| **Distinguish from Framework/Taxonomy Paper (3.7)** | Elicitation's contribution is new empirical (qualitative) data collected from people; a framework paper's contribution is a conceptual model, which may be informed by the literature but need not involve new elicited data. |
| **Non-examples** | A paper that surveys the published literature rather than surveying people (-> Meta-review/Survey, 3.6); a study where experts perform a task under controlled, measured conditions (-> User Study, 3.1, likely Field or Lab). |

## 3.3 Code: Algorithm/Controller Evaluation (Simulation-Only)

| **Definition** | A paper whose primary contribution is a swarm behavior or control algorithm (control law, task allocation, formation control, path planning, etc.), validated entirely in simulation, with no human operator in the loop at any point. |
| --- | --- |
| **Key indicators** | A control-theoretic or algorithmic contribution is the article's stated main result. Validation is via simulation (e.g., MATLAB, Gazebo, a custom simulator), with no human subject or interface described. Performance is measured via algorithmic metrics — convergence, coverage, allocation efficiency, path length — rather than any human measure. |
| **Example** | A new consensus-based formation-control law tested across simulated swarm sizes and communication conditions. |
| **Distinguish from Simulation Benchmarking Study (3.5)** | Algorithm evaluation introduces and validates one (or a small closely related family of) new algorithm(s); benchmarking's primary contribution is a systematic comparison across multiple algorithms/interfaces/conditions, sometimes including a human-performance model. |
| **Distinguish from Modeling/Theoretical Paper (3.11)** | Algorithm evaluation validates primarily through simulated trial runs; a theoretical paper's primary validation is analytical (proofs, closed-form derivations, stability analysis), with simulation, if present, illustrative rather than the main evidence. |
| **Non-examples** | Any paper including a human-performance model standing in for an operator (-> Simulation Benchmarking Study, 3.5, since a human element, even simulated, is present and the framing is typically comparative); a paper reporting the same algorithm run on physical hardware (-> Physical Robot Demonstration, 3.4, or System/Architecture Paper, 3.9). |

## 3.4 Code: Physical Robot Demonstration / Proof-of-Concept

| **Definition** | A paper reporting a real hardware swarm/robot system that was built and operated to show feasibility, with NO human reaction, feedback, or observed behavior reported at all — typically a case study or system report ("we built X and it worked") describing only what the hardware did. |
| --- | --- |
| **Key indicators** | Real hardware described: physical robots, sensors, an outdoor or lab hardware trial. Narrative or descriptive reporting of what the system/hardware did, with no human participant's reaction, feedback, or behavior described anywhere in the article. As of v0.2, this code is reserved for the zero-human-data case: if even a few informal human observations or comments are reported, code User Study (3.1) instead, per Section 2's research-aim priority rule, and use this code as Secondary if the platform/demo is genuinely the article's main claimed contribution. |
| **Example** | A report describing a first field deployment of a set of physical ground robots executing a coordinated behavior, with a narrative account of the run and no human-subject data of any kind. |
| **Distinguish from User Study (3.1)** | As of v0.2: any reported human reaction, feedback, or observed behavior — however informal — means User Study applies (at least as Secondary); this code applies only when literally no such human data is reported. |
| **Distinguish from System/Architecture Paper (3.9)** | A demonstration's contribution is showing that a specific deployed behavior/mission worked; a system/architecture paper's contribution is the platform/toolkit/testbed itself as reusable infrastructure, of which a demonstration run may be only a light illustration. |
| **Non-examples** | A hardware trial with any reported human feedback, no matter how informal (-> User Study, 3.1, per the v0.2 research-aim priority rule); a purely simulated hardware description with no physical build (-> Algorithm/Controller Evaluation, 3.3, or Simulation Benchmarking Study, 3.5). |

## 3.5 Code: Simulation Benchmarking Study

| **Definition** | A systematic comparison of multiple algorithms and/or interfaces across simulated conditions, without live human operators — sometimes substituting a human-performance model for a real person — with the comparison itself, rather than a single new method, as the article's main contribution. |
| --- | --- |
| **Key indicators** | An explicit comparison across two or more algorithms, interfaces, or conditions. A simulation environment, possibly incorporating a human-performance or operator model (e.g., a queuing-theoretic neglect-tolerance model) in place of a real operator. A systematic experimental design with independent variables spanning conditions, but no live human subjects. |
| **Example** | Comparing several task-allocation algorithms' performance across simulated swarm sizes and communication-loss conditions using an operator-workload model in place of a real operator. |
| **Distinguish from Algorithm/Controller Evaluation (3.3)** | Benchmarking's contribution is the comparison itself, across multiple methods/conditions; algorithm evaluation's contribution is a single new algorithm being validated, typically without a systematic multi-method comparison as the main point. |
| **Distinguish from User Study (3.1)** | Benchmarking involves no live human participant, even where a human-performance model stands in for one; a User Study requires a real person whose behavior/response is measured. |
| **Non-examples** | A live human-subjects experiment (-> User Study, 3.1); a single algorithm's simulation validation with no comparative benchmarking design (-> Algorithm/Controller Evaluation, 3.3). |

## 3.6 Code: Meta-Review / Survey

| **Definition** | A paper whose primary contribution is synthesizing existing published literature on a topic, rather than reporting new primary data of any kind (empirical, elicited, algorithmic, or analytical). |
| --- | --- |
| **Key indicators** | A stated review scope and body of prior work being summarized/organized. No new participants, hardware trials, simulation runs, or derivations reported as the article's own contribution. Often includes a table or count of reviewed articles by theme, method, or year. |
| **Example** | A literature review organizing prior human-swarm interaction studies by interface type and measured construct. |
| **Distinguish from Framework/Taxonomy Paper (3.7)** | A survey's primary contribution is organizing or summarizing what already exists; a framework/taxonomy paper's primary contribution is a new conceptual model or classification scheme, which may draw on the literature but proposes something new rather than only an organized summary of it. |
| **Non-examples** | A paper proposing a new taxonomy as its main contribution, even if grounded in an extensive literature review (-> Framework/Taxonomy Paper, 3.7); a paper collecting new survey/questionnaire data from people (-> Expert Elicitation, 3.2 — note the terminology clash: "survey" here means literature survey, not a questionnaire administered to people). |

Assign one of the following two subtypes alongside the Meta-Review / Survey code.

| **3.6.1 Systematic Review** | Follows an explicit, reproducible search-and-screening methodology (e.g., PRISMA), typically reporting the search strategy, inclusion/exclusion criteria, and a flow/count of screened and included studies, with some structured or quantitative synthesis (coded tables, frequency counts across the included set). |
| --- | --- |
| **3.6.2 Narrative / Topical Survey** | Reviews and organizes literature around a topic without a formal, reproducible search protocol; synthesis is thematic or qualitative rather than count-based or protocol-driven. |

## 3.7 Code: Framework/Taxonomy Paper

| **Definition** | A paper whose primary contribution is a conceptual model, design space, or classification scheme (e.g., levels of autonomy, interaction taxonomies) without reporting new empirical data. |
| --- | --- |
| **Key indicators** | Proposes named dimensions, levels, or categories as the article's central contribution. May include illustrative examples drawn from the literature, but does not report new data collection. Often includes a diagram, decision tree, or table laying out the proposed scheme. |
| **Example** | A MICAH-style framework proposing categories of human-swarm interaction along multiple named dimensions. |
| **Distinguish from Meta-Review/Survey (3.6)** | A framework paper's contribution is a new organizing scheme; a survey's contribution is summarizing what already exists without necessarily proposing a new scheme of its own. |
| **Distinguish from Modeling/Theoretical Paper (3.11)** | Framework/taxonomy papers propose conceptual or qualitative categories; theoretical papers propose formal mathematical or analytical models with derivations. |
| **Non-examples** | A paper proposing new levels of autonomy and also validating them with new user data at comparable weight (-> Primary: Framework/Taxonomy Paper, Secondary: User Study, per Section 2's mixed-contribution rule). |

## 3.8 Code: Position/Vision Paper

| **Definition** | A paper that argues for a research direction or identifies open challenges and a research agenda, without reporting new data and without proposing a formal new framework or classification scheme. |
| --- | --- |
| **Key indicators** | Argumentative or opinion-driven structure ("we argue," "we call for," "the field should..."). Identification of gaps, challenges, or a research agenda as the central content. No new data of any kind, and no structured classification scheme (if one is present, see Framework/Taxonomy Paper instead). |
| **Example** | A paper arguing that human-swarm interaction research should prioritize a specific under-studied challenge, without new data or a proposed taxonomy. |
| **Distinguish from Framework/Taxonomy Paper (3.7)** | Position papers argue and identify gaps in prose; framework papers go further and propose a structured conceptual model or classification scheme for those gaps/challenges. |
| **Non-examples** | A paper proposing a structured taxonomy of open challenges (-> Framework/Taxonomy Paper, 3.7, since a classification scheme is present, not just an argument). |

## 3.9 Code: System/Architecture Paper

| **Definition** | A paper whose primary contribution is describing a novel platform, toolkit, or testbed (software and/or hardware) as itself — the reusable infrastructure — which may include a light illustrative validation or demo but where that validation is not the point of the article. |
| --- | --- |
| **Key indicators** | A named system with an architecture diagram or description of its components/modules. Framing emphasizes reusability, extensibility, or generality of the platform/toolkit/testbed, rather than a single mission outcome. Any included use case or demo is illustrative and secondary to describing the system itself. |
| **Example** | A paper introducing a new swarm-simulation toolkit or a modular ground-control-station architecture, with a brief illustrative use case. |
| **Distinguish from Physical Robot Demonstration (3.4)** | A demonstration's contribution is showing that a specific deployed behavior/mission worked; a system/architecture paper's contribution is the platform/toolkit itself as reusable infrastructure, independent of any one mission. |
| **Distinguish from Design/Interface Concept Paper (3.10)** | A system/architecture paper's scope is a full platform or toolkit, often including underlying software/hardware architecture beyond the interface layer; a design/interface concept paper's scope is specifically a single new interaction technique or UI. |
| **Non-examples** | A paper primarily reporting a new algorithm's simulation results, where the described system is only the vehicle for that algorithm (-> Algorithm/Controller Evaluation, 3.3, if the algorithm, not the platform, is the stated contribution). |

## 3.10 Code: Design/Interface Concept Paper

| **Definition** | A paper presenting a new interaction technique or user interface (e.g., gesture control, an AR overlay) with NO reported human evaluation of any kind — typically a workshop or short paper describing the concept/prototype itself, often framed as a precursor to a planned future study. |
| --- | --- |
| **Key indicators** | Description of a novel interaction concept or UI, often with mockups, wireframes, or an early prototype. No human reaction, feedback, or behavior reported at all — as of v0.2, even informal designer walkthroughs or a handful of pilot comments now count as User Study (3.1) per Section 2's research-aim priority rule, so this code narrows to the genuinely zero-evaluation case. Often explicitly framed as early-stage, future work, or a precursor to a planned evaluation. |
| **Example** | A short paper presenting a new gesture-based swarm-control concept with a working prototype and no reported human feedback of any kind. |
| **Distinguish from User Study (3.1)** | As of v0.2: any reported human reaction to or feedback on the interface, however informal, means User Study applies instead; this code is reserved for concepts presented with zero reported human evaluation. |
| **Distinguish from System/Architecture Paper (3.9)** | A design/interface concept paper's scope is a single interaction technique or UI; a system/architecture paper's scope is a broader platform or toolkit, which may include but is not limited to its interface. |
| **Non-examples** | A paper reporting even informal pilot feedback, designer walkthrough comments, or think-aloud observations from real people (-> User Study, 3.1, per the v0.2 research-aim priority rule). |

## 3.11 Code: Modeling/Theoretical Paper

| **Definition** | A paper presenting analytical or mathematical modeling of human-swarm systems (e.g., control-theoretic models of operator attention, queuing models of neglect tolerance), validated primarily analytically — via proofs, closed-form derivations, or stability analysis — rather than empirically or through simulation trials. |
| --- | --- |
| **Key indicators** | Equations, derivations, or formal proofs constitute the article's primary contribution. Validation is analytical (bounds, stability results, closed-form solutions); any simulation present is illustrative or a secondary check rather than the main evidence. No human participants and no systematic empirical/simulated comparison as the central method. |
| **Example** | A control-theoretic model of operator attention allocation across multiple robots, validated via stability analysis with an illustrative simulated example. |
| **Distinguish from Algorithm/Controller Evaluation (3.3)** | A theoretical paper's primary validation is analytical; algorithm evaluation's primary validation is empirical, via simulated trial runs across conditions. |
| **Distinguish from Simulation Benchmarking Study (3.5)** | A theoretical paper does not primarily compare algorithms empirically; it derives or proves properties of a model. |
| **Non-examples** | A paper whose primary results come from running simulations across conditions rather than from derivations or proofs (-> Algorithm/Controller Evaluation, 3.3, or Simulation Benchmarking Study, 3.5, as appropriate). |

## 3.12 Decision Procedure

- Step 0 (added v0.2 — check this first): does the article report ANY real person interacting with, operating, or reacting to the system, however informally (a stated N, a quote, a paraphrased comment, an observed behavior, a workload/performance/trust/SA measure — formal or informal)? If yes -> User Study (3.1) applies, per Section 2's research-aim priority rule. Assign it as Primary unless another contribution (a system, architecture, framework, algorithm) is clearly and substantially the article's main claimed focus, in which case assign User Study as Secondary and continue below to find the Primary code. Either way, assign User Study's Setting (3.1.1), Measured Construct(s) (3.1.2), and Study Modality Flags (3.1.3) sub-attributes.

- If Step 0 found no human-reaction data at all, locate the article's stated contribution(s), usually in the abstract and the introduction's "contributions" list, and its methods section.

- Ask: did the article collect or generate any new primary data (from real hardware, from simulation runs, or from a new elicitation)? If no — it is one of the no-new-data codes: an argumentative piece with no proposed classification scheme -> Position/Vision Paper (3.8); a proposed classification scheme/conceptual model -> Framework/Taxonomy Paper (3.7); a synthesis of existing literature -> Meta-Review/Survey (3.6), then choose 3.6.1 or 3.6.2 by whether a reproducible search protocol is reported.

- If yes, and the new data came from real hardware operated with zero human-subjects data reported (see Step 0) -> Physical Robot Demonstration / Proof-of-Concept (3.4). If instead the article's point is the reusable platform/toolkit itself (of which any hardware run is only an illustration) -> System/Architecture Paper (3.9).

- If yes, and the new data came purely from simulation with no human involved at all -> if the contribution is a single new algorithm/controller being validated, code Algorithm/Controller Evaluation (Simulation-Only) (3.3); if the contribution is a systematic comparison across multiple algorithms/interfaces/conditions (with or without a human-performance model standing in for a person) -> Simulation Benchmarking Study (3.5).

- If yes, and the new data came from real people but as opinions, requirements, or reports with no described interaction with the system itself -> Expert Elicitation / Interview or Survey Study (3.2).

- If a new interaction technique or UI is presented with zero reported human evaluation (see Step 0) -> Design/Interface Concept Paper (3.10).

- If, after this procedure, the article still does not clearly fit any single code, or fits two codes at genuinely comparable weight -> apply Section 2's Secondary-code and Unclear/Candidate-New-Code rules rather than forcing a single best guess silently.

# 4. Relationship to the Companion Classification_Codebook

This Study-Type codebook is applied first. Its output determines how the companion Classification_Codebook's task-environment, team-structure, interaction-style, coordination-architecture, computational-characteristics, and human-involvement dimensions should subsequently be approached for a given article:

- User Study, Physical Robot Demonstration, and System/Architecture Paper articles are the primary candidates for full coding against every dimension in the companion codebook, since they describe an actual operating human-robot(-swarm) system.

- Algorithm/Controller Evaluation and Simulation Benchmarking Study articles will typically code "Not Applicable" for Human Involvement Level and any human-side Team Structure/Interaction Style attributes, since no human is in the loop, but may still code meaningfully for Coordination Architecture and Computational Characteristics.

- Meta-Review/Survey, Framework/Taxonomy Paper, and Position/Vision Paper articles generally describe other systems rather than one of their own; the companion codebook's dimensions should either be applied to the specific systems/studies the article discusses (noted individually) or skipped with "Not Applicable" if the article stays at a purely conceptual level.

- Expert Elicitation and Design/Interface Concept Paper articles will often code "Not Described" for several companion-codebook dimensions (e.g., Coordination Architecture, Computational Characteristics) since these papers are frequently light on system implementation detail — this is expected and should be flagged per the companion codebook's own instructions rather than treated as a coding failure.

- Modeling/Theoretical Paper articles should have their analytical model's assumptions checked against the companion codebook's dimensions (e.g., does the model assume a particular Coordination Architecture or Team Structure?) even though no system was built or run.

# 5. Format for Adding or Revising Codes

Follow the same amendment process as the companion Classification_Codebook (its Section 13): propose new or revised codes rather than finalizing them unilaterally, use the same full-definition-table structure (Definition, Key indicators, Example, Distinguish from [other code(s)], Non-examples) for any new top-level study-type code, and log every change in the Change Log (Section 6) below with the date, what changed, and the article that motivated it. Because this dimension is designed to be near-exhaustive and mutually exclusive by construction, prefer tightening a "Distinguish from" note or a Key-indicator over adding an entirely new top-level code unless a genuinely distinct contribution type recurs across more than one article.

# 6. Change Log

| 2026-07-10 (v0.1): Codebook created as a new, standalone companion to Classification_Codebook, covering only the Primary Study/Contribution Type dimension. Defined eleven top-level codes at the user's specification: User Study (3.1, with Setting, Measured Construct(s), and Study Modality Flags sub-attributes), Expert Elicitation / Interview or Survey Study (3.2), Algorithm/Controller Evaluation (Simulation-Only) (3.3), Physical Robot Demonstration / Proof-of-Concept (3.4), Simulation Benchmarking Study (3.5), Meta-Review / Survey (3.6, split into Systematic Review 3.6.1 and Narrative/Topical Survey 3.6.2), Framework/Taxonomy Paper (3.7), Position/Vision Paper (3.8), System/Architecture Paper (3.9), Design/Interface Concept Paper (3.10), and Modeling/Theoretical Paper (3.11). Added a Decision Procedure (3.12) and a cross-reference section (Section 4) explaining how this codebook's output should steer application of the companion Classification_Codebook's dimensions. Not yet tested against the project's existing article corpus (Extracted_info.docx) — recommend a test pass against those articles before v0.2. |
| --- |
| 2026-07-10 (v0.2): Test-classified all 14 articles catalogued in Extracted_info.docx against v0.1; results were reviewed with the user but, per their request, were not written back into Extracted_info.docx. Two user-directed revisions followed from that test pass. (1) Research-aim priority rule for User Study: added to Section 2 and propagated into 3.1's Definition/Key indicators/Distinguish-from cells, 3.4 (Physical Robot Demonstration), 3.10 (Design/Interface Concept Paper), and the Decision Procedure (3.12, new Step 0) — an article is now coded User Study whenever it reports ANY human reaction to, feedback on, or observed behavior with the system, however informal, since live human-subjects data is the most relevant contribution type for this project's research aim; Physical Robot Demonstration and Design/Interface Concept Paper are correspondingly narrowed to the zero-human-data case only. This was motivated directly by the Williams et al. (2023) test case, previously flagged as an ambiguous System/Architecture-vs-Demonstration-vs-User-Study seam because ~15 personnel gave informal qualitative feedback with no formal N or statistics; it now codes cleanly as User Study (Secondary: System/Architecture Paper). (2) Setting default rule and rename: renamed 3.1.1's third code from "VR/Simulation" to "Simulated/Remote (incl. VR)" and broadened its definition to cover online/remote/crowdsourced simulated tasks, not only VR-headset studies; also made Simulated/Remote the explicit default for the Setting sub-attribute, to be overridden only by clear, explicit textual evidence of a physical-hardware Lab environment or a real-world Field deployment. This resolves the Jia et al. (2026) test case, previously a forced fit into VR/Simulation for a 393-participant online/browser-based study with no VR headset involved; Jia et al. is now classified Simulated/Remote under the new default rule without needing to be force-fit. Both changes were applied to the codebook text itself (not merely noted as flags) at the user's direction; the updated codebook has not yet been re-tested against the full 14-article set end-to-end beyond the two motivating cases. |
| --- |
| 2026-07-10 (v0.3): Broadened the Wizard-of-Oz Study Modality Flag definition (Section 3.1.3) to explicitly cover a disclosed/transparent form — a human (experimenter) narrating or determining simulated system behavior with this made known to the participant — alongside the existing covert/undisclosed form, which the prior wording ("typically undisclosed or downplayed") did not clearly accommodate. This was motivated by the Zhou et al. (2025) test case, in which the experimenter verbally described system-generated simulated UAV behaviors to participants after each command rather than the system rendering them automatically; this was previously an awkward fit since it substitutes human judgment for automated behavior generation (mechanically WoZ-like) but is openly disclosed as part of the simulation rather than hidden. Coders should now note in the justification which form (disclosed vs. covert) applies when assigning this flag. A related proposal from the same batch-coding pass — broadening this codebook's own Section 3.11 (Modeling/Theoretical Paper) to explicitly cover human-performance/queuing-simulation models validated empirically rather than analytically (raised by Donmez et al., 2010 and Parasuraman et al., 2005) — was deferred by the user for later consideration and is not reflected in this version. |