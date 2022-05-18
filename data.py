# define api data as a list to simulate paged responses
apidata = []
apidata.append(["jano", "fero", "miso"])
apidata.append(["peto", "tono", "ondro"])
apidata.append(["gusto", "husto", "skusto"])
apidata.append(["majka", "janka"])

# function to get api data with 0-based start as an offset, return empty if no data left
def get_api_data(start):
        if len(apidata) > start :
                return apidata[start]
        else:
                pass

# print the source api data as a list of lists
print("Source:")
print(apidata)

# define result as empty array
result = []

# initialize the offset
index = 0

# loop over the api request function until empty response and save responses to the result list
while True:
        response = get_api_data(index)
        if response:
                for data in response:
                        result.append(data)
                index += 1
        else:
                break

# print the result                
print("Result:")
print (result)
