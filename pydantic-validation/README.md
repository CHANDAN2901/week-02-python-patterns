# Week 02 – Pydantic v2 Validation

A hands-on learning project to understand **Pydantic v2** by building real-world data models and validating structured data. This project is part of my AI Engineering learning journey, focusing on the data validation layer used in modern Python applications such as FastAPI, AI agents, and LLM-powered systems.

---

## 📚 Learning Objectives

By completing this project, I learned how to:

* Build data models using `BaseModel`
* Validate user input with Pydantic
* Use `Field()` for constraints and metadata
* Work with `EmailStr`
* Handle optional fields
* Create nested models
* Use `UUID` and `Decimal`
* Validate dictionaries using `model_validate()`
* Serialize models using `model_dump()`
* Convert models into JSON using `model_dump_json()`
* Handle validation errors gracefully
* Design reusable API response models

---

## 🛠 Tech Stack

* Python 3.12
* uv
* Pydantic v2
* Ruff

---

## 📂 Project Structure

```text
pydantic-validation/
│
├── app/
│   ├── models/
│   │   ├── user_profile.py
│   │   ├── receipt.py
│   │   ├── invoice.py
│   │   ├── chat_message.py
│   │   └── api_response.py
│   │
│   └── main.py
│
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

---

## 🚀 Installation

Clone the repository

```bash
git clone <repository-url>
cd pydantic-validation
```

Create a virtual environment

```bash
uv venv
```

Activate it

**macOS/Linux**

```bash
source .venv/bin/activate
```

**Windows**

```powershell
.venv\Scripts\activate
```

Install dependencies

```bash
uv sync
```

---

## ▶️ Running the Project

```bash
uv run main.py
```

This will execute demonstrations for all implemented models.

---

# Models Implemented

## 1. UserProfile

Represents a user's profile.

### Concepts Learned

* BaseModel
* EmailStr
* Field validation
* Optional fields
* Required fields

### Example

```python
user = UserProfile(
    name="Chandan Yadav",
    email="chandan@gmail.com",
    age=24,
)
```

---

## 2. Receipt

Represents a shopping receipt containing multiple purchased items.

### Concepts Learned

* Nested Models
* List of Models
* Decimal
* datetime

Example hierarchy

```text
Receipt
│
├── Store Name
├── Purchase Date
├── Total
└── Items
    ├── Milk
    ├── Bread
    └── Rice
```

---

## 3. Invoice

Represents a business invoice.

### Concepts Learned

* UUID
* Decimal
* Enum
* default_factory
* datetime

Features

* Auto-generated invoice ID
* Auto-generated timestamp
* Invoice status management

---

## 4. ChatMessage

Represents a single AI conversation message.

### Concepts Learned

* Literal
* Token tracking
* AI conversation structure
* Timestamp generation

Supported roles

* system
* user
* assistant

---

## 5. APIResponse

A reusable API response wrapper.

Example structure

```json
{
  "success": true,
  "message": "User fetched successfully",
  "data": {},
  "errors": []
}
```

This pattern is commonly used in REST APIs and FastAPI applications.

---

# Pydantic Features Practiced

## Validation

```python
UserProfile.model_validate(data)
```

Validates a Python dictionary before creating a model instance.

---

## Serialization

Convert model into a Python dictionary

```python
model.model_dump()
```

Convert model into JSON

```python
model.model_dump_json(indent=4)
```

---

## Validation Errors

Invalid data raises a `ValidationError`.

Example

```python
try:
    UserProfile.model_validate(data)
except ValidationError as e:
    print(e)
```

---

# Sample Output

```text
USER PROFILE DEMO

{
    "success": true,
    "message": "User fetched successfully",
    "data": {
        ...
    }
}
```

---

# Key Concepts Learned

* BaseModel
* Field
* EmailStr
* Optional
* Literal
* Enum
* UUID
* Decimal
* datetime
* Nested Models
* model_validate()
* model_dump()
* model_dump_json()
* ValidationError
* default_factory

---

# Why Pydantic?

Pydantic provides automatic validation and serialization of Python objects using type hints. It is widely used in:

* FastAPI
* AI Agents
* LangChain
* LlamaIndex
* OpenAI Structured Outputs
* Anthropic Tool Use
* Backend APIs
* Microservices

Instead of manually validating incoming data, Pydantic ensures the data conforms to the expected schema before it reaches the application logic.

---

# Future Improvements

Planned topics to explore in the next iteration:

* Field Validators (`@field_validator`)
* Model Validators (`@model_validator`)
* Computed Fields
* Aliases
* ConfigDict
* Generic Models
* Discriminated Unions
* JSON Schema Generation
* FastAPI Integration
* Structured Outputs for LLMs

---

# What I Learned

This project strengthened my understanding of data validation in Python and demonstrated how Pydantic simplifies creating reliable, type-safe models. I learned how to build reusable schemas, validate nested data, serialize models into JSON, and design consistent API responses—all foundational skills for modern backend development and AI applications.
