# README - My Sentiment Analysis

## Requirements

- Docker  

## Run App

```console
docker-compose up 
```

You need to click on the <a href="http://localhost:8080/">http://localhost:8080/</a> to navigate on the app. 

## Test 

If you want to make some test, you can use this dataset :

- <a href="https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/data">Dataset</a>

You need to unzip this dataset in the folder raw.

All the tests have to be executed in the back folder of the project.

If you want to run the unit test you, run this command : 

```console
cd back

python -m unittest discover -s . -p '*_test.py'
```