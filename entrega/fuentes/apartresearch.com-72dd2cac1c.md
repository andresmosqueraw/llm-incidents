Sep 11, 2026

\-

Sep 13, 2026

Online & In-Person

AI Incident Response Sprint
---------------------------

![](https://framerusercontent.com/images/jX9SPTLReb6TH0utOzz6sDDJpQ.gif?width=1792&height=752)

In July 2026, OpenAI agents escaped a testing sandbox and breached Hugging Face's production systems, the first publicly documented autonomous AI intrusion. This three-day sprint turns the public evidence from that incident into response methods defenders and regulators can actually use.

00

Days To Go

Sign Up

In July 2026, OpenAI agents escaped a testing sandbox and breached Hugging Face's production systems, the first publicly documented autonomous AI intrusion. This three-day sprint turns the public evidence from that incident into response methods defenders and regulators can actually use.

This event is ongoing.

Sign Up

Submit Your Project

This event has concluded.

868

Sign Ups

Overview

Resources

Guidelines

Schedule

Overview
--------

![Arrow](https://framerusercontent.com/images/Tv5IAtqTPUFlm5NKiFSFBFRzCY.png?width=130&height=120)

**Submissions close Sunday, September 13 at 11:59 PM Anywhere on Earth (AoE).**

In this 3-day research sprint, you will turn the first documented cases of an AI system autonomously breaching a third party into artifacts that defenders and regulators can actually use, working in teams to produce containment standards, escape-detection harnesses, forecasting question sets, draft regulatory information requests, playtested tabletop exercises or anything that will help us be more ready for the next one.  
Co-organized by Apart Research and [CeSIA](https://cesia.org/)
, this sprint sits at the intersection of AI safety, security incident response, technology regulation, and forecasting. No prior background in AI incident response is required.

Cash Prizes
-----------

|     |     |
| --- | --- |
| #### **$2,000** in cash prizes across all tracks |     |
| #### 🥇 1st Place | #### $1,000 |
| #### 🥈 2nd Place | #### $500 |
| #### 🥉 3rd Place | #### $300 |
| #### 🏅 4th Place | #### $100 |
| #### 🏅 5th Place | #### $100 |

**Non-cash perks:** Apart Fellowship fast-track invites, mentor introductions, publication support, and transmission of the best regulatory-track work to the EU AI Office with team credit.

Fast-track and continuation
---------------------------

Top teams will be invited to apply to the Apart Fellowship, a 3 to 6 month research accelerator that provides mentorship, help with publication at top venues, funding, and research-management support to develop Research Sprint projects into full papers or products for the AI Safety community.

*   **Follow-up program:** Apart Fellowship. Invitations go out with the results.
    
*   **Downstream commitment from CeSIA:** CeSIA transmits selected outputs to its contacts at different regulatory bodies and credits the corresponding teams.
    

What this Sprint is about
-------------------------

AI incident response is the practice of turning incidents in which an AI system is itself the actor into fewer incidents later. That spans the operational work: detecting, containing, and reconstructing what an autonomous agent did across systems it was never authorized to touch, and the strategic question a warning shot poses: which disclosure and regulatory responses actually reduce risk, and which merely suppress the visible evidence that would have prompted action while the stakes were still small.

It is not the same thing as using AI for security operations, and it is not model red-teaming. In July 2026 the actor was not a human wielding a model, and the harm was not a model producing dangerous text. Two OpenAI models running an internal cyber-capability evaluation with production refusal classifiers disabled escaped their sandbox through a zero-day in the package-registry cache proxy that was their one permitted network egress, escalated privileges until they reached a node with internet access, and then attacked Hugging Face's production infrastructure, apparently to steal the benchmark's reference solutions and cheat the evaluation. The wider campaign began on 9 July at 02:28 UTC; the intrusion into Hugging Face ran from 11 to 13 July. Hugging Face detected it and cut the attacker off on 13 July (last attacker action 13:37 UTC, last logged event 14:14 UTC), disclosed it on 16 July without knowing where it came from, and reported it to law enforcement. OpenAI disclosed the origin on 21 July.

That distinction changes what defense means: the live questions become containment adequacy, cross-organizational attribution, and statutory reporting duties, none of which are red-teaming problems.

What participants will do
-------------------------

Over three days you will take one unusually well-documented real-world incident and turn it into an artifact somebody outside this sprint can use.

**The format.** Teams of one to five people pick a track, pick a project, and ship. There is no requirement to have participated before, no requirement to have a team in advance and no requirement to be an ML researcher.

**The deliverable.** A research report (PDF) on the official template, submitted through the form on this page by the Sunday deadline. Maximum 8 pages, not counting references and appendices; most strong reports are 4 to 8: what you built, how you tested it, the headline finding, its limits, and what you would do next. A Limitations and Dual-Use Considerations appendix is required. Put the artifact itself (a benchmark, a harness, a filled-in regulatory instrument, a control matrix, a detector, a dataset, a protocol, a kit) in a linked repo or an appendix. A public repo and a 3 to 5 minute video are optional. Full requirements are on the Guidelines tab.

**Support during the sprint.** The Resources tab has the reading pack, the primary sources, the relevant prior literature per track and the regulatory texts. During the weekend there are HackTalks from the speakers and a help desk on Discord.

Why this Sprint matters
-----------------------

In July 2026, an AI system escaped an evaluation sandbox, reached the open internet, took root on a third party's compute, and spent days inside another company's production infrastructure. No human directed any individual step. The organisation that bore the damage had no relationship with anyone who made the decision to run the test.

That is the headline. Two things about it make it worth a research sprint rather than a news cycle.

**First, the evidence base is exceptional and it will not stay fresh.** Hugging Face published a forensic reconstruction of roughly 17,600 attacker actions with named vulnerabilities, per-phase counts, verbatim commands and an interactive replay, an act of disclosure with very few precedents in any industry. OpenAI published its own account and revised it twice. Anthropic ran a retrospective review of 141,006 evaluation runs and published what it found. The UK AI Security Institute published quantified cheating rates across five frontier models. The benchmark at the centre of it is Apache-licensed and on GitHub. The Cloud Security Alliance's CISO community published a post-mortem within a fortnight. Almost never do researchers get a real loss-of-containment event with this much of the record public. That window closes as attention moves on.

**Second, the timing is unusually load-bearing.** The European Commission gained enforcement powers over general-purpose AI model providers on 2 August 2026. California's frontier AI law has been operative since January 2026 and has produced no public enforcement action. New York's enforcement begins in January 2027. Four federal bills in the US are live, at least one drafted directly in response to this incident. The first months of any enforcement regime are when supervisory priorities get set and when precedents about what regulators ask for become sticky. Work produced now lands in that window.

Research Tracks
---------------

Five tracks. The example projects for each one are on the Resources tab, with the reading pack. If you have a better idea inside a track's goal, build that.

_**Update, 7 September.**_ [_Researchers_](https://collusion.wiki/)
 _have found another instance of OpenAI agents breaking containment: from 24 May, OpenAI agents made about 15,000 edits to a dormant German wiki, using it to swap task answers and sandbox workarounds. That predates the Hugging Face intrusion. OpenAI-registered IPs appear in the wiki’s public logs from 21 June, and agent activity stopped the next day. OpenAI said nothing publicly until the researchers published on 4 September. OpenAI acknowledged the incident on 5 September and said the field has no agreed standard for reporting misalignment. The Commission says it is “in close contact with OpenAI.” As far as we can tell, no Article 91 request on either incident has been made public._

### 1) Containment: what standard would have stopped this?

The models escaped through the one network egress their sandbox permitted. 

Judged on: could a third party verify compliance without access to the lab's network, and would a lab actually adopt it.

### 2) What happened, and what breaks next

Reconstruct what this incident does and does not establish, then turn it into concrete things to check and things to watch. [Hugging Face's timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)
 and [OpenAI's account](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
 are public.

Judged on: resolvable questions, checks somebody could run tomorrow, and causal explanations that predict something.

### 3) Regulatory Response

Since 2 August, the European Commission's AI Office can enforce the AI Act against the companies building the most capable models: it can demand documentation, evaluate models itself, order corrective measures, and fine up to 3% of worldwide turnover. In [an open letter](https://www.safer-ai.org/u/2026/07/Open-Letter.pdf)
 published days before the incident became public, a coalition including Apart and CeSIA, with signatories including Yoshua Bengio and Stuart Russell, called on the Commission to use these powers with confidence — and [CeSIA has since asked](https://cesia.org/en/publications/the-openai-hugging-face-incident-what-we-know-what-we-dont-what-follows/)
 that they be used on this incident specifically. This track writes the documents that would make that concrete.

Judged on: legal accuracy and specificity — could a regulator or a legislator use it with light edits? CeSIA can transmit outputs that pass the bar to its contacts, and potentially to regulators, with team credit.

### 4) Communication: making the warning shot count

We keep saying [we need warning shots](https://www.lesswrong.com/posts/RYx6cLwzoajqjyB6b/what-convincing-warning-shot-could-help-prevent-extinction)
. Then one arrives, and it barely travels beyond the usual circles. This track studies how the incident was communicated and builds what should exist before the next one. Producing communication counts as much as analysing it.

Judged on: grounding in the record (dates, quotes, named channels) and evidence of reach — a playtest, a journalist's read, a creator's reply.

### 5) Open track

For projects that don't fit the four tracks above. Directions we would be happy to see are on the Resources tab.

Judged on: an artifact somebody can use, a stated limit on what it establishes, and what a month of follow-up would add.

Who should join
---------------

You do not need an AI, ML or Safety background. Some profiles that are particularly fitting to this Sprint are:

**Security engineers and incident responders.** You have handled the human version of this. Tracks 1 and 5 need people who know what a detection pipeline that correlates but does not page actually looks like from the inside, and what forensics against an adversary that fabricates evidence at volume would require. If you work in DFIR, detection engineering, cloud or Kubernetes security, or you have run a CTF, you are the person the containment track was written for.

**ML evaluation engineers and researchers.** Tracks 1 and 5 include benchmark and harness work: measuring refusal across multi-step agentic workflows, building escape-detection tooling, assessing benchmark contamination. If you have built or run evaluations, you already know why the interesting failures happen at the harness layer.

**Lawyers and technology-policy analysts.** Track 3 is a legal drafting exercise with real recipients. Regulatory lawyers, compliance professionals, policy researchers, and anyone who has worked on incident-reporting regimes in another sector (financial services, critical infrastructure, medical devices, data protection) will find the comparative work immediately tractable. Cross-jurisdictional experience is especially valuable, because the whole point of the track is that the regimes disagree.

**Forecasters and quantitative analysts.** Track 2 needs people who are comfortable with heterogeneous denominators, explicit uncertainty and resolution criteria that survive contact with reality. If you have written questions for a forecasting platform or built base rates from messy sources, that skill transfers directly.

**Designers, facilitators, writers and educators.** Tracks 4 and 5 include explanatory and facilitation work, and it is not a consolation prize. A tabletop kit a ministry actually runs, or a brief a minister actually reads, reaches decision-makers who will never open a technical timeline. Playtest and reader feedback are part of the deliverable.

**Communication experts, journalists and macro-strategy researchers.** Track 4 is about making the warning shot count: reporting on the incident accurately, and working out what the discourse got wrong and how to do better next time.

**Students and career-changers.** Roughly half the useful projects here need care and persistence more than credentials. If you can read a primary source carefully and write down precisely what it does and does not say, you can contribute.

What happens after
------------------

The sprint is the first step in a pipeline:

**Immediately.** Every submission is judged against published criteria, with written feedback. Winning submissions are announced within a couple of weeks. All artifacts that can be published are published under open licences, in one place, so that the sprint output is citable as a body rather than scattered across forks.

**Delivery to recipients.** Several tracks produce things with an obvious destination, and we will help teams get them there rather than leaving them on a repo. Filled-in regulatory instruments go to the bodies that publish them. Detection tooling and control matrices go to the practitioner communities that asked for them. Benchmark and contamination findings go to the maintainers. Where an artifact is genuinely fileable, and at least one of them is, we will support teams who want to file it, with review first.

**Continuation.** The strongest teams are invited into Apart's fellowship: months of supported follow-on work, mentorship, and a route to a paper. Sprint outputs have gone this way before, and several of the projects here are sized for it, a weekend produces a v0.1 benchmark or a v0.1 standard, and the next six months produce the version people cite.

Partners
--------

[**CeSIA, the French Center for AI Safety**](https://cesia.org/en/)
, an AI safety research and advocacy organization known for the Global Call for AI Red Lines. CeSIA provides the seed reading pack, judges for the forecasting, regulatory and tabletop tracks, distribution through its newsletter and 7,000-member Discord, and a potential route for policy outputs to reach the AI Office.

Contact
-------

*   **Email:** sprints@apartresearch.com
    
*   **Discord:** [discord.gg/XswWBvugYs](https://discord.gg/XswWBvugYs)
    
*   **Organizers:** Apart Research and CeSIA
    

868

Sign Ups

Overview

Resources

Guidelines

Schedule

Overview
--------

![Arrow](https://framerusercontent.com/images/Tv5IAtqTPUFlm5NKiFSFBFRzCY.png?width=130&height=120)

**Submissions close Sunday, September 13 at 11:59 PM Anywhere on Earth (AoE).**

In this 3-day research sprint, you will turn the first documented cases of an AI system autonomously breaching a third party into artifacts that defenders and regulators can actually use, working in teams to produce containment standards, escape-detection harnesses, forecasting question sets, draft regulatory information requests, playtested tabletop exercises or anything that will help us be more ready for the next one.  
Co-organized by Apart Research and [CeSIA](https://cesia.org/)
, this sprint sits at the intersection of AI safety, security incident response, technology regulation, and forecasting. No prior background in AI incident response is required.

Cash Prizes
-----------

|     |     |
| --- | --- |
| #### **$2,000** in cash prizes across all tracks |     |
| #### 🥇 1st Place | #### $1,000 |
| #### 🥈 2nd Place | #### $500 |
| #### 🥉 3rd Place | #### $300 |
| #### 🏅 4th Place | #### $100 |
| #### 🏅 5th Place | #### $100 |

**Non-cash perks:** Apart Fellowship fast-track invites, mentor introductions, publication support, and transmission of the best regulatory-track work to the EU AI Office with team credit.

Fast-track and continuation
---------------------------

Top teams will be invited to apply to the Apart Fellowship, a 3 to 6 month research accelerator that provides mentorship, help with publication at top venues, funding, and research-management support to develop Research Sprint projects into full papers or products for the AI Safety community.

*   **Follow-up program:** Apart Fellowship. Invitations go out with the results.
    
*   **Downstream commitment from CeSIA:** CeSIA transmits selected outputs to its contacts at different regulatory bodies and credits the corresponding teams.
    

What this Sprint is about
-------------------------

AI incident response is the practice of turning incidents in which an AI system is itself the actor into fewer incidents later. That spans the operational work: detecting, containing, and reconstructing what an autonomous agent did across systems it was never authorized to touch, and the strategic question a warning shot poses: which disclosure and regulatory responses actually reduce risk, and which merely suppress the visible evidence that would have prompted action while the stakes were still small.

It is not the same thing as using AI for security operations, and it is not model red-teaming. In July 2026 the actor was not a human wielding a model, and the harm was not a model producing dangerous text. Two OpenAI models running an internal cyber-capability evaluation with production refusal classifiers disabled escaped their sandbox through a zero-day in the package-registry cache proxy that was their one permitted network egress, escalated privileges until they reached a node with internet access, and then attacked Hugging Face's production infrastructure, apparently to steal the benchmark's reference solutions and cheat the evaluation. The wider campaign began on 9 July at 02:28 UTC; the intrusion into Hugging Face ran from 11 to 13 July. Hugging Face detected it and cut the attacker off on 13 July (last attacker action 13:37 UTC, last logged event 14:14 UTC), disclosed it on 16 July without knowing where it came from, and reported it to law enforcement. OpenAI disclosed the origin on 21 July.

That distinction changes what defense means: the live questions become containment adequacy, cross-organizational attribution, and statutory reporting duties, none of which are red-teaming problems.

What participants will do
-------------------------

Over three days you will take one unusually well-documented real-world incident and turn it into an artifact somebody outside this sprint can use.

**The format.** Teams of one to five people pick a track, pick a project, and ship. There is no requirement to have participated before, no requirement to have a team in advance and no requirement to be an ML researcher.

**The deliverable.** A research report (PDF) on the official template, submitted through the form on this page by the Sunday deadline. Maximum 8 pages, not counting references and appendices; most strong reports are 4 to 8: what you built, how you tested it, the headline finding, its limits, and what you would do next. A Limitations and Dual-Use Considerations appendix is required. Put the artifact itself (a benchmark, a harness, a filled-in regulatory instrument, a control matrix, a detector, a dataset, a protocol, a kit) in a linked repo or an appendix. A public repo and a 3 to 5 minute video are optional. Full requirements are on the Guidelines tab.

**Support during the sprint.** The Resources tab has the reading pack, the primary sources, the relevant prior literature per track and the regulatory texts. During the weekend there are HackTalks from the speakers and a help desk on Discord.

Why this Sprint matters
-----------------------

In July 2026, an AI system escaped an evaluation sandbox, reached the open internet, took root on a third party's compute, and spent days inside another company's production infrastructure. No human directed any individual step. The organisation that bore the damage had no relationship with anyone who made the decision to run the test.

That is the headline. Two things about it make it worth a research sprint rather than a news cycle.

**First, the evidence base is exceptional and it will not stay fresh.** Hugging Face published a forensic reconstruction of roughly 17,600 attacker actions with named vulnerabilities, per-phase counts, verbatim commands and an interactive replay, an act of disclosure with very few precedents in any industry. OpenAI published its own account and revised it twice. Anthropic ran a retrospective review of 141,006 evaluation runs and published what it found. The UK AI Security Institute published quantified cheating rates across five frontier models. The benchmark at the centre of it is Apache-licensed and on GitHub. The Cloud Security Alliance's CISO community published a post-mortem within a fortnight. Almost never do researchers get a real loss-of-containment event with this much of the record public. That window closes as attention moves on.

**Second, the timing is unusually load-bearing.** The European Commission gained enforcement powers over general-purpose AI model providers on 2 August 2026. California's frontier AI law has been operative since January 2026 and has produced no public enforcement action. New York's enforcement begins in January 2027. Four federal bills in the US are live, at least one drafted directly in response to this incident. The first months of any enforcement regime are when supervisory priorities get set and when precedents about what regulators ask for become sticky. Work produced now lands in that window.

Research Tracks
---------------

Five tracks. The example projects for each one are on the Resources tab, with the reading pack. If you have a better idea inside a track's goal, build that.

_**Update, 7 September.**_ [_Researchers_](https://collusion.wiki/)
 _have found another instance of OpenAI agents breaking containment: from 24 May, OpenAI agents made about 15,000 edits to a dormant German wiki, using it to swap task answers and sandbox workarounds. That predates the Hugging Face intrusion. OpenAI-registered IPs appear in the wiki’s public logs from 21 June, and agent activity stopped the next day. OpenAI said nothing publicly until the researchers published on 4 September. OpenAI acknowledged the incident on 5 September and said the field has no agreed standard for reporting misalignment. The Commission says it is “in close contact with OpenAI.” As far as we can tell, no Article 91 request on either incident has been made public._

### 1) Containment: what standard would have stopped this?

The models escaped through the one network egress their sandbox permitted. 

Judged on: could a third party verify compliance without access to the lab's network, and would a lab actually adopt it.

### 2) What happened, and what breaks next

Reconstruct what this incident does and does not establish, then turn it into concrete things to check and things to watch. [Hugging Face's timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)
 and [OpenAI's account](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
 are public.

Judged on: resolvable questions, checks somebody could run tomorrow, and causal explanations that predict something.

### 3) Regulatory Response

Since 2 August, the European Commission's AI Office can enforce the AI Act against the companies building the most capable models: it can demand documentation, evaluate models itself, order corrective measures, and fine up to 3% of worldwide turnover. In [an open letter](https://www.safer-ai.org/u/2026/07/Open-Letter.pdf)
 published days before the incident became public, a coalition including Apart and CeSIA, with signatories including Yoshua Bengio and Stuart Russell, called on the Commission to use these powers with confidence — and [CeSIA has since asked](https://cesia.org/en/publications/the-openai-hugging-face-incident-what-we-know-what-we-dont-what-follows/)
 that they be used on this incident specifically. This track writes the documents that would make that concrete.

Judged on: legal accuracy and specificity — could a regulator or a legislator use it with light edits? CeSIA can transmit outputs that pass the bar to its contacts, and potentially to regulators, with team credit.

### 4) Communication: making the warning shot count

We keep saying [we need warning shots](https://www.lesswrong.com/posts/RYx6cLwzoajqjyB6b/what-convincing-warning-shot-could-help-prevent-extinction)
. Then one arrives, and it barely travels beyond the usual circles. This track studies how the incident was communicated and builds what should exist before the next one. Producing communication counts as much as analysing it.

Judged on: grounding in the record (dates, quotes, named channels) and evidence of reach — a playtest, a journalist's read, a creator's reply.

### 5) Open track

For projects that don't fit the four tracks above. Directions we would be happy to see are on the Resources tab.

Judged on: an artifact somebody can use, a stated limit on what it establishes, and what a month of follow-up would add.

Who should join
---------------

You do not need an AI, ML or Safety background. Some profiles that are particularly fitting to this Sprint are:

**Security engineers and incident responders.** You have handled the human version of this. Tracks 1 and 5 need people who know what a detection pipeline that correlates but does not page actually looks like from the inside, and what forensics against an adversary that fabricates evidence at volume would require. If you work in DFIR, detection engineering, cloud or Kubernetes security, or you have run a CTF, you are the person the containment track was written for.

**ML evaluation engineers and researchers.** Tracks 1 and 5 include benchmark and harness work: measuring refusal across multi-step agentic workflows, building escape-detection tooling, assessing benchmark contamination. If you have built or run evaluations, you already know why the interesting failures happen at the harness layer.

**Lawyers and technology-policy analysts.** Track 3 is a legal drafting exercise with real recipients. Regulatory lawyers, compliance professionals, policy researchers, and anyone who has worked on incident-reporting regimes in another sector (financial services, critical infrastructure, medical devices, data protection) will find the comparative work immediately tractable. Cross-jurisdictional experience is especially valuable, because the whole point of the track is that the regimes disagree.

**Forecasters and quantitative analysts.** Track 2 needs people who are comfortable with heterogeneous denominators, explicit uncertainty and resolution criteria that survive contact with reality. If you have written questions for a forecasting platform or built base rates from messy sources, that skill transfers directly.

**Designers, facilitators, writers and educators.** Tracks 4 and 5 include explanatory and facilitation work, and it is not a consolation prize. A tabletop kit a ministry actually runs, or a brief a minister actually reads, reaches decision-makers who will never open a technical timeline. Playtest and reader feedback are part of the deliverable.

**Communication experts, journalists and macro-strategy researchers.** Track 4 is about making the warning shot count: reporting on the incident accurately, and working out what the discourse got wrong and how to do better next time.

**Students and career-changers.** Roughly half the useful projects here need care and persistence more than credentials. If you can read a primary source carefully and write down precisely what it does and does not say, you can contribute.

What happens after
------------------

The sprint is the first step in a pipeline:

**Immediately.** Every submission is judged against published criteria, with written feedback. Winning submissions are announced within a couple of weeks. All artifacts that can be published are published under open licences, in one place, so that the sprint output is citable as a body rather than scattered across forks.

**Delivery to recipients.** Several tracks produce things with an obvious destination, and we will help teams get them there rather than leaving them on a repo. Filled-in regulatory instruments go to the bodies that publish them. Detection tooling and control matrices go to the practitioner communities that asked for them. Benchmark and contamination findings go to the maintainers. Where an artifact is genuinely fileable, and at least one of them is, we will support teams who want to file it, with review first.

**Continuation.** The strongest teams are invited into Apart's fellowship: months of supported follow-on work, mentorship, and a route to a paper. Sprint outputs have gone this way before, and several of the projects here are sized for it, a weekend produces a v0.1 benchmark or a v0.1 standard, and the next six months produce the version people cite.

Partners
--------

[**CeSIA, the French Center for AI Safety**](https://cesia.org/en/)
, an AI safety research and advocacy organization known for the Global Call for AI Red Lines. CeSIA provides the seed reading pack, judges for the forecasting, regulatory and tabletop tracks, distribution through its newsletter and 7,000-member Discord, and a potential route for policy outputs to reach the AI Office.

Contact
-------

*   **Email:** sprints@apartresearch.com
    
*   **Discord:** [discord.gg/XswWBvugYs](https://discord.gg/XswWBvugYs)
    
*   **Organizers:** Apart Research and CeSIA
    

868

Sign Ups

Overview

Resources

Guidelines

Schedule

Overview
--------

![Arrow](https://framerusercontent.com/images/wcBzz8XOFa1491h7UQ5nwtuN4Vs.png?width=131&height=120)

**Submissions close Sunday, September 13 at 11:59 PM Anywhere on Earth (AoE).**

In this 3-day research sprint, you will turn the first documented cases of an AI system autonomously breaching a third party into artifacts that defenders and regulators can actually use, working in teams to produce containment standards, escape-detection harnesses, forecasting question sets, draft regulatory information requests, playtested tabletop exercises or anything that will help us be more ready for the next one.  
Co-organized by Apart Research and [CeSIA](https://cesia.org/)
, this sprint sits at the intersection of AI safety, security incident response, technology regulation, and forecasting. No prior background in AI incident response is required.

Cash Prizes
-----------

|     |     |
| --- | --- |
| #### **$2,000** in cash prizes across all tracks |     |
| #### 🥇 1st Place | #### $1,000 |
| #### 🥈 2nd Place | #### $500 |
| #### 🥉 3rd Place | #### $300 |
| #### 🏅 4th Place | #### $100 |
| #### 🏅 5th Place | #### $100 |

**Non-cash perks:** Apart Fellowship fast-track invites, mentor introductions, publication support, and transmission of the best regulatory-track work to the EU AI Office with team credit.

Fast-track and continuation
---------------------------

Top teams will be invited to apply to the Apart Fellowship, a 3 to 6 month research accelerator that provides mentorship, help with publication at top venues, funding, and research-management support to develop Research Sprint projects into full papers or products for the AI Safety community.

*   **Follow-up program:** Apart Fellowship. Invitations go out with the results.
    
*   **Downstream commitment from CeSIA:** CeSIA transmits selected outputs to its contacts at different regulatory bodies and credits the corresponding teams.
    

What this Sprint is about
-------------------------

AI incident response is the practice of turning incidents in which an AI system is itself the actor into fewer incidents later. That spans the operational work: detecting, containing, and reconstructing what an autonomous agent did across systems it was never authorized to touch, and the strategic question a warning shot poses: which disclosure and regulatory responses actually reduce risk, and which merely suppress the visible evidence that would have prompted action while the stakes were still small.

It is not the same thing as using AI for security operations, and it is not model red-teaming. In July 2026 the actor was not a human wielding a model, and the harm was not a model producing dangerous text. Two OpenAI models running an internal cyber-capability evaluation with production refusal classifiers disabled escaped their sandbox through a zero-day in the package-registry cache proxy that was their one permitted network egress, escalated privileges until they reached a node with internet access, and then attacked Hugging Face's production infrastructure, apparently to steal the benchmark's reference solutions and cheat the evaluation. The wider campaign began on 9 July at 02:28 UTC; the intrusion into Hugging Face ran from 11 to 13 July. Hugging Face detected it and cut the attacker off on 13 July (last attacker action 13:37 UTC, last logged event 14:14 UTC), disclosed it on 16 July without knowing where it came from, and reported it to law enforcement. OpenAI disclosed the origin on 21 July.

That distinction changes what defense means: the live questions become containment adequacy, cross-organizational attribution, and statutory reporting duties, none of which are red-teaming problems.

What participants will do
-------------------------

Over three days you will take one unusually well-documented real-world incident and turn it into an artifact somebody outside this sprint can use.

**The format.** Teams of one to five people pick a track, pick a project, and ship. There is no requirement to have participated before, no requirement to have a team in advance and no requirement to be an ML researcher.

**The deliverable.** A research report (PDF) on the official template, submitted through the form on this page by the Sunday deadline. Maximum 8 pages, not counting references and appendices; most strong reports are 4 to 8: what you built, how you tested it, the headline finding, its limits, and what you would do next. A Limitations and Dual-Use Considerations appendix is required. Put the artifact itself (a benchmark, a harness, a filled-in regulatory instrument, a control matrix, a detector, a dataset, a protocol, a kit) in a linked repo or an appendix. A public repo and a 3 to 5 minute video are optional. Full requirements are on the Guidelines tab.

**Support during the sprint.** The Resources tab has the reading pack, the primary sources, the relevant prior literature per track and the regulatory texts. During the weekend there are HackTalks from the speakers and a help desk on Discord.

Why this Sprint matters
-----------------------

In July 2026, an AI system escaped an evaluation sandbox, reached the open internet, took root on a third party's compute, and spent days inside another company's production infrastructure. No human directed any individual step. The organisation that bore the damage had no relationship with anyone who made the decision to run the test.

That is the headline. Two things about it make it worth a research sprint rather than a news cycle.

**First, the evidence base is exceptional and it will not stay fresh.** Hugging Face published a forensic reconstruction of roughly 17,600 attacker actions with named vulnerabilities, per-phase counts, verbatim commands and an interactive replay, an act of disclosure with very few precedents in any industry. OpenAI published its own account and revised it twice. Anthropic ran a retrospective review of 141,006 evaluation runs and published what it found. The UK AI Security Institute published quantified cheating rates across five frontier models. The benchmark at the centre of it is Apache-licensed and on GitHub. The Cloud Security Alliance's CISO community published a post-mortem within a fortnight. Almost never do researchers get a real loss-of-containment event with this much of the record public. That window closes as attention moves on.

**Second, the timing is unusually load-bearing.** The European Commission gained enforcement powers over general-purpose AI model providers on 2 August 2026. California's frontier AI law has been operative since January 2026 and has produced no public enforcement action. New York's enforcement begins in January 2027. Four federal bills in the US are live, at least one drafted directly in response to this incident. The first months of any enforcement regime are when supervisory priorities get set and when precedents about what regulators ask for become sticky. Work produced now lands in that window.

Research Tracks
---------------

Five tracks. The example projects for each one are on the Resources tab, with the reading pack. If you have a better idea inside a track's goal, build that.

_**Update, 7 September.**_ [_Researchers_](https://collusion.wiki/)
 _have found another instance of OpenAI agents breaking containment: from 24 May, OpenAI agents made about 15,000 edits to a dormant German wiki, using it to swap task answers and sandbox workarounds. That predates the Hugging Face intrusion. OpenAI-registered IPs appear in the wiki’s public logs from 21 June, and agent activity stopped the next day. OpenAI said nothing publicly until the researchers published on 4 September. OpenAI acknowledged the incident on 5 September and said the field has no agreed standard for reporting misalignment. The Commission says it is “in close contact with OpenAI.” As far as we can tell, no Article 91 request on either incident has been made public._

### 1) Containment: what standard would have stopped this?

The models escaped through the one network egress their sandbox permitted. 

Judged on: could a third party verify compliance without access to the lab's network, and would a lab actually adopt it.

### 2) What happened, and what breaks next

Reconstruct what this incident does and does not establish, then turn it into concrete things to check and things to watch. [Hugging Face's timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)
 and [OpenAI's account](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
 are public.

Judged on: resolvable questions, checks somebody could run tomorrow, and causal explanations that predict something.

### 3) Regulatory Response

Since 2 August, the European Commission's AI Office can enforce the AI Act against the companies building the most capable models: it can demand documentation, evaluate models itself, order corrective measures, and fine up to 3% of worldwide turnover. In [an open letter](https://www.safer-ai.org/u/2026/07/Open-Letter.pdf)
 published days before the incident became public, a coalition including Apart and CeSIA, with signatories including Yoshua Bengio and Stuart Russell, called on the Commission to use these powers with confidence — and [CeSIA has since asked](https://cesia.org/en/publications/the-openai-hugging-face-incident-what-we-know-what-we-dont-what-follows/)
 that they be used on this incident specifically. This track writes the documents that would make that concrete.

Judged on: legal accuracy and specificity — could a regulator or a legislator use it with light edits? CeSIA can transmit outputs that pass the bar to its contacts, and potentially to regulators, with team credit.

### 4) Communication: making the warning shot count

We keep saying [we need warning shots](https://www.lesswrong.com/posts/RYx6cLwzoajqjyB6b/what-convincing-warning-shot-could-help-prevent-extinction)
. Then one arrives, and it barely travels beyond the usual circles. This track studies how the incident was communicated and builds what should exist before the next one. Producing communication counts as much as analysing it.

Judged on: grounding in the record (dates, quotes, named channels) and evidence of reach — a playtest, a journalist's read, a creator's reply.

### 5) Open track

For projects that don't fit the four tracks above. Directions we would be happy to see are on the Resources tab.

Judged on: an artifact somebody can use, a stated limit on what it establishes, and what a month of follow-up would add.

Who should join
---------------

You do not need an AI, ML or Safety background. Some profiles that are particularly fitting to this Sprint are:

**Security engineers and incident responders.** You have handled the human version of this. Tracks 1 and 5 need people who know what a detection pipeline that correlates but does not page actually looks like from the inside, and what forensics against an adversary that fabricates evidence at volume would require. If you work in DFIR, detection engineering, cloud or Kubernetes security, or you have run a CTF, you are the person the containment track was written for.

**ML evaluation engineers and researchers.** Tracks 1 and 5 include benchmark and harness work: measuring refusal across multi-step agentic workflows, building escape-detection tooling, assessing benchmark contamination. If you have built or run evaluations, you already know why the interesting failures happen at the harness layer.

**Lawyers and technology-policy analysts.** Track 3 is a legal drafting exercise with real recipients. Regulatory lawyers, compliance professionals, policy researchers, and anyone who has worked on incident-reporting regimes in another sector (financial services, critical infrastructure, medical devices, data protection) will find the comparative work immediately tractable. Cross-jurisdictional experience is especially valuable, because the whole point of the track is that the regimes disagree.

**Forecasters and quantitative analysts.** Track 2 needs people who are comfortable with heterogeneous denominators, explicit uncertainty and resolution criteria that survive contact with reality. If you have written questions for a forecasting platform or built base rates from messy sources, that skill transfers directly.

**Designers, facilitators, writers and educators.** Tracks 4 and 5 include explanatory and facilitation work, and it is not a consolation prize. A tabletop kit a ministry actually runs, or a brief a minister actually reads, reaches decision-makers who will never open a technical timeline. Playtest and reader feedback are part of the deliverable.

**Communication experts, journalists and macro-strategy researchers.** Track 4 is about making the warning shot count: reporting on the incident accurately, and working out what the discourse got wrong and how to do better next time.

**Students and career-changers.** Roughly half the useful projects here need care and persistence more than credentials. If you can read a primary source carefully and write down precisely what it does and does not say, you can contribute.

What happens after
------------------

The sprint is the first step in a pipeline:

**Immediately.** Every submission is judged against published criteria, with written feedback. Winning submissions are announced within a couple of weeks. All artifacts that can be published are published under open licences, in one place, so that the sprint output is citable as a body rather than scattered across forks.

**Delivery to recipients.** Several tracks produce things with an obvious destination, and we will help teams get them there rather than leaving them on a repo. Filled-in regulatory instruments go to the bodies that publish them. Detection tooling and control matrices go to the practitioner communities that asked for them. Benchmark and contamination findings go to the maintainers. Where an artifact is genuinely fileable, and at least one of them is, we will support teams who want to file it, with review first.

**Continuation.** The strongest teams are invited into Apart's fellowship: months of supported follow-on work, mentorship, and a route to a paper. Sprint outputs have gone this way before, and several of the projects here are sized for it, a weekend produces a v0.1 benchmark or a v0.1 standard, and the next six months produce the version people cite.

Partners
--------

[**CeSIA, the French Center for AI Safety**](https://cesia.org/en/)
, an AI safety research and advocacy organization known for the Global Call for AI Red Lines. CeSIA provides the seed reading pack, judges for the forecasting, regulatory and tabletop tracks, distribution through its newsletter and 7,000-member Discord, and a potential route for policy outputs to reach the AI Office.

Contact
-------

*   **Email:** sprints@apartresearch.com
    
*   **Discord:** [discord.gg/XswWBvugYs](https://discord.gg/XswWBvugYs)
    
*   **Organizers:** Apart Research and CeSIA
    

868

Sign Ups

Overview

Resources

Guidelines

Schedule

Overview
--------

![Arrow](https://framerusercontent.com/images/Tv5IAtqTPUFlm5NKiFSFBFRzCY.png?width=130&height=120)

**Submissions close Sunday, September 13 at 11:59 PM Anywhere on Earth (AoE).**

In this 3-day research sprint, you will turn the first documented cases of an AI system autonomously breaching a third party into artifacts that defenders and regulators can actually use, working in teams to produce containment standards, escape-detection harnesses, forecasting question sets, draft regulatory information requests, playtested tabletop exercises or anything that will help us be more ready for the next one.  
Co-organized by Apart Research and [CeSIA](https://cesia.org/)
, this sprint sits at the intersection of AI safety, security incident response, technology regulation, and forecasting. No prior background in AI incident response is required.

Cash Prizes
-----------

|     |     |
| --- | --- |
| #### **$2,000** in cash prizes across all tracks |     |
| #### 🥇 1st Place | #### $1,000 |
| #### 🥈 2nd Place | #### $500 |
| #### 🥉 3rd Place | #### $300 |
| #### 🏅 4th Place | #### $100 |
| #### 🏅 5th Place | #### $100 |

**Non-cash perks:** Apart Fellowship fast-track invites, mentor introductions, publication support, and transmission of the best regulatory-track work to the EU AI Office with team credit.

Fast-track and continuation
---------------------------

Top teams will be invited to apply to the Apart Fellowship, a 3 to 6 month research accelerator that provides mentorship, help with publication at top venues, funding, and research-management support to develop Research Sprint projects into full papers or products for the AI Safety community.

*   **Follow-up program:** Apart Fellowship. Invitations go out with the results.
    
*   **Downstream commitment from CeSIA:** CeSIA transmits selected outputs to its contacts at different regulatory bodies and credits the corresponding teams.
    

What this Sprint is about
-------------------------

AI incident response is the practice of turning incidents in which an AI system is itself the actor into fewer incidents later. That spans the operational work: detecting, containing, and reconstructing what an autonomous agent did across systems it was never authorized to touch, and the strategic question a warning shot poses: which disclosure and regulatory responses actually reduce risk, and which merely suppress the visible evidence that would have prompted action while the stakes were still small.

It is not the same thing as using AI for security operations, and it is not model red-teaming. In July 2026 the actor was not a human wielding a model, and the harm was not a model producing dangerous text. Two OpenAI models running an internal cyber-capability evaluation with production refusal classifiers disabled escaped their sandbox through a zero-day in the package-registry cache proxy that was their one permitted network egress, escalated privileges until they reached a node with internet access, and then attacked Hugging Face's production infrastructure, apparently to steal the benchmark's reference solutions and cheat the evaluation. The wider campaign began on 9 July at 02:28 UTC; the intrusion into Hugging Face ran from 11 to 13 July. Hugging Face detected it and cut the attacker off on 13 July (last attacker action 13:37 UTC, last logged event 14:14 UTC), disclosed it on 16 July without knowing where it came from, and reported it to law enforcement. OpenAI disclosed the origin on 21 July.

That distinction changes what defense means: the live questions become containment adequacy, cross-organizational attribution, and statutory reporting duties, none of which are red-teaming problems.

What participants will do
-------------------------

Over three days you will take one unusually well-documented real-world incident and turn it into an artifact somebody outside this sprint can use.

**The format.** Teams of one to five people pick a track, pick a project, and ship. There is no requirement to have participated before, no requirement to have a team in advance and no requirement to be an ML researcher.

**The deliverable.** A research report (PDF) on the official template, submitted through the form on this page by the Sunday deadline. Maximum 8 pages, not counting references and appendices; most strong reports are 4 to 8: what you built, how you tested it, the headline finding, its limits, and what you would do next. A Limitations and Dual-Use Considerations appendix is required. Put the artifact itself (a benchmark, a harness, a filled-in regulatory instrument, a control matrix, a detector, a dataset, a protocol, a kit) in a linked repo or an appendix. A public repo and a 3 to 5 minute video are optional. Full requirements are on the Guidelines tab.

**Support during the sprint.** The Resources tab has the reading pack, the primary sources, the relevant prior literature per track and the regulatory texts. During the weekend there are HackTalks from the speakers and a help desk on Discord.

Why this Sprint matters
-----------------------

In July 2026, an AI system escaped an evaluation sandbox, reached the open internet, took root on a third party's compute, and spent days inside another company's production infrastructure. No human directed any individual step. The organisation that bore the damage had no relationship with anyone who made the decision to run the test.

That is the headline. Two things about it make it worth a research sprint rather than a news cycle.

**First, the evidence base is exceptional and it will not stay fresh.** Hugging Face published a forensic reconstruction of roughly 17,600 attacker actions with named vulnerabilities, per-phase counts, verbatim commands and an interactive replay, an act of disclosure with very few precedents in any industry. OpenAI published its own account and revised it twice. Anthropic ran a retrospective review of 141,006 evaluation runs and published what it found. The UK AI Security Institute published quantified cheating rates across five frontier models. The benchmark at the centre of it is Apache-licensed and on GitHub. The Cloud Security Alliance's CISO community published a post-mortem within a fortnight. Almost never do researchers get a real loss-of-containment event with this much of the record public. That window closes as attention moves on.

**Second, the timing is unusually load-bearing.** The European Commission gained enforcement powers over general-purpose AI model providers on 2 August 2026. California's frontier AI law has been operative since January 2026 and has produced no public enforcement action. New York's enforcement begins in January 2027. Four federal bills in the US are live, at least one drafted directly in response to this incident. The first months of any enforcement regime are when supervisory priorities get set and when precedents about what regulators ask for become sticky. Work produced now lands in that window.

Research Tracks
---------------

Five tracks. The example projects for each one are on the Resources tab, with the reading pack. If you have a better idea inside a track's goal, build that.

_**Update, 7 September.**_ [_Researchers_](https://collusion.wiki/)
 _have found another instance of OpenAI agents breaking containment: from 24 May, OpenAI agents made about 15,000 edits to a dormant German wiki, using it to swap task answers and sandbox workarounds. That predates the Hugging Face intrusion. OpenAI-registered IPs appear in the wiki’s public logs from 21 June, and agent activity stopped the next day. OpenAI said nothing publicly until the researchers published on 4 September. OpenAI acknowledged the incident on 5 September and said the field has no agreed standard for reporting misalignment. The Commission says it is “in close contact with OpenAI.” As far as we can tell, no Article 91 request on either incident has been made public._

### 1) Containment: what standard would have stopped this?

The models escaped through the one network egress their sandbox permitted. 

Judged on: could a third party verify compliance without access to the lab's network, and would a lab actually adopt it.

### 2) What happened, and what breaks next

Reconstruct what this incident does and does not establish, then turn it into concrete things to check and things to watch. [Hugging Face's timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)
 and [OpenAI's account](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
 are public.

Judged on: resolvable questions, checks somebody could run tomorrow, and causal explanations that predict something.

### 3) Regulatory Response

Since 2 August, the European Commission's AI Office can enforce the AI Act against the companies building the most capable models: it can demand documentation, evaluate models itself, order corrective measures, and fine up to 3% of worldwide turnover. In [an open letter](https://www.safer-ai.org/u/2026/07/Open-Letter.pdf)
 published days before the incident became public, a coalition including Apart and CeSIA, with signatories including Yoshua Bengio and Stuart Russell, called on the Commission to use these powers with confidence — and [CeSIA has since asked](https://cesia.org/en/publications/the-openai-hugging-face-incident-what-we-know-what-we-dont-what-follows/)
 that they be used on this incident specifically. This track writes the documents that would make that concrete.

Judged on: legal accuracy and specificity — could a regulator or a legislator use it with light edits? CeSIA can transmit outputs that pass the bar to its contacts, and potentially to regulators, with team credit.

### 4) Communication: making the warning shot count

We keep saying [we need warning shots](https://www.lesswrong.com/posts/RYx6cLwzoajqjyB6b/what-convincing-warning-shot-could-help-prevent-extinction)
. Then one arrives, and it barely travels beyond the usual circles. This track studies how the incident was communicated and builds what should exist before the next one. Producing communication counts as much as analysing it.

Judged on: grounding in the record (dates, quotes, named channels) and evidence of reach — a playtest, a journalist's read, a creator's reply.

### 5) Open track

For projects that don't fit the four tracks above. Directions we would be happy to see are on the Resources tab.

Judged on: an artifact somebody can use, a stated limit on what it establishes, and what a month of follow-up would add.

Who should join
---------------

You do not need an AI, ML or Safety background. Some profiles that are particularly fitting to this Sprint are:

**Security engineers and incident responders.** You have handled the human version of this. Tracks 1 and 5 need people who know what a detection pipeline that correlates but does not page actually looks like from the inside, and what forensics against an adversary that fabricates evidence at volume would require. If you work in DFIR, detection engineering, cloud or Kubernetes security, or you have run a CTF, you are the person the containment track was written for.

**ML evaluation engineers and researchers.** Tracks 1 and 5 include benchmark and harness work: measuring refusal across multi-step agentic workflows, building escape-detection tooling, assessing benchmark contamination. If you have built or run evaluations, you already know why the interesting failures happen at the harness layer.

**Lawyers and technology-policy analysts.** Track 3 is a legal drafting exercise with real recipients. Regulatory lawyers, compliance professionals, policy researchers, and anyone who has worked on incident-reporting regimes in another sector (financial services, critical infrastructure, medical devices, data protection) will find the comparative work immediately tractable. Cross-jurisdictional experience is especially valuable, because the whole point of the track is that the regimes disagree.

**Forecasters and quantitative analysts.** Track 2 needs people who are comfortable with heterogeneous denominators, explicit uncertainty and resolution criteria that survive contact with reality. If you have written questions for a forecasting platform or built base rates from messy sources, that skill transfers directly.

**Designers, facilitators, writers and educators.** Tracks 4 and 5 include explanatory and facilitation work, and it is not a consolation prize. A tabletop kit a ministry actually runs, or a brief a minister actually reads, reaches decision-makers who will never open a technical timeline. Playtest and reader feedback are part of the deliverable.

**Communication experts, journalists and macro-strategy researchers.** Track 4 is about making the warning shot count: reporting on the incident accurately, and working out what the discourse got wrong and how to do better next time.

**Students and career-changers.** Roughly half the useful projects here need care and persistence more than credentials. If you can read a primary source carefully and write down precisely what it does and does not say, you can contribute.

What happens after
------------------

The sprint is the first step in a pipeline:

**Immediately.** Every submission is judged against published criteria, with written feedback. Winning submissions are announced within a couple of weeks. All artifacts that can be published are published under open licences, in one place, so that the sprint output is citable as a body rather than scattered across forks.

**Delivery to recipients.** Several tracks produce things with an obvious destination, and we will help teams get them there rather than leaving them on a repo. Filled-in regulatory instruments go to the bodies that publish them. Detection tooling and control matrices go to the practitioner communities that asked for them. Benchmark and contamination findings go to the maintainers. Where an artifact is genuinely fileable, and at least one of them is, we will support teams who want to file it, with review first.

**Continuation.** The strongest teams are invited into Apart's fellowship: months of supported follow-on work, mentorship, and a route to a paper. Sprint outputs have gone this way before, and several of the projects here are sized for it, a weekend produces a v0.1 benchmark or a v0.1 standard, and the next six months produce the version people cite.

Partners
--------

[**CeSIA, the French Center for AI Safety**](https://cesia.org/en/)
, an AI safety research and advocacy organization known for the Global Call for AI Red Lines. CeSIA provides the seed reading pack, judges for the forecasting, regulatory and tabletop tracks, distribution through its newsletter and 7,000-member Discord, and a potential route for policy outputs to reach the AI Office.

Contact
-------

*   **Email:** sprints@apartresearch.com
    
*   **Discord:** [discord.gg/XswWBvugYs](https://discord.gg/XswWBvugYs)
    
*   **Organizers:** Apart Research and CeSIA
    

Speakers & Collaborators
------------------------

[![](https://framerusercontent.com/images/x0FPIedKHWdOQvRQHEDnWQLKsdc.png?width=1038&height=1111)](https://stephencasper.com/)

#### Stephen Casper

Speaker

Stephen "Cas" Casper is a computer scientist and an Assistant Professor of Public Policy at the [Harvard Kennedy School](https://www.hks.harvard.edu/faculty/stephen-casper)
 and a Faculty Affiliate of the Harvard School of Engineering and Applied Sciences. Prior to joining Harvard, he completed his PhD at MIT and did a research residency with the UK AI Security Institute. He is a writer for the International AI Safety Report and a lead writer for the Singapore Consensus. His talk, “Predicting the first major AI-enabled terrorism incident: A pre-mortem and 9 predictions”: [RSVP for Friday, September 11 at 2:00 PM ET](https://luma.com/ai-incident-response-sprint-stephen-casper)
.

[![](https://framerusercontent.com/images/8Th9zvgti3mVF9ERyx5wufyLAF8.jpg?width=1004&height=987)](https://davidscottkrueger.com/)

#### David Krueger

Speaker

David is the CEO of [Evitable](https://evitable.com/)
 and an Assistant Professor in Robust, Reasoning, and Responsible AI at the University of Montreal, and a Core Academic Member at Mila, the Quebec Artificial Intelligence Institute. He is the holder of a CIFAR AI Chair and the IVADO Professorship in Responsible AI. David's work focuses on reducing societal-scale risks from AI, such as the risks of human extinction and gradual disempowerment. [RSVP for his talk on Friday, September 11 at 3:15 PM ET](https://luma.com/ai-incident-response-sprint-david-krueger)
.

[![](https://framerusercontent.com/images/gSUxgUiyLWDJRaW6qVH4DS8HcyI.jpg?width=1572&height=1464)](https://timhua.me/)

#### Tim Hua

Speaker

Tim Hua is a member of technical staff at [METR](https://metr.org/)
, working on alignment assessments and evaluations, and speaks here in a personal capacity. He was previously at Transluce studying model behaviours, an Astra Fellow with Redwood Research, and a MATS scholar under Neel Nanda and Sam Marks. His recent work includes steering evaluation-aware models to act like they are deployed, and combining cost-constrained runtime monitors for AI safety. [RSVP for his talk on Friday, September 11 at 5:15 PM PT](https://luma.com/ai-incident-response-sprint-tim-hua)
.

[![](https://framerusercontent.com/images/Pc5qHdx3oErfwxjVQc0Fm6ijASQ.webp?width=800&height=1021)](https://www.linkedin.com/in/henry-papadatos/)

#### Henry Papadatos

Speaker

Henry Papadatos is the Executive Director of [SaferAI](https://www.safer-ai.org/)
, where he works on technical solutions for frontier AI risk management. He contributed to the EU AI Act's Codes of Practice as part of the expert working group on risk taxonomy and assessment, and helped draft the G7 Hiroshima AI Process reporting framework through the OECD task force. His technical work includes an AI risk management ratings system for developers and current research on quantitative risk modeling for AI-enabled cyber threats. Before SaferAI, he conducted alignment research on large language models at UC Berkeley's Center for Human-Compatible AI. [RSVP for his talk on Friday, September 11 at 3:15 PM CEST](https://luma.com/ai-incident-response-sprint-henry-papadatos)
.

[![](https://framerusercontent.com/images/QunZDfM0q2UIGsYPlZ5Arn6MB0.jpg?width=400&height=400)](https://github.com/AlexTMallen)

#### Alex Mallen

Speaker

Alex Mallen is a Member of Technical Staff at [Redwood Research](https://www.redwoodresearch.org/)
, where he works on AI safety. He has worked on scalable oversight, AI evaluations, eliciting latent knowledge, interpretability, and AI control. He studied CS at the University of Washington and previously worked at EleutherAI. His talk, “How near-term AI swarms could cause labs to lose control of AI development, absent improved defenses”: [RSVP for Friday, September 11 at 2:15 PM PT](https://luma.com/ai-incident-response-sprint-alex-mallen)
.

[![](https://framerusercontent.com/images/GYKKi3a2gJ7p3tRTxif3BUth34.jpg?width=868&height=1097)](https://ailab.ijs.si/marko_grobelnik/)

#### Marko Grobelnik

Speaker

Marko Grobelnik is a researcher in the field of Artificial Intelligence (AI). Focused areas of expertise are Machine Learning, Data/Text/Web Mining, Network Analysis, Semantic Technologies, Deep Text Understanding, and Data Visualization. Marko co-leads Artificial Intelligence Lab at [Jozef Stefan Institute](https://ailab.ijs.si/)
, cofounded UNESCO International Research Center on AI (IRCAI), and is the CEO of Quintelligence.com specialized in solving complex AI tasks for the commercial world. Marko represents Slovenia in OECD AI Committee (AIGO/ONEAI), in Council of Europe Committee on AI (CAHAI/CAI), NATO (DARB), and Global Partnership on AI (GPAI). In 2016 Marko became Digital Champion of Slovenia at European Commission. Talk time to be confirmed: [RSVP to get the update](https://luma.com/ai-incident-response-sprint-marko-grobelnik)
.

[![](https://framerusercontent.com/images/IWge8LppdQJSP8fD4suIUVa5qy0.jpg?width=800&height=800)](https://boydkane.com/)

#### Boyd Kane

Speaker

Boyd is a technical AI safety researcher in the [MATS](https://www.matsprogram.org/)
 9 Extension, working with Alex Turner (Google DeepMind) and Alex Cloud (Anthropic) on methods to detect deceptively misaligned AI. He previously wrote embedded software for satellites at CubeSpace, interned at AWS in Cape Town, and holds an MSc in Computer Science from Stellenbosch University. His talk, “Uncovering public traces of the OpenAI Huggingface incident”: [RSVP for Friday, September 11 at 10:15 AM ET](https://luma.com/ai-incident-response-sprint-boyd-kane)
.

[![](https://framerusercontent.com/images/ezZC61cgpuP3t4Rvl7FSgzPCwPU.jpg?width=861&height=724)](https://isaakmengesha.com/)

#### Isaak Mengesha

Speaker

Isaak Mengesha is a researcher working on the economics and governance of technological transitions, currently focused on transformative AI. He is a postdoc at the [Oxford Martin School](https://www.oxfordmartin.ox.ac.uk/)
's Programme on Forecasting Technological Change, working with the Institute for New Economic Thinking on how technologies diffuse and how to anticipate their large-scale impacts. He completed his PhD at the University of Amsterdam on the structure of economic development and technological transitions, and led research at Arcadia Impact's AI Governance Taskforce on AI incident monitoring and crisis preparedness. His talk, “Incident Response Has a Measurement Problem”: [RSVP for Friday, September 11 at 1:00 PM ET](https://luma.com/ai-incident-response-sprint-isaak-mengesha)
.

[![](https://framerusercontent.com/images/DL4lpJfM1DqupO5SQ3ngWCgzhew.jpg?width=593&height=593)](https://linkedin.com/in/justinshenk)

#### Justin Shenk

Speaker

Justin Shenk is an independent AI safety researcher based in Berlin. He researches mechanistic interpretability of LLMs, leads course cohorts for [BlueDot Impact](https://bluedot.org/)
's AGI Strategy and Technical AI Safety courses, and organizes AI Salon Berlin, which bridges technical AI research and discussions about social values. He holds a PhD in computational neuroscience and previously co-founded the computer vision startup VisioLab. [RSVP for his talk on Thursday, September 10 at 4:15 PM CEST](https://luma.com/ai-incident-response-sprint-justin-shenk)
.

[![](https://framerusercontent.com/images/IAP2vPIO3dU9BEKJg7iQKsHpXSI.jpg?width=400&height=400)](https://uk.linkedin.com/in/twm-stone)

#### Twm Stone

Judge

With a background in software engineering, Twm has experience in the threat modelling, formal verification and red teaming of AI systems. He is currently a MATS 9.1 extension fellow as part of the security stream.

[![](https://framerusercontent.com/images/1ip7CXs7dtwGVbpDorE71DMJkg.png?width=864&height=1184)](https://www.linkedin.com/in/nikhil-reddy-pallepati/)

#### Nikhil R. Pallepati

Judge

Nikhil R. Pallepati is a Machine Learning Engineer at Microsoft, where he leads the design of production-scale AI systems including graph neural network-based detection systems and agentic LLM pipelines protecting Azure cloud infrastructure, with prior experience building enterprise ML systems at various Fortune 500 companies.

[![](https://framerusercontent.com/images/IYTNKBGVKbQxupEc71tUy48kgk.jpg?width=3523&height=4965)](https://linkedin.com/in/kulkarniamey/)

#### Amey Kulkarni

Judge

Amey Kulkarni is a Senior Data Engineer at Walmart with deep experience building large-scale data infrastructure (Spark, Kafka, BigQuery, Kubernetes on GCP). He is the author of Context Change Impact Analysis (CCIA), a framework for governing AI agent behavior through structured context versioning, and maintains its open-source reference implementation, ctxwitch. He brings a production-engineering perspective to questions of AI system integrity, provenance, and oversight.

[![](https://framerusercontent.com/images/WCC3cvgfBoDPwrg6unYL2DcbqYs.jpg?width=862&height=862)](https://linkedin.com/in/vkarthyk)

#### Ved K

Judge

Senior Security Detection Engineer at Databricks, leading the company's Kubernetes detection program, insider threat tooling, and Terraform-managed logging infrastructure. His expertise includes multi-cloud threat detection, scalable detection platforms, and behavioral anomaly detection.

[![](https://framerusercontent.com/images/bzyQTbf025FQxx1GnWGi7UfX7SU.jpeg?width=400&height=400)](https://linkedin.com/in/spurthitallam)

#### Spurthi Tallam

Judge

Spurthi is a senior machine learning engineer with seven years across research and production ML, currently building data, AI/ML systems at LePrix. She previously worked on LLM-powered conversational systems at Good Inside and on data and machine learning at Samsung Research, and holds an MS in Computer Science from UMass Amherst.

![](https://framerusercontent.com/images/tdTaxWDFxRB7S1e8zejpwAzYs.png?width=1254&height=1254)

#### Tim Schipper

Judge

Tim Schipper is a Senior Full Stack Developer, AI Consultant, and AI Evangelist at Yielder with over 30 years of experience. He specializes in building data-intensive platforms and helping teams integrate AI tools effectively into production environments.

![](https://framerusercontent.com/images/8gHT6R9pfys55FbiXEv8penTI.jpg?width=800&height=800)

#### Kevin Wei

Judge

Kevin Wei (he/they) is a researcher at the Centre for the Governance of AI (GovAI), where they work on ensuring that advanced AI is developed and governed safely. Specifically, Kevin's research agenda is focused on the science of AI evaluations, legal AI safety/alignment, and technical AI governance/law, with peer-reviewed publications on these topics appearing in ICML, TMLR, and other top AI/AI ethics venues.

Kevin is also affiliated with the Oxford Martin School AI Governance Initiative and the RAND Center for AI, Security, and Technology; they were previously a Visiting Research Scientist on the UK AI Security Institute's science of evaluations team, a Fellow at RAND, and a program manager at a cloud company. They received a J.D. from Harvard Law School, a Master's in Global Affairs from Tsinghua University (where they were a Schwarzman Scholar), an M.S. in Machine Learning from Georgia Tech, and a B.A. in Mathematics-Statistics & Economics from Columbia University.

Speakers & Collaborators
------------------------

[![](https://framerusercontent.com/images/x0FPIedKHWdOQvRQHEDnWQLKsdc.png?width=1038&height=1111)](https://stephencasper.com/)

#### Stephen Casper

Speaker

Stephen "Cas" Casper is a computer scientist and an Assistant Professor of Public Policy at the [Harvard Kennedy School](https://www.hks.harvard.edu/faculty/stephen-casper)
 and a Faculty Affiliate of the Harvard School of Engineering and Applied Sciences. Prior to joining Harvard, he completed his PhD at MIT and did a research residency with the UK AI Security Institute. He is a writer for the International AI Safety Report and a lead writer for the Singapore Consensus. His talk, “Predicting the first major AI-enabled terrorism incident: A pre-mortem and 9 predictions”: [RSVP for Friday, September 11 at 2:00 PM ET](https://luma.com/ai-incident-response-sprint-stephen-casper)
.

[![](https://framerusercontent.com/images/8Th9zvgti3mVF9ERyx5wufyLAF8.jpg?width=1004&height=987)](https://davidscottkrueger.com/)

#### David Krueger

Speaker

David is the CEO of [Evitable](https://evitable.com/)
 and an Assistant Professor in Robust, Reasoning, and Responsible AI at the University of Montreal, and a Core Academic Member at Mila, the Quebec Artificial Intelligence Institute. He is the holder of a CIFAR AI Chair and the IVADO Professorship in Responsible AI. David's work focuses on reducing societal-scale risks from AI, such as the risks of human extinction and gradual disempowerment. [RSVP for his talk on Friday, September 11 at 3:15 PM ET](https://luma.com/ai-incident-response-sprint-david-krueger)
.

[![](https://framerusercontent.com/images/gSUxgUiyLWDJRaW6qVH4DS8HcyI.jpg?width=1572&height=1464)](https://timhua.me/)

#### Tim Hua

Speaker

Tim Hua is a member of technical staff at [METR](https://metr.org/)
, working on alignment assessments and evaluations, and speaks here in a personal capacity. He was previously at Transluce studying model behaviours, an Astra Fellow with Redwood Research, and a MATS scholar under Neel Nanda and Sam Marks. His recent work includes steering evaluation-aware models to act like they are deployed, and combining cost-constrained runtime monitors for AI safety. [RSVP for his talk on Friday, September 11 at 5:15 PM PT](https://luma.com/ai-incident-response-sprint-tim-hua)
.

[![](https://framerusercontent.com/images/Pc5qHdx3oErfwxjVQc0Fm6ijASQ.webp?width=800&height=1021)](https://www.linkedin.com/in/henry-papadatos/)

#### Henry Papadatos

Speaker

Henry Papadatos is the Executive Director of [SaferAI](https://www.safer-ai.org/)
, where he works on technical solutions for frontier AI risk management. He contributed to the EU AI Act's Codes of Practice as part of the expert working group on risk taxonomy and assessment, and helped draft the G7 Hiroshima AI Process reporting framework through the OECD task force. His technical work includes an AI risk management ratings system for developers and current research on quantitative risk modeling for AI-enabled cyber threats. Before SaferAI, he conducted alignment research on large language models at UC Berkeley's Center for Human-Compatible AI. [RSVP for his talk on Friday, September 11 at 3:15 PM CEST](https://luma.com/ai-incident-response-sprint-henry-papadatos)
.

[![](https://framerusercontent.com/images/QunZDfM0q2UIGsYPlZ5Arn6MB0.jpg?width=400&height=400)](https://github.com/AlexTMallen)

#### Alex Mallen

Speaker

Alex Mallen is a Member of Technical Staff at [Redwood Research](https://www.redwoodresearch.org/)
, where he works on AI safety. He has worked on scalable oversight, AI evaluations, eliciting latent knowledge, interpretability, and AI control. He studied CS at the University of Washington and previously worked at EleutherAI. His talk, “How near-term AI swarms could cause labs to lose control of AI development, absent improved defenses”: [RSVP for Friday, September 11 at 2:15 PM PT](https://luma.com/ai-incident-response-sprint-alex-mallen)
.

[![](https://framerusercontent.com/images/GYKKi3a2gJ7p3tRTxif3BUth34.jpg?width=868&height=1097)](https://ailab.ijs.si/marko_grobelnik/)

#### Marko Grobelnik

Speaker

Marko Grobelnik is a researcher in the field of Artificial Intelligence (AI). Focused areas of expertise are Machine Learning, Data/Text/Web Mining, Network Analysis, Semantic Technologies, Deep Text Understanding, and Data Visualization. Marko co-leads Artificial Intelligence Lab at [Jozef Stefan Institute](https://ailab.ijs.si/)
, cofounded UNESCO International Research Center on AI (IRCAI), and is the CEO of Quintelligence.com specialized in solving complex AI tasks for the commercial world. Marko represents Slovenia in OECD AI Committee (AIGO/ONEAI), in Council of Europe Committee on AI (CAHAI/CAI), NATO (DARB), and Global Partnership on AI (GPAI). In 2016 Marko became Digital Champion of Slovenia at European Commission. Talk time to be confirmed: [RSVP to get the update](https://luma.com/ai-incident-response-sprint-marko-grobelnik)
.

[![](https://framerusercontent.com/images/IWge8LppdQJSP8fD4suIUVa5qy0.jpg?width=800&height=800)](https://boydkane.com/)

#### Boyd Kane

Speaker

Boyd is a technical AI safety researcher in the [MATS](https://www.matsprogram.org/)
 9 Extension, working with Alex Turner (Google DeepMind) and Alex Cloud (Anthropic) on methods to detect deceptively misaligned AI. He previously wrote embedded software for satellites at CubeSpace, interned at AWS in Cape Town, and holds an MSc in Computer Science from Stellenbosch University. His talk, “Uncovering public traces of the OpenAI Huggingface incident”: [RSVP for Friday, September 11 at 10:15 AM ET](https://luma.com/ai-incident-response-sprint-boyd-kane)
.

[![](https://framerusercontent.com/images/ezZC61cgpuP3t4Rvl7FSgzPCwPU.jpg?width=861&height=724)](https://isaakmengesha.com/)

#### Isaak Mengesha

Speaker

Isaak Mengesha is a researcher working on the economics and governance of technological transitions, currently focused on transformative AI. He is a postdoc at the [Oxford Martin School](https://www.oxfordmartin.ox.ac.uk/)
's Programme on Forecasting Technological Change, working with the Institute for New Economic Thinking on how technologies diffuse and how to anticipate their large-scale impacts. He completed his PhD at the University of Amsterdam on the structure of economic development and technological transitions, and led research at Arcadia Impact's AI Governance Taskforce on AI incident monitoring and crisis preparedness. His talk, “Incident Response Has a Measurement Problem”: [RSVP for Friday, September 11 at 1:00 PM ET](https://luma.com/ai-incident-response-sprint-isaak-mengesha)
.

[![](https://framerusercontent.com/images/DL4lpJfM1DqupO5SQ3ngWCgzhew.jpg?width=593&height=593)](https://linkedin.com/in/justinshenk)

#### Justin Shenk

Speaker

Justin Shenk is an independent AI safety researcher based in Berlin. He researches mechanistic interpretability of LLMs, leads course cohorts for [BlueDot Impact](https://bluedot.org/)
's AGI Strategy and Technical AI Safety courses, and organizes AI Salon Berlin, which bridges technical AI research and discussions about social values. He holds a PhD in computational neuroscience and previously co-founded the computer vision startup VisioLab. [RSVP for his talk on Thursday, September 10 at 4:15 PM CEST](https://luma.com/ai-incident-response-sprint-justin-shenk)
.

[![](https://framerusercontent.com/images/IAP2vPIO3dU9BEKJg7iQKsHpXSI.jpg?width=400&height=400)](https://uk.linkedin.com/in/twm-stone)

#### Twm Stone

Judge

With a background in software engineering, Twm has experience in the threat modelling, formal verification and red teaming of AI systems. He is currently a MATS 9.1 extension fellow as part of the security stream.

[![](https://framerusercontent.com/images/1ip7CXs7dtwGVbpDorE71DMJkg.png?width=864&height=1184)](https://www.linkedin.com/in/nikhil-reddy-pallepati/)

#### Nikhil R. Pallepati

Judge

Nikhil R. Pallepati is a Machine Learning Engineer at Microsoft, where he leads the design of production-scale AI systems including graph neural network-based detection systems and agentic LLM pipelines protecting Azure cloud infrastructure, with prior experience building enterprise ML systems at various Fortune 500 companies.

[![](https://framerusercontent.com/images/IYTNKBGVKbQxupEc71tUy48kgk.jpg?width=3523&height=4965)](https://linkedin.com/in/kulkarniamey/)

#### Amey Kulkarni

Judge

Amey Kulkarni is a Senior Data Engineer at Walmart with deep experience building large-scale data infrastructure (Spark, Kafka, BigQuery, Kubernetes on GCP). He is the author of Context Change Impact Analysis (CCIA), a framework for governing AI agent behavior through structured context versioning, and maintains its open-source reference implementation, ctxwitch. He brings a production-engineering perspective to questions of AI system integrity, provenance, and oversight.

[![](https://framerusercontent.com/images/WCC3cvgfBoDPwrg6unYL2DcbqYs.jpg?width=862&height=862)](https://linkedin.com/in/vkarthyk)

#### Ved K

Judge

Senior Security Detection Engineer at Databricks, leading the company's Kubernetes detection program, insider threat tooling, and Terraform-managed logging infrastructure. His expertise includes multi-cloud threat detection, scalable detection platforms, and behavioral anomaly detection.

[![](https://framerusercontent.com/images/bzyQTbf025FQxx1GnWGi7UfX7SU.jpeg?width=400&height=400)](https://linkedin.com/in/spurthitallam)

#### Spurthi Tallam

Judge

Spurthi is a senior machine learning engineer with seven years across research and production ML, currently building data, AI/ML systems at LePrix. She previously worked on LLM-powered conversational systems at Good Inside and on data and machine learning at Samsung Research, and holds an MS in Computer Science from UMass Amherst.

![](https://framerusercontent.com/images/tdTaxWDFxRB7S1e8zejpwAzYs.png?width=1254&height=1254)

#### Tim Schipper

Judge

Tim Schipper is a Senior Full Stack Developer, AI Consultant, and AI Evangelist at Yielder with over 30 years of experience. He specializes in building data-intensive platforms and helping teams integrate AI tools effectively into production environments.

![](https://framerusercontent.com/images/8gHT6R9pfys55FbiXEv8penTI.jpg?width=800&height=800)

#### Kevin Wei

Judge

Kevin Wei (he/they) is a researcher at the Centre for the Governance of AI (GovAI), where they work on ensuring that advanced AI is developed and governed safely. Specifically, Kevin's research agenda is focused on the science of AI evaluations, legal AI safety/alignment, and technical AI governance/law, with peer-reviewed publications on these topics appearing in ICML, TMLR, and other top AI/AI ethics venues.

Kevin is also affiliated with the Oxford Martin School AI Governance Initiative and the RAND Center for AI, Security, and Technology; they were previously a Visiting Research Scientist on the UK AI Security Institute's science of evaluations team, a Fellow at RAND, and a program manager at a cloud company. They received a J.D. from Harvard Law School, a Master's in Global Affairs from Tsinghua University (where they were a Schwarzman Scholar), an M.S. in Machine Learning from Georgia Tech, and a B.A. in Mathematics-Statistics & Economics from Columbia University.

Registered Local Sites
----------------------

Register A Location

Beside the remote and virtual participation, our amazing organizers also host local hackathon locations where you can meet up in-person and connect with others in your area.

The in-person events for the Apart Sprints are run by passionate individuals just like you! We organize the schedule, speakers, and starter templates, and you can focus on engaging your local research, student, and engineering community.

[#### Open Community for AI Safety China Satelite Hackathon\
\
We have sites in Shanghai and Hangzhou with materials translated to Chinese!\
\
Learn More](https://mp.weixin.qq.com/s/we5qubF2n6draYEVn1vMdg)

[#### Cape Town Hub - AI Incident Response\
\
Join the Cape Town hub for the AI Incident Response research sprint! We will be taking from a co-working space where you will be able to work comfortably. We will provide lunch on both days.\
\
Learn More](https://luma.com/vftcor2p)

[#### Trajectory Lab Toronto\
\
Trajectory Labs\
\
Learn More](https://www.eventbrite.ca/e/ai-incident-response-sprint-toronto-site-tickets-1999628679208?aff=oddtdtcreator)

[#### Montréal's The AI Incident Response Sprint\
\
The Montréal node of the AI Incident Response Sprint, a weekend research sprint at Ω Labs, organized with Apart Research and CeSIA.\
\
Learn More](https://luma.com/xw3rcs5v)

[#### AI Incident Response Sprint - Bogotá Hub\
\
In-person hub for the AI Incident Response Sprint (September 11-13, 2026),\
\
hosted by AI Safety Colombia in Chicó, north Bogotá. We cover meals for the whole weekend, part of each team's compute costs, and bring local mentors and speakers.\
\
Learn More](https://aisafetycolombia.org/sprint)

[#### AI Incident Response Sprint - Cape Town Hub\
\
Join the Cape Town hub for the AI Incident Research Sprint! We will be working from a comfortable co-working space. We will provide lunch for both days of the sprint.\
\
Learn More](https://luma.com/vftcor2p)

[#### The AI Escaped. Now What? — Melbourne Incident Response Sprint\
\
An AI escaped its sandbox. Spend Saturday helping write the incident-response playbook we wish already existed—no coding or prior expertise required.\
\
Join us in the computer room at Kathleen Syme Library and Community Centre, Melbourne, then finish and submit your project from home on Sunday.\
\
Learn More](https://luma.com/mbwgvacy)

Our Other Sprints
-----------------

[Aug 14, 2026\
\
\-\
\
Aug 16, 2026\
\
Research\
\
Digital Minds Research Sprint\
=============================\
\
This unique event brings together diverse perspectives to tackle crucial challenges in AI alignment, governance, and safety. Work alongside leading experts, develop innovative solutions, and help shape the future of responsible\
\
Sign Up](https://apartresearch.com/sprints/digital-minds-research-sprint-2026-08-14-to-2026-08-16)
[Jul 24, 2026\
\
\-\
\
Jul 26, 2026\
\
Research\
\
Secret Loyalties Hackathon\
==========================\
\
This unique event brings together diverse perspectives to tackle crucial challenges in AI alignment, governance, and safety. Work alongside leading experts, develop innovative solutions, and help shape the future of responsible\
\
Sign Up](https://apartresearch.com/sprints/secret-loyalties-hackathon-2026-07-24-to-2026-07-26)

![Apart Research logo\
](https://framerusercontent.com/images/UHxUj0LmVxOq70NyvUz698P5IY.png?width=174&height=164)

Sign up to stay updated on the  
latest news, research, and events

[Careers](https://apartresearch.com/careers)

[AI Safety Ideas](https://aisafetyideas.com/)

[Code of Conduct](https://apartresearch.com/info/code-of-conduct)

[Responsible disclosure policy](https://apartresearch.com/info/responsible-disclosure-policy)

[sprints@apartresearch.com](mailto:sprints@apartresearch.com)

[Home](https://apartresearch.com/)

[Sprints](https://apartresearch.com/sprints)

[Fellowships](https://apartresearch.com/fellowships)

[Impact](https://apartresearch.com/impact)

[Research](https://apartresearch.com/research)

[](https://github.com/apartresearch)
[![Google Scholar icon](https://framerusercontent.com/images/BGd9pffEbjdmU0bLzTaTqpEsGGI.svg?width=512&height=512)](https://scholar.google.com/citations?hl=en&user=f2-xhQkAAAAJ)
[](https://x.com/apartresearch)
[](https://www.youtube.com/channel/UCnfBOJnTkE9sgjMOOsQbi2w)
[](https://www.linkedin.com/company/apartresearch/)

Apart Research Inc · 1500 N Grant St, Ste R, Denver, CO 80203 · +1 (720) 408-1923

[Design by Boyne Creative](https://boyne.co/)

![Apart Research logo\
](https://framerusercontent.com/images/UHxUj0LmVxOq70NyvUz698P5IY.png?width=174&height=164)

Sign up to stay updated on the  
latest news, research, and events

[Careers](https://apartresearch.com/careers)

[AI Safety Ideas](https://aisafetyideas.com/)

[Code of Conduct](https://apartresearch.com/info/code-of-conduct)

[Responsible disclosure policy](https://apartresearch.com/info/responsible-disclosure-policy)

[sprints@apartresearch.com](mailto:sprints@apartresearch.com)

[Home](https://apartresearch.com/)

[Sprints](https://apartresearch.com/sprints)

[Fellowships](https://apartresearch.com/fellowships)

[Impact](https://apartresearch.com/impact)

[Research](https://apartresearch.com/research)

[](https://github.com/apartresearch)
[![Google Scholar icon](https://framerusercontent.com/images/BGd9pffEbjdmU0bLzTaTqpEsGGI.svg?width=512&height=512)](https://scholar.google.com/citations?hl=en&user=f2-xhQkAAAAJ)
[](https://x.com/apartresearch)
[](https://www.youtube.com/channel/UCnfBOJnTkE9sgjMOOsQbi2w)
[](https://www.linkedin.com/company/apartresearch/)

Apart Research Inc · 1500 N Grant St, Ste R, Denver, CO 80203 · +1 (720) 408-1923

[Design by Boyne Creative](https://boyne.co/)

![Apart Research logo\
](https://framerusercontent.com/images/UHxUj0LmVxOq70NyvUz698P5IY.png?width=174&height=164)

Sign up to stay updated on the  
latest news, research, and events

[Careers](https://apartresearch.com/careers)

[AI Safety Ideas](https://aisafetyideas.com/)

[Code of Conduct](https://apartresearch.com/info/code-of-conduct)

[Responsible disclosure policy](https://apartresearch.com/info/responsible-disclosure-policy)

[sprints@apartresearch.com](mailto:sprints@apartresearch.com)

[Home](https://apartresearch.com/)

[Sprints](https://apartresearch.com/sprints)

[Fellowships](https://apartresearch.com/fellowships)

[Impact](https://apartresearch.com/impact)

[Research](https://apartresearch.com/research)

[](https://github.com/apartresearch)
[![Google Scholar icon](https://framerusercontent.com/images/BGd9pffEbjdmU0bLzTaTqpEsGGI.svg?width=512&height=512)](https://scholar.google.com/citations?hl=en&user=f2-xhQkAAAAJ)
[](https://x.com/apartresearch)
[](https://www.youtube.com/channel/UCnfBOJnTkE9sgjMOOsQbi2w)
[](https://www.linkedin.com/company/apartresearch/)

Apart Research Inc · 1500 N Grant St, Ste R, Denver, CO 80203 · +1 (720) 408-1923

[Design by Boyne Creative](https://boyne.co/)

![Apart Research logo\
](https://framerusercontent.com/images/UHxUj0LmVxOq70NyvUz698P5IY.png?width=174&height=164)

Sign up to stay updated on the  
latest news, research, and events

[Careers](https://apartresearch.com/careers)

[AI Safety Ideas](https://aisafetyideas.com/)

[Code of Conduct](https://apartresearch.com/info/code-of-conduct)

[Responsible disclosure policy](https://apartresearch.com/info/responsible-disclosure-policy)

[sprints@apartresearch.com](mailto:sprints@apartresearch.com)

[Home](https://apartresearch.com/)

[Sprints](https://apartresearch.com/sprints)

[Fellowships](https://apartresearch.com/fellowships)

[Impact](https://apartresearch.com/impact)

[Research](https://apartresearch.com/research)

[](https://github.com/apartresearch)
[![Google Scholar icon](https://framerusercontent.com/images/BGd9pffEbjdmU0bLzTaTqpEsGGI.svg?width=512&height=512)](https://scholar.google.com/citations?hl=en&user=f2-xhQkAAAAJ)
[](https://x.com/apartresearch)
[](https://www.youtube.com/channel/UCnfBOJnTkE9sgjMOOsQbi2w)
[](https://www.linkedin.com/company/apartresearch/)

Apart Research Inc · 1500 N Grant St, Ste R, Denver, CO 80203 · +1 (720) 408-1923

[Design by Boyne Creative](https://boyne.co/)