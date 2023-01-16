import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit.components.v1 as components
import streamlit_nested_layout
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time
import requests
import lottie




# Layout
st.set_page_config(page_title='MGI VS MU',
                   page_icon=':bar_chart:', layout='wide')

# set minimum width of the page
# st.markdown(
#     """
#     <style>
#     .reportview-container .main .block-container{
#         max-width: 1500px;
#         padding-top: 0.5rem;
#         padding-right: 0.5rem;
#         padding-left: 0.5rem;
#         padding-bottom: 0.5rem;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )


# create columns
col1, col2 = st.columns(2)
with col1:
    # create header in center of page
    # st.header("Miss Grand International")

    st.markdown("<h1 style='text-align: center; color: light blue;'>Miss Grand International\n</h1>",
                unsafe_allow_html=True)
    # space between 2 rows
    st.markdown("<br>", unsafe_allow_html=True)
    # st.markdown("<br>", unsafe_allow_html=True)

    # create 3 metrics in the same row with 3 columns in first column
    col1_1, col1_2, col1_3 = st.columns(3)
    ######################################################################################
    with col1_1:
        # st.metric("Date Published", "25 Oct 2022")
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-calendar-week"
        sline = "Date Published"
        lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = "25 Oct 2022"

        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                <i class='{iconname} fa-xs'></i> {i}
                                </style><BR><span style='font-size: 14px; 
                                margin-top: 0;'>{sline}</style></span></p>"""

        st.markdown(lnk + htmlstr, unsafe_allow_html=True)
    ######################################################################################
    with col1_2:
        # st.metric("Views", "15.5M")
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-eye" ##### 
        sline = "Views" #####
        lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = "15.5M" #####

        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                <i class='{iconname} fa-xs'></i> {i}
                                </style><BR><span style='font-size: 14px; 
                                margin-top: 0;'>{sline}</style></span></p>"""

        st.markdown(lnk + htmlstr, unsafe_allow_html=True)
    ######################################################################################
    with col1_3:
        # st.metric("Likes", "211K")
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-thumbs-up" ##### 
        sline = "Likes" #####
        lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = "211K" #####

        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                <i class='{iconname} fa-xs'></i> {i}
                                </style><BR><span style='font-size: 14px; 
                                margin-top: 0;'>{sline}</style></span></p>"""

        st.markdown(lnk + htmlstr, unsafe_allow_html=True)
    ######################################################################################
    ######################################################################################

    # create 2 metrics in the lower row with 3 columns in first column
    col1_4, col1_5 = st.columns(2)
    ######################################################################################
    with col1_4:
        # st.metric("Total chats", "XXXX")
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-comment" ##### 
        sline = "Total Chats" #####
        lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = "100K" #####

        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                <i class='{iconname} fa-xs'></i> {i}
                                </style><BR><span style='font-size: 14px; 
                                margin-top: 0;'>{sline}</style></span></p>"""

        st.markdown(lnk + htmlstr, unsafe_allow_html=True)
    ######################################################################################
    with col1_5:
        # st.metric("AVG.Chat/Minute", "XXXX")
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-chart-bar" ##### 
        sline = "AVG.Chat/Minute" #####
        lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = "443" #####

        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                <i class='{iconname} fa-xs'></i> {i}
                                </style><BR><span style='font-size: 14px; 
                                margin-top: 0;'>{sline}</style></span></p>"""

        st.markdown(lnk + htmlstr, unsafe_allow_html=True)
    ######################################################################################

with col2:
    # st.header("Miss Universe")
    st.markdown("<h1 style='text-align: center; color: light blue;'>Miss Universe\n</h1>",
                unsafe_allow_html=True)
    # space between 2 rows
    st.markdown("<br>", unsafe_allow_html=True)
    # st.markdown("<br>", unsafe_allow_html=True)

    # create 3 metrics in the same row with 3 columns in first column
    col2_1, col2_2, col2_3 = st.columns(3)
    ######################################################################################
    with col2_1:
        # st.metric("Date Published", "15 Jan 2022")
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-calendar-week"
        sline = "Date Published"
        lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = "15 Jan 2023"

        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                <i class='{iconname} fa-xs'></i> {i}
                                </style><BR><span style='font-size: 14px; 
                                margin-top: 0;'>{sline}</style></span></p>"""

        st.markdown(lnk + htmlstr, unsafe_allow_html=True)
    ######################################################################################
    with col2_2:
        # st.metric("Views", "XXXM")
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-eye" ##### 
        sline = "Views" #####
        lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = "5.1M" #####

        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                <i class='{iconname} fa-xs'></i> {i}
                                </style><BR><span style='font-size: 14px; 
                                margin-top: 0;'>{sline}</style></span></p>"""

        st.markdown(lnk + htmlstr, unsafe_allow_html=True)
    ######################################################################################
    with col2_3:
        # st.metric("Likes", "XXXK")
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-thumbs-up" ##### 
        sline = "Likes" #####
        lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = "56K" #####

        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                <i class='{iconname} fa-xs'></i> {i}
                                </style><BR><span style='font-size: 14px; 
                                margin-top: 0;'>{sline}</style></span></p>"""

        st.markdown(lnk + htmlstr, unsafe_allow_html=True)

    # create 2 metrics in the lower row with 3 columns in first column
    col2_4, col2_5 = st.columns(2)
    ######################################################################################
    with col2_4:
        # st.metric("Total chats", "197K")
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-comment" ##### 
        sline = "Total Chats" #####
        lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = "197K" #####

        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                <i class='{iconname} fa-xs'></i> {i}
                                </style><BR><span style='font-size: 14px; 
                                margin-top: 0;'>{sline}</style></span></p>"""

        st.markdown(lnk + htmlstr, unsafe_allow_html=True)
    ######################################################################################
    with col2_5:
        # st.metric("AVG.Chat/Minute", "XXX")
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-chart-bar" ##### 
        sline = "AVG.Chat/Minute" #####
        lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = "1031" #####

        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                <i class='{iconname} fa-xs'></i> {i}
                                </style><BR><span style='font-size: 14px; 
                                margin-top: 0;'>{sline}</style></span></p>"""

        st.markdown(lnk + htmlstr, unsafe_allow_html=True)
    ######################################################################################
    ######################################################################################
# space between 2 rows
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


######################################################################################
######################################################################################
###### Countries Summary ########
# col_country, col_bott = st.columns(2)
# with col_country:
#     st.markdown("<h3 style='text-align: left; color: light blue;'>Countries Summary</h3>",
#                 unsafe_allow_html=True)
# with col_bott:
#     # create dropdown menu
#     option = st.selectbox('', ('All Countries', 'Top 10 Countries'))


# df_country = pd.read_csv('final_data/country_summary_final_mgi_mu.csv')
# if option == 'All Countries':
#     # # bubble maps
#     # fig_map = px.scatter_geo(df_country, locations="country", locationmode='country names', color="owner", size="amount", hover_name="country", projection="natural earth", size_max=60)
#     # fig_map.update_layout(showlegend=False,
#     # geo=dict(showframe=False, showcoastlines=True, projection_type='equirectangular'))
#     # fig_map.update_layout(margin=dict(l=1, r=1, t=1, b=1))
#     # # use dark theme for the map
#     # fig_map.update_layout(template='plotly_dark')
#     # st.plotly_chart(fig_map, use_container_width=True, theme="streamlit")
#     # html code for embedding flourish
#     components.html(
#         """
#         <div class="flourish-embed flourish-hierarchy" data-src="visualisation/12450319" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div> 
#         """,
#         height=600,
#         scrolling=False,
#     )

# if option == 'Top 10 Countries':

#     df_top10_mgi = df_country[df_country['owner'] == 'MGI'].sort_values(
#         by='amount', ascending=False).head(10)
#     df_top10_mgi.sort_values(by='amount', ascending=True, inplace=True)
#     df_top10_mu = df_country[df_country['owner'] == 'MU'].sort_values(
#         by='amount', ascending=False).head(10)

#     fig_top10 = make_subplots(rows=1, cols=2, specs=[
#                               [{"type": "bar"}, {"type": "bar"}]])

#     fig_top10.add_trace(
#         go.Bar(x=df_top10_mgi['country'],
#                y=df_top10_mgi['amount'], name='Amount'),
#         row=1, col=1)

#     fig_top10.add_trace(
#         go.Bar(x=df_top10_mu['country'],
#                y=df_top10_mu['amount'], name='Amount'),
#         row=1, col=2)

#     fig_top10.update_layout(
#         margin=dict(l=50, r=50, t=50, b=50),
#         showlegend=False,)
    
#     # edit y axis scale to same scale #
#     fig_top10.update_yaxes(range=[0, 13000], row=1, col=1)
#     fig_top10.update_yaxes(range=[0, 13000], row=1, col=2)

#     st.plotly_chart(fig_top10, use_container_width=True, theme="streamlit")

st.markdown("<h3 style='text-align: left; color: light blue;'>MOST FREQUENTLY MENTIONED COUNTRIES</h3>",
                 unsafe_allow_html=True)
df_country = pd.read_csv('final_data/country_summary_final_mgi_mu.csv')
# create tap
tab_count_1, tab_count_2 = st.tabs(["Sumamary", "Top 10 Countries"])
with tab_count_1:
    components.html(
        """
        <div class="flourish-embed flourish-hierarchy" data-src="visualisation/12450319" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div> 
        """,
        height=600,
        scrolling=False,
    )

with tab_count_2:
    df_top10_mgi = df_country[df_country['owner'] == 'MGI'].sort_values(
        by='amount', ascending=False).head(10)
    df_top10_mgi.sort_values(by='amount', ascending=True, inplace=True)
    df_top10_mu = df_country[df_country['owner'] == 'MU'].sort_values(
        by='amount', ascending=False).head(10)

    fig_top10 = make_subplots(rows=1, cols=2, specs=[
                              [{"type": "bar"}, {"type": "bar"}]])

    fig_top10.add_trace(
        go.Bar(x=df_top10_mgi['country'],
               y=df_top10_mgi['amount'], name='Amount'),
        row=1, col=1)

    fig_top10.add_trace(
        go.Bar(x=df_top10_mu['country'],
               y=df_top10_mu['amount'], name='Amount'),
        row=1, col=2)

    fig_top10.update_layout(
        margin=dict(l=50, r=50, t=50, b=50),
        showlegend=False,)
    
    # edit y axis scale to same scale #
    fig_top10.update_yaxes(range=[0, 13000], row=1, col=1)
    fig_top10.update_yaxes(range=[0, 13000], row=1, col=2)

    # chart size #
    fig_top10.update_layout(
        autosize=False,
        # width=1000,
        height=600)

    st.plotly_chart(fig_top10, use_container_width=True, theme="streamlit")

######################################################################################
######################################################################################
##### Top Emoji #####
st.markdown("<h3 style='text-align: left; color: light blue;'>EMOJI USED IN CHAT</h3>",
            unsafe_allow_html=True)

# create tap
col_emo1, col_emo2 = st.columns(2)
with col_emo1:
    wch_colour_box = (38,39,48)
    wch_colour_font = (250,250,250)
    fontsize = 30
    sline = "64" #####
    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                {wch_colour_box[1]}, 
                                                {wch_colour_box[2]}, 0.75); 
                            color: rgb({wch_colour_font[0]}, 
                                    {wch_colour_font[1]}, 
                                    {wch_colour_font[2]}, 0.75); 
                            font-size: {fontsize}px;
                            text-align: center; 
                            border-radius: 7px; 
                            padding-left: 12px; 
                            padding-top: 18px; 
                            padding-bottom: 18px; 
                            line-height:25px;'>
                            </style>{sline}</style>
                            </style><BR><span style='font-size: 14px; 
                            '>Total Emoji Types</style></span></p>"""
    st.markdown(htmlstr, unsafe_allow_html=True)

    # create 3 metrics in the same row with 3 columns in first column
    em11, em12, em13 = st.columns(3)
    with em11:
        # add emoji
        # st.markdown(
        #     "<h2 style='text-align: center; color: green;'>✌️</h2>", unsafe_allow_html=True)
        # st.markdown(
        #     "<h3 style='text-align: center; color: green;'>310</h3>", unsafe_allow_html=True)
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 50
        sline = "1st" #####
        i = '27%'
        
        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px;
                                text-align: center; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                </style><BR>✌️</style><BR>
                                </style><BR><span style='font-size: 14px; 
                                '>{sline}</style></span>
                                </style><BR><span style='font-size: 30px; 
                                '>{i}</style></span></p>"""
        

        st.markdown(htmlstr, unsafe_allow_html=True)

    with em12:
        # st.markdown(
        #     "<h2 style='text-align: center; color: green;'>👸🏼</h2>", unsafe_allow_html=True)
        # st.markdown(
        #     "<h3 style='text-align: center; color: green;'>217</h3>", unsafe_allow_html=True)
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 50
        sline = "2nd" #####
        i = '20%'
        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px;
                                text-align: center; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                </style><BR>👸🏼</style><BR>
                                </style><BR><span style='font-size: 14px; 
                                '>{sline}</style></span>
                                </style><BR><span style='font-size: 30px; 
                                '>{i}</style></span></p>"""
        st.markdown(htmlstr, unsafe_allow_html=True)

    with em13:
        # st.markdown(
        #     "<h2 style='text-align: center; color: green;'>👏</h2>", unsafe_allow_html=True)
        # st.markdown(
        #     "<h3 style='text-align: center; color: green;'>84</h3>", unsafe_allow_html=True)
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 50
        sline = "3rd" #####
        i = '8%'
        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px;
                                text-align: center; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                </style><BR>👏</style><BR>
                                </style><BR><span style='font-size: 14px; 
                                '>{sline}</style></span>
                                </style><BR><span style='font-size: 30px; 
                                '>{i}</style></span></p>"""
        st.markdown(htmlstr, unsafe_allow_html=True)

with col_emo2:
    wch_colour_box = (38,39,48)
    wch_colour_font = (250,250,250)
    fontsize = 30
    sline = "96" #####
    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                {wch_colour_box[1]}, 
                                                {wch_colour_box[2]}, 0.75); 
                            color: rgb({wch_colour_font[0]}, 
                                    {wch_colour_font[1]}, 
                                    {wch_colour_font[2]}, 0.75); 
                            font-size: {fontsize}px;
                            text-align: center; 
                            border-radius: 7px; 
                            padding-left: 12px; 
                            padding-top: 18px; 
                            padding-bottom: 18px; 
                            line-height:25px;'>
                            </style>{sline}</style>
                            </style><BR><span style='font-size: 14px; 
                            '>Total Emoji Types</style></span></p>"""
    st.markdown(htmlstr, unsafe_allow_html=True)
    # create 3 metrics in the same row with 3 columns in first column
    em21, em22, em23 = st.columns(3)
    with em21:
        # st.markdown(
        #     "<h2 style='text-align: center; color: green;'>👎</h2>", unsafe_allow_html=True)
        # st.markdown(
        #     "<h3 style='text-align: center; color: green;'>10K</h3>", unsafe_allow_html=True)
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 50
        sline = "1st" #####
        i = '33%'
        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px;
                                text-align: center; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                </style><BR>👎</style><BR>
                                </style><BR><span style='font-size: 14px; 
                                '>{sline}</style></span>
                                </style><BR><span style='font-size: 30px; 
                                '>{i}</style></span></p>"""
        st.markdown(htmlstr, unsafe_allow_html=True)
    
    
    with em22:
        # st.markdown(
        #     "<h2 style='text-align: center; color: green;'>👸🏼</h2>", unsafe_allow_html=True)
        # st.markdown(
        #     "<h3 style='text-align: center; color: green;'>10K</h3>", unsafe_allow_html=True)
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 50
        sline = "2nd" #####
        i = '17%'
        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px;
                                text-align: center; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                </style><BR>👸🏼</style><BR>
                                </style><BR><span style='font-size: 14px; 
                                '>{sline}</style></span>
                                </style><BR><span style='font-size: 30px; 
                                '>{i}</style></span></p>"""
        st.markdown(htmlstr, unsafe_allow_html=True)
    
    
    with em23:
        # st.markdown(
        #     "<h2 style='text-align: center; color: green;'>👏</h2>", unsafe_allow_html=True)
        # st.markdown(
        #     "<h3 style='text-align: center; color: green;'>10K</h3>", unsafe_allow_html=True)
        wch_colour_box = (38,39,48)
        wch_colour_font = (250,250,250)
        fontsize = 50
        sline = "3rd" #####
        i = '7%'
        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                    {wch_colour_box[1]}, 
                                                    {wch_colour_box[2]}, 0.75); 
                                color: rgb({wch_colour_font[0]}, 
                                        {wch_colour_font[1]}, 
                                        {wch_colour_font[2]}, 0.75); 
                                font-size: {fontsize}px;
                                text-align: center; 
                                border-radius: 7px; 
                                padding-left: 12px; 
                                padding-top: 18px; 
                                padding-bottom: 18px; 
                                line-height:25px;'>
                                </style><BR>👏</style><BR>
                                </style><BR><span style='font-size: 14px; 
                                '>{sline}</style></span>
                                </style><BR><span style='font-size: 30px; 
                                '>{i}</style></span></p>"""
        st.markdown(htmlstr, unsafe_allow_html=True)

######################################################################################
######################################################################################
##### Sentiment Analysis #####
st.markdown("<BR><h3 style='text-align: left; color: light blue;'>SENTIMENT ANALYSIS</h3>",
            unsafe_allow_html=True)

tab_sen_1, tab_sen_2 = st.tabs(["Sentiment Summary", "Sentiment Chart Race"])

with tab_sen_1:
    col_sen1, col_sen2 = st.columns(2)
    with col_sen1:
        # sen11, sen12 = st.columns(2)
        # with sen11:
        #     st.markdown(
        #         "<h4 style='text-align: left; color: green;'>Positive</h4>", unsafe_allow_html=True)
        # with sen12:
        #     st.markdown(
        #         "<h4 style='text-align: right; color: red;'>Negative</h4>", unsafe_allow_html=True)
        # # create progress bar
        # progress_bar = st.progress(0.7)

        components.html(
            """
            <!-- Styles -->
            <style>
            #chartdiv {
            width: 100%;
            height: 300px;
            }

            </style>

            <!-- Resources -->
            <script src="https://cdn.amcharts.com/lib/4/core.js"></script>
            <script src="https://cdn.amcharts.com/lib/4/charts.js"></script>
            <script src="https://cdn.amcharts.com/lib/4/themes/animated.js"></script>
            <script src="https://cdn.amcharts.com/lib/4/themes/dark.js"></script>
            <script src="//www.amcharts.com/lib/4/themes/material.js"></script>
            

            <!-- Chart code -->
            <script>
            am4core.ready(function() {
            am4core.useTheme(am4themes_animated);

            // Themes begin
            function am4themes_myTheme(target) {
            if (target instanceof am4core.ColorSet) {
                target.list = [
                am4core.color("#06d6a0"),
                am4core.color("#f94144"),
                am4core.color("#E77624"),
                am4core.color("#DF3520"),
                am4core.color("#64297B"),
                am4core.color("#232555")
                ];
            }
            }
            am4core.useTheme(am4themes_myTheme);
            // Themes end

            var chart = am4core.create("chartdiv", am4charts.PieChart);
            chart.hiddenState.properties.opacity = 0; // this creates initial fade-in

            chart.data = [
            {
                country: "Positive",
                value: 77
            },
            {
                country: "Negative",
                value: 23
            },
            ];
            chart.radius = am4core.percent(70);
            chart.innerRadius = am4core.percent(40);
            chart.startAngle = 180;
            chart.endAngle = 360;  

            var series = chart.series.push(new am4charts.PieSeries());
            series.dataFields.value = "value";
            series.dataFields.category = "country";

            series.slices.template.cornerRadius = 10;
            series.slices.template.innerCornerRadius = 7;
            series.slices.template.draggable = true;
            series.slices.template.inert = true;
            series.alignLabels = false;

            series.hiddenState.properties.startAngle = 90;
            series.hiddenState.properties.endAngle = 90;

            chart.legend = new am4charts.Legend();
            chart.legend.disabled = true;
            series.labels.template.disabled = true;

            }); // end am4core.ready()
            </script>

            <!-- HTML -->
            <div id="chartdiv"></div>
            """,
            height=300,
        )

    with col_sen2:
        sen21, sen22 = st.columns(2)
        # with sen21:
        #     st.markdown(
        #         "<h4 style='text-align: left; color: green;'>Positive</h4>", unsafe_allow_html=True)
        # with sen22:
        #     st.markdown(
        #         "<h4 style='text-align: right; color: red;'>Negative</h4>", unsafe_allow_html=True)
        # # create progress bar
        # progress_bar = st.progress(0.7)

        components.html(
            """
            <!-- Styles -->
            <style>
            #chartdiv {
            width: 100%;
            height: 300px;
            }

            </style>

            <!-- Resources -->
            <script src="https://cdn.amcharts.com/lib/4/core.js"></script>
            <script src="https://cdn.amcharts.com/lib/4/charts.js"></script>
            <script src="https://cdn.amcharts.com/lib/4/themes/animated.js"></script>
            <script src="https://cdn.amcharts.com/lib/4/themes/dark.js"></script>
            <script src="//www.amcharts.com/lib/4/themes/material.js"></script>
            

            <!-- Chart code -->
            <script>
            am4core.ready(function() {
            am4core.useTheme(am4themes_animated);

            // Themes begin
            function am4themes_myTheme(target) {
            if (target instanceof am4core.ColorSet) {
                target.list = [
                am4core.color("#06d6a0"),
                am4core.color("#f94144"),
                am4core.color("#E77624"),
                am4core.color("#DF3520"),
                am4core.color("#64297B"),
                am4core.color("#232555")
                ];
            }
            }
            am4core.useTheme(am4themes_myTheme);
            // Themes end

            var chart = am4core.create("chartdiv", am4charts.PieChart);
            chart.hiddenState.properties.opacity = 0; // this creates initial fade-in

            chart.data = [
            {
                country: "Positive",
                value: 60
            },
            {
                country: "Negative",
                value: 40
            },
            ];
            chart.radius = am4core.percent(70);
            chart.innerRadius = am4core.percent(40);
            chart.startAngle = 180;
            chart.endAngle = 360;  

            var series = chart.series.push(new am4charts.PieSeries());
            series.dataFields.value = "value";
            series.dataFields.category = "country";

            series.slices.template.cornerRadius = 10;
            series.slices.template.innerCornerRadius = 7;
            series.slices.template.draggable = true;
            series.slices.template.inert = true;
            series.alignLabels = false;

            series.hiddenState.properties.startAngle = 90;
            series.hiddenState.properties.endAngle = 90;

            chart.legend = new am4charts.Legend();
            chart.legend.disabled = true;
            series.labels.template.disabled = true;

            }); // end am4core.ready()
            </script>

            <!-- HTML -->
            <div id="chartdiv"></div>
            """,
            height=300,
        )

with tab_sen_2:
    components.html(
    """
    <div class="flourish-embed flourish-chart" data-src="visualisation/12454772"><script src="https://public.flourish.studio/resources/embed.js"></script></div>
    """,
    height=600,
    scrolling=False,
)

######################################################################################
######################################################################################
##### Top Words #####
st.markdown("<h3 style='text-align: left; color: light blue;'>MOST FREQUENTLY USED WORD</h3>",
            unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Positive", "Negative"])

with tab1:
    col_word1, col_word2 = st.columns(2)
    with col_word1:
        st.image('final_data/Wordcloud_grand_pos.png', width=550)

    with col_word2:
        st.image('final_data/wordcloud_mu_pos.png', width=550)

with tab2:
    col_word3, col_word4 = st.columns(2)
    with col_word3:
        st.image('final_data/wordcloud_grand_neg.png', width=550)

    with col_word4:
        st.image('final_data/wordcloud_mu_neg.png', width=550)

# # html code for embedding flourish
# components.html(
#     """
#     <div class="flourish-embed flourish-hierarchy" data-src="visualisation/12450319" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>
#     """,
#     height=600,
#     scrolling=False,
# )

# <div class="flourish-embed flourish-hierarchy" data-src="visualisation/12450319"><script src="https://public.flourish.studio/resources/embed.js"></script></div>
# "<div class='flourish-embed flourish-hierarchy' data-src='visualisation/12450319'><script src='https://public.flourish.studio/resources/embed.js'></script></div>"


# add text
st.markdown(
    "<BR><BR><h6 style='text-align: right; color: white;'>Created by:</h6>", unsafe_allow_html=True)
st.markdown(
    "<h6 style='text-align: right; color: white;'>Korawee P. 6420422007</h6>", unsafe_allow_html=True)
st.markdown(
    "<h6 style='text-align: right; color: white;'>Sorawit S. 6420422020</h6>", unsafe_allow_html=True)