import praw
import config.config as config
from textblob import TextBlob

reddit = praw.Reddit(
    client_id=config.CLIENT_ID,
    client_secret=config.CLIENT_SECRET,
    user_agent=config.USER_AGENT
)


def analyze_emotion(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positivo'
    elif analysis.sentiment.polarity < 0:
        return 'Negativo'
    else:
        return 'Neutro'
    
def main():
    
   repeat = "s"
   
   while repeat.lower() == "s":
    print("Digite o que gostaria que fosse pesquisado no Reddit e veja a análise emocional dos posts:")
    search_term = input()
    subreddit = reddit.subreddit('all')
    
    
    for post in subreddit.search(search_term, limit=4):
        sentiment = analyze_emotion(post.selftext)
        print(f'Título: {post.title}')
        print(f'Corpo do Texto: {post.selftext}')
        print(f'Sentimento: {sentiment}')
        print('---')
    
    print("Gostaria de pesquisar novamente? S ou N")  
    
    repeat = input()

if __name__ == '__main__':
    main()