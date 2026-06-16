class Camera:
    def click_photos(self):
        print("Photo clicked")

class Phone :
    def call(self):
        print("Calling")

class SmartPhone(Camera,Phone):
    def browser(self):
        print("browsring internet")

s = SmartPhone()
s.click_photos()
s.call()
s.browser