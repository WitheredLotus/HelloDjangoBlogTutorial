# -*- coding = utf-8 -*-
# @Time : 2020/8/29 12:41
# @Author : EmperorHons
# @File : run_uvicorn.py
# @Software : PyCharm


import uvicorn
import os


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hellodjangoblogtutorial.settings")
    uvicorn.run(
        "hellodjangoblogtutorial.asgi:application",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )


if __name__ == "__main__":
    main()