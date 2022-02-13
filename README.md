# Insider Threat Tactics, Techniques, and Procedures (TTP) Knowledge Base
To advance our collective understanding of insider threats, the Center for Threat-Informed Defense developed the Insider Threat TTP Knowledge Base, a collection of TTPs used by insiders in IT environments. This Knowledge Base builds upon
data collected on insider threat incidents and lessons learned and experience from the ATT&CK knowledge base. With this lexicon of known insider threat TTPs as a foundation, defenders will detect, mitigate, and emulate insider actions on IT systems and stop them.

## File List
| File | Description |
|------|-------------|
| [design-principles-and-methodology.docx](https://github.com/center-for-threat-informed-defense/insider-threat-ttp-kb/blob/main/design-principles-and-methodology.docx?raw=true) | A document describing the design principles and methodology of the Insider Threat TTP Knowledgebase |
| [insider-threat-ttp-kb.csv](insider-threat-ttp-kb.csv) | A spreadsheet containing the Insider Threat TTP Knowledgebase |
| [insider-threat-ttp-kb.json](insider-threat-ttp-kb.json) | A navigator layer representing the Insider Threat TTP Knowledgebase |
| [insider-threat-heatmap.json](insider-threat-heatmap.json) | A navigator layer representing the Insider Threat TTP Knowledgebase as a heatmap|

## Call for Contributors
This initial Knowledge Base is an evidence-based examination of detected, documented insider threat actions on IT systems from across various organizations and industries. We need your help to validate or refute this initial analysis. We seek to learn about your insider threat use cases and data sources, enabling us to mature this KB and raise the level of difficulty for any insider. Help us expand the knowledge base by contributing your data.

Contributions must fit the guidelines listed below:
- Only include actions that involve the use of IT systems and can be detected through structured data logs
- Only include TTPs that are validated by documentation (e.g., exist within an organization's case files or tracking system). Details, at a minimum, must include
-- A corresponding technique and tactic (either an existing ATT&CK technique or a proposed technique)
-- A date or date/time offset
-- A data source
-- Contextual information describing the event
- Details that would identify an organization or individuals should be anonymized

Example
| Technique ID | Sub-Technique ID | Technique Name | Proposed Tactic Group | Timestamp | Data Source | Log type within source | Notes                 |
|--------------|------------------|----------------|-----------------------|-----------|-------------|------------------------|-----------------------|
| T1078 | T1078.002 | Valid Accounts: Domain Accounts | Persistence | Sept 3, 2021 | Identify System Data | AAD Logs | User's account was terminated and user left the company |

Contact [us](ctid@mitre-engenuity.org) to learn more about contributing to the knowledge base.  

## Questions and Feedback
Publishing the Knowledge Base is a first step toward establishing a community-wide collaboration to advance our collective understanding of insider threat. We are actively seeking feedback on this initial release and will continue to evolve it with your support. Please submit issues for any technical questions/concerns or contact ctid@mitre-engenuity.org directly for more general inquiries.


### Proposing Changes

* Please open a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) (PR) against the `main` branch for any desired changes. The PR will be reviewed by the project team.
* Note that all PR checks must pass to be eligible for merge approval.


## Notice
Copyright 2022 MITRE Engenuity. Approved for public release. Document number CT0041.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

This project makes use of ATT&CK®

[ATT&CK Terms of Use](https://attack.mitre.org/resources/terms-of-use/)
