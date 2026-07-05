# чат 

Kivy-приложение.

## Запуск

```powershell
kivy_venv\Scripts\python.exe main.py
```

## Сборка APK

Сборка через GitHub Actions:

1. Перейти в Actions → Build APK → Run workflow
2. Указать версию (например `v1.0.0`)
3. Готовый APK скачать из артефактов

Либо локально через buildozer (требуется Linux):
```bash
buildozer -v android debug
```
