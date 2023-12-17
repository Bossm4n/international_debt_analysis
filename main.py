import json
import csv
import pandas as pd
import numpy as np

def get_misssing_values(total_data):
    all_categories_num = [{'numof_country_name': 0}, {'numof_country_code': 0}, {'numof_counterpart_area_name': 0},
                          {'numof_counterpart_area_code': 0}, {
                              'numof_series_name': 0}, {'numof_series_code': 0},
                          {'numof_2000': 0}, {'numof_2001': 0}, {'numof_2002': 0}, {
                              'numof_2003': 0}, {'numof_2004': 0},
                          {'numof_2005': 0}, {'numof_2006': 0},
                          {'numof_2007': 0}, {'numof_2008': 0}, {'numof_2009': 0}, {
                              'numof_2010': 0}, {'numof_2011': 0},
                          {'numof_2012': 0}, {'numof_2013': 0},
                          {'numof_2014': 0}, {'numof_2015': 0}, {'numof_2016': 0}, {
                              'numof_2017': 0}, {'numof_2018': 0},
                          {'numof_2019': 0}, {'numof_2020': 0}]

    def get_value(category_name, temp_name, category_value):
        if category_name == temp_name and category_value == '':
            return 1
        else:
            return 0

    for line_of_data in total_data:
        for data_point in line_of_data.items():
            category, value = data_point

            line_of_data_name = 'numof_' + category.lower().replace(' ', '_').replace('-', '_')
            for category_dict in all_categories_num:
                temp_category_name = list(category_dict.keys())[0]
                category_dict[temp_category_name] += get_value(
                    temp_category_name, line_of_data_name, value)

    for i in all_categories_num:
        name = list(i.keys())[0]
        value = list(i.values())[0]
        print(f"The {name.replace('_', ' ')} values missing is {value}")


def get_correct_values(total_data):
    all_categories_num = [{'numof_country_name': 0}, {'numof_country_code': 0},
                          {'numof_counterpart_area_name': 0},
                          {'numof_counterpart_area_code': 0}, {
                              'numof_series_name': 0},
                          {'numof_series_code': 0},

                          {'numof_2000': 0}, {'numof_2001': 0}, {
                              'numof_2002': 0}, {'numof_2003': 0},
                          {'numof_2004': 0},
                          {'numof_2005': 0}, {'numof_2006': 0},
                          {'numof_2007': 0}, {'numof_2008': 0}, {
                              'numof_2009': 0}, {'numof_2010': 0},
                          {'numof_2011': 0},
                          {'numof_2012': 0}, {'numof_2013': 0},
                          {'numof_2014': 0}, {'numof_2015': 0}, {
                              'numof_2016': 0}, {'numof_2017': 0},
                          {'numof_2018': 0},
                          {'numof_2019': 0}, {'numof_2020': 0}]

    def get_value(category_name, temp_name, category_value):
        if category_name == temp_name and category_value != '':
            return 1
        else:
            return 0

    for line_of_data in total_data:
        for data_point in line_of_data.items():
            category, value = data_point

            line_of_data_name = 'numof_' + category.lower().replace(' ', '_').replace('-', '_')
            for category_dict in all_categories_num:
                temp_category_name = list(category_dict.keys())[0]
                category_dict[temp_category_name] += get_value(
                    temp_category_name, line_of_data_name, value)

    for i in all_categories_num:
        name = list(i.keys())[0]
        value = list(i.values())[0]
        print(f"The {name.replace('_', ' ')} values correct is {value}")


def remove_missing_values(unclean_data):
    cleaned_data = unclean_data
    for data_line in cleaned_data:
        delete_arr = []
        for i in data_line:
            if i == '1970' or i == '1971' or i == '1972' or i == '1973' or i == '1974' or i == '1975' or i == '1976' or i == '1977' or i == '1978' or i == '1979' or i == '1980' or i == '1981' or i == '1982' or i == '1983' or i == '1984' or i == '1985' or i == '1986' or i == '1987' or i == '1988' or i == '1989' or i == '1990' or i == '1991' or i == '1992' or i == '1993' or i == '1994' or i == '1995' or i == '1996' or i == '1997' or i == '1998' or i == '1999' or i == '2021' or i == '2022' or i == '2023' or i == '2024' or i == '2025' or i == '2026' or i == '2027' or i == '2028':
                delete_arr.append(i)
        for i in delete_arr:
            data_line.pop(i)
    return cleaned_data


def get_useful_fields(unclean_data):
    cleaned_data = unclean_data
    series_names_to_keep = [
        "Average grace period on new external debt commitments (years)",
        "Average grant element on new external debt commitments (%)",
        "Average maturity on new external debt commitments (years)",
        "Concessional debt (% of total external debt)",
        "Current account balance (current US$)",
        "Exports of goods, services and primary income (current US$)",
        "External debt stocks (% of exports of goods, services and primary income)",
        "External debt stocks (% of GNI)",
        "External debt stocks, long-term (DOD, current US$)",
        "External debt stocks, short-term (DOD, current US$)",
        "External debt stocks, total (DOD, current US$)",
        "Foreign direct investment, net inflows in reporting economy (DRS, current US$)",
        "GNI (current US$)",
        "Grants, excluding technical cooperation (current US$)",
        "Imports of goods, services and primary income (current US$)",
        "Interest forgiven (current US$)",
        "Interest payments on external debt (% of GNI)",
        "Interest payments on external debt, public sector (PPG) (INT, current US$)",
        "Interest payments on external debt, short-term (INT, current US$)",
        "Interest payments on external debt, total (INT, current US$)",
        "Short-term debt (% of total external debt)",
        "Total change in external debt stocks (current US$)",
        "Total debt service (% of exports of goods, services and primary income)",
        "Total reserves (% of total external debt)",
        "Total reserves (includes gold, current US$)",
        "Use of IMF credit (DOD, current US$)",
        "Use of IMF credit, SDR allocations (DOD, current US$)"
    ]

    filtered_data = [
        data_line for data_line in cleaned_data if data_line['Series Name'] in series_names_to_keep]

    return filtered_data


def get_clean_json(unclean_data):
    clean_data = remove_missing_values(unclean_data)
    cleaner_data = get_useful_fields(clean_data)
    with open("IDS_ALLCountries_Data_clean.json", "w") as outfile:
        json.dump(cleaner_data, outfile)
    print('done :)')


def get_useful_years(individual_data):
    years_to_keep = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
                     '2012', '2013',
                     '2014', '2015', '2016', '2017', '2018', '2019', '2020']
    years_only_data = {}
    for i in individual_data:
        if i in years_to_keep:
            if individual_data[i] == '': years_only_data[i] = np.nan
            else: years_only_data[i] = individual_data[i]
    return years_only_data


def rearrange_data(unarranged_data):
    arranged_data = {}
    temp_country_data = []
    country_name = unarranged_data[0]['Country Code']

    for data_line in unarranged_data:
        current_country_name = data_line['Country Code']

        if country_name == current_country_name:
            temp_country_data.append(
                {data_line['Series Name']: get_useful_years(data_line)})
        else:
            arranged_data[country_name] = temp_country_data
            temp_country_data = [
                {data_line['Series Name']: get_useful_years(data_line)}]
            country_name = current_country_name
    arranged_data[country_name] = temp_country_data
    return arranged_data


def json_to_csv(json_data, csv_filename):
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row
        header = json_data[0].keys()
        csv_writer.writerow(header)

        # Write the data rows
        for item in json_data:
            csv_writer.writerow(item.values())
    return


# Load in the first json file - original json:
datafile = open('IDS_ALLCountries_Data.json')
data = json.load(datafile)

# Call this function, when "IDS_ALLCountries_Data_clean.json" is empty, to send in the 1st phase of clean data:
get_clean_json(data)


# Load in the 1st phase of the cleaned data:
datafile2 = open('IDS_ALLCountries_Data_clean.json')
data2 = json.load(datafile2)

# Call this function when the data has not been re-arranged to be sorted by country:
phase_2_data = rearrange_data(data2)

# Send/write the re-arranged data to a json file:
with open("2nd_phase_data.json", "w") as outfile:
    json.dump(phase_2_data, outfile)
print('done :)')


datafile3 = open('2nd_phase_data.json')
data3 = json.load(datafile3)
# json_to_csv(sudan'temp_country_data.csv')

for i in data3:
    categories_data = data3[i]
    new_json = []
    for j in categories_data:
        category_data_name = next(iter(j))
        datainjson = {'Category': category_data_name, **j[category_data_name]}
        new_json.append(datainjson)
    with open(f"countries_data/{i}", "w") as outfile:
        json.dump(new_json, outfile)
