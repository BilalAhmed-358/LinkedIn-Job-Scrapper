
import streamlit as st
from st_pages import add_page_title

add_page_title(layout="wide")
job_list_for_company= ['JOB 1 \nLink: https://www.linkedin.com/jobs/search/?currentJobId=3676007668&f_C=2425698&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3676007668%2C3629701760%2C3663798086%2C3612586367%2C3638774484%2C3649880633%2C3665793627%2C3649226694%2C3649230245&refId=C1MvOG7swEEebHP0s%2FC4DQ%3D%3D&trackingId=gq9GDC9%2F9rpBbiQ0HxxmfQ%3D%3D&trk=d_flagship3_company', 'JOB 2 \nLink: https://www.linkedin.com/jobs/search/?currentJobId=3629701760&f_C=2425698&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3676007668%2C3629701760%2C3663798086%2C3612586367%2C3638774484%2C3649880633%2C3665793627%2C3649226694%2C3649230245&refId=C1MvOG7swEEebHP0s%2FC4DQ%3D%3D&trackingId=bnsNBdzHBdbHgqdJ%2B4VIIA%3D%3D&trk=d_flagship3_company', 'JOB 3 \nLink: https://www.linkedin.com/jobs/search/?currentJobId=3663798086&f_C=2425698&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3676007668%2C3629701760%2C3663798086%2C3612586367%2C3638774484%2C3649880633%2C3665793627%2C3649226694%2C3649230245&refId=C1MvOG7swEEebHP0s%2FC4DQ%3D%3D&trackingId=65gJMY1LIAhUjsA92VBQGQ%3D%3D&trk=d_flagship3_company']
st.write("This is the page for Segment-io company")
st.write("The following jobs are available in the company")
for i in range(len(job_list_for_company)):
    st.write(job_list_for_company[i])
