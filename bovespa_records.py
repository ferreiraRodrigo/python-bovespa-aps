import bovespa
from classes.Company import Company
import numpy as np

# Split the company data and put it all in a matrix      
def split_company_data(file):
        bovespa_file = bovespa.File(file)
        companys_index = []
        companys = []

        for bovespa_record in bovespa_file.query():
                if bovespa_record.company_name in companys_index:
                        companys[companys_index.index(bovespa_record.company_name)].add_price(bovespa_record.price_close)
                else:
                        new_company = Company(bovespa_record.company_name)
                        companys_index.append(bovespa_record.company_name)
                        companys.append(new_company)
                        companys[len(companys) - 1].add_price(bovespa_record.price_close)
        return companys, companys_index

#Return the standard deviation(based on bovespa_record.price_close) of each company         
def get_company_data(file):
        standard_deviation = []
        [companys, companys_name] = split_company_data(file)
        for company in companys:
                standard_deviation.append(np.std(company.price_history))
        
        return standard_deviation, companys_name