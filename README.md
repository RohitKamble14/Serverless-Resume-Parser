# 🧠 Serverless Resume Parser using AWS Lambda, S3, and DynamoDB

A serverless resume parser built using AWS services. When a resume PDF is uploaded to S3, a Lambda function is triggered to extract key information such as **Name**, **Email**, and **Phone** using `PyMuPDF` and `regex`, and stores it in a DynamoDB table.

---

## 📐 Architecture Diagram

![Architecture](./screenshots/architecture.png)

---

## 🧰 Tech Stack

- **AWS Lambda** – For resume parsing logic
- **Amazon S3** – For storing uploaded PDF resumes
- **Amazon DynamoDB** – For storing parsed user data
- **PyMuPDF** – For PDF text extraction
- **Regex (re)** – For pattern-based data extraction
- **Boto3** – AWS SDK for Python

---
## How It Works

- **1.Resume is uploaded to S3 bucket (resume-parser-uploads-rohit).**
- **2.S3 triggers Lambda function on upload event.**
- **3.Lambda: Downloads the PDF.**
  `Uses PyMuPDF to extract name, email, and phone.
  `Saves data into DynamoDB (ResumeData table).
