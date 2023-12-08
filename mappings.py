from mitreattack.stix20 import MitreAttackData

import pandas as pd

def main():
    #Download https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json
    #to ../scripts
    mitre_attack_data = MitreAttackData("enterprise-attack-14.1.json")
    insider_threat_ttps = pd.read_csv('insider-threat-ttp-kb.csv')

    # get data components detecting insider threat technique
    output_dict = {}
    for technique_id in insider_threat_ttps['Technique ID']:
        technique = mitre_attack_data.get_object_by_attack_id(technique_id, 'attack-pattern')
        datacomponents_detecting_technique = mitre_attack_data.get_datacomponents_detecting_technique(technique.id)
        mitigations_mitigating_technique = mitre_attack_data.get_mitigations_mitigating_technique(technique.id)

        output_dict[technique_id] = [technique.name]

        for datacomponent in datacomponents_detecting_technique:
            datasource = mitre_attack_data.get_object_by_stix_id(datacomponent["object"].x_mitre_data_source_ref)
            print(mitre_attack_data.get_attack_id(datasource.id)) #this is DS####
            output_dict[technique_id].append([mitre_attack_data.get_attack_id(datasource.id), datasource.name])

        for mitigation in mitigations_mitigating_technique:
            print(mitre_attack_data.get_attack_id(mitigation["object"].id)) #this is M####
            output_dict[technique_id].append([mitre_attack_data.get_attack_id(mitigation["object"].id), mitigation["object"].name])

    output_df = pd.DataFrame.transpose(pd.DataFrame.from_dict(output_dict, orient='index'))
    output_df.to_csv('output.csv')

if __name__ == "__main__":
    main()


















# mitre_attack_data = MitreAttackData('enterprise-attack-14.1.json')
# mitre_attack_dict = stixToDf.techniquesToDf(attackToExcel.get_stix_data("enterprise-attack"), "enterprise-attack")

# insider_threat_df = pd.read_csv('insider-threat-ttp-kb.csv')
# print('here')
# mitre_attack_dict['techniques'] = mitre_attack_dict['techniques'][mitre_attack_dict['techniques']['ID'].isin(insider_threat_df['Technique ID'])]
# data_sources = mitre_attack_data.get_objects_by_type('x-mitre-data-source')
# for ds in data_sources:
#     print(mitre_attack_data.get_attack_id(ds))
# print('here')


# mitigations = []

# for technique_stix_id in mitre_attack_dict['techniques']['STIX ID'].values:
#     mitigations.append(mitre_attack_data.get_mitigations_mitigating_technique(technique_stix_id))
    
