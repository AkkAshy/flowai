### 1. *Admin panel*
- *marshrut:* `/admin/`,
- login: admin
- password: baton2904


### 2. *Autentifikaciya (JWT)*

#### a) JWT- token aliw
- *usıl:* `POST`
- *marshrut:* `/api/token/`
- *Soraw denesi:*
  ```json
  {
      "username": "test_user",
      "password": "secure_password"
  }
  ```
- *Kútilgen juwap:*
  ```json
  {
      "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQzOTI2NzAyLCJpYXQiOjE3NDM5MjQwODksImp0aSI6IjdiOWUxOGQ5ODRlODQ1NGM4ZTVmMTdhZWQ3MmMxYmQ4IiwidXNlcl9pZCI6NH0.woS8BWYoSUFTzJ9Btnad0wYwo2AxhUuqkpTxnFXhlCo",
      "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NDAxMDQ4OSwiaWF0IjoxNzQzOTI0MDg5LCJqdGkiOiIxMGY0NzgwZDZkMjI0ZTkzYTA2OTliMmUxMWM3YWJiOSIsInVzZXJfaWQiOjR9.umA7_z5fJ5bxIjhxRMcZbjw1-hW-Mz5qa3OqpFY-PCY"
  }
  ```

#### b) *JWT-token janartiw*
- *usıl:* `POST`
- *marshrut:* `/api/token/refresh/`
- *Soraw denesi:*
  ```json
  {
      "refresh": "your_refresh_token"
  }
  ```
- **Kútilgen juwap:**
  ```json
  {
      "access": "new_access_token"
  }
  ```

---

### 3. **User**

#### a) *Regestraciya*
- *usıl:* `POST`
- *marshrut:* `/api/users/register/`
- *Soraw denesi:*
  ```json
  {
  "username": "archmage2",
  "email": "archmage2@example.com",
  "password": "testpassword123",
  "password2": "testpassword123",
  "phone_number": "1234567890",
  "role": "teacher"
  }
  ```
- *Kútilgen juwap:*
  ```json
  {
      "message": "User registered successfully."
  }
  ```

#### b) *Avtorizaciya*
- *usıl:* `POST`
- *marshrut:* `/api/users/login/`
- *Soraw denesi:*
  ```json
  {
      "username": "new_user",
      "password": "secure_password"
  }
  ```
- *Kútilgen juwap:*
  ```json
  {
      "access": "your_access_token",
      "refresh": "your_refresh_token"
  }
  ```

#### c) *Profildi koriw*
- *usıl:* `GET`
- *marshrut:* `/api/users/profile/`
- *bas betler:*
  ```json
  Authorization: Bearer your_access_token
  ```
- *Kútilgen juwap:*
  ```json
  {
      "id": 1,
      "phone_number": "998901234567",
      "email": "new_user@example.com",
      "role": "student"
  }
  ```

### 4. *Kirislar*

#### a) *Kurslar spisogi*
- *usıl:* `GET`
- *marshrut:* `/api/courses/`
- *Kútilgen juwap:*
  ```json
  [
      {
          "id": 1,
          "title": "Python Basics",
          "description": "Learn the basics of Python programming.",
          "instructor": 1
      }
  ]
  ```

#### b) *Kwris jaratiw*
- *usıl:* `POST`
- *marshrut:* `/api/courses/`
- *bas betler:*
  ```json
  Authorization: Bearer your_access_token
  ```
- *Soraw denesi:*
  ```json
  {
      "title": "Python Basics",
      "description": "Learn the fundamentals of Python programming.",
      "start_date": "2023-10-01",
      "end_date": "2023-12-31",
      "instructor": 1
  }
  ```
- *Kútilgen juwap:*
  ```json
  {
      "id": 1,
      "title": "Python Basics",
      "description": "Learn the fundamentals of Python programming.",
      "start_date": "2023-10-01",
      "end_date": "2023-12-31",
      "instructor": 1,
      "created_at": "2023-09-25T12:34:56Z"
  } 
  ```

#### c) *Aniq bir wristi koriw*
- *usıl:* `GET`
- *marshrut:* `/api/courses/<id>/`
- *Kútilgen juwap:*
  ```json
  {
      "id": 1,
      "title": "Python Basics",
      "description": "Learn the basics of Python programming.",
      "instructor": 1
  }
  ```

---

### 5. *Sabaqtar*

#### a) *Sabaqtar spisogi*
- *usıl:* `GET`
- *marshrut:* `/api/lessons/`
- *Kútilgen juwap:*
  ```json
  [
      {
          "id": 1,
          "course": 1,
          "title": "Introduction to Python",
          "content": "This is the first lesson.",
          "order": 1
      }
  ]
  ```

#### b) **Sabaq jaratiw**
- *usıl:* `POST`
- *marshrut:* `/api/lessons/`
- *bas betler:*
  ```json
  Authorization: Bearer your_access_token
  ```
- *Soraw denesi:*
  ```json
  {
      "course": 1,
      "title": "Variables and Data Types",
      "content": "Learn about variables and data types in Python.",
      "order": 2
  }
  ```
- *Kútilgen juwap:*
  ```json
  {
      "id": 2,
      "course": 1,
      "title": "Variables and Data Types",
      "content": "Learn about variables and data types in Python.",
      "order": 2
  }
  ```

#### c) *Aniq BIR sabaqti koriw*
- *usıl:* `GET`
- *marshrut:* `/api/lessons/<id>/`
- *Kútilgen juwap:*
  ```json
  {
      "id": 1,
      "course": 1,
      "title": "Introduction to Python",
      "content": "This is the first lesson.",
      "order": 1
  }
  ```

---

### 6. *Тесты*

#### a) *Testter  spisogi*
- *usıl:* `GET`
- *marshrut:* `/api/lessons/tests/`
- *Kútilgen juwap:*
  ```json
  [
      {
          "id": 1,
          "lesson": 1,
          "title": "Python Basics Test",
          "test_type": "choice",
          "is_published": true
      }
  ]
  ```

#### b) *Test jaratiw*
- *usıl:* `POST`
- *marshrut:* `/api/lessons/tests/`
- *bas betler:*
  ```json
  Authorization: Bearer your_access_token
  ```
- *Soraw denesi:*
  ```json
  {
      "lesson": 1,
      "title": "Python Intermediate Test",
      "test_type": "text",
      "is_published": true
  }
  ```
- *Kútilgen juwap:*
  ```json
  {
      "id": 2,
      "lesson": 1,
      "title": "Python Intermediate Test",
      "test_type": "text",
      "is_published": true
  }
  ```

---

### 7. *Swraqtar*

#### a) *Siwraqtar spisogi*
- *usıl:* `GET`
- *marshrut:* `/api/lessons/questions/`
- *Kútilgen juwap:*
  ```json
  [
      {
          "id": 1,
          "test": 1,
          "text": "What is Python?",
          "options": ["A", "B", "C"],
          "correct_answer": "A"
      }
  ]
  ```

#### b) *Swraq jaratiw*
- *usıl:* `POST`
- *marshrut:* `/api/lessons/questions/`
- *bas betler:*
  ```json
  Authorization: Bearer your_access_token
  ```
- *Soraw denesi:*
  ```json
  {
      "test": 1,
      "text": "What is a variable?",
      "options": ["A", "B", "C"],
      "correct_answer": "B"
  }
  ```
- *Kútilgen juwap:*
  ```json
  {
      "id": 2,
      "test": 1,
      "text": "What is a variable?",
      "options": ["A", "B", "C"],
      "correct_answer": "B"
  }
  ```

---

### 8. *Jawaptardi jiberiw*
- *usıl:* `POST`
- *marshrut:* `/api/lessons/submit-test/<test_id>/`
- *bas betler:*
  ```json
  Authorization: Bearer your_access_token
  ```
- **Soraw denesi:**
  ```json
  {
      "answers": {
          "1": "A",
          "2": "B"
      }
  }
  ```
- *Kútilgen juwap:*
  ```json
  {
      "message": "Тест завершен!",
      "score": 80.0
  }
  ```
