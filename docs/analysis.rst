Case Analysis
==============
Throughout the collection of cases from V1 and V2, the Center team has put together several resources to inform insider programs through thorough analysis of the submitted cases.


Frequency Heatmap 
------------------
This heatmap contains the techniques of the MITRE ATT&CK® framework that were used in insider threat cases with an overlay of the frequency seen of each technique through submitted cases. 
The red indicates that the technique was more commonly used, orange means it was somewhat commonly used, and yellow indicates that those were the least common techniques used. 

.. raw:: html

    <p>
        <a class="btn btn-primary" target="_blank" href="https://mitre-attack.github.io/attack-navigator/#layerURL=https://center-for-threat-informed-defense.github.io/sensor-mappings-to-attack/navigator/insider-threat-heatmap.json">
        <i class="fa fa-map-signs"></i> Open Heatmap in Navigator</a>

        <a class="btn btn-primary" target="_blank" href="..\insider-threat-heatmap.json" download="insider-threat-heatmap.json">
        <i class="fa fa-download"></i> Download Heatmap JSON</a>
    
    </p>

.. image:: /images/heatmap.PNG
   :scale: 75%

.. TODO add inferences below

Inferences
-------------
* The majority of cases can be broken into two categories: **exfiltration** and **fraud**.

* During analysis it was seen that all cases utilized the current permissions given to the employee and no privilege escalation was required to achieve their goal. 

* In many cases where fraud was detected there was some form of immediate monetary compensation. In all of those cases the compensation was under $250 and in most of those cases there were multiple instances of small amounts.  



Fraud
******

* Account creation

* Accessing accounts

* Processing refunds/payments

* Account alteration

.. TODO add sub-heading for fraud heatmap below



Exfiltration 
*************
* Exfiltration via USA/removable storage media

* Access of data repository such as One Drive or SharePoint

.. TODO add sub-heading for exfil heatmap below


.. TODO add limitations below

Limitations
------------
* At this time the focus for this project is on technical indicators of insider threats, for that reason there were cases that were submitted and determined to be non-technical resulting in removal prior to analysis. Many of the cases removed were carried out due to physical controls.  

* When analyzing these submissions, it is important to keep in mind that researchers will not know the ins and outs of the organization contributing data therefore there might be context or conclusions that are not fully drawn.  

* There will be cases that were either not reported during the project’s call for contributions or that has yet to be detected by the organization.  

* The human factor is a place where growth has been identified and researchers are working to expand on. This specifically focuses on the Observable Human Indicators (OHIs). Collecting data about the insider threat allows for connections to be drawn and possible warning signs identified.  