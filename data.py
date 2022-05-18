apidata = []
apidata.append(["jano", "fero", "miso"])
apidata.append(["peto", "tono", "ondro"])
apidata.append(["gusto", "husto", "skusto"])
apidata.append(["majka", "janka"])

def get_api_data(start):
        if len(apidata) > start :
                return apidata[start]
        else:
                pass


print("Source:")
print(apidata)

result = []
index = 0

while True:
        response = get_api_data(index)
        if response:
                for data in response:
                        result.append(data)
                index += 1
        else:
                break

print("Result:")
print (result)
