from kivy.app import App
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.loader import Loader
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.stacklayout import  StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics.context_instructions import Color
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.config import Config




Config.set('kivy','window_icon','dfb.png')

class BoxLayout1(BoxLayout):
     text1 = StringProperty("hello")
     text2 = StringProperty("hello")
     img1 = StringProperty("dd.jpg")
     img2 = StringProperty("dd.jpg")
     demo = StringProperty("EDD")
     hd = StringProperty("***b***")
     preview = StringProperty("6/27/2021")
     a1 = ""
     a2 = ""
     am1 = "a1.jpg"
     am2 = "a2.jpg"
     ah = ""

     b1 = ""
     b2 = ""
     bm1 = "b1.jpg"
     bm2 = "b2.jpg"
     bh = ""

     c1 = ""
     c2 = ""
     cm1 = "c1.jpg"
     cm2 = "c2.jpg"
     ch = ""

     d1 = "[b] YAHOO NO BE CRIME NA THE SMARTNESS IN ME I DEY PROVE. I WOULD RATHER USE MY SMART WAY THAN STEALING OR FALSING. they don chop us back in the days, its time for us to chop them too. 'WHAT GOES AROUND TURNS AROUND'. today is pain tomorrow is power. ONLY WHEN YOU GET RICH YOU BECOME LORD AND POWERFUL. do not mistake my kindness for weakness, the beast in me is only sleeping not dead. IF YOU THINK SAY YOU DEY LOOSE YOUR DATA REMEMBER SAY TREE LOOSES LEAVES EVERYDAY BUT STILL STAND ALONE FOR A BETTER DAY. the only thing that can stop YOU is YOU. person wey popular and got rich was once in your stage and never give up. THEY NO GO SUPPORT YOU BUT WHEN YOU GAT THE MONEY THEM GO FEEL AND HAIL YOU. take the risk oga, if you win you be HAPPY if you loose you will gain lot of lesson, OGA THE MORE YOU REASON....DETERMINE THE QUALITY OF YOUR LIFE. better live life on your own term. FOCUS ON THE GOAL NOT WHAT PEOPLE SAYS. doubting would definitely make you fail. [/b]"
     d2 = "[color=#ff0000](1) YOU NO LOOSE DATA ON CLIENT YOU ONLY PAID FOR LESSON\n \n(2) SOMETIMES IT IS BETTER TO JUST REMAIN SILENT AND SMILE.\n \n(3) IT IS GOING TO HAPPEN BECAUSE I WANT IT TO HAPPEN\n \n(4) THE BIG LESSON IN LIFE IS NEVER TO BE SCARED OF ANYONE OR ANYTHING. \n \n(5) SET A GOAL SO BIG THAT YOU CANT NOT ACHIEVE IT UNTILL GROWN INTO THE PERSON WHO CAN. \n \n(6) NO MATTER THE SITUATION NEVER LET YOUR EMOTIONS OVERPOWER YOUR INTLLIGENCE\n\n(7) DO NOT GIVE YOUR PAST TO DETERMINE YOUR FUTURE\n\n(8) FROM LITTLE SEED GROW MIGHTY TREES\n\n(9) THE HARDEST BATTLE IS BETWEEN WHAR YOU KNOW IN YOUR HEAD AND WHAT YOU FEL IN YOUR HEART\n\n(10) TALK LESS SMILE MUCH [/color]"
     dm1 = "d1.jpg"
     dm2 = "d2.jpg"
     dh = "[color=#ff0000](1) RISK IS THE DOWNPAYMENT ON SUCCESS\n\n(2) SMILE, IT DESTROYS YOUR ENEMIES\n\n(3) MY GOAL IS NOT TO BE BETTER THAN ANYONE BUT BETTER THAN RECENTLY THAT I AM\n\n(4) CHOOSE THOSE WHO CHOOSE YOU\n\n(5) THE CLIMB IS HIGH BUT THE VIEW IS TOTALLY WORTH IT\n\n(6) MOTIVATE YOURSELF STOP LISTENING TO THOSE THAT ONLY SEES YOUR MISTAKE\n\n(7) DEFICULTS WAY WILL SURELY LEADS TO SUCCESS\n\n(8) IF YOU CAN NOT DO GREAT THINGS DO SMALL THINGS IN SMALL WAYS\n\n(9) WHEN LIFE PUT YOU IN TOUGH SITUATION DONT SAY 'why me' SAY 'try me' \n\n(10) SILENCE IS A SOURCE OF GREAT STRENGTH.[/color]"

     def a(self, a):
          self.demo = a.text
          self.preview = "6/27/2021"
          self.text1 = self.a1
          self.text2 = self.a2
          self.img1 = self.am1
          self.img2 = self.am2
          self.hd = self.ah
     
     def b(self, b):
          self.demo = b.text
          self.preview = "6/27/2021"
          self.text1 = self.b1
          self.text2 = self.b2
          self.img1 = self.bm1
          self.img2 = self.bm2
          self.hd = self.bh
     
     def c(self, c):
          self.demo = c.text
          self.preview = "6/27/2021"
          self.text1 = self.c1
          self.text2 = self.c2
          self.img1 = self.cm1
          self.img2 = self.cm2
          self.hd = self.ch

     def d(self, d):
          self.demo = d.text
          self.preview = "6/27/2021"
          self.text1 = self.d1
          self.text2 = self.d2
          self.img1 = self.dm1
          self.img2 = self.dm2
          self.hd = self.dh
    
     def Goto(self, a):
          self.ids.down.remove_widget(self.ids.options)
          if a.state == "normal":
             self.ids.down.remove_widget(self.ids.options)
          else:
             self.ids.down.add_widget(self.ids.options)

class MainWidget(Widget):
    pass
     
class GformatApp(App):
     pass
    
GformatApp().run()