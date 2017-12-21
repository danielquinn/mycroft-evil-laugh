from os.path import dirname, join
from time import sleep

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.util import play_mp3

__author__ = "Daniel Quinn"

LOGGER = getLogger(__name__)

class EvilLaughSkill(MycroftSkill):

    def __init__(self):
        LOGGER.info("EvilLaugh: INIT")
        super(EvilLaughSkill, self).__init__(name="EvilLaughSkill")

    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        LOGGER.info("EvilLaugh: INIT2")
        self.load_data_files(dirname(__file__))
        evil_laugh_intent = IntentBuilder("EvilLaughIntent").require("EvilLaughKeyword").build()
        self.register_intent(evil_laugh_intent, self.handle_evil_laugh_intent)

    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.
    def handle_evil_laugh_intent(self, message):
        LOGGER.info("Executing")
        self.enclosure.reset()
        self.process = play_mp3(join(dirname(__file__), "mp3", "laugh.mp3"))
        self.enclosure.eyes_brightness(10)
        self.enclosure.eyes_color(r=124, g=114, b=213)
        sleep(1)
        self.enclosure.eyes_color(r=132, g=53, b=142)
        sleep(1)
        self.enclosure.eyes_brightness(20)
        self.enclosure.eyes_color(r=142, g=53, b=87)
        sleep(1)
        self.enclosure.eyes_brightness(30)
        self.enclosure.eyes_color(r=150, g=0, b=0)  # Red
        sleep(1)
        self.enclosure.eyes_narrow()
        sleep(3)
        self.process.wait()
        self.enclosure.reset()
        self.enclosure.eyes_blink("b")
        self.enclosure.eyes_color(r=72, g=150, b=212)  # Blue

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, the method just contains the keyword "pass", which
    # does nothing.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return EvilLaughSkill()

