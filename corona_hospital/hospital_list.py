def extract_info(hospital_list):
    result = []
    for i in hospital_list:
        city = i.contents[1].string
        location = i.contents[2].string
        name = i.contents[3].text.split()[0]
        number = i.contents[4].string

        hospital_info = {
            "city" : city,
            "location" : location,
            "name" : name,
            "number" : number
        }
        result.append(hospital_info)
    
    return result
    print(result)