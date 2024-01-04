Knowledge Base
===============

Green = Seen: Insider Tactics, Techniques, and Procedures
-----------------------------------------------------------

The ATT&CK® Navigator matrix - which the team calls the green = seen chart - illustrates all of the TTPs seen to be used by insiders. This information stems from the case files submitted by participating organizations and illustrates the potential TTPs an enterprise could see in their network. 

.. tip::

    See the :doc:`heatmap </analysis>` to visualize the frequency of each technique.


.. FIX LINKS!!!!!

.. raw:: html

    <p>
    
        <a class="btn btn-primary" target="_blank" href="https://mitre-attack.github.io/attack-navigator/#layerURL=https://center-for-threat-informed-defense.github.io/sensor-mappings-to-attack/navigator/Auditd-heatmap.json">
        <i class="fa fa-map-signs"></i> Open in ATT&CK® Navigator</a>

        <a class="btn btn-primary" target="_blank" href="..\extradocs\insider-threat-ttp-kb.csv" download="insider-threat-ttp-kb.csv">
        <i class="fa fa-download"></i> Download CSV</a>

        <a class="btn btn-primary" target="_blank" href="..\insider-threat-ttp-kb.json" download="insider-threat-ttp-kb.json">
        <i class="fa fa-download"></i> Download JSON</a>
    </p>

    

PLACEHOLDER IMAGE

.. image:: /images/green_seen.PNG
   :scale: 75%


Data Collection
----------------

The data in the knowledge base is validated by identification of TTPs used by the subject and method of detection, in line with ATT&CK® guidelines. Data in the knowledge base is collected through submission of project participant cases into a secure case submission portal. Participants provided a sequential list of TTPs per case, with additional information on the data sources used to detect those TTPs, select observable human indicators, and notes about the subject. The data in the knowledge base appears as the following:

* Types of logs, analytics, or other methods to identify the threat including:

    * Data source(s) used to identify/validate each TTP within each case 

    * Format of each data source (if applicable) 

    * Existing analytics used to detect TTP (if applicable) 

    * Timestamps of each TTP to better understand the overall timeline 

* The tactic each technique corresponds to. Just like in Enterprise ATT&CK®, a technique can fall under multiple tactics depending on how the insider used the technique in each case. Along the way, there may be insider actions that do not neatly fit into Enterprise ATT&CK® tactics or techniques. Contributors can propose new or modified tactics and techniques in these circumstances. 

* Techniques can be modified from an existing Enterprise ATT&CK® technique with new language to make it applicable to insider threats if required. 

* Brand new techniques can also be created when an existing technique is not sufficient. 