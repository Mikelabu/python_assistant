import wx


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
                            label="Hello I am PyDa Digital Assistant. How can I help you?")
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
        print("It worked!")


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
