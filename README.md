# Video assigning using NLP
## Required libraries
We will use the spacy library for doing NLP:
```
pip install -U spacy
```
and the deep-translator for translating from spanish to english:
```
pip install -U deep_translator
```

## Model
As NLP model we will use en_core_web_lg from spacy as it has been the best performing one:
```
python -m spacy download en_core_web_lg
```

## How it works
First we load the model into a variable:
```
nlp = spacy.load("en_core_web_lg")
```
after reading, extracting and translating the needed data from the jsons (articles.json and videos.json), it's time to process it:
```
article = nlp(article_extracted_data)
video = nlp(video_extracted_data)
```
as extracted_data we use keywords translated to english.

Then we can compare the data and give it a score:
```
score = article.similarity(video)
```

## Score
The score is a float from 0 to 100. In this case, it represents how related is a video to an article in terms of context, meaning and topic.
Where 0 is not related at all and 100 is completely related.

## Results
Once we have a similarity score for an article with each video, we pick the 3 best results and add them to the results json file.
