import sys, os, logging, requests, sqlite3, subprocess, bs4, re, threading, argparse, asyncio, datetime, http.server, json, socketserver
from app.classd.classdef import Entity, Kerneltuple_


# ==========tests=================
# Define test cases for the Entity class
entity_test_cases = [
    {
        "name": "Entity 1",
        "description": "Description 1"
    },
    {
        "name": "Entity 2",
        "description": "Description 2"
    }
]
# These test cases are used to test the Entity class by creating instances of the class and printing their attributes.
for test_case in entity_test_cases:
    entity = Entity(test_case["name"], test_case["description"])
    import sys, os, logging, requests, sqlite3, subprocess, bs4, re, threading, argparse, asyncio, datetime, http.server, json, socketserver
    from app.classd.classdef import Entity, Kerneltuple_
    
    
    # ==========tests=================
    # Define test cases for the Entity class
    entity_test_cases = [
        {
            "name": "Entity 1",
            "description": "Description 1"
        },
        {
            "name": "Entity 2",
            "description": "Description 2"
        }
    ]
    # These test cases are used to test the Entity class by creating instances of the class and printing their attributes.
    for test_case in entity_test_cases:
        entity = Entity(test_case["name"], test_case["description"])
        print(entity.name)
        print(entity.description)
    kernel_tuple_test_cases = [
        {
            'inode': 'some_inode_value',
            'pathname': 'some_pathname_value',
            'filetype': 'some_filetype_value',
            'permissions': 'some_permissions_value',
            'owner': 'some_owner_value',
            'group_id': 'some_group_id_value',
            'PID': 'some_PID_value',
            'unit_file': 'some_unit_file_value',
            'unit_file_addr': 'some_unit_file_addr_value',
            'size': 'some_size_value',
            'mtime': 'some_mtime_value',
            'atime': 'some_atime_value'
        },
    ]
        'pathname': 'some_pathname_value',
        'filetype': 'some_filetype_value',
        'permissions': 'some_permissions_value',
        'owner': 'some_owner_value',
        'group_id': 'some_group_id_value',
        'PID': 'some_PID_value',
        'unit_file': 'some_unit_file_value',
        'unit_file_addr': 'some_unit_file_addr_value',
        'size': 'some_size_value',
        'mtime': 'some_mtime_value',
        'atime': 'some_atime_value'
    },
]
for ktest_case in kernel_tuple_test_cases:
    ktuple = Kerneltuple_(**ktest_case)
    print(ktuple)
from app.classd.classdef import Entity, Kerneltuple_
kernel_tuple_test_cases = [
    {
        'inode': 'some_inode_value',
        'pathname': 'some_pathname_value',
        'filetype': 'some_filetype_value',
        'permissions': 'some_permissions_value',
        'owner': 'some_owner_value',
        'group_id': 'some_group_id_value',
        'PID': 'some_PID_value',
        'unit_file': 'some_unit_file_value',
        'unit_file_addr': 'some_unit_file_addr_value',
        'size': 'some_size_value',
        'mtime': 'some_mtime_value',
        'atime': 'some_atime_value'
        'atime': 'some_atime_value'
    },
]
# These test cases are used to test the Kerneltuple_ class by creating instances of the class and printing their attributes.

for ktest_case in kernel_tuple_test_cases:
    ktuple = Kerneltuple_(**ktest_case)
    print(ktuple)
