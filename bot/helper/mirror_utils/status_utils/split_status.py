from time import time
from bot import DOWNLOAD_DIR, LOGGER
from bot.helper.ext_utils.bot_utils import get_readable_file_size, MirrorStatus, get_readable_time, EngineStatus
from bot.helper.ext_utils.fs_utils import get_path_size

class SplitStatus:
    def __init__(self, name, size, gid, listener, message):
        self.__name = name
        self.__gid = gid
        self.__size = size
        self.__listener = listener
        self.__uid = listener.uid
        self.__start_time = time()
        self.message = listener.message
        self.message = message

    def gid(self):
        return self.__gid

    def speed_raw(self):
        return self.processed_bytes() / (time() - self.__start_time)

    def progress_raw(self):
        try:
            return self.processed_bytes() / self.__size * 100
        except:
            return 0

    def progress(self):
        return '0'

    def speed(self):
        return '0'

    def name(self):
        return self.__name

    def size_raw(self):
        return self.__size

    def size(self):
        return get_readable_file_size(self.__size)

    def eta(self):
        return '0s'

    def status(self):
        return MirrorStatus.STATUS_SPLITTING

    def processed_bytes(self):
        return 0

    def download(self):
        return self

    def cancel_download(self):
        LOGGER.info(f'Cancelling Split: {self.__name}')
        if self.__listener.suproc is not None:
            self.__listener.suproc.kill()
        self.__listener.onUploadError('Splitting stopped by user!')

    def eng(self):
        return EngineStatus.STATUS_SPLIT