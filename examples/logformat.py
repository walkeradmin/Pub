# -*- coding:utf-8 -*-
import logging
import logging.handlers
import os.path
# import time
# from colorama import Fore, Style
import sys


class Logger(object):
    def __init__(self, logger, filename):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        :param logger:  定义对应的程序模块名name，默认为root
        """
        # self.path = "C:\\Users\\Administrator\\IdeaProjects\\MyProject"
        self.path = os.getcwd()
        self.logger = logging.getLogger(name=logger)
        self.logger.setLevel(logging.DEBUG)                     # log level critical > error > warning > info > debug
        # os.chdir(self.path)
        if not os.path.exists(self.path + "\\formatLogs"):
            os.makedirs(self.path + "\\formatLogs")
        file = self.path + "/formatLogs/" + filename
        fh = logging.handlers.TimedRotatingFileHandler(filename=file, when='D', interval=1, backupCount=0,
                                                       encoding='utf-8')    # log segmentation
        fh.suffix = '%Y-%m-%d.log'
        fh.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(name)s - %(message)s"))
        if not self.logger.handlers:                            # if logger.handlers is null add，else write log
            ch = logging.StreamHandler(sys.stdout)              # creat handler，output console
            ch.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                "%(asctime)s - %(filename)s[line:%(lineno)d] - %(name)s - %(message)s")
            ch.setFormatter(formatter)                          # definition handler Output format
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    def debug(self, msg):
        """
        定义输出的颜色debug--white，info--green，warning/error/critical--red
        :param msg: 输出的log文字
        :return:
        """
        # self.logger.debug(Fore.WHITE + "DEBUG - " + str(msg) + Style.RESET_ALL)
        self.logger.debug("DEBUG - " + str(msg))

    def info(self, msg):
        # self.logger.info(Fore.BLUE + "INFO - " + str(msg) + Style.RESET_ALL)
        self.logger.info("INFO - " + str(msg))

    def warning(self, msg):
        # self.logger.warning(Fore.RED + "WARNING - " + str(msg) + Style.RESET_ALL)
        self.logger.warning("WARNING - " + str(msg))

    def error(self, msg):
        # self.logger.error(Fore.RED + "ERROR - " + str(msg) + Style.RESET_ALL)
        self.logger.error("ERROR - " + str(msg))

    def critical(self, msg):
        # self.logger.critical(Fore.RED + "CRITICAL - " + str(msg) + Style.RESET_ALL)
        self.logger.critical("CRITICAL - " + str(msg))


if __name__ == '__main__':
    log = Logger(logger='autoExcel')
    log.debug("debug")
    log.info("info")
    log.error("error")
    log.warning("warning")
    log.critical("critical")
