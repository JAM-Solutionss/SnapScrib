from dataclasses import dataclass
import cv2
from SnapScrib import video


@dataclass
class Video:
    _file_path: str
    _name: str = None
    video_data: bytes = None
    length: float = 0

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, fpath: str):
        self._file_path = fpath

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name
        if not self._name:
            self._name = self._file_path.split("\\")[-1].split(".")[0]

    def load(self) -> None:
        self.video_data = cv2.VideoCapture(self._file_path)

    def play(self):
        if self.video_data is None:
            self.load()

        while True:
            ret, frame = self.video_data.read()
            if not ret:
                break

            cv2.imshow("Video", frame)

            if cv2.waitKey(25) & 0xFF == ord("q"):
                break


if __name__ == "__main__":
    video_fpath = r"videos\videoplayback.mp4"
    video = Video(video_fpath)
    video.load()
    video.play()
