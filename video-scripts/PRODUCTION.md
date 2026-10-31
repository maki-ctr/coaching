# Video production (NotebookLM)

Eight explainer videos, one per course module. The scripts in this folder are the source of truth. Produce videos only after the scripts are approved.

## Pipeline

1. **One new notebook per video.** Never reuse a notebook; old sources carry old errors.
2. **Two sources only:**
   - the module's script (`0N-*.txt`) as the main source;
   - the matching pages of the official U.S. Soccer B Course Guide, once Freddy has it from the Learning Center. Until then, use the script alone.
3. **Format:** Explainer. Paste the custom prompt below.
4. **Watch with the checklist** for that module: every "Must hear" item present, no "Reject if" item.
5. **Get the transcript** and check it against the same lists before publishing.
6. **Upload to YouTube as Unlisted** (not Private, or it won't play inside the app).
7. **Add the video ID** to `CONFIG.videos` at the top of the script in `index.html`, e.g. `videos: {1:"abc123XYZ", ...}`.
8. If a video has a one-word slip that can't cost understanding, add a correction note under the video instead of regenerating. Regenerate if it teaches something wrong.

## Custom prompt (all videos)

> Create an explainer for a football coach preparing for the U.S. Soccer B License. Follow the main script's order exactly. Keep its definitions and numbers word for word. Use the Harbor FC U17 scenario as written. Do not add facts, statistics, examples, course requirements or terms that aren't in the sources. Do not mention UEFA or other federations. Keep a calm, practical coaching tone.

## Stricter fallback prompt (for regeneration)

> Follow the main script only, in order, sentence by sentence where possible. Do not invent course requirements, dates, durations or assessment details. Do not change any number. Do not describe the waiver as automatic. Do not call pitch size an environmental constraint. Do not describe the flags or KPIs as official U.S. Soccer standards. If something isn't in the script, leave it out.

## Checklists

### 1. The route to the A
**Must hear:** waiver of the C License for former pro/national-team players; the host decides; request through the Learning Center; U13+ 11v11 team for the whole course; about 24 weeks, blended, two in-person meetings; five competencies; B held at least 12 months, counted from the award; A-Youth vs A-Senior chosen by team environment; Pro requires A held at least a year.
**Reject if:** the waiver is called automatic or guaranteed; a specific number of playing years is stated as the rule; the course is called a written exam; the 12 months count from the course start; UEFA licenses are discussed.

### 2. Building the game model
**Must hear:** five moments; principles you can train and measure; three or four per moment; the Harbor identity line; 4-3-3; the five-second counter-press; model vs plan distinction; the two-minute pitch.
**Reject if:** "game model" and "game plan" are used as the same thing; principles are added that aren't in the script; the formation changes.

### 3. Designing training from the game model
**Must hear:** six-step thread; 6 of 41 (15%) against Westside; three runners found behind; 80 minutes; 15/20/25/20 practices with the stated areas; the re-press rule; task, environment, individual constraints; pitch size is a task constraint; representative practice.
**Reject if:** any practice duration, area or number changes; pitch size is called environmental; drills without opponents are recommended.

### 4. Coaching the session
**Must hear:** seven intervention types; 40 interventions in 18 minutes; counts 9/8/7/6/5/4/1; 2.2 per minute; 12% questions (4 of 34); 6 to 8 specific vs general; 2.8 stoppages per 10 minutes; flags are prompts, not rules; rubric criteria are placeholders until the official rubric arrives.
**Reject if:** any count or ratio changes; flags are presented as official standards or thresholds; the rubric is presented as U.S. Soccer's.

### 5. Coaching games
**Must hear:** model vs plan; three key messages against Westside; short pre-agreed cues; half-time 0:00–1:00 settle, 1:00–2:30 two or three points, 2:30–3:00 one message; "win it back in five seconds"; brief after the whistle, detail at the next session; 6 of 41 vs 30% target; review becomes next session.
**Reject if:** half-time timings change; more than three key messages are recommended; immediate detailed criticism is recommended.

### 6. Developing players
**Must hear:** four corners incl. psychosocial; Marcus's four targets; targets built into team training; SMART, agreed with the player; PHV ages (13.5–14 boys, 11.5–12 girls, wide variation); relative age effect; bio-banding; growth-related pain: manage load and refer; Leo's monthly check-in.
**Reject if:** PHV ages change; medical diagnosis or treatment advice is added; late maturers are described as less talented.

### 7. Performance analysis
**Must hear:** KPI measures one principle; four KPIs with definitions, results (15%, 14, 5, 11.2) and targets (30%, 20, 8, under 9); PPDA definition and "lower is more intense"; define, code, read the trend, change training; inter-rater reliability; process vs outcome.
**Reject if:** any figure changes; PPDA direction is reversed; possession % is recommended as a KPI; figures are presented as real match data.

### 8. Assessment readiness
**Must hear:** four pieces of evidence per competency; context, decision, evidence, change; the week-7 example with 2.8 stoppages, 12% questions and 24% next match; three mistakes; playing career as a resource; official rubric replaces placeholders.
**Reject if:** the example's numbers change; specific assessor scoring criteria are invented; the answer shape is presented as an official U.S. Soccer format.
