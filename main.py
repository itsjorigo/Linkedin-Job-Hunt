# import csv
# import logging
# from linkedin_jobs_scraper import LinkedinScraper
# from linkedin_jobs_scraper.events import Events, EventData, EventMetrics
# from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
# from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, OnSiteOrRemoteFilters

# # Change root logger level (default is WARN)
# logging.basicConfig(level=logging.INFO)


# # Initialize CSV file and write the header row
# csv_file = open('linkedin_jobs.csv', 'w', newline='', encoding='utf-8')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Title', 'Company', 'Company Link', 'Date Posted', 'Job Link', 'Insights', 'Description Length'])


# # Fired once for each successfully processed job
# def on_data(data: EventData):
#     csv_writer.writerow([data.title, data.company, data.company_link, data.date, data.link, data.insights, len(data.description)])
#     print('[ON_DATA]', data.title, data.company, data.company_link, data.date, data.link, data.insights, len(data.description))


# # Fired once for each page (25 jobs)
# def on_metrics(metrics: EventMetrics):
#     print('[ON_METRICS]', str(metrics))


# def on_error(error):
#     print('[ON_ERROR]', error)


# def on_end():
#     print('[ON_END]')
#     csv_file.close()


# scraper = LinkedinScraper(
#     chrome_executable_path='C:\\Users\\User\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe',  # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver)
#     chrome_binary_location=None,  # Custom path to Chrome/Chromium binary (e.g. /foo/bar/chrome-mac/Chromium.app/Contents/MacOS/Chromium)
#     chrome_options=None,  # Custom Chrome options here
#     headless=True,  # Overrides headless mode only if chrome_options is None
#     max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
#     slow_mo=2,  # Slow down the scraper to avoid 'Too many requests 429' errors (in seconds)
#     page_load_timeout=40  # Page load timeout (in seconds)    
# )

# # Add event listeners
# scraper.on(Events.DATA, on_data)
# scraper.on(Events.ERROR, on_error)
# scraper.on(Events.END, on_end)

# queries = [
#     Query(
#         query='software engineering intern',
#         options=QueryOptions(
#             locations=['Sri Lanka'],
#             limit=5  
#         )
#     ),
#     Query(
#         query='software intern',
#         options=QueryOptions(
#             locations=['Sri Lanka'],
#             limit=5  
#         )
#     ),

# ]

# scraper.run(queries)

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
            chrome_executable_path='C:\\Users\\User\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe',  # Update this path or set to None if it's in PATH
            chrome_options=None,  # You can specify custom Chrome options here
            headless=True,  # Can be adjusted based on your needs
            max_workers=1,
            slow_mo=2,
            page_load_timeout=40
        )

        # Add event listeners
        scraper.on(Events.DATA, on_data)
        scraper.on(Events.ERROR, on_error)
        scraper.on(Events.END, on_end)

        # Define your queries
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
            # Add more queries as needed
        ]

        # Run the scraper
        scraper.run(queries)

# Call the scraping function
scrape_to_csv()
