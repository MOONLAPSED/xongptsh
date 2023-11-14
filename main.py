"""
This module contains the main function that initializes the logger and creates an instance of the Entity class. 
It also handles keyboard interrupts and system exits.
"""
import sys, os, argparse, json, logging, asyncio, datetime, requests, sqlite3, socketserver, subprocess, bs4, re, threading
import http.server
import socketserver
from classes import *

def main():
    """
    This is the main function that initializes the logger and creates an instance of the Entity class. 
    It does not take any parameters and does not return any value.
    """
    logger = logging.getLogger(__name__)
    p = Entity('letter', 'p')
    p.__str__()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
    try:
            sys.exit(0)
    except SystemExit:
        os._exit(0)