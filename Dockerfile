# Slim Python base image
FROM python:3.12-slim

# Show times in Sydney time
ENV TZ=Australia/Sydney

# Install time zone data, then remove the package lists to keep the image small
RUN apt-get update && apt-get install -y --no-install-recommends tzdata \
    && rm -rf /var/lib/apt/lists/*

# Working folder inside the container
WORKDIR /app

# Copy the project into the container
COPY . /app

# Make sure the entrypoint script can run
RUN chmod +x /app/.github/scripts/entrypoint.sh

# Run the entrypoint script when the container starts
ENTRYPOINT ["/app/.github/scripts/entrypoint.sh"]