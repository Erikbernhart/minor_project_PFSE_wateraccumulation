import streamlit as st
from main import debit
from main import waterheight
from main import water_above_roof


st.header("roof overflow design for flat roof")


area_value = st.sidebar.number_input("roof area in (m^2)",50)
n_value = st.sidebar.number_input("number of water overflows",1)

Area = area_value 

n = n_value 

debit_latex, debit_value = debit(Area, n)

st.write("calculating the water debit in m^3/s")
st.latex(debit_latex)

height_A_value=st.sidebar.number_input("start of overflow above roof (mm)",30)
width_value = st.sidebar.number_input("width of overflow (mm)",200)
height_value = st.sidebar.number_input("height of overflow in (mm) ",20)

width_overload=width_value
height_above_roof=height_A_value
Q_hi=debit_value
height_of_overload=height_value

D_ndi_latex, D_ndi_value= waterheight(width_overload,Q_hi)
st.write("calculating the waterheight in mm")
st.latex(D_ndi_latex)
D_ndi=D_ndi_value
d_hw_latex,d_hw_value=water_above_roof(D_ndi)
st.write("calculating the total height in mm")
st.latex(d_hw_latex)

hcrit=height_above_roof+height_of_overload-30


ho=height_value
h_nd=height_A_value
d_hw=D_ndi+h_nd
import plotly.graph_objects as go
fig=go.Figure()
fig.add_trace(go.Scatter(x=[0,70,70,100,100,0], y=[0,0,h_nd,h_nd,d_hw,d_hw], fill="toself",fillcolor="lightblue", line=dict(color="lightblue"),showlegend=False))
fig.add_trace(go.Scatter(x=[0,100,100,70,70,0,0,None,70,100,100,70,70], y=[-30,-30,h_nd,h_nd,0,0,-30,None,h_nd+ho,h_nd+ho,h_nd+ho+ho,h_nd+ho+ho,h_nd+ho], fill="toself",fillcolor="grey", line=dict(color="black"),showlegend=False))
fig.add_trace(go.Scatter(x=[0,100,], y=[hcrit,hcrit],mode="lines", line=dict(color="black", dash="dash"),showlegend=False))
x1, y1 = 70, 30 + h_nd
x2, y2 = 100, 30 + h_nd


x_point, y_point = 65, h_nd+3
label_text = f"<span style='color:black; font-weight:bold;'>h_nd = {h_nd}mm</span>"

# Add an annotation for the point
fig.add_annotation(
    text=label_text,  # Text label for the point
    x=x_point,  # X-coordinate of the point
    y=y_point,  # Y-coordinate of the point
    showarrow=False,  # Display an arrow pointing to the annotation
    arrowhead=1,  # Specify the arrowhead style
    
)
x_point, y_point = 30, hcrit+3
if hcrit>d_hw_value:
    label_text2 =f" <span style='color:black; font-weight:bold;'>hcrit =maximum available waterheight  {hcrit}mm</span>"
else:
    label_text2 = f"<span style='color:red; font-weight:bold;'>maximum water height exceeded!! make overflow wider or higher</span>"

# Add an annotation for the point
fig.add_annotation(
    text=label_text2,  # Text label for the point
    x=x_point,  # X-coordinate of the point
    y=y_point,  # Y-coordinate of the point
    showarrow=False,  # Display an arrow pointing to the annotation
    arrowhead=1,  # Specify the arrowhead style
)
x_point, y_point = 65, round(d_hw,0)+3
label_text1 = f"<span style='color:black; font-weight:bold;'>d_hw = {round(d_hw,0)}mm</span>"

# Add an annotation for the point
fig.add_annotation(
    text=label_text1,  # Text label for the point
    x=x_point,  # X-coordinate of the point
    y=y_point,  # Y-coordinate of the point
    showarrow=False,  # Display an arrow pointing to the annotation
    arrowhead=1,  # Specify the arrowhead style
)

fig.update_layout(
    xaxis=dict(showgrid=False),  # Remove x-axis gridlines
    yaxis=dict(showgrid=False),  # Remove y-axis gridlines
    paper_bgcolor='rgba(0,0,0,0)',  # Set transparent background
    plot_bgcolor='rgba(0,0,0,0)'  # Set transparent plot background
)
fig.update_xaxes(showline=False, showticklabels=False)  # Remove x-axis
fig.update_yaxes(showline=True, showticklabels=True, side="right")  # Show y-axis on the right

fig.layout.height = 800
fig.layout.width = 800
fig
