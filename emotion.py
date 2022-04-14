from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise...')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print('waiting for your message...')
    recordeaudio=recognizer.listen(source)
    print('done recording')
try:
    print('printing the message..' )
    text = recognizer.recognize_google(recordeaudio,language='en')
    print('your message:{}'.format(text))
except Exception as ex:
    print(ex)
            
sentence=[str(text)]
analyzer = SentimentIntensityAnalyzer()
for i in sentence:
    v = analyzer.polarity_scores(i)
    print(v)