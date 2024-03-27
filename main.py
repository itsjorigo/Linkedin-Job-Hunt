import csv
import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData, EventMetrics
from linkedin_jobs_scraper.query import Query, QueryOptions

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a function to handle scraping and writing to CSV
def scrape_to_csv():
    # Initialize CSV file within a context manager to ensure proper closing
    with open('linkedin_jobs.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Title', 'Company', 'Company Link', 'Date Posted', 'Job Link', 'Insights', 'Description Length'])

        def on_data(data: EventData):
            csv_writer.writerow([data.title, data.company, data.company_link, data.date, data.link, data.insights, len(data.description)])
            print('[ON_DATA]', data.title, data.company, data.company_link, data.date, data.link, data.insights, len(data.description))

        def on_error(error):
            print('[ON_ERROR]', error)

        def on_end():
            print('[ON_END]')

        # Initialize the scraper
        scraper = LinkedinScraper(
            chrome_executable_path=None,
            chrome_options=None,
            headless=True,
            max_workers=1,
            slow_mo=2,
            page_load_timeout=40
        )

        # Add event listeners
        scraper.on(Events.DATA, on_data)
        scraper.on(Events.ERROR, on_error)
        scraper.on(Events.END, on_end)

        queries = [
            Query(
                query='software engineering intern',
                options=QueryOptions(
                    locations=['Sri Lanka'],
                    limit=5
                )
            ),
            Query(
                query='engineering intern',
                options=QueryOptions(
                    locations=['Sri Lanka'],
                    limit=5  
                )
            ),
            Query(
                query='tech intern',
                options=QueryOptions(
                    locations=['Sri Lanka'],
                    limit=5  
                )
            ),
            Query(
                query='IT intern',
                options=QueryOptions(
                    locations=['Sri Lanka'],
                    limit=5  
                )
            ),

            Query(
                query='software engineer intern',
                options=QueryOptions(
                    locations=['Colombo'], 
                    limit=5
                )
            ),
            Query(
                query='developer intern',
                options=QueryOptions(
                    locations=['Sri Lanka'],
                    limit=5  
                )
            )
        ]

        scraper.run(queries)

# Call the scraping function
scrape_to_csv()
