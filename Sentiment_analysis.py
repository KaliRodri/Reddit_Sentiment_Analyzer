import praw
import config.config as config
import tkinter as tk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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


def analyze_emotion(title, body):
    analyzer = SentimentIntensityAnalyzer()
   
    title_sentiment = analyzer.polarity_scores(title)
    body_sentiment = analyzer.polarity_scores(body) if body else {'compound': 0}
    
    combined_sentiment = (title_sentiment['compound'] + body_sentiment['compound']) /2
    
    if combined_sentiment > 0:
        sentiment = 'Positivo'
    elif combined_sentiment < 0:
        sentiment = 'Negativo'
    else: 
        sentiment = 'Neutro'
    
    return sentiment
    

def get_posts(reddit, search_term, limit=5):
    subreddit = reddit.subreddit('all')
    
    try: 
        return list(subreddit.search(search_term, limit=limit))
    except Exception as e:
        print(f"Erro na pesquisa dos posts: {e}")
        return []
    
  
def analyze_post():
    search_term = entry.get().strip()
    if not search_term:
        result_text.insert(tk.END, "A pesquisa não pode ser vazia\n")
        return  
    
    reddit = connect_reddit()
    posts = get_posts(reddit, search_term)
    
    result_text.delete(1.0, tk.END)
    for post in posts:
        sentiments = analyze_emotion(post.title, post.selftext)
        result_text.insert(tk.END, "Título: ", "bold",  f"{post.title}\n")
        if post.selftext:
            result_text.insert(tk.END, "Corpo do Texto: ", "bold",  f"{post.selftext}\n")
        else:
            result_text.insert(tk.END, "Esse post não contém corpo do Texto\n")
        result_text.insert(tk.END, "Sentimento: ", "bold", f" {sentiments}\n")
        result_text.insert(tk.END, "---\n")
            
# Configuração da janela principal                  
root = tk.Tk()
root.title("Reddit Sentiment Analyzer")
root.geometry("800x600")

# Configuração do Label 
label = tk.Label(root, text="Digite o que gostaria que fosse pesquisado no Reddit e veja a análise emocional dos posts: ", font=("Arial" , 10, "bold"))
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

search_button = tk.Button(root, text="Buscar", command=analyze_post)
search_button.pack(pady=10)

# Configuração do widget Text
result_text = tk.Text(root, wrap=tk.WORD, height=20, width=70,)
result_text.pack(pady=10)


# Configuração das tags para formatação
result_text.tag_configure("bold", font=("Helvetica", 9, "bold"))

root.mainloop()
    
