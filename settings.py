import json

brands,fueltype = [],[]
brandmodels, __jsondata = {},{}

with open("settings.json", encoding="utf-8") as __file:
    __jsondata = json.loads(__file.read())
for __models in __jsondata["Data"]:
    brandmodels[__models["brand"]] = __models["models"]
    brands.append(__models["brand"])
brands.sort()
fueltype = __jsondata["Brandstof"]
brands = __jsondata["Merken"]

if __name__ == "__main__":
    __jsondata["BrandModels"] = brandmodels
    __jsondata.pop("Data")
    with open("testdata.json", 'w+', encoding="utf-8") as __test:
        json.dump(__jsondata, __test, ensure_ascii=False, indent=1)
