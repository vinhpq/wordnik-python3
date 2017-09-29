from wordnik import *
#from confluence import Api

#wiki_url = "http://mobilerndhub.sec.samsung.net/wiki/"  # Samsung DPI Wiki url
#user = "singleid" # Your singleid
#pw = "rnd_password"   # Your R&D Corp password
#api = Api(wiki_url, user, pw)


apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'e268c9028ca1739c1600d0b184801e3309730c1a6a7d75873'
#apiKey = 'a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'
client = swagger.ApiClient(apiKey, apiUrl)

wordApi = WordsApi.WordsApi(client)
word_of_the_day = wordApi.getWordOfTheDay()

examples = word_of_the_day.examples
definitions = word_of_the_day.definitions

print(word_of_the_day.word)

for definition in definitions:
    print("(" + definition.partOfSpeech + ") " + definition.text)

for i in range(len(examples)):
    print("ex(%d"%(i+1) + ") " + examples[i].text)
