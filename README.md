# Portfolio Site

A Django-based portfolio website with resume and project showcase sections, containerized with Docker.

## Features

- **Responsive Design**: Works on desktop and high-resolution displays (2K/4K)
- **Project Portfolio**: Showcase your projects with images, videos, and PDFs
- **Resume Section**: Display your experience, education, and skills
- **Contact Form**: Working email contact form with SMTP support
- **GitHub Integration**: Automatically fetches and displays your GitHub repositories
- **Docker Support**: Easy deployment with Docker and Docker Compose

## Setup

### Prerequisites

- Docker and Docker Compose
- Python 3.9+ (for local development)
- Node.js and npm (for local development)

### Environment Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and configure your settings:
   - `SECRET_KEY`: Generate a new Django secret key for production
   - Email settings for contact form functionality
   - `DEBUG`: Set to `False` in production
   - `ALLOWED_HOSTS`: Add your domain names

### Running with Docker

```bash
# Build and start the container
docker compose up --build

# Or run in detached mode
docker compose up --build -d
```

The site will be available at `http://localhost:8000`

### Local Development

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node dependencies
npm install

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver
```

## Email Configuration

The contact form supports SMTP email sending. Configure these environment variables in `.env`:

- `EMAIL_HOST`: Your SMTP server
- `EMAIL_PORT`: SMTP port (usually 465 for SSL)
- `EMAIL_HOST_USER`: Your email address
- `EMAIL_HOST_PASSWORD`: Your email password or app-specific password
- `EMAIL_SSL_VERIFY`: Set to `False` if using self-signed certificates

## Security Notes

- Never commit `.env` file to version control
- Generate a new `SECRET_KEY` for production
- Use environment-specific email credentials
- Set `DEBUG=False` in production
- Configure proper `ALLOWED_HOSTS` for your domain

## Recent Updates

- Fixed high-resolution display scrolling issue on portfolio tab
- Implemented working Django-based email contact form
- Added support for self-signed SSL certificates in email
- Dockerized deployment with proper static file handling
- Fixed PDF modal display with X-Frame-Options configuration
