# Use specific version of nvidia cuda image
FROM megaease/base:cuda11.8.0-v0.0.1

# Remove any third-party apt sources to avoid issues with expiring keys.
RUN rm -f /etc/apt/sources.list.d/*.list

# Install Python dependencies (Worker Template)
COPY requirements.txt /requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install -r /requirements.txt --no-cache-dir && \
    rm /requirements.txt

# Copy and run script to fetch models
COPY . /usr/src/app

WORKDIR /usr/src/app

# Load models to image
RUN python src/build.py

CMD ["python", "-u", "src/main.py"]