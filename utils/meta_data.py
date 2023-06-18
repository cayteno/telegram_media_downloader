"""Meta data for download filter"""


class ReString:
    """for re match"""

    def __init__(self, re_string: str):
        self.re_string = re_string


class NoneObj:
    """for None obj to match"""

    def __init__(self):
        pass


# pylint: disable=R0902
# pylint: disable=R0913
class MetaData:
    """
    * `message_date` : - Date the message was sent
    * like: message_date > 2022.03.04 && message_date < 2022.03.08
    * `message_id` : - Message 's id
    * `media_file_size` : - File size
    * `media_width` : - Include photo and video
    * `media_height` : - Include photo and video
    * `media_file_name` : - file name
    * `message_caption` : - message_caption
    * `message_duration` : - message_duration
    """

    AVAILABLE_MEDIA = (
        "audio",
        "document",
        "photo",
        "sticker",
        "animation",
        "video",
        "voice",
        "video_note",
        "new_chat_photo",
    )

    def __init__(
        self,
        message_date: str = None,
        message_id: int = None,
        message_caption: str = None,
        media_file_size: int = None,
        media_width: int = None,
        media_height: int = None,
        media_file_name: str = None,
        media_duration: int = None,
        media_type: str = None,
        file_extension: str = None,
    ):
        self.message_date = message_date
        self.message_id = message_id
        self.message_caption = message_caption
        self.media_file_size = media_file_size
        self.media_width = media_width
        self.media_height = media_height
        self.media_file_name = media_file_name
        self.media_duration = media_duration
        self.media_type = media_type
        self.file_extension = file_extension

    def data(self) -> dict:
        """Meta map"""
        return {
            "message_date": self.message_date,
            "message_id": self.message_id,
            "message_caption": self.message_caption,
            "media_file_size": self.media_file_size,
            "media_width": self.media_width,
            "media_height": self.media_height,
            "media_file_name": self.media_file_name,
            "media_duration": self.media_duration,
            # small
            "id": self.message_id,
            "caption": self.message_caption,
            "file_size": self.media_file_size,
            "file_name": self.media_file_name,
            "media_type": self.media_type,
            "file_extension": self.file_extension,
        }
