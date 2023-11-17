import sys, os, logging, requests, sqlite3, subprocess, re, threading, argparse, asyncio, datetime, http.server, json, socketserver, traceback
from app.classd.classdef import Entity, Kerneltuple_

entity_test_cases = [
    {
        "name": "Entity 1",
        "description": "Description 1"
    },
    {
        "name": "Entity 2",
        import sys, os, logging, requests, sqlite3, subprocess, re, threading, argparse, asyncio, datetime, http.server, json, socketserver, traceback
        from app.classd.classdef import Entity, Kerneltuple_
        
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
        
        for ktest_case in kernel_tuple_test_cases:
            ktuple = Kerneltuple_(**ktest_case)
            print(ktuple)
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

for ktest_case in kernel_tuple_test_cases:
    ktuple = Kerneltuple_(**ktest_case)
    print(ktuple)
BACKOFF_FACTOR = 1
BACKOFF_FACTOR = 1
BACKOFF_FACTOR = 1
