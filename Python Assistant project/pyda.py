import wx
import wolframalpha
import wikipedia
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, What would you like to know?")
engine.runAndWait()


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
                          pos=wx.DefaultPosition, size=wx.Size(450, 100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                          wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="PyDa")
        panel = wx.Panel(self)
        # box size
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        # label
        lbl = wx.StaticText(panel,
                            label="Hello how can I help you?")
        # create box for question
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(
            panel, style=wx.TE_PROCESS_ENTER, size=(400, 30))
        # focus text
        self.txt.SetFocus()

        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

        # define on enter function

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            # wolframalpha
            app_id = "52EE7V-6X76VJVT2K"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            # .text will ensure text amswers only
            answer = next(res.results).text
            print(answer)
            engine = pyttsx3.init()
            engine.say("The Answer Is" + answer)
            engine.runAndWait()
            #pyttsx.synth("The answer is " + answer)

        except:
            # wikipedia
            # this can be handled better-- needs to be changed
            # when searching for who is thomas eddison the result comes back with someone that has worked with eddison.
            input = input.split(' ')
            input = ' '.join(input[2:])
            wikipedia.set_lang("en")
            answer = wikipedia.summary(input, sentences=2)
            print(answer)
            engine = pyttsx3.init()
            engine.say("The Answer Is" + answer)
            engine.runAndWait()


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
