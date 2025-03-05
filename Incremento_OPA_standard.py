import streamlit as st
import plotly.graph_objs as go
import pandas as pd

def create_production_increment_chart():
    """
    Create an interactive stacked bar chart showing production increment
    """
    # Create the figure with stacked bars
    fig = go.Figure(data=[
        # 2023 OPA bar
        go.Bar(
            x=['2023 (OPA)', '2024', 'Incremento'],
            y=[4920945, 0, 0],
            name='2023 (OPA)',
            marker_color='#1E90FF',
            text=['€4.920.945', '', ''],
            textposition='outside',
            textfont=dict(size=20)  # Aumenta la dimensione del testo
        ),
        # 2024 ROFS bar (bottom of 2024 stack)
        go.Bar(
            x=['2023 (OPA)', '2024', 'Incremento'],
            y=[0, 2301670, 0],
            name='2024 (ROFS)',
            marker_color='#FF4500',
            text=['', '€2.301.670', ''],
            textposition='outside',
            textfont=dict(size=14)  # Aumenta la dimensione del testo
        ),
        # 2024 GOCO bar (top of 2024 stack)
        go.Bar(
            x=['2023 (OPA)', '2024', 'Incremento'],
            y=[0, 3399644, 0],
            name='2024 (GOCO)',
            marker_color='#FFA500',
            text=['', '€3.399.644', ''],
            textposition='outside',
            textfont=dict(size=14)  # Aumenta la dimensione del testo
        ),
        # Increment bar
        go.Bar(
            x=['2023 (OPA)', '2024', 'Incremento'],
            y=[0, 0, 780369],
            name='Incremento',
            marker_color='#2E8B57',
            text=['', '', '€780.369<br><span style="font-size:16px">(+16%)</span>'],
            textposition='outside',
            textfont=dict(size=20)  # Aumenta la dimensione del testo
        )
    ])
    
    # Customize layout
    fig.update_layout(
        title={
            'text': 'Confronto OPA --> GOCO + ROFS',
            'font': {'size': 20}  # Aumenta la dimensione del titolo
        },
        xaxis_title='Periodo',
        yaxis_title='Valore della Produzione (€)',
        barmode='stack',
        height=600,
        width=800,
        template='plotly_white',
        legend_title_text='Componenti',
        # Aggiungi l'importo totale 5.701.314 in alto a destra
        annotations=[
            dict(
                x=0.5,  # Centered horizontally
                y=1.1,  # Adjust as needed for vertical positioning
                xref='paper',
                yref='paper',
                text='€ 5.701.314',
                showarrow=False,
                font=dict(size=20, color='white'),
                xanchor='center'  # Ensures the text is centered at x=0.5
            )
        ]

    )
    
    # Migliora la leggibilità degli assi
    fig.update_xaxes(
        tickfont=dict(size=12),
        title_font=dict(size=14)
    )
    fig.update_yaxes(
        tickfont=dict(size=12),
        title_font=dict(size=14)
    )
    
    return fig

def main():
    
    
    # Configure Streamlit page
    st.set_page_config(
        page_title="Dashboard Incremento Produzione",
        page_icon=":chart_with_upwards_trend:",
        layout="wide"
    )
    
    # Title and introduction
    st.title("Incremento Valore della Produzione OPA 2023-2024")
    
    # Detailed analysis section
    st.markdown("### Analisi Dettagliata")
    st.markdown("""
    L'analisi mostra un significativo incremento della produzione tra il 2023 e il 2024:
    
    - Il Valore della Produzione 2023 (OPA) di <span style='font-size:20px; font-weight:bold;'>€4.920.945</span>
    - Il Valore della Produzione nel 2024 (GOCO+ROFS) è di <span style='font-size:20px; font-weight:bold;'>€5.701.314</span>, composta da €3.399.644 (GOCO) e €2.301.670 (ROFS)
    - Si registra un incremento di €780.369 (<span style='font-size:20px; font-weight:bold;'>+16%</span>)
    """, unsafe_allow_html=True)
    
    # Create columns for better layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Display the interactive chart
        chart = create_production_increment_chart()
        st.plotly_chart(chart, use_container_width=True)
    
    with col2:
        # Key metrics and insights
        st.markdown("### Dettagli Chiave")
        
        metrics = {
            "Produzione 2023 (OPA)": "€4.920.945",
            "Totale Produzione 2024 (GOCO + ROFS)": "€5.701.314"}
        
        
        for label, value in metrics.items():
            st.metric(label=label, value=value)

        # Incremento Totale and Percentuale Incremento in italic dark green
        st.markdown("  * GOCO: €3.399.644", unsafe_allow_html=True)
        st.markdown("  * ROFS: €2.301.670", unsafe_allow_html=True)

        metrics = {
            "Incremento Totale": "€780.369",
            "Percentuale Incremento": "+16%"
        }
        
        for label, value in metrics.items():
            st.metric(label=label, value=value)

if __name__ == "__main__":
    main()

# Istruzioni per l'installazione:
# 1. Creare un ambiente virtuale (opzionale ma consigliato)
# 2. Installare le dipendenze:
#    pip install streamlit plotly pandas
# 3. Salvare lo script come app.py
# 4. Eseguire con: streamlit run app.py