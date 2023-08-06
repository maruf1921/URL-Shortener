import requests

def shorten_link(full_link, link_name):

    API_KEY = 'c21697380423dfe231ca23f3d2f9bf6882622'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    print()
    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        print('Title:', title)
        print('Link:', short_link)
    except:
        status = data['url']['status']
        if(status == 1):
            print("the shortened link comes from the domain that shortens the link, i.e. the link has already been shortened")
        elif (status == 2):
            print("the entered link is not a link")
        elif (status == 3):
            print("the preferred link name is already taken")
        elif (status == 4):
            print("Invalid API key")
        elif (status == 5):
            print("the link has not passed the validation. Includes invalid characters")
        elif (status == 6):
            print("The link provided is from a blocked domain")
        elif (status == 8):
            print("You have reached your monthly link limit. You can upgrade your subscription plan to add more links.")
        else:
            print('Error')


link = input("Inter a link: ")
name = input("Give your link a name: ")

shorten_link(link, name)




