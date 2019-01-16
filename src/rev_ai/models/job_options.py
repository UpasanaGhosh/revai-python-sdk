# -*- coding: utf-8 -*-
"""Job Submit Options Model"""


class JobSubmitOptions:
    def __init__(self,  metadata=None, callback_url=None, skip_diarization=False):
        """
        :param metadata: info to associate with the transcription job
        :param callback_url: callback url to invoke on job completion as a webhook
        :param skip_diarization: should rev.ai skip diaization when transcribing this file
        """
        self.metadata = "" if metadata is None else metadata
        self.callback_url = callback_url
        self.skip_diarization = skip_diarization