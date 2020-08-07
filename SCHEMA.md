# Recipe Collector Schema

Version 1.0.0

---

| Recipe |          |             |           |
| ------ | -------- | ----------- | --------- |
| Field  | Type     | Required?   | Nullable? |
| id     | `int`    | ✔           | ❌       |
| name   | `string` | ✔           | ❌       |
| author
| image_url
| source_url
| ingredients | `Ingredient[]` |
| directions  | `string[]`     |
| prep_time   | `Prep_Time`    |
| cook_time


    Recipe
        name
        author
        source_url
        image_url
        prep_time
            quantity
            unit
        cook_time
            quantity
            unit
        yields
            quantity
            unit
        ingredients[]
            name
            quantity
            unit
            done-ness?
        instructions[]
        categories[]
        tags[]