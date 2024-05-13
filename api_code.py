import requests

    
def api_func_img(keyword, api_key): 
    url = f'https://api.unsplash.com/photos/random?query={keyword}&client_id={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
       # print(data)
        image_url = data.get('urls').get('regular')
        return image_url
    else:
        return None
    




# if __name__ == '__main__':
#     print(api_func())


        #   const url = 'https://api.unsplash.com/photos/random?query=${keyword}&client_id=${apiKey}'
