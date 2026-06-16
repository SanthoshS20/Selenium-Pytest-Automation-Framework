FROM python:3.11-slim

LABEL maintainer="qa-team"
LABEL description="Selenium pytest automation framework"

RUN apt-get update && apt-get install -y --no-install-recommends \
        curl \
        unzip \
        ca-certificates \
        git \
        # ChromeDriver shared-library dependencies
        libglib2.0-0 \
        libnss3 \
        libnspr4 \
        libdbus-1-3 \
        libatk1.0-0 \
        libatk-bridge2.0-0 \
        libcups2 \
        libdrm2 \
        libxkbcommon0 \
        libxcomposite1 \
        libxdamage1 \
        libxfixes3 \
        libxrandr2 \
        libgbm1 \
    && rm -rf /var/lib/apt/lists/* \
    \
    && CHROMEDRIVER_VERSION=$(curl -fsSL \
        "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions.json" \
        | python3 -c \
        "import sys, json; print(json.load(sys.stdin)['channels']['Stable']['version'])") \
    && echo ">>> Installing ChromeDriver ${CHROMEDRIVER_VERSION}" \
    \
    && curl -fsSL \
        "https://storage.googleapis.com/chrome-for-testing-public/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip" \
        -o /tmp/chromedriver.zip \
    && unzip -q /tmp/chromedriver.zip -d /tmp/ \
    && mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver \
    && rm -rf /tmp/chromedriver.zip /tmp/chromedriver-linux64 \
    \
    && chromedriver --version

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


# ── Default entrypoint: run all tests ───────────────────────
ENTRYPOINT ["pytest"]
CMD ["-v", "--env=qa", "--alluredir=reports/allure-reports", "tests/"]