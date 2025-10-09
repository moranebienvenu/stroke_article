# import nbformat
# import requests
# import plotly.graph_objects as go
# import pandas as pd
# import json
# from IPython.display import display, HTML
# import ipywidgets as widgets
# from ipywidgets import interact, Dropdown, SelectMultiple, Checkbox
# from ipywidgets import HBox, VBox, GridBox, Layout
# import numpy as np
# from plotly.subplots import make_subplots

# class DashNeuroTmapClient:
#     def __init__(self, dash_url="http://127.0.0.1:8050"):
#         """
#         Client pour interagir avec l'application Dash
        
#         Args:
#             dash_url: URL de base de l'application Dash
#         """
#         self.base_url = dash_url
#         self.api_url = f"{dash_url}/api"
#         self.current_plots = None
#         self.overlays = []
        
#     def check_health(self):
#         """Vérifie si l'API Dash est accessible"""
#         try:
#             response = requests.get(f"{self.api_url}/health", timeout=5)
#             if response.status_code == 200:
#                 data = response.json()
#                 print("✅ Dash API is healthy!")
#                 print(f"Available datasets: {data['available_datasets']}")
#                 return True
#             else:
#                 print(f"❌ API health check failed: {response.status_code}")
#                 return False
#         except Exception as e:
#             print(f"❌ Cannot connect to Dash API: {e}")
#             print(f"Make sure your Dash app is running on {self.base_url}")
#             return False
    
#     def get_available_subjects(self, dataset='master'):
#         """Récupère la liste des sujets disponibles"""
#         try:
#             response = requests.get(f"{self.api_url}/subjects", 
#                                   params={'dataset': dataset}, timeout=10)
#             if response.status_code == 200:
#                 return response.json()
#             else:
#                 print(f"Error getting subjects: {response.status_code}")
#                 return None
#         except Exception as e:
#             print(f"Error: {e}")
#             return None
    
#     def generate_plots(self, dataset='master', analysis_type='session_sex', 
#                       session='V1', sex_filter='men', groups='A', subject=None, title=None):
#         """
#         Génère des graphiques via l'API Dash
        
#         Args:
#             dataset: 'master', 'dataset1', ou 'dataset2'
#             analysis_type: 'single' ou 'session_sex'
#             session: 'V1', 'V2', ou 'V3'
#             sex_filter: 'all', 'men', ou 'women'
#             groups: Liste des groupes (ex: ['A', 'B', 'C'])
#             subject: ID du sujet (requis pour analysis_type='single')
#             title: Titre personnalisé pour l'overlay
#         """

#         payload = {
#             'dataset': dataset,
#             'analysis_type': analysis_type,
#             'session': session,
#             'sex_filter': sex_filter,
#             'groups': groups,
#             'title': title
#         }
        
#         if subject:
#             payload['subject'] = subject
            
#         try:
#             response = requests.post(f"{self.api_url}/generate_plots", 
#                                    json=payload, timeout=30)
            
#             if response.status_code == 200:
#                 data = response.json()
#                 self.current_plots = data['plots']
#                 print(f"✅ {data['message']}")
#                 return data['plots']
#             else:
#                 error_data = response.json()
#                 print(f"❌ Error: {error_data.get('error', 'Unknown error')}")
#                 return None
                
#         except Exception as e:
#             print(f"❌ Request failed: {e}")
#             return None
    
#     def update_plots(self, **kwargs):
#         """Met à jour les graphiques actuels avec de nouveaux paramètres"""
#         try:
#             response = requests.put(f"{self.api_url}/update_plots", 
#                                   json=kwargs, timeout=30)
            
#             if response.status_code == 200:
#                 data = response.json()
#                 self.current_plots = data['plots']
#                 print(f"✅ Plots updated successfully")
#                 return data['plots']
#             else:
#                 error_data = response.json()
#                 print(f"❌ Update failed: {error_data.get('error', 'Unknown error')}")
#                 return None
                
#         except Exception as e:
#             print(f"❌ Update failed: {e}")
#             return None
    
#     def get_current_plots(self):
#         """Récupère les graphiques actuels"""
#         try:
#             response = requests.get(f"{self.api_url}/get_plots", timeout=10)
            
#             if response.status_code == 200:
#                 data = response.json()
#                 self.current_plots = data['plots']
#                 return data['plots']
#             else:
#                 error_data = response.json()
#                 print(f"❌ Error: {error_data.get('error', 'No plots available')}")
#                 return None
                
#         except Exception as e:
#             print(f"❌ Failed to get plots: {e}")
#             return None
    
#     def display_plots(self, plots_data=None):
#         """Affiche les 3 graphiques Plotly côte à côte"""
#         if plots_data is None:
#             plots_data = self.current_plots
            
#         if not plots_data:
#             print("No plots to display. Generate plots first.")
#             return None
        
#         try:
#             fig1 = go.Figure(plots_data['fig1'])
#             fig2 = go.Figure(plots_data['fig2'])
#             fig3 = go.Figure(plots_data['fig3'])
            
#             for fig in [fig1, fig2, fig3]:
#                 fig.update_layout(height=350,width=350, margin=dict(l=40, r=40, t=40, b=40),
#                     legend=dict(
#                         orientation="h",
#                         yanchor="bottom",
#                         y=-0.3,
#                         xanchor="center",
#                         x=0.5
#                 )   )
            
#             # organisation en grille (3 colonnes)
#             display(GridBox(
#                 children=[
#                     go.FigureWidget(fig1),
#                     go.FigureWidget(fig2),
#                     go.FigureWidget(fig3)
#                 ],
#                 layout=Layout(grid_template_columns="repeat(3, 33%)")
#             ))
            
#             return fig1, fig2, fig3
        
#         except Exception as e:
#             print(f"❌ Error displaying plots: {e}")
#             return None

#     def generate_overlay(self, dataset='master', analysis_type='session_sex', 
#                         session='V1', sex_filter='women', groups='A', 
#                         subject=None, title=None):
#         """
#         Génère un overlay avec état naturel
        
#         Args:
#             dataset: 'master', 'dataset1', ou 'dataset2'
#             analysis_type: 'single' ou 'session_sex' (défaut: session_sex)
#             session: 'V1', 'V2', ou 'V3' (défaut: V1)
#             sex_filter: 'all', 'men', ou 'women' (défaut: women)
#             groups: Liste des groupes
#             subject: ID du sujet (pour analysis_type='single')
#             title: Titre personnalisé pour l'overlay
#         """
#         if groups is None:
#             groups = ['NA', 'A', 'B', 'W', 'G', 'C', 'AN', 'TCM', 'TCS', 'TCMix']
        
#         if title is None:
#             title = f"Session {session}"
#             if sex_filter != 'all':
#                 title += f" ({'Men' if sex_filter == 'men' else 'Women'})"
#             # if groups:
#             #     title += f" | Groups: {', '.join(groups)}"
        
#         payload = {
#             'dataset': dataset,
#             'analysis_type': analysis_type,
#             'session': session,
#             'sex_filter': sex_filter,
#             'groups': groups,
#             'title': title
#         }
        
#         if subject:
#             payload['subject'] = subject
            
#         try:
#             response = requests.post(f"{self.api_url}/overlay/generate", 
#                                    json=payload, timeout=30)
            
#             if response.status_code == 200:
#                 data = response.json()
#                 print(f"✅ {data['message']}")
#                 self.overlays.append(data['overlay'])
#                 return data['overlay']
#             else:
#                 error_data = response.json()
#                 print(f"❌ Error: {error_data.get('error', 'Unknown error')}")
#                 return None
                
#         except Exception as e:
#             print(f"❌ Overlay generation failed: {e}")
#             return None

#     def get_combined_plots(self):
#         """Récupère les graphiques combinés (base + overlays)"""
#         try:
#             response = requests.get(f"{self.api_url}/overlay/combine", timeout=10)
#             if response.status_code == 200:
#                 data = response.json()
#                 return data['combined_plots']
#             return None
#         except Exception as e:
#             print(f"Error getting combined plots: {e}")
#             return None
    
#     def display_combined_plots(self):
#         """Affiche les graphiques combinés avec overlays"""
#         combined_data = self.get_combined_plots()
#         if not combined_data:
#             print("No combined plots available. Generate base plots and overlays first.")
#             return None
        
#         try:
#             fig1 = go.Figure(combined_data['fig1'])
#             fig2 = go.Figure(combined_data['fig2'])
#             fig3 = go.Figure(combined_data['fig3'])
            
#             # Améliorer la légende
#             for fig in [fig1, fig2, fig3]:
#                 fig.update_layout(
#                     height=350,
#                     width=350, 
#                     margin=dict(l=40, r=40, t=40, b=40),
#                     legend=dict(
#                         orientation="h",
#                         yanchor="bottom",
#                         y=-0.3,
#                         xanchor="center",
#                         x=0.5
#                     )
#                 )
            
#             # organisation en grille (3 colonnes) - identique à display_plots
#             display(GridBox(
#                 children=[
#                     go.FigureWidget(fig1),
#                     go.FigureWidget(fig2),
#                     go.FigureWidget(fig3)
#                 ],
#                 layout=Layout(grid_template_columns="repeat(3, 33%)")
#             ))
            
#             return fig1, fig2, fig3
            
#         except Exception as e:
#             print(f"Error displaying combined plots: {e}")
#             return None
            
#     def create_advanced_interface(self):
#         """Interface avancée avec gestion des overlays"""
#         subjects_data = self.get_available_subjects(dataset="master")
#         if not subjects_data:
#             print("Cannot create interface: no subjects data available")
#             return None

#         # Widgets pour la base
#         base_session = Dropdown(options=['V1', 'V2', 'V3'], value='V1', description='Base Session:')
#         base_sex = Dropdown(options=['all', 'men', 'women'], value='men', description='Base Sex:')
        
#         # Widgets pour l'overlay (seulement session et sexe)
#         overlay_session = Dropdown(options=['V1', 'V2', 'V3'], value='V1', description='Overlay Session:')
#         overlay_sex = Dropdown(options=['all', 'men', 'women'], value='women', description='Overlay Sex:')
        
#         # Container pour les graphiques
#         plot_output = widgets.Output()

#         observers_active = False
        
#         def display_base_with_overlay():
#             """Affiche base + overlay (état par défaut)"""
#             with plot_output:
#                 plot_output.clear_output(wait=True)
                
#                 # Effacer les overlays existants
#                 self.clear_overlays()

#                 # Créer un titre personnalisé SANS les groupes pour la base
#                 base_title = f"Session {base_session.value}"
#                 if base_sex.value != 'all':
#                     base_title += f" ({'Men' if base_sex.value == 'men' else 'Women'})"
                
#                 # Générer la base
#                 base_plots = self.generate_plots(
#                     dataset="master",
#                     analysis_type="session_sex",
#                     session=base_session.value,
#                     sex_filter=base_sex.value,
#                     groups=['A'],
#                     title=base_title
#                 )
                
#                 if base_plots:
#                     # Générer l'overlay (groupes fixes pour l'état naturel)
#                     overlay_plots = self.generate_overlay(
#                         dataset="master",
#                         analysis_type="session_sex",
#                         session=overlay_session.value,
#                         sex_filter=overlay_sex.value,
#                         groups=['A']  # Groupe fixe pour l'état naturel
#                     )
                    
#                     if overlay_plots:
#                         self.display_combined_plots()
#                     else:
#                         self.display_plots(base_plots)
         
        
#         def reset_to_default():
#             """Réinitialise tous les widgets aux valeurs par défaut"""
#             base_session.value = 'V1'
#             base_sex.value = 'men'
#             overlay_session.value = 'V1'
#             overlay_sex.value = 'women'
            

#         # Afficher l'interface de manière contrôlée
#         interface_elements = [
#             HBox([base_session, base_sex]),
#             HBox([overlay_session, overlay_sex]),
#             HBox([widgets.Button(description="🔄 Reset to Default", button_style='warning')]),
#             plot_output
#         ]
    
#         # Afficher tous les éléments
#         for element in interface_elements:
#             display(element)
        
#         # Configurer le bouton reset
#         reset_btn = interface_elements[2].children[0]  # Récupérer le bouton
#         reset_btn.on_click(lambda b: reset_to_default())
        
#         # Premier affichage (base + overlay par défaut)
#         display_base_with_overlay()
        
        
#         # Lier les événements des widgets - mise à jour automatique
#         def on_any_change(change):
#             """Quand un paramètre change, mettre à jour base + overlay"""
#             if observers_active:
#                 display_base_with_overlay()
        
#         observers_active = True
#         # Tous les widgets déclenchent une mise à jour automatique
#         for widget in [base_session, base_sex, overlay_session, overlay_sex]:
#             widget.observe(on_any_change, names='value')
        
#         return None 
        
#     def clear_overlays(self):
#         """Efface tous les overlays localement et via l'API"""
#         self.overlays = []
#         try:
#             response = requests.delete(f"{self.api_url}/overlay/clear", timeout=10)
#             if response.status_code == 200:
#                 return True
#             return False
#         except Exception as e:
#             return False

#     def generate_correlation_heatmaps(self, dataset='master', session='V1', 
#                                         system_type='Synaptic ratio', groups=['A']):
#             """
#             Génère des heatmaps de corrélation identiques à celles du Dash
#             """
#             payload = {
#                 'dataset': dataset,
#                 'session': session,
#                 'system_type': system_type,
#                 'groups': groups
#             }
            
#             try:
#                 response = requests.post(f"{self.api_url}/correlation/generate_heatmaps", 
#                                     json=payload, timeout=30)
                
#                 if response.status_code == 200:
#                     data = response.json()
#                     return data['heatmaps']
#                 else:
#                     error_data = response.json()
#                     print(f"❌ Error: {error_data.get('error', 'Unknown error')}")
#                     return None
                    
#             except Exception as e:
#                 print(f"❌ Heatmap generation failed: {e}")
#                 return None

#    #Affichez 3 heatmaps côte à côte, "All", "Men" et "Women", pour même variable, même session
#     def display_correlation_heatmaps(self, heatmaps_data=None):
#         """Affiche les 3 heatmaps de corrélation identiques à Dash"""
#         if heatmaps_data is None:
#             heatmaps_data = self.get_correlation_heatmaps()
            
#         if not heatmaps_data:
#             #print("No correlation heatmaps to display. Generate heatmaps first.")
#             return None
        
#         try:
#             figures = []
#             titles = ['All Subjects', 'Men Only', 'Women Only']
            
#             for i, sex_filter in enumerate(['all', 'men', 'women']):
#                 if (sex_filter in heatmaps_data and 
#                     heatmaps_data[sex_filter]['status'] == 'success'):
                    
#                     # Utiliser directement la figure Plotly générée par Dash
#                     fig_dict = heatmaps_data[sex_filter]['heatmap']
#                     fig = go.Figure(fig_dict)
                    
#                     # Ajuster seulement la taille pour l'affichage côte à côte
#                     fig.update_layout(
#                         height=450,
#                         width=450,
#                         margin=dict(l=60, r=30, t=80, b=100),
#                         title_x=0.5
#                     )
                    
#                     figures.append(fig)
#                 else:
#                     # Créer une figure vide avec message d'erreur
#                     fig = go.Figure()
#                     fig.add_annotation(
#                         text=f"No data for {titles[i]}",
#                         xref="paper", yref="paper",
#                         x=0.5, y=0.5, xanchor='center', yanchor='middle',
#                         showarrow=False,
#                         font=dict(size=14, color="red")
#                     )
#                     fig.update_layout(
#                         height=450,
#                         width=450,
#                         title=dict(
#                             text=titles[i],
#                             x=0.5,
#                             xanchor='center'
#                         ),
#                         xaxis=dict(showticklabels=False),
#                         yaxis=dict(showticklabels=False)
#                     )
#                     figures.append(fig)
            
#             # # Supprimer l'erreur de la sortie -- modification test
#             # import warnings
#             # with warnings.catch_warnings():
#             #     warnings.simplefilter("ignore")
                
#             #     # Capturer la sortie stderr
#             #     import sys
#             #     from io import StringIO
#             #     old_stderr = sys.stderr
#             #     sys.stderr = StringIO()
            
#                 try:
#                     # Afficher les 3 heatmaps côte à côte
#                     display(GridBox(
#                         children=[
#                             go.FigureWidget(figures[0]),
#                             go.FigureWidget(figures[1]),
#                             go.FigureWidget(figures[2])
#                         ],
#                         layout=Layout(
#                             grid_template_columns="repeat(3, 33%)",
#                             width="100%",
#                             justify_content="space-around"
#                         )
#                     ))
#                 except Exception as e:
#                     if "nbformat" in str(e):
#                         print("⚠️ Please install nbformat>=4.2.0 to enable interactive Plotly display.")
#                     else:
#                         pass
#                         #print(f"❌ Display error: {e}")
#                 # finally:
#                 #     sys.stderr = old_stderr
            
#             return figures
            
#         except Exception as e:
#             print(f"❌ Error displaying correlation heatmaps: {e}")
#             return None


#     def create_correlation_interface(self):
#         """Interface interactive pour les heatmaps de corrélation """
        
#         subjects_data = self.get_available_subjects(dataset="master")
#         if not subjects_data:
#             print("Cannot create interface: no subjects data available")
#             return None

#         # Widgets de configuration 
#         session_widget = widgets.Dropdown(
#             options=['V1', 'V2', 'V3'],
#             value='V1',
#             description='Session:'
#         )

#         system_widget = widgets.Dropdown(
#             options=['Synaptic ratio', 'Neurotransmitter (Loc)', 'Neurotransmitter (Tract)', 'Clinical Outcomes'],
#             value='Synaptic ratio',
#             description='System:'
#         )

#         groups_widget = widgets.Dropdown(
#             options=['A', 'NA'],  
#             value='A',
#             description='Groups:'
#         )

#         #  Bouton reset 
#         reset_btn = widgets.Button(
#             description='🔄 Reset to Default',
#             button_style='warning',
#             layout=widgets.Layout(width='200px')
#         )

#         # Container pour les graphiques 
#         plot_output = widgets.Output()

#         observers_active = False
        
#         def display_heatmaps():
#             """Affiche les 3 heatmaps côte à côte"""
#             with plot_output:
#                 plot_output.clear_output(wait=True)
                
#                 try:
#                     heatmaps_data = self.generate_correlation_heatmaps(
#                         session=session_widget.value,
#                         system_type=system_widget.value,
#                         groups=groups_widget.value
#                     )

#                     if heatmaps_data:
#                         self.display_correlation_heatmaps(heatmaps_data)
#                     else:
#                         print("❌ No heatmaps generated (missing data or server error)")
#                 except Exception as e:
#                     print(f"❌ Error displaying heatmaps: {e}")
        
#         def reset_to_default(_=None):
#             """Réinitialise tous les widgets aux valeurs par défaut"""
#             session_widget.value = 'V1'
#             system_widget.value = 'Synaptic ratio'
#             groups_widget.value = ['A']
        
#         # Configuration du bouton reset
#         reset_btn.on_click(reset_to_default)

#         # Afficher l'interface de manière contrôlée 
#         interface_elements = [
#             widgets.HBox([session_widget,system_widget,groups_widget]),
#             #widgets.HBox([system_widget, groups_widget]),
#             widgets.HBox([reset_btn]),
#             plot_output
#         ]

#         # Afficher tous les éléments
#         for element in interface_elements:
#             display(element)
        
#         #  Lier les événements des widgets - mise à jour automatique
#         def on_any_change(change):
#             """Quand un paramètre change, mettre à jour les heatmaps"""
#             if observers_active:
#                 display_heatmaps()
        
#         observers_active = True
#         # Tous les widgets déclenchent une mise à jour automatique
#         for widget in [session_widget, system_widget, groups_widget]:
#             widget.observe(on_any_change, names='value')
        
#         # Premier affichage (comme create_advanced_interface)
#         display_heatmaps()
    
#         return None
   
   
#     #Heatmap avec variables croisée et interactive  
#     def generate_cross_correlation_heatmap(self, dataset='master',
#                                         session1='V1', sex_filter1='All', outcome1='Synaptic ratio', groups1=['A'],
#                                         session2='V1', sex_filter2='All', outcome2='Synaptic ratio', groups2=['A']):
#         """Génère une heatmap de corrélation croisée entre deux sets"""
#         payload = {
#             'dataset': dataset,
#             'session1': session1,
#             'sex_filter1': sex_filter1,
#             'outcome1': outcome1,
#             'groups1': groups1,
#             'session2': session2,
#             'sex_filter2': sex_filter2,
#             'outcome2': outcome2,
#             'groups2': groups2
#         }
        
#         try:
#             response = requests.post(f"{self.api_url}/correlation/generate_cross_heatmaps", 
#                                 json=payload, timeout=30)
            
#             if response.status_code == 200:
#                 data = response.json()
#                 return data
#             else:
#                 error_data = response.json()
#                 print(f"❌ Error: {error_data.get('error', 'Unknown error')}")
#                 return None
                
#         except Exception as e:
#             print(f"❌ Cross correlation generation failed: {e}")
#             return None

#     def create_interactive_correlation_interface_auto(self):

#         """Interface interactive avec mise à jour automatique"""
    
#         from IPython.display import display, clear_output
        
#         # Widgets pour Set 1
#         session1 = widgets.Dropdown(options=['V1', 'V2', 'V3'], value='V1', description='Session 1:')
#         sex1 = widgets.Dropdown(options=['All', 'Men only', 'Women only'], value='Men only', description='Sex 1:')
#         outcome1 = widgets.Dropdown(
#             options=['Synaptic ratio', 'Neurotransmitter (Loc)', 
#                     'Neurotransmitter (Tract)', 'Clinical Outcomes'],
#             value='Synaptic ratio',
#             description='Outcome 1:'
#         )
        
#         # Widgets pour Set 2
#         session2 = widgets.Dropdown(options=['V1', 'V2', 'V3'], value='V1', description='Session 2:')
#         sex2 = widgets.Dropdown(options=['All', 'Men only', 'Women only'], value='Men only', description='Sex 2:')
        
#         outcome2 = widgets.Dropdown(
#             options=['Synaptic ratio', 'Neurotransmitter (Loc)', 
#                     'Neurotransmitter (Tract)', 'Clinical Outcomes'],
#             value='Synaptic ratio',
#             description='Outcome 2:'
#         )
        
       
#         permanent_message = widgets.HTML(
#             value="""
#             <div style='
#                 background-color: #e3f2fd; 
#                 border: 1px solid #2196f3; 
#                 border-radius: 5px; 
#                 padding: 8px; 
#                 margin: 10px 0;
#                 color: #1565c0;
#                 font-size: 14px;
#             '>
#             💡 <b>Note:</b> You must choose the same sex group for each subject set to obtain correlation analysis
#             </div>
#             """
#         )

#         # Container pour la figure et les stats
#         output_container = widgets.VBox()
#         observers_active = False
        
#         def update_heatmap():
#             result = self.generate_cross_correlation_heatmap(
#                 dataset='master',
#                 session1=session1.value,
#                 sex_filter1=sex1.value,
#                 outcome1=outcome1.value,
#                 groups1=['A'],
#                 session2=session2.value,
#                 sex_filter2=sex2.value,
#                 outcome2=outcome2.value,
#                 groups2=['A']
#             )
            
#             if result and result['status'] == 'success':
#                 # Créer un NOUVEAU FigureWidget à chaque mise à jour
#                 fig = go.FigureWidget(result['heatmap'])
                
#                 # Créer le widget de statistiques
#                 stats_text = widgets.HTML(
#                     value=f"<p><b>Set 1:</b> {result['subject_count_set1']} subjects | "
#                         f"<b>Set 2:</b> {result['subject_count_set2']} subjects | "
#                         f"<b>Common:</b> {result['common_subjects']} subjects</p>"
#                 )
                
#                 # Mettre à jour le container avec la nouvelle figure
#                 output_container.children = [stats_text, fig]
#             else:
#                 error_text = widgets.HTML(value="<p style='color: red;'>Failed to generate heatmap</p>")
#                 output_container.children = [error_text]
        
#         def on_change(change):
#             if observers_active:
#                 update_heatmap()
        
#         # Organisation de l'interface
#         set1_controls = widgets.VBox([
#             widgets.HTML("<h3>Set 1 Parameters</h3>"),
#             session1, sex1, outcome1
#         ])
        
#         set2_controls = widgets.VBox([
#             widgets.HTML("<h3>Set 2 Parameters</h3>"),
#             session2, sex2, outcome2
#         ])
        
#         controls = widgets.HBox([set1_controls, set2_controls])
        
#         display(controls)
#         display(permanent_message)
#         display(output_container)
        
#         # Affichage initial
#         update_heatmap()
        
#         # Activer les observers après le premier affichage
#         observers_active = True
#         for widget in [session1, sex1, outcome1, session2, sex2, outcome2]:
#             widget.observe(on_change, names='value')
import requests
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
from IPython.display import HTML, display

class DashNeuroTmapClient:
    def __init__(self, dash_url="http://127.0.0.1:8050"):
        self.base_url = dash_url
        self.api_url = f"{dash_url}/api"
        self.current_plots = None
        self.overlays = []
        
    def check_health(self):
        try:
            response = requests.get(f"{self.api_url}/health", timeout=5)
            if response.status_code == 200:
                data = response.json()
                print("✅ Dash API is healthy!")
                print(f"Available datasets: {data['available_datasets']}")
                return True
            else:
                print(f"❌ API health check failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Cannot connect to Dash API: {e}")
            return False
    
    def get_available_subjects(self, dataset='master'):
        try:
            response = requests.get(f"{self.api_url}/subjects", 
                                  params={'dataset': dataset}, timeout=10)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def generate_plots(self, dataset='master', analysis_type='session_sex', 
                      session='V1', sex_filter='men', groups='A', subject=None, title=None):
        payload = {
            'dataset': dataset,
            'analysis_type': analysis_type,
            'session': session,
            'sex_filter': sex_filter,
            'groups': groups,
            'title': title
        }
        
        if subject:
            payload['subject'] = subject
            
        try:
            response = requests.post(f"{self.api_url}/generate_plots", 
                                   json=payload, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                self.current_plots = data['plots']
                return data['plots']
            return None
        except Exception as e:
            print(f"❌ Request failed: {e}")
            return None
    
    def generate_overlay(self, dataset='master', analysis_type='session_sex', 
                        session='V1', sex_filter='women', groups='A', 
                        subject=None, title=None):
        if groups is None:
            groups = ['NA', 'A', 'B', 'W', 'G', 'C', 'AN', 'TCM', 'TCS', 'TCMix']
        
        if title is None:
            title = f"Session {session}"
            if sex_filter != 'all':
                title += f" ({'Men' if sex_filter == 'men' else 'Women'})"
        
        payload = {
            'dataset': dataset,
            'analysis_type': analysis_type,
            'session': session,
            'sex_filter': sex_filter,
            'groups': groups,
            'title': title
        }
        
        if subject:
            payload['subject'] = subject
            
        try:
            response = requests.post(f"{self.api_url}/overlay/generate", 
                                   json=payload, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                self.overlays.append(data['overlay'])
                return data['overlay']
            return None
        except Exception as e:
            print(f"❌ Overlay generation failed: {e}")
            return None

    def get_combined_plots(self):
        try:
            response = requests.get(f"{self.api_url}/overlay/combine", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data['combined_plots']
            return None
        except Exception as e:
            return None
    
    def clear_overlays(self):
        self.overlays = []
        try:
            response = requests.delete(f"{self.api_url}/overlay/clear", timeout=10)
            return response.status_code == 200
        except:
            return False

    def create_static_figure(self, base_session='V1', base_sex='men', 
                            overlay_session='V1', overlay_sex='women'):
        """
        Crée une figure statique pour un ensemble de paramètres donné
        Parfait pour l'export HTML/PDF dans MyST
        """
        self.clear_overlays()
        
        base_title = f"Session {base_session} ({'Men' if base_sex == 'men' else 'Women'})"
        base_plots = self.generate_plots(
            dataset="master",
            analysis_type="session_sex",
            session=base_session,
            sex_filter=base_sex,
            groups=['A'],
            title=base_title
        )
        
        if not base_plots:
            return None
        
        overlay_plots = self.generate_overlay(
            dataset="master",
            analysis_type="session_sex",
            session=overlay_session,
            sex_filter=overlay_sex,
            groups=['A']
        )
        
        combined_data = self.get_combined_plots()
        if not combined_data:
            return None
        
        # Créer figure avec 3 subplots
        fig = make_subplots(
            rows=1, cols=3,
            subplot_titles=("Brain Region 1", "Brain Region 2", "Brain Region 3"),
            horizontal_spacing=0.08
        )
        
        fig1_data = go.Figure(combined_data['fig1'])
        fig2_data = go.Figure(combined_data['fig2'])
        fig3_data = go.Figure(combined_data['fig3'])
        
        # Ajouter traces avec gestion des légendes
        for trace in fig1_data.data:
            trace.showlegend = True
            fig.add_trace(trace, row=1, col=1)
            
        for trace in fig2_data.data:
            trace.showlegend = False  # Éviter duplication légende
            fig.add_trace(trace, row=1, col=2)
            
        for trace in fig3_data.data:
            trace.showlegend = False
            fig.add_trace(trace, row=1, col=3)
        
        # Mise en forme
        fig.update_layout(
            height=450,
            title_text=f"Base: {base_title} | Overlay: Session {overlay_session} ({overlay_sex.capitalize()})",
            title_x=0.5,
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.15,
                xanchor="center",
                x=0.5
            )
        )
        
        # Mise à jour des axes
        fig.update_xaxes(title_text="X-axis", row=1, col=1)
        fig.update_xaxes(title_text="X-axis", row=1, col=2)
        fig.update_xaxes(title_text="X-axis", row=1, col=3)
        fig.update_yaxes(title_text="Y-axis", row=1, col=1)
        
        return fig

    def create_interactive_html(self):
        """
        Crée un widget HTML interactif avec JavaScript pur
        Compatible avec MyST, pas besoin de kernel Jupyter actif
        """
        html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
            <style>
                .controls {{
                    padding: 20px;
                    background: #f5f5f5;
                    border-radius: 8px;
                    margin-bottom: 20px;
                    display: flex;
                    gap: 20px;
                    align-items: center;
                    flex-wrap: wrap;
                }}
                .control-group {{
                    display: flex;
                    flex-direction: column;
                    gap: 5px;
                }}
                label {{
                    font-weight: bold;
                    font-size: 14px;
                }}
                select {{
                    padding: 8px 12px;
                    border-radius: 4px;
                    border: 1px solid #ccc;
                    font-size: 14px;
                }}
                button {{
                    padding: 10px 20px;
                    background: #007bff;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 14px;
                    margin-left: auto;
                }}
                button:hover {{
                    background: #0056b3;
                }}
                #plotDiv {{
                    width: 100%;
                    height: 500px;
                }}
                .loading {{
                    text-align: center;
                    padding: 20px;
                    color: #666;
                }}
            </style>
        </head>
        <body>
            <div class="controls">
                <div class="control-group">
                    <label for="baseSession">Base Session:</label>
                    <select id="baseSession">
                        <option value="V1" selected>V1</option>
                        <option value="V2">V2</option>
                        <option value="V3">V3</option>
                    </select>
                </div>
                
                <div class="control-group">
                    <label for="baseSex">Base Sex:</label>
                    <select id="baseSex">
                        <option value="men" selected>Men</option>
                        <option value="women">Women</option>
                        <option value="all">All</option>
                    </select>
                </div>
                
                <div class="control-group">
                    <label for="overlaySession">Overlay Session:</label>
                    <select id="overlaySession">
                        <option value="V1" selected>V1</option>
                        <option value="V2">V2</option>
                        <option value="V3">V3</option>
                    </select>
                </div>
                
                <div class="control-group">
                    <label for="overlaySex">Overlay Sex:</label>
                    <select id="overlaySex">
                        <option value="women" selected>Women</option>
                        <option value="men">Men</option>
                        <option value="all">All</option>
                    </select>
                </div>
                
                <button onclick="updatePlot()">🔄 Update Plot</button>
            </div>
            
            <div id="plotDiv"></div>
            <div id="loading" class="loading" style="display:none;">Loading...</div>
            
            <script>
                const API_URL = '{api_url}';
                
                async function clearOverlays() {{
                    await fetch(`${{API_URL}}/overlay/clear`, {{ method: 'DELETE' }});
                }}
                
                async function generateBase(session, sex) {{
                    const response = await fetch(`${{API_URL}}/generate_plots`, {{
                        method: 'POST',
                        headers: {{ 'Content-Type': 'application/json' }},
                        body: JSON.stringify({{
                            dataset: 'master',
                            analysis_type: 'session_sex',
                            session: session,
                            sex_filter: sex,
                            groups: ['A'],
                            title: `Session ${{session}} (${{sex}})`
                        }})
                    }});
                    return response.json();
                }}
                
                async function generateOverlay(session, sex) {{
                    const response = await fetch(`${{API_URL}}/overlay/generate`, {{
                        method: 'POST',
                        headers: {{ 'Content-Type': 'application/json' }},
                        body: JSON.stringify({{
                            dataset: 'master',
                            analysis_type: 'session_sex',
                            session: session,
                            sex_filter: sex,
                            groups: ['A']
                        }})
                    }});
                    return response.json();
                }}
                
                async function getCombinedPlots() {{
                    const response = await fetch(`${{API_URL}}/overlay/combine`);
                    return response.json();
                }}
                
                async function updatePlot() {{
                    const loading = document.getElementById('loading');
                    loading.style.display = 'block';
                    
                    try {{
                        const baseSession = document.getElementById('baseSession').value;
                        const baseSex = document.getElementById('baseSex').value;
                        const overlaySession = document.getElementById('overlaySession').value;
                        const overlaySex = document.getElementById('overlaySex').value;
                        
                        await clearOverlays();
                        await generateBase(baseSession, baseSex);
                        await generateOverlay(overlaySession, overlaySex);
                        
                        const combined = await getCombinedPlots();
                        
                        // Créer subplots
                        const traces = [
                            ...combined.combined_plots.fig1.data.map(t => ({{...t, xaxis: 'x', yaxis: 'y'}})),
                            ...combined.combined_plots.fig2.data.map(t => ({{...t, xaxis: 'x2', yaxis: 'y2'}})),
                            ...combined.combined_plots.fig3.data.map(t => ({{...t, xaxis: 'x3', yaxis: 'y3'}}))
                        ];
                        
                        const layout = {{
                            grid: {{ rows: 1, columns: 3, pattern: 'independent' }},
                            height: 500,
                            showlegend: true,
                            legend: {{ orientation: 'h', y: -0.2 }},
                            xaxis: {{ domain: [0, 0.3] }},
                            xaxis2: {{ domain: [0.35, 0.65] }},
                            xaxis3: {{ domain: [0.7, 1] }},
                            yaxis: {{ anchor: 'x' }},
                            yaxis2: {{ anchor: 'x2' }},
                            yaxis3: {{ anchor: 'x3' }}
                        }};
                        
                        Plotly.newPlot('plotDiv', traces, layout);
                    }} catch (error) {{
                        console.error('Error updating plot:', error);
                        alert('Error updating plot. Check console.');
                    }} finally {{
                        loading.style.display = 'none';
                    }}
                }}
                
                // Charger plot initial
                updatePlot();
            </script>
        </body>
        </html>
        """
        
        html_content = html_template.format(api_url=self.api_url)
        return HTML(html_content)
    
        """
        Crée une figure Plotly interactive avec contrôles HTML intégrés
        Compatible avec MyST et exportation HTML statique
        """
        # Données initiales
        self.clear_overlays()
        
        base_title = "Session V1 (Men)"
        base_plots = self.generate_plots(
            dataset="master",
            analysis_type="session_sex",
            session='V1',
            sex_filter='men',
            groups=['A'],
            title=base_title
        )
        
        if not base_plots:
            return None
        
        overlay_plots = self.generate_overlay(
            dataset="master",
            analysis_type="session_sex",
            session='V1',
            sex_filter='women',
            groups=['A']
        )
        
        combined_data = self.get_combined_plots()
        if not combined_data:
            return None
        
        # Créer une figure avec subplots
        fig = make_subplots(
            rows=1, cols=3,
            subplot_titles=("Plot 1", "Plot 2", "Plot 3"),
            horizontal_spacing=0.1
        )
        
        # Charger les 3 graphiques
        fig1_data = go.Figure(combined_data['fig1'])
        fig2_data = go.Figure(combined_data['fig2'])
        fig3_data = go.Figure(combined_data['fig3'])
        
        # Ajouter les traces
        for trace in fig1_data.data:
            fig.add_trace(trace, row=1, col=1)
        for trace in fig2_data.data:
            fig.add_trace(trace, row=1, col=2)
        for trace in fig3_data.data:
            fig.add_trace(trace, row=1, col=3)
        
        # Layout
        fig.update_layout(
            height=500,
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.15,
                xanchor="center",
                x=0.5
            ),
            updatemenus=[
                # Base Session
                dict(
                    buttons=[
                        dict(label="Base: V1", method="skip"),
                        dict(label="Base: V2", method="skip"),
                        dict(label="Base: V3", method="skip"),
                    ],
                    direction="down",
                    showactive=True,
                    x=0.01,
                    xanchor="left",
                    y=1.15,
                    yanchor="top"
                ),
                # Base Sex
                dict(
                    buttons=[
                        dict(label="Base: Men", method="skip"),
                        dict(label="Base: Women", method="skip"),
                        dict(label="Base: All", method="skip"),
                    ],
                    direction="down",
                    showactive=True,
                    x=0.15,
                    xanchor="left",
                    y=1.15,
                    yanchor="top"
                ),
                # Overlay Session
                dict(
                    buttons=[
                        dict(label="Overlay: V1", method="skip"),
                        dict(label="Overlay: V2", method="skip"),
                        dict(label="Overlay: V3", method="skip"),
                    ],
                    direction="down",
                    showactive=True,
                    x=0.5,
                    xanchor="left",
                    y=1.15,
                    yanchor="top"
                ),
                # Overlay Sex
                dict(
                    buttons=[
                        dict(label="Overlay: Women", method="skip"),
                        dict(label="Overlay: Men", method="skip"),
                        dict(label="Overlay: All", method="skip"),
                    ],
                    direction="down",
                    showactive=True,
                    x=0.7,
                    xanchor="left",
                    y=1.15,
                    yanchor="top"
                ),
            ]
        )
        
        return fig