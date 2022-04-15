from os import system as RunCMD

class AudioVideoJoiner():
    def __init__():
        pass

    def JoinAudioAndVideo(self,audio:str,video:str,output:str) -> int:
        return RunCMD(f'ffmpeg -i "{video}" -i "{audio}" -c:v copy -c:a aac "{output}"')