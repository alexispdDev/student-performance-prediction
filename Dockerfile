# Start from a lightweight official Python 3.13 image based on Debian Bookworm
FROM python:3.13.9-slim-bookworm

# Copy the `uv` and `uvx` binaries from the official Astral UV image into /bin/
# This gives access to the fast dependency manager (like pip, but faster and modern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory inside the container
# All subsequent commands will run inside /app
WORKDIR /app

# Add the local virtual environment’s `bin` folder to PATH
# so installed tools and packages can be executed directly
ENV PATH="/app/.venv/bin:$PATH"

# Copy Python project metadata and lock files into the image
# - pyproject.toml: defines project dependencies and build system
# - uv.lock: pinned dependency versions for reproducible installs
# - .python-version: specifies the Python version used locally (for consistency)
COPY "pyproject.toml" "uv.lock" ".python-version" ./

# Install dependencies using `uv`, respecting locked versions for consistency
RUN uv sync --no-dev --locked

# Copy your application code and model file into the container
COPY "src/student_performance_prediction/predict.py" "src/student_performance_prediction/model.bin" ./

# Expose port 8000 so it can be accessed outside the container
EXPOSE 8000

# Define the command that runs when the container starts
# Here, it runs your Python script `predict.py`
ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]
