# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
from scrapy.exceptions import NotConfigured

class TerlarisPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        try:
            self.con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                db='bhinneka'
            )
            self.cur = self.con.cursor()
        except mysql.connector.Error as err:
            raise NotConfigured(f"Error connecting to MySql : {err}")

    def create_table(self):

        try:
            self.cur.execute(
                """CREATE TABLE IF NOT EXIST terlaris (
                    nama TEXT,
                    harga INT,
                    cicilan TEXT,
                    link TEXT
                    )"""
            )
        except mysql.connector.Error as err:
            raise NotConfigured(f"Error creating table : {err}")

    def process_item(self, item, spider):
        try:
            self.store_db(item)
            print("pipline : " + item['nama'])
        except mysql.connector.Error as err
            spider.log(f"Error storing item in database : {err}")
        return item

    def store_db(self):
        self.cur.execute(
            """INSERT INTO terlaris (nama, harga, cicilan, link)
                VALUES (%S, %S, %S, %S)
            """, (item['nama'], item['harga'], item['cicilan'], item['link'])
        )
        self.con.commit()

    def close_spider(self):
        try:
            self.con.close()
        except mysql.connector.Error as err
            spider.log(f'Error closing database connection : {err}')