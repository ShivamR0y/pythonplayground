import openpyxl,pprint
print('Opening workbook....')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
contyData = {}

print('Reading rows...')
for row in range(2,sheet.get_highest_row() + 1):
    state = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value
    #make sure the key for this state exist
    countyData.setdefault(state,{})
    #make sure the key for the county exist
    countyData[state].setdefault(county,{'tracts':0,'pop':0})

    contyData[state][county]['tracts']+=1
    countyData[state][county]['pop']+=int(pop)

print('writing data')
resultFile = open('census2010.txt','w')
resultFile.write('allData = '+pprint.pformat(countyData))
resultFile.close()
print('Done.')
