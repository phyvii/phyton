import webbrowser
import requests

url = input("Enter the website url: ")
zapisane = "http://archive.org/wayback/available?url="
odpowiedz = requests.get(zapisane+url)

if odpowiedz.status_code == 200:
    odebranee= odpowiedz.json()
    archiwalne = [odebranee['archived_snapshots']['closest']]

    for i in range(2):
        czas = archiwalne[i]['timestamp']
        data = f"{zapisane}{url}&timestamp={czas}"
        odpowiedz = requests.get(data)
        data = odpowiedz.json()
        archiwalne.append(data['archived_snapshots']['closest'])

    i = 1
    for zapis in archiwalne:
        archiwalne = zapis['url']
        time = zapis['timestamp']
        filename = f"{time}{i}.html"
        i = i+1
        odpowiedz = requests.get(archiwalne)
        content = odpowiedz.content
        with open(filename, "wb") as f:
            f.write(content)

        print(filename)

else:
    print("something went wrong")
