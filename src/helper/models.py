class StartTextResult:
    photo_ids: list[str]
    text_1: str
    text_2: str

    def __init__(self, photo_ids: list[str], text_1: str, text_2: str):
        self.photo_ids = photo_ids
        self.text_1 = text_1
        self.text_2 = text_2
