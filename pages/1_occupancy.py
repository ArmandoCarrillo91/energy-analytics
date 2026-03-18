import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from utils.db import run_query
from datetime import datetime, timedelta

st.title("Weekly Occupancy · Heatmap")
st.caption("Which time slots fill on their own?")

if "week_offset" not in st.session_state:
    st.session_state.week_offset = 0

today = datetime.today()
week_start = today - timedelta(days=today.weekday()) + timedelta(weeks=st.session_state.week_offset)
week_end = week_start + timedelta(days=6)

col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    if st.button("← Prev"):
        st.session_state.week_offset -= 1
        st.rerun()

with col2:
    label = "Current week" if st.session_state.week_offset == 0 else f"{week_start.strftime('%b %d')} — {week_end.strftime('%b %d, %Y')}"
    st.markdown(f"<p style='text-align:center; padding-top:6px; color:#C8A415; font-weight:500'>{label}</p>", unsafe_allow_html=True)

with col3:
    if st.button("Next →"):
        st.session_state.week_offset += 1
        st.rerun()

df = run_query(f"""
    SELECT
        TRIM(TO_CHAR(cr.class_date, 'Day'))  AS day_of_week,
        EXTRACT(DOW FROM cr.class_date)       AS day_num,
        TO_CHAR(cr.class_date, 'HH24:00')    AS hour,
        COUNT(*) FILTER (
            WHERE cr.reservation_status NOT IN ('cancelled', 'refunded')
            AND cr.is_refunded = false
        )                                     AS confirmed,
        COUNT(*)                              AS total
    FROM class_reservations cr
    WHERE cr.class_date >= '{week_start.strftime('%Y-%m-%d')}'
      AND cr.class_date <  '{week_end.strftime('%Y-%m-%d')} 23:59:59'
    GROUP BY 1, 2, 3
    ORDER BY day_num, hour
""")

if df.empty:
    st.info("No data for this week.")
    st.stop()

pivot = df.pivot_table(
    index="hour",
    columns="day_of_week",
    values="confirmed",
    aggfunc="sum"
).fillna(0)

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_order = [d for d in day_order if d in pivot.columns]
pivot = pivot[day_order]

total_max = pivot.values.max()

text_matrix = [
    [
        f"{round(v / total_max * 100)}%" if v > 0 else "-"
        for v in row
    ]
    for row in pivot.values
]

energy_colorscale = [
    [0.0,  "#1A1A1A"],
    [0.25, "#3D2E00"],
    [0.5,  "#7A5C00"],
    [0.75, "#B0900F"],
    [1.0,  "#C8A415"],
]

fig = go.Figure(data=go.Heatmap(
    z=pivot.values,
    x=pivot.columns.tolist(),
    y=pivot.index.tolist(),
    text=text_matrix,
    texttemplate="%{text}",
    textfont=dict(size=12, color="#F7F5F0"),
    colorscale=energy_colorscale,
    hoverongaps=False,
    hovertemplate="<b>%{x}</b><br>%{y}<br>%{z} confirmed<extra></extra>",
    showscale=False,
))

fig.update_layout(
    height=520,
    margin=dict(l=60, r=20, t=40, b=40),
    xaxis=dict(side="top", tickfont=dict(color="#F7F5F0")),
    yaxis=dict(autorange="reversed", tickfont=dict(color="#F7F5F0")),
    plot_bgcolor="#1A1A1A",
    paper_bgcolor="#1A1A1A",
    font=dict(color="#F7F5F0", family="sans-serif"),
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Bikes audit")
st.dataframe(run_query("SELECT * FROM bikes"), use_container_width=True)

st.subheader("Reservation configs")
st.dataframe(run_query("SELECT * FROM reservation_configs"), use_container_width=True)

st.subheader("Schedules")
st.dataframe(run_query("SELECT * FROM schedules"), use_container_width=True)