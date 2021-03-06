import bovespa
from classes.Company import Company
import numpy as np

# Split the company data in two arrays(companys = historical prices and companys_index = companys name )   
def split_company_data(file):
        bovespa_file = bovespa.File(file)
        companys_index = []
        companys = []

        for bovespa_record in bovespa_file.query():
                if bovespa_record.company_name in companys_index:
                        companys[companys_index.index(bovespa_record.company_name)].add_price(bovespa_record.price_open ,bovespa_record.price_close)
                else:
                        companys_index.append(bovespa_record.company_name)
                        new_company = Company(bovespa_record.company_name)
                        new_company.add_price(bovespa_record.price_open ,bovespa_record.price_close)
                        companys.append(new_company)    

        return companys, companys_index

#Return both risk and average profit for each comapny         
def get_company_data(file, minimum_activity):
        standard_deviation = []
        average_profit = []
        profit_history = []

        [companys, companys_name] = split_company_data(file)
        for index, company in enumerate(companys):
                if(len(company.price_close_history) < minimum_activity):
                        companys.pop(index)
                        companys_name.pop(index)
                else:
                        standard_deviation.append(company.get_standard_deviation())
                        average_profit.append(company.get_average_profit())
                        profit_history.append(company.get_profit_history())

        return standard_deviation, average_profit, profit_history, companys_name