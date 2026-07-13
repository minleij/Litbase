# Summary Template: User Study

Use this template whenever the Study-Type codebook assigned User Study as the Primary **or** Secondary code for the article — including when it's only a small, informal part of a larger system/architecture or algorithm paper. Per the Study-Type codebook's own research-aim priority rule, this is deliberately the common case for this project, so it's worth extracting these fields carefully rather than treating the summary step as a formality.

## Purpose

These summaries exist to do two jobs at once: let a researcher get useful context on an article in under a minute, and let the corpus support qualitative analysis later — specifically, connecting *issues* and *recommendations* back to the *type of system* that produced them, across many articles at once. Write the summary with the second job in mind, not just the first: a vague "the system worked well" doesn't help someone doing cross-article synthesis later, even if it's an accurate one-line gist.

## Fields to extract

Write each field as free text (a sentence to a short paragraph, not a single word or a bare list unless the content genuinely is a list). Base every field on what the article actually reports — if a field genuinely isn't covered by the article, say so explicitly (e.g. "Not reported") rather than leaving it blank or inferring content that isn't there.

- **Task** — What did participants actually do? The scenario, mission, or activity they performed with or through the system (e.g., "search a simulated town for civilians and high-value targets while directing a swarm of up to 100 robots via sketch and AR gestures").

- **Control** — How did participants exercise control over the system? The interface(s), command modality, and level of directness (e.g., sketch gestures translated into high-level tactics that the swarm bids on internally; joystick teleoperation of a single vehicle; a delegation-style "plays" interface). This is about the human-system control relationship specifically, distinct from Task.

- **Participants** — Who took part, how many, and what's known about their background (e.g., "8 military-rated helicopter test pilots"; "~15 military personnel and researchers of varied backgrounds, informal feedback only"). Note explicitly if the sample was informal/unspecified rather than a formally reported N — this is itself useful information for the corpus, not something to paper over.

- **Results** — The main outcomes of the trial(s): what worked, what was measured, and what was found, whether quantitative (task completion time, workload scores) or qualitative (participant feedback themes). Keep this to genuine reported findings, not the authors' broader interpretive claims about the field.

- **Issues** — Problems, limitations, or difficulties identified during the study — by participants, by the authors, or observed in the results (e.g., high cognitive load in one condition, an interface participants found confusing, a scenario where autonomy failed to hand off control cleanly). This is one of the two most important fields for this corpus: write it so that a reader doing cross-article synthesis could group this issue with similar issues from other articles. If no issues are reported at all, say so explicitly rather than omitting the field — that's a meaningful finding too.

- **Recommendations** — Design or research recommendations made by the authors, whether explicitly stated ("future systems should...") or reasonably implied by their discussion of the issues above. Like Issues, write this so it's usable for cross-article synthesis, and state explicitly if none are given.

- **Autonomous Capabilities** — What the system did on its own, independent of the human-control description above: e.g., autonomous path planning, target classification, task bidding/allocation among robots, obstacle avoidance. This is deliberately kept separate from Control, since a system can have a human directly controlling *and* substantial autonomous capability running underneath (e.g., a bidding system that autonomously decomposes a human's high-level tactic into robot primitives) — describe both without conflating them.

## Note on secondary User Study cases

If User Study is a Secondary code (e.g., the article's main contribution is a System/Architecture paper that also reports informal user feedback), still fill out all seven fields above based on whatever the user-study portion of the article reports — just keep Task/Control/Participants/Results proportionate to how much the article actually says about that portion. Don't pad these out with the system's general capabilities beyond what's relevant to the human-facing trial; that belongs in Autonomous Capabilities or is better captured by the Task-Environment classification in Step 4 of `SKILL.md`.
