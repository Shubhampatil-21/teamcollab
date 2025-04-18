import click
import asyncio
import aiohttp
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# API URLs
QUOTE_API = "https://api.quotable.io/random"
WIKI_API_BASE = "https://en.wikipedia.org/api/rest_v1/page/summary"

# Generic fetch function with retry
async def fetch_data(session, url, retries=3, base_delay=1):
 for attempt in range(retries):
     try:
         async with session.get(url, timeout=5, ssl=False) as response:
             response.raise_for_status()
             return await response.json()
     except (aiohttp.ClientError, asyncio.TimeoutError) as e:
         logging.warning(f'Attempt {attempt + 1} failed for {url}: {e}')
         if attempt == retries - 1:
             logging.error(f"All retries failed for {url}")
             return None
         await asyncio.sleep(base_delay * 2 ** attempt)

# Fetch and print Wikipedia summaries (once per topic)
async def fetch_wikipedia_summaries(session, topics):
 for topic in topics:
     wiki_url = f"{WIKI_API_BASE}/{topic}"
     data = await fetch_data(session, wiki_url)
     if data:
         summary = data.get("extract", "No summary found.")
         logging.info(f'Summary for topic "{topic}": "{summary}"')
     else:
         logging.warning(f"Failed to fetch Wikipedia summary for topic: {topic}")

# Fetch and print quote for each email
async def fetch_quotes(session, emails):
 for email in emails:
     logging.info(f"Fetching quote for: {email}")
     data = await fetch_data(session, QUOTE_API)
     if data:
         quote = data.get("content", "No quote found.")
         logging.info(f'Quote for {email}: "{quote}"')
     else:
         logging.warning(f"Could not fetch quote for {email}")

# Main coroutine
async def main(emails, topics):
 async with aiohttp.ClientSession() as session:
     await asyncio.gather(
         fetch_wikipedia_summaries(session, topics),
         fetch_quotes(session, emails)
     )

# CLI
@click.group()
def cli():
 pass

@cli.command()
@click.argument("emails", nargs=-1)
@click.option("--topics", multiple=True, required=True, help="Wikipedia topics to fetch")
def fetch(emails, topics):
 asyncio.run(main(emails, topics))

if __name__ == "__main__":
 cli()
