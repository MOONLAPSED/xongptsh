""" This module defines the UnixFilesystem class, a subclass of the Iteration class from the main module. 
    This class represents a Unix filesystem iteration with various attributes.
    Attributes:
    - inode (str): The inode of the filesystem.
    - pathname (str): The pathname of the filesystem.
    - filetype (str): The filetype of the filesystem.
    - permissions (str): The permissions of the filesystem.
    - owner (str): The owner of the filesystem.
    - group_id (str): The group_id of the filesystem.
    - PID (str): The PID of the filesystem.
    - unit_file (str): The unit_file of the filesystem.
    - unit_file_addr (str): The unit_file_addr of the filesystem.
    - size (str): The size of the filesystem.
    - mtime (str): The mtime of the filesystem.
    - atime (str): The atime of the filesystem.
    """
import logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG)
from main import Iteration


class UnixFilesystem(Iteration):
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
        super().__init__(inode, "Unix filesystem")
        self.pathname = pathname
        self.filetype = filetype
        self.permissions = permissions
        self.owner = owner
        self.group_id = group_id
        self.size = size
        self.PID = PID
        self.unit_file = unit_file  # or name of process or daemon or service
        self.unit_file_addr = (
            unit_file_addr  # or symlink/pointer to process or daemon or service
        )
        self.mtime = mtime
        self.atime = atime

    def __str__(self):
from main import Iteration


class UnixFilesystem(Iteration):
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
        super().__init__(inode, "Unix filesystem")
        self.pathname = pathname
        self.filetype = filetype
        self.permissions = permissions
        self.owner = owner
        self.group_id = group_id
        self.size = size
        self.PID = PID
        self.unit_file = unit_file  # or name of process or daemon or service
        self.unit_file_addr = (
            unit_file_addr  # or symlink/pointer to process or daemon or service
        )
        self.mtime = mtime
        self.atime = atime

    def __str__(self):
        """
        This method returns a string representation of the UnixFilesystem object.

        Parameters:
        None

        Returns:
        str: A string representation of the UnixFilesystem object in the format "inode: pathname".
        """
        logger = logging.getLogger(__name__)
        logger.debug("Debug information: {}".format(self.inode))
        return "{}: {}".format(self.inode, self.pathname)
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
        super().__init__(inode, "Unix filesystem")
        self.pathname = pathname
        self.filetype = filetype
        self.permissions = permissions
        self.owner = owner
        self.group_id = group_id
        self.size = size
        self.PID = PID
        self.unit_file = unit_file  # or name of process or daemon or service
        self.unit_file_addr = (
            unit_file_addr  # or symlink/pointer to process or daemon or service
        )
        self.mtime = mtime
        self.atime = atime
        """
        This method returns a string representation of the UnixFilesystem object.

        Parameters:
        None

        Returns:
        str: A string representation of the UnixFilesystem object in the format "inode: pathname".
        """
        logger = logging.getLogger(__name__)
        logger.debug("Debug information: {}".format(self.inode))
        return "{}: {}".format(self.inode, self.pathname)
        Parameters:
        None

        Returns:
        str: A string representation of the UnixFilesystem object in the format "inode: pathname".
        """
        return "{}: {}".format(self.inode, self.pathname)
