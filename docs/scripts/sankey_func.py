import plotly.graph_objects as go
from mitreattack.stix20 import MitreAttackData
import pandas as pd
import sphinx_plotly_directive as spd

def sankey_func():
  fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["A1", "A2", "B1", "B2", "C1", "C2"],
      color = "blue"
    ),
    link = dict(
      source = [0, 1, 0, 2, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = [2, 3, 3, 4, 4, 5],
      value = [8, 4, 2, 8, 4, 2]
  ))])

  fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
  fig.write_html('docs/_build/mitigationsanddatasources/sankey_func.html')
  return fig

def my_func():
  mitre_attack_data = MitreAttackData("enterprise-attack-14.1.json")
  insider_threat_ttps = pd.read_csv('insider-threat-ttp-kb.csv')

  labels = []
  sources = []
  targets = []

  technique_coutner = 0
  mitigation_counter = insider_threat_ttps['Technique ID'].size

  for technique_id, technique_name in zip(insider_threat_ttps['Technique ID'], insider_threat_ttps['Technique Title']):
    technique = mitre_attack_data.get_object_by_attack_id(technique_id, 'attack-pattern')
    labels.append(technique_id + ': ' + technique_name)
    mitigations_mitigating_technique = mitre_attack_data.get_mitigations_mitigating_technique(technique.id)
    for mitigation in mitigations_mitigating_technique:
      sources.append(technique_coutner)
      targets.append(mitigation_counter)

      mitigation_counter += 1
    technique_coutner += 1 
    

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
         

#source to represent source node - will be technique
#target to represent target node - will be mitigation,
#volume to set the flow volume - will be hardcoded 3 (?)
#label to show the node name - will be technique / mitigation ID + name combo (?)
my_func()