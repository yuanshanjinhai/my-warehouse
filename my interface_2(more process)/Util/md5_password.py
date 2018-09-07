# coding=utf-8
import hashlib
def md5ps(password):
    m5 = hashlib.md5()
    m5.update(password)
    pwd = m5.hexdigest()
    return pwd

if __name__ == '__main__':
    print md5ps("guolin123456")
