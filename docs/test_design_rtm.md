# Test Design & Requirements Traceability Matrix

Before any test was automated, each one was derived using a black-box
test design technique from the course syllabus rather than written
ad hoc. This document maps requirement -> test case -> the technique
used to derive it -> where it lives in the automated suite.

## Login

| Req ID | Requirement | Test Case ID | Design Technique | Test File |
|--------|-------------|---------------|-------------------|-----------|
| REQ-01 | Valid credentials log the user in | TC01 | Equivalence Partitioning (valid class) | tests/test_login.py |
| REQ-02 | Unknown username is rejected | TC02 | Equivalence Partitioning (invalid class) | tests/test_login.py |
| REQ-03 | Wrong password is rejected | TC03 | Equivalence Partitioning (invalid class) | tests/test_login.py |
| REQ-04 | Empty username/password is rejected | TC04 | Boundary Value Analysis (empty input) | tests/test_login.py |
| REQ-05 | Locked-out accounts cannot log in | TC05 | Equivalence Partitioning (negative class) | tests/test_login.py |

## Cart

| Req ID | Requirement | Test Case ID | Design Technique | Test File |
|--------|-------------|---------------|-------------------|-----------|
| REQ-06 | Adding an item updates the cart badge count | — | State-based functional test | tests/test_cart.py |
| REQ-07 | Adding multiple items keeps the count accurate | — | State-based functional test | tests/test_cart.py |
| REQ-08 | Cart page contents match what was added | — | Functional / state verification | tests/test_cart.py |

## Checkout

| Req ID | Requirement | Test Case ID | Design Technique | Test File |
|--------|-------------|---------------|-------------------|-----------|
| REQ-09 | Checkout proceeds when all fields are filled | TC06 | Decision Table (all conditions true) | tests/test_checkout.py |
| REQ-10 | Checkout blocked when first name is missing | TC07 | Decision Table | tests/test_checkout.py |
| REQ-11 | Checkout blocked when last name is missing | TC08 | Decision Table | tests/test_checkout.py |
| REQ-12 | Checkout blocked when postal code is missing | TC09 | Decision Table | tests/test_checkout.py |

## Decision table behind the checkout cases

| First Name | Last Name | Postal Code | Expected Result | Case |
|------------|-----------|-------------|------------------|------|
| Present | Present | Present | Proceeds to Overview | TC06 |
| Missing | Present | Present | Error shown | TC07 |
| Present | Missing | Present | Error shown | TC08 |
| Present | Present | Missing | Error shown | TC09 |

## Current coverage

9 of 9 designed test cases automated (100%). As new requirements are
added (e.g. sorting, logout, multi-item checkout), add a row here
first, then write the test — the matrix is the source of truth, not
the test file.
