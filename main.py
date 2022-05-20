import json
import random
import time
import tweepy
#استبدل الاكس بالمفاتيح الخاصة بحسابك
consumer_key = 'R0KVn8V2Hdv5e1hSaiMM2QOI6'
consumer_secret = 'ZjrHNt8u5tEGotcqBzFVV1w5VhPlNuYArRjc6NlGT2cSlGBgDi'
access_token= "1527295383432335360-mkpUXXBBZG3ZGTrU330MwMs9IpDIFc"
access_secret = "QLDCrJ1wLClW9vaWIelNIaULAsN5ONTuQdrHORaLXaJeb"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def main():
    with open("azkar.json", "r") as read_file:
        data = json.load(read_file)  
    random_azkar = random.choice(data)
    category = random_azkar["category"]
    zekr = random_azkar["zekr"]
    l = len(zekr)
    print(l)
#في حالة ان الذكر اكثر من ١٦٠ حرف  يتم الاختيار مره اخرى لان تويتر لا يقبل اكثر من ١٨٠ حرف
    while l > 160:
        random_azkar = random.choice(data)
        category = random_azkar["category"]
        zekr = random_azkar["zekr"]
        l = len(zekr)
        print(l)
    print("التصنيف: "+category+"\nالذكر: "+zekr+"\n")
    #نشر الذكر في تويتر
    api.update_status("التصنيف: "+category+"\nالذكر: "+zekr+"\n#اذكار")
    print("Tweeted")
   
#تكرار مع انتظار ١٨٠٠ ثانية يساوي نصف ساعة
while True:
    main()
    time.sleep(1800)
