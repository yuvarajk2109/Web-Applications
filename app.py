import wx

class ArithmeticApp(wx.Frame):
    def __init__(self, parent, title):
        super(ArithmeticApp, self).__init__(parent, title=title, size=(400, 300))
        
        panel = wx.Panel(self)

        wx.StaticText(panel, label="Basic Calculator", pos=(90, 20))
        
        wx.StaticText(panel, label="First Number:", pos=(30, 60))
        self.num1_text = wx.TextCtrl(panel, pos=(180, 55), size=(150, -1))
        
        wx.StaticText(panel, label="Second Number:", pos=(30, 100))
        self.num2_text = wx.TextCtrl(panel, pos=(180, 95), size=(150, -1))


        wx.StaticText(panel, label="Result:", pos=(30, 140))
        self.result_text = wx.TextCtrl(panel, pos=(180, 135), size=(150, -1), style=wx.TE_READONLY)
        
        btn_add = wx.Button(panel, label="+", pos=(50, 190))
        btn_sub = wx.Button(panel, label="-", pos=(110, 190))
        btn_mul = wx.Button(panel, label="×", pos=(170, 190))
        btn_div = wx.Button(panel, label="÷", pos=(230, 190))
        btn_mod = wx.Button(panel, label="%", pos=(290, 190))
        
        btn_add.Bind(wx.EVT_BUTTON, self.on_add)
        btn_sub.Bind(wx.EVT_BUTTON, self.on_subtract)
        btn_mul.Bind(wx.EVT_BUTTON, self.on_multiply)
        btn_div.Bind(wx.EVT_BUTTON, self.on_divide)
        btn_mod.Bind(wx.EVT_BUTTON, self.on_modulus)
        
        self.Centre()
        self.Show()
    
    def get_inputs(self):
        try:
            num1 = float(self.num1_text.GetValue())
            num2 = float(self.num2_text.GetValue())
            return num1, num2
        except ValueError:
            wx.MessageBox("Please enter valid numbers!", "Error", wx.OK | wx.ICON_ERROR)
            return None, None

    def on_add(self, event):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            self.result_text.SetValue(str(num1 + num2))

    def on_subtract(self, event):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            self.result_text.SetValue(str(num1 - num2))

    def on_multiply(self, event):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            self.result_text.SetValue(str(num1 * num2))

    def on_divide(self, event):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            if num2 == 0:
                wx.MessageBox("Division by zero is not allowed!", "Error", wx.OK | wx.ICON_ERROR)
                return
            self.result_text.SetValue(str(num1 / num2))

    def on_modulus(self, event):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            if num2 == 0:
                wx.MessageBox("Modulus by zero is not allowed!", "Error", wx.OK | wx.ICON_ERROR)
                return
            self.result_text.SetValue(str(num1 % num2))


if __name__ == "__main__":
    app = wx.App()
    ArithmeticApp(None, title="Arithmetic Operations")
    app.MainLoop()