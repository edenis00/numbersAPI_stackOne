# Numbers API

## Description

An Api that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Installation (Locally)

Step 1: Clone the git repository
    ```sh
        git clone "https://github.com/edenis00/numbersAPI_stackOne"
    ```

Step 2: Setup a virtual environment(recommended)
    ```sh
        python -m venv venv
        source venv/bin/activate
    ```

Step 3: Install dependencies
    ```sh
        pip install -r requirements.txt
    ```

## Usage

Step 1: Run command
    ```sh
        uvicorn app.main:app --reload
    ```

Step 2: Visit this url [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser

## Endpoints

### `GET /api/classify-number?number=<number>`

#### Success (200 OK)

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```
