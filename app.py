import plotly.express as px
import streamlit as st
from datetime import date
df= px.data.tips()
st.set_page_config(
layout='wide',
page_title= 'My streamlit Dash Board',
page_icon='💰'
)
css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size: 26px;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)


tab1,tab2,tab3,tab4,tab5= st.tabs(['home','main_board','help','news','sigh in'])

with tab1:
    st.write('<h1 style = "text-align: center;">Hello Streamlit Dash Board For Tips Dataset!</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,12,1])

with col1:
    st.write(' ')

with col2:
    st.image('menu-analysis.jpg',width=1500)

with col3:
    st.write(' ')

with tab4:
    st.write('<h1 style = "text-align: center;">Hello Streamlit Dash Board For Tips Dataset!</h1>', unsafe_allow_html=True)
    st.write('<h4 style= "color: Green;">It is one of the example datasets built into the seaborn package and is used in the documentation of the seaborn package and can be easily loaded using the seaborn load_dataset command.</h4>', unsafe_allow_html=True )
    st.image('menu-analysis.jpg', width=2000, use_column_width='auto')
x= False    
with tab5:
        name01= st.text_input('Enter your username')
        pass_word= st.text_input('Enter Your Password',type= 'password')
        d= st.date_input('Enter Your Birth date as a reference but not mainly required',date(1993,12,31))
        st.write(f'<h5 style= "text-align:center; color:red;">{d}</h5>', unsafe_allow_html= True)       
        phone= st.number_input('Enter your phone as a refernce but not mainly required')
        st.write(f'<h5 style= "text-align:center; color:red;">{phone}</h5>', unsafe_allow_html= True) 
        st.image('menu-analysis.jpg', width=2000, use_column_width='auto')
        if name01=='omar' and pass_word=='a1234':
            x= True
        
with tab3:
    st.write('<h1 style = "text-align: center;">to download this dataset csv visit the below link: </h1>', unsafe_allow_html=True)
    st.write('<h1 style = "text-align: center;">https://github.com/plotly/datasets/blob/master/tips.csv</h1>', unsafe_allow_html=True)
    st.image('menu-analysis.jpg', width=2000, use_column_width='auto')
    
    
with tab2:    

    if x== True:
  
        page= st.sidebar.radio('select page',['Dataset Overview', 'Describtive Statistics', 'Charts'])
        if page == 'Dataset Overview':
            st.write('<h2 style= "text-aligncenter; color:green;">Tips Dataset all data</h2>', unsafe_allow_html=True)
            space,col,space= st.columns([2,4,2])
            col.dataframe(df,width=600,height=700)
        
        elif page== 'Describtive Statistics':
            col1, space, col4= st.columns([5,1,5])
            with col1:
                with st.container():
                    col1,col2,col3= st.columns([2,2,2])
                    with col1:
                        day1= st.selectbox('select day No 01',df['day'].unique())
                        day1_mean= df[df['day']== day1]['total_bill'].mean()
                    with col2:
                        day2= st.selectbox('select day No 02',df['day'].unique())
                        day2_mean= df[df['day']== day2]['total_bill'].mean()
                    with col3:  
                        st.metric('Averafe bill between your selected days is: ', round(day1_mean-day2_mean,2))
                        
                st.dataframe(df.describe(include='number'), width=500, height=200)
             
            with col4:
                with st.container():
                    col1,col2,col3= st.columns([2,2,2])
                    with col1:
                        day01= st.selectbox('select your frist day',df['day'].unique())
                        day1_sum= df[df['day']== day01]['total_bill'].sum()
                    with col2:
                        day02= st.selectbox('select your second day',df['day'].unique())
                        day02_sum= df[df['day']== day02]['total_bill'].sum()
                    with col3:  
                        st.metric('Averafe bill between your total bills of the selected days is: ',round(day1_sum-day02_sum,2))
                        
                st.dataframe(df.describe(include='O'), width=500, height=200)
                
            col5, space, col7= st.columns([5,1,5])
            with col5:
                st.dataframe(df.describe(), width= 500)
                st.dataframe(df.groupby('day').mean(), width=500)
               
                
            with col7:
                rad= st.radio('select a Day',df['day'].unique(), horizontal=True)
                slid= st.slider('select table size', int(df['size'].min()),int(df['size'].max()), step=1)
                check_graph= st.checkbox('show a graph', False)
                if check_graph:
                    df2= df[(df['day']== rad) & (df['size']== slid)]
                    fig= px.sunburst(df2, path= ('day','size','sex'), color_discrete_sequence=px.colors.qualitative.Antique, width=500, height= 500)
                    st.plotly_chart(fig)
                    
        elif page == 'Charts':
            tab1, tab2 = st.tabs(['UniVariate', 'BiVariate'])
            with tab1:
                with st.container():
                    space, col, space2 = st.columns([3, 4, 3])
                    col_name = col.selectbox('select Column to show its distribution'.title(), df.columns)
                if col_name in df.select_dtypes(include='number'):
                    col1, space, col2 = st.columns([5, 3, 5])
                    fig1 = px.histogram(df, x = col_name, color_discrete_sequence=px.colors.qualitative.Antique,
                                        title=f'{col_name} hist distibution', width=550)
                    fig2 = px.box(df, x = col_name, color_discrete_sequence=px.colors.qualitative.Bold,
                                  title=f'{col_name} boxplot distibution',width =  550)
                    col1.plotly_chart(fig1)
                    col2.plotly_chart(fig2)
                else:
                    col1, space, col2 = st.columns([5, 2, 5])
                    fig1 = px.histogram(df, x = col_name, color_discrete_sequence=px.colors.qualitative.Antique,
                                        title=f'{col_name} hist distibution', width=550)
                    fig2 = px.pie(df, names = col_name, color_discrete_sequence=px.colors.qualitative.Bold, hole= 0.3,
                                  title=f'{col_name} boxplot distibution',width =  550)
                    col1.plotly_chart(fig1)
                    col2.plotly_chart(fig2)
                with tab2:
                    col1, space, col2 = st.columns([5,2,5])
                    with col1:
                        fig = px.histogram(df, x = 'total_bill', color = 'sex',
                                           color_discrete_sequence=px.colors.qualitative.Antique, width=550,
                                          title='total_bill distibution separated to each gender')
                        st.plotly_chart(fig)
                        fig2 = px.scatter(df, x = 'total_bill', y = 'tip',color='day', size = 'size', size_max = 40,
                                          color_discrete_sequence = px.colors.qualitative.Antique, width=550,
                                         title='correlation between tips and total bill according to each day')
                        st.plotly_chart(fig2)
                    with col2:
                        fig = px.sunburst(df, path=['day', 'time', 'sex'], color_discrete_sequence=px.colors.qualitative.Antique,
                                         width=550)
                        st.plotly_chart(fig)
                        fig2 = px.histogram(df, x='day', y='total_bill', color='time', histfunc='sum',
                                           color_discrete_sequence = px.colors.qualitative.Antique, width=550)
                        st.plotly_chart(fig2)

    else:

        st.write('<h1 style = "text-align: center;">please sigh in frist to use the analytical solutions </h1>', unsafe_allow_html=True)


    

        
