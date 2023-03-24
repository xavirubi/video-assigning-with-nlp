import json
import spacy
from deep_translator import GoogleTranslator


f_articles = open('articles.json')
f_videos = open('videos.json')

articles_data = json.load(f_articles)
videos_data = json.load(f_videos)

article_ids = list(article_id for article_id in articles_data.keys())
video_ids = list(video_id for video_id in videos_data.keys())

def article_keywords(id):
    return articles_data[id]["keywords"]

def video_keywords(id):
    return videos_data[id]["keywords"]


nlp = spacy.load("en_core_web_lg")

related = {i: [] for i in range(0, len(article_ids))}

for i in range(0, len(article_ids)):
    article = nlp(GoogleTranslator(source='es', target='en').translate(' '.join(article_keywords(article_ids[i]))))
    for j in range(0, len(video_ids)):
        video = nlp(GoogleTranslator(source='es', target='en').translate(' '.join(video_keywords(video_ids[j]))))
        similarity = float(int(article.similarity(video) * 10000) / 100)
        related[i].append((j, similarity))


def convert_results_to_dict(related_videos):
    for videos in related_videos.values():
        videos.sort(key=lambda tup: tup[1], reverse=True)

    for videos in related_videos.values():
        while len(videos) > 3:
            videos.pop(len(videos) - 1)

    results = {article_id: {} for article_id in article_ids}
    for article, videos in enumerate(related_videos.values()):
        for video in videos:
            results[article_ids[article]].update({video_ids[video[0]]: {"score": video[1]}})
    return results

results = convert_results_to_dict(related)

results_json = json.dumps(results, indent=4)

with open("video_assigning_results.json", "w") as outfile:
    outfile.write(results_json)


if __name__ == "__main__":
