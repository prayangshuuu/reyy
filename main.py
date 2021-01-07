from fbchat import log, Client, Message
from fbchat.models import *
from fbchat.models import ThreadType
from googletrans import Translator
from youtubesearchpython import SearchVideos
from youtubesearchpython import SearchPlaylists
from omdbapi.movie_search import GetMovie
from options import *
from utils import *
from gtts import gTTS
import wikipedia
import sports

class rhekkabx(Client):

    def onMessage(self,
                  mid=None,
                  author_id=None,
                  message=None,
                  message_object=None,
                  thread_id=None,
                  thread_type=ThreadType.GROUP,
                  ts=None,
                  metadata=None,
                  msg=None):

        if (message_object != "NoneType"):
            msgText = message_object.text.lower()

        if (msgText.split()[0] == "/ytvs"):
            ytb = msgText.split(' ', 1)[1]
            res = ytb.replace(" ", "")
            search = SearchVideos(res, offset = 1, mode = "json", max_results = 20)
            reply = search.result()

        elif (msgText.split()[0] == "/ytps"):
            ytb = msgText.split(' ', 1)[1]
            res = ytb.replace(" ", "")
            search = SearchPlaylists(res, offset = 1, mode = "json", max_results = 20)
            reply = search.result()

        elif (msgText == "/ls.c"):
            reply = str("Live Cricket Score By Reyy ROBO \n\n ")+ str(sports.get_sport(sports.CRICKET))

        elif (msgText == "/ls.f"):
            reply = str("Live Football Score By Reyy ROBO \n\n ")+ str(sports.get_sport(sports.FOOTBALL))

        elif (msgText == "/ls.b"):
            reply = str("Live Basketball Score By Reyy ROBO \n\n ")+ str(sports.get_sport(sports.BASKETBALL))

        elif (msgText == "/ls.f"):
            all_matches = sports.all_matches()
            reply = str("Live Cricket Score By Reyy ROBO \n\n ")+ str(all_matches['cricket'])
        elif message_object.text == "remove me" and thread_type == ThreadType.GROUP:
            log.info("{} will be removed from {}".format(author_id, thread_id))
            self.removeUserFromGroup(author_id,  thread_id=thread_id)

        elif (msgText.split()[0] == "/tn"):
            ltext = msgText.split(' ', 1)[1]
            lang = ltext.split()[0]
            mainText = ltext.split(' ', 1)[1]
            translator = Translator()
            translation = translator.translate(mainText ,dest=lang)
            reply = (f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

        elif (msgText.split()[0] == "/wiki"):
            wikiTxt = msgText.split(' ', 1)[1]
            newWiki = wikiTxt.replace(" ", "")
            reply = wikipedia.summary(newWiki)

        elif (msgText.split()[0] == "/read"):
            sep = msgText.split(' ', 1)[1]
            say = sep.replace(" ", "")
            lang = 'en'
            tts = gTTS(text=say, lang=lang)
            tts.save("result.mp3")
            self.sendLocalVoiceClips("result.mp3", thread_id=thread_id, thread_type=thread_type)

        elif (msgText.split()[0] == "/read@bn"):
            sep = msgText.split(' ', 1)[1]
            say = sep.replace(" ", "")
            lang = 'bn'
            tts = gTTS(text=say, lang=lang)
            tts.save("result.mp3")
            self.sendLocalVoiceClips("result.mp3", thread_id=thread_id, thread_type=thread_type)

        elif (msgText.split()[0] == "/read@hi"):
            sep = msgText.split(' ', 1)[1]
            say = sep.replace(" ", "")
            lang = 'hi'
            tts = gTTS(text=say, lang=lang)
            tts.save("result.mp3")
            self.sendLocalVoiceClips("result.mp3", thread_id=thread_id, thread_type=thread_type)

        if "👍" in msgText:
            reply = "মনি লাইক দিলে ঐ আংগুল হাতুরি দিয়া বাড়োই ভাইংগা দেবো"

        if "ব্যাঙাচি" in msgText:
            reply = "ব্যাঙাচি - মে ২০২০ (ভূত) :- https://drive.google.com/file/d/1HcoyV6cSXGxookH1l0vyB5oboRde1cSz/view \n\n ব্যাঙাচি - জুন ২০২০ (কল্পবিজ্ঞান) :- https://drive.google.com/file/d/1PRx4ggpNgGWCC-8KAAps983JLvQa47S7/view \n\n ব্যাঙাচি - জুলাই ২০২০ (প্রাচীন পৃথিবী) :- https://drive.google.com/file/d/1nqio0k7J7Iwid6f5GI6qLHC6hCOnwjI_/view \n\n ব্যাঙাচি - আগস্ট ২০২০ (সৌরজগৎ) :- https://drive.google.com/file/d/1kV7o3qgzG1PjAa-fv98eC5eHRE1cdSU7/view \n\n ব্যাঙাচি - সেপ্টেম্বর ২০২০ (সমুদ্র) :- https://drive.google.com/file/d/1h9op3j6KYznmIyBE_tuWzgYnhVIskpDN/view \n\n"

        elif "🖕" in msgText:
            reply = "তোর ঐ আংগুলে জুতার বারি হারামি । এসব কি ছিঃ মার্কা ইমুজি দেস ভালা হ "

        elif "😡" in msgText:
            reply = "ভাগো তোমার রাগ দেখার সময় নেই"

        elif "😂" in msgText:
            reply = "এতো হাহা ইমুজি দিলে ফাচ টাহা পাবেন?"

        elif "😘" in msgText:
            reply = "নায়েচ ওয়াও থেনকু"

        elif (msgText == "হাই") or (msgText == "হ্যালো") or (msgText == "ভাই") or (msgText == "বাই") or (msgText == "বাঈ"):
            reply = "😇 রে বটের সালাম নেন। যা বলার বলে দেন 😇। না বুঝলে বুঝায় দেন 🙂 বদ্দা কামের কথা না থাকলে মানে মানে বিদায় নেন"

        elif "কি কর?" in msgText:
            reply = " এ রঙ্গের দুনিয়ায় আমার করার কিছু নাই 😎 বইয়া বইয়া মোবাইল টিপি আপনি কি করেন ভাই?"

        elif "বইসা আছি" in msgText or "কিছুনা" in msgText  or "বইয়া আছি" in msgText or "বসে আছি" in msgText or "শুয়ে আছি" in msgText:
            reply = "তো আই কিত্তাম?"

        elif "ফাক" in msgText or "মাদারবোর্ড" in msgText or "মাদারচোদ" in msgText or "বারোচুদা" in msgText or "শিনাল" in msgText or "চুদা" in msgText or "রেন্ধি" in msgText or "খানকি" in msgText or "মাগী" in msgText or "বাড়া" in msgText or "পাক" in msgText or "বাল" in msgText or "ধোন" in msgText:
            reply = "😷 ভাই আপনি এখান থেকে বেড়োন পরিবেশ টা নষ্ট করে দিচ্ছেন 😾 দেখা করেন আপনাকে শুটিয়ে লাল করে দিবো যতসব ফাউল লোকজন 😾 বেয়াদ্দপ কোথাকার"

        elif (msgText == "গান শুনাও") or (msgText == "গান শুনা") or (msgText == "গান শুনাও না প্লিজ ") or (msgText == "গান গাও"):
            reply = "ইয়ো ইয়ো . চারাস গাঞ্জা মেরেকো পেয়ারা । চারাস গাঞ্জা মেরেকো পেয়ারা ফুকু মে সুভা সাম সারাদিন রাত । মাম্মি বোলে মাত কার পাপা বোলে মাত কার । পাতা হে মেইনে কিয়া বোলা? চারাস গাঞ্জা মেরেকো পেয়ার"

        elif (msgText == "আরেকটা গান শুনাও") or (msgText == "আরেকটা গান শুনান") or (msgText == "আরেকটা গান শুনাও না প্লিজ ") or (msgText == "আরেকটা গান শুনাম না প্লিজ "):
            reply = "মুড নাই পরে একদিন"

        elif (msgText == "তুই তো সালা বট তোর আবার মুড ও আছে😂") or (msgText == "তুই তো সালা বট তোর আবার মুড ও আছে😂") or (msgText == "তুই তো বট তোর আবার মুড ও আছে😂") or (msgText == "তুই তো বট তোর আবার মুড ও আছে"):
            reply = "আমার মুড ফিলিং সবই আছে । বিশ্বাস না হইলে কইরেন না কারণ বিশ্বাস করা না করাটা আপনার বিষয়"

        elif (msgText == "ঘুষি দিমু") or (msgText == "মারামারি করবি") or (msgText == "মারামারি করবি?") or (msgText == "লাত্থি মারুম") or (msgText == "এক্কেরে লাত্থি মারুম") or (msgText == "চড় খাবি"):
            reply = "আও দেখে যারা কিসমে কিতনা হে দাম"

        elif (msgText == "কিরে ঘুমাবি না?") or (msgText == "কিরে ঘুমাবি না") or (msgText == "ঘুমাবি না?") or (msgText == "ঘুমাবি না") or (msgText == "ঘুমাবা না?") or (msgText == "ঘুমাবা না") or (  msgText == "ঘুম নেই চোখে?") or (msgText == "ঘুম নেই চোখে") or (msgText == "ঘুমাবি কখন?") or ( msgText == "ঘুমাবি কখন"):
            reply = "ঘুমালে প্রেয়াংশু বাঈ ফাস টাহা কাইট্টা নেবে বেতন থেইক্কা । ঐ ফাচ টাহা কি আপনি দিবেন যদি দেন টাপাটাপ বিকাশ করেন আমি তারপরে ঠাস কইরা ঘুম দেই"

        elif (msgText == "কোন ক্লাসে পড়ো?") or (msgText == "কোন ক্লাসে পড়েন?") or (msgText == "কোন ক্লাসে পড়?") or ( msgText == "কোন ক্লাসে পড়ো"):
            reply = "😀বটের আবার কিসের পড়াশোনা । প্রেয়াংশু বাঈ যা শেখাই তাই শিখি 😎 স্কুলে ভর্তি হমু না পড়াশোনা ভালা লাগে না😇 । অহ হ্যা, তুমি কোন ক্লাসে পড়ো🙂🙂"

        elif (msgText == "hi") or (msgText == "hlw") or (msgText == "hii") or (msgText == "hey") or (msgText == "heyy") :
            reply = "😀 রেক বটের সালাম নেও যা বলার বলে দেও 😎 । না বুঝলে বুঝাইয়ে দেও😇 । কামের কথা শেষ কইরা মানে মানে বিদায় নেও🙂🙂"

        elif (msgText == "কি কর?") or (msgText == "কিতা কর?") or (msgText == "কিতা করো?") or (msgText == "কি করো") or ( msgText == "কিরে করতাছো?") or (msgText == "কিরে করতাছ?") or (msgText == "কিরে করো?") or (msgText == "কিরে কি কর") or (msgText == "কিরে কি করিস?") or (msgText == "কিরে কি করিস") or (msgText == "কি করিস?"):
            reply = " এ রঙ্গের দুনিয়ায় আমার করার কিছু নাই 😎 বইয়া বইয়া মোবাইল টিপি তুমি কি কর ভাই? "


        def sendMsgg():
            if author_id != self.uid:
                self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
        self.markAsDelivered(author_id, thread_id)
        sendMsgg()


client = rhekkabx("niag.nasij.3","123456ABC.")
client.listen()