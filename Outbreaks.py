class TieredOutbreaks:
  def __init__(self, raw_tables):
    if(len(raw_tables) != 3):
      raise Exception(f'Invalid table data provided. 3 tables should be input, {len(raw_tables)} was provided.')
    self.tier1 = self.extract_from_table(raw_tables[0])
    self.tier2 = self.extract_from_table(raw_tables[1])
    self.tier3 = self.extract_from_table(raw_tables[2])

  def extract_from_table(self, table):
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

class Outbreak:
  """
  Location
  Site
  Exposure Period
  Note
  """
  def __init__(self, cells):
    if(len(cells) != 4):
      raise Exception(f'Invalid cell data provided. 4 cells should be input, {len(cells)} were provided.')
    self.location = cells[0]
    self.site = cells[1]
    self.exposure_period = cells[2]
    self.note = cells[3]