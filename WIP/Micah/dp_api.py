dpi_api_base_url = "https://www.donorperfect.net/prod/xmlrequest.asp?action=dp_gifts&params="
dpi_api_username = "123"
dpi_api_password = "123"

def format_url(params):
    final_url = dpi_api_base_url
    for index, val in enumerate(params):
        if index < len(params):
            if type(val).__name__ == "str":
                final_url+= "'" + val + "'" + ','
            else:
                final_url+=str(val) + ','
        else:
            if type(val).__name__ == "str":
                final_url+= "'" + val + "'"
            else:
                final_url+=str(val)
    formatted_url = final_url + r"&login=" + dpi_api_username + r"&pass=" + dpi_api_password
    return formatted_url
