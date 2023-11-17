import logging
from main import Kerneltuple_

logging.basicConfig(filename='debug.log', level=logging.DEBUG)

class UnixFilesystem(Kerneltuple_):
    def __init__(
        self,
        inode,
        pathname,
        filetype,
        permissions,
        owner,
        group_id,
        PID,
        unit_file,
        unit_file_addr,
        size,
        mtime,
        atime,
    ):
        super().__init__(Kerneltuple_, "Unix filesystem")
        self.inode = inode
        self.pathname = pathname
        self.filetype = filetype
        self.permissions = permissions
        self.owner = owner
        self.group_id = group_id
        self.PID = PID
        self.unit_file = unit_file
        self.unit_file_addr = unit_file_addr
        self.size = size
        self.mtime = mtime
        self.atime = atime

    def __str__(self):
        return f"{self.inode}: {self.pathname}"
