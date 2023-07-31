
import streamlit as st
from st_pages import add_page_title

add_page_title(layout="wide")
job_list_for_company= ['JOB: 0, https://www.linkedin.com/jobs/search/?currentJobId=3662374136&f_C=400528%2C2425698&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3662374136%2C3672253912%2C3672832066%2C3655382795%2C3665792838%2C3666584482%2C3666588320%2C3666588319%2C3677276314&refId=jU%2B9tV6qrjrK6P2UKAsr8A%3D%3D&trackingId=Wy%2BH6tF6JiJ%2FQVzPomBZqQ%3D%3D&trk=d_flagship3_company', 'JOB: 1, https://www.linkedin.com/jobs/search/?currentJobId=3672253912&f_C=400528%2C2425698&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3662374136%2C3672253912%2C3672832066%2C3655382795%2C3665792838%2C3666584482%2C3666588320%2C3666588319%2C3677276314&refId=jU%2B9tV6qrjrK6P2UKAsr8A%3D%3D&trackingId=XyHgnvCYyLMti3%2FfIJjMTw%3D%3D&trk=d_flagship3_company', 'JOB: 2, https://www.linkedin.com/jobs/search/?currentJobId=3672832066&f_C=400528%2C2425698&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3662374136%2C3672253912%2C3672832066%2C3655382795%2C3665792838%2C3666584482%2C3666588320%2C3666588319%2C3677276314&refId=jU%2B9tV6qrjrK6P2UKAsr8A%3D%3D&trackingId=IvjHhHDwBVAdCmlCVSbNiQ%3D%3D&trk=d_flagship3_company']
st.write("This is the page for Twilio-inc- company")
st.write("The following jobs are available in the company")
for i in range(len(job_list_for_company)):
    st.write(job_list_for_company[i])
