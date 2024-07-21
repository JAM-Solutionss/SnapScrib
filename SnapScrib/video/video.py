from dataclasses import dataclass
from moviepy.editor import VideoFileClip

from SnapScrib import video


@dataclass
class Video:
    file_path: str
    name: str = None
    video_data: bytes = None
    audio_data: bytes = None
    length: float = 0

    def load_video(self) -> None:
        self.video_data = VideoFileClip(self.file_path)

    def load_audio(self) -> None:
        if self.video_data:
            self.audio_data = self.video_data.audio
        else:
            self.load_video()
            self.audio_data = self.video_data.audio


if __name__ == "__main__":
    