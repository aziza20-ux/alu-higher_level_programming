#!/bin/bash
#compliments
curl -sI $1 | grep Allow | cut -d ' ' -f2-
