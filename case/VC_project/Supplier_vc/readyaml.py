import requests
import os
import yaml
import lib


def read_company_information(yamlpath):
    # dirpath = os.path.dirname(os.path.realpath(__file__))
    # print(dirpath)
    #
    # yamlpath=os.path.join(dirpath, "suppliers.yml")
    # print(yamlpath)
    #
    fp = open(yamlpath, "r", encoding="utf-8")
    yamldata = fp.read()
    print(yamldata)
    print(type(yamldata))
    yamldats=yaml.load(yamldata,Loader=yaml.FullLoader)['company_information']
    # print(type(yamldats))
    # print(yamldats)
    return yamldats

if __name__ == "__main__":
    dirpath = os.path.dirname(os.path.realpath(__file__))
    print(dirpath)
    yamlpath = os.path.join(dirpath, "suppliers.yml")
    print(yamlpath)
    company = read_company_information(yamlpath)
    print(company)
