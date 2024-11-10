import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

config = {
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'custom_plot',
        'height': 1080,
        'width': 1920,
        'scale': 4
    }
}

titles = [
    "Vilka ämnen?",
    "Vilka värden?",
    "Tillräcklig tid per yrkesroll?",
    "Var är vi?",
    "Ålderfördelning",
    "Vilka är våra hinder?",
    ]

def create_topic_value_graphs(df):

    def count_categories(series):
        all_cats = []
        for cats in series:
            if isinstance(cats, list):
                all_cats.extend(cats)
        return pd.Series(all_cats).value_counts()

    topics_counts = count_categories(df['ämnen_cat'])
    if 'Ej angiven' in topics_counts.index:
        topics_counts = topics_counts.drop('Ej angiven')
    
    topics_counts_sorted = topics_counts.sort_values()
    
    fig1 = go.Figure(go.Bar(
        x=topics_counts_sorted.values,
        y=topics_counts_sorted.index,
        orientation='h',
        marker_color='#3498db',
        text=topics_counts_sorted.values,
        textposition='auto',
    ))

    fig1.update_layout(
        title={
            'text': titles[0],
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24)
        },
        height=800,
        width=1200,
        xaxis_title='Antal',
        font=dict(size=14),
        yaxis={'categoryorder': 'total ascending'},
        margin=dict(l=200)
    )

    fig1.show(config=config)

    values_counts = count_categories(df['värde_cat'])
    if 'Ej angiven' in values_counts.index:
        values_counts = values_counts.drop('Ej angiven')
    
    values_counts_sorted = values_counts.sort_values()

    fig2 = go.Figure(go.Bar(
        x=values_counts_sorted.values,
        y=values_counts_sorted.index,
        orientation='h',
        marker_color='#2ecc71',
        text=values_counts_sorted.values,
        textposition='auto',
    ))

    fig2.update_layout(
        title={
            'text': titles[1],
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24)
        },
        height=800,
        width=1200,
        xaxis_title='Antal',
        font=dict(size=14),
        yaxis={'categoryorder': 'total ascending'},
        margin=dict(l=200)
    )

    fig2.show(config=config)

    return fig1, fig2
    

def create_visualizations(df):
    
    # 1. Time Adequacy by Role
    role_time = pd.crosstab(df['yrkesroll_cat'], df['tillräcklig_tid_cat'])
    if 'Ej angiven' in role_time.columns:
        role_time = role_time.drop('Ej angiven', axis=1)
    if 'Övrigt' in role_time.columns:
        role_time = role_time.drop('Övrigt', axis=1)
    
    fig1 = go.Figure()
    
    fig1.add_trace(go.Bar(
        name='Ja',
        x=role_time.index,
        y=role_time['Ja'],
        marker_color='#2ecc71'
    ))
    
    fig1.add_trace(go.Bar(
        name='Nej',
        x=role_time.index,
        y=role_time['Nej'],
        marker_color='#e74c3c'
    ))

    fig1.add_trace(go.Bar(
        name='Vet ej',
        x=role_time.index,
        y=role_time['Vet ej'],
        marker_color='#b0b0b0'
    ))
    
    fig1.update_layout(
        barmode='group',
        title=titles[2],
        height=800,
        width=1200,
        title_x=0.5,
        font=dict(size=14),
        title_font_size=24,
        yaxis_title='Antal'
    )
    
    fig1.show(config=config)

    
    # 2. Places Treemap
    def count_categories(series):
        all_cats = []
        for cats in series:
            if isinstance(cats, list):
                all_cats.extend(cats)
        return pd.Series(all_cats).value_counts()

    places_counts = count_categories(df['platser_cat'])
    places_counts = places_counts[places_counts.index != 'Ej angiven']

    fig2 = px.treemap(
        names=places_counts.index,
        parents=['Platser'] * len(places_counts),
        values=places_counts.values,
        title=titles[3],
        color=places_counts.values,
        color_continuous_scale='Viridis'
    )

    fig2.update_layout(
        height=800,
        width=1200,
        title_x=0.5,
        title_font_size=24,
        font=dict(size=14)
    )
    
    fig2.update_coloraxes(showscale=False)

    fig2.update_traces(
        textinfo='label+value',
        hovertemplate='Plats: %{label}<br>Antal: %{value}<extra></extra>'
    )

    fig2.show(config=config)

    # 3. Age Distribution - Violin Plot
    df_filtered = df[~df['tillräcklig_tid_cat'].isin(['Ej angiven', 'Övrigt'])]

    fig3 = go.Figure()

    colors = {'Ja': '#2ecc71', 'Nej': '#e74c3c', 'Vet ej': '#b0b0b0'}

    for category in sorted(df_filtered['tillräcklig_tid_cat'].unique()):
        fig3.add_trace(go.Violin(
            x=df_filtered['tillräcklig_tid_cat'][df_filtered['tillräcklig_tid_cat'] == category],
            y=df_filtered['ålder_clean'][df_filtered['tillräcklig_tid_cat'] == category],
            name=category,
            box_visible=True,
            meanline_visible=True,
            points='outliers',
            marker_color=colors[category]
        ))

    fig3.update_layout(
        title=titles[4],
        height=800,
        width=1200,
        title_x=0.5,
        title_font_size=24,
        font=dict(size=14),
        xaxis_title='Tillräcklig tid?',
        yaxis_title='Ålder',
        violinmode='group'
    )

    fig3.show(config=config)

    # 4. Barriers/Obs - Sunburst
    barriers_counts = count_categories(df['hinder_cat'])
    total = barriers_counts.sum()

    barriers_percentages = (barriers_counts / total * 100).round(1)

    labels = [f"{idx}<br>{val} ({pct}%)" for idx, val, pct in 
            zip(barriers_counts.index, barriers_counts.values, barriers_percentages)]

    fig4 = go.Figure(go.Sunburst(
        labels=labels,
        parents=['Hinder']*len(barriers_counts),
        values=barriers_counts.values,
        branchvalues='total',
        textfont=dict(size=14),
        insidetextorientation='horizontal'
    ))

    fig4.update_layout(
        title={
            'text': titles[5],
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24)
        },
        height=800,
        width=1200,
        font=dict(size=14),
        showlegend=False
    )

    fig4.show(config=config)