Knowledge Base
===============
Method and Design 
-----------------------
Many times, network defenders will focus on the TTPs of the last major insider threat case to hit the news, anticipating that every insider threat will act like a Manning, Snowden, or Hanssen. When so much attention is paid to the one-in-a-million indicators associated with these notorious cases, more mundane but equally damaging actions might be overlooked. Hunting the one-in-a million cases often puts defenders into the mindset of thinking about what is possible, instead of what is probable. It causes defenders to “be creative” when designing sensors or searching for indicators because defenders must speculate on techniques that an insider could hypothetically execute. This creativity causes Insider Threat Programs and SOCs to lose focus. The researchers have deemed these TTPs as “could”—as in an insider threat could use these TTPs to harm an organization. Could comprise a superset of actual, hypothetical, and fantastical insider actions. Frederick the Great is quoted as saying “he who defends everything defends nothing.” As a result of this Insider Threat TTP Knowledge Base, organizations can shift their mitigations from living up to Frederick the Great’s warning to actionable detections and response. With limited resources, an organization is better equipped to defend their networks if they can focus their efforts where they are most beneficial. This project informs defenders where their resources are best spent. To get there, the researchers reduced the set of TTPs in the “could” section down to a much more reasonable “would” set. These are TTPs that have a reasonable chance of being used by an insider threat. We assessed each TTP for the skill level needed for successful execution and the potential benefit each TTP would give to an insider threat. Inclusion in the “would” set was validated by the Center researchers and Center participants, as individuals with extensive experience across public and private sector cyber defense, with further specialized experience in detection and response to insider threat events. This experience and expertise drew out the “would” set of TTPs as a transition between the ephemerous “could” and the data-driven “did” TTPs, which comprise the Insider Threat TTP Knowledge Base. The TTPs were only counted as “did” if they were seen in the documented case files. 


Cases
------ 

Project participants provided a sequential list of TTPs per case, with information on the data sources used to detect those TTPs. Our findings are therefore validated by both what TTPs were used by the insiders and how these TTPs were detected. Validating data appeared in the following forms: 

* Types of logs, analytics, or other methods will help future SOCs and insider threat analysts. 

    * Data source(s) used to identify/validate each TTP within each case 

    * Format of each data source (if applicable) 

    * Existing analytics used to detect TTP (if applicable) 

    * Timestamps of each TTP to better understand the overall timeline 

* The tactic each technique should fall under. Just like the Enterprise ATT&CK matrix, a technique can fall under multiple tactics depending on how the insider used the technique in each case. Along the way, there may be insider actions that do not neatly fit into Enterprise ATT&CK tactics or techniques. Contributors can propose new or modified tactics and techniques. 

* Techniques can be modified from an existing Enterprise ATT&CK technique with new language to make it applicable to insider threats. 

* Brand new techniques can also be created when an existing technique is not sufficient. 

Analysis 
---------