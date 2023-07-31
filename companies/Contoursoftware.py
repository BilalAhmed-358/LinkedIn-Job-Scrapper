
import streamlit as st
from st_pages import add_page_title

add_page_title(layout="wide")
job_list_for_company= ['JOB 1 \nLink: https://www.linkedin.com/jobs/search/?currentJobId=3523766702&f_C=1801323&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3523766702%2C3668224915%2C3669962166%2C3668329466%2C3668334189%2C3670543803%2C3669960389%2C3669960388%2C3666484817&refId=q7r58jerbqjKt1u8zO3brA%3D%3D&trackingId=Q%2BofZZiDiOUZIJOXZKrSPQ%3D%3D&trk=d_flagship3_company', 'JOB 2 \nLink: https://www.linkedin.com/jobs/search/?currentJobId=3668224915&f_C=1801323&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3523766702%2C3668224915%2C3669962166%2C3668329466%2C3668334189%2C3670543803%2C3669960389%2C3669960388%2C3666484817&refId=q7r58jerbqjKt1u8zO3brA%3D%3D&trackingId=SVw81bTFNwgF7gj6aKc8uA%3D%3D&trk=d_flagship3_company', 'JOB 3 \nLink: https://www.linkedin.com/jobs/search/?currentJobId=3669962166&f_C=1801323&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3523766702%2C3668224915%2C3669962166%2C3668329466%2C3668334189%2C3670543803%2C3669960389%2C3669960388%2C3666484817&refId=q7r58jerbqjKt1u8zO3brA%3D%3D&trackingId=5LS42H26PEuyrZDUpPGQGg%3D%3D&trk=d_flagship3_company']
st.write("This is the page for Contoursoftware company")
st.write("The following jobs are available in the company")
for i in range(len(job_list_for_company)):
    st.write(job_list_for_company[i])
