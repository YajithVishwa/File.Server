# Fileserver API

This internal backend API project is designed to handle file operations through API calls. It is intended for internal use and will be hosted within a secure network environment.

## Features
- File upload, retrieval, and management through RESTful API calls.
- Built with Docker for easy deployment and portability.

## Getting Started

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed on your machine.

### Environment Variables
The application requires an environment variable `UPLOAD_FILE` to specify the directory for file storage. During container creation, ensure that you set it according to your desired folder path.

### API Documentation
For detailed API usage and endpoints, refer to [API Documentation](https://documenter.getpostman.com/view/33179464/2sAY4sk4uD)

## Installation

1. Clone the repository:
   git clone https://github.com/YajithVishwa/File.Server.git
   cd File.Server
2. Build Dockerfile
   docker build -t fileserver-api .
3. Run Docker Container
  docker run -d -p <your-port>:5000 -e UPLOAD_FILE=<path-to-your-folder> fileserver-api
