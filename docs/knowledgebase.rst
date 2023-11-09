Knowledge Base
===============
Method and Design 
-----------------------

Network defenders often focus on the TTPs of high-profile insider threat cases, such as Manning, Snowden, or Hanssen, causing them to overlook more mundane but equally damaging actions. This focus on one-in-a-million cases leads to prioritizing what is possible rather than what is probable, leading to speculative defense strategies. Researchers have categorized these TTPs as "could," consisting of actual, hypothetical, and fantastical insider actions.

However, organizations can shift their focus to actionable detections and response by using the Insider Threat TTP Knowledge Base, which informs defenders where their resources are best spent. The TTPs in the Knowledge Base are categorized as "did" if they were observed in documented case files, providing a data-driven approach to insider threat defense. This enables organizations to better allocate their limited resources and focus their efforts where they are most beneficial. See the :ref:`Green = Seen` section to view the current techniques that are categorized as "did". 

.. image:: /images/did.png


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

:download:`Insider Threat TTP CSV File <../insider-threat-ttp-kb.csv>`


:download:`Insider Threat TTP JSON File <../insider-threat-ttp-kb.json>`

