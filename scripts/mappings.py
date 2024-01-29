from mitreattack.stix20 import MitreAttackData
import pandas as pd
# from textwrap import wrap

def construct_dataframes(df, mitre_attack_data, insider_threat_ttps):

  #Given a list of InT Techniques:
  #Get their associated mitigations and data sources
  for technique_id in insider_threat_ttps['Technique ID']:
      technique_obj = mitre_attack_data.get_object_by_attack_id(technique_id, 'attack-pattern')
    
      if 'Mitigation IDs' in df.columns:
        mitigations_mitigating_technique = mitre_attack_data.get_mitigations_mitigating_technique(technique_obj.id)

        mitigation_ids = [mitre_attack_data.get_attack_id(mitigation["object"].id) for mitigation in mitigations_mitigating_technique]
        # mitigation_ids_and_links = ['`' + mitre_attack_data.get_attack_id(mitigation["object"].id)  +
        #                              ' <' + mitigation["object"].external_references[0].url +
        #                              '>`_' for mitigation in mitigations_mitigating_technique]
        df.loc[len(df)] = ['`' + technique_id + ' <' + technique_obj.external_references[0].url + '>`_',
                            str(mitigation_ids).translate({ord(i): None for i in '[]\''})]
      #Datasources
      else:
        datacomponents_detecting_technique = mitre_attack_data.get_datacomponents_detecting_technique(technique_obj.id)
        datasources_detecting_technique = []
        datasource_ids = []
        for datacomponent in datacomponents_detecting_technique:
          if mitre_attack_data.get_object_by_stix_id(datacomponent["object"].x_mitre_data_source_ref) not in datasources_detecting_technique:
            datasources_detecting_technique.append(mitre_attack_data.get_object_by_stix_id(datacomponent["object"].x_mitre_data_source_ref))

        for datasource in datasources_detecting_technique:
          datasource_ids.append(mitre_attack_data.get_attack_id(datasource.id))
        
        df.loc[len(df)] = ['`' + technique_id + ' <' + technique_obj.external_references[0].url + '>`_',
                            str(datasource_ids).translate({ord(i): None for i in '[]\''})]
  return df

def main():
  mitre_attack_data = MitreAttackData("enterprise-attack-14.1.json")
  insider_threat_ttps = pd.read_csv('insider-threat-ttp-kb.csv')

  mitigation_columns = ['Technique ID', 'Mitigation IDs']
  datasource_columns = ['Technique ID', 'Datasource IDs']

  techniques_mitigations_df = construct_dataframes(pd.DataFrame(columns= mitigation_columns), mitre_attack_data, insider_threat_ttps)
  techniques_mitigations_df.to_csv(r'docs\extra\mitigations.csv', mode='w', index=False)

  techniques_datasources_df = construct_dataframes(pd.DataFrame(columns= datasource_columns), mitre_attack_data, insider_threat_ttps)
  techniques_datasources_df.to_csv(r'docs\extra\datasources.csv', mode='w', index=False)

if __name__ == "__main__":
  main()