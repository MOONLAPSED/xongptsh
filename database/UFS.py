"""
This module defines the UnixFilesystem class, a subclass of the Iteration class from the main module. 
The UnixFilesystem class represents a Unix filesystem iteration with various attributes such as inode, pathname, filetype, permissions, owner, group_id, PID, unit_file, unit_file_addr, size, mtime, and atime.
"""
from main import Iteration

class UnixFilesystem(Iteration):
    def __init__(self, inode, pathname, filetype, permissions, owner, group_id, PID, unit_file, unit_file_addr, size, mtime, atime):
        super().__init__(inode, "Unix filesystem")
        self.pathname = pathname
        self.filetype = filetype
        self.permissions = permissions
        self.owner = owner
        self.group_id = group_id
        self.size = size
        self.PID = PID
        self.unit_file = unit_file # or name of process or daemon or service
        self.unit_file_addr = unit_file_addr  # or symlink/pointer to process or daemon or service
        self.mtime = mtime
        from main import Iteration
        
        class UnixFilesystem(Iteration):
            def __init__(self, inode, pathname, filetype, permissions, owner, group_id, PID, unit_file, unit_file_addr, size, mtime, atime):
                super().__init__(inode, "Unix filesystem")
                self.pathname = pathname
                self.filetype = filetype
                self.permissions = permissions
                self.owner = owner
                self.group_id = group_id
                self.size = size
                self.PID = PID
                self.unit_file = unit_file # or name of process or daemon or service
                self.unit_file_addr = unit_file_addr  # or symlink/pointer to process or daemon or service
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
                return "{}: {}".format(self.inode, self.pathname)
    def __str__(self):
        return "{}: {}".format(self.inode, self.pathname)