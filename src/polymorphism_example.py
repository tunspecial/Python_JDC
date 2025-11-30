from typing import Protocol

class GameMode(Protocol):
    def play_mode(self , playerone:str , playertwo:str) -> None:
        ...

class Game:
    def __init__(self , playing:GameMode):
        self.playing = playing

    def playing(self , playerone , playertwo):
        print("Game Starting!!!")
        self.playing.play_mode(playerone , playertwo)
        print("Game Ending!!!")

class OfflineMode(GameMode):
    def play_mode(self , playerone:str , playertwo:str) -> None:
        print(f"{playerone} and {playertwo} is game playing with offline mode!!!")

class OnlineMode(GameMode):
    def play_mode(self , playerone:str , playertwo:str) -> None:
        print(f"{playerone} and {playertwo} is game playing with online mode!!!")

if __name__ == "__main__":
    game = OfflineMode()
    game.play_mode("Mg Mg" , "Ko Ko")

    game = OnlineMode()
    game.play_mode("Zaw Zaw" , "Ma Ma")
