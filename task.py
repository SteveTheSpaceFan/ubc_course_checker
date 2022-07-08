import smtplib
import time
from email.message import EmailMessage
from urllib.parse import parse_qs
from urllib.parse import urlparse

import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By


class Task:
    def __init__(self, url, max_sleep_time, recipients):
        self.url = url
        self.max_sleep_time = max_sleep_time
        self.min_sleep_time = self.max_sleep_time / 4
        self.recipients = recipients
        self.finished = False
        self.checked_times = 0
        self.course_name = parse_qs(urlparse(url).query)['dept'][0] + " " + parse_qs(urlparse(url).query)['course'][0]

    def check(self):
        browser = webdriver.Chrome()
        browser.get(self.url)
        all_rows = browser.find_elements(By.TAG_NAME, 'tr')  # Find all the all_rows

        for row in all_rows:
            row_class_name = row.get_attribute("class")
            if row_class_name[:7] == "section":
                cols = row.find_elements(By.TAG_NAME, 'td')
                status = cols[0].text
                course_name = cols[1].text
                row_type = cols[2].text
                if status == "" and row_type == "Lecture":
                    self.notify(course_name)
                    self.finished = True

    def notify(self, course_name):
        sender_email = "ultradumbautobot@gmail.com"
        rec_email = self.recipients
        password = "tvveshhlysgmeqrb"

        message = self.url

        em = EmailMessage()
        em['From'] = sender_email
        em['To'] = rec_email
        em['Subject'] = course_name + " is now available!"
        em.set_content(message)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, em.as_string())
        print("Found course " + course_name)

    def start(self):
        print("Started task: " + self.url)
        while not self.finished:
            self.check()
            self.checked_times += 1
            print(self.course_name + " checked " + str(self.checked_times) + " times")
            time.sleep(self.min_sleep_time + np.random.rand() * (self.max_sleep_time - self.min_sleep_time))
        print("Finished task: " + self.url)
