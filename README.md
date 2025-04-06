# Privacy Toolkit X³ 🔒

<div id="header" align="center">
  <img src="https://i.giphy.com/KiXiO1iR3fFhC.webp" width="600"/>
</div>


## 🛡️ Что это?
**Privacy Toolkit X³** — это продвинутый набор инструментов для параноидального уровня защиты данных. Он включает:

❯ Фичи для **этичных хакеров**
❯ Инструменты **операционной безопасности (OPSEC)**
❯ Экстремальные режимы для **журналистов и активистов**
❯ Функции цифровой **"постановки под наблюдение"**



🌟 Основные возможности:

🔐 Основная защита

| **Функция**  | **Описание**   | **Команда**   |
| :---:        |     :---:      |     :---:     |
| Шифрование DNS	   | Авто-переключение на DoH/DoT     | `enable_encrypted_dns()`    |
| Очистка метаданных     | Удаление EXIF, PDF meta и др.       | `clean_metadata()`      |
| Генератор паролей     | Криптостойкие пароли + менеджер       | `generate_password()`      |


☠️ Режим паранойи

| Функция | Риск	 | Описание |
| :---:         |     :---:      |          :---: |
| USB-Killer	   | ⚡⚡⚡     | Физическая нейтрализаця USB-устройств|
| Dead Man Switch     | ⚡⚡⚡⚡       | Самоуничтожение данных при угрозе      |
| WiFi Deauth     | ⚡⚡       | Атака на роутеры (для тестирования)      |


💣 Хаос-режим (Только для тестов!)

```python
from chaos import NuclearOption

NuclearOption().activate(
    wifi_jamming=True,
    fake_bios=True,
    encrypt_attacker=True 
)
```

🛠 Установка:

Требования:

| Операционная система | Питон |
| --- | --- |
| Linux (Kali/Ubuntu/Debian) | 3.8+ |

```bash
# Установка зависимостей
sudo apt update
sudo apt install -y \
    python3-pip \
    tor \
    network-manager \
    net-tools \
    udisks2 \
    yubikey-manager
```

Установка из GitHub:

```bash
git clone https://github.com/your_username/privacy-toolkit-x.git
cd privacy-toolkit-x

# Установка Python-зависимостей
pip3 install -r requirements.txt

# Запуск
sudo python3 privacy_toolkit.py
```
