#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options 

class Outbreak:
  """
  Location
  Site
  Exposure Period
  Note
  """
  def __init__(self, cell):
    self.location = cell[0]
    self.site = cell[1]
    self.exposure_period = cell[2]
    self.note = cell[3]

class TieredOutbreaks:
  def __init__(self, tables):
    self.tier1 = extract_outbreaks_from_table(tables[0])
    self.tier2 = extract_outbreaks_from_table(tables[1])
    self.tier3 = extract_outbreaks_from_table(tables[2])

def extract_outbreaks_from_table(table):
  rows = table.find_elements_by_tag_name("tr")
  rows.pop(0) # remove the header row
  outbreaks = []
  for row in rows:
    cells = row.find_elements_by_tag_name("td")
    cell_data = list(map(lambda cell: cell.text, cells))
    if(cell_data == ['-', '-', '-', '-']): # catch for empty data
      continue
    outbreak = Outbreak(cell_data)
    outbreaks.append(outbreak)
  return outbreaks

def main():
  options = Options() 
  options.headless = True
  driver = webdriver.Chrome(options=options)
  driver.get("https://www.dhhs.vic.gov.au/case-locations-and-outbreaks-covid-19")

  outbreaks = TieredOutbreaks(driver.find_elements_by_tag_name("table"))

  print(f'There are {len(outbreaks.tier1)} tier 1 outbreaks, {len(outbreaks.tier2)} tier 2 outbreaks and {len(outbreaks.tier3)} tier 3 outbreaks.')

  driver.quit()

if __name__ == "__main__":
    main()