import plotly.graph_objects as go
from mitreattack.stix20 import MitreAttackData
import pandas as pd
from textwrap import wrap

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
          obj_to_add = [#tactic.name, mitre_attack_data.get_attack_id(tactic.id),
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
          obj_to_add = [#tactic.name, mitre_attack_data.get_attack_id(tactic.id),
                    technique_obj.name, mitre_attack_data.get_attack_id(technique_obj.id),
                    mitre_attack_data.get_attack_id(datasource.id), datasource.name
                    ]
          df.loc[len(df)] = obj_to_add
  return df

#Orders the techniques by number of linked mitigations or datasources, most to least
def order_graph_by_frequency(df):
  column_name = df.columns[2]
  df['count'] = df.groupby(column_name)[column_name].transform('count')
  df = df.sort_values('count', ascending=False)
  return df.drop('count', axis=1)

# Wraps labels at width limit
def wrap_labels(labels):
  wrapped_labels = []
  for label in labels:
    wrapped_label = "<br>".join(wrap(label, width=50))
    wrapped_labels.append(wrapped_label)
  return wrapped_labels

def parallel_categories(df, filepath):
  #Get only techniques + mitigations, or techniques + datasources
  df = order_graph_by_frequency(df[['Technique', 'Technique ID', df.columns[2], df.columns[3]]].drop_duplicates())
  dimensions=[
    # {'label':'Tactics','values':[f'{a} {b}' for a, b in zip(df['Tactic'], df['Tactic ID'])]},
    {'label':'Techniques','values':wrap_labels([f'{a} {b}' for a, b in zip(df['Technique'], df['Technique ID'])])},
    {'label': df.columns[2] + 's','values':wrap_labels([f'{a} {b}' for a, b in zip(df.iloc[:, 2], df.iloc[:, 3])])}
    ]
    #indexes were 4, 4, 5 
  fig = go.Figure(data = go.Parcats(dimensions=dimensions))
  fig.update_layout(
    hovermode="closest",
    showlegend=False,
    xaxis={'automargin': True},
    yaxis={'automargin': True},
    margin=dict(l=215, r=200, b=20, t=20, pad=None),
  ) 
  if df.columns[2] == 'Datasource':
    fig.update_layout(
      margin=dict(l=215, r=100, b=20, t=20, pad=None),
  ) 
  config = {'displayModeBar': True}
  # fig.show()
  fig.write_html(filepath, config=config)
  #just generate the div and then use the cdn link as a script tag in mds.rst
  #don't generate the html at all??? Just what I need for the graph and them style *-1.html myself? 

def main():
  mitre_attack_data = MitreAttackData("enterprise-attack-14.1.json")
  insider_threat_ttps = pd.read_csv('insider-threat-ttp-kb.csv')
  mitigations_filepath = 'docs/_static/html/mitigations-1.html'
  datasources_filepath = 'docs/_static/html/datasources-1.html'

  mitigation_columns = [#'Tactic', 'Tactic ID',
            'Technique', 'Technique ID',
            'Mitigation', 'Mitigation ID']
  datasource_columns = [#'Tactic', 'Tactic ID',
            'Technique', 'Technique ID',
            'Datasource', 'Datasource ID']

  tactics_techniques_mitigations_df = construct_dataframes(pd.DataFrame(columns= mitigation_columns), mitre_attack_data, insider_threat_ttps)
  parallel_categories(tactics_techniques_mitigations_df, mitigations_filepath)

  tactics_techniques_datasources_df = construct_dataframes(pd.DataFrame(columns= datasource_columns), mitre_attack_data, insider_threat_ttps)
  parallel_categories(tactics_techniques_datasources_df, datasources_filepath)

if __name__ == "__main__":
  main()