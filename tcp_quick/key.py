from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import os

class Key:
    """
    密钥管理类

    用于生成RSA密钥对文件和AES密钥文件
    用于获取RSA公钥、RSA私钥和AES密钥
    """

    @staticmethod
    def create_rsa_key(public_key_path:str,private_key_path:str,bits:int=2048)->bool:
        """
        生成RSA密钥对文件
        :param public_key_path:公钥文件路径
        :param private_key_path:私钥文件路径
        :param bits:密钥长度
        """
        # 检查文件夹是否存在，不存在则创建
        if not os.path.exists(os.path.dirname(public_key_path)):
            os.makedirs(os.path.dirname(public_key_path))
        # 生成RSA密钥对
        key=RSA.generate(bits)
        public_key=key.publickey().export_key()
        private_key=key.export_key()
        # 保存RSA密钥对
        with open(public_key_path,"wb") as file:
            file.write(public_key)
        with open(private_key_path,"wb") as file:
            file.write(private_key)
        # 校验是否保存成功
        with open(public_key_path,"rb") as file:
            public_key=file.read()
        with open(private_key_path,"rb") as file:
            private_key=file.read()
        return public_key==key.publickey().export_key() and private_key==key.export_key()

    @staticmethod
    def create_aes_key(key_path:str,size:int=32)->bool:
        """
        生成AES密钥文件
        :param key_path:AES密钥文件路径
        :param size:密钥长度
        """
        # 检查文件夹是否存在，不存在则创建
        if not os.path.exists(os.path.dirname(key_path)):
            os.makedirs(os.path.dirname(key_path))
        # 生成AES密钥
        key=get_random_bytes(size)
        # 保存AES密钥
        with open(key_path,"wb") as file:
            file.write(key)
        # 校验是否保存成功
        with open(key_path,"rb") as file:
            return file.read()==key

    @staticmethod
    def get_rsa_public_key(public_key_path:str)->RSA.RsaKey:
        """
        获取RSA公钥
        :param public_key_path:公钥文件路径
        """
        # 检查文件是否存在
        if not os.path.exists(public_key_path):
            raise FileNotFoundError(f"公钥文件{public_key_path}不存在")
        with open(public_key_path,"rb") as file:
            key=RSA.import_key(file.read())
        return key

    @staticmethod
    def get_rsa_private_key(private_key_path:str)->RSA.RsaKey:
        """
        获取RSA私钥
        :param private_key_path:私钥文件路径
        """
        # 检查文件是否存在
        if not os.path.exists(private_key_path):
            raise FileNotFoundError(f"私钥文件{private_key_path}不存在")
        with open(private_key_path,"rb") as file:
            key=RSA.import_key(file.read())
        return key

    @staticmethod
    def get_aes_key(key_path:str)->bytes:
        """
        获取AES密钥
        :param key_path:AES密钥文件路径
        """
        # 检查文件是否存在
        if not os.path.exists(key_path):
            raise FileNotFoundError(f"AES密钥文件{key_path}不存在")
        with open(key_path,"rb") as file:
            key=file.read()
        return key
    
    @staticmethod
    def rand_iv(size:int=16)->bytes:
        """
        生成随机IV
        :param size:IV长度
        """
        return get_random_bytes(size)