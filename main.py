import sys, os, argparse, json, logging, asyncio, datetime, requests, sqlite3, socketserver, subprocess, bs4, re, threading
import http.server
import socketserver
from classes import *

def main():
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