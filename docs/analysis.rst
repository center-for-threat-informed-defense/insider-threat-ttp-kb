Case Analysis
==============
Throughout the collection of cases from V1 and V2, the Center team has put together several resources to inform insider programs through analysis of the submitted cases.


Frequency Heatmap 
------------------
This heatmap contains the techniques of the MITRE ATT&CK® framework that were used in insider threat cases with an overlay of the frequency seen of each technique through submitted cases. 
The red indicates that the technique was more commonly used, orange means it was somewhat commonly used, and yellow indicates that those were the least common techniques used. 

The heatmap consists of three categories of frequency:

* **Frequent**: The technique was seen in more than 16% of cases submitted by participants.

* **Moderate:** The technique was seen in 6-15% of cases submitted by participants.

* **Infrequent:** The technique was seen in less than 5% of cases submitted by participants.


.. raw:: html

    <p>
        <a class="btn btn-primary" target="_blank" href="https://mitre-attack.github.io/attack-navigator/#layerURL=https://center-for-threat-informed-defense.github.io/insider-threat-ttp-kb/navigator/insider-threat-heatmap.json">
        <i class="fa fa-map-signs"></i> Open Heatmap in Navigator</a>

        <a class="btn btn-primary" target="_blank" href="..\insider-threat-heatmap.json" download="insider-threat-heatmap.json">
        <i class="fa fa-download"></i> Download Heatmap JSON 145KB</a>
    
    </p>

.. image:: /images/heatmap.svg
   :scale: 75%

.. TODO add inferences below

Evidence Based Inferences
----------------------------
* The majority of cases can be broken into two categories: **exfiltration** and **fraud**.

* During analysis it was seen that all cases utilized the current permissions given to the employee and no privilege escalation was required to achieve their goal. 

* In many cases where fraud was detected there was some form of immediate monetary compensation. In all of those cases the compensation was under $250 and in most of those cases there were multiple instances of small amounts.  

* Indicators deemed non-technical can typically be grouped into Financial Theft (T1657). These techniques can be broken down further into:

    * **Circumventing Security Controls**: security checks put in place by an organization were circumvented to avoid detection (e.x. improper key control or avoidance of cameras)

    * **Collusion**: multiple employees worked together to perform actions such as sending all customers to one employee for compensation

    * **Deceit for Personal Gain**: Use of insider knowledge to decieve untrained employees

    * **Failure to Follow Procedure**: Employees unintentionally or intentionally gave the wrong amount of money to a customer or not properly log cash flow 

    * **Physical Theft**: any type of theft that occurs with physical objects such as cash or physical machines


Fraud
******


**Insider threats routinely utilized their current given permissions to commit fraud.** 
This was most commonly seen with (T1565) Data Manipulation and (T1136) Create Account. These permissions were used to generate illegitimate refunds and payments to accounts handled by the subject as well as to apply and approve for illegitimate loans. Privilege escalation was rarely identified when a subject was commiting fraud.

**In fraud cases insider threats routinely researched the customer before committing fraud.** This is seen in many instances of (T1213) Data from Information Repositories prior to techniques such as (T1098) Account Manipulation and (T1565) Data Manipulation. The insider threat would utilize the internal customer database to review account information prior to targeting the customer’s account. 

**The common goal among insider threats committing fraud was monetary compensation. This occurred through four main methods:**

* **Creation of accounts:** The accounts created were loans for customers not present but verified by the insider threat, as well as the creation of illegitimate bank accounts. The information used to create these accounts were of family members or friends with no knowledge of the account. The account was maintained and used by the insider threat. 

* **Unauthorized accessing of accounts:** Legitimate accounts of customers that were accessed by the insider threat led to acts such as the processing of illegitimate payments or the altering of account data. 

* **Processing refunds/payments:** The insider threat processed payments from an existing customer account to an account managed by them, or processed refunds for accounts managed by them or a close acquaintance. 

* **Altering accounts:** Existing customer accounts were altered to allow for insider threats to remain in access without being detected. This included changing the email or phone number associated with the account.  


.. raw:: html

    <p>

        <a class="btn btn-primary" target="_blank" href="..\fraud_heat.json" download="fraud_heat.json">
        <i class="fa fa-download"></i> Download Fraud Heatmap JSON 4KB</a>
    
    </p>

.. image:: /images/fraud_heat.svg
   :scale: 75%



Exfiltration 
*************


**Data was often accessed from a data repository such as One Drive or SharePoint:** Prior to exfiltration, files were accessed and downloaded from data repositories such as One Drive and SharePoint.

**Data was commonly staged by the subject prior to exfiltration:** Large quantities of files, 500+, were downloaded from shared resources such as OneDrive and SharePoint then stored locally on the insider’s system (T1074) or to an archived file (T1560) prior to exfiltration.

**A common exfiltration channel is USB/removable device storage:** Due to the physical size of USB devices and other removable media it is easy to conceal and be transported in and out of organizations with little difficulty. Furthermore, these devices are often used frequently so their movement is less likely to raise red flags. Exfiltration Over Physical Medium (T1052) is seen with a higher frequency, specifically USB devices (T1052.001) than other exfiltration techniques. 

.. raw:: html

    <p>

        <a class="btn btn-primary" target="_blank" href="..\exfil_heat.json" download="exfil_heat.json">
        <i class="fa fa-download"></i> Download Exfiltration Heatmap JSON 6KB</a>
    
    </p>
    
.. image:: /images/exfil_heat.svg
   :scale: 75%



.. TODO add limitations below

Limitations
------------

* When analyzing these submissions, it is important to keep in mind that researchers will not know the ins and outs of the organization contributing data therefore context such as detection mechanism may not be known. 

* Some insider threats can go years without being detected, therefore all of the techniques an insider has done may not be identified. 
	
* The human factor has been identified as an area for growth, and researchers are working to expand upon it. This specifically focuses on the Observable Human Indicators (OHIs). Collecting data about the insider threat allows for the identification of patterns, insights and possible warning signs. 
