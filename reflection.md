# Module 10 Reflection

## Overview
In this module, I built a secure FastAPI application with user authentication, 
password hashing, Pydantic validation, and a full CI/CD pipeline.

## Key Experiences

### 1. Secure Password Hashing
I learned that storing plain-text passwords is a critical security vulnerability.
Using bcrypt, every password is salted and hashed before being stored in the 
database. Even if the database is compromised, attackers cannot recover the 
original passwords.

### 2. Pydantic Validation
Pydantic schemas (UserCreate and UserRead) act as a security layer between the 
client and the database. UserCreate accepts raw passwords for processing, while 
UserRead deliberately excludes password_hash so it is never exposed in API 
responses. This separation of concerns prevents accidental data leakage.

### 3. Database Testing with GitHub Actions
Setting up a real PostgreSQL container inside GitHub Actions was challenging but 
rewarding. I learned that integration tests must use a real database to catch 
issues like duplicate username/email constraints that unit tests cannot detect.

### 4. CI/CD Pipeline
Configuring the CI/CD pipeline taught me how modern DevOps works. Every push to 
main automatically runs all tests, and only if they pass does it build and deploy 
the Docker image to Docker Hub. This ensures broken code is never deployed.

## Challenges

### GitHub Authentication
I encountered permission errors when pushing to GitHub because my local Git was 
using a different account. I learned to use Personal Access Tokens with the 
correct repo and workflow scopes to authenticate properly.

### Docker Hub Token
The initial CI/CD deployment failed because the Docker Hub token was not saved 
correctly in GitHub Secrets. After updating the secret with the correct token, 
the deployment succeeded.

## What I Learned
- Never store plain-text passwords; always use a hashing library like bcrypt
- Pydantic schemas are essential for input validation and output safety
- GitHub Actions can spin up real services like PostgreSQL for integration testing
- CI/CD pipelines enforce code quality by blocking deployments when tests fail
- Docker Hub serves as a registry for sharing and deploying container images

## Conclusion
This module gave me hands-on experience with security best practices and DevOps 
principles that are used in real-world production applications.
