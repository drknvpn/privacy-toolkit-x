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

| **Обязательные зависимости** |
| --- |
| python3.8+, tor, network-manager, libusb-1.0 |

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

Установка из GitHub (рекомендуется):

```bash
git clone https://github.com/drknvpn/privacy-toolkit-x.git
cd privacy-toolkit-x

# Установка Python-зависимостей
pip3 install -r requirements.txt

# Запуск
sudo python3 privacy_toolkit.py
```

📑 Если нужны команды для установки зависимостей отдельно:

Все зависимости:
```bash
# Установка всех зависимостей
pip install -r requirements.txt
```

Только основные зависимости:
```bash
# Только основные (без опциональных)
pip install $(grep -v "^#" requirements.txt | grep -v "optional")
```

❗Вне зависимости от того, какой метод установки вы выбрали, две зависимости требуют отдельного внимания.

# yubikey-manager > требует ручной установки
# mat2 > установка через apt

📚 Документация:

[Документация в удобном «HTML» виде][docs]

[docs]: https://htmlpreview.github.io/?https://github.com/drknvpn/privacy-toolkit-x/blob/main/docs/manual.html


🌍 Сообщество:

[Баг-репорты][bugs]

[Обсуждения на ГитХаб][issuesgithub]

[Обсуждения в телеграмм][issuestelegramm]

[bugs]: https://github.com/drknvpn/privacy-toolkit-x/issues

[issuesgithub]: https://github.com/drknvpn/privacy-toolkit-x/issues

[issuestelegramm]: https://t.me/darkniiit

📜 Лицензия:

GNU GPLv3 — Используйте, модифицируйте, распространяйте свободно.




**Безопасность должна быть доступной, но помните:**

- Этот инструмент предназначен ТОЛЬКО для:
+ 1. Этичного хакинга
+ 2. Тестирования безопасности
+ 3. Академических исследований

! Любое незаконное использование ЗАПРЕЩЕНО !
Автор не несет ответственности за неправомерное использование.
