import re
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?=%E2%9C%93&term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text,"html.parser")
  jobs = soup.find_all("section",class_ ="jobs")
  # class 가 job인 모든 section을 찾는다