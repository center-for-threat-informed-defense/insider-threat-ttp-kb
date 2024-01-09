import plotly.graph_objects as go
from mitreattack.stix20 import MitreAttackData
import pandas as pd

def construct_dataframes(df, mitre_attack_data, insider_threat_ttps):

  #Given a list of InT Techniques:
  #Get their associated tactics, mitigations, and data sources
  tactics = [tactic for tactic in mitre_attack_data.get_tactics(remove_revoked_deprecated=True)
              if mitre_attack_data.get_attack_id(tactic.id)
                in insider_threat_ttps['Tactic ID'].values]
  
  for tactic in tactics: 
    tactic_shortname = tactic.x_mitre_shortname
  
    techniques_by_tactic = [technique for technique in mitre_attack_data.get_techniques_by_tactic(tactic_shortname, domain='enterprise-attack')
                                if mitre_attack_data.get_attack_id(technique.id)
                                  in insider_threat_ttps['Technique ID'].values]
    
    for technique_obj in techniques_by_tactic:
      
      #Mitigations
      if 'Mitigation' in df.columns:
        mitigations_mitigating_technique = mitre_attack_data.get_mitigations_mitigating_technique(technique_obj.id)

        for mitigation in mitigations_mitigating_technique:
          obj_to_add = [tactic.name, mitre_attack_data.get_attack_id(tactic.id),
                            technique_obj.name, mitre_attack_data.get_attack_id(technique_obj.id),
                            mitigation["object"].name, mitre_attack_data.get_attack_id(mitigation["object"].id),
                            ]
          df.loc[len(df)] = obj_to_add

      #Datasources
      else:
        datacomponents_detecting_technique = mitre_attack_data.get_datacomponents_detecting_technique(technique_obj.id)
        datasources_detecting_technique = []
        for datacomponent in datacomponents_detecting_technique:
          if mitre_attack_data.get_object_by_stix_id(datacomponent["object"].x_mitre_data_source_ref) not in datasources_detecting_technique:
            datasources_detecting_technique.append(mitre_attack_data.get_object_by_stix_id(datacomponent["object"].x_mitre_data_source_ref))

        for datasource in datasources_detecting_technique:
          obj_to_add = [tactic.name, mitre_attack_data.get_attack_id(tactic.id),
                    technique_obj.name, mitre_attack_data.get_attack_id(technique_obj.id),
                    mitre_attack_data.get_attack_id(datasource.id), datasource.name
                    ]
          df.loc[len(df)] = obj_to_add
  return df

def parallel_categories(df, filepath):
  dimensions=[
    {'label':'Tactics','values':[f'{a} {b}' for a, b in zip(df['Tactic'], df['Tactic ID'])]},
    {'label':'Techniques','values':[f'{a} {b}' for a, b in zip(df['Technique'], df['Technique ID'])]},
    {'label': df.columns[4] + 's','values':[f'{a} {b}' for a, b in zip(df.iloc[:, 4], df.iloc[:, 5])]}
    ]

  fig = go.Figure(go.Parcats(dimensions=dimensions))
  fig.update_layout(
    margin=dict(
        l=200,
        r=200,
        b=20,
        t=20,
        pad=4
    )
  )

  config = {'displayModeBar': True}
  fig.write_html(filepath, config=config)

def main():
  mitre_attack_data = MitreAttackData("enterprise-attack-14.1.json")
  insider_threat_ttps = pd.read_csv('insider-threat-ttp-kb.csv')
  mitigations_filepath = 'docs/_static/html/mitigations-1.html'
  datasources_filepath = 'docs/_static/html/datasources-1.html'

  mitigation_columns = ['Tactic', 'Tactic ID',
            'Technique', 'Technique ID',
            'Mitigation', 'Mitigation ID']
  datasource_columns = ['Tactic', 'Tactic ID',
            'Technique', 'Technique ID',
            'Datasource', 'Datasource ID']

  tactics_techniques_mitigations_df = construct_dataframes(pd.DataFrame(columns= mitigation_columns), mitre_attack_data, insider_threat_ttps)
  parallel_categories(tactics_techniques_mitigations_df, mitigations_filepath)

  tactics_techniques_datasources_df = construct_dataframes(pd.DataFrame(columns= datasource_columns), mitre_attack_data, insider_threat_ttps)
  parallel_categories(tactics_techniques_datasources_df, datasources_filepath)

if __name__ == "__main__":
  main()