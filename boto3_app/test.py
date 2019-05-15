import boto3
import botocore
import getopt
import sys

# print(sys.argv)
def usage():
	print(
"""
Usage:sys.args[0] [option]
-h or --help：显示帮助信息
-m or --module：模块名称   例如：ansible all -m shell -a 'date'
-a or --args：模块对于的参数  例如：ansible all -m shell -a 'date'
-v or --version：显示版本
"""
	)

def download(download_file):
	print(download_file)

def upload(upload_file):
	print(upload_file)


if len(sys.argv) == 1:
	usage()
	sys.exit()

try:
	opts, args = getopt.getopt(sys.argv[1:], "hu:d:v", ["help", "output="])   # sys.argv[1:] 过滤掉第一个参数(它是脚本名称，不是参数的一部分)
except getopt.GetoptError:
	print("argv error,please input")

for cmd, arg in opts:  
	if cmd in ("-h", "--help"):
		print("help info")
		sys.exit()
	elif cmd in ("-u", "--upload"):
		upload_file = arg
		download(upload_file)
	elif cmd in ("-d", "--download"):
		download_file = arg
		upload(download_file)
	elif cmd in ("-v", "--version"):
		print("%s version 1.0" % sys.argv[0])


# BUCKET_NAME = 'hoverbucket'    # replace with your bucket name
# KEY = 'my_image_in_s3.jpg'          # replace with your object key
 
# s3 = boto3.resource('s3')
 
# try:
#     s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')
# except botocore.exceptions.ClientError as e:
#     if e.response['Error']['Code'] == "404":
#         print("The object does not exist.")
#     else:
#         raise
