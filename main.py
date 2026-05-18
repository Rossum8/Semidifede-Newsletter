import google.generativeai as genai
import os
import json
import feedparser
import glob
from datetime import datetime

# Configure Gemini API using environment variables (this makes it easy to switch Google accounts later)
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not found. Please set it.")

genai.configure(api_key=api_key)

def read_planner():
    try:
        with open('planner.md', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "No planner.md found for this week."

def read_raw_files():
    raw_content = ""
    for filepath in glob.glob('raw/*'):
        if filepath.endswith('.md') or filepath.endswith('.txt'):
            with open(filepath, 'r', encoding='utf-8') as f:
                raw_content += f"\n--- {filepath} ---\n" + f.read()
    if not raw_content:
        raw_content = "No raw notes provided this week."
    return raw_content

def fetch_rss_feeds():
    try:
        with open('sources.json', 'r', encoding='utf-8') as f:
            sources = json.load(f)
    except FileNotFoundError:
        return "No sources.json found."
    
    feed_content = ""
    for url in sources.get('rss_feeds', []):
        feed = feedparser.parse(url)
        feed_title = feed.feed.title if hasattr(feed.feed, 'title') else url
        feed_content += f"\n--- Feed: {feed_title} ---\n"
        for entry in feed.entries[:3]: # Get top 3 entries per feed to avoid overloading the prompt
            feed_content += f"- {entry.title}: {entry.link}\n"
            if hasattr(entry, 'summary'):
                # Basic cleanup of summary text (if it contains HTML, a proper parser might be needed, but this is fine for an LLM)
                feed_content += f"  Summary: {entry.summary[:300]}...\n"
    
    if not feed_content:
        feed_content = "No recent RSS feed articles found."
    return feed_content

def generate_newsletter(planner, raw, feeds):
    # We use gemini-pro for high quality generation
    model = genai.GenerativeModel('models/gemini-2.5-flash')
    
    prompt = f"""
    You are the "Semidifede Editor", creating a weekly Catholic newsletter in italian.
    
    Here is the Planner for this week:
    {planner}
    
    Here are the Raw Notes/Excerpts provided:
    {raw}
    
    Here are the latest articles from trusted Catholic sources:
    {feeds}
    
    Istruzioni: 
1. Adatta il contenuto raccolto al planner.
 2. Scrivi una newsletter in Markdown ben formattata, che inizia con "Ciao" e parla rivolta alla seconda persona singolare. 
3. Includi un titolo accattivante scritto con le iniziali in minuscolo (esclusa l'iniziale della prima parola), una breve introduzione, sezioni basate sul planner e una riflessione conclusiva. 
4. Cerca su "https://www.mogliemammepervocazione.com/author/rossana/" articoli inerenti al planner da cui prendere spunto. 
5. Se il planner presenta delle lacune, genera autonomamente contenuti cattolici pertinenti o utilizza le ultime notizie/blog per colmarle. 
6. Assicurati che il tono di voce sia caldo, colloquiale, personale e coinvolgente per un pubblico cattolico quasi esclusivamente femminile di catechiste e genitori cattolici. 
7. Inserisci sempre la proposta di una risorsa inerente al tema del planner presente su "https://semi-di-fede.mailerpage.io/risorse" (per entrare in questo sito scrivi come password la parola quaresima), proponendo di fare il download. 
8. Concludi la newsletter con un ringraziamento e un arrivederci e firma con il nome Rossana
8. Pubblica SOLO il contenuto in Markdown per la newsletter.  

    """
    
    print("Sending content to Gemini API...")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("Reading planner...")
    planner_text = read_planner()
    
    print("Reading raw files...")
    raw_text = read_raw_files()
    
    print("Fetching RSS feeds...")
    feed_text = fetch_rss_feeds()
    
    print("Generating newsletter draft...")
    newsletter_draft = generate_newsletter(planner_text, raw_text, feed_text)
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"drafts/issue_{date_str}.md"
    
    # Ensure drafts directory exists
    os.makedirs('drafts', exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(newsletter_draft)
    
    print(f"Draft successfully created at {filename}")
