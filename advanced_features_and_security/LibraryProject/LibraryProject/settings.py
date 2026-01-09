# -----------------------------------
# HTTPS & SECURITY SETTINGS
# -----------------------------------

# إعادة توجيه HTTP إلى HTTPS
SECURE_SSL_REDIRECT = True

# HSTS
SECURE_HSTS_SECONDS = 31536000  # سنة واحدة
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# ملفات تعريف الارتباط الآمنة
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# رؤوس أمان إضافية
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_REFERRER_POLICY = 'no-referrer-when-downgrade'

# ----------------------------
# إعداد رأس البروكسي عند استخدام HTTPS خلف بروكسي
# ----------------------------
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
