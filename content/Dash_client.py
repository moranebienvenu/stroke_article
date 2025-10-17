import nbformat
import requests
import plotly.graph_objects as go
import pandas as pd
import json
from IPython.display import display, HTML
import ipywidgets as widgets
from ipywidgets import interact, Dropdown, SelectMultiple, Checkbox
from ipywidgets import HBox, VBox, GridBox, Layout
import numpy as np
from plotly.subplots import make_subplots

class DashNeuroTmapClient:
    def __init__(self, dash_url="http://127.0.0.1:8050"):
        """
        Client pour interagir avec l'application Dash
        
        Args:
            dash_url: URL de base de l'application Dash
        """
        self.base_url = dash_url
        self.api_url = f"{dash_url}/api"
        self.current_plots = None
        self.overlays = []
        
    def check_health(self):
        """Vérifie si l'API Dash est accessible"""
        try:
            response = requests.get(f"{self.api_url}/health", timeout=5)
            if response.status_code == 200:
                data = response.json()
                print("✅ Dash API is healthy!")
                #print(f"Available datasets: {data['available_datasets']}")
                return True
            else:
                print(f"❌ API health check failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Cannot connect to Dash API: {e}")
            print(f"Make sure your Dash app is running on {self.base_url}")
            return False
    
    def get_available_subjects(self, dataset='master'):
        """Récupère la liste des sujets disponibles"""
        try:
            response = requests.get(f"{self.api_url}/subjects", 
                                  params={'dataset': dataset}, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error getting subjects: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def generate_plots(self, dataset='master', analysis_type='session_sex', 
                      session='V1', sex_filter='men', groups='A', subject=None, title=None):
        """
        Génère des graphiques via l'API Dash
        
        Args:
            dataset: 'master', 'dataset1', ou 'dataset2'
            analysis_type: 'single' ou 'session_sex'
            session: 'V1', 'V2', ou 'V3'
            sex_filter: 'all', 'men', ou 'women'
            groups: Liste des groupes (ex: ['A', 'B', 'C'])
            subject: ID du sujet (requis pour analysis_type='single')
            title: Titre personnalisé pour l'overlay
        """

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
                #print(f"✅ {data['message']}")
                return data['plots']
            else:
                error_data = response.json()
                print(f"❌ Error: {error_data.get('error', 'Unknown error')}")
                return None
                
        except Exception as e:
            print(f"❌ Request failed: {e}")
            return None
    
    def update_plots(self, **kwargs):
        """Met à jour les graphiques actuels avec de nouveaux paramètres"""
        try:
            response = requests.put(f"{self.api_url}/update_plots", 
                                  json=kwargs, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                self.current_plots = data['plots']
                #print(f"✅ Plots updated successfully")
                return data['plots']
            else:
                error_data = response.json()
                print(f"❌ Update failed: {error_data.get('error', 'Unknown error')}")
                return None
                
        except Exception as e:
            print(f"❌ Update failed: {e}")
            return None
    
    def get_current_plots(self):
        """Récupère les graphiques actuels"""
        try:
            response = requests.get(f"{self.api_url}/get_plots", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.current_plots = data['plots']
                return data['plots']
            else:
                error_data = response.json()
                print(f"❌ Error: {error_data.get('error', 'No plots available')}")
                return None
                
        except Exception as e:
            print(f"❌ Failed to get plots: {e}")
            return None
    
    def display_plots(self, plots_data=None):
        """Affiche les 3 graphiques Plotly côte à côte"""
        if plots_data is None:
            plots_data = self.current_plots
            
        if not plots_data:
            print("No plots to display. Generate plots first.")
            return None
        
        try:
            fig1 = go.Figure(plots_data['fig1'])
            fig2 = go.Figure(plots_data['fig2'])
            fig3 = go.Figure(plots_data['fig3'])
            
          
            for fig in [fig2, fig3]:
                fig.update_layout(height=250, 
                                  width=250,
                                  showlegend=False,
                                  title=dict( 
                                    y=1,  
                                    x=0.5,
                                    xanchor='center',
                                    yanchor='top'
                                  ))
            fig1.update_layout(height=250, 
                                width=250,
                                legend=dict(
                                    orientation="h",
                                    yanchor="top",
                                    y=-0.2,
                                    xanchor="center",
                                    x=0.5
                                ), 
                                title=dict( 
                                y=1,  
                                x=0.5,
                                xanchor='center',
                                yanchor='top'
                                ))

            display(GridBox(
                children=[
                    go.FigureWidget(fig1),
                    go.FigureWidget(fig2),
                    go.FigureWidget(fig3)
                ],
                layout=Layout(grid_template_columns="repeat(3, 33%)",
                justify_content='center',
                align_items='center')      
            ))
            
            return fig1, fig2, fig3
        
            #for fig in [fig1, fig2, fig3]:
            #     fig.update_layout(height=250, width=250, #margin=dict(l=20, r=20, t=20, b=40), 
            #         legend=dict(
            #             orientation="h",
            #             yanchor="top",
            #             y=-0.1,
            #             xanchor="center",
            #             x=0.5
            #     ), #essai 
            #        title=dict( 
            #         y=1.05,  
            #         x=0.5,
            #         xanchor='center',
            #         yanchor='top'
            #     )   )
            
            # # organisation en grille (3 colonnes)
            # display(GridBox(
            #     children=[
            #         go.FigureWidget(fig1),
            #         go.FigureWidget(fig2),
            #         go.FigureWidget(fig3)
            #     ],
            #     layout=Layout(grid_template_columns="repeat(3, 33%)",
            #     justify_content='center',
            #     align_items='center')      
            #     #width='100%')
            # ))
            
            # return fig1, fig2, fig3
        
        except Exception as e:
            print(f"❌ Error displaying plots: {e}")
            return None

    def generate_overlay(self, dataset='master', analysis_type='session_sex', 
                        session='V1', sex_filter='women', groups='A', 
                        subject=None, title=None):
        """
        Génère un overlay avec état naturel
        
        Args:
            dataset: 'master', 'dataset1', ou 'dataset2'
            analysis_type: 'single' ou 'session_sex' (défaut: session_sex)
            session: 'V1', 'V2', ou 'V3' (défaut: V1)
            sex_filter: 'all', 'men', ou 'women' (défaut: women)
            groups: Liste des groupes
            subject: ID du sujet (pour analysis_type='single')
            title: Titre personnalisé pour l'overlay
        """
        if groups is None:
            groups = ['NA', 'A', 'B', 'W', 'G', 'C', 'AN', 'TCM', 'TCS', 'TCMix']
        
        if title is None:
            title = f"Session {session}"
            if sex_filter != 'all':
                title += f" ({'Men' if sex_filter == 'men' else 'Women'})"
            # if groups:
            #     title += f" | Groups: {', '.join(groups)}"
        
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
                #print(f"✅ {data['message']}")
                self.overlays.append(data['overlay'])
                return data['overlay']
            else:
                error_data = response.json()
                print(f"❌ Error: {error_data.get('error', 'Unknown error')}")
                return None
                
        except Exception as e:
            print(f"❌ Overlay generation failed: {e}")
            return None

    def get_combined_plots(self):
        """Récupère les graphiques combinés (base + overlays)"""
        try:
            response = requests.get(f"{self.api_url}/overlay/combine", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data['combined_plots']
            return None
        except Exception as e:
            print(f"Error getting combined plots: {e}")
            return None
    
    def display_combined_plots(self):
        """Affiche les graphiques combinés avec overlays"""
        combined_data = self.get_combined_plots()
        if not combined_data:
            print("No combined plots available. Generate base plots and overlays first.")
            return None
        
        try:
            fig1 = go.Figure(combined_data['fig1'])
            fig2 = go.Figure(combined_data['fig2'])
            fig3 = go.Figure(combined_data['fig3'])
            
            # Améliorer la légende
            for fig in [fig1, fig2]:
                fig.update_layout(height=250, 
                                  width=250,
                                  showlegend=False,
                                  title=dict( 
                                    y=1,  
                                    x=0.5,
                                    xanchor='center',
                                    yanchor='top'
                                  ))
            fig3.update_layout(height=250, 
                                width=250,
                                legend=dict(
                                    orientation="h",
                                    yanchor="top",
                                    y=-0.2,
                                    xanchor="center",
                                    x=0.5
                                ), 
                                title=dict( 
                                y=1,  
                                x=0.5,
                                xanchor='center',
                                yanchor='top'
                                ))

            display(GridBox(
                children=[
                    go.FigureWidget(fig1),
                    go.FigureWidget(fig2),
                    go.FigureWidget(fig3)
                ],
                layout=Layout(grid_template_columns="repeat(3, 33%)",
                justify_content='center',
                align_items='center')      
            ))
            
            return fig1, fig2, fig3
            #     fig.update_layout(
            #         height=250,
            #         width=250, 
            #         #showlegend=False, 
            #         margin=dict(l=20, r=20, t=20, b=40),
            #         legend=dict(
            #             orientation="h",
            #             yanchor="top",
            #             y=-0.1,
            #             xanchor="center",
            #             x=0.5
            #         ), #essai 
            #         title=dict( 
            #             y=0.95,  
            #             x=0.5,
            #             xanchor='center',
            #             yanchor='top'
            #         )   )
            
            # # organisation en grille (3 colonnes) - identique à display_plots
            # display(GridBox(
            #     children=[
            #         go.FigureWidget(fig1),
            #         go.FigureWidget(fig2),
            #         go.FigureWidget(fig3)
            #     ],
            #     layout=Layout(grid_template_columns="repeat(3, 33%)",
            #     justify_content='center',
            #     align_items='center')      
            #     #width='100%')
            # ))

            # return fig1, fig2, fig3
            
        except Exception as e:
            print(f"Error displaying combined plots: {e}")
            return None
            
    def create_advanced_interface(self, base_session_default='V1', base_sex_default='men', overlay_session_default='V1', overlay_sex_default='women', groups_default=['A']):
        """Interface avancée avec gestion des overlays"""
        subjects_data = self.get_available_subjects(dataset="master")
        if not subjects_data:
            print("Cannot create interface: no subjects data available")
            return None

        # Widgets pour la base
        base_session = Dropdown(options=['V1', 'V2', 'V3'], value=base_session_default, description='Base Session:')
        base_sex = Dropdown(options=['all', 'men', 'women'], value=base_sex_default, description='Base Sex:')
        
        # Widgets pour l'overlay (seulement session et sexe)
        overlay_session = Dropdown(options=['V1', 'V2', 'V3'], value=overlay_session_default, description='Overlay Session:')
        overlay_sex = Dropdown(options=['all', 'men', 'women'], value=overlay_sex_default, description='Overlay Sex:')
        
        # Container pour les graphiques
        plot_output = widgets.Output()

        observers_active = False
        
        def display_base_with_overlay():
            """Affiche base + overlay (état par défaut)"""
            with plot_output:
                plot_output.clear_output(wait=True)
                
                # Effacer les overlays existants
                self.clear_overlays()

                # Créer un titre personnalisé SANS les groupes pour la base
                base_title = f"Session {base_session.value}"
                if base_sex.value != 'all':
                    base_title += f" ({'Men' if base_sex.value == 'men' else 'Women'})"
                
                # Générer la base
                base_plots = self.generate_plots(
                    dataset="master",
                    analysis_type="session_sex",
                    session=base_session.value,
                    sex_filter=base_sex.value,
                    groups=groups_default,
                    title=base_title
                )
                
                if base_plots:
                    # Générer l'overlay (groupes fixes pour l'état naturel)
                    overlay_plots = self.generate_overlay(
                        dataset="master",
                        analysis_type="session_sex",
                        session=overlay_session.value,
                        sex_filter=overlay_sex.value,
                        groups=groups_default  # Groupe fixe pour l'état naturel
                    )
                    
                    if overlay_plots:
                        self.display_combined_plots()
                    else:
                        self.display_plots(base_plots)
         
        
        def reset_to_default():
            """Réinitialise tous les widgets aux valeurs par défaut"""
            base_session.value = 'V1'
            base_sex.value = 'men'
            overlay_session.value = 'V1'
            overlay_sex.value = 'women'
            

        # Afficher l'interface de manière contrôlée
        interface_elements = [
            HBox([base_session, base_sex]),
            HBox([overlay_session, overlay_sex]),
            HBox([widgets.Button(description="🔄 Reset to Default", button_style='warning')]),
            plot_output
        ]
    
        # Afficher tous les éléments
        for element in interface_elements:
            display(element)
        
        # Configurer le bouton reset
        reset_btn = interface_elements[2].children[0]  # Récupérer le bouton
        reset_btn.on_click(lambda b: reset_to_default())
        
        # Premier affichage (base + overlay par défaut)
        display_base_with_overlay()
        
        
        # Lier les événements des widgets - mise à jour automatique
        def on_any_change(change):
            """Quand un paramètre change, mettre à jour base + overlay"""
            if observers_active:
                display_base_with_overlay()
        
        observers_active = True
        # Tous les widgets déclenchent une mise à jour automatique
        for widget in [base_session, base_sex, overlay_session, overlay_sex]:
            widget.observe(on_any_change, names='value')
        
        return None
        
    def clear_overlays(self):
        """Efface tous les overlays localement et via l'API"""
        self.overlays = []
        try:
            response = requests.delete(f"{self.api_url}/overlay/clear", timeout=10)
            if response.status_code == 200:
                return True
            return False
        except Exception as e:
            return False

   #Affichez 3 heatmaps côte à côte, "All", "Men" et "Women", pour même variable, même session
    def generate_correlation_heatmaps(self, dataset='master', session='V1', 
                                        system_type='Synaptic ratio', groups=['A']):
            """
            Génère des heatmaps de corrélation identiques à celles du Dash
            """
            payload = {
                'dataset': dataset,
                'session': session,
                'system_type': system_type,
                'groups': groups
            }
            
            try:
                response = requests.post(f"{self.api_url}/correlation/generate_heatmaps", 
                                    json=payload, timeout=30)
                
                if response.status_code == 200:
                    data = response.json()
                    return data['heatmaps']
                else:
                    error_data = response.json()
                    print(f"❌ Error: {error_data.get('error', 'Unknown error')}")
                    return None
                    
            except Exception as e:
                print(f"❌ Heatmap generation failed: {e}")
                return None

    def display_correlation_heatmaps(self, heatmaps_data=None, system_type="Synaptic ratio"):
        """Affiche les 3 heatmaps de corrélation identiques à Dash"""
        if heatmaps_data is None:
            return None
        
        try:
            figures = []
            titles = ['All Subjects', 'Men Only', 'Women Only']
            
            for i, sex_filter in enumerate(['all', 'men', 'women']):
                if (sex_filter in heatmaps_data and 
                    heatmaps_data[sex_filter]['status'] == 'success'):
                    
                    # Utiliser directement la figure Plotly générée par Dash
                    fig_dict = heatmaps_data[sex_filter]['heatmap']
                    fig = go.Figure(fig_dict)
                    
                    # Ajuster seulement la taille pour l'affichage côte à côte
                    fig.update_layout(
                        title=dict(
                            text=titles[i],
                            x=0.5,
                            xanchor='center'
                        )
                    )
                    
                    figures.append(fig)
                else:
                    # Créer une figure vide avec message d'erreur
                    fig = go.Figure()
                    fig.add_annotation(
                        text=f"No data for {titles[i]}",
                        xref="paper", yref="paper",
                        x=0.5, y=0.5, xanchor='center', yanchor='middle',
                        showarrow=False,
                        font=dict(size=14, color="red")
                    )
                    fig.update_layout(
                        height=300,
                        width=300,
                        title=dict(
                            text=titles[i],
                            x=0.5,
                            xanchor='center'
                        ),
                        xaxis=dict(showticklabels=False),
                        yaxis=dict(showticklabels=False)
                    )
                    figures.append(fig)

            # Créer une figure avec 3 subplots
            fig_combined = make_subplots(
                rows=1, cols=3,
                subplot_titles=titles,
                horizontal_spacing=0.03,  # Espace entre les heatmaps
                specs=[[{"type": "heatmap"}, {"type": "heatmap"}, {"type": "heatmap"}]]
            )
            
            # Ajouter chaque heatmap
            for idx, fig in enumerate(figures):
                if len(fig.data) > 0:
                    trace = fig.data[0]
                    trace.showscale = (idx == 2)  # Colorbar seulement sur la dernière
                    fig_combined.add_trace(trace, row=1, col=idx+1)
            
            # Mise en page globale
            fig_combined.update_layout(
                height=600,
                width=850,  # Large pour 3 heatmaps à modifier si ca ne va pas
                showlegend=False,
                #margin=dict(l=10, r=10, t=10, b=10)
            )
            
            # Mettre à jour les axes pour chaque subplot
            for i in range(1, 4):
                fig_combined.update_xaxes(
                    tickangle=45,
                    tickfont=dict(size=9),
                    row=1, col=i
                )
                fig_combined.update_yaxes(
                    autorange='reversed',
                    tickfont=dict(size=9),
                    row=1, col=i
                )
            
            # Afficher la figure combinée
            fig_combined.show()
            
            return fig_combined
            
        except Exception as e:
            print(f"❌ Error displaying correlation heatmaps: {e}")
            import traceback
            traceback.print_exc()
            return None
            
    def create_correlation_interface(self):
        """Interface interactive pour les heatmaps de corrélation """
        
        subjects_data = self.get_available_subjects(dataset="master")
        if not subjects_data:
            print("Cannot create interface: no subjects data available")
            return None

        # Widgets de configuration 
        session_widget = widgets.Dropdown(
            options=['V1', 'V2', 'V3'],
            value='V1',
            description='Session:'
        )

        system_widget = widgets.Dropdown(
            options=['Synaptic ratio', 'Neurotransmitter (Loc)', 'Neurotransmitter (Tract)', 'Clinical Outcomes'],
            value='Synaptic ratio',
            description='System:'
        )

        groups_widget = widgets.Dropdown(
            options=['A', 'NA'],  
            value='A',
            description='Groups:'
        )

        #  Bouton reset 
        reset_btn = widgets.Button(
            description='🔄 Reset to Default',
            button_style='warning',
            layout=widgets.Layout(width='200px')
        )

        # Container pour les graphiques 
        plot_output = widgets.Output()

        observers_active = False
        
        def display_heatmaps():
            """Affiche les 3 heatmaps côte à côte"""
            with plot_output:
                plot_output.clear_output(wait=True)
                
                try:
                    heatmaps_data = self.generate_correlation_heatmaps(
                        session=session_widget.value,
                        system_type=system_widget.value,
                        groups=groups_widget.value
                    )

                    if heatmaps_data:
                        self.display_correlation_heatmaps(heatmaps_data, system_type=system_widget.value)
                    else:
                        print("❌ No heatmaps generated (missing data or server error)")
                except Exception as e:
                    print(f"❌ Error displaying heatmaps: {e}")
        
        def reset_to_default(_=None):
            """Réinitialise tous les widgets aux valeurs par défaut"""
            session_widget.value = 'V1'
            system_widget.value = 'Synaptic ratio'
            groups_widget.value = ['A']
        
        # Configuration du bouton reset
        reset_btn.on_click(reset_to_default)

        # Afficher l'interface de manière contrôlée 
        interface_elements = [
            widgets.HBox([session_widget,system_widget,groups_widget]),
            widgets.HBox([reset_btn]),
            plot_output
        ]

        # Afficher tous les éléments
        for element in interface_elements:
            display(element)
        
        #  Lier les événements des widgets - mise à jour automatique
        def on_any_change(change):
            """Quand un paramètre change, mettre à jour les heatmaps"""
            if observers_active:
                display_heatmaps()
        
        observers_active = True
        # Tous les widgets déclenchent une mise à jour automatique
        for widget in [session_widget, system_widget, groups_widget]:
            widget.observe(on_any_change, names='value')
        
        # Premier affichage (comme create_advanced_interface)
        display_heatmaps()
    
        return None
   
   
    #Heatmap avec variables croisée et interactive  
    def generate_cross_correlation_heatmap(self, dataset='master',
                                        session1='V1', sex_filter1='All', outcome1='Synaptic ratio', groups1=['A'],
                                        session2='V3', sex_filter2='All', outcome2='Synaptic ratio', groups2=['A']):
        """Génère une heatmap de corrélation croisée entre deux sets"""
        payload = {
            'dataset': dataset,
            'session1': session1,
            'sex_filter1': sex_filter1,
            'outcome1': outcome1,
            'groups1': groups1,
            'session2': session2,
            'sex_filter2': sex_filter2,
            'outcome2': outcome2,
            'groups2': groups2
        }
        
        try:
            response = requests.post(f"{self.api_url}/correlation/generate_cross_heatmaps", 
                                json=payload, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                error_data = response.json()
                print(f"❌ Error: {error_data.get('error', 'Unknown error')}")
                return None
                
        except Exception as e:
            print(f"❌ Cross correlation generation failed: {e}")
            return None

    def create_interactive_correlation_interface_auto(self):

        """Interface interactive avec mise à jour automatique"""
    
        from IPython.display import display, clear_output
        
        # Widgets pour Set 1
        session1 = widgets.Dropdown(options=['V1', 'V2', 'V3'], value='V1', description='Session 1:')
        sex1 = widgets.Dropdown(options=['All', 'Men only', 'Women only'], value='Men only', description='Sex 1:')
        outcome1 = widgets.Dropdown(
            options=['Synaptic ratio', 'Neurotransmitter (Loc)', 
                    'Neurotransmitter (Tract)', 'Clinical Outcomes'],
            value='Synaptic ratio',
            description='Outcome 1:'
        )
        
        # Widgets pour Set 2
        session2 = widgets.Dropdown(options=['V1', 'V2', 'V3'], value='V1', description='Session 2:')
        sex2 = widgets.Dropdown(options=['All', 'Men only', 'Women only'], value='Men only', description='Sex 2:')
        
        outcome2 = widgets.Dropdown(
            options=['Synaptic ratio', 'Neurotransmitter (Loc)', 
                    'Neurotransmitter (Tract)', 'Clinical Outcomes'],
            value='Synaptic ratio',
            description='Outcome 2:'
        )
        
       
        permanent_message = widgets.HTML(
            value="""
            <div style='
                background-color: #e3f2fd; 
                border: 1px solid #2196f3; 
                border-radius: 5px; 
                padding: 8px; 
                margin: 10px 0;
                color: #1565c0;
                font-size: 14px;
            '>
            💡 <b>Note:</b> You must choose the same sex group for each subject set to obtain correlation analysis
            </div>
            """
        )

        # Container pour la figure et les stats
        output_container = widgets.VBox()
        observers_active = False
        
        def update_heatmap():
            result = self.generate_cross_correlation_heatmap(
                dataset='master',
                session1=session1.value,
                sex_filter1=sex1.value,
                outcome1=outcome1.value,
                groups1=['A'],
                session2=session2.value,
                sex_filter2=sex2.value,
                outcome2=outcome2.value,
                groups2=['A']
            )
            
            if result and result['status'] == 'success':
                # Créer un NOUVEAU FigureWidget à chaque mise à jour
                fig = go.FigureWidget(result['heatmap'])
                
                # Créer le widget de statistiques
                stats_text = widgets.HTML(
                    value=f"<p><b>Set 1:</b> {result['subject_count_set1']} subjects | "
                        f"<b>Set 2:</b> {result['subject_count_set2']} subjects | "
                        f"<b>Common:</b> {result['common_subjects']} subjects</p>"
                )
                
                # Mettre à jour le container avec la nouvelle figure
                output_container.children = [stats_text, fig]
            else:
                error_text = widgets.HTML(value="<p style='color: red;'>Failed to generate heatmap</p>")
                output_container.children = [error_text]
        
        def on_change(change):
            if observers_active:
                update_heatmap()
        
        # Organisation de l'interface
        set1_controls = widgets.HBox([
            widgets.HTML("<h3>Set 1</h3>"),
            session1, sex1, outcome1
        ])
        
        set2_controls = widgets.HBox([
            widgets.HTML("<h3>Set 2</h3>"),
            session2, sex2, outcome2
        ])
        

        #Afficher l'interface de manière contrôlée 
        interface_elements = [
            widgets.HBox([set1_controls, set2_controls]),
            permanent_message,
            output_container
        ]

        # Afficher tous les éléments
        for element in interface_elements:
            display(element)
        
        # Affichage initial
        update_heatmap()
        
        # Activer les observers après le premier affichage
        observers_active = True
        for widget in [session1, sex1, outcome1, session2, sex2, outcome2]:
            widget.observe(on_change, names='value')
