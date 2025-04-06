#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import random
import logging
import uuid
import platform
import subprocess
import threading
import socket
import hashlib
import json
from datetime import datetime
from cryptography.fernet import Fernet
import psutil
import pyudev
import pyautogui
import scapy.all as scapy
import requests
from PIL import Image
import pyexiv2
import yaml
try:
    from yubikey_manager import YubiKey
except ImportError:
    pass

# ======================
# КОНФИГУРАЦИЯ ЛОГОВ
# ======================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/privacy_toolkit.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# ======================
# КЛАСС БЕЗОПАСНОСТИ
# ======================
class PrivacyTools:
    def __init__(self):
        self.config = self._load_config()
        self.encryption_key = self._generate_encryption_key()

    def _load_config(self):
        """Загружает конфигурацию из YAML-файла"""
        config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f) or {}
        except FileNotFoundError:
            logger.warning("Конфиг не найден, используется стандартный")
            return {
                'auto_clean': True,
                'killswitch': False,
                'paranoid_mode': False
            }

    def _generate_encryption_key(self):
        """Генерирует ключ шифрования на основе хеша системы"""
        system_info = f"{platform.node()}{platform.version()}"
        return hashlib.sha256(system_info.encode()).hexdigest()

    def clean_metadata(self, file_path):
        """Удаляет метаданные из файлов"""
        try:
            if file_path.endswith(('.jpg', '.jpeg', '.png')):
                img = Image.open(file_path)
                data = list(img.getdata())
                clean_img = Image.new(img.mode, img.size)
                clean_img.putdata(data)
                clean_img.save(file_path)
                logger.info(f"Очищены метаданные: {file_path}")
            
            elif file_path.endswith(('.pdf', '.docx', '.odt')):
                subprocess.run(['mat2', file_path], check=True)
                logger.info(f"Очищены метаданные: {file_path}")
                
        except Exception as e:
            logger.error(f"Ошибка очистки {file_path}: {e}")

# ======================
# КЛАСС СЕТЕВОЙ БЕЗОПАСНОСТИ
# ======================
class NetworkSecurity:
    def __init__(self):
        self.vpn_status = False
        self.tor_status = False
    
    def enable_killswitch(self):
        """Активирует блокировку интернета при отключении VPN"""
        try:
            subprocess.run(['iptables', '-A', 'OUTPUT', '-j', 'DROP'], check=True)
            subprocess.run(['iptables', '-I', 'OUTPUT', '-o', 'lo', '-j', 'ACCEPT'], check=True)
            logger.info("VPN Killswitch активирован")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Ошибка Killswitch: {e}")
            return False

    def change_mac(self, interface='eth0'):
        """Меняет MAC-адрес указанного интерфейса"""
        new_mac = ":".join(["{:02x}".format(random.randint(0, 255)) for _ in range(6)])
        try:
            subprocess.run(['ifconfig', interface, 'down'], check=True)
            subprocess.run(['ifconfig', interface, 'hw', 'ether', new_mac], check=True)
            subprocess.run(['ifconfig', interface, 'up'], check=True)
            logger.info(f"MAC изменен [{interface}]: {new_mac}")
            return new_mac
        except subprocess.CalledProcessError as e:
            logger.error(f"Ошибка смены MAC: {e}")
            return None

# ======================
# КЛАСС ЭКСТРЕМАЛЬНОЙ БЕЗОПАСНОСТИ
# ======================
class ParanoidMode:
    def __init__(self):
        self.usb_monitor = threading.Event()
    
    def usb_kill(self):
        """Мониторинг и уничтожение подозрительных USB-устройств"""
        context = pyudev.Context()
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by('usb')
        
        for device in iter(monitor.poll, None):
            if device.action == 'add':
                logger.warning(f"Обнаружено USB: {device}")
                try:
                    subprocess.run(['udisksctl', 'power-off', '-b', device.device_node])
                    logger.info(f"USB устройство отключено: {device.device_node}")
                except:
                    logger.error("Ошибка отключения USB")

    def dead_mans_switch(self, password):
        """Шифрует и удаляет данные при тревоге"""
        try:
            # Шифрование директорий
            for root, dirs, files in os.walk('/home'):
                for file in files:
                    path = os.path.join(root, file)
                    self._encrypt_file(path, password)
            
            # Очистка логов
            open('/var/log/privacy_toolkit.log', 'w').close()
            logger.info("Экстренное шифрование завершено!")
            
            # Отправка уведомления
            self._send_alert("Сработал Dead Man's Switch!")
            
        except Exception as e:
            logger.error(f"Ошибка активации Dead Man's Switch: {e}")

# ======================
# ЗАПУСК ПРОГРАММЫ
# ======================
if __name__ == "__main__":
    print("""    
██████╗░██████╗░██╗██╗░░░██╗░█████╗░░█████╗░██╗░░░██╗░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░██╗░░██╗██╗████████╗░░░░░░██╗░░██╗
██╔══██╗██╔══██╗██║██║░░░██║██╔══██╗██╔══██╗╚██╗░██╔╝░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██║░██╔╝██║╚══██╔══╝░░░░░░╚██╗██╔╝
██████╔╝██████╔╝██║╚██╗░██╔╝███████║██║░░╚═╝░╚████╔╝░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░█████═╝░██║░░░██║░░░█████╗░╚███╔╝░
██╔═══╝░██╔══██╗██║░╚████╔╝░██╔══██║██║░░██╗░░╚██╔╝░░╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░██╔═██╗░██║░░░██║░░░╚════╝░██╔██╗░
██║░░░░░██║░░██║██║░░╚██╔╝░░██║░░██║╚█████╔╝░░░██║░░░░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗██║░╚██╗██║░░░██║░░░░░░░░░██╔╝╚██╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░░░░░░░╚═╝░░╚═╝

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

██████╗░███████╗░██████╗████████╗  ██╗███╗░░██╗  ██████╗░███████╗░█████╗░░█████╗░███████╗
██╔══██╗██╔════╝██╔════╝╚══██╔══╝  ██║████╗░██║  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝
██████╔╝█████╗░░╚█████╗░░░░██║░░░  ██║██╔██╗██║  ██████╔╝█████╗░░███████║██║░░╚═╝█████╗░░
██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░  ██║██║╚████║  ██╔═══╝░██╔══╝░░██╔══██║██║░░██╗██╔══╝░░
██║░░██║███████╗██████╔╝░░░██║░░░  ██║██║░╚███║  ██║░░░░░███████╗██║░░██║╚█████╔╝███████╗
╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░  ╚═╝╚═╝░░╚══╝  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝

██████╗░░█████╗░░██████╗██╗░░██╗░█████╗░  ████████╗███████╗░█████╗░██╗░░██╗███╗░░██╗██╗░██████╗░██╗░░░██╗███████╗
██╔══██╗██╔══██╗██╔════╝██║░░██║██╔══██╗  ╚══██╔══╝██╔════╝██╔══██╗██║░░██║████╗░██║██║██╔═══██╗██║░░░██║██╔════╝
██████╔╝███████║╚█████╗░███████║███████║  ░░░██║░░░█████╗░░██║░░╚═╝███████║██╔██╗██║██║██║██╗██║██║░░░██║█████╗░░
██╔═══╝░██╔══██║░╚═══██╗██╔══██║██╔══██║  ░░░██║░░░██╔══╝░░██║░░██╗██╔══██║██║╚████║██║╚██████╔╝██║░░░██║██╔══╝░░
██║░░░░░██║░░██║██████╔╝██║░░██║██║░░██║  ░░░██║░░░███████╗╚█████╔╝██║░░██║██║░╚███║██║░╚═██╔═╝░╚██████╔╝███████╗
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░╚═════╝░╚══════╝   
    """)
    
    # Инициализация модулей
    tools = PrivacyTools()
    network = NetworkSecurity()
    paranoid = ParanoidMode()
    
    # Пример использования
    if tools.config.get('killswitch'):
        network.enable_killswitch()
    
    if tools.config.get('auto_clean'):
        tools.clean_metadata('/home/user/secret.docx')
    
    if tools.config.get('paranoid_mode'):
        usb_thread = threading.Thread(target=paranoid.usb_kill)
        usb_thread.daemon = True
        usb_thread.start()
