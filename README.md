#  AI Quote Generator API

An API that serves fresh motivational quotes powered by AI (or placeholder logic). Deployable, testable, and built for scale.

##  Endpoints

- `GET /generate?theme=success`
- `GET /history`

##  Run via Docker

```bash
docker build -t ai-quotes .
docker run -p 8000:8000 --env-file .env ai-quotes
