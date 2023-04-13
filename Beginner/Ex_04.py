websites = (
  "google.com",
  "https://naver.com"
)

for website in websites:
  if not (website.startswith("https://")):
    website = f"https://{website}"
  print(website)
