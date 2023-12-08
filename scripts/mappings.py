from mitreattack.stix20 import MitreAttackData
import json

mitre_attack_data = MitreAttackData('enterprise-attack-14.1.json')

insider_threat_file = open('insider-threat-ttp-kb.json')
insider_threat_dict = json.load(insider_threat_file)
print(insider_threat_dict)

insider_threat_techniques = insider_threat_dict['techniques']

insider_threat_mitigations = []
for insider_threat_technique in insider_threat_techniques[:5]:
    print(insider_threat_technique['techniqueID'])
    insider_threat_mitigations.append(m for m in mitre_attack_data.get_mitigations_mitigating_technique(mitre_attack_data.get_object_by_attack_id(insider_threat_technique['techniqueID'], 'attack-pattern')['id']))
    insider_threat_datasources = mitre_attack_data.get_object_by_attack_id(insider_threat_technique['techniqueID'], 'attack-pattern')['x_mitre_data_sources']

for mitigation in insider_threat_mitigations:
    print(mitigation)