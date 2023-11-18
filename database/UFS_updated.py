from app.classd.classdef_updated import Entity_
from main import Kerneltuple_


class UnixFilesystem(Kerneltuple_, Entity_):
    """
    The UnixFilesystem class represents a Unix filesystem.

    Attributes:
    inode (int): The inode of the filesystem.
    pathname (str): The pathname of the filesystem.
    filetype (str): The type of the filesystem.
    permissions (str): The permissions of the filesystem.
    owner (str): The owner of the filesystem.
    group_id (str): The group ID of the filesystem.
    PID (int): The PID of the filesystem.
    unit_file (str): The unit file of the filesystem.
    unit_file_addr (str): The address of the unit file.
    size (int): The size of the filesystem.
    mtime (int): The modification time of the filesystem.
    atime (int): The access time of the filesystem.
    """

    """
    Module description goes here.
    """
    The UnixFilesystem class represents a Unix filesystem.

    Attributes:
    inode (int): The inode of the filesystem.
    pathname (str): The pathname of the filesystem.
    filetype (str): The type of the filesystem.
    permissions (str): The permissions of the filesystem.
    owner (str): The owner of the filesystem.
    group_id (str): The group ID of the filesystem.
    PID (int): The PID of the filesystem.
    unit_file (str): The unit file of the filesystem.
    unit_file_addr (str): The address of the unit file.
    size (int): The size of the filesystem.
    mtime (int): The modification time of the filesystem.
    atime (int): The access time of the filesystem.
    """

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
    """
    The constructor for the UnixFilesystem class.

    :param inode: The inode of the filesystem.
    :type inode: int
    :param pathname: The pathname of the filesystem.
    :type pathname: str
    :param filetype: The type of the filesystem.
    :type filetype: str
    :param permissions: The permissions of the filesystem.
    :type permissions: str
    :param owner: The owner of the filesystem.
    :type owner: str
    :param group_id: The group ID of the filesystem.
    :type group_id: str
    :param PID: The PID of the filesystem.
    :type PID: int
    :param unit_file: The unit file of the filesystem.
    :type unit_file: str
    :param unit_file_addr: The address of the unit file.
    :type unit_file_addr: str
    :param size: The size of the filesystem.
    :type size: int
    :param mtime: The modification time of the filesystem.
    :type mtime: int
    :param atime: The access time of the filesystem.
    :type atime: int
    """
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
            """
            Returns a string representation of the UnixFilesystem object.
        
            Returns:
            str: A string representation of the UnixFilesystem object.
            """
            return f"{self.inode}: {self.pathname}"
            super().__init__(Kerneltuple_, "Unix filesystem")

    def __str__(self):
        """
        Returns a string representation of the UnixFilesystem object.

        :return: A string representation of the UnixFilesystem object.
        :rtype: str
        """
        return f"{self.inode}: {self.pathname}"
        super().__init__(Kerneltuple_, "Unix filesystem")
