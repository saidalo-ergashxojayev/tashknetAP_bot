class StartTextResult:
    photo_id: str
    text_1: str
    text_2: str

    def __init__(self, photo_id: str, text_1: str, text_2: str):
        self.photo_id = photo_id
        self.text_1 = text_1
        self.text_2 = text_2
