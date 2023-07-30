
import streamlit as st
from st_pages import add_page_title

add_page_title(layout="wide")
job_list_for_company= ['JOB: 0, https://www.linkedin.com/jobs/search/?currentJobId=3667914114&f_C=1035%2C1418841%2C1386954%2C165397%2C3763403%2C3290211%2C263515%2C3641570%2C2270931%2C3238203%2C10073178%2C1148098%2C5097047%2C589037%2C692068%2C3178875%2C164951%2C18086638%2C19537%2C30203%2C1889423%2C19053704%2C2446424%2C11206713&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3667914114%2C3670701642%2C3669528543%2C3664010726%2C3670952962%2C3662374426%2C3664013273%2C3678412813%2C3663684385&refId=SmNL7dtA8mgPfMgmaRbYPQ%3D%3D&trackingId=XqN96GXz948y%2FyIFNfSmkw%3D%3D&trk=d_flagship3_company', 'JOB: 1, https://www.linkedin.com/jobs/search/?currentJobId=3670701642&f_C=1035%2C1418841%2C1386954%2C165397%2C3763403%2C3290211%2C263515%2C3641570%2C2270931%2C3238203%2C10073178%2C1148098%2C5097047%2C589037%2C692068%2C3178875%2C164951%2C18086638%2C19537%2C30203%2C1889423%2C19053704%2C2446424%2C11206713&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3667914114%2C3670701642%2C3669528543%2C3664010726%2C3670952962%2C3662374426%2C3664013273%2C3678412813%2C3663684385&refId=SmNL7dtA8mgPfMgmaRbYPQ%3D%3D&trackingId=8ZJHZn%2BIVoaFzT2EQrgiQg%3D%3D&trk=d_flagship3_company', 'JOB: 2, https://www.linkedin.com/jobs/search/?currentJobId=3669528543&f_C=1035%2C1418841%2C1386954%2C165397%2C3763403%2C3290211%2C263515%2C3641570%2C2270931%2C3238203%2C10073178%2C1148098%2C5097047%2C589037%2C692068%2C3178875%2C164951%2C18086638%2C19537%2C30203%2C1889423%2C19053704%2C2446424%2C11206713&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3667914114%2C3670701642%2C3669528543%2C3664010726%2C3670952962%2C3662374426%2C3664013273%2C3678412813%2C3663684385&refId=SmNL7dtA8mgPfMgmaRbYPQ%3D%3D&trackingId=zSM5Y2ZvWZKSxa7nF8ictw%3D%3D&trk=d_flagship3_company']
st.write("This is the page for Microsoft company")
st.write("The following jobs are available in the company")
for i in range(len(job_list_for_company)):
    st.write(job_list_for_company[i])
