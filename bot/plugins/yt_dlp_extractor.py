import logging
import os
import time

import yt_dlp
from typing import Dict

from bot.plugins.youtube_audio_extractor import YouTubeAudioExtractorPlugin


class YTDLPExtractorPlugin(YouTubeAudioExtractorPlugin):
    @staticmethod
    def _delete_old_files():
        current_time = time.time()
        for file in os.listdir('tmp'):
            file_path = os.path.join('tmp', file)
            file_age = (current_time - os.path.getatime(file_path))
            if file_age > 60 * 60:
                os.remove(file_path)

    async def execute(self, function_name, helper, **kwargs) -> Dict:
        try:

            link = kwargs['youtube_link']
            ret = yt_dlp.YoutubeDL(params={
                'quiet': True,
                'no_color': True,
                'format': 'bestaudio',
                'socket_timeout': 30,
                'ignore_no_formats_error': True,
                'outtmpl': 'tmp/%(title)s.%(ext)s',
            })
            video = ret.extract_info(link)
            file_path = video['requested_downloads'][0]['filepath']
            self._delete_old_files()
            return {
                'direct_result': {
                    'kind': 'file',
                    'format': 'path',
                    'value': file_path
                }
            }
        except Exception as e:
            logging.warning(f'Failed to extract audio from YouTube video: {str(e)}')
            return {'result': 'Failed to extract audio'}
