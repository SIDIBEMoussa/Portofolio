import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# SIDIBE Moussa, Data Science Ingineer, Msc. Digital Sciences
##### *Resume* 
''')

image = Image.open('Moussa.png')
st.image(image, width=150)

st.markdown('''
  <h5> I'm looking for Permanent, temporary, apprenticeship or internship contract in Data Science/Analyst or Data engineering </h5>
''', unsafe_allow_html=True)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Junior Data scientist engineer
- Passionate of data science solution for business and Marketing by using prediction, explanation, segmentation,
classification, ... to tackle business problematics
- I'm a French native speaker and fluent in English with full working proficiency
- I participated in research projects and evaluation of the Moroccan's literacy program
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
#st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/moussa-sidibe-datascientist/" target="_blank">SIDIBE Moussa</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#personal-projects">Personal Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certications">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master of Science** (Digital Sciences), *Université Paris Cité*, France',
'2022-Present')
st.markdown('''
- Master full teaches in English that combine Data Skills and teaches technics to exploit research papers
''')

txt('**Ingineer Degree** (Data Science), *Institut National de Statistique et d\'Economie Appliquée*, Morocco',
'2019-2022')
st.markdown('''
- Graduated with First Class Honors.
- These three years, I learned strong statistical skills for data analysis and forecasting, also we have covered others technics for data analysis using Machine Learning libraries like Scikit-learn, statmodels, ... and Deep Learning with PyTorch for image classification, regression, time series, ...
- We covered also database management courses that contain Database modeling and implementation, SQL to retrieve information from Database
''')

txt('**Preparatory classes for the Grandes Ecoles (CPGE)** (Mathematics and Physics), *CPGE Omar Ibn Abdel Aziz*, Morocco',
'2017-2019')
st.markdown('''
- Two years of intense working in MATHEMATICS, PHYSICS and SCIENCE FOR THE ENGINEER plus others courses
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Science intern**, Boston Consulting Group | BCG, Paris',
'Sept-Nov 2022')
st.markdown('''
**Mission**: Discover the reason of churning from customer and develop a classiﬁer to predict them and allow marketing team to keep in board with special promotion
- This internship turn around these steps from problem mapping with Business understanding, Hypotheses Framing afterward selection of requires dataset about customers
- Exploration Data Analysis to discover the data in more details, missing data, density distribution and feature engineering possibilities.
- Afterward, I applied feature engineer by creating new features, transformation, categorical data encoding, ...
- This step is for building a model for churn prediction and defining a threshold based on churn probability computed by taking in account the accuracy of the model
and afterward adjust the marketing strategies that can keep the potential churners inboard and prevent company to lose money.
''')

txt('**Data Analyst**, National Agency against illiteracy(ANLCA), Morocco',
'March-July 2022')
st.markdown('''
  **Mission**: Evaluation of literacy programs (the determinants of the validation and certiﬁcation of learning) \\
**About**: ANLCA was created and placed in direction of the chief of government of Morocco. This agency is charged to eradicate illiteracy from Morocco with a defined program and agenda.
Then the program of alphabetization was elaborated and administrated in all regions of Morocco.
- Firstly, I started to contextualize the study and familiarize myself with international context of evaluation of public policies and alphabetization.
- According to the data in our disposal and statistical tools that can be applied we evaluate the target variable **_success of student_** and I make a model by taking into account interpretability of model as the problem of evaluation
- In this mission, we faced problem of data quality, the best performance indicator that can explain the success of the student with certain characteristics according to the region, professors, literate parent, ... but information available about individuals was few poor in quality
- Result : As the model built was statistically significant, we interpret the result and recommend the structuration of the database and the variables to include in the database for the further evaluation

''')

txt('**Data Engineer/Data Science**, Kavaa Global Services, Morocco',
'July-Sept 2021')
st.markdown('''
  **Mission**: Implementation of the ODK-X data collection tool and analysis of covid-19 data in Morocco \\
**About**: The project was about SMART MEDICAL GATE which has the main goal to create connected hospital to allow people of hard accessible area of African countries with healthcare desert to get access to medical consultation from Physicians from big City.

- Firstly, I handle the process of set up the software on my computer and for enterprise and produce the documentation of different problem faced during the process
- Afterward, I connect the software with Digital Ocean to gathered the data collected and centralize them.
- Data is collected from different user account with SmartPhone or computer and the data collected are sent to the server on Digital Ocean
- After that, I worked on collection from open source the Covid-19 data of Morocco and Analyze them and model it by using time series prediction and coming covid-peak.
''')



#####################
st.markdown('''
## Personal Projects
''')

txt('**Data Engineer/Data Science**,Université Paris Cité, France',
'June-July 2023')
st.markdown('''
  **Mission**: This project was about to develop an image segmentation model on a few images

- In this project, I start by preprocessing images and explore them. After that as we have just twenty(20) images of Retina Blood Vessel, coming data augmentation with vertical, horizontal and rotation flipping to create sixty(60) others images as trianing data set and twenty(20) images for test set
- Followed by creating Unet model from scratch on Pytorch and trained on augmented and scaled images
- To optimize learning process, Adam optimizer and ReduceLROnPlateau was used to tune optimization process and learning rate
- Results: The model achieve an accuracy: 96.72%, Recall = 82.28%
''')

txt('**Data Science**,Institut National de Statistique et d\'Economie Appliquée', 'Dec 2021 - Jan 2022')
st.markdown('''
  **Mission**: This project was about to implement a Telegram chatboot
- Understand how to use telegram API
- Specify the need of ChatBoot
- Analyse the need described in the speciﬁcation document
- Designing and implementing of a conversation
- Deploying in local environment
''')

txt('**Data Science**,Institut National de Statistique et d\'Economie Appliquée', 'Dec 2021 - Jan 2022')
st.markdown('''
  **Mission**: This project was about demand forecasting of BIOBLANC

- This project contains lot of challenges. First one, was multicollinearity between independent or regressors variables and the second was deal high dimensionality.
- As a regression problem, many models were candidates for the task. To solve the problem of multicollinearity, we use ACP one side to solve the both problem, but the correlation with the target was weak.
Then we tend to use a strategy that will use PCA and maximize at the same time the correlation with the target. Then we develop from scratch **_Partial Least Square Regression_** on SAS and R and compare with other model like **Lasso, Ridge Regression**, ...
- **Results**: As the result we achieve RMSE of 0.55 for PLS, 0.57 for Ridge and 0.47 for Lasso Regression and the model was highly interpretable with the contribution of each feature in the prediction.
''')


#txt4('AutoWeka', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')



#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`,`C`, `Java`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`, `BigQuery`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `Tableau`, `PowerBI`, `Kepler`')
txt3('Machine Learning', '`scikit-learn`, , `BigQueryML`')
txt3('Deep Learning', '`Pytorch`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `MLFlow`') # `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`
txt3('Cloud', '`Azure`, `GCP`')  

#####################
st.markdown('''
## Certifications
''')
st.write('''
   - [Google Cloud Big Data and Machine Learning Fundamentals | Coursera](https://www.coursera.org/account/accomplishments/certificate/UATHS87KN2AC) 
   - [Machine Learning with Python | Coursera](https://www.coursera.org/account/accomplishments/certificate/75NBTL6LJF3H)
   - [Modernizing with GCP | Coursera](https://www.coursera.org/account/accomplishments/certificate/G9ATVZL9ACM6)
   - [Building Batch Data Pipelines on GCP | Coursera](https://www.coursera.org/account/accomplishments/certificate/4BGHXMC2GGE7)
   - [Neural Networks and Deep Learning | Coursera](https://www.coursera.org/account/accomplishments/certificate/VWN8NFLZBL22)
   - [Dashboard with Tableau | OpenClassrooms](https://openclassrooms.com/fr/course-certificates/7319986865)
   - [Database Design and Programming With SQL | Oracle](https://inseaac-my.sharepoint.com/personal/msidibe_insea_ac_ma/_layouts/15/onedrive.aspx?id=\%2Fpersonal\%2Fmsidibe\%5Finsea\%5Fac\%5Fma\%2FDocuments\%2FCertificates\%2FOracle%20Academy\%20Final\%20Exam%20Award\%20%2D%20SIDIBE%20Moussa\%2Epdf&parent=\%2Fpersonal\%2Fmsidibe\%5Finsea\%5Fac\%5Fma\%2FDocuments\%2FCertificates&ga=1)
   - [Natural Language Processing with Classification and Vector Spaces | Coursera](https://www.coursera.org/account/accomplishments/certificate/6YB7HUE2N9CU)
  
  ''')


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/moussa-sidibe-datascientist/')
#txt2('Twitter', 'https://twitter.com/thedataprof')
txt2('GitHub', 'https://github.com/SIDIBEMoussa')
#txt2('', 'https://github.com/chaninlab/')
#txt2('', 'https://github.com/dataprofessor')
#txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
#txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
#txt2('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
#txt2('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
#txt2('Publons', 'https://publons.com/a/303133/')
