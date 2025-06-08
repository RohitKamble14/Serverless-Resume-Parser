# 🧠 Serverless Resume Parser using AWS Lambda, S3, and DynamoDB

A serverless resume parser built using AWS services. When a resume PDF is uploaded to S3, a Lambda function is triggered to extract key information such as **Name**, **Email**, and **Phone** using `PyMuPDF` and `regex`, and stores it in a DynamoDB table.

---

## 📐 Architecture Diagram

![Architecture]![Serverless Resume Parser drawio (1)](https://github.com/user-attachments/assets/6a1c5133-c5e0-459e-9904-e66d0fe72a82)


---

## 🧰 Tech Stack

- **AWS Lambda** – For resume parsing logic
- **Amazon S3** – For storing uploaded PDF resumes
- **Amazon DynamoDB** – For storing parsed user data
- **PyMuPDF** – For PDF text extraction
- **Regex (re)** – For pattern-based data extraction
- **Boto3** – AWS SDK for Python

---

## 🚀 How It Works

1. A PDF resume is uploaded to an **S3 bucket**.
2. The upload triggers a **Lambda function**.
3. Lambda:
   - Downloads the PDF.
   - Extracts candidate info using `PyMuPDF`.
   - Stores the data in a **DynamoDB** table.
4. Logs are visible in **CloudWatch**.

---


   
