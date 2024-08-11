import praw
import config.config as config
from textblob import TextBlob

def connect_reddit():
    try:
        reddit = praw.Reddit(
            client_id=config.CLIENT_ID,
            client_secret=config.CLIENT_SECRET,
            user_agent=config.USER_AGENT
        )
        return reddit
    except Exception as e:
        print(f"Erro ao conectar ao Reddit: {e}")
        exit()


def analyze_emotion(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positivo'
    elif analysis.sentiment.polarity < 0:
        return 'Negativo'
    else:
        return 'Neutro'

def get_posts(reddit, search_term, limit=5):
    subreddit = reddit.subreddit('all')
    
    try: 
        return list(subreddit.search(search_term, limit=limit))
    except Exception as e:
        print(f"Erro na pesquisa dos posts: {e}")
        return []
    
def print_analysis_results(posts):
    for post in posts:
        sentiment = analyze_emotion(post.selftext)
        print(f"Título: {post.title}")
        if post.selftext:
            print(f"Corpo do Texto: {post.selftext}")
        else:
            print("Esse post não contém corpo do Texto:")
        print(f'Sentimento: {sentiment}')
        print('---')

        
    
def main():
   
   reddit = connect_reddit()
   repeat = "s"
   
   while repeat.lower() == "s":
    search_term = input("Digite o que gostaria que fosse pesquisado no Reddit e veja a análise emocional dos posts: ").strip() 
    if not search_term:
        print("A pesquisa não pode ser vazia")
        continue
    posts = get_posts(reddit, search_term)
    print_analysis_results(posts)
    
    print("Gostaria de pesquisar novamente? Digite 'S' para Sim ou qualquer outra tecla para sair.")
    repeat = input()

if __name__ == '__main__':
    main()
