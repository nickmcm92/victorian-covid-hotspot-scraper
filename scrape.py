from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from Outbreaks import TieredOutbreaks

def main():
  options = Options() 
  options.headless = True
  driver = webdriver.Chrome(options=options)
  driver.get("https://www.dhhs.vic.gov.au/case-locations-and-outbreaks-covid-19")

  raw_tables = driver.find_elements_by_tag_name("table")
  outbreaks = TieredOutbreaks(raw_tables)

  print(f'There are {len(outbreaks.tier1)} tier 1 outbreaks, {len(outbreaks.tier2)} tier 2 outbreaks and {len(outbreaks.tier3)} tier 3 outbreaks.')

  driver.quit()

if __name__ == "__main__":
    main()