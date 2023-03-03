

    """
    FilmReel is a list of all past states of an object.
    Call capture_frame on every frame, even if not recording.
    It will capture None for every frame that capture_frame is called (for sync/timekeeping purposes)
    Future plans for this class:
    1) delta recording mode, i.e. frames only track differences from previous frame, 
       rather than copy the entire object each frame (which is bad for memory)
    2) offloading of oldest/most distant frames onto external files,
       in order to save memory when dealing with particularly long timelines or large matrices
    """
    class FilmReel(list):
        def __init__(self, parent, auto_start_recording: bool = False):
            super().__init__([])
            self.__parent = parent
            self.__recording = auto_start_recording

        def start_recording(self):
            self.__recording = True

        def stop_recording(self):
            self.__recording = False

        def capture_frame(self, frame=None):
            # frame=None by default so that FilmReel still keeps time while

            if self.__recording:
                self.append(frame)
            else:
                raise Exception("This matrix's timekeeper is not set to record.")



def main():
    pass

if __name__ == "__main__":
    main()
