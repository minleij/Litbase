# HSI/HRI Task-Environment Classification Codebook

*Living codebook for coding the human-swarm / human-robot interaction (HSI/HRI) literature reviewed in this project.*

*Version 0.8  ·  Created 2026-07-07  ·  Last updated 2026-07-10  ·  Companion document to Extracted_info.docx*

# 1. Purpose and Scope

This codebook defines a set of standardized dimensions and codes for classifying articles in the human-swarm interaction (HSI) and human-robot interaction (HRI) literature reviewed in this project (see Extracted_info.docx for the underlying article summaries). It is intended to be applied by a large language model (an instance of Claude, or a comparable model) to new articles as they are added to the project, so that the growing set of papers can be compared systematically along consistent dimensions rather than read in isolation.

The codebook contains dimensions covering the task environment (originally derived from the hazard taxonomy in Wattearachchi et al. (2025), then generalized), the human-robot team's structure and interaction style, the coordination architecture governing decision authority across the robot team, its computational/autonomy characteristics, and the human involvement level. These are drawn from Dahiya et al. (2022), the NATO Autonomy Guidelines by Franzini et al. (2023), and, as of v0.4, Verma et al. (2020) and the convergent path-planning taxonomies of Geeta et al. (2025) and Lin et al. (2022). It is designed to be extended and revised: new dimensions and codes will be added, and existing codes may be redefined, as they are applied to more articles. The "Format for Adding or Revising Dimensions and Codes" section near the end specifies how to do this, and the Change Log section is a running record of what has changed and why.

# 2. How a Classifying Model Should Use This Codebook

- Unit of analysis: each code is applied at the level of a single reviewed article (or, where relevant, to a specific experiment/condition within an article, which should be noted explicitly).

- Evidence requirement: before assigning a code, locate the specific passage(s) in the article describing the task environment, object/entity structure, or other relevant construct. Do not infer a code from the article's title, keywords, or general topic alone.

- Multiple codes allowed: a dimension's codes are not necessarily mutually exclusive across an article as a whole - some studies test more than one condition (e.g. an article may include both Distributed and Moving task objects). Assign every code that is supported by the text, and note which condition/experiment each applies to if they differ.

- Codes from different dimensions combine: a single article, condition, or object may need one code from each dimension (e.g. a "Moving Task Object" that is also an "Avoidance Task"). Report all applicable dimension-code pairs rather than picking only one.

- Not Applicable vs. Not Described (v0.5 split): earlier versions of this codebook used a single combined tag, "Not Applicable / Not Described," for two different situations. As of v0.5 these are separate tags with separate meanings, and should not be merged back together: assign "Not Applicable" when a dimension does not conceptually apply to the system the article describes at all (e.g. Operational Domain for a purely theoretical study with no deployment context; Coordination Architecture for a system with only a single robot; Task-Object dynamics for a task that genuinely has no external tracked object, such as a purely internal battery-monitoring function). Assign "Not Described" when the dimension plausibly applies to the system being studied, but the article's text simply does not provide enough detail to determine a code (e.g. the article studies several robots, so Coordination Architecture conceptually applies, but never describes how those robots' actions are coordinated). Do not force a best-guess fit in either case - but do not collapse the two into each other either, since "the article never says" and "this doesn't apply to this kind of system" are different findings and both are useful to track separately across the corpus.

- Uncertain fit, and why it matters: if the article describes a relevant construct that does not clearly map onto any existing code, or a dimension that does not seem to apply cleanly, assign "Unclear / Candidate New Code" and describe the construct in a short note. Do not silently stretch an existing definition to force a fit, and do not silently invent and finalize a new code on your own authority.

- Surface uncertainty and Not-Described cases to the user: every time a code is marked "Not Described," "Not Applicable," or "Unclear / Candidate New Code" for an article, flag this explicitly back to the user in your response (not just in an internal note), together with: (a) the passage or construct that prompted it (for "Not Described," note specifically what was missing that would have let you code it), (b) why it doesn't fit the existing codes (for "Unclear"), and (c) a proposed name and draft definition for a new or revised code, if one comes to mind. The purpose is to let the user decide, case by case, whether an existing code's definition should be widened, a new code should be added, or the case is a genuine one-off exception. Do not update this document's definitions yourself based on this judgment call - propose the change and wait for the user's decision, exactly as happened when the original hazard-only codes were generalized into the current Task-Object dimension.

- Expect the codebook to evolve: codes defined from one article's terminology (e.g. "hazard") will often need to be generalized or split as new articles are added. Treat the current definitions as the best available draft, not a fixed standard.

- Output format: when classifying an article, report results as: Dimension -> Code(s) assigned -> one to two sentence justification with a paraphrased (not quoted) textual basis -> page/section reference if available. Do not reproduce more than a short (<15 word) verbatim phrase from any source when justifying a code.

- Definitions are authoritative: the definitions in the dimension sections of this codebook take precedence over the model's own prior associations with terms like "distributed," "moving," or "autonomous" from outside this project - these are project-specific technical codes, not general-purpose English usage.

- Some dimensions are explicitly provisional: a dimension's introductory paragraph may flag it as likely to need revision as new articles are reviewed (for example because the source taxonomy it was drawn from covers a narrower range of systems than this project's corpus, or because the underlying technology is still changing). For these dimensions, treat "Unclear / Candidate New Code" flags as expected and routine rather than exceptional, and surface them per the previous bullets.

# 3. Dimension: Task-Object Spatial-Temporal Dynamics

This dimension describes how a task-relevant object is structured in space and time within the task environment, independent of what the operator or system is required to do about it (that behavioral relationship is captured separately in Section 4). A "task-relevant object" is any entity, zone, or event the operator/system must detect, track, and act upon in some way: this includes hazards and threats, but equally covers targets, search subjects, incidents/events, or teams - e.g. a hazard zone, a lost person, a fleeing suspect, a ground team, or a set of incident reports from different zones.

This dimension was originally introduced, in a hazard-only form, based on the three-condition design in Wattearachchi et al. (2025), "Designing Effective Human-Swarm Interaction Interfaces: Insights from a User Study on Task Performance," in which 31 participants guided a 20-robot swarm to a target while avoiding hazards under three conditions (distributed, moving, spreading). It has been generalized here so the same spatial-temporal patterns can be coded regardless of whether the object is something to avoid, pursue, search for, or monitor.

Apply this dimension to any article whose task involves detecting, tracking, or otherwise acting on discrete task-relevant object(s)/event(s) in an environment. If the system being studied genuinely has no such object/event structure by design (e.g. a purely internal system-health monitoring function), code this dimension "Not Applicable." If such an object plausibly exists but the article's text doesn't describe it in enough detail, code "Not Described" instead.

## 3.1 Code: Distributed Task Object

| **Definition** | Multiple separate instances of the task-relevant object/event appear at scattered locations, arising intermittently over time; each individual instance, once present, is static (it does not move or grow). |
| --- | --- |
| **Key indicators** | Multiple discrete instances appear across the environment, not just one. Each individual instance does not move and does not grow/expand once it has appeared. Instances appear intermittently or unpredictably in onset (time and/or location), rather than in one continuous or patterned motion. Often tied to separate, independent causes/sources rather than one adversarial or contagious process. |
| **Source example (avoidance framing)** | Falling rocks or trees, loss of GPS signal, strong winds, and damaged terrain (Wattearachchi et al., 2025) - each is a scattered, self-contained hazard event rather than a moving or expanding one. |
| **Generalized examples (non-avoidance)** | Separate incident reports or requests for action arising from different zones or ground teams in a military/emergency-response scenario; multiple independent leads or targets appearing at different locations without relocating. |
| **Distinguish from Moving Task Object** | A Distributed object, once instantiated, stays where it is; a Moving object's defining feature is that it changes location over the course of the task. |
| **Distinguish from Spreading Task Object** | Distributed objects arise as multiple separate, scattered instances; a Spreading object grows outward continuously from a single point of origin. |
| **Non-examples** | A single object/area that grows over time (-> Spreading); an object that translates across the environment, such as a patrolling threat or a moving person (-> Moving). |

## 3.2 Code: Moving Task Object

| **Definition** | The task-relevant object occupies a location that shifts/changes continuously or repeatedly throughout the task, requiring the operator or system to continuously track and respond to its current location rather than address it once. |
| --- | --- |
| **Key indicators** | The object's spatial location changes dynamically and continuously (or repeatedly) during the task. Requires ongoing monitoring, tracking, or re-acquisition rather than a one-off decision. Often associated with an actively-directed or autonomously-moving source (a person, vehicle, or adversary), as opposed to a passive, fixed environmental feature. |
| **Source example (avoidance framing)** | Adversarial patrolling - a threat that moves through the environment over time (Wattearachchi et al., 2025). |
| **Generalized examples (non-avoidance)** | A lost person moving through terrain during a search-and-rescue task; a fleeing suspect being pursued; a mobile enemy unit being tracked for a strike or counter-drone engagement. |
| **Distinguish from Distributed Task Object** | Distributed objects do not relocate after they appear; Moving objects are defined precisely by their ongoing relocation. |
| **Distinguish from Spreading Task Object** | Moving objects translate/shift position without necessarily growing in size; a Spreading object grows outward from a fixed origin and need not translate. |
| **Non-examples** | An object that only grows from an origin point without relocating (-> Spreading); an object that appears once and stays fixed in place (-> Distributed). |

## 3.3 Code: Spreading Task Object

| **Definition** | The task-relevant object/condition originates at a single point and expands/grows outward over time, so that the affected area continuously increases in size (a contagion- or fire-like growth pattern). |
| --- | --- |
| **Key indicators** | Single, identifiable point of origin. The affected area's boundary grows/expands continuously over the course of the task. Growth is typically contiguous (spreads outward from the existing area) rather than appearing as disconnected new instances. |
| **Source example (avoidance framing)** | A spreading fire (Wattearachchi et al., 2025) - the canonical example of outward expansion from a single origin. |
| **Generalized examples (non-avoidance)** | Not yet clearly attested in the non-hazard/military articles reviewed so far. Possible future analogues include an expanding search cordon or containment zone, a spreading contamination/outbreak area, or spreading civil unrest - but none of these has been confirmed against a source article yet. |
| **Distinguish from Distributed Task Object** | A Spreading object has one growing origin; a Distributed object consists of multiple separate, non-growing instances scattered around the environment. |
| **Distinguish from Moving Task Object** | A Spreading object grows in place rather than translating; a Moving object translates/shifts position and need not grow. |
| **Non-examples** | Multiple unrelated object instances appearing at different locations (-> Distributed); an object that relocates without growing (-> Moving). |
| **Open flag** | This code was harder to generalize beyond the fire/hazard framing than Distributed or Moving. If an article's task-relevant object doesn't fit Distributed or Moving but also doesn't clearly "spread," mark "Unclear / Candidate New Code" per Section 2 rather than forcing it into this code. |

## 3.4 Code: Static/Fixed Task Object

| **Definition** | A single task-relevant entity or zone that is initially unknown to the operator/system and must be discovered via search, but that, once found, neither relocates, grows, nor recurs as multiple scattered instances - distinguishing it from Distributed (which requires multiple instances), Moving, and Spreading. |
| --- | --- |
| **Key indicators** | Exactly one instance of the task-relevant object/event exists for the task or sub-task at hand. Its location is unknown at the outset and must be discovered through exploration/search. Once located, it remains fixed in place and does not grow or spread. |
| **Source example** | Divband Soorati et al. (2021), Experiment I: a single disaster location is placed at a fixed, initially-unknown point in the mission zone, which the swarm must discover and localize; it does not move, grow, or recur as multiple instances during that experiment. |
| **Generalized examples** | A single, one-off event requiring detection and response, such as an isolated equipment or battery failure (Di Gregorio et al., 2021) - though see the Monitoring/Maintenance Task Distinguish-from note (Section 4.6): events concerning a system's own internal status are coded "Not Applicable" here even when they are single, fixed occurrences, since this code is reserved for external task-objects. |
| **Distinguish from Distributed Task Object (3.1)** | Distributed requires multiple separate, scattered instances; Static/Fixed is a single instance only. |
| **Distinguish from Moving Task Object (3.2)** | A Static/Fixed object does not relocate once found, unlike a Moving object. |
| **Distinguish from Spreading Task Object (3.3)** | A Static/Fixed object does not grow or expand once found, unlike a Spreading object. |
| **Non-examples** | Multiple scattered targets appearing over time (-> Distributed, 3.1); a single target that relocates after being found (-> Moving, 3.2); a hazard expanding from a point of origin (-> Spreading, 3.3); a change in the system's own internal status such as a battery event (-> Not Applicable here; see Monitoring/Maintenance Task, 4.6). |

## 3.5 Decision Procedure

- Locate the passage(s) describing the task-relevant object(s)/event(s) the operator or system must detect, track, or act on.

- If there is no such object/event structure in the task at all, by the nature of the system studied -> code "Not Applicable" and stop. If such an object plausibly exists for this kind of task but the text doesn't describe it -> code "Not Described" and stop.

- If the object grows outward continuously from a single point of origin -> code Spreading Task Object (3.3).

- If the object's location shifts/translates position over the course of the task -> code Moving Task Object (3.2).

- If the object appears as multiple separate, scattered instances that are individually static -> code Distributed Task Object (3.1).

- If the object is a single instance only, initially unknown and discovered via search, that neither relocates nor grows once found -> code Static/Fixed Task Object (3.4).

- If an article's study design includes more than one of these patterns (as in Wattearachchi et al., 2025, which tests Distributed, Moving, and Spreading), assign all applicable codes and note which experimental condition each corresponds to.

- If the object's spatial-temporal pattern does not clearly match any of the above -> code "Unclear / Candidate New Code," describe it briefly, and surface it to the user per Section 2.

# 4. Dimension: Behavioral Relation to Task Object

This dimension describes what the operator or system is required to do in relation to a task-relevant object described under Section 3 - for example, avoid it, pursue it, search for it, monitor it, or engage/neutralize it. It is applied together with, and independently of, the spatial-temporal dynamics codes: e.g. Wattearachchi et al. (2025)'s moving hazard is coded as Moving Task Object plus Avoidance Task, while Hughes et al. (2012)'s tracked high-value target is coded as Moving Task Object plus Pursuit Task.

Six codes are currently defined in this dimension: Avoidance Task (4.1), Search Task (4.2), Engagement Task (4.3), Pursuit Task (4.4), Defend/Block Task (4.5), and Monitoring/Maintenance Task (4.6). Unlike Section 3, more than one of these codes will often apply to the same article, since a single mission commonly combines several behavioral relations across its phases (e.g. search, then pursue, then engage, while separately avoiding a hazard) - see the Decision Procedure (4.7) for how to assign multiple codes and note which phase/condition each applies to.

## 4.1 Code: Avoidance Task

| **Definition** | The operator's or system's required behavior toward the task-relevant object is to avoid, evade, or steer clear of it: contact with the object carries a negative consequence, and the objective is to prevent or minimize such contact while still accomplishing the primary task (e.g. reaching a target). |
| --- | --- |
| **Key indicators** | Contact with the object has an explicit negative consequence (e.g. damage, deactivation, penalty, loss). The operator/system actively marks, steers around, or otherwise routes away from the object. The object is not itself the goal of the task - it is an obstacle to the actual goal. |
| **Source example** | In Wattearachchi et al. (2025), robots that enter a hazard region are deactivated; participants mark cells to route the swarm around all three hazard types (distributed, moving, spreading) while still guiding robots to the target. |
| **Distinguish from Defend/Block Task (4.5)** | Avoidance concerns the operator's own robots steering clear of a passive or environmental hazard for their own safety; Defend/Block concerns positioning robots to stop an active, adversarial agent from reaching a separate object of value. |
| **Non-examples** | Tasks where contact with the object is the goal rather than something to prevent - e.g. pursuing and reaching a fleeing suspect (-> Pursuit Task, 4.4, then Engagement Task, 4.3), searching for and locating a lost person (-> Search Task, 4.2), or striking a detected threat (-> Engagement Task, 4.3). |

## 4.2 Code: Search Task

| **Definition** | The operator's or system's required behavior toward the task-relevant object is to locate, detect, or identify it via area coverage or observation, where the object's location or presence is initially unknown; acquiring or confirming the object is the goal, prior to any further action taken on it. |
| --- | --- |
| **Key indicators** | The task-relevant object's location, presence, or identity is unknown at the outset and must be discovered through scanning, patrolling, or systematic coverage of an area. The operator/system reports, marks, or confirms the object once found. No negative consequence is framed for approaching or contacting the object - the goal is precisely to reach/detect it, not to avoid it. |
| **Source example** | Williamson et al. (2023): a swarm autonomously scans for and detects civilians, high-value targets, and enemy forces via an Overhead Scan tactic, notifying the operator once located. |
| **Generalized examples** | Reconnoitring suspected enemy positions (Zhou et al., 2025); marking discovered civilian vehicles (Fern et al., 2018); locating a suspicious-activity report at a designated grid location (Taylor et al., 2017); reporting sighted contacts along a transit route (Osga et al., 2013); locating hidden targets in a search-and-rescue map (Ramchurn et al., 2015). |
| **Distinguish from Avoidance Task (4.1)** | A Search Task's objective is to find/reach the object; an Avoidance Task's objective is to prevent contact with it. |
| **Distinguish from Pursuit Task (4.4)** | Search concerns an object whose location/presence is not yet known; Pursuit concerns an already-identified object that must be continuously followed as it moves. |
| **Distinguish from Engagement Task (4.3)** | Search's goal is detection/identification itself; Engagement's goal is to act decisively on an already-identified object. A single mission often combines both in sequence (search, then engage) - code both if the text supports it. |
| **Non-examples** | Steering away from a marked hazard zone (-> Avoidance Task, 4.1); continuously tracking a moving target already found (-> Pursuit Task, 4.4). |

## 4.3 Code: Engagement Task

| **Definition** | The operator's or system's required behavior toward the task-relevant object is to make contact with, neutralize, capture, or otherwise act decisively upon it, where such contact or acquisition is itself the goal of the task. |
| --- | --- |
| **Key indicators** | The task-relevant object has typically already been identified (often via a prior Search Task). The operator/system takes a decisive, often irreversible action directed at the object (e.g. firing on it, capturing it, securing it). Success is measured by whether the object was successfully acted upon, not by avoiding or merely observing it. |
| **Source example** | Williamson et al. (2023): once a hostile target is identified and confirmed, the swarm's Secure Artifact tactic acts on it directly to neutralize the threat. |
| **Generalized examples** | Prosecuting a confirmed high-value target by lasing and firing on it (Fern et al., 2018); capturing an opponent's flag (Parasuraman et al., 2005); conducting pre-emptive strikes on identified enemy groupings (Zhou et al., 2025). |
| **Distinguish from Search Task (4.2)** | Search's goal is detecting/identifying the object; Engagement's goal is acting decisively on an object once identified. |
| **Distinguish from Avoidance Task (4.1)** | Avoidance treats contact with the object as a negative outcome to prevent; Engagement treats contact with (or acquisition of) the object as the desired outcome. |
| **Distinguish from Defend/Block Task (4.5)** | Engagement is directed at the task-relevant object itself; Defend/Block is directed at preventing an opposing agent from reaching a separate object of value (e.g. one's own flag or a protected asset), without necessarily contacting the opposing agent. |
| **Non-examples** | Rerouting a robot around a hazard so it is never contacted (-> Avoidance Task, 4.1); positioning robots to keep an adversary away from an asset without acting on the adversary directly (-> Defend/Block Task, 4.5). |

## 4.4 Code: Pursuit Task

| **Definition** | The operator's or system's required behavior toward the task-relevant object is to continuously follow or maintain custody of it as it moves, where the object has already been identified/located and the ongoing challenge is keeping track of it rather than finding or acting on it. |
| --- | --- |
| **Key indicators** | The object is a Moving Task Object (3.2) that has already been detected/identified. The operator/system must continuously reacquire or maintain sensor/visual contact with it as it relocates, typically in preparation for a later Engagement or hand-off, rather than a one-off detection. |
| **Source example** | Hughes et al. (2012): once identified, a high-value target or fleeing "squirter" must be continuously tracked by the swarm as it moves toward or away from a location, maintaining visual custody until it stops or is intercepted. |
| **Generalized examples** | Tracking a military vehicle until it stops or reveals a weapon (Fern et al., 2018). |
| **Distinguish from Search Task (4.2)** | Search concerns finding an object whose location is unknown; Pursuit concerns continuously following an object that is already found. |
| **Distinguish from Engagement Task (4.3)** | Pursuit is about maintaining custody/contact with a moving object; Engagement is about acting decisively to neutralize or capture it. The two often occur in sequence within the same mission (pursue, then engage) - code both if the text supports it. |
| **Non-examples** | Scanning an area for a not-yet-located target (-> Search Task, 4.2); firing on or capturing a tracked target (-> Engagement Task, 4.3). |

## 4.5 Code: Defend/Block Task

| **Definition** | The operator's or system's required behavior is to position assets so as to prevent an opposing, adversarial agent from reaching or acquiring a separate object or area of value, rather than to find, follow, avoid, or directly engage a target itself. |
| --- | --- |
| **Key indicators** | An active, adversarial opposing agent (not a passive hazard) is attempting to reach or acquire something of value. The operator's/system's robots position themselves (e.g. patrolling a border, circling a protected asset) to intercept or block the opponent's access, rather than acting directly on the opponent or avoiding contact with a hazard. |
| **Source example** | Parasuraman et al. (2005): in RoboFlag, robots executing the Circle Defense or Patrol Border plays position themselves to prevent the opposing team from reaching and capturing the home flag. |
| **Generalized examples** | Securing road infrastructure to prevent enemy sabotage (Zhou et al., 2025). |
| **Distinguish from Avoidance Task (4.1)** | Avoidance concerns the operator's own robots steering clear of a hazard for their own safety; Defend/Block concerns positioning robots to stop an adversary's separate objective, independent of any hazard to the robots themselves. |
| **Distinguish from Engagement Task (4.3)** | Defend/Block's objective is achieved by blocking/positioning, without necessarily contacting or acting on the opposing agent directly; Engagement requires decisive action directed at the task-relevant object itself. |
| **Non-examples** | Steering a robot away from a hazard region for its own safety (-> Avoidance Task, 4.1); directly firing on or capturing an identified adversary (-> Engagement Task, 4.3). |

## 4.6 Code: Monitoring/Maintenance Task

| **Definition** | The operator's or system's required behavior is to detect and respond to a change in the task-relevant system's own internal health or status (e.g. battery level, component failure, connectivity), rather than to an external environmental entity, zone, or event as defined in Section 3. |
| --- | --- |
| **Key indicators** | The task-relevant "object" is the robot/system's own operating status rather than something external in the environment. The operator/system must notice a status change (e.g. a battery threshold crossed) and take a corrective or preventative action (e.g. recalling the unit) in response. |
| **Source example** | Di Gregorio et al. (2021): operators monitor each drone's battery level and must decide when to recall a drone to base before it is automatically forced to return at a critical threshold. |
| **Scope note** | This code is a deliberate, narrow extension of Section 4's scope: unlike the other codes in this dimension, it does not describe a relation to a Section 3 environmental task-object at all, but to the system's own internal state. Code Section 3 (Task-Object Spatial-Temporal Dynamics) as "Not Applicable" whenever Monitoring/Maintenance Task applies, since no external task-object exists to characterize spatially or temporally for that behavior. |
| **Distinguish from Avoidance Task (4.1)** | Avoidance concerns an external hazard the robot must not contact; Monitoring/Maintenance concerns the robot's own internal status, unrelated to any external hazard. |
| **Distinguish from Search Task (4.2)** | Search concerns detecting an external, previously-unknown object; Monitoring/Maintenance concerns detecting a change in a known, internal system parameter. |
| **Non-examples** | Detecting an external threat or target (-> Search Task, 4.2, or Engagement Task, 4.3); rerouting around an external hazard zone (-> Avoidance Task, 4.1). |

## 4.7 Decision Procedure

- Identify what the operator/system is described as doing in relation to each task-relevant object coded under Section 3 (or, for Monitoring/Maintenance Task, in relation to the system's own internal status).

- If contact with the object is explicitly framed as something to prevent, with a stated negative consequence for contact -> code Avoidance Task (4.1).

- If the object's location/presence is initially unknown and the goal is to detect/locate/identify it -> code Search Task (4.2).

- If the object has already been identified and the goal is to continuously follow/maintain custody of it as it moves -> code Pursuit Task (4.4).

- If the goal is to make contact with, neutralize, capture, or otherwise act decisively upon an already-identified object -> code Engagement Task (4.3). Search, Pursuit, and Engagement often combine in sequence within a single mission (search, then pursue, then engage) - code every phase the text supports, noting which condition/phase each applies to.

- If the required behavior is to position assets to block an active, adversarial agent from reaching a separate object of value, rather than to act on a target directly -> code Defend/Block Task (4.5).

- If the required behavior is to detect and respond to a change in the system's own internal status (e.g. battery, component health) rather than to an external object -> code Monitoring/Maintenance Task (4.6), and code Section 3 "Not Applicable" for that same behavior.

- More than one code may apply to a single article if it involves multiple distinct behavioral relations (e.g. searching for a target, then engaging it, while separately avoiding a hazard) - assign every code the text supports and note which task/phase each applies to.

- If Section 3 was coded "Not Applicable" for this article (no task-relevant object at all, and no internal-status monitoring behavior either) -> code this dimension "Not Applicable" too, for the same reason. If a task-relevant object exists (Section 3 gave it a real code) but the article's text doesn't describe how the operator/system is meant to relate to it -> code "Not Described" instead.

- If the behavioral relation still does not clearly match any of the above -> code "Unclear / Candidate New Code," describe it briefly, and surface it to the user per Section 2.

# 5. Dimension: Team Structure

This dimension describes the composition of the human-robot team itself - how many humans and robots are present, and whether the agents on each side are similar to or different from one another. It is drawn from Dahiya et al. (2022), "A Survey of Multi-Agent Human-Robot Interaction Systems," and applies to essentially every article in this corpus, since nearly all of them study some human-robot team.

## 5.1 Attribute: Team Size

Team size refers to the number of humans and the number of robots present in the system being studied.

| **Single-human - Single-robot** | One human interacts with one robot (the conventional dyadic HRI case). |
| --- | --- |
| **Single-human - Multi-robot** | One human interacts with or supervises more than one robot (e.g. a single operator commanding a swarm or fleet). |
| **Multi-human - Single-robot** | More than one human interacts with a single robot (e.g. a pilot/sensor-operator crew sharing control of one UAV, or a robot serving a group of people). |
| **Multi-human - Multi-robot** | More than one human and more than one robot are all part of the same interacting system. |

## 5.2 Attribute: Team Composition

Team composition describes whether the agents on the human side, and separately the agents on the robot side, are similar to (homogeneous) or different from (heterogeneous) one another in role, capability, embodiment, or authority.

| **Homogeneous** | The robots (and/or the humans) in the team are interchangeable or near-identical in role, capability, and embodiment - e.g. a swarm of identical robots, or a group of humans with no distinguished roles. |
| --- | --- |
| **Heterogeneous** | The robots (and/or the humans) differ meaningfully in role, capability, embodiment, or authority - e.g. robots with different manipulators or sensors, or humans with distinct roles such as supervisor vs. operator. |

Note that composition can be assessed separately for the human side and the robot side of the same team; if an article's team is homogeneous on one side and heterogeneous on the other, record both.

## 5.3 Decision Procedure

- Identify the number of humans and number of robots described as part of the interacting system -> assign the matching Team Size code.

- Assess whether the robots differ from one another in role/capability/embodiment; do the same for the humans if there is more than one -> assign Homogeneous or Heterogeneous for each side that has multiple agents.

- Team Structure applies to essentially every article (there is always at least one human and one robot to describe), so if team size or composition simply isn't stated clearly enough to determine -> code "Not Described" for that attribute rather than "Not Applicable."

# 6. Dimension: Interaction Style

This dimension describes how agents in the team communicate and interact with one another, independent of team structure. It is drawn from Dahiya et al. (2022).

Provisional note: the Interaction Directness attribute below (direct vs. indirect) is expected to need revision as new control and communication modalities (e.g. shared autonomy, mixed-initiative interfaces, novel sensing-based interaction) are encountered in the literature. Treat it as a starting point rather than an exhaustive pair of codes.

## 6.1 Attribute: Interaction Model

Interaction model describes how many agents are connected at each end of a given interaction or communication channel.

| **One-to-one** | At any given moment, an interaction connects exactly one agent to exactly one other agent (e.g. an operator giving an individual command to a single robot), even if other agents are present in the environment. |
| --- | --- |
| **One-to-many** | One agent's action or communication is directed at, or received by, multiple other agents simultaneously (e.g. a single operator issuing a group command to a whole robot swarm, or one robot addressing a group of humans). |
| **Many-to-many** | Multiple agents on both ends interact simultaneously, typically mediated by a shared interface or proxy (e.g. several human operators and several robots all connected through a common control system). |

## 6.2 Attribute: Interaction Directness

| **Direct** | An agent actively and explicitly communicates to a specific recipient (verbal or non-verbal). |
| --- | --- |
| **Indirect** | A third-party agent receives or is affected by information from an interaction not addressed to it ("eavesdropping"/observation), or agents are affected by each other's mere presence without explicit communication. |

## 6.3 Attribute: Communication Proximity

| **Remote** | Agents are not co-located; communication happens through a screen-based or other remote interface (e.g. teleoperation of robots in a hazardous or distant environment). |
| --- | --- |
| **Proximate** | Agents share the same physical space and can communicate via auditory, visual, or physical channels (speech, gesture, touch, etc.). |

## 6.4 Decision Procedure

- Identify the channel(s) of interaction described in the article and, for each, determine how many agents are on the sending and receiving end -> assign One-to-one, One-to-many, or Many-to-many.

- For each interaction, determine whether it is explicitly addressed to its recipient (Direct) or picked up by a non-addressed party / arises from mere co-presence (Indirect).

- Determine whether the interacting agents are co-located (Proximate) or physically separated (Remote).

- An article may exhibit more than one code per attribute (e.g. one-to-one between operator and individual robots, plus indirect observation between humans) - record all that are supported by the text.

- If a described interaction does not fit Direct/Indirect as currently defined (e.g. a genuinely novel modality) -> code "Unclear / Candidate New Code" per Section 2 rather than forcing the fit, since this attribute is flagged as provisional.

# 7. Dimension: Coordination Architecture

This dimension describes where decision-making authority for coordinating the robot team's actions resides - held by a single designated agent for the whole mission, held by a single agent that can change over time, distributed equally across all robots, or organized into local sub-groups - independent of how an individual robot computes its own actions (Section 8) or how the human interacts with the team (Section 6).

It is new in v0.4, drawn from Verma et al. (2020), "Multi-Robot Coordination Analysis, Taxonomy, Challenges and Future Scope," and Lin et al. (2022), "A Review of Path-Planning Approaches for Multiple Mobile Robots." Both articles independently treat centralized vs. decentralized coordination as a primary axis for classifying multi-robot systems; Verma further subdivides each side of that split, which this dimension adopts.

Apply this dimension to any article describing coordination among two or more robots. If an article studies a single robot only, this dimension does not conceptually apply - code "Not Applicable." If two or more robots are present but the article doesn't describe how coordination among them is organized, code "Not Described" instead.

## 7.1 Code: Strongly Centralized Coordination

| **Definition** | Coordination decisions for the whole team are made by a single fixed leader (a designated robot or a remote server/ground station) for the entire mission; other robots follow that leader's decisions/commands rather than deciding independently. |
| --- | --- |
| **Key indicators** | One robot or a central server is assigned as leader/coordinator prior to the task and remains leader throughout. Other robots' actions are described as commanded, scheduled, or assigned by it rather than negotiated. |
| **Source example** | A single fixed leader/server is responsible for making coordination decisions on behalf of all other robots for the entire mission, with the leader role never reassigned (Verma et al., 2020). |
| **Generalized examples** | A central mission-planning server that decomposes high-level operator tactics into per-robot commands and task assignments for an entire engagement. |
| **Distinguish from Weakly Centralized Coordination** | Leadership does not change hands during the mission. |
| **Distinguish from Distributed Coordination** | A single point of coordinating authority exists, rather than all robots sharing authority equally. |
| **Non-examples** | A leader role that rotates or is reassigned dynamically during the task (-> Weakly Centralized); robots negotiating peer-to-peer with no leader at all (-> Distributed). |

## 7.2 Code: Weakly Centralized Coordination

| **Definition** | A single robot/system holds coordinating authority at any given moment, but which robot holds that role can change dynamically during the mission (e.g. based on battery, position, priority, or other situational criteria), rather than being fixed in advance. |
| --- | --- |
| **Key indicators** | Leader-selection criteria are described (e.g. proximity, remaining resources, priority rules); the article mentions leader hand-off, re-election, or reselection during the task. |
| **Source example** | More than one robot is permitted to serve as leader during a mission, with the leader selected dynamically based on the current situation rather than fixed at the outset (Verma et al., 2020). |
| **Distinguish from Strongly Centralized Coordination** | The identity of the leader is not fixed for the whole mission. |
| **Distinguish from Hierarchical Coordination** | Only one leader is active at a time for the whole team, rather than multiple simultaneous local leaders each responsible for a sub-group. |
| **Non-examples** | A leader fixed at the outset and unchanged (-> Strongly Centralized); multiple simultaneous sub-group leaders (-> Hierarchical). |

## 7.3 Code: Distributed Coordination

| **Definition** | No single robot or server holds coordinating authority; all robots are equivalent in their responsibility and ability to decide, coordinating (if at all) through peer-to-peer interaction, shared local rules, or emergent/implicit signals (e.g. stigmergy) rather than through a leader. |
| --- | --- |
| **Key indicators** | No leader/coordinator role is described. Robots are described as acting autonomously and locally, with any coordination emerging from local rules, peer negotiation, or environment-mediated signals rather than commands from a single source. |
| **Source example** | All robots are independent and equal with respect to coordinating responsibility, with every robot taking decisions autonomously and no single control robot present (Verma et al., 2020). |
| **Generalized examples** | A PSO-based swarm in which each robot's velocity update depends only on locally shared best-position information, with no central controller; correlated-random-walk exploration in which a best-of-n outcome emerges from local information exchange with no leader robot. |
| **Distinguish from Strongly/Weakly Centralized Coordination** | No agent, fixed or rotating, is designated as authoritative for the whole team. |
| **Distinguish from Hierarchical Coordination** | There is no sub-group structure with local leaders; every robot has the same standing. |
| **Note** | Implicit, environment-mediated (stigmergic) coordination counts as Distributed Coordination even when robots never explicitly message one another - the absence of any leader is the defining feature, not the presence or absence of explicit communication. |

## 7.4 Code: Hierarchical Coordination

| **Definition** | Coordination is locally centralized - sub-groups of the team each have their own local leader/coordinator - but no single overarching leader controls the whole team. |
| --- | --- |
| **Key indicators** | Multiple simultaneous leader/coordinator roles are described, each responsible for a subset of robots; sub-groups work on different sub-tasks or in different zones, coordinated internally but not by one top-level authority. |
| **Source example** | The system has local leaders for sub-groups of robots, but these local leaders are not themselves controlled by any single overall leader (Verma et al., 2020). |
| **Distinguish from Weakly Centralized Coordination** | Multiple leaders are active concurrently (one per sub-group), rather than a single leader role that migrates between robots over time. |
| **Distinguish from Distributed Coordination** | Sub-groups have internal leaders, rather than every robot standing on equal footing. |
| **Non-examples** | A single leader for the whole team, fixed or rotating (-> Strongly/Weakly Centralized); no leaders at any level (-> Distributed). |

## 7.5 Code: Hybrid Coordination

| **Definition** | The system combines centralized and decentralized coordination mechanisms for different aspects, phases, or levels of the task (e.g. centrally assigned goals with decentralized local execution). |
| --- | --- |
| **Key indicators** | The article explicitly describes different coordination mechanisms operating at different stages or scopes within the same system (e.g. a central station periodically broadcasts goal positions, while robots decentrally plan their own motion to reach them). |
| **Source example** | Coordination is achieved partly in a centralized manner, such as a central station periodically sending goal positions to all robots, and partly in a decentralized manner, such as each robot's own motion planning to reach the assigned goal (Verma et al., 2020). |
| **Distinguish from the other codes** | Assign Hybrid only when both a centralized and a decentralized mechanism are explicitly described as coexisting; if only one mechanism is described, use the single matching code instead. |

## 7.6 Decision Procedure

- Locate the passage(s) describing how coordination/task-allocation decisions are made across the robot team - not how an individual robot decides its own low-level actions, which belongs to Section 8.

- If the article describes a single robot only -> "Not Applicable" (the dimension does not conceptually apply). If it describes two or more robots but does not describe how they coordinate -> "Not Described" instead - proceed to the remaining steps only for articles with multiple robots.

- If one fixed robot/server makes coordinating decisions for the whole mission -> Strongly Centralized Coordination.

- If the coordinating role is held by one robot/server at a time but can be reassigned during the mission -> Weakly Centralized Coordination.

- If multiple sub-group leaders operate concurrently with no single overarching leader -> Hierarchical Coordination.

- If no leader of any kind exists and all robots have equal coordinating authority (including purely implicit/stigmergic coordination) -> Distributed Coordination.

- If the article explicitly describes both centralized and decentralized mechanisms operating together -> Hybrid Coordination, plus a brief note on how they combine.

- If the coordination mechanism is described but does not fit any of the above -> "Unclear / Candidate New Code" per Section 2.

- If coordination is not described in enough detail to determine this (but two or more robots are present) -> "Not Described."

# 8. Dimension: Computational Characteristics (Robot Control)

This dimension describes the computational mechanism by which a robot's motion or behavior is generated, independent of the task it performs (Sections 3-4), how coordination authority is distributed across the team (Section 7), or how autonomous it is in the human-involvement sense (Section 9).

Revision note (v0.4): this dimension originally (v0.3) used a coarse two-code split - Optimization-Based Control vs. Predefined/Rule-Based Control - drawn from Dahiya et al. (2022). That split has been retired in favor of the five more granular codes below, following the convergent classical / heuristic / bio-inspired / learning-based taxonomy independently proposed by Geeta et al. (2025), "Path Planning for Fully Autonomous UAVs - A Taxonomic Review and Future Perspectives," and Lin et al. (2022), "A Review of Path-Planning Approaches for Multiple Mobile Robots." The old Predefined/Rule-Based code is retained unchanged (renumbered 8.5) because it captures scripted/Wizard-of-Oz control that the path-planning-derived codes do not cover; the old Optimization-Based code has been split apart into 8.3 and 8.4 below, which are more specific about the underlying mechanism. See the Change Log for the full mapping from v0.3 to v0.4.

Provisional note (retained): even this finer split may need to expand as new control paradigms (e.g. further hybrid architectures, novel planning representations) appear in the corpus.

Note on task-allocation algorithms (added v0.5): Sections 8.1-8.5 were derived from taxonomies of how an individual robot's motion/path is computed (Geeta et al., 2025; Lin et al., 2022). Testing against this project's corpus surfaced a distinct family of algorithms concerned instead with which robot performs which task - auction/bidding-based allocation, decentralized constraint-optimization/message-passing algorithms such as max-sum, and similar mechanisms - that do not fit any of 8.1-8.5 without stretching their definitions. Section 8.6 below is a deliberately perfunctory placeholder for this family, added so such articles can be flagged consistently rather than forced into a path-planning code. Task-allocation computation as its own topic needs further exploration - likely its own dedicated taxonomy and dimension in a future codebook version - before 8.6 should be considered a finished code.

## 8.1 Code: Classical Geometric / Sampling-Based Control

| **Definition** | Robot motion/paths are computed via deterministic geometric, graph-search, or sampling-based algorithms operating over an explicit map or configuration space, without a learned model or a population-based/metaheuristic search component (e.g. artificial potential fields, visibility graphs, Voronoi diagrams, probabilistic roadmaps (PRM), rapidly-exploring random trees (RRT), Dijkstra's algorithm). |
| --- | --- |
| **Key indicators** | The article names a specific classical algorithm family (APF, VD, VG, PRM, RRT, Dijkstra, etc.). The path is computed by geometric construction or explicit graph traversal rather than iterative optimization over a population or a trained model. |
| **Source example** | An artificial-potential-field method generates a collision-free route by treating obstacles as repulsive and the goal as attractive, without learning or population-based search (Geeta et al., 2025; Lin et al., 2022). |
| **Distinguish from Heuristic Search-Based Control** | Classical methods here can shade into heuristic search - if the algorithm explicitly uses a heuristic cost estimate to guide the order of search (A*, D*, Theta*), code 8.2 instead of 8.1. |
| **Distinguish from Bio-Inspired / Metaheuristic Optimization Control** | No population of candidate solutions or nature-inspired update rule is involved. |
| **Non-examples** | PSO, ACO, GA (-> Bio-Inspired/Metaheuristic, 8.3); A*, D*, Theta* (-> Heuristic Search-Based, 8.2). |

## 8.2 Code: Heuristic Search-Based Control

| **Definition** | Robot motion/paths are computed via search algorithms that use a heuristic cost or distance estimate to guide and prune the search toward a goal (e.g. A*, D*, Theta*, greedy heuristics, bi-level programming, Lin-Kernighan-style heuristics). |
| --- | --- |
| **Key indicators** | The article names a heuristic-informed search algorithm, or explicitly discusses a heuristic function estimating the remaining cost-to-goal. |
| **Source example** | An A*-based path planner uses a heuristic distance estimate to find a near-optimal route more efficiently than uninformed search (Geeta et al., 2025; Lin et al., 2022). |
| **Distinguish from Classical Geometric / Sampling-Based Control** | Uninformed graph/geometric methods without a guiding heuristic function belong in 8.1 instead. |
| **Distinguish from Bio-Inspired / Metaheuristic Optimization Control** | No population-based or nature-inspired search mechanism is involved - a single heuristic-guided search path is computed, not an evolving population of candidates. |
| **Non-examples** | Dijkstra, RRT, PRM without a guiding heuristic (-> Classical, 8.1); PSO, GA, ACO (-> Bio-Inspired, 8.3). |

## 8.3 Code: Bio-Inspired / Metaheuristic Optimization Control

| **Definition** | Robot motion/behavior is computed via a population-based or nature-inspired metaheuristic optimization process (e.g. Particle Swarm Optimization (PSO), Ant Colony Optimization (ACO), Genetic Algorithms (GA), Pigeon-Inspired Optimization, Grey Wolf Optimizer). |
| --- | --- |
| **Key indicators** | The article names a bio-inspired/metaheuristic algorithm and describes a population of candidate solutions, a fitness/objective function, and an iterative update rule inspired by natural collective behavior. |
| **Source example** | A PSO-based local-best swarm controller computes each robot's velocity update from locally shared best positions among neighboring robots (Wattearachchi et al., 2025, in this project's corpus; Geeta et al., 2025; Lin et al., 2022). |
| **Distinguish from Learning-Based Control** | Parameters are recomputed/updated by the metaheuristic's own search rule at run time rather than learned from data ahead of deployment - though the two can be combined (e.g. a metaheuristic used to tune a learned model); assign both codes with a note if so. |
| **Note** | This code corresponds to, and subsumes, what the v0.3 codebook called "Optimization-Based Control" whenever the optimization mechanism is specifically population-based/metaheuristic in nature. See 8.4 for the learned-model case, which v0.3 also folded into the same single code. |

## 8.4 Code: Learning-Based Control

| **Definition** | Robot motion/behavior is computed, fully or partly, by a model trained on data - machine learning, deep learning, or (deep) reinforcement learning - rather than by a fixed algorithm or a metaheuristic search run fresh each time. |
| --- | --- |
| **Key indicators** | The article names ML/DL/DRL methods (e.g. DQN, DDPG, SAC, TD3, neural-network-based planners) and describes a training process, a learned policy/model, or a trained network producing actions or paths. |
| **Source example** | A deep-reinforcement-learning agent is trained to produce collision-free UAV trajectories in dynamic environments (Geeta et al., 2025). |
| **Distinguish from Bio-Inspired / Metaheuristic Optimization Control** | Bio-inspired/metaheuristic methods search anew for each problem instance rather than deploying a model pre-trained on data, though hybrids exist (e.g. a metaheuristic used to tune a learned model's parameters) - assign both codes with a note when this occurs. |

## 8.5 Code: Predefined / Rule-Based Control

| **Definition** | Robot behavior is implemented via fixed if-then rules, expert-knowledge-based logic, pre-specified action sequences, or a hidden human teleoperator standing in for the robot's decision-making (Wizard of Oz), rather than a computed optimization, search, or learned model. |
| --- | --- |
| **Key indicators** | The article describes if-then rules, scripted behavior, or a fixed sequence of actions. A human "Wizard" covertly controls some or all of the robot's actions, speech, or behavior during the study. |
| **Source example** | A Wizard-of-Oz study in which a hidden operator controls a robot's speech and gestures to test human reactions to a fixed behavioral script (Dahiya et al., 2022). |
| **Distinguish from Classical Geometric / Sampling-Based Control** | This code is reserved for fixed behavioral if-then rules, scripted action sequences, or human-in-disguise control, not for deterministic path-planning algorithms operating over a map - a deterministic geometric/graph path algorithm should be coded 8.1-8.4 as appropriate, even though it is not "learned." |

## 8.6 Code: Task-Allocation (Placeholder)

| **Definition** | A deliberately minimal, perfunctory placeholder code for computational mechanisms that decide which robot performs which task, role, or sub-goal (task allocation/assignment) rather than how an individual robot's own motion/path is computed. Covers auction/bidding-based allocation, decentralized constraint-optimization or message-passing algorithms (e.g. max-sum), and similar mechanisms. |
| --- | --- |
| **Key indicators** | The article describes robots or a central system deciding task/role assignment across the team - who does what - rather than, or in addition to, how any one robot moves. Terms like "task allocation," "bidding," "auction," "assignment," or a named decentralized coordination algorithm (e.g. max-sum) are typically present. |
| **Source example** | A max-sum decentralized coordination algorithm computes task allocations across a UAV team to minimize completion time (Ramchurn et al., 2015, in this project's corpus); a swarm's individual robots bid on which of them is best suited to carry out a given high-level tactic (Williams et al., 2023, in this project's corpus). |
| **Status** | This code is intentionally not further subdivided (into e.g. auction-based vs. constraint-optimization-based) - it exists to flag articles whose control mechanism is fundamentally about task allocation, for a dedicated task-allocation taxonomy and dimension to be developed later, rather than to fully classify them now. See the note above this section. |
| **Distinguish from 8.1-8.5** | 8.1-8.5 describe how a robot computes its own motion/path once it has a task; 8.6 describes how the team decides who gets which task in the first place. The two can and often do co-occur in the same article (e.g. a system may use 8.6 for task assignment and 8.5 for how an individual robot then executes its assigned task) - assign both with a note when this happens. |

## 8.7 Decision Procedure

- Locate the passage(s) describing how the robot's actions/motion are generated or decided.

- If the mechanism is fundamentally about deciding which robot performs which task (allocation, assignment, auction/bidding, or a decentralized constraint-optimization/message-passing algorithm such as max-sum) rather than about how a robot's own motion/path is computed -> 8.6 Task-Allocation (Placeholder), and flag the article as a candidate for future task-allocation-specific coding per the note above.

- If a specific classical geometric/graph/sampling algorithm without a guiding heuristic is described -> 8.1 Classical Geometric/Sampling-Based Control.

- If a heuristic-informed search algorithm is described -> 8.2 Heuristic Search-Based Control.

- If a population-based/nature-inspired metaheuristic is described -> 8.3 Bio-Inspired/Metaheuristic Optimization Control.

- If a trained ML/DL/DRL model is described -> 8.4 Learning-Based Control.

- If fixed if-then rules, a scripted sequence, or Wizard-of-Oz control is described -> 8.5 Predefined/Rule-Based Control.

- These codes are not mutually exclusive: hybrid systems (e.g. a metaheuristic-tuned learned model, task allocation via 8.6 combined with per-robot execution via 8.5, or rule-based logic gating a learned controller) should receive all applicable codes with a brief note on how they combine.

- If the control mechanism is not described in enough detail to determine this -> "Not Described" (a control mechanism of some kind always conceptually exists, so "Not Applicable" should not normally apply to this dimension).

- If a described mechanism does not fit any of the above, including 8.6 -> "Unclear / Candidate New Code" per Section 2.

# 9. Dimension: Human Involvement Level

This dimension describes the level of human involvement expected in a function's operation and output, independent of how that function's behavior is computed (Section 8), how coordination authority is distributed across the robot team (Section 7), or what task-relevant object it relates to (Sections 3-4). It is drawn from the NATO Autonomy Guidelines for Practitioners (Franzini et al., 2023), and reflects NATO's agreed definitions.

The NATO source frames this as a property of an individual autonomy function, and provides a deterministic two-question flowchart to assign it (see 9.4). It also defines more granular sub-types within each of the three top-level codes (e.g. HInL-A "human in control in person" vs. HInL-B "remote pilot/operator"); this codebook adopts only the three top-level codes for now. Sub-types can be added later as a refinement if the corpus needs the extra granularity.

Added in v0.6: Section 9.5 below adds a second, more granular attribute to this dimension - Level of Human Control Abstraction (LHCA), a five-level operator-centric scale drawn from Johnson et al. (2020), "Applying Control Abstraction to the Design of Human-Agent Teams." It is assigned alongside, not instead of, the three HInL/HOnL/HOffL codes above; see 9.5 for how the two relate.

## 9.1 Code: Human-in-the-loop (HInL)

| **Definition** | A control mode in which a function requires human intervention to operate as desired. |
| --- | --- |
| **Key indicators** | The function affects, assists, or requires inputs from a human physically present, and/or fails or loses its purpose if human interaction is withdrawn. |
| **Source** | NATO Autonomy Guidelines (Franzini et al., 2023), Section 2.1.3 / Characterisation Stage II. |

## 9.2 Code: Human-on-the-loop (HOnL)

| **Definition** | A control mode in which a function's execution and/or outputs are monitored by a human who can exert control as required, but under normal conditions the function executes without human intervention. |
| --- | --- |
| **Key indicators** | The function delivers its output and achieves its purpose without human interaction, but a human reviews, can override, or otherwise oversees the function's operation or output. |
| **Source** | NATO Autonomy Guidelines (Franzini et al., 2023), Section 2.1.3 / Characterisation Stage II. |

## 9.3 Code: Human-off-the-loop (HOffL)

| **Definition** | A control mode in which a function is not monitored or interrupted by a human and executes without their intervention. |
| --- | --- |
| **Key indicators** | The function does not interface with any human at any stage (inputs, process, outputs, or effects), other than perhaps switching it on or off, and does not fail or lose value without human interaction. |
| **Source** | NATO Autonomy Guidelines (Franzini et al., 2023), Section 2.1.3 / Characterisation Stage II. |

## 9.4 Decision Procedure: Human-in/on/off-the-loop (NATO)

- Does any stage of the function (inputs, process, outputs, effect) interface with a human present, excluding simply switching the system on or off? If no -> ask the next question; if yes, ask whether the function requires continuous human "eyes on" input to operate as intended - if yes -> Human-in-the-loop; if the function interfaces with a human but does not require continuous input -> still assess against Human-on-the-loop below.

- Does the function stop delivering its output or lose its purpose/value if starved of human interaction (i.e. does it fail without a human)? If yes -> Human-in-the-loop. If no -> Human-on-the-loop.

- If the function has no dependency on a human at any of these stages -> Human-off-the-loop.

- This flowchart follows Franzini et al. (2023) Figure 4 and is intended to be applied per function or capability described in an article; an article describing multiple functions with different human-involvement levels should record a code per function.

- Every function has some human involvement level in principle, so this dimension is essentially always conceptually applicable; if the article does not describe human involvement clearly enough to apply this flowchart -> code "Not Described."

## 9.5 Attribute: Level of Human Control Abstraction (LHCA)

This attribute adds a fifth, more granular layer to the Human Involvement Level dimension, describing how granular the operator's required control inputs are within a given system state - independent of, and complementary to, the three-level Human-in/on/off-the-loop split above. It is drawn from Johnson et al. (2020), "Applying Control Abstraction to the Design of Human-Agent Teams," whose LHCA framework classifies system states - not whole articles or whole systems - by the granularity of operator input, on the premise that coarser inputs demand less continuous operator attention.

| **Direct (LHCA 1)** | The operator provides continuous control inputs that set the exact position/output of every control surface or motor directly (e.g. joystick axes mapped straight to elevators, ailerons, throttle). The operator is responsible for all aspects of system operation. |
| --- | --- |
| **Augmented (LHCA 2)** | The operator provides continuous input of desired actions/intent; the system closes the inner control loop, translating that intent into the corresponding control-surface/motor outputs. |
| **Parametric (LHCA 3)** | The operator gives discrete input of parameters the system should meet (e.g. waypoints, avoidance regions); onboard sensors/control algorithms maintain those parameters. The operator retains responsibility for safety monitoring, including obstacle avoidance, even when the system is functioning correctly. |
| **Goal-Oriented (LHCA 4)** | The operator gives discrete input of a goal to achieve within the mission; the system determines and executes all steps needed to meet that goal. The operator's role reduces to planning the next goal and monitoring for system failure. |
| **Mission-Capable (LHCA 5)** | The operator enters the entire mission's goals, together with standing rules/procedures, before the mission starts; the system then operates independently throughout. The operator has no mandatory monitoring role during execution. |

Application Rule 1 (state, not system): LHCA describes an instantaneous system state, not a whole article or whole system. A single system can support, and transition between, multiple LHCAs - operator-initiated (e.g. engaging an autopilot moves a state from Direct/Augmented to Parametric) or system-initiated (e.g. an automatic ground-collision-avoidance function taking over moves a state to Parametric). Code every distinct state an article describes, and note the trigger for any transition between them.

Application Rule 2 (minimum wins): when an article describes several simultaneous control inputs at different granularities within one state (e.g. an operator steering manually while an autopilot holds altitude), code the state at the lowest/most granular LHCA among them, not the average or the coarsest. Operator attention is driven by whichever input demands the finest granularity, so that is the input that determines the code.

Scope note (added v0.7): Johnson et al.'s (2020) own worked examples focus on flight-control surfaces, but the same continuous/discrete input logic is not inherently limited to flight control - it applies to any subsystem the operator directly manipulates within the state being coded, including sensor/camera/payload actuation and one-off authorization decisions (e.g. a weapons-release/engagement command). Treat a discrete authorization of a specific action ("engage this target") as a Goal-Oriented input like any other discrete goal, and treat continuous manual manipulation of a camera/sensor gimbal as Direct or Augmented input like any other continuous control, rather than treating these as outside LHCA's scope. Rule 2 (minimum wins) applies across subsystems, not only within one control channel: if an operator is, for instance, continuously panning a camera (Direct/Augmented) while the vehicle's own navigation runs autonomously in the background (which alone would be Goal-Oriented), code the combined state at the lower/more granular of the two, per the same logic as the cruise-control precedent above. Reserve "Unclear / Candidate New Code" strictly for control-input patterns that still don't fit any of the five levels after applying this broader scope - it should be the rare exception, not a default for non-flight-control functions.

Relationship to Human-in/on/off-the-loop (9.1-9.3): the two frameworks classify different things - the NATO codes classify a whole function/capability by whether it needs a human to operate as intended, while LHCA classifies an instantaneous control state by how granular the operator's input is - so assign both independently rather than treating them as equivalent. As loose orientation only (not a strict mapping): LHCA 1-2 will typically co-occur with Human-in-the-loop; LHCA 3 can co-occur with either Human-in-the-loop or Human-on-the-loop depending on whether the article's "safety monitoring" role requires continuous eyes-on attention; LHCA 4-5 will typically co-occur with Human-on-the-loop rather than Human-off-the-loop, since even Mission-Capable control still involves the operator at mission setup, which is more interaction than NATO's Human-off-the-loop definition allows.

## 9.6 Decision Procedure: LHCA

- Identify the specific system state being described (per Rule 1, LHCA is assigned per state, not per whole article) - an article describing an operator switching between manual flight and autopilot should be coded separately for each state.

- Is the operator giving continuous control input in this state? If yes: is the operator deciding the exact position of a control surface/motor/servo? Yes -> Direct (LHCA 1). No, the operator gives continuous input of a desired action but the system closes the inner loop -> Augmented (LHCA 2).

- If the operator's input is discrete rather than continuous: does the operator hold the preponderance of responsibility for safety monitoring/obstacle avoidance? Yes -> Parametric (LHCA 3). No: did the operator direct the system toward a goal within the mission, or the entire mission? Goal within mission -> Goal-Oriented (LHCA 4). Entire mission, set before the mission starts -> Mission-Capable (LHCA 5).

- If multiple simultaneous control inputs of different granularities are described within the same state, apply Rule 2: code the state at the lowest/most granular LHCA among them.

- If the article describes multiple distinct states (e.g. before/after an autopilot is engaged) -> code each separately and note the transition trigger per Rule 1.

- LHCA conceptually applies to essentially any human-system control state, so "Not Applicable" should rarely be used here - reserve it for cases with no described operator interface at all (e.g. a purely theoretical study). If the granularity of operator control isn't described in enough detail to place it on this scale -> "Not Described" instead.

- If a described control-input pattern doesn't fit any of the five levels -> "Unclear / Candidate New Code" per Section 2.

# 10. Dimension: Operational Domain

This dimension records the physical or operational domain(s) in which the studied system is deployed or intended to operate. It is drawn from the NATO Autonomy Guidelines (Franzini et al., 2023), Characterisation Stage I.

| **Air** | The system operates in the air domain (e.g. UAVs, aircraft). |
| --- | --- |
| **Land** | The system operates in the land domain (e.g. ground robots, UGVs). |
| **Maritime** | The system operates in the maritime domain (e.g. surface vessels, underwater vehicles). |
| **Space** | The system operates in the space domain. |
| **Cyber** | The system's operational domain is cyberspace/information systems rather than a physical environment. |
| **Spectrum** | The system's operational domain is the electromagnetic spectrum (e.g. signals, jamming, sensing). |
| **Cross-Domain** | The system's design or intended deployment spans more than one of the domains above (e.g. an air-and-ground search-and-rescue system); record the specific domains involved alongside this code. |

## 10.1 Decision Procedure

- Identify the domain(s) in which the studied system's agents (robots/UAVs/vessels/etc.) physically or operationally act.

- Assign one domain code if the system operates in a single domain; assign Cross-Domain plus the specific domains involved if it spans more than one.

- If the system has no deployment context at all (e.g. a purely theoretical/computational study) -> code "Not Applicable." If a deployment context plausibly exists but the domain simply isn't stated -> code "Not Described" instead.

# 11. Lexicon Anchor: Automatic vs. Autonomous

This section is not a coding dimension with its own codes; it is a definitional anchor that other dimensions (particularly Section 8, Computational Characteristics, and Section 9, Human Involvement Level) rely on. It is included so that a classifying model uses these terms consistently rather than relying on informal or inconsistent everyday usage. Definitions are taken verbatim in substance from the NATO Autonomy Guidelines (Franzini et al., 2023), Section 2.1.1.

| **Automatic** | Pertaining to a system, or a function of a system, that in response to inputs, follows a predetermined set of rules or sequence of events to provide a fully predictable outcome. Outcomes are entirely predictable given a consistent set of inputs. |
| --- | --- |
| **Autonomous** | Pertaining to a system, or a function of a system, that displays characteristics of autonomy: it can learn, adapt, and take decisions. An external entity assigns goals and constraints within which the system defines its own course of action; outcomes are potentially unpredictable but bounded by the assigned constraints. |
| **Relationship to other dimensions** | "Automatic" corresponds most closely to Predefined/Rule-Based Control (Section 8.5) and, for deterministic non-learned path algorithms, to Classical or Heuristic Search-Based Control (Sections 8.1-8.2), combined with a Human-off-the-loop or Human-on-the-loop involvement level (Section 9). "Autonomous" corresponds most closely to Bio-Inspired/Metaheuristic Optimization or Learning-Based Control (Sections 8.3-8.4). These are related but not identical framings - Section 8 describes the control mechanism, Section 9 describes human involvement, and this Lexicon entry clarifies the vocabulary that links them. |

# 12. Worked Example: Combining Multiple Dimensions

## 12.1 Wattearachchi et al. (2025): Hazard Avoidance

Wattearachchi et al. (2025) would be coded as follows, illustrating how dimensions combine for a single article:

- Task-Object Spatial-Temporal Dynamics: Distributed Task Object; Moving Task Object; Spreading Task Object (all three, one per experimental condition).

- Behavioral Relation to Task Object: Avoidance Task (applies to all three conditions - contact with any hazard type deactivates a robot).

- Team Structure: Single-human - Multi-robot (Team Size); Homogeneous (Team Composition - 20 identical robots).

- Interaction Style: One-to-many (Interaction Model - one operator directing many robots via swipe force/avoidance regions); Direct (Interaction Directness); Proximate is not applicable here since the operator uses a screen-based tablet interface - so Remote (Communication Proximity).

- Coordination Architecture: Distributed Coordination (each robot's PSO local-best velocity update depends only on locally shared neighbor information; no leader robot or central coordinator is described).

- Computational Characteristics: Bio-Inspired/Metaheuristic Optimization Control (PSO local-best swarm search governs robot motion).

- Human Involvement Level: Human-on-the-loop (the swarm searches autonomously via PSO; the human monitors and intervenes with swipes/avoidance markings as needed). LHCA (Section 9.5): Parametric Control - swipe-force and avoidance-region inputs are discrete, gesture-triggered parameter-setting actions (not sustained continuous joystick-style control), and the operator retains responsibility for monitoring the swarm's exposure to hazards while the PSO controller executes movement autonomously.

- Operational Domain: Land (ground robots searching a terrain grid).

## 12.2 Worked Example: New Behavioral Relation and Task-Object Codes (v0.8)

The codes added in v0.8 (Section 4.2-4.6, and Section 3.4) were themselves motivated by exactly the process Section 2 describes: articles that didn't fit any existing code were flagged as "Unclear / Candidate New Code" across a batch-coding pass of the project's corpus, and the resulting proposals were reviewed and adopted by the user. The following brief examples, one per new code, are drawn from that corpus and illustrate typical usage:

- **Search Task (4.2)**: Williamson et al. (2023) - the swarm autonomously scans for and reports civilians, high-value targets, and enemy forces before any further action is taken on them.
- **Engagement Task (4.3)**: Williamson et al. (2023) - once identified, hostile targets are neutralized directly (e.g. via the Secure Artifact tactic); also Fern et al. (2018), where confirmed high-value targets are prosecuted (lased and fired upon).
- **Pursuit Task (4.4)**: Hughes et al. (2012) - a high-value target or fleeing "squirter," once identified, must be continuously tracked as it moves, prior to any engagement.
- **Defend/Block Task (4.5)**: Parasuraman et al. (2005) - RoboFlag's Circle Defense and Patrol Border plays position robots to block the opposing team from reaching the home flag, independent of any hazard to the defending robots themselves.
- **Monitoring/Maintenance Task (4.6)**: Di Gregorio et al. (2021) - operators must notice and respond to a drone's battery status crossing a threshold, a relation to the system's own internal state rather than an external object (Section 3 is coded "Not Applicable" for this behavior).
- **Static/Fixed Task Object (3.4)**: Divband Soorati et al. (2021), Experiment I - a single, initially-unknown disaster location must be discovered, but it does not relocate, grow, or recur as multiple instances, distinguishing it from Distributed, Moving, and Spreading.

A single article commonly combines several of these across its different phases: e.g. a mission that requires searching for a target (Search Task), tracking it once found (Pursuit Task), and then engaging it (Engagement Task), while a separate part of the same mission requires avoiding an unrelated hazard (Avoidance Task) - code every phase the text supports, per the Decision Procedure (4.7), noting which condition or mission phase each code applies to.

# 13. Format for Adding or Revising Dimensions and Codes

When a new distinction emerges from a future article that is not covered by an existing dimension, add it using the same structure as the dimension sections above:

- A dimension heading (H1) with a one- to two-sentence description of what the dimension captures and which source article(s) motivated it.

- One H2 subsection per code or attribute. For codes with rich, potentially ambiguous boundaries (as in Sections 3-4 and 7-8), use the full definition table: Definition, Key indicators, Source example(s), Generalized examples, Distinguish from [other code(s)], Non-examples. For more straightforward categorical attributes drawn directly from an established taxonomy (as in Sections 5, 6, 9, 10), a compact Definition-only table per code is sufficient.

- A closing "Decision Procedure" subsection giving the classifying model a step-by-step rule for choosing between the dimension's codes, including how to handle "Not Applicable," "Not Described," and multi-code cases.

- An entry in the Change Log section noting the date, what was added or changed, and the source article that motivated it.

When an existing code needs to be widened, narrowed, split, or renamed (as happened when the original hazard-specific codes became Task-Object codes, and when the v0.3 Computational Characteristics binary split became the v0.4 five-code family), edit the code's table in place, update any cross-references ("Distinguish from..." cells, worked examples), and log the change rather than leaving the old and new definitions both in the document.

Candidate dimensions that may still be worth adding as more of the reviewed articles are processed include: situational-awareness measurement approach (e.g. SAGAT vs. SART) and NATO's HInL-A/B/C sub-types within Human-in-the-loop. A broader "MRS Team Coordination Properties" dimension (cooperative vs. competitive, reactive vs. deliberative, explicit/implicit-active/implicit-passive communication mode) was also considered, drawing on Verma et al. (2020) Section 3, but was deliberately not added in v0.4 - it was judged too granular to reliably apply across this corpus's current range of articles. Johnson (2020)'s five-level Level of Human Control Abstraction, previously listed here as a candidate, was added in v0.6 as Section 9.5. These are suggestions only - add a dimension once a second article provides a genuine point of comparison, not preemptively.

# 14. Change Log

| **2026-07-07 (v0.1)** | Codebook created. Added Dimension: Hazard / Threat Environment Dynamics, with codes Distributed, Moving, and Spreading hazard, based on Wattearachchi et al. (2025). |
| --- | --- |
| **2026-07-07 (v0.2)** | Generalized the hazard dimension to Task-Object Spatial-Temporal Dynamics (codes renamed Distributed / Moving / Spreading Task Object) so it can apply beyond avoidance scenarios (e.g. military pursuit/search tasks). Added new Dimension: Behavioral Relation to Task Object, with code Avoidance Task, to separately capture the hazard-specific "must avoid contact" relation that was previously bundled into the hazard codes. Updated usage instructions to require surfacing Not-Applicable and Unclear/Candidate-New-Code cases to the user for discussion before the codebook is revised. Flagged Spreading Task Object as harder to generalize beyond the fire example; no confirmed non-hazard analogue yet. |
| **2026-07-07 (v0.3)** | Added five new sections based on Dahiya et al. (2022) and the NATO Autonomy Guidelines (Franzini et al., 2023): Dimension: Team Structure (Team Size, Team Composition); Dimension: Interaction Style (Interaction Model, Interaction Directness, Communication Proximity); Dimension: Computational Characteristics / Robot Control (Optimization-Based, Predefined/Rule-Based); Dimension: Human Involvement Level (Human-in/on/off-the-loop, per NATO's flowchart); Dimension: Operational Domain (Air/Land/Maritime/Space/Cyber/Spectrum/Cross-Domain); and a non-coding Lexicon Anchor defining Automatic vs. Autonomous to keep terminology consistent across dimensions. Deliberately excluded NATO's Control Layer, Output Explainability/Reversibility, and Readiness Level scales as too fine-grained for whole-article classification. Flagged Interaction Directness (Section 6.2) and Computational Characteristics (Section 7) as provisional and likely to need expansion as new control/communication modalities appear in the corpus. Updated the Worked Example to show all dimensions applied to Wattearachchi et al. (2025), and generalized internal section-number cross-references so they don't go stale as the codebook grows. |
| **2026-07-09 (v0.4)** | Added new Dimension: Coordination Architecture (Section 7), with codes Strongly Centralized, Weakly Centralized, Distributed, Hierarchical, and Hybrid Coordination, based on Verma et al. (2020) and Lin et al. (2022), both of which treat centralized-vs-decentralized robot-team decision authority as a primary classification axis. This dimension is new, not a replacement of anything in v0.3. Refined Dimension: Computational Characteristics (Robot Control) (renumbered Section 8) by retiring the v0.3 coarse Optimization-Based/Predefined-Rule-Based split in favor of five more granular codes - Classical Geometric/Sampling-Based (8.1), Heuristic Search-Based (8.2), Bio-Inspired/Metaheuristic Optimization (8.3), Learning-Based (8.4), and retained Predefined/Rule-Based (8.5, unchanged from v0.3) - based on the convergent classical/heuristic/bio-inspired/learning-based taxonomy independently proposed by Geeta et al. (2025) and Lin et al. (2022). The old v0.3 Optimization-Based code is superseded by (split across) the new 8.3 and 8.4; the old Predefined/Rule-Based code carries forward unchanged as 8.5. Renumbered all subsequent sections (Human Involvement Level -> 9, Operational Domain -> 10, Lexicon Anchor -> 11, Worked Example -> 12, Format -> 13, Change Log -> 14) and updated internal cross-references, the Lexicon Anchor's mapping to Section 8, and the Worked Example accordingly. Considered, and deliberately declined to add, a separate "MRS Team Coordination Properties" dimension (cooperative/competitive, reactive/deliberative, communication mode) from Verma et al. (2020) Section 3 - flagged in Section 13 as likely too granular for the current corpus; also noted Johnson (2020)'s five-level Level of Human Control Abstraction as a candidate future refinement of Section 9, not yet added. |
| **2026-07-09 (v0.5)** | Split the combined "Not Applicable / Not Described" tag (used throughout Section 2 and every dimension's Decision Procedure since v0.1) into two distinct tags: "Not Applicable" (the dimension does not conceptually apply to the system described - e.g. a single-robot article and Coordination Architecture) and "Not Described" (the dimension plausibly applies, but the article's text doesn't provide enough detail to code it - e.g. multiple robots are present but their coordination mechanism is never described). Updated Section 2's core usage instructions and every dimension's Decision Procedure (Sections 3, 4, 5, 7, 8, 9, 10) accordingly; most "not stated in the text" cases across the codebook are "Not Described" rather than "Not Applicable." Added Section 8.6, Code: Task-Allocation (Placeholder), a deliberately minimal stand-in code for control mechanisms concerned with which robot performs which task (auction/bidding-based allocation, decentralized constraint-optimization/message-passing algorithms such as max-sum) rather than how an individual robot's motion/path is computed - this gap was surfaced when Williams et al. (2023)'s tactical bidding and Ramchurn et al. (2015)'s max-sum coordination, both in this project's corpus, didn't fit any of 8.1-8.5. Renumbered the Section 8 Decision Procedure to 8.7 accordingly. Added an explicit note (in Section 8, before 8.1) that task-allocation computation is its own topic needing further exploration - likely a dedicated future taxonomy and dimension - and that 8.6 is a flag for such cases, not a finished classification of them. Test-classified all 14 articles catalogued in Extracted_info.docx against Coordination Architecture (Section 7) and Computational Characteristics (Section 8); results, including best-guess codes for underspecified cases, were written back into Extracted_info.docx. |
| **2026-07-09 (v0.6)** | Added Section 9.5, Attribute: Level of Human Control Abstraction (LHCA), and its Decision Procedure (Section 9.6), based on Johnson et al. (2020), "Applying Control Abstraction to the Design of Human-Agent Teams." LHCA is a five-level, operator-centric scale (Direct, Augmented, Parametric, Goal-Oriented, Mission-Capable) describing the granularity of operator control input within a given system state, assigned alongside (not instead of) the existing three-level Human-in/on/off-the-loop codes (9.1-9.3, renumbered Decision Procedure to 9.4). Carried over Johnson's two application rules as explicit coding guidance: LHCA is assigned per system-state rather than per whole article, and a system with multiple simultaneous control inputs at different granularities is coded at the lowest/most granular LHCA among them ("minimum wins"). Added a loose, explicitly non-equivalent cross-reference between LHCA and the HInL/HOnL/HOffL codes. Updated the Section 12 Worked Example (Wattearachchi et al., 2025) to include an LHCA code (Parametric Control) alongside its existing Human-on-the-loop code. Removed Johnson (2020)'s LHCA from the Section 13 candidate-dimensions list, since it is now implemented. |
| **2026-07-09 (v0.7)** | Added a Scope note to Section 9.5, prompted by testing LHCA against six example articles: Johnson et al.'s (2020) own worked examples focus on flight-control surfaces, but two test cases (a weapons-engagement authorization in Taylor et al., 2017; continuous camera pan/zoom during target search in Donmez et al., 2010) initially got coded "Unclear" or treated as out of scope, when in fact the decision tree applies cleanly once "control surface" is read to include any subsystem the operator directly manipulates (sensor/payload actuation, one-off authorization decisions). Clarified that Rule 2 (minimum wins) applies across subsystems within a state, not only within one control channel - e.g. continuous camera control (Direct/Augmented) dominates a state's code even when the vehicle's own navigation is simultaneously running at Goal-Oriented in the background. Reserve "Unclear / Candidate New Code" for LHCA strictly for patterns that don't fit any of the five levels even after applying this broader scope - it should be rare, not a default for non-flight-control functions. |
| --- |
| **2026-07-10 (v0.8)** | Added six new codes, motivated by a batch-coding pass of 15 articles in the project's corpus during which "Unclear / Candidate New Code" was raised repeatedly for behavioral relations and a task-object pattern with no existing match. Added Section 3.4, Code: Static/Fixed Task Object (a single, initially-unknown task-object that neither relocates, grows, nor recurs as multiple instances once found - source example: Divband Soorati et al., 2021, Experiment I), renumbering the Section 3 Decision Procedure to 3.5. Added five new codes to Section 4, Behavioral Relation to Task Object, which had previously defined only Avoidance Task and explicitly anticipated needing more: Section 4.2, Code: Search Task (locating/identifying an object of initially-unknown location or presence; raised in 12 of the 15 batch-coded articles, by far the most recurrent gap - source example: Williamson et al., 2023); Section 4.3, Code: Engagement Task (making decisive contact with/neutralizing an already-identified object; raised in 5 articles - source example: Williamson et al., 2023); Section 4.4, Code: Pursuit Task (continuously following an already-identified moving object; raised in 2 articles - source example: Hughes et al., 2012); Section 4.5, Code: Defend/Block Task (positioning assets to block an adversarial agent from a separate object of value, distinct from Avoidance Task's focus on the operator's own robots' safety; raised in 2 articles - source example: Parasuraman et al., 2005); and Section 4.6, Code: Monitoring/Maintenance Task (detecting and responding to the system's own internal health/status rather than an external task-object, a deliberate narrow extension of this dimension's scope; raised in 1 article - source example: Di Gregorio et al., 2021). Renumbered the Section 4 Decision Procedure to 4.7 and rewrote it to cover all six codes, including how they combine across mission phases (e.g. search, then pursue, then engage) and the Monitoring/Maintenance Task's requirement to code Section 3 "Not Applicable" for that same behavior. Restructured Section 12 into 12.1 (the existing Wattearachchi et al., 2025 worked example) and added 12.2, a worked example demonstrating each new code against its corpus source article, replacing the now-resolved "hypothetical future article" placeholder for the pursuit case. Two related, narrower-evidence proposals raised in the same batch-coding pass - broadening Study-Type codebook Section 3.11 (Modeling/Theoretical Paper) to cover empirically-validated human-performance/queuing models, and a definitional question about disclosed human-narrated simulation as a Wizard-of-Oz-adjacent pattern - were deferred by the user for later consideration and are not reflected in this version. |