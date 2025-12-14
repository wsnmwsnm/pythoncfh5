[app]
title = 极速换肤2.0  # APP名称
package.name = gameskinmod  # 包名（小写无空格）
package.domain = org.yourname  # 自定义域名（如org.user）
source.dir = .  # 源码目录（固定）
source.include_exts = py,png,jpg,kv,atlas  # 包含文件类型
source.include_dirs = assets  # 必须包含assets目录（内置文件用）
requirements = python3,kivy==2.3.0,plyer==2.1.0,python-dateutil==2.8.2,pillow==10.2.0
android.sdk = 24  # 最低安卓版本
android.ndk = 25b  # 适配Kivy的NDK版本
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE  # 读写SD卡权限（关键）
android.release = False  # 测试用debug模式
android.icon = icon.png  # 可选：放入图标文件（尺寸512x512）

[buildozer]
log_level = 2
warn_on_root = 1