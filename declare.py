#!/usr/bin/env python3

import os
import sys
import random
import logging
import getpass
import base64
import argparse
import time

import requests
from datetime import datetime
from datetime import timedelta


def get_date():
    return datetime.today().strftime("%d/%m/%Y")


def get_time_of_day():
    hr = int(datetime.today().strftime("%H"))
    return "P" if hr >= 12 else "A"


def get_rand_temp():
    return round(random.uniform(36.0, 36.6), 1)


def auth_and_get_cookie(user, password):
    VAFS_CLIENT_ID = "97F0D1CACA7D41DE87538F9362924CCB-184318"
    endpoint = "https://vafs.nus.edu.sg/adfs/oauth2/authorize"

    params = {
        "response_type": "code",
        "client_id": VAFS_CLIENT_ID,
        "resource": "sg_edu_nus_oauth",
        "redirect_uri": "https://myaces.nus.edu.sg:443/htd/htd"
    }

    data = {
        "UserName": "nusstu\\" + user,
        "PassWord": password,
        "AuthMethod": "FormsAuthentication"
    }

    logging.debug("Authenticating with VAFS")
    response = requests.post(endpoint, params=params, data=data)
    if response.status_code != 200 or "JSESSIONID" not in response.cookies:
        logging.error(
            "Unable to authenticate with VAFS. Are your NUSNET credentials correct?"
        )
        sys.exit(1)
    else:
        logging.debug("VAFS successfully authenticated")
        return response.cookies["JSESSIONID"]


def submit_temp(temp, date, time_of_day, sympt_flag, fam_sympt_flag, cookie):
    cookie = {"JSESSIONID": cookie}
    endpoint = "https://myaces.nus.edu.sg/htd/htd"
    data = {
        "actionName": "dlytemperature",
        "tempDeclOn": date,
        "declFrequency": time_of_day,
        # "temperature": temp,
        "symptomsFlag": sympt_flag,
        "familySymptomsFlag": fam_sympt_flag
    }

    logging.info(
        f"Submitting temperature {temp} degrees for {time_of_day}M on {date} (Symptoms: {sympt_flag}, Same household with symptoms: {fam_sympt_flag})"
    )
    response = requests.post(endpoint, cookies=cookie, data=data)

    if response.status_code != 200:
        logging.error("Failed to declare temperature. HTTP Error Code: " +
                      response.status_code)
        sys.exit(1)
    else:
        logging.info("Submitted successfully")


def get_credentials():
    logging.info(
        "NUSNET credentials not found. Creating a new credential file")
    print("\nWARNING: Your NUSNET credentials will be saved in plaintext.\n"
          "This has to be done so that the script can log you in.\n")

    password, verify = "", "_"
    while password != verify:
        print(
            "Please enter your NUSNET username (e0123456, without the nusstu\\): "
        )
        user = input()
        print(
            "Please enter your NUSNET password and press enter (you will not see what you've typed)"
        )
        password = getpass.getpass()
        print("Again")
        verify = getpass.getpass()
        if (password != verify):
            print("Passwords did not match!\n")

    with open("creds.txt", "wb+") as f:
        f.write(base64.b64encode(user.encode("ascii")) + b"\n")
        f.write(base64.b64encode(password.encode("ascii")))

    logging.info("Saved NUSNET credentials in creds.txt")
    return user, password


def read_credentials():
    if not os.path.exists("creds.txt"):
        return get_credentials()
    else:
        with open("creds.txt", "rb") as f:
            user = base64.b64decode(f.readline()).decode("ascii").strip()
            password = base64.b64decode(f.readline()).decode("ascii").strip()
        return user, password


def random_datetime(start_datetime, end_datetime, format_pattern):
    delta = (
        datetime.strptime(
            end_datetime,
            format_pattern) -
        datetime.strptime(
            start_datetime,
            format_pattern))
    # print(delta.seconds)
    inc = random.randrange(delta.seconds)
    rand_time = datetime.strptime(start_datetime,
                                  format_pattern) + timedelta(seconds=inc)
    return datetime.strftime(rand_time, format_pattern)
    # print(inc)


def main_func():
    parser = argparse.ArgumentParser(
        description="Submits NUS temperature declaration",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "temp",
        metavar="TEMP",
        type=float,
        help="temperature you would like to declare. leave blank for random",
        default=get_rand_temp(),
        nargs="?")
    parser.add_argument("-v",
                        "--verbose",
                        help="verbose - enable debug messages",
                        action="store_true")
    parser.add_argument(
        "-t",
        "--time",
        type=str,
        help="time of day - 'A' or 'P'. defaults to current time",
        default=get_time_of_day())
    parser.add_argument(
        "-s",
        "--sym",
        type=str,
        help="whether you have symptoms - 'Y' or 'N'. defaults to no",
        default="N")
    parser.add_argument(
        "-f",
        "--famsym",
        type=str,
        help="whether someone in the same household with symptoms - 'Y' or 'N'. defaults to no",
        default="N")
    args = parser.parse_args()
    logging.basicConfig(format="[%(levelname)s] %(asctime)s: %(message)s",
                        datefmt="%d/%m/%Y %I:%M:%S %p",
                        level=logging.DEBUG if args.verbose else logging.INFO,
                        handlers=[
                            logging.FileHandler("temp.log", "a"),
                            logging.StreamHandler()
                        ])

    # user, password = read_credentials()
    user = 'e0546117'
    password = 'hjyql19950905-'

    session_cookie = auth_and_get_cookie(user, password)
    submit_temp(temp=args.temp,
                date=get_date(),
                time_of_day=args.time,
                sympt_flag=args.sym,
                fam_sympt_flag=args.sym,
                cookie=session_cookie)


target_time_list_1 = ['10:20:22']
target_time_list_2 = ['14:10:09']
star_time_1 = '10:25:00'
end_time_1 = '10:58:00'
star_time_2 = '14:30:00'
end_time_2 = '15:30:00'
format_pattern = '%H:%M:%S'

# main_func()
while True:
    cur_time = datetime.now()
    cur_time = cur_time.strftime(format_pattern)

    if cur_time == '00:50:00':
        target_time_1 = random_datetime(
            star_time_1, end_time_1, format_pattern)
        target_time_2 = random_datetime(
            star_time_2, end_time_2, format_pattern)
        print("Generate random timing: ", target_time_1, target_time_2)
        target_time_list_1.append(target_time_1)
        target_time_list_2.append(target_time_2)

    if (cur_time == target_time_list_1[-1]
        ) or (cur_time == target_time_list_2[-1]):
        print('Start')
        main_func()
        print('*************Successful Submission!******************')

    time.sleep(1)
    print('sleeping   ', time.strftime("%H:%M:%S", time.localtime()),
          'Target Timing:', target_time_list_1[-1], target_time_list_2[-1])
