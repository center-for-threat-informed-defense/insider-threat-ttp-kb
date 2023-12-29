import plotly.graph_objects as go
from mitreattack.stix20 import MitreAttackData
import pandas as pd
import sphinx_plotly_directive as spd
import plotly.express as px

# def sankey_func():
#   fig = go.Figure(data=[go.Sankey(
#     node = dict(
#       pad = 15,
#       thickness = 20,
#       line = dict(color = "black", width = 0.5),
#       label = ["A1", "A2", "B1", "B2", "C1", "C2"],
#       color = "blue"
#     ),
#     link = dict(
#       source = [0, 1, 0, 2, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
#       target = [2, 3, 3, 4, 4, 5],
#       value = [8, 4, 2, 8, 4, 2]
#   ))])

#   fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
#   fig.write_html('docs/_build/mitigationsanddatasources/sankey_func.html')
#   return fig

def sankey():
  mitre_attack_data = MitreAttackData("enterprise-attack-14.1.json")
  insider_threat_ttps = pd.read_csv('insider-threat-ttp-kb.csv')

  labels = []
  sources = []
  targets = []

  technique_coutner = 0
  mitigation_counter = insider_threat_ttps['Technique ID'].size

  datasources_dict = {}
  mitigations_dict = {}

  #Given a list of InT Techniques:
  #Get their associated tactics, mitigations, and data sources
  tactics = [tactic for tactic in mitre_attack_data.get_tactics(remove_revoked_deprecated=True)
              if mitre_attack_data.get_attack_id(tactic.id)
                in insider_threat_ttps['Tactic ID'].values]
  
  techniques_by_tactic = [technique for tactic_shortname in 
                          [tactic.x_mitre_shortname for tactic in tactics]
                            for technique in mitre_attack_data.get_techniques_by_tactic(tactic_shortname, domain='enterprise-attack')
                              if mitre_attack_data.get_attack_id(technique.id)
                                in insider_threat_ttps['Technique ID'].values]
  
  
  mitigations_mitigating_technique = [mitre_attack_data.get_mitigations_mitigating_technique(technique_obj.id)
                                       for technique_obj in techniques_by_tactic]
  datacomponents_detecting_technique = [mitre_attack_data.get_datacomponents_detecting_technique(technique_obj.id)
                                        for technique_obj in techniques_by_tactic]
  datasources = [mitre_attack_data.get_object_by_stix_id(datacomponent["object"].x_mitre_data_source_ref)
                  for datacomponent in datacomponents_detecting_technique]
  
  
  
  
  # for tactic_shortname in [tactic.x_mitre_shortname for tactic in tactics]:
  #   techniques_by_tactic = [technique for technique in 
  #                           mitre_attack_data.get_techniques_by_tactic(tactic_shortname, domain='enterprise-attack')
  #                             if mitre_attack_data.get_attack_id(technique.id) in 
  #                             insider_threat_ttps['Technique ID'].values]
    
  techniques = [technique for technique in mitre_attack_data.get_techniques_by_tactic([tactic.shortname for tactic in tactics], domain='enterprise-attack') if mitre_attack_data.get_attack_id(technique.id) in insider_threat_ttps['Technique ID'].values]
  for technique_id, technique_name in zip(insider_threat_ttps['Technique ID'], insider_threat_ttps['Technique Title']):
    technique_obj = mitre_attack_data.get_object_by_attack_id(technique_id, 'attack-pattern')
    mitigations_mitigating_technique = mitre_attack_data.get_mitigations_mitigating_technique(technique_obj.id)
    datacomponents_detecting_technique = mitre_attack_data.get_datacomponents_detecting_technique(technique_obj.id)
    datasources = [mitre_attack_data.get_object_by_stix_id(datacomponent["object"].x_mitre_data_source_ref) for datacomponent in datacomponents_detecting_technique]





  ############################

  for technique_id, technique_name in zip(insider_threat_ttps['Technique ID'], insider_threat_ttps['Technique Title']):
    technique = mitre_attack_data.get_object_by_attack_id(technique_id, 'attack-pattern')
    # labels.append(technique_id + ': ' + technique_name)
    datasources_dict[technique_id] = [technique.name]
    mitigations_dict[technique_id] = [technique.name]

    mitigations_mitigating_technique = mitre_attack_data.get_mitigations_mitigating_technique(technique.id)
    datacomponents_detecting_technique = mitre_attack_data.get_datacomponents_detecting_technique(technique.id)
    for mitigation in mitigations_mitigating_technique:
      sources.append(technique_coutner)
      targets.append(mitigation_counter)

    for datacomponent in datacomponents_detecting_technique:
      datasource = mitre_attack_data.get_object_by_stix_id(datacomponent["object"].x_mitre_data_source_ref)
      datasources_dict[technique_id].append([mitre_attack_data.get_attack_id(datasource.id), datasource.name])
  fig = go.Figure(data=[go.Sankey(
  node = dict(
    pad = 15,
    thickness = 20,
    line = dict(color = "black", width = 0.5),
    label = labels,
    color = "blue"
  ),
  link = dict(
    source = sources, # indices correspond to labels, eg A1, A2, A1, B1, ...
    target = targets,
    value = [3] * len(sources)
    ))])

  fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
  spd.save_plotly_figure(fig, 'docs/_static/html/mitigationsanddatasources-1.html')

# I want a numeric index on the far left column
# tactics, techniques, mitigations, data sources, size (left to right)
# dimensions
"""
dimensions=[
{'label':'Technique',
'values':[]},
{'label':'Data Sources',
'values':[]},
'label':'Mitigations',
'values':[]}
]
"""

def parallel_categories():
  df = px.data.tips()
  fig = px.parallel_categories(df, dimensions=['sex', 'smoker', 'day'],
        color="size", color_continuous_scale=px.colors.sequential.Inferno,
        labels={'sex':'Payer sex', 'smoker':'Smokers at the table', 'day':'Day of week'})

  fig = px.parallel_categories(df, dimensions=df.columns(),
        color="size", color_continuous_scale=px.colors.sequential.Inferno,
        labels={})


         

#source to represent source node - will be technique
#target to represent target node - will be mitigation,
#volume to set the flow volume - will be hardcoded 3 (?)
#label to show the node name - will be technique / mitigation ID + name combo (?)
# parallel_categories()
sankey()