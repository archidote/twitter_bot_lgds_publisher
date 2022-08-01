from sympy import quo
from controller import * 
from meme_publisher import * 
from quote_publisher import * 

schedule.every(1).minutes.do(lambda: img_publisher())
schedule.every(2).minutes.do(lambda: quote_publisher())

while 1:
    schedule.run_pending()
    time.sleep(1)

