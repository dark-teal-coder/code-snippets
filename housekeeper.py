import os
import time
from configparser import ConfigParser, ExtendedInterpolation
import logging
import logging.handlers

# Ref.: http://www.blog.pythonlibrary.org/2013/11/14/python-101-how-to-write-a-cleanup-script/

def readConfig():
	try:
		config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'conf', 'config.ini')
	except:
		config_path = 'conf/config.ini'
	print(config_path)
	config = ConfigParser(interpolation=ExtendedInterpolation())
	config.optionxform = str
	config.read(config_path)
	return config

config = readConfig()
print(config.sections())

def buildlog(log_filename):
	# log_filename = log_path+'/hko.log'
	formatter = logging.Formatter('%(asctime)s <%(levelname)s>: %(process)d %(pathname)s/%(filename)s: %(funcName)s Line:%(lineno)d %(message)s')
	handler = logging.handlers.RotatingFileHandler(log_filename, maxBytes=1000*1000, backupCount=2)
	handler.setFormatter(formatter)

	logger = logging.getLogger()
	logger.setLevel(logging.ERROR)
	logger.addHandler(handler)
	return logger

logger=buildlog(config['common']['log_path']+'/housekeep.log')



def cleanup(number_of_days, path):
	"""
	Removes files from the passed in path that are older than or equal to the number_of_days
	"""
	time_in_secs = time.time() - (number_of_days * 24 * 60 * 60)

	for root, dirs, files in os.walk(path, topdown=False):
		for file in files:
			full_path = os.path.join(root, file)
			stat = os.stat(full_path)
			if stat.st_mtime <= time_in_secs:  # stat.st_mtime: time of last modification
				remove(full_path)

		if not os.listdir(root):
			remove(root)


def remove(path):
	"""
	Remove the file or directory
	"""
	if os.path.isdir(path):
		try:
			os.rmdir(path)
		except OSError:
			logger.fatal("Unable to remove the folder: {}".format(path), exc_info=True)
	else:
		try:
			if os.path.exists(path):
				os.remove(path)
		except OSError:
			logger.fatal("Unable to remove the file: {}".format(path), exc_info=True)

for topic in config.options('topics'):
	try:
		housekeep_day = float(config[topic]['housekeep_day'])
		housekeep_path = config[topic]['housekeep_path']
		# print(housekeep_day, housekeep_path, sep="\n")
		cleanup(housekeep_day, housekeep_path)
	except Exception as e:
		logger.fatal("Error in topic: {}".format(e), exc_info=True)
