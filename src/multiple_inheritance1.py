
class DisplayDevice:
    def display_info(self , message):
        return f"Displaying : {message}"

class TouchInterface:
    def handle_touch(self, location):
        return f"Touch detected at : {location}"

class VoiceInterface:
    def handle_voice(self , command):
        return f"voice command received : {command}"

    def power_on(self):
        return "Voice Interface Power On"

class SmartSpeaker(VoiceInterface):
    def display_info(self , song):
        return f"Playing Music {song}"

    def handle_touch(self , location):
        return f"Smart Speaker touch control : {location}"

    def power_on(self):
        return "Smart Speaker Power On and Ready to Listen"

class SmartDisplay(DisplayDevice , TouchInterface):
    def show_video(self , video_title):
        return f"{self.display_info(f"showing Video : {video_title}")}"

    def power_on(self):
        return "Smart display power on and showing howe screen"

class SmartDevice(SmartSpeaker , SmartDisplay):
    def run_app(self , app_name):
        display_output = self.display_info(f"Lunching : {app_name}")
        touch_output = self.handle_voice("center")
        return f"{display_output} | {touch_output}"

if __name__ == "__main__":
    print(SmartDevice.mro())

