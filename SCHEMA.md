# Recipe Collector

## Schema Version 1.0.0

---

| User       |             |           |           |
| ---------- | ----------- | --------- | --------- |
| Field      | Type        | Required? | Nullable? |
| _id        | `Object ID` | ✔         | ❌       |
| username   | `String`    | ✔         | ❌       |
| email      | `String`    | ✔         | ❌       |
| password   | `String`    | ✔         | ❌       |
| role       | `String`    | ❌        | ✔        |
| created_at | `Date`      | ✔         | ❌       |
| updated_at | `Date`      | ✔         | ❌       |
| deleted_at | `Date`      | ❌        | ✔        |

<br/>

| Recipe       |             |           |           |             |
| ------------ | ----------- | --------- | --------- | ----------- |
| Field        | Type        | Required? | Nullable? | Foreign Key |
| _id          | `Object ID` | ✔         | ❌       | -           |
| name         | `String`    | ✔         | ❌       | -           |
| author       | `String`    | ✔         | ❌       | -           |
| source_url   | `String`    | ✔         | ❌       | -           |
| image_url    | `String`    | ✔         | ❌       | -           |
| prep_time    | `String`    | ✔         | ❌       | -           |
| cook_time    | `String`    | ✔         | ❌       | -           |
| yields       | `String`    | ✔         | ❌       | -           |
| ingredients  | `String[]`  | ✔         | ❌       | -           |
| notes        | `String[]`  | ✔         | ❌       | -           |
| instructions | `String[]`  | ✔         | ❌       | -           |
| categories   | `String[]`  | ✔         | ❌       | -           |
| tags         | `String[]`  | ✔         | ❌       | -           |
| created_by   | `Object ID` | ✔         | ❌       | User._id    |
| created_at   | `Date`      | ✔         | ❌       | -           |
| updated_at   | `Date`      | ✔         | ❌       | -           |
| deleted_at   | `Date`      | ❌        | ✔        | -           |

```python
# Future Schema Plans
#   prep_time = { quantity: Double, unit: String }
#   cook_time = { quantity: Double, unit: String }
#   yields    = { quantity: Double, unit: String }
#   ingredients = [
#     { name: String, quantity: Double, unit: String, instruction: String }
#   ]
```

## API Version 1.0.0

| `GET`                 | Response |
| --------------------- | -------- |
| `/api/v1/recipes`     | `[]`     |
| `/api/v1/recipes/:id` | `{}`     |

<br/>

| `POST`              | Response |
| ------------------- | -------- |

<br/>

| `PUT`               | Response |
| ------------------- | -------- |

<br/>

| `DELETE`            | Response |
| ------------------- | -------- |