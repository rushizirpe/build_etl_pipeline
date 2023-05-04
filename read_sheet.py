import pandas as pd
import datetime as dt


def read_sheet(_file_path, _sheet_name, _nrows):

    # sheet = pd.read_excel('mrtssales92-present.xls', sheet_name=_sheet_name, header = 4, nrows = _nrows)
    sheet = pd.read_excel(_file_path, sheet_name = _sheet_name, header = 4, nrows = _nrows)
   
    # drop the first and last columns [Unnamed: 0, TOTAL] 
    nr_of_columns = sheet.shape[1]
    # print('nr_of_columns: ', nr_of_columns)

    # if will be true if the sheet_name= 2021
    if nr_of_columns > 6:
        sheet.drop(sheet.columns[[0, -1]],axis = 1, inplace = True)
   
   # else will be true if the sheet_name= 2021
    else:
        sheet.drop(sheet.columns[[0, -2, -1]],axis = 1, inplace = True)
        

    # cleaning column names
    old_columns = sheet.columns
    _columns = list(old_columns)
    _columns[1:] = [index.replace('.',' ').replace('  ', ' ').replace(' ', ', ')for index in _columns[1:]]

    # changing column name to date format (e.g Jan, 20 -->  2020-01-01)
    _columns[1:] = [dt.datetime.strftime(dt.datetime.strptime(index,'%b, %Y'),'%Y-%m-%d') for index in _columns[1:]]
    _columns[0] = 'business_kind'
    column_names = dict(zip(old_columns,_columns))
    sheet.rename(columns=column_names, inplace=True)

    # drop the first row where business_kind = NOT ADJUSTED

    sheet.drop(sheet.loc[sheet['business_kind']=='NOT ADJUSTED'].index, inplace = True)

    #resetting the index to 0 --> after dropping the row with index 0, the index was starting at 1.
    sheet.reset_index(drop = True , inplace = True)

    # drop the first row where business_kind = NOT ADJUSTED

    sheet.drop(sheet.loc[sheet['business_kind']=='NOT ADJUSTED'].index, inplace = True)

    #resetting the index to 0 --> after dropping the row with index 0, the index was starting at 1.
    sheet.reset_index(drop = True , inplace = True)

    # clean content of column 'business_kind'
    _business_kind = sheet['business_kind'].astype(str)
    _business_kind = [index.replace(' ', '_').replace(',','').replace('.','').replace('(1)','').replace('-','_').replace('\'','').replace('(','').replace(')','').lower() for index in _business_kind]
    sheet['business_kind'] = _business_kind

    # melt pivot table
    sheet_melt = sheet.melt(id_vars='business_kind', var_name = 'month', value_name = 'amount_million')

    # replace non-numeric values in 'amount_million' to NaN
    _amount_million = sheet_melt['amount_million'].apply(pd.to_numeric, errors='coerce')
    sheet_melt['amount_million'] = _amount_million

    return sheet_melt
