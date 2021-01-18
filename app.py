from flask import Flask, redirect, render_template, request, session, abort, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'