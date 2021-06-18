# abuseipdbFunc
Python function to scrape abuseipdb.com without API key

Sample Output (redacted):

```$ python main.py 1xx.xxx.xxx.xxx
{'findings': {0: {'category': {0: {'category_name': 'Bad Web Bot',
                                   'category_value': 'Webpage scraping (for '
                                                     'email addresses, '
                                                     'content, etc) and '
                                                     'crawlers that do not '
                                                     'honor robots.txt. '
                                                     'Excessive requests and '
                                                     'user agent spoofing can '
                                                     'also be reported '
                                                     'here. '}},
                  'reporter_comment': '',
                  'reporter_country': 'Switzerland',
                  'reporter_country_code': 'ch',
                  'reporter_date': '20xx-xx-xxT00:13:10-04:00',
                  'reporter_name': ' XXXXX '},
              1: {'category': {0: {'category_name': 'Hacking',
                                   'category_value': ''},
                               1: {'category_name': 'Brute-Force',
                                   'category_value': 'Credential brute-force '
                                                     'attacks on webpage '
                                                     'logins and services like '
                                                     'SSH, FTP, SIP, SMTP, '
                                                     'RDP, etc. This category '
                                                     'is seperate from DDoS '
                                                     'attacks. '},
                               2: {'category_name': 'Web App Attack',
                                   'category_value': 'Attempts to probe for or '
                                                     'exploit installed web '
                                                     'applications such as a '
                                                     'CMS like '
                                                     'WordPress/Drupal, '
                                                     'e-commerce solutions, '
                                                     'forum software, '
                                                     'phpMyAdmin and various '
                                                     'other software '
                                                     'plugins/solutions.'}},
                  'reporter_comment': 'Trolling for vulnerabilities using '
                                      '/.git/HEAD. Auto blocked and Banned.',
                  'reporter_country': 'Portugal',
                  'reporter_country_code': 'pt',
                  'reporter_date': '20xx-xx-xxT00:13:10-04:00',
                  'reporter_name': ' XXXXX '}},
 'infos': {'ip_address': '1xx.xxx.xxx.xxx',
           'ip_country_code': 'id',
           'ip_country_name': 'Indonesia'}}```
