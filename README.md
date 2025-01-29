# Energética OpenAPI

Energética OpenAPI is a FastAPI-based REST API designed to serve various services for Energética Coop. It provides endpoints for querying anonymized aggregated information about cooperative members, contracts and local energy communities. It also provides some endpoints that compute document models for internal consumption. The API is structured to grow alongside the cooperative's needs.

## 🚀 Motivation

Energética Coop required a centralized API to streamline data access and service integration. Instead of maintaining multiple separate services, this API consolidates functionalities into a single, scalable system, making it easier to maintain and extend.

## 🛠 Quick Start

### 1. Install Docker

To run the API, you need Docker installed. You can download and install **Docker Desktop** from the official site:

- [Docker Engine for Linux](https://docs.docker.com/engine/install/)

### 2. Clone the repository

```sh
git clone https://github.com/energeticacoop/energetica-openapi.git
cd energetica-openapi
```

### 3. Run the API using Docker

Ensure Docker is installed, then start the container:

```sh
docker build -t energetica-api .
docker run -p 80:80 energetica-api
```

### 4. Check if the API is running

Use `curl` to test the health endpoint:

```sh
curl -X GET http://localhost/health
```

Expected response:

```json
{ "status": "ok" }
```

### 5. Authentication

Some endpoints require authentication via a Bearer token. Obtain a token by sending a POST request with your credentials:

```sh
curl -X POST "http://localhost/auth/token" \
     -H "Content-Type: application/json" \
     -d '{"username": "your_user", "password": "your_password"}'
```

Example response:

```json
{ "access_token": "your_token_here", "token_type": "bearer" }
```

Use this token in the `Authorization` header for protected endpoints:

```sh
curl -X GET "http://localhost/protected-endpoint" \
     -H "Authorization: Bearer your_token_here"
```

### 6. OpenAPI Documentation

FastAPI automatically generates interactive API documentation. Access it at:

- OpenAPI UI: [http://localhost/docs](http://localhost/docs)
- OpenAPI JSON: [http://localhost/openapi.json](http://localhost/openapi.json)

## 🤝 Contributing

We welcome contributions! To contribute:

1. **Fork the repository:**

   ```sh
   git clone https://github.com/energeticacoop/energetica-openapi.git
   cd energetica-openapi
   ```

2. **Create a new branch:**

   ```sh
   git checkout -b feature-name
   ```

3. **Make your changes and commit:**

   ```sh
   git commit -m 'Add new feature'
   ```

4. **Push to your branch:**

   ```sh
   git push origin feature-name
   ```

5. **Open a Pull Request:**
   Go to the repository on GitHub and open a Pull Request for your branch.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
