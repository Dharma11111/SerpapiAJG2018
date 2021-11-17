from testDictionaryResulttt import *
from serpapi import GoogleSearch

# params = { #after 2018 sudah sampe start 180 num 20
#   "api_key": "b3ecd5f1d97e4a2f94621031611d9cb51a498abb337db047c4186a891a5c437e",
#   "engine": "google_scholar",
#   "q": "'csr' AND 'financial distress'",
#   "hl": "en",
#   "start": "180",
#   "num": "20",  #max 20
#   "as_ylo": "2018"
# }

params = { #before 2018 sudah sampe start XX num XX
  "api_key": "b3ecd5f1d97e4a2f94621031611d9cb51a498abb337db047c4186a891a5c437e",
  "engine": "google_scholar",
  "q": "'csr' AND 'financial distress'",
  "hl": "en",
  "start": "10",
  "num": "20",  #max 20
  "as_yhi": "2018"
}

def collectJurnalMainFunction():
  search = GoogleSearch(params)
  results = search.get_dict()
  print(results)
  collectJournal(results)


  
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")






# collectJurnalMainFunction()



# printListResult(14)



